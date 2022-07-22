#!/usr/bin/env python3

from pkg_resources import parse_requirements
from setuptools import find_packages, setup

PACKAGE_NAME = "cad_reflective_cns"

with open("requirements/production.txt") as f:
    requirements = parse_requirements(f)

    dependencies = [
        *[str(req.req) for req in requirements]
    ]

setup(
    name=PACKAGE_NAME,
    use_scm_version=dict(write_to=f"{PACKAGE_NAME}/version.py"),
    packages=find_packages(),
    install_requires=dependencies,
    setup_requires=["setuptools_scm"],
)

