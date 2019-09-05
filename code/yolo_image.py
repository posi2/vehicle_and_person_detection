import sys
import argparse
from yolo import YOLO
from PIL import Image
import glob
def detect_img(yolo):
        
    imdir = './input/image/'
    ext = ['png','jpg','jpeg']

    files = []
    [files.extend(glob.glob(imdir + '*.' + e)) for e in ext]

    for img_path in files:
        image = Image.open(img_path)
        img_path = img_path.split("/")
        flag = True
        r_image = yolo.detect_image(image, flag, img_path[3])
        r_image.show()
      
    yolo.close_session()

FLAGS = None

if __name__ == '__main__':
    # class YOLO defines the default value, so suppress any default here
    parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
    FLAGS = parser.parse_args()
    """
    Image detection mode, disregard any remaining command line arguments
    """
    print("Image detection mode")
    detect_img(YOLO(**vars(FLAGS)))
    