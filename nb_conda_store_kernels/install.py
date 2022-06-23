import os
import sys
import pathlib

from jupyter_core.paths import jupyter_config_path
from traitlets.config.manager import BaseJSONConfigManager

JA = "JupyterApp"
NBA = "NotebookApp"
CKSM = "nb_conda_store_kernels.CondaStoreKernelSpecManager"
JKSM = "jupyter_client.kernelspec.KernelSpecManager"
KSMC = "kernel_spec_manager_class"
JCKP = "jupyter_client.kernel_providers"
NCKDCKP = "nb_conda_store_kernels.discovery:CondaStoreKernelProvider"
JC = "jupyter_config"
JNC = "jupyter_notebook_config"
ENDIS = ['disabled', 'enabled']


def install():
    jupyter_config_path = pathlib.Path("~/.jupyter").expanduser()
    cfg = BaseJSONConfigManager(config_dir=str(jupyter_config_path))
    cfg.set("jupyter_config", {
        "JupyterApp": {
            "kernel_spec_manager_class": "nb_conda_store_kernels.manager.CondaStoreKernelSpecManager"
        }
    })


if __name__ == "__main__":
    install()
