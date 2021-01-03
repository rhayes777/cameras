#!/usr/bin/env python

import time
from queue import Queue

import cv2 as cv
from threading import Thread

from .util import filename_for_time


class Reader:
    def __init__(self, lag: int, duration: int):
        self.lag = lag
        self.duration = duration

        self.is_stopped = False
        self.queue = Queue()

    def filename(self):
        return filename_for_time(
            time.time() - self.lag,
            self.duration
        )

    def start(self):
        t = Thread(target=self.update, args=())
        t.daemon = True
        t.start()
        return self

    def update(self):
        last_filename = None
        while True:
            if self.is_stopped:
                break

            filename = self.filename()
            if filename == last_filename:
                continue
            cap = cv.VideoCapture(self.filename())
            print(f"opened {filename}")
            while cap.isOpened():
                ret, frame = cap.read()
                # if frame is read correctly ret is True
                if not ret:
                    print("Can't receive frame (stream end?). Exiting ...")
                    break
                self.queue.put(frame)
            cap.release()
            last_filename = filename

    @property
    def is_frame(self):
        return not self.queue.empty()

    def stop(self):
        self.is_stopped = True

    def next(self):
        return self.queue.get()


class Display:
    def __init__(self, reader: Reader):
        self.reader = reader

    def run(self):
        self.reader.start()
        while True:
            if self.reader.is_frame:
                frame = self.reader.next()
                cv.imshow('frame', frame)

                if cv.waitKey(1) == ord('q'):
                    break

        self.reader.stop()


def read():
    reader = Reader(10, 5)
    display = Display(reader)
    display.run()
    cv.destroyAllWindows()


if __name__ == "__main__":
    read()
