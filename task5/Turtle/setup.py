from setuptools import find_packages, setup

package_name = 'Turtle'

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
    maintainer='Jarvis',
    maintainer_email='haneenali46843@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'goal_to_goal = Turtle.goal_to_goal:main',
            'turtle_controller = Turtle.turtle_controller:main',
            'turtle_client = Turtle.Turtle_client:main',
        ],
    },
)
