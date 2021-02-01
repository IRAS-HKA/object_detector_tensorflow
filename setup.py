import os
from glob import glob
from setuptools import setup

package_name = 'object_detector_tensorflow'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'config'), glob('config/*.yaml'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Andreas Zachariae',
    maintainer_email='andreas.zachariae@hs-karlsruhe.de',
    description='Python based ROS Nodes for TensorFlow Object Detection Inference',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'continuous_detection_node = object_detector_tensorflow.continuous_detection_node:main',
            'detection_node = object_detector_tensorflow.detection_node:main',
            'test_node = object_detector_tensorflow.client:main',
        ],
    },
)
