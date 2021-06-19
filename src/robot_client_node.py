#!/usr/bin/env python3

import rospy
from atwork_commander_msgs.msg import RobotState
from atwork_commander_msgs.msg import Task

def task_callback(msg):
    rospy.loginfo(msg)

if __name__ == "__main__":
    rospy.init_node("suii_refbox_client", anonymous=True)

    refboxName = "atwork_commander"
    teamName = "RoboHubEindhoven"
    robotName = "suii"

    if (rospy.get_param('~refboxName') != refboxName):
        rospy.WARN("Incorrect refbox name")
    if (rospy.get_param('~teamName') != teamName):
        rospy.WARN("Incorrect team name")
    if(rospy.get_param('~robotName') != robotName):
        rospy.WARN("Incorrect robot name")

    task_sub = rospy.Subscriber("/"+refboxName+"/task", Task, task_callback, queue_size=1)
    state_pub = rospy.Publisher("/"+refboxName+"/robot_state", RobotState, queue_size=1)

    robot_state = RobotState()
    robot_state.sender.team_name = teamName
    robot_state.sender.robot_name = robotName

    rate = rospy.Rate(2)

    while not rospy.is_shutdown():
        try:
            robot_state.sender.header.stamp = rospy.Time.now()
            state_pub.publish(robot_state)
            rospy.spin()
            rate.sleep()
        except rospy.ROSInterruptException:
            break
