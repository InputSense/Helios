import os
import cv2


class CVWorker:
    
    def __init__(self, width, height):
        os.chdir(os.path.dirname(__file__))

        # declaring gcvdata as a class variable makes it persistent
        self.gcvdata = bytearray([0x00])


    def __del__(self):
        del self.gcvdata


    def process(self, frame):

        # declaring gcvdata in frame makes it new every frame
        gcvdata = bytearray([0x00])

        # always return frame and gcvdata
        # gcvdata must be one or the other, not both
        return frame, gcvdata
        # OR
        return frame, self.gcvdata




