from jupyter_client.manager import KernelManager

from nb_conda_store_kernels.manager import CondaStoreKernelSpecManager


class CondaKernelProvider:
    id = "conda-store"

    def __init__(self):
        self.cksm = CondaStoreKernelSpecManager(conda_only=True)

    def find_kernels(self):
        for name, data in self.cksm.get_all_specs().items():
            yield name, data["spec"]

    def make_manager(self, name):
        return KernelManager(kernel_spec_manager=self.cksm, kernel_name=name)
