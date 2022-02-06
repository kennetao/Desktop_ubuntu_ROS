#!/usr/bin/env python
import rospy
import time
from xbox_360_pad.msg import xbox_360_pad

#create a new publisher. we specify the topic name, then type of message then the queue size
pub = rospy.Publisher('xbox_360_pad_topic', xbox_360_pad, queue_size=10)

#we need to initialize the node
rospy.init_node('xbox_360_pad_topic', anonymous=True)

#set the loop rate
rate = rospy.Rate(1) # 20hz

xboxpad = xbox_360_pad()
while not rospy.is_shutdown():

    xboxpad.joy_l_lr += 1

    xboxpad.joy_l_ud += 2

    xboxpad.joy_r_lr += 3

    xboxpad.joy_r_ud += 4

    rospy.loginfo("I publish:")
    rospy.loginfo(xboxpad)

    pub.publish(xboxpad)
    rate.sleep()