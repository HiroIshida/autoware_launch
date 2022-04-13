# Copyright 2021 Tier IV, Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import launch
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import ComposableNodeContainer
from launch_ros.actions import Node
from launch_ros.descriptions import ComposableNode


# ishida debug launch
def generate_launch_description():

    node1 = Node(
        package='mission_planner',
        name='mission_planner',
        executable='mission_planner',
        remappings=[
            ('input/vector_map', '/map/vector_map'),
            ('input/goal_pose', '/planning/mission_planning/goal'),
            ('input/checkpoint', '/planning/mission_planning/checkpoint'),
            ('output/route', '/planning/mission_planning/route'),
            ('visualization_topic_name',
             '/planning/mission_planning/route_marker'),
        ],
        parameters=[
            {
                'map_frame': 'map',
                'base_link_frame': 'base_link',
            }
        ],
        prefix=['xterm -e gdb -ex run --args'],
    )

    node2 = Node(
        package='mission_planner',
        name='goal_pose_visualizer',
        executable='goal_pose_visualizer_node',
        remappings=[
            ('input/route', '/planning/mission_planning/route'),
            ('output/goal_pose',
             '/planning/mission_planning/echo_back_goal_pose'),
        ],
    )
    return launch.LaunchDescription([
        node1,
    ])
