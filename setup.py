#!/usr/bin/env python
# flake8: noqa

import os
from pip.req import parse_requirements
from setuptools import setup, find_packages


import a10_neutron_lbaas


def get_requires(rname='requirements.txt'):
    this_dir = os.path.realpath(os.path.dirname(__file__))
    fname = os.path.join(this_dir, rname)
    reqs = parse_requirements(fname)
    res = [str(ir.req) for ir in reqs]

    return res

setup(
    name = "a10-neutron-lbaas",
    version=a10_neutron_lbaas.__version__,
    packages = find_packages(),

    author = "A10 Networks",
    author_email = "dougw@a10networks.com",
    description = "A10 Networks Openstack LBaaS Driver Middleware",
    license = "Apache",
    keywords = "a10 axapi acos adc slb load balancer openstack neutron lbaas",
    url = "https://github.com/a10networks/a10-neutron-lbaas",

    long_description = open('README.md').read(),

    classifiers = [
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet',
    ],

    install_requires=get_requires()
)
