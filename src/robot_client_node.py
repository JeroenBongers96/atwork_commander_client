#!/usr/bin/env python3

import rospy
from atwork_commander_msgs.msg import RobotState
from atwork_commander_msgs.msg import Task
from suii_communication_ros1.srv import TableGoal

task_list = []

class SendTableGoal:
    def __init__(self):
        print("waiting for service table_goal...")
        rospy.wait_for_service('table_goal')
        self.table_goal = rospy.ServiceProxy('table_goal', TableGoal)
        print("table_goal found")

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

        self.robot_state = RobotState()
        self.robot_state.sender.team_name = teamName
        self.robot_state.sender.robot_name = robotName

        task_sub = rospy.Subscriber("/"+refboxName+"/task", Task, self.task_callback, queue_size=1)
        self.state_pub = rospy.Publisher("/"+refboxName+"/robot_state", RobotState, queue_size=1)
    
    def send_goal(self, table):
        try:
            resp = self.table_goal(table)
            print("Goal achieved: {}".format(resp.succes))
            return resp.succes
        except rospy.ServiceException as e:
            print("Service call failed: %s"%e)

    def task_callback(self, msg):
        print("=======================")
        task_list = []
        for state in msg.arena_start_state:
            task_list.append(state.workstation_name)
        for state in msg.arena_target_state:
            task_list.append(state.workstation_name)
        task_list.append("END_WS")
        print(task_list)

        for goal in task_list:
            print("Going to: {}".format(goal))
            self.send_goal("TEST_GOAL") 
                    
        #TODo: Respond to refbox that test is finished and shut down script!!!!! Otherwise it will keep looping.

    def run(self):
        rate = rospy.Rate(2)
        while not rospy.is_shutdown():
            try:
                self.robot_state.sender.header.stamp = rospy.Time.now()
                self.robot_state.sender.header.stamp = rospy.Time.now()
                self.robot_state.pose.x = 0.0 #robot.getPose().x (for example)
                self.robot_state.pose.y = 0.0 #robot.getPose().y (for example)
                self.robot_state.pose.theta = 0.0 #robot.getPose().a (for example)
                self.robot_state.path.header.stamp = rospy.Time.now()
                self.robot_state.path.header.frame_id = "map"
                self.robot_state.path.poses = [] # An array of poses (PoseStamped) that represents a Path for a robot to follow
                self.state_pub.publish(self.robot_state)
                rate.sleep()
            except rospy.ROSInterruptException:
                break
        
if __name__ == "__main__":
    run_class = SendTableGoal()
    run_class.run()
