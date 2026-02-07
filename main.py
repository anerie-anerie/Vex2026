#region VEXcode Generated Robot Configuration
from vex import *
import urandom
import math

# Brain should be defined by default
brain=Brain()

# Robot configuration code
controller_1 = Controller(PRIMARY)

Upper = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
rightIN = Motor(Ports.PORT2, GearSetting.RATIO_18_1, True)
leftIN = Motor(Ports.PORT14, GearSetting.RATIO_18_1, False)

left_drive_smart = Motor(Ports.PORT10, GearSetting.RATIO_18_1, True)
right_drive_smart = Motor(Ports.PORT6, GearSetting.RATIO_18_1, False)

Upper.set_velocity(80, PERCENT)
leftIN.set_velocity(80, PERCENT)
rightIN.set_velocity(80, PERCENT)

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

# add a small delay to make sure we don't print in the middle of the REPL header
wait(200, MSEC)
# clear the console to make sure we don't have the REPL in the console
print("\033[2J")

#CONSTANTS
DEADZONE = 6

# Better stopping for accurate autos
left_drive_smart.set_stopping(BRAKE)
right_drive_smart.set_stopping(BRAKE)


# intake/outtake commands

def outtake_all():

    # Outtake
    Upper.spin(REVERSE)
    rightIN.spin(REVERSE)
    leftIN.spin(REVERSE)


def intake_all():

    # Intake
    Upper.spin(FORWARD)
    rightIN.spin(FORWARD)
    leftIN.spin(FORWARD)


def intake_stop():
    Upper.stop(COAST)
    rightIN.stop(COAST)
    leftIN.stop(COAST)


def intake_roller():
    #intake flaps at bottom

    # Intake
    rightIN.spin(FORWARD)
    leftIN.spin(FORWARD)

def outtake_roller():
    #outtake flaps at bottom

    # outtake
    rightIN.spin(REVERSE)
    leftIN.spin(REVERSE)

def intake_belt():
    Upper.spin(FORWARD)
    
def outtake_belt():
    Upper.spin(REVERSE)

# DRIVER CONTROL

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

#kept two different auto functions in case of turning angle issues

def auto_right_low():

    #robot FORWARD facing on the right of the goal to score onto the low goal
    brain.screen.clear_screen()
    brain.screen.set_cursor(1,1)
    brain.screen.print("AUTO STARTING")
    drivetrain.set_drive_velocity(60, PERCENT)

    # Drive forward 30 inches
    drivetrain.drive_for(FORWARD, 30, INCHES)

    # Turn left 45°
    drivetrain.turn_for(LEFT, 45, DEGREES)

    # Start outtake
    Upper.set_velocity(30, PERCENT)
    leftIN.set_velocity(30, PERCENT)
    rightIN.set_velocity(30, PERCENT)

    Upper.spin(REVERSE)
    rightIN.spin(REVERSE)
    leftIN.spin(REVERSE)

    # Drive forward while outtaking
    drivetrain.drive_for(REVERSE, 7, INCHES)
    Upper.set_velocity(80, PERCENT)
    leftIN.set_velocity(80, PERCENT)
    rightIN.set_velocity(80, PERCENT)

    wait(3000, MSEC)

    # Stop motors
    Upper.stop()
    rightIN.stop()
    leftIN.stop()

def auto_left_high():

    #robot on the left of the goal (starting backwards) to score in the high goal  
    brain.screen.clear_screen()
    brain.screen.set_cursor(1,1)
    brain.screen.print("AUTO STARTING")

    #robot is backwards positioned to the left
    drivetrain.set_drive_velocity(60, PERCENT)

    # Drive forward 30 inches
    drivetrain.drive_for(REVERSE, 30, INCHES)

    # Turn left 45°
    drivetrain.turn_for(RIGHT, 45, DEGREES)

    # Start outtake
    Upper.set_velocity(30, PERCENT)
    leftIN.set_velocity(30, PERCENT)
    rightIN.set_velocity(30, PERCENT)

    Upper.spin(FORWARD)
    rightIN.spin(FORWARD)
    leftIN.spin(FORWARD)

    # Drive forward while outtaking
    drivetrain.drive_for(REVERSE, 7, INCHES)

    Upper.set_velocity(80, PERCENT)
    leftIN.set_velocity(80, PERCENT)
    rightIN.set_velocity(80, PERCENT)

    wait(3000, MSEC)

    # Stop motors
    Upper.stop()
    rightIN.stop()
    leftIN.stop()

#button bindings
controller_1.buttonX.pressed(intake_all)
controller_1.buttonY.pressed(outtake_all)

controller_1.buttonL1.pressed(intake_roller)
controller_1.buttonL2.pressed(outtake_roller)
controller_1.buttonR1.pressed(intake_belt)
controller_1.buttonR2.pressed(outtake_belt)

controller_1.buttonX.released(intake_stop)
controller_1.buttonY.released(intake_stop)

controller_1.buttonL1.released(intake_stop)
controller_1.buttonL2.released(intake_stop)
controller_1.buttonR1.released(intake_stop)
controller_1.buttonR2.released(intake_stop)

def ondriver_drivercontrol_0():
    drivercontrol()

def onauton_autonomous_0():
    #pick the auto in here
    auto_right_low()

def vexcode_auton_function():
    # Start the autonomous control tasks
    auton_task_0 = Thread( onauton_autonomous_0 )
    # wait for the driver control period to end
    while( competition.is_autonomous() and competition.is_enabled() ):
        # wait 10 milliseconds before checking again
        wait( 10, MSEC )
    # Stop the autonomous control tasks
    auton_task_0.stop()

def vexcode_driver_function():
    # Start the driver control tasks
    driver_control_task_0 = Thread( ondriver_drivercontrol_0 )

    # wait for the driver control period to end
    while( competition.is_driver_control() and competition.is_enabled() ):
        # wait 10 milliseconds before checking again
        wait( 10, MSEC )
    # Stop the driver control tasks
    driver_control_task_0.stop()


# register the competition functions (comp mode... fancy)
competition = Competition( vexcode_driver_function, vexcode_auton_function )

wait(3000, MSEC)
auto_right_low()
