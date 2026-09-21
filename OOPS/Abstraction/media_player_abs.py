# 19. Create an abstract MediaPlayer with:
# • load()
# • play()
# • stop()
# Implement:
# • MP3Player
# • WAVPlayer
# • AACPlayer
# Demonstrate calling each via a unified interface.

from abc import ABC, abstractmethod
class MediaPlayer(ABC):
    @abstractmethod
    def load(self):
        pass
    @abstractmethod
    def play(self):
        pass
    @abstractmethod
    def stop(self):
        pass
class MP3Player(MediaPlayer):
    def load(self):
        print("Loading MP3")
    def play(self):
        print("Playing MP3")
    def stop(self):
        print("Stopping MP3")
class WAVPlayer(MediaPlayer):
    def load(self):
        print("Loading WAV file")
    def play(self):
        print("Playing WAV")
    def stop(self):
        print("Stopping WAV")
class AACPlayer(MediaPlayer):
    def load(self):
        print("Loading AAC file")
    def play(self):
        print("Playing AAC")
    def stop(self):
        print("Stopping AAC")
players = [MP3Player(), WAVPlayer(), AACPlayer()]
for p in players:
    p.load()
    p.play()
    p.stop()