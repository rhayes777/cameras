import subprocess
import threading
import time

WAIT_SECONDS = 1


# ffmpeg -f avfoundation -framerate 30 -i default output.mp4
# /Applications/VLC.app/Contents/MacOS/VLC output.mp4


class Recorder(threading.Thread):
    def __init__(self, interval):
        self.interval = interval
        self.stopped = threading.Event()
        super().__init__()

    def run(self):
        while not self.stopped.wait(self.interval):
            self.record()

    def record(self):
        filename = f"{int(time.time() / self.interval)}.mp4"
        subprocess.Popen([
            "ffmpeg", "-f", "avfoundation", "-framerate", "30", "-i", "default", filename
        ])


def foo():
    print(time.ctime())
    threading.Timer(WAIT_SECONDS, foo).start()


if __name__ == "__main__":
    recorder = Recorder(
        5
    )
    recorder.start()
