import argparse
import sys
from os import *
import cv2
import numpy as np

from Transform import getClues, getBackgroundColor, drawClues, drawGrid
from Process import make_pixel, newColors


def main(fileName, maxDim=80, toBW = False, numColors = "", getResult = True):

    print("Processing "+fileName+"...")
    try:
        processed = cv2.imread(fileName)
    except:
        print(fileName + "is not a right image or path")
        sys.exit()
    processed = make_pixel(processed, maxDim, toBW)
    processed = newColors(processed, n = numColors)
    if getResult:
        cv2.imwrite("_Pic"+fileName,processed)
    print("Making nonogram...")
    backgroundCl = getBackgroundColor(processed)
    clues = getClues(processed, backgroundCl)
    h, w = processed.shape[:2]
    result = drawGrid(clues, (w, h), backgroundCl)
    result = drawClues(np.float32(result), clues, (w, h))
    cv2.imwrite("_Pix"+fileName, result)
    print("Finish!")

parser = argparse.ArgumentParser(description = "Make a nonogram from a picture.")
parser.add_argument("image",nargs=1,help="path to image to be processed")
parser.add_argument("-d","--maxDim",default=[80],nargs=1,type=int,help="maximum nombuer of squares in nonogram (default = 80)")
parser.add_argument("-b","--blackAndWhite",action="count",help="image should be converted to black and white or color")
parser.add_argument("-n","--numColor","--numColour",nargs="?",type=int,default=0,help="positive integer to denote the number of colors that should appear in your nonogram IN ADDITION to your background color.\nA 0 or negative integer means the algorithm will choose this number for you. \n (default = 0)")
parser.add_argument("-r","--getResult",nargs="?",type=bool,default=True,help="boolean to indicate whether you want the finished picture (default = True)")
args = parser.parse_args()
print("arguments: " + str(args))
main(args.image[0], args.maxDim[0], bool(args.blackAndWhite), (1 if args.blackAndWhite else args.numColor), args.getResult)