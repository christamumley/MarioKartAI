import torch
import torchvision
from torchvision.io import read_image, write_png, ImageReadMode
import torchvision.transforms as T
import time
import os

class Processor:

    @classmethod
    def process_image(cls, path):

        img = read_image(path, ImageReadMode.RGB)
        # top left height width
        size = T.functional.get_image_size(img)
        width, height = size

        img = T.functional.crop(img, int(height/10), int(width/10), int(height/3), int(width/2.1))

        # img = torchvision.transforms.ToPILImage()(img)
        # img.show()
        # exit(0)
        write_png(img, path)

    @classmethod
    def rescale(cls, dir = "ReinforcementImages/"):
        for file in os.listdir(dir):
            print(file)
            cls.process_image(f"{dir}{file}")


if __name__ == "__main__":
    start = time.time()
    # Processor.process_image("Images/captured_1.png")
    # Processor.process_image("ReinforcementImages/reinforce2-15_up_left_.png")
    Processor.rescale(dir="Images/")
    # Processor.process_json_data("example_input.json")
    print(f"Took {time.time() - start} seconds to process image")