# nb_conda_store_kernels

## Usage

Modify the jupyter configuration to enable `nb_conda_store_kernels` as
a kernel manager in `jupyter_config.py`. Several of the settings can
be configured via traitlets. However several will need to be set via
environment variables. 

```python
c.JupyterApp.kernel_spec_manager_class = "nb_conda_store_kernels.manager.CondaStoreKernelSpecManager"
c.CondaStoreKernelSpecManager.conda_store_url = "http://conda-store-server:5000/conda-store"
c.CondaStoreKernelSpecManager.conda_store_auth = "basic"
```

Environment variables which correspond to the environment variables
that [conda-store](https://github.com/quansight/conda-store) uses:
 - `CONDA_STORE_URL`
 - `CONDA_STORE_AUTH`
 - `CONDA_STORE_NO_VERIFY_SSL`
 - `CONDA_STORE_USERNAME`
 - `CONDA_STORE_PASSWORD`
 - `CONDA_STORE_TOKEN`

This package is heavily under development and much may change. If
configured properly environment should show up in ~10 second delays
from changes in the Conda-Store server.

## Development

Start Conda-Store server

```
docker-compose up --build
nix develop
python -m nb_conda_store_kernels.install
jupyter lab
```

Login to Conda-Store at [localhost:5000](http://localhost:5000) and
create a new environment.
