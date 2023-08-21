#include "../include/local_map_builder.h"

int main(int _argc, char **_argv){
    srand((unsigned int) time(0));
    ros::init(_argc, _argv, "local_map_builder");
    ros::NodeHandle node_handler;
    ros::Rate rate(10);
    ROS_INFO("Creating\n");
    LocalMapBuilder builder(node_handler);
    while(ros::ok){
        ros::spinOnce();
        rate.sleep();
    }
}