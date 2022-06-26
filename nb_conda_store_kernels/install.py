import pathlib

from traitlets.config.manager import BaseJSONConfigManager


def install():
    jupyter_config_path = pathlib.Path("~/.jupyter").expanduser()
    cfg = BaseJSONConfigManager(config_dir=str(jupyter_config_path))
    cfg.set(
        "jupyter_config",
        {
            "JupyterApp": {
                "kernel_spec_manager_class": "nb_conda_store_kernels.manager.CondaStoreKernelSpecManager"
            }
        },
    )


if __name__ == "__main__":
    install()
