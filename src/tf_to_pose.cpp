#include <ros/ros.h>
#include <tf2_ros/transform_listener.h>
#include <geometry_msgs/TransformStamped.h>
#include <geometry_msgs/PoseWithCovarianceStamped.h>

/*
cov value    | confidence
-------------------------
0.01         | High
0.1          | Medium
1            | Low
10           | Fail
*/

int main(int argc, char** argv){
  ros::init(argc, argv, "tf_to_pose");

  ros::NodeHandle node;

  ros::Publisher pose_pub = 
    node.advertise<geometry_msgs::PoseWithCovarianceStamped>("out_pose", 10);

  tf2_ros::Buffer tfBuffer;
  tf2_ros::TransformListener tfListener(tfBuffer);

  double cov_pose;
  double cov_twist;

  node.param("cov_pose", cov_pose, 0.1);
  node.param("cov_twist", cov_twist, 0.1);

  ros::Rate rate(30.0);
  while (node.ok()){
    geometry_msgs::TransformStamped transformStamped;
    try{
      transformStamped = tfBuffer.lookupTransform("target_frame", "source_frame",
                               ros::Time(0));
    }
    catch (tf2::TransformException &ex) {
      ROS_WARN("%s",ex.what());
      ros::Duration(1.0).sleep();
      continue;
    }

    geometry_msgs::PoseWithCovarianceStamped pose_msg;
    pose_msg.header.stamp = transformStamped.header.stamp;
    pose_msg.pose.pose.position.x = transformStamped.transform.translation.x;
    pose_msg.pose.pose.position.y = transformStamped.transform.translation.y;
    pose_msg.pose.pose.position.z = transformStamped.transform.translation.z;
    pose_msg.pose.pose.orientation = transformStamped.transform.rotation;


    pose_msg.pose.covariance = {cov_pose, 0, 0, 0, 0, 0, 
                                0, cov_pose, 0, 0, 0, 0, 
                                0, 0, cov_pose, 0, 0, 0, 
                                0, 0, 0, cov_twist, 0, 0, 
                                0, 0, 0, 0, cov_twist, 0, 
                                0, 0, 0, 0, 0, cov_twist}; 

    pose_pub.publish(pose_msg);

    rate.sleep();
  }
  return 0;
};

