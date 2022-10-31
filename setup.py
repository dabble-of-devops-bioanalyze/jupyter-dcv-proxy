#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages
import versioneer

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

test_requirements = []

setup(
    author="Jillian Rowe",
    author_email="jillian@dabbleofdevops.com",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="Jupyter proxy extension to proxy a NICE DCV application.",
    install_requires=["jupyter-server-proxy>=3.2.0"],
    entry_points={"jupyter_serverproxy_servers": ["dcv = jupyter_dcv_proxy:setup_dcv"]},
    include_package_data=True,
    package_data={
        "jupyter_dcv_proxy": ["icons/dcv.svg", "run-dcv-user-session.sh"],
    },
    license="Apache Software License 2.0",
    long_description=readme + "\n\n" + history,
    keywords="jupyter_dcv_proxy",
    name="jupyter-dcv-proxy",
    packages=find_packages(include=["jupyter_dcv_proxy", "jupyter_dcv_proxy.*"]),
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/dabble-of-devops-bioanalyze/jupyter-dcv-proxy",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    zip_safe=False,
)
