#!/usr/bin/env python
import os

import cv2 as cv
import time
from .util import filename_for_time


class Reader:
    def __init__(self, lag: int):
        self.lag = lag

    def filename(self):
        return filename_for_time(
            time.time() - self.lag
        )

    def run(self):
        while os.path.exists(
            self.filename()
        ):
            self.show()

    def show(self):
        cap = cv.VideoCapture(
            self.filename()
        )
        while cap.isOpened():
            ret, frame = cap.read()
            # if frame is read correctly ret is True
            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                break
            cv.imshow('frame', frame)
        cap.release()


def read():
    reader = Reader(10)
    reader.run()


if __name__ == "__main__":
    read()
