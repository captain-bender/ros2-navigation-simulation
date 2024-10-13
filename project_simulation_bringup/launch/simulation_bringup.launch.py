from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch_xml.launch_description_sources import XMLLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    # Get the directory of the turtlebot3_gazebo package
    turtlebot3_gazebo_dir = get_package_share_directory('turtlebot3_gazebo')

    # Path to the original XML launch file
    xml_launch_file = os.path.join(turtlebot3_gazebo_dir, 'launch', 'main_turtlebot3_lab.launch.xml')

    # Include the XML launch description
    return LaunchDescription([
        IncludeLaunchDescription(
            XMLLaunchDescriptionSource(xml_launch_file)
        )
    ])

