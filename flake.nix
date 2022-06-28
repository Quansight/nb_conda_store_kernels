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
        in
        {
          devShell = pkgs.mkShell {
            buildInputs = [
              pythonPackages.jupyterlab

              pythonPackages.pytest
              pythonPackages.black
              pythonPackages.flake8
              pythonPackages.build
              pythonPackages.setuptools

              pkgs.docker-compose
            ];
          };
        }
      );
}
