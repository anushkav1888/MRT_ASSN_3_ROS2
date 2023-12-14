from setuptools import find_packages, setup

package_name = 'package'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'       
                       'sensor_msgs',
                       'cv_bridge',],
    zip_safe=True,
    maintainer='anushka',
    maintainer_email='anushkav1888@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'pub = package.pub:main',
            'sub = package.sub:main',
        ],
    },
)
