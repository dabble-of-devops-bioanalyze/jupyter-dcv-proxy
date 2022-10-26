from setuptools import setup, find_packages
import setuptools
import versioneer

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jupyter-dcv-proxy",
    url="https://github.com/dabble-of-devops-bioanalyze/jupyter-dcv-proxy",
    author="Jillian Rowe",
    description="Jupyter extension to proxy DCV",
    license="Apache Software License 2.0",
    long_description=long_description,
    packages=setuptools.find_packages(),
    keywords=["Jupyter"],
    classifiers=["Framework :: Jupyter"],
    scripts=["jupyter_dcv_proxy/run-dcv-user-session.sh"],
    install_requires=["jupyter-server-proxy>=3.2.0"],
    entry_points={"jupyter_serverproxy_servers": ["dcv = jupyter_dcv_proxy:setup_dcv"]},
    package_data={
        "jupyter_dcv_proxy": ["icons/dcv.svg"],
    },
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
)
