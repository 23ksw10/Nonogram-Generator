# Nonogram-Generator

## About the Project

<img src="https://user-images.githubusercontent.com/50804079/160569499-11dd6075-5d5d-4fcf-9794-5cd059a56e82.jpg"  width="600">
<img src="https://user-images.githubusercontent.com/50804079/160572288-0cc94e58-63bc-483e-b7a8-5eec5993774e.jpg"  width="600">


**Nonograms** are picture logic puzzles. Mode details about Nonogram(https://en.wikipedia.org/wiki/Nonogram)


**Nonogram-Generators** can make any pictures you have to Nonogram. Color or Black and White. Any size you want.
## Usage
---
GenNonogram.py [-h] [-d MAXDIM] [-b] [-n [NUMCOLOR]] [-r [GETRESULT]] image

    positional arguments:
        image: path to image to be processed

    optional arguments:
        -h, --help: show this help message and exit
        -d MAXDIM, --maxDim MAXDIM: maximum no. of squares in any dimension in the nonogram (default = 80)
        -b, --blackAndWhite: indicate the image should be converted to black and white
        -n [NUMCOLOR], --numColor [NUMCOLOR], --numColour [NUMCOLOR]: positive integer to denote the number of colors that should appear in your nonogram IN ADDITION to your background color. A 0 or negative integer means the algorithm will choose this number for you. (default = 0)
        -r [GETRESULT], --getResult [GETRESULT] boolean to indicate whether you want a separate file containing the finished picture (default = True)
