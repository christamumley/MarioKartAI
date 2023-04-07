import torch
from torch import Tensor
import torch.nn as nn
import torchvision
import pytorch_lightning as pl
import matplotlib.pyplot as plt
import numpy as np
from torch.utils.data import Dataset, DataLoader
import os
import time
from torchmetrics.classification.accuracy import BinaryAccuracy

import os
import pandas as pd

from torchvision.io import read_image, ImageReadMode
import torchvision.transforms as T
import pickle

from selenium.webdriver.common.keys import Keys


class MarioSegmentation(pl.LightningModule):
    def __init__(self):
        super().__init__()
        self.acc_metric = BinaryAccuracy()
        self.criterion = nn.BCELoss()

        self.first_downsample = nn.Sequential(
            nn.Conv2d(in_channels=3, out_channels=32, kernel_size=3, stride=2, padding=1),
            nn.BatchNorm2d(32),
            nn.ReLU(True),
        )

        self.second_downsample = nn.Sequential(
            nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, stride=2, padding=1),
            nn.BatchNorm2d(64),
            nn.ReLU(True)
        )

        self.third_downsample = nn.Sequential(
            nn.Conv2d(in_channels=64, out_channels=128, kernel_size=3, stride=2, padding=1),
            nn.BatchNorm2d(128),
            nn.ReLU(True),
        )

        self.first_upsample = nn.Sequential(
            nn.ConvTranspose2d(in_channels=128, out_channels=64, kernel_size=3, stride=2, padding=1, output_padding=1),
            nn.BatchNorm2d(64),
            nn.ReLU(True),
        )

        self.second_upsample = nn.Sequential(
            nn.ConvTranspose2d(in_channels=64, out_channels=32, kernel_size=3, stride=2, padding=1, output_padding=1),
            nn.BatchNorm2d(32),
            nn.ReLU(True),
        )

        self.third_upsample = nn.Sequential(
            nn.ConvTranspose2d(in_channels=32, out_channels=16, kernel_size=3, stride=2, padding=1, output_padding=1),
            nn.BatchNorm2d(16),
            nn.ReLU(True),
        )
        self.final_layer = nn.Sequential(
            nn.Conv2d(in_channels=16, out_channels=1, kernel_size=1),
        )

    def configure_optimizers(self):
        optimizer = torch.optim.Adam(self.parameters(), lr=1e-3)
        return optimizer

    def training_step(self, batch, batch_idx):
        x, y = batch
        y[y == 255] = 0
        y[y > 0] = 1
        y_pred = self.forward(x)
        loss = self.criterion(y_pred, y.float())
        self.log("train_loss", loss)
        acc = self.acc_metric(y_pred, y)
        self.log("train_acc", acc, prog_bar=True)
        return loss

    def validation_step(self, batch, batch_idx):
        x, y = batch
        y[y == 255] = 0
        y[y > 0] = 1
        y_pred = self.forward(x)
        loss = self.criterion(y_pred, y.float())
        self.log("train_loss", loss)
        acc = self.acc_metric(y_pred, y)
        self.log("train_acc", acc, prog_bar=True)
        return loss

    def forward(self, x):
        first_downsample = self.first_downsample(x)
        second_downsample = self.second_downsample(first_downsample)
        third_downsample = self.third_downsample(second_downsample)
        first_upsample = self.first_upsample(third_downsample)
        merge = first_upsample + second_downsample
        second_upsample = self.second_upsample(merge)
        merge = second_upsample + first_downsample
        third_upsample = self.third_upsample(merge)
        result = self.final_layer(third_upsample)

        return nn.Sigmoid()(result)


class Decider:
    TRAINED_PATH = "segmentation_model_weights"
    def __init__(self):
        self.model = MarioSegmentation()
        self.model.load_state_dict(torch.load(self.TRAINED_PATH))

        self.resize_obj = T.Resize((1200,1200), antialias=True)


    def process_img(self, img_path):
        img = read_image(f"{img_path}", ImageReadMode.RGB)

        size = T.functional.get_image_size(img)
        width, height = size

        img = T.functional.crop(img, int(height / 10), int(width / 5), int(height / 3), int(width / 4))

        # Resizes to 640,640
        img = self.resize_obj.forward(img)

        img = img.float()
        img = img.unsqueeze(0)

        return img
    def direction_to_move(self, img_path):
        """
        Provided a file path to an image, return the key we should press
        :param img_path: The image path we are processing
        :return: The key we should be pressing
        """
        img = self.process_img(img_path)

        preds = self.model.forward(img).squeeze(0)
        preds = preds > .5
        preds = preds.float()

        top_half = torch.hsplit(preds, 2)[0]

        thirds = torch.tensor_split(top_half, 3, dim=2)
        # thirds = (thirds[0] * 1.2, thirds[1], thirds[2] * 1.2)

        # Divided area into three sections, where each section corresponds to a location we can move to
        directions = {(Keys.LEFT, 'left'): thirds[0], (Keys.UP, 'straight'): thirds[1], (Keys.RIGHT, 'right'): thirds[2]}

        optimal_direct = None
        optimal_score = None

        totalSum = 0

        for key in directions:
            key_score = torch.sum(directions[key])
            totalSum += key_score
            if optimal_direct is None or optimal_score < key_score:
                optimal_direct = key
                optimal_score = key_score
        return optimal_direct


if __name__ == "__main__":
    move = Decider().direction_to_move("Images/captured2_6.png")
    print(f"We should turn {move}")