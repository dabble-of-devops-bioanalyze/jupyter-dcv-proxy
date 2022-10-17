# jupyter-dcv-proxy

**jupyter-dcv-proxy** provides Jupyter server and notebook extensions to proxy DCV.

This is useful for desktop only applications such as [QuPath](https://github.com/qupath/qupath)
and [CellProfiler](https://cellprofiler.org/).

## Installation

### Pre-reqs

Both DCV and Configurable HTTP Proxy must be installed and available in your PATH.

[Configurable HTTP Proxy](https://github.com/jupyterhub/configurable-http-proxy#install)
[DCV](https://docs.aws.amazon.com/dcv/latest/userguide/getting-started.html)

On many AWS systems, including [BioAnalyze HPC](https://hpc.bioanalyze.io/readme.html) these are already installed. It's
worth it to check first.

```bash
which configurable-http-proxy
which dcv
```

### Install jupyter-dcv-proxy

Install the library via `pip`:

```
pip install jupyter-dcv-proxy
```
