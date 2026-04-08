from setuptools import find_packages, setup

package_name = 'my_robot_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='student',
    maintainer_email='student@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "velocity_control = my_robot_controller.velocity_control:main",
            "velocity_control_FSM = my_robot_controller.velocity_control_FSM:main",
            "example_navigation = my_robot_controller.example_navigation:main",
            "nave_to_pose = my_robot_controller.nave_to_pose:main"
        ],
    },
)
