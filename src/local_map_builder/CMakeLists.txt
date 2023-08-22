cmake_minimum_required(VERSION 2.8.3 FATAL_ERROR)

if(NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE Release)
endif()

project(local_map_builder)
find_package(octomap REQUIRED)

find_package(catkin REQUIRED COMPONENTS 
  roscpp
  rospy
  std_msgs
  message_generation
  geometry_msgs
  sensor_msgs
  octomap_msgs
  tf
)

include_directories(include/${CMAKE_PROJECT_NAME})
include_directories(${catkin_INCLUDE_DIRS})

add_library(local_map_builder SHARED src/local_map_builder.cpp)
target_link_libraries(local_map_builder ${OCTOMAP_LIBRARIES} ${catkin_LIBRARIES})

add_executable(local_map_builder_node src/local_map_builder_node.cpp)
target_link_libraries(local_map_builder_node local_map_builder)
