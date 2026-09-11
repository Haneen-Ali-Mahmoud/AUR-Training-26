import os

from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():

    package_name = 'Turtle'

    config_file = os.path.join(
        get_package_share_directory(package_name),
        'config',
        'params.yaml'
    )

    turtlesim_node = Node(
        package='turtlesim',
        executable='turtlesim_node',
        name='turtlesim'
    )

    goal_node = Node(
        package='Turtle',
        executable='goal_to_goal',
        name='goal_to_goal',
        parameters=[config_file]
    )

    Turtle_client = Node(
        package='Turtle',
        executable='Turtle_client',
        name='Turtle_client')

    return LaunchDescription([turtlesim_node, goal_node, Turtle_client])