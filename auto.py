'''
auto code options (anerie will add more paths tonight)
Approximately 12.67 inches to the bottom lip.
Upper Center Goal: Approximately 8.01 inches to the bottom lip.
Lower Center Goal: Approximately 0.5 inches.'''

#auto routes: use 2 pre-loaded and score into upper central goal or low central goal -> intake more

#starts right from the goal (put robot in backwards position, moves forward then turns left and then drives forward while outtaking)
def auto():
    brain.screen.clear_screen()
    brain.screen.set_cursor(1,1)
    brain.screen.print("AUTO STARTING")
    drivetrain.set_drive_velocity(70, PERCENT)

    # Drive forward 30 inches
    drivetrain.drive_for(REVERSE, 30, INCHES)

    # Turn left 45°
    drivetrain.turn_for(RIGHT, 45, DEGREES)

    # Start outtake
    Upper.set_velocity(70, PERCENT)
    leftIN.set_velocity(70, PERCENT)
    rightIN.set_velocity(70, PERCENT)

    Upper.spin(FORWARD)
    rightIN.spin(REVERSE)
    leftIN.spin(FORWARD)

    # Drive forward while outtaking
    drivetrain.drive_for(FORWARD, 7, INCHES)

    # Stop motors
    Upper.stop()
    rightIN.stop()
    leftIN.stop()
