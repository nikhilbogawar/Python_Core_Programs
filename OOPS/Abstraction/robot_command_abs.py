# 16. Create an abstract class RobotCommand with:
# • execute()
# • undo()
# Implement:
# • PickCommand
# • PlaceCommand
# • MoveCommand
# Demonstrate how abstraction cleanly represents commands without revealing details.

from abc import ABC, abstractmethod
class RobotCommand(ABC):
    @abstractmethod
    def execute(self):
        pass
    @abstractmethod
    def undo(self):
        pass
class PickCommand(RobotCommand):
    def execute(self):
        print("Picking object")
    def undo(self):
        print("Undo pick")
class PlaceCommand(RobotCommand):
    def execute(self):
        print("Placing object")
    def undo(self):
        print("Undo place")
class MoveCommand(RobotCommand):
    def execute(self):
        print("Moving robot")
    def undo(self):
        print("Undo move")
rc=[PickCommand(),PlaceCommand(),MoveCommand()]
for cmd in rc:
    cmd.execute(); cmd.undo()
