import torch
import torchvision
from torchvision.io import read_image
import torchvision.transforms as T
import time
# from turbojpeg import TurboJPEG, TJPF_GRAY, TJSAMP_GRAY, TJFLAG_PROGRESSIVE, TJFLAG_FASTUPSAMPLE, TJFLAG_FASTDCT


from PIL import Image
class Processor:

    @classmethod
    def process_image(cls, path):

        img = read_image(path)
        # top left height width
        img = T.functional.crop(img, 400, 450, 250, 700)
        img = T.ToPILImage()(img)
        img.show()


if __name__ == "__main__":
    start = time.time()
    Processor.process_image("Images/captured_1.png")
    print(f"Took {time.time() - start} seconds to process image")