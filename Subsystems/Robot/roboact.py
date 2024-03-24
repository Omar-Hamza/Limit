import sys
import time
import math
from gazebo_msgs.msg import ModelState
from gazebo_msgs.srv import SetModelState
import rospy

def set_joint_position(joint_name, position):
    # Create a service proxy for setting the robot's joint position
    set_model_state = rospy.ServiceProxy('/gazebo/set_model_state', SetModelState)
    # Create a ModelState message to set the joint position
    model_state = ModelState()
    model_state.model_name = 'youbot'  # Replace 'robot' with the name of your robot model
    model_state.pose.position.x = 0.0
    model_state.pose.position.y = 0.0
    model_state.pose.position.z = 0.0
    model_state.pose.orientation.x = 0.0
    model_state.pose.orientation.y = 0.0
    model_state.pose.orientation.z = 0.0
    model_state.pose.orientation.w = 1.0
    model_state.twist.linear.x = 0.0
    model_state.twist.linear.y = 0.0
    model_state.twist.linear.z = 0.0
    model_state.twist.angular.x = 0.0
    model_state.twist.angular.y = 0.0
    model_state.twist.angular.z = 0.0
    model_state.reference_frame = ''
    # Set joint position
    model_state.pose.position.z = position
    # Call the service to set the model state
    resp = set_model_state(model_state)

def main():
    # Initialize the ROS node
    rospy.init_node('gazebo_robot_controller')

    # Wait for the set_model_state service to become available
    rospy.wait_for_service('/gazebo/set_model_state')

    # Control loop
    while not rospy.is_shutdown():
        # Move the robot's joint sinusoidally
        for t in range(100):
            position = math.sin(2 * math.pi * t / 100.0)  # Sinusoidal motion
            set_joint_position('wheel_joint_fr', position)  # Replace 'joint_name' with the name of the joint you want to control
            time.sleep(0.1)  # Wait for 0.1 seconds between each position command

if __name__ == '__main__':
    main()
