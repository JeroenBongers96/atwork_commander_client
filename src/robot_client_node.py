#!/usr/bin/env python3

import rospy
from atwork_commander_msgs.msg import RobotState
from atwork_commander_msgs.msg import Task
from suii_communication_ros1.srv import TableGoal

task_list = []

def task_callback(msg):
    print("=======================")
    task_list = []
    for state in msg.arena_start_state:
        task_list.append(state.workstation_name)
    for state in msg.arena_target_state:
        task_list.append(state.workstation_name)
    task_list.append("END_WS")
    print(task_list)

    #TODO: Use table_goal service to send goal
    # print("start waiting")
    # rospy.wait_for_service('suii_communication_ros1/TableGoal')
    # print("done waiting")
    # try:
    #     exe_goal = rospy.ServiceProxy('suii_communication_ros1/TableGoal', TableGoal)
    #     resp1 = exe_goal("WS01")
    #     print(resp1.succes) 
    # except rospy.ServiceException as e:
    #     print("Service call failed: %s"%e)
    
    #TODo: Respond to refbox that test is finished

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
            rate.sleep()
        except rospy.ROSInterruptException:
            break
