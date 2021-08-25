from setuptools import setup, find_packages


setup(
    name='grecka',
    version='0.0.1',
    description='Greek to greeklish transformer',
    install_requires=[],
    tests_require=[
    ],
    setup_requires=[
    ],
    extras_require={
    },
    test_suite='nose.collector',
    packages=find_packages(exclude=['test']),
    include_package_data=True,
)
