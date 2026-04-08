from setuptools import setup

package_name = 'autonomous_exploration'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='abd',
    maintainer_email='abd@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'control = autonomous_exploration.control:main',
            'my_control = autonomous_exploration.my_control:main',
            'nav_to_pose = autonomous_exploration.nav_to_pose:main',
            'example_navigation = autonomous_exploration.example_navigation:main',
            'sanitize = autonomous_exploration.sanitize:main',
            'heatmap = autonomous_exploration.heatmap:main'


        ],
    },
)
