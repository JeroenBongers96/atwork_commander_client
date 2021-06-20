#!/usr/bin/env python

from __future__ import print_function

import sys
import rospy
from suii_communication_ros1.srv import TableGoal

class SendTableGoal:
    def __init__(self):
        print("sending goal...")
        rospy.wait_for_service('table_goal')
        self.table_goal = rospy.ServiceProxy('table_goal', TableGoal)
        print("table_goal found")
            
    def send_goal(self, table):
        try:
            resp = self.table_goal(table)
            print("Goal achieved: {}".format(resp.succes))
            return resp.succes
        except rospy.ServiceException as e:
            print("Service call failed: %s"%e)

if __name__ == "__main__":
    task = SendTableGoal()
    task.send_goal("TEST_GOAL")