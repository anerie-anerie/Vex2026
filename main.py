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

myVariable = 0

'''
def controller_1buttonX_pressed_callback_0():
    global myVariable
    Upper.spin(FORWARD)
    rightIN.spin(FORWARD)
    leftIN.spin(REVERSE)
    Upper.set_velocity(70, PERCENT)
    leftIN.set_velocity(70, PERCENT)
    rightIN.set_velocity(70, PERCENT)
    wait(6, SECONDS)
    Upper.stop()
    rightIN.stop()
    leftIN.stop()

'''

def controller_1buttonX_pressed():
    Upper.set_velocity(70, PERCENT)
    leftIN.set_velocity(70, PERCENT)
    rightIN.set_velocity(70, PERCENT)

    Upper.spin(FORWARD)
    rightIN.spin(REVERSE)
    leftIN.spin(FORWARD)

def controller_1buttonX_released():
    Upper.stop(COAST)
    rightIN.stop(COAST)
    leftIN.stop(COAST)


# system event handlers
controller_1.buttonX.pressed(controller_1buttonX_pressed)
controller_1.buttonX.released(controller_1buttonX_released)

DEADZONE = 5


def drivercontrol():
    while True:
        forward = controller_1.axis3.position()
        turn = controller_1.axis1.position()

        # Apply deadzone
        if abs(forward) < DEADZONE:
            forward = 0
        if abs(turn) < DEADZONE:
            turn = 0

        left_speed = forward + turn
        right_speed = forward - turn

        # Clamp speeds to ±100 (important!)
        left_speed = max(min(left_speed, 100), -100)
        right_speed = max(min(right_speed, 100), -100)

        left_drive_smart.spin(FORWARD, left_speed, PERCENT)
        right_drive_smart.spin(FORWARD, right_speed, PERCENT)

        wait(10, MSEC)

drivercontrol()

# add 15ms delay to make sure events are registered correctly.
wait(15, MSEC)
