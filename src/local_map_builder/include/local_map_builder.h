#pragma once

#include <octomap/octomap.h>
#include <iostream>
#include <ros/ros.h>

#include "sensor_msgs/Range.h"

#include "octomap_msgs/Octomap.h"
#include "octomap_msgs/conversions.h"


class LocalMapBuilder {
public:
    LocalMapBuilder(ros::NodeHandle & _node_handler);
	~LocalMapBuilder();
}