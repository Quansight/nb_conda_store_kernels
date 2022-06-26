FROM --platform=linux/amd64 condaforge/mambaforge

COPY environment.yaml /opt/nb_conda_store_kernels/environment.yaml

ENV PATH=/opt/conda/condabin:/opt/conda/envs/nb_conda_store_kernels/bin:/opt/conda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH}

RUN mamba env create -f /opt/nb_conda_store_kernels/environment.yaml

COPY . /opt/nb_conda_store_kernels/

RUN cd /opt/nb_conda_store_kernels && \
    pip install -e .

RUN mkdir -p /home/jovyan && \
    mkdir -p /home/jovyan/.jupyter && \
    cp /opt/nb_conda_store_kernels/tests/assets/jupyter_config.py /home/jovyan/.jupyter/jupyter_config.py && \
    chown -R 1000:1000 /home/jovyan

WORKDIR /home/jovyan
