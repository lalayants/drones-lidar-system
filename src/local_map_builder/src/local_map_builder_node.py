#!/bin/python3

import rospy
import numpy
import sys
import time

import os

print(os.getcwd())
from local_map_builder.msg import costmap_3d
from sensor_msgs.msg import Range

# Node example class.
class LocalMapBuilder():
    def __init__(self):
        self._local_map_publisher = rospy.Publisher('/obstacle_map', costmap_3d, queue_size=2)
        self._lidar_listener_forward = rospy.Subscriber('vl53l1x/range', Range, self.forward_callback)
        
    def forward_callback(self, msg):
        print('Forward: ', msg.range)
    
    def publish_map(self):
        print('Publish')


if __name__ == '__main__':
    rospy.init_node('local_map_builder')
    rate = rospy.Rate(10)
    try:
        lmp = LocalMapBuilder()
        while not rospy.is_shutdown():
            lmp.publish_map()
            rate.sleep()
    except rospy.ROSInterruptException: pass