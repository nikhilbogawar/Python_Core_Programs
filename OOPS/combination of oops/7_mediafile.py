# 7. Design:
# • Abstract class MediaFile with play(), stop()
# • Subclasses: MP3File, MP4File, WAVFile
# • Private file path validation done internally
# • A function start_player(media) that works with ANY object that has play()
# (duck typing)
# Demonstrate mixing true polymorphism + duck typing.
from abc import ABC, abstractmethod
class MediaFile(ABC):
    @abstractmethod
    def play(self):
        pass
    @abstractmethod
    def stop(self):
        pass
class MP3File(MediaFile):
    def play(self):
        print("Playing MP3")
    def stop(self):
        print("Stopping MP3")
class MP4File(MediaFile):
    def play(self):
        print("Playing MP4")
    def stop(self):
        print("Stopping MP4")
class WAVFile(MediaFile):
    def play(self):
        print("Playing WAV")
    def stop(self):
        print("Stopping WAV")
def start_player(media):
    media.play()
start_player(MP3File())
start_player(MP4File())
