# nb_conda_store_kernels

## Development

Start Conda-Store server

```
docker-compose up --build
nix develop
python -m nb_conda_store_kernels.install
jupyter lab
```

Launch one of the two kernels
