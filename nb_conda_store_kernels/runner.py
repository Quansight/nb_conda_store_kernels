import sys


def execute_tarball(namespace: str, name: str, connection_file: str):
    print(
        f"[CondaStoreKernels] Executing {namespace}/{name} with file: {connection_file}"
    )


if __name__ == "__main__":
    namespace, name, connection_file = sys.argv[1:]
    execute_tarball(namespace, name, connection_file)
