#!/usr/bin/env python

import datetime as dt
import time
from .util import filename_for_time

import cv2


class VideoWriter:
    def __init__(self, cap, duration: int):
        self.cap = cap
        self._duration = duration
        self.duration = dt.timedelta(
            seconds=duration
        )

        # Get the width and height of frame
        self.width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) + 0.5)
        self.height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) + 0.5)

        self.shape = (self.width, self.height)

    def capture(self):
        now = dt.datetime.now()
        terminate_at = now + self.duration

        filename = filename_for_time(
            time.time(),
            duration=self._duration
        )

        # Define the codec and create VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Be sure to use the lower case
        out = cv2.VideoWriter(filename, fourcc, 20.0, self.shape)

        while dt.datetime.now() < terminate_at:
            ret, img = self.cap.read()

            if img is not None:
                # write the flipped frame
                out.write(img)

        out.release()


def write():
    cap = cv2.VideoCapture(1)

    writer = VideoWriter(cap, 5)

    while True:
        writer.capture()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    write()
