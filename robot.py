import wpilib
from rev.color import ColorSensorV3


class MyRobot(wpilib.TimedRobot):

    def robotInit(self):

        RevColor = ColorSensorV3(wpilib.I2C.Port.kOnboard)

    def robotPeriodic(self):

        RGBColor = self.RevColor.getcolor()

        wpilib.SmartDashboard.putNumber("Red", RGBColor.red)
        wpilib.SmartDashboard.putNumber("Green", RGBColor.green)
        wpilib.SmartDashboard.putNumber("Blue", RGBColor.blue)


        wpilib.Timer.delay(0.5)


if __name__ == "main":
    wpilib.run(MyRobot)
