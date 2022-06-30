import sys
import argparse
import pathlib

from jupyter_core.paths import jupyter_config_path
from traitlets.config.manager import BaseJSONConfigManager


def main():
    parser = argparse.ArgumentParser(
        description="nb_conda_store_kernels install and uninstall"
    )
    parser.add_argument(
        "--enable",
        action="store_true",
        help="Enable nb_conda_store_kernels kernel manager",
    )
    parser.add_argument(
        "--disable",
        action="store_true",
        help="Disable nb_conda_store_kernels kernel manager",
    )
    args = parser.parse_args()

    config_path = pathlib.Path(jupyter_config_path()[0])

    if args.enable and args.disable:
        print("Cannot have both enable and disable options active")
        sys.exit(1)
    elif args.enable:
        enable(config_path)
    elif args.disable:
        disable(config_path)


KERNEL_MANAGER = "nb_conda_store_kernels.manager.CondaStoreKernelSpecManager"


def enable(config_path: pathlib.Path):
    cfg = BaseJSONConfigManager(config_dir=str(config_path))
    data = cfg.get("jupyter_config")
    data["JupyterApp"] = data.get("JupyterApp", {})
    data["JupyterApp"]["kernel_spec_manager_class"] = KERNEL_MANAGER
    cfg.set("jupyter_config", data)


def disable(config_path: pathlib.Path):
    cfg = BaseJSONConfigManager(config_dir=str(config_path))
    data = cfg.get("jupyter_config")
    if data.get("JupyterApp", {}).get("kernel_spec_manager_class") == KERNEL_MANAGER:
        del data["JupyterApp"]["kernel_spec_manager_class"]
    cfg.set("jupyter_config", data)


if __name__ == "__main__":
    main()
