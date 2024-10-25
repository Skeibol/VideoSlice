import cv2
import numpy as np

A3_DIMS = (1191,842)
# 4*20, 3*20
FRAME_DIMS = (80,60)

def setPixels(x: int, y: int, width, height, value, inputImage):
    center = (int(y+(height/2)),int(x+(width/2)))

    frameX = center[0] - int(FRAME_DIMS[0]/2)
    frameY = center[1] - int(FRAME_DIMS[1]/2)

    inputImage[y:y+height,x:x+width,:] = value

    inputImage[frameX:frameX+FRAME_DIMS[0],frameY:frameY+FRAME_DIMS[1],:] = 0




if __name__ == "__main__":
    horizontalSlices = 9
    verticalSlices = 13

    A3Width = int(A3_DIMS[1] / horizontalSlices)
    A3Height = int(A3_DIMS[0] / verticalSlices)

    print(f"w: {A3Width*horizontalSlices} h:{A3Height*verticalSlices}")

    pic = np.full((1191, 842, 3), 255, dtype=np.uint8)
    color = 0
    colorFactor = 255/(horizontalSlices*verticalSlices)
    for i in range(verticalSlices):
        for j in range(horizontalSlices):

            setPixels(j*A3Width,i*A3Height,A3Width,A3Height, color, pic)
            color+=colorFactor

    cv2.imwrite('color_img.jpg', pic)
    cv2.imshow('image', pic)
    cv2.waitKey(0)
