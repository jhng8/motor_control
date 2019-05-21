import l293d
import time

# Documentation for L239D chip - https://l293d.readthedocs.io/en/latest/user-guide/python-scripts/
# Parameters used in code - https://l293d.readthedocs.io/en/latest/methods/clockwise-anticlockwise/
# Hardware set up used - https://l293d.readthedocs.io/en/latest/user-guide/hardware-setup/

""" 
IMPORTANT NOTE TO SELF/OTHERS - Make sure GPIO pin numbers from Raspberry pi 
match up with diagram (order matters), as an incomplete connection could reverse
the polarity of the DC motors and possibly break the gears, not spin, or make 
the motors jitter and not move (reversed polarity)
"""

""" Code """

""" Sets motor 1 and motor 2 GPIO pins """
# Motor 1 uses Rpi pins 22, 18, 16
upDownMotor1 = l293d.DC(22,18,16)
# Motor 2 uses Rpi pins 15, 13, 11
upDownMotor2 = l293d.DC(15,13,11)

""" Sets motor 3 and motor 4 GPIO pins """
# Motor 3 uses Rpi pins 29, 31, 33
turnMotor = l293d.DC(32,31,29)
# Motor 4 uses Rpi pins 37, 36, 35
clawMotor = l293d.DC(37,36,33)

""" Used for arm control up and down"""

def up():
    """ 
    Function that makes the robotic arm go up.
    Arguments of duration (1.95) and speed (10) makes the VEX motor 269 
    turn 90 degrees when attached to a 6V power supply.
    """
    print("Going Up")
    for motor in [upDownMotor1,upDownMotor2]:                   
        motor.clockwise(duration=1.95, speed=10)
        time.sleep(1)
    
def down():
    """ 
    Function that makes the robotic arm go down.
    Arguments of duration (1.95) and speed (10) makes the VEX motor 269 turn 
    90 degrees when attached to a 6V power supply.
    """
    print("Going Down")
    for motor in [upDownMotor1,upDownMotor2]:
        motor.anticlockwise(duration=1.95,speed=10)
        time.sleep(1)
    
def turnRight():
    """ 
    Function that makes the robotic arm go right.
    Arguments of duration (1.95) and speed (50) makes the VEX 393 turn 90 degrees
    when attached to a 6V power supply
    """
    print("Going Right")
    turnMotor.clockwise(duration=1.95, speed=50)
    
def turnLeft():
    """ 
    Function that makes the robotic arm go left.
    Arguments of duration (1.95) and speed (50) makes the VEX 393 turn 90 degrees
    when attached to a 6V power supply
    """
    print("Going Left")
    turnMotor.anticlockwise(duration=1.95,speed=50)
    
def openClaw():
    """ 
    Function that opens the robotic claw by turing the connected motor by 
    90 degrees clockwise (VEX Motor 393 connected to 6V battery pack)
    """
    print("Opening Claw")
    clawMotor.clockwise(duration=1.95, speed=50)

def closeClaw():
    """ 
    Function that opens the robotic claw by turing the connected motor by 
    90 degrees counterclockwise (VEX Motor 393 connected to 6V battery pack 
    """
    print("Closing Claw")
    clawMotor.anticlockwise(duration=1.95, speed=50)

def pickUpRight():
    """ 
    Picks up item on the crane's right side at around 90 degrees by calling 
    other functions (takes no arguments)
    """
    print("$$$$ Start Picking up Right")
    #turns right
    turnRight()
    #opens claw, descends to pick object up
    openClaw()
    down()
    #gets object, goes back up
    closeClaw()
    up()
    #turns left again
    turnLeft()
    #drops item
    openClaw()
    #allows time for item to drop, closes
    time.sleep(2)
    closeClaw()
    print("$$$$ Done Picking up Right")
    
def pickUpLeft():
    """ 
    Picks up item on the crane's left side at around 90 degrees by calling 
    other functions (takes no arguments)
    """
    print("$$$$ Start Picking up Left")
    #turns right
    turnLeft()
    #opens claw, descends to pick object up
    openClaw()
    down()
    #gets object, goes back up
    closeClaw()
    up()
    #turns left again
    turnRight()
    #drops item
    openClaw()
    #allows time for item to drop, closes
    time.sleep(2)
    closeClaw()
    print("$$$$ Done Picking up Item at Left")

def test():
    upDownMotor1.clockwise(duration=2)
    upDownMotor1.anticlockwise(duration=2)
    upDownMotor2.clockwise(duration=2)
    upDownMotor2.anticlockwise(duration=2)
    clawMotor.clockwise(duration=2)
    clawMotor.anticlockwise(duration=2)
    turnMotor.clockwise(duration=2)
    turnMotor.anticlockwise(duration=2)
    
# Calls function
pickUpLeft()

# Cleans up GPIO board so that nothing is left over and does not fry the circuit board
l293d.cleanup()