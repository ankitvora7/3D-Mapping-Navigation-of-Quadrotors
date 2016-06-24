#!/usr/bin/env python
import rospy
from moveit_msgs.msg import PlanningScene
from octomap_msgs.msg import Octomap
class PublishPlanningScene:
    def __init__(self):
        self.octo_msgs_sub = rospy.Subscriber('/octomap_full',Octomap,self.cb)
        self.planning_scene_pub = rospy.Publisher('/planning_scene',PlanningScene,queue_size=10)
        self.scene_now = PlanningScene()
    def cb(self,octo_msg):
        data = octo_msg
        self.scene_now.world.octomap.octomap = data
        self.planning_scene_pub.publish(self.scene_now)
if __name__ == '__main__':
    rospy.init_node('octomapWorld_publisher')
    pubPS = PublishPlanningScene()
    print "[octomapWorld_publisher]: Publishing planning scene"
    rospy.spin()
