cmake_minimum_required(VERSION 2.8.3)
project(qut10_jackal)

find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  roscpp
  rospy
  std_msgs
  tf2
  tf2_ros
  tf2_geometry_msgs
)
catkin_package(
  CATKIN_DEPENDS geometry_msgs roscpp rospy std_msgs tf2 tf2_ros
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

add_executable(tf_to_pose src/tf_to_pose.cpp)
target_link_libraries(tf_to_pose ${catkin_LIBRARIES})
if(catkin_EXPORTED_TARGETS)
  add_dependencies(tf_to_pose ${catkin_EXPORTED_TARGETS})
endif()


## Install C++ nodes
install(TARGETS tf_to_pose
  ARCHIVE DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
  LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
  RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)


## Install Other Resources
install(DIRECTORY launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})

install(DIRECTORY rviz
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})

