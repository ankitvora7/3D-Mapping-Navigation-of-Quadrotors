#!/usr/bin/env python
from geometry_msgs.msg import Pose2D, PoseStamped
import tf
import rospy
def goal_cb(msg):
    rec_goal = msg
    new_goal = rec_goal
    goal_2D_pub.publish(new_goal)
goal_2D_pub = rospy.Publisher('goal',PoseStamped,queue_size=5)
goal_stamped_sub = rospy.Subscriber('move_base_simple/goal',PoseStamped,goal_cb)

if __name__ == '__main__':
    rospy.init_node('convert_goal')
    print "[convert_goal] : Initialized"
    while not rospy.is_shutdown():
        continue
