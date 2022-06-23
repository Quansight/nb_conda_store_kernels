{
  description = "nb_conda_store_kernels";

  inputs = {
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem
      (system:
        let pkgs = nixpkgs.legacyPackages.${system};
            pythonPackages = pkgs.python3Packages;
            nb_conda_store_kernels = pythonPackages.buildPythonPackage {
              pname = "nb_conda_store_kernels";
              version = "0.1.0";

              src = ./.;

              propagatedBuildInputs = [
                pythonPackages.jupyter-client
                pythonPackages.traitlets
              ];
            };
        in
        {
          devShell = pkgs.mkShell {
            buildInputs = [
              nb_conda_store_kernels
              pythonPackages.jupyterlab
            ];
          };
        }
      );
}
