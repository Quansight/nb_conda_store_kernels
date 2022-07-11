# nb_conda_store_kernels

This extension enables a Jupyter Notebook or JupyterLab application to access environments stored in Conda-Store and run kernels for Python, R, and other languages. When a kernel from an external environment is selected, the environment is downloaded, extracted, conda environment is automatically activated, and finally the kernel is launched. This package was heavily inspired by [nb_conda_kernels](https://github.com/Anaconda-Platform/nb_conda_kernels).

Any notebook launched via a `nb_conda_store_kernel` kernel will have
notebook metadata about the environment used. This provides a powerful
mechanism for running the notebook later in a reproducible way.

```
{
    ...,
    "kernelspec": {
        ...,
        "name": "conda-store://<namespace>/<environment_name>:<build-id>",
        ...,
    },
    ...
}
```

The package works by defining a custom KernelSpecManager that calls the Conda-Store REST API for available conda environments with required packages. It dynamically modifies each KernelSpec so that it can be properly run from the notebook environment. When you create a new notebook, these modified kernels will be made available in the selection list. Additionally without [Conda-Pack](https://conda.github.io/conda-pack/)

## Usage

This package does not need `pip` or `conda` to run properly but
currently only run on Linux. It should be installed in the environment
from which you run Jupyter Notebook or JupyterLab. It is recommended
for install `nb_conda_store_kernsl` via Conda due to activation hooks
which simplify the installation but there is no strong reason to use
conda.

```shell
conda install -c conda-forge nb_conda_store_kernels
```

Alternatively `pip` works as well but requires one additional step.

```shell
pip install nb_conda_store_kernels
python -m nb_conda_store_kernels.install --enable
# python -m nb_conda_store_kernels.install --disable # to disable
```

`python -m nb_conda_store_kernels.install --enable` simply modifies a
single jupyter setting. If that did not work (it should and is a bug
if not) you need to add the following setting to `jupyter_config.py`.

```shell
mkdir ~/.jupyter
echo 'c.JupyterApp.kernel_spec_manager_class = "nb_conda_store_kernels.manager.CondaStoreKernelSpecManager"' > ~/.jupyter/jupyter_conifg.py
```

In order to `nb_conda_store_kernels` to connect properly to
Conda-Store it needs several environment variables set. Under the
covers `conda-store` the client is being using and has [detailed
documentation](https://github.com/quansight/conda-store/conda-store)
on configuration.

```
export CONDA_STORE_URL=http(s)://...
export CONDA_STORE_AUTH=none|basic|token
# export CONDA_STORE_USERNAME=... # using basic auth 
# export CONDA_STORE_PASSWORD=... # using basic auth
# export CONDA_STORE_TOKEN=...    # using token auth
```

Finally launch JupyterLab!

```shell
jupyter lab
```

### Connecting to existing conda-store server

Visit conda-store server you are using and get a token for your given
user via vising the `/user` endpoint after you login.

```shell
docker run -p 8888:8888 -e CONDA_STORE_TOKEN=... quansight/nb-conda-store-kernels:v0.1.5
```

### Use with nbconvert, voila, papermill,...

Since `nb_conda_store_kernels` uses the `conda-store` client under the
covers these use cases are supported by the client with proper
environment variables being set. There are plans to extend other tools
to use Conda-Store.

```shell
conda-store run namespace/environment -- python -c "print('Hello, Conda-Store!')"
```

## Development

Start Conda-Store server

```
docker-compose up --build
jupyter lab
```

Login to Conda-Store at [localhost:5000](http://localhost:5000) and
create a new environment.
