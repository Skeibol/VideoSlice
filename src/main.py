import cv2
from VideoReader import VideoReader
import numpy as np
import argparse
import os

def makeMosaic(x: int, y: int, width, height, inputImage, mosaicImage):

    center = (int(y+(height/2)),int(x+(width/2)))

    frameX = center[0] - int(FRAME_DIMS[0]/2)
    frameY = center[1] - int(FRAME_DIMS[1]/2)

    #inputImage[y:y+height,x:x+width,:] = 255

    inputImage[frameX:frameX+FRAME_DIMS[0],frameY:frameY+FRAME_DIMS[1],:] = mosaicImage

def parse():
    prs = argparse.ArgumentParser(add_help=False)
    prs.add_argument('-file', dest='src', type=str, help='video name (in videos folder)')
    prs.add_argument('-out', dest='out', type=str, help='output file name')
    prs.add_argument('-w', dest='width', type=int, help='width of mosaic frames(default 80)', default=80)
    prs.add_argument('-h', dest='height', type=int, help='height of mosaic frames(default 60)', default=60)
    prs.add_argument('-rows', dest='rows', type=int, help='no. of rows(default 12)', default=12)
    prs.add_argument('-cols', dest='cols', type=int, help='no. of cols(default 10', default=10)
    prs.add_argument('-help', '--help', action='help', default=argparse.SUPPRESS,
                        help='Show this help message and exit.')
    prs.add_argument('-init', action='store_true')



    return prs.parse_args()

def tryMakeFolders():
    if os.path.exists(IMAGE_DIRECTORY):
        pass
    else:
        try:
            os.mkdir(f"{IMAGE_DIRECTORY}")
            print(f"Directory {IMAGE_DIRECTORY} created")
        except FileExistsError:
            print(f"Directory '{IMAGE_DIRECTORY}' already exists.")
        except PermissionError:
            print(f"Permission denied: Unable to create '{IMAGE_DIRECTORY}'.")
        except Exception as e:
            print(f"An error occurred: {e}")

    if os.path.exists(VIDEOS_DIRECTORY):
        pass
    else:
        try:
            os.mkdir(f"{VIDEOS_DIRECTORY}")
            print(f"Directory {VIDEOS_DIRECTORY} created")
        except FileExistsError:
            print(f"Directory '{VIDEOS_DIRECTORY}' already exists.")
        except PermissionError:
            print(f"Permission denied: Unable to create '{VIDEOS_DIRECTORY}'.")
        except Exception as e:
            print(f"An error occurred: {e}")



def initialize():
    tryMakeFolders()

if __name__ == "__main__":
    IMAGE_DIRECTORY = "./images"
    VIDEOS_DIRECTORY = "./videos"


    args = parse()
    if args.init:
        initialize()
        raise SystemExit("Initialized app. . .  Put video in videos folder")

    if args.src is None:
        raise SystemExit("Bad file path. Include file name and extension and make sure the file is in the videos folder (-src <filename.mp4>)")

    A3_DIMS = (1191, 842)
    FRAME_DIMS = (args.width, args.height)  # 4*20, 3*20
    COLUMNS = args.cols
    ROWS = args.rows
    FILENAME = args.src

    if not os.path.exists(f"{VIDEOS_DIRECTORY}/{FILENAME}"):
        raise SystemExit("Your video is out of whack bro. It dont exist, put it in videos folder and include extension (.mp4)")


    A3Width = int(A3_DIMS[1] / COLUMNS)
    A3Height = int(A3_DIMS[0] / ROWS)

    print(f"width : {A3Width*COLUMNS} height :{A3Height*ROWS}")

    reader = VideoReader(f'{VIDEOS_DIRECTORY}/{FILENAME}')


    A3Paper = np.full((1191, 842, 3), 255, dtype=np.uint8)

    for i in range(ROWS):
        for j in range(COLUMNS):
            reader.getNextFrame()
            frame = reader.getReshapedFrame(FRAME_DIMS)
            if frame is not None:
                makeMosaic(j*A3Width,i*A3Height,A3Width,A3Height, A3Paper, frame)





    if args.out is not None:
        print(f"File saved as {args.out}.jpg")
        cv2.imwrite(f'{IMAGE_DIRECTORY}/{args.out}.jpg', A3Paper)
    else:
        imgNumber = 0
        while os.path.isfile(f'{IMAGE_DIRECTORY}/slide{imgNumber}.jpg'):
            imgNumber+=1
        print(f"File saved as slide{imgNumber}.jpg")
        cv2.imwrite(f'{IMAGE_DIRECTORY}/slide{imgNumber}.jpg', A3Paper)
