#!/usr/bin/env python

from __future__ import print_function

import sys
import rospy
from suii_communication_ros1.srv import TableGoal

def add_two_ints_client(x, y):
    rospy.wait_for_service('table_goal')
    try:
        add_two_ints = rospy.ServiceProxy('table_goal', TableGoal)
        resp1 = add_two_ints("ws01")
        return resp1.succes
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

if __name__ == "__main__":
  add_two_ints_client(1,2)