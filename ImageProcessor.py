import torch
import torchvision
from torchvision.io import read_image, write_png, ImageReadMode
import torchvision.transforms as T
import time
import os

import labelbox as lb
import labelbox.types as lb_types
from PIL import Image
import numpy as np

import json
class Processor:

    @classmethod
    def process_image(cls, path):

        img = read_image(path, ImageReadMode.RGB)

        # top left height width
        size = T.functional.get_image_size(img)
        width, height = size

        img = T.functional.crop(img, int(height/10), int(width/5), int(height/3), int(width/4))
        # img = T.ToPILImage()(img)
        #
        # img.show()
        write_png(img, path)
        # torchvision.utils.save_image(img, path)

    @classmethod
    def rescale(cls):
        for file in os.listdir("Images/"):
            cls.process_image(f"Images/{file}")
            print(file)

    @classmethod
    def process_json_data(cls, fp):


        # API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiJjbGZybDJ0ZXExYWR1MDcydDkyeDkxeDBjIiwib3JnYW5pemF0aW9uSWQiOiJjbGZybDJ0ZWYxYWR0MDcydDZsMjVkNHowIiwiYXBpS2V5SWQiOiJjbGZyb2x2bXgwYnVqMDc0OTkwcTI2cHp0Iiwic2VjcmV0IjoiMGY5N2RjNTlmZjdjOTQyYWM3NjZiNTljYzA4Njk0OGMiLCJpYXQiOjE2Nzk5NzMwOTksImV4cCI6MjMxMTEyNTA5OX0.hFH1cVZVeujMuAhRSW4XpR4kFFL_RZ_8UvqSRGH_FBo"
        # client = lb.Client(api_key=API_KEY)
        # project = client.get_project("clfrmpagh1erf070r20nffelm")
        #
        # labels = project.label_generator()
        #
        # labels = list(labels)
        # print(labels)
        #
        # hex_to_rgb = lambda hex_color: tuple(
        #     int(hex_color[i + 1:i + 3], 16) for i in (0, 2, 4))
        # colors = {
        #     tool.name: hex_to_rgb(tool.color)
        #     for tool in lb.OntologyBuilder.from_project(project).tools
        # }
        #
        # for label in labels:
        #     print(label)
        #     exit(0)
        #
        # # Grab the first label and corresponding image
        # label = labels[0]
        # image_np = label.data.value
        #
        # # Draw the annotations onto the source image
        # for annotation in label.annotations:
        #     if isinstance(annotation.value, lb_types.Geometry):
        #         image_np = annotation.value.draw(canvas=image_np,
        #                                          color=colors[annotation.name],
        #                                          thickness=5)
        # Image.fromarray(image_np.astype(np.uint8)).show()

if __name__ == "__main__":
    start = time.time()
    # Processor.process_image("Images/captured_1.png")
    Processor.rescale()
    # Processor.process_json_data("example_input.json")
    print(f"Took {time.time() - start} seconds to process image")