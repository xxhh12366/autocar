#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
import time

class RobotPoseMonitor(Node):
    def __init__(self):
        super().__init__('robot_pose_monitor')
        # 订阅Gazebo发布的机器人位姿话题（话题名和机器人名对应）
        self.subscription = self.create_subscription(
            PoseStamped,
            '/model/my_robot/pose',  # Gazebo默认发布的机器人位姿话题
            self.pose_callback,
            10)
        self.subscription  # 防止未使用变量警告
        self.last_print_time = time.time()  # 记录上次打印时间
        self.current_pose = None  # 存储最新位姿

    def pose_callback(self, msg):
        # 更新最新位姿
        self.current_pose = msg.pose
        # 每隔1秒打印一次
        if time.time() - self.last_print_time >= 1.0:
            self.print_pose()
            self.last_print_time = time.time()

    def print_pose(self):
        if self.current_pose is None:
            self.get_logger().warn("还未接收到小车位姿数据！")
            return
        # 提取坐标信息
        x = self.current_pose.position.x
        y = self.current_pose.position.y
        z = self.current_pose.position.z
        # 提取姿态（四元数），可选打印
        rx = self.current_pose.orientation.x
        ry = self.current_pose.orientation.y
        rz = self.current_pose.orientation.z
        rw = self.current_pose.orientation.w
        
        # 打印坐标（核心信息）
        self.get_logger().info(
            f"小车当前坐标 -> X: {x:.3f}, Y: {y:.3f}, Z: {z:.3f}"
        )
        # 可选：打印姿态四元数
        # self.get_logger().info(
        #     f"姿态四元数 -> X: {rx:.3f}, Y: {ry:.3f}, Z: {rz:.3f}, W: {rw:.3f}"
        # )

def main(args=None):
    rclpy.init(args=args)
    node = RobotPoseMonitor()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
