import setuptools

setuptools.setup(
    name="nb_conda_store_kernels",
    version="0.1.0",
    url="https://github.com/Quansight/nb_conda_store_kernels",
    author="Quansight",
    description="Launch Jupyter kernels from Conda-Store",
    long_description=open('README.md').read(),
    packages=setuptools.find_packages(),
    include_package_data=True,
    zip_safe=False,
    entry_points={
        "jupyter_client.kernel_providers": [
            # The name before the '=' should match the id attribute
            'conda-store = nb_conda_store_kernels.discovery:CondaStoreKernelProvider',
        ]}
)
