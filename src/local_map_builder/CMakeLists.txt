cmake_minimum_required(VERSION 2.8.3 FATAL_ERROR)

if(NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE Release)
endif()

project(local_map_builder)
find_package(octomap REQUIRED)

find_package(catkin REQUIRED COMPONENTS 
  3d_navigation 
  roscpp
  rospy
  std_msgs
  geometry_msgs
  nav_msgs
  octomap_msgs
  tf
)

include_directories(include/${CMAKE_PROJECT_NAME})
include_directories(${catkin_INCLUDE_DIRS})

add_library(local_mapper SHARED src/local_map_builder.cpp)
target_link_libraries(local_mapper ${OCTOMAP_LIBRARIES} ${catkin_LIBRARIES})

add_executable(local_mapper_node src/local_map_builder_node.cpp)
target_link_libraries(local_mapper_node local_mapper)
