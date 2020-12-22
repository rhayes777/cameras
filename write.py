#!/usr/bin/env python

import datetime as dt
import time

import cv2


class VideoWriter:
    def __init__(self, cap, duration: int):
        self.cap = cap
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

        increment = round(int(time.time()) / 5)

        # Define the codec and create VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Be sure to use the lower case
        out = cv2.VideoWriter(f'videos/{increment}.mp4', fourcc, 20.0, self.shape)

        while dt.datetime.now() < terminate_at:
            ret, img = self.cap.read()

            if ret:
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
