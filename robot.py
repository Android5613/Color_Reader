import wpilib
from rev.color import ColorSensorV3


class MyRobot(wpilib.TimedRobot):

    RevColorChannel = 0

    def robotInit(self):

        self.RevColor = ColorSensorV3(self.RevColorChannel)

    def teleopPeriodic(self):

        print(self.RevColor.getColor())

        wpilib.Timer.delay(0.5)


if __name__ == "main":
    wpilib.run(MyRobot)
