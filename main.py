#region VEXcode Generated Robot Configuration
from vex import *
import urandom
import math

# Brain should be defined by default
brain=Brain()

# Robot configuration code
controller_1 = Controller(PRIMARY)

Upper = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
rightIN = Motor(Ports.PORT2, GearSetting.RATIO_18_1, False)
leftIN = Motor(Ports.PORT14, GearSetting.RATIO_18_1, False)

left_drive_smart = Motor(Ports.PORT10, GearSetting.RATIO_18_1, True)
right_drive_smart = Motor(Ports.PORT6, GearSetting.RATIO_18_1, False)

# Drivetrain (REQUIRED for auto)
drivetrain = DriveTrain(left_drive_smart, right_drive_smart, 319.19, 295, 40, MM, 1)
# wait for rotation sensor to fully initialize
wait(30, MSEC)


# Make random actually random
def initializeRandomSeed():
    wait(100, MSEC)
    random = brain.battery.voltage(MV) + brain.battery.current(CurrentUnits.AMP) * 100 + brain.timer.system_high_res()
    urandom.seed(int(random))
      
# Set random seed 
initializeRandomSeed()


def play_vexcode_sound(sound_name):
    # Helper to make playing sounds from the V5 in VEXcode easier and
    # keeps the code cleaner by making it clear what is happening.
    print("VEXPlaySound:" + sound_name)
    wait(5, MSEC)

# add a small delay to make sure we don't print in the middle of the REPL header
wait(200, MSEC)
# clear the console to make sure we don't have the REPL in the console
print("\033[2J")

#endregion VEXcode Generated Robot Configuration


# constants

AUTO_TEST = True   # <-- CHANGE TO False FOR REAL MATCHES
DEADZONE = 4

# Better stopping for accurate autos
left_drive_smart.set_stopping(BRAKE)
right_drive_smart.set_stopping(BRAKE)


############################################
# ⭐ INTAKE BUTTONS
############################################

def controller_1buttonY_pressed():
    Upper.set_velocity(70, PERCENT)
    leftIN.set_velocity(70, PERCENT)
    rightIN.set_velocity(70, PERCENT)

    # Outtake
    Upper.spin(REVERSE)
    rightIN.spin(FORWARD)
    leftIN.spin(REVERSE)


def controller_1buttonX_pressed():
    Upper.set_velocity(70, PERCENT)
    leftIN.set_velocity(70, PERCENT)
    rightIN.set_velocity(70, PERCENT)

    # Intake
    Upper.spin(FORWARD)
    rightIN.spin(REVERSE)
    leftIN.spin(FORWARD)


def controller_1button_released():
    Upper.stop(COAST)
    rightIN.stop(COAST)
    leftIN.stop(COAST)



############################################
# ⭐ DRIVER CONTROL
############################################

def drivercontrol():
#left joystick forward and backwards, right joystick is right and left
    while True:
        
        forward = controller_1.axis3.position()
        turn = controller_1.axis1.position()

        # Deadzone
        if abs(forward) < DEADZONE:
            forward = 0
        if abs(turn) < DEADZONE:
            turn = 0

        left_speed = forward + turn
        right_speed = forward - turn

        # Clamp speeds
        left_speed = max(min(left_speed, 100), -100)
        right_speed = max(min(right_speed, 100), -100)

        left_drive_smart.spin(FORWARD, left_speed, PERCENT)
        right_drive_smart.spin(FORWARD, right_speed, PERCENT)

        wait(10, MSEC)



def auto():
    brain.screen.clear_screen()
    brain.screen.set_cursor(1,1)
    brain.screen.print("AUTO STARTING")
    drivetrain.set_drive_velocity(60, PERCENT)

    # Drive forward 30 inches
    drivetrain.drive_for(REVERSE, 30, INCHES)

    # Turn left 45°
    drivetrain.turn_for(LEFT, 45, DEGREES)

    # Start outtake
    Upper.set_velocity(70, PERCENT)
    leftIN.set_velocity(70, PERCENT)
    rightIN.set_velocity(70, PERCENT)

    Upper.spin(FORWARD)
    rightIN.spin(REVERSE)
    leftIN.spin(FORWARD)

    # Drive forward while outtaking
    drivetrain.drive_for(REVERSE, 7, INCHES)

    wait(2000, MSEC)

    # Stop motors
    Upper.stop()
    rightIN.stop()
    leftIN.stop()

controller_1.buttonX.pressed(controller_1buttonX_pressed)
controller_1.buttonY.pressed(controller_1buttonY_pressed)
controller_1.buttonX.released(controller_1button_released)
controller_1.buttonY.released(controller_1button_released)

wait(2000, MSEC)

auto()

drivercontrol()
