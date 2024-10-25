import cv2
from utils import greatestCommonDenominator


class VideoReader():
    def __init__(self, videoPath):

        self.loadedVideo = cv2.VideoCapture(videoPath)
        self.width = self.loadedVideo.get(3)
        self.height = self.loadedVideo.get(4)
        self.aspectRatio = self.getAspectRatio()

        if self.aspectRatio[0] != 4 or self.aspectRatio[1] != 3:
            raise SystemExit("Your dims are out of whack bro")

    def getVideoDimensions(self):
        width = self.loadedVideo.get(3)  # 3- width 4- height
        height = self.loadedVideo.get(4)

        return width, height

    def getAspectRatio(self):
        gcd = greatestCommonDenominator(self.width, self.height)
        return int(self.width / gcd), int(self.height / gcd)

    def getReshapedFrame(self,dimensions):
        return cv2.rotate(cv2.resize(self.loadedVideo.read()[1], dimensions), cv2.ROTATE_90_CLOCKWISE)

    def getNextFrame(self):
        success, frame = self.loadedVideo.read()
        if success:
            return frame
        else:
            return None