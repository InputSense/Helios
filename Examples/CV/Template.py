# CV scripts use standard python as defined in your cv environment. Import any modules as needed
import os
import cv2


# The main worker class, must be called CVWorker (GCVWorker also works for legacy purposes)
class CVWorker:


    def __init__(self, width, height):
        os.chdir(os.path.dirname(__file__))

        # declaring gcvdata as a class variable creates it to keep persistence
        self.gcvdata = bytearray([0x00])
        
        # any other self variables can be declared in init
        self.my_variable = 10


    # it is recommended to del self variables upon stoppage
    def __del__(self):
        del self.gcvdata


    def process(self, frame):

        # declaring gcvdata in frame creates it empty every frame
        gcvdata = bytearray([0x00])

        #script logic goes here

        # always return frame and gcvdata
        # gcvdata must be one or the other, not both
        return frame, gcvdata
        # OR
        return frame, self.gcvdata



