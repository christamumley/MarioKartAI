import torch
from torch import Tensor
import torch.nn as nn
import torchvision
import pytorch_lightning as pl
import matplotlib.pyplot as plt
import numpy as np

from SegmentationAI import Decider
from selenium.webdriver.common.keys import Keys

class ImitationNN(pl.LightningModule):

    def __init__(self):
        super().__init__()

        self.layers = nn.Sequential(
            nn.Linear(in_features=128 * 128, out_features=64 * 64),
            nn.Linear(in_features=64 * 64, out_features=32 * 32),
            nn.Linear(in_features=32 * 32, out_features=6)
        )

        self.loss = nn.CrossEntropyLoss()

    def configure_optimizers(self):
        optimizer = torch.optim.SGD(self.parameters(), lr=0.01)
        return optimizer

    def training_step(self, batch, batch_idx):
        feats, target = batch

        pred = self.forward(feats)

        pred_idx = highest_idx(pred)

        labels = torch.Tensor(np.zeros(len(pred)))
        labels[target] = 1

        loss = self.loss(pred, labels)

        return loss

    def validation_step(self, batch, batch_idx):
        feats, target = batch
        pred = self.forward(feats)

        pred_idx = highest_idx(pred)

        labels = torch.Tensor(np.zeros(len(pred)))
        labels[target] = 1

        loss = self.loss(pred, labels)

        return loss

    def forward(self, x):
        flatten = torch.flatten(x)
        return self.layers(flatten)


class ImitationDriver:
    state_dict = "imitation_model_weights"
    def __init__(self):
        self.model = ImitationNN()
        self.model.load_state_dict(torch.load(self.state_dict))


        self.processor = Decider()

    def make_prediction(self, img_path):
        img = self.processor.process_img(img_path)

        img = self.processor.image_map(img)

        preds = self.model(img)

        pred_idx = self.highest_idx(preds)

        # ALWAYS MAKE SURE THESE ARE THE SAME THAN THOSE GENERATED IN THE NOTEBOOK!!!!!
        # maps = {0: 'up', 1: 'up left', 2: 'up right', 3: ''}
        maps = {0: (Keys.UP, 'up'),
                1: (Keys.LEFT, 'up left'),
                2: (Keys.RIGHT, 'right'),
                3: (Keys.RIGHT, 'up right'),
                4: (Keys.LEFT, 'left'),
                5: (Keys.SPACE,'')
                }
        #{0: 'up', 1: 'up left', 2: 'right', 3: 'up right', 4: 'left', 5: ''}

        direct = maps[pred_idx]

        return direct

    @classmethod
    def highest_idx(cls, vals):
        m = None
        out_idx = None

        for idx, val in enumerate(vals):
            if m is None or val > m:
                m = val
                out_idx = idx
        return out_idx


if __name__ == "__main__":
    i = ImitationDriver()
    i.make_prediction("Images/current_state.png")
