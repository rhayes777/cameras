#!/usr/bin/env python

import time

import cv2 as cv

from .util import filename_for_time


class Reader:
    def __init__(self, lag: int):
        self.lag = lag

    def filename(self):
        return filename_for_time(
            time.time() - self.lag
        )

    def show(self):
        cap = cv.VideoCapture(self.filename())
        while cap.isOpened():
            ret, frame = cap.read()
            # if frame is read correctly ret is True
            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                break
            cv.imshow('frame', frame)
            if cv.waitKey(1) == ord('q'):
                break
        cap.release()

    def run(self):
        while True:
            if cv.waitKey(1) == ord('q'):
                break
            self.show()


def read():
    Reader(10).run()
    cv.destroyAllWindows()


if __name__ == "__main__":
    read()
