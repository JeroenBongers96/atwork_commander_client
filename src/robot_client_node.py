#!/usr/bin/env python3

import rospy
from atwork_commander_msgs.msg import RobotState
from atwork_commander_msgs.msg import Task

if __name__ == "__main__":
    while not rospy.is_shutdown():
        try:
            print("node is running")
        except rospy.ROSInterruptException:
            break
