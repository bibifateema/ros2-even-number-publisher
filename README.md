# ROS 2 Even Number Publisher

A simple ROS 2 Python publisher that publishes
even numbers using a timer.

## Features
- Publishes even numbers starting from 2
- Uses ROS 2 Python (rclpy)
- Publishes through Int32 message
- Timer-based publishing (1 second interval)

## Topic
/even_numbers

## Message Type
std_msgs/msg/Int32

## Run
```bash
ros2 run even_number_pkg even_publisher
