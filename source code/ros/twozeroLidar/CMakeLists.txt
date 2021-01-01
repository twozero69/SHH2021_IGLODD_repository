cmake_minimum_required(VERSION 2.8.3)
project(twozeroLidar)

## Compile as C++11, supported in ROS Kinetic and newer
add_compile_options(-std=c++11)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  roscpp
  std_msgs
  pcl_ros
  sensor_msgs
  laser_geometry
  pcl_conversions
  nav_msgs
  tf
)

catkin_package(
  INCLUDE_DIRS include
# LIBRARIES twozeroLidar
  CATKIN_DEPENDS roscpp std_msgs pcl_ros sensor_msgs image_geometry laser_geometry nav_msgs tf
# DEPENDS system_lib
)

###########
## Build ##
###########

## Specify additional locations of header files
## Your package locations should be listed before other locations
#include_directories(include)
include_directories(
 include
  ${catkin_INCLUDE_DIRS}
)


## Declare a C++ executable
## With catkin_make all packages are built within a single CMake context
## The recommended prefix ensures that target names across packages don't collide
add_executable(${PROJECT_NAME} src/twozeroLidar.cpp)

## Specify libraries to link a library or executable target against
 target_link_libraries(${PROJECT_NAME}
   ${catkin_LIBRARIES}
 )


