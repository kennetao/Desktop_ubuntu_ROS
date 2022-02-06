cmake_minimum_required(VERSION 2.8.3)
project(xbox_360_pad)

## Find catkin macros and libraries
find_package(catkin REQUIRED COMPONENTS
  rospy
  message_generation
)


## Generate messages in the 'msg' folder
 add_message_files(
   FILES
   xbox_360_pad.msg 
)


## Generate added messages and services with any dependencies listed here
 generate_messages(
   DEPENDENCIES
 )


###################################
## catkin specific configuration ##
###################################
catkin_package(
  LIBRARIES xbox_360_pad
  CATKIN_DEPENDS rospy message_runtime
  DEPENDS system_lib
)

###########
## Build ##
###########

## Specify additional locations of header files
## Your package locations should be listed before other locations
include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)


