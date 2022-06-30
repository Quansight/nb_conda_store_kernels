import tempfile
import os

from jupyter_client.kernelspec import KernelSpecManager, KernelSpec
from jupyter_client.utils import run_sync
from traitlets import Bool, Unicode
from conda_store import api


class CondaStoreKernelSpecManager(KernelSpecManager):
    """A custom KernelSpecManager able to search conda-store for
    environments and create kernelspecs for them.
    """

    conda_store_url = Unicode(
        os.environ.get("CONDA_STORE_URL", "http://localhost:5000/"),
        help="Base prefix URL for connecting to conda-store cluster",
        config=True,
    )

    conda_store_verify_ssl = Bool(
        "CONDA_STORE_NO_VERIFY" not in os.environ,
        help="Verify all TLS connections",
        config=True,
    )

    conda_store_auth = Unicode(
        os.environ.get("CONDA_STORE_AUTH", "none"),
        help="Authentication type to use with Conda-Store. Available options are none, token, and basic",
        config=True,
    )

    name_format = Unicode(
        "{namespace}/{name}:{build}",
        config=True,
        help="""String name format; available field names within the string:
        '{namespace}' = Namespace for particular environment
        '{name}' = Environment name
        '{build}' = Build Id for particular environment
        """,
    )

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.log.info("[nb_conda_store_kernels] enabled")

    @property
    def kernel_specs(self):
        return run_sync(self._kernel_specs)()

    async def _kernel_specs(self):
        async with api.CondaStoreAPI(
            conda_store_url=self.conda_store_url,
            auth=self.conda_store_auth,
            verify_ssl=self.conda_store_verify_ssl,
        ) as conda_store_api:
            environments = await conda_store_api.list_environments(
                status="COMPLETED",
                artifact="CONDA_PACK",
                packages=["ipykernel"],
            )

        kernel_specs = {}
        for environment in environments:
            namespace = environment["namespace"]["name"]
            name = environment["name"]
            build = environment["current_build_id"]

            display_name = self.name_format.format(
                namespace=namespace, name=name, build=build
            )
            kernel_specs[f"conda-store://{namespace}/{name}:{build}"] = KernelSpec(
                display_name=display_name,
                argv=[
                    "conda-store",
                    "run",
                    str(build),
                    "--",
                    "python",
                    "-m",
                    "IPython",
                    "kernel",
                    "-f",
                    "{connection_file}",
                ],
                language="python",
                resource_dir=os.path.join(
                    tempfile.gettempdir(),
                    "conda-store",
                    str(build),
                ),
                metadata={},
            )
        return kernel_specs

    def find_kernel_specs(self):
        return {name: spec.resource_dir for name, spec in self.kernel_specs.items()}

    def get_kernel_spec(self, kernel_name):
        return self.kernel_specs[kernel_name]

    def get_all_specs(self):
        return {
            name: {"resource_dir": spec.resource_dir, "spec": spec.to_dict()}
            for name, spec in self.kernel_specs.items()
        }

    def remove_kernel_spec(self, name):
        pass
