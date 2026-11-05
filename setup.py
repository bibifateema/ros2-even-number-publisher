from setuptools import find_packages, setup

package_name = 'even_number_pkg'

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
    maintainer='bibifatema',
    maintainer_email='bibifatema1415@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [ 
                      'even_publisher = even_number_pkg.even_publisher:main',
                      'random_publisher = even_number_pkg.random_publisher:main',
        ],
    },
)
