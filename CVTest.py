import os
import cv2
import random
import gtuner


class GCVWorker:
    def __init__(self, width, height):
        os.chdir(os.path.dirname(__file__))
        self.gcvdata = bytearray([0x00])
        self.noun = "user"
        self.nouns = ["user", "player", "member", "patron", "client", "consumer", "operator", "utilizer", "handler", "contender", "competitor", "contestant", "performer", "actor", "rival", "protagonist", "antagonist", "challenger", "adversary", "opponent", "friend", "teammate", "peer", "counterpart", "enemy"]
        self.frame_count = 0
        self.speed = 0.00001


    def __del__(self):
        del self.gcvdata


    def process(self, frame):
        gcvdata = bytearray([0x00])
        gcvdata[0] = self.frame_count
        self.speed += 0.0000125
        gcvdata.extend(int(self.speed * 0x10000).to_bytes(4, byteorder='big', signed=True))

        cv2.putText(frame, "Hello, " + str(self.noun), (770,200), cv2.FONT_HERSHEY_COMPLEX, 0.666, (255, 255, 255), 1, cv2.LINE_AA)

        if self.frame_count == 60:
            self.noun = self.nouns[random.randint(0, len(self.nouns)-1)]
            self.frame_count = 0
        cv2.putText(frame, str(self.frame_count), (10, 20), cv2.FONT_HERSHEY_COMPLEX, 0.666, (255, 255, 255), 1, cv2.LINE_AA)
        self.frame_count += 1
        return (frame, gcvdata)




