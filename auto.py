'''
auto code options (anerie will add more paths tonight)
Approximately 12.67 inches to the bottom lip.
Upper Center Goal: Approximately 8.01 inches to the bottom lip.
Lower Center Goal: Approximately 0.5 inches.'''

#auto routes: use 2 pre-loaded and score into upper central goal or low central goal -> intake more

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

    Upper.spin(FORWARD)
    rightIN.spin(REVERSE)
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

def auto_left_high():

    #robot on the left of the goal to score in the high goal  
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
    rightIN.spin(REVERSE)
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
    rightIN.stop()
    leftIN.stop()

