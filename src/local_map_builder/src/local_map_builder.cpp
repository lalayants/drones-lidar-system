#include "local_map_builder.h"

LocalMapBuilder::LocalMapBuilder(ros::NodeHandle & _node_handler){
    ROS_INFO("LocalMapBuilder creation started");
    map_listener = node_handler.subscribe("/vl53l1x/range", 10, &LocalMapBuilder::set_forward_callback, this);
}

LocalMapBuilder::~LocalMapBuilder()
{ }

void LocalMapBuilder::set_forward_callback(const geometry_msgs::Point::ConstPtr & msg){
    ROS_INFO("Lidar: %f\n", msg->range);
}
