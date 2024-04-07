import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
# URDF 파일 경로 설정
urdf_file = 'urdf_robot.urdf'
package_description = 'urdf_robot'

    # URDF 파일 경로 설정
urdf_path = os.path.join(get_package_share_directory(package_description), "urdf", urdf_file)


# URDF 파일 읽기
try:
    with open(urdf_path, 'r') as file:
        urdf_content = file.read()
        print("URDF 파일 내용:\n", urdf_content)
except FileNotFoundError:
    print("URDF 파일을 찾을 수 없습니다.")