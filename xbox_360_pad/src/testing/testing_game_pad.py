#!/usr/bin/env python
#import rospy
import evdev
import time
#from xbox_360_pad.msg import xbox_360_pad

#create a new publisher. we specify the topic name, then type of message then the queue size
#pub = rospy.Publisher('xbox_360_pad_topic', xbox_360_pad, queue_size=10)

#we need to initialize the node
#rospy.init_node('xbox_360_pad_topic', anonymous=True)

#set the loop rate
#rate = rospy.Rate(20) # 20hz

counter = 0

while(True):
    try:
        gamepad = evdev.InputDevice('/dev/input/event' + str(counter))
        counter += 1
        if(gamepad.name == 'Microsoft X-Box 360 pad'):
            break
        if(counter > 10):
            counter = 0

        #print(gamepad.name)

    except Exception as e:
        print(e)
    time.sleep(0.2)

#xboxpad = xbox_360_pad()

#while not rospy.is_shutdown():

for event in gamepad.read_loop():

    # Left Joy left right
    if(event.type == 3 and event.code == 0):
        print(event.value)
        #xboxpad.joy_l_lr = event.value

    # Left Joy up dow
    elif(event.type == 3 and event.code == 1):
        print(event.value)
        #xboxpad.joy_l_ud = event.value

    # Right Joy left right
    elif(event.type == 3 and event.code == 3):
        print(event.value)
        #xboxpad.joy_r_lr = event.value

    # Right Joy up dow
    elif(event.type == 3 and event.code == 4):
        print(event.value)
        #xboxpad.joy_r_ud = event.value

    #rospy.loginfo("I publish:")
    #rospy.loginfo(xboxpad)

    #pub.publish(xboxpad)
    #rate.sleep()