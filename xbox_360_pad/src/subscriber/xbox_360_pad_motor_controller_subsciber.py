#!/usr/bin/env python
import rospy
from xbox_360_pad.msg import xbox_360_pad




def motor_control_callback(message):
    #get_caller_id(): Get fully resolved name of local node
    #ospy.loginfo(rospy.get_caller_id())

    rospy.loginfo(message)


    

def listener():

    rospy.init_node('mecanum_motor_controller_listener', anonymous=True)

    rospy.Subscriber("xbox_360_pad_topic", xbox_360_pad, motor_control_callback)

    rospy.spin()

if __name__ == '__main__':
    listener()
