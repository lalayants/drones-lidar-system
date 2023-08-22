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
    # Must have __init__(self) function for a class, similar to a C++ class constructor.
    def __init__(self):
        self.t = time.time()
        # Get the ~private namespace parameters from command line or launch file.
        # init_message = rospy.get_param('~message', 'hello')
        # rate = float(rospy.get_param('~rate', '1.0'))
        # topic = rospy.get_param('~topic', 'chatter')
        # rospy.loginfo('rate = %d', rate)
        # rospy.loginfo('topic = %s', topic)
        
        self._local_map_publisher = rospy.Publisher('/obstacle_map', costmap_3d, queue_size=2)
        self._lidar_listener_forward = rospy.Subscriber('vl53l1x/range', Range, self.forward_callback)
        
        
        # Main while loop.
        # while not rospy.is_shutdown():
        #     # Fill in custom message variables with values from dynamic reconfigure server.
        #     msg.message = self.message
        #     msg.a = self.a
        #     msg.b = self.b
        #     # Publish our custom message.
        #     pub.publish(msg)
        #     # Sleep for a while before publishing new messages. Division is so rate != period.
        #     if rate:
        #         rospy.sleep(1/rate)
        #     else:
        #         rospy.sleep(1.0)
    def forward_callback(self, msg):
        print('Forward: ', msg.range)
    
    def publish_map(self):
        
        print('Publish', time.time() - self.t)
        self.t = time.time()


# Main function.
if __name__ == '__main__':
    # Initialize the node and name it.
    rospy.init_node('local_map_builder')
    rate = rospy.Rate(1)
    # Go to class functions that do all the heavy lifting. Do error checking.
    try:
        lmp = LocalMapBuilder()
        while not rospy.is_shutdown():
            rospy.spin()
            rate.sleep()
    except rospy.ROSInterruptException: pass