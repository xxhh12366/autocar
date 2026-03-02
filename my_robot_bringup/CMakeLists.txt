cmake_minimum_required(VERSION 3.8)
project(my_robot_bringup)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)

# 安装静态资源（launch/config/worlds）到share目录
install(
  DIRECTORY launch config worlds scripts
  DESTINATION share/${PROJECT_NAME}/
)

# 单独安装Python脚本到lib目录（ROS 2要求可执行脚本放在这里）
install(PROGRAMS
  scripts/get_robot_pose.py  # 指定具体的脚本文件
  DESTINATION lib/${PROJECT_NAME}  # 安装到lib/my_robot_bringup目录
)

ament_package()
