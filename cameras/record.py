import os
import subprocess
import threading
import time

from abc import ABC, abstractmethod


class VideoThread(threading.Thread, ABC):
    def __init__(self, interval, directory):
        self.interval = interval
        self.stopped = threading.Event()
        self.directory = directory
        super().__init__()

    def _filename_at_time(self, seconds: float):
        return f"{self.directory}/{int(seconds / self.interval)}.mp4"

    def run(self):
        while not self.stopped.wait(self.interval):
            self.do()

    @abstractmethod
    def do(self):
        pass


class Player(VideoThread):
    def __init__(self, interval, lag, directory):
        super().__init__(interval, directory)
        self.lag = lag

    def do(self):
        filename = self._filename_at_time(
            time.time() - self.lag
        )
        print(f"Attempting to play {filename}")
        if os.path.exists(filename):
            subprocess.Popen([
                "/Applications/VLC.app/Contents/MacOS/VLC", filename
            ])
        else:
            print("Does not exist")


class Recorder(VideoThread):
    def do(self):
        filename = self._filename_at_time(
            time.time()
        )
        subprocess.Popen([
            "ffmpeg", "-f", "avfoundation", "-t", str(self.interval), "-framerate", "30", "-i", "default", filename
        ])
