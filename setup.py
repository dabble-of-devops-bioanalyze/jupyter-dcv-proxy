import setuptools

setuptools.setup(
    name="jupyter-dcv-proxy",
    version='2.0.2',
    url="https://github.com/dabble-of-devops-bioanalyze/jupyter-dcv-proxy",
    author="Jillian Rowe",
    description="Jupyter extension to proxy DCV",
    packages=setuptools.find_packages(),
    keywords=['Jupyter'],
    classifiers=['Framework :: Jupyter'],
    install_requires=[
        'jupyter-server-proxy>=3.2.0'
    ],
    entry_points={
        'jupyter_serverproxy_servers': [
            'dcv = jupyter_dcv_proxy:setup_dcv'
        ]
    },
    package_data={
        'jupyter_dcv_proxy': ['icons/dcv.svg'],
    },
)
