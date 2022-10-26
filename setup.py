from setuptools import setup, find_packages
import setuptools
import versioneer

setuptools.setup(
    name="jupyter-dcv-proxy",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    url="https://github.com/dabble-of-devops-bioanalyze/jupyter-dcv-proxy",
    author="Jillian Rowe",
    description="Jupyter extension to proxy DCV",
    packages=setuptools.find_packages(),
    keywords=["Jupyter"],
    classifiers=["Framework :: Jupyter"],
    scripts=["jupyter_dcv_proxy/run-dcv-user-session.sh"],
    install_requires=["jupyter-server-proxy>=3.2.0"],
    entry_points={"jupyter_serverproxy_servers": ["dcv = jupyter_dcv_proxy:setup_dcv"]},
    package_data={
        "jupyter_dcv_proxy": ["icons/dcv.svg"],
    },
)
