# -*- coding: utf-8 -*-
try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='cephci',
    version='0.1',
    description='Ceph CI tests that run in jenkins using openstack provider',
    author='Vasu Kulkarni',
    author_email='vasu@redhat.com',
    install_requires=[
        'apache-libcloud',
        'docopt==0.6.2',
        'gevent==1.4.0',
        'reportportal-client==3.2.0',
        'requests==2.21.0',
        'paramiko==2.4.2',
        'pyyaml>=4.2b1',
        'jinja2==2.10.1',
        'junitparser==1.4.0'
    ],
    zip_safe=True,
    include_package_data=True,
    packages=find_packages(exclude=['ez_setup']),
)
