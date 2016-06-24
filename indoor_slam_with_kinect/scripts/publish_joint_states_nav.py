#!/usr/bin/env python
import rospy
from nav_msgs.msg import Odometry
from sensor_msgs.msg import JointState
class PublishJointStates:
    def __init__(self):
        self.nav_msgs_odom_sub = rospy.Subscriber('/ground_truth/state',Odometry,self.cb)
        self.joint_state_pub = rospy.Publisher('joint_states',JointState,queue_size=10)
        self.joint_now = JointState()
    def cb(self,odom_state):
        x = odom_state.pose.pose.position.x
        y = odom_state.pose.pose.position.y
        z = odom_state.pose.pose.position.z
        self.joint_now.position = [x, y, z]
        self.joint_now.header.frame_id = '/map'
        self.joint_now.name = ['virtual_joint', 'virtual_joint', 'virtual_joint']
        self.joint_state_pub.publish(self.joint_now)
if __name__ == '__main__':
    rospy.init_node('publisher_joint_states')
    pubJS = PublishJointStates()
    print "[Publisher_joint_states]: Publishing joint state"
    rospy.spin()
