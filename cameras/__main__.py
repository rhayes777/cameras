import os

from .record import Recorder, Player

if __name__ == "__main__":
    interval = 5
    directory = f"{os.getcwd()}/videos"

    os.makedirs(directory, exist_ok=True)

    recorder = Recorder(
        interval=interval,
        directory=directory
    )
    player = Player(
        interval=interval,
        lag=interval,
        directory=directory
    )
    recorder.start()
    player.start()
