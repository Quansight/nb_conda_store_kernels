from jupyter_client.kernelspec import KernelSpecManager, KernelSpec, NoSuchKernel

from traitlets import Bool, Unicode, TraitError, validate


class CondaStoreKernelSpecManager(KernelSpecManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.log.info("[nb_conda_store_kernels] enabled")

    KERNEL_SPECS = {
        'datascience': KernelSpec(
            display_name="datascience-test",
            argv=["false"],
            metadata={
                "conda_store": "idtodatascience",
                "resource_dir": "/path/to/datascience",
            },
        ),
        'webdev': KernelSpec(
            display_name="webdev-test",
            argv=["false"],
            metadata={
                "conda_store": "idtowebdev",
                "resource_dir": "/path/to/webdev",
            },
        ),
    }

    def find_kernel_specs(self):
        return {name: spec.metadata['resource_dir'] for name, spec in self.KERNEL_SPECS.items()}

    def get_kernel_spec(self, kernel_name):
        return self.KERNEL_SPECS[kernel_name]

    def get_all_specs(self):
        return {name: {'resource_dir': spec.metadata['resource_dir'], 'spec': spec.to_dict()} for name, spec in self.KERNEL_SPECS.items()}

    def remove_kernel_spec(self, name):
        pass
