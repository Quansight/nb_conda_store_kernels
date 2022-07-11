FROM --platform=linux/amd64 condaforge/mambaforge

COPY environment.yaml /opt/nb_conda_store_kernels/environment.yaml

ENV PATH=/opt/conda/condabin:/opt/conda/envs/nb_conda_store_kernels/bin:/opt/conda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH}

RUN mamba env create -f /opt/nb_conda_store_kernels/environment.yaml

COPY . /opt/nb_conda_store_kernels/

RUN cd /opt/nb_conda_store_kernels && \
    pip install -e .

ARG UID=1000
ARG GID=1000
ARG USER=jovyan

RUN useradd -l -m -s /bin/bash -N -u "${UID}" "${USER}" && \
    mkdir -p /home/jovyan/.jupyter && \
    cp /opt/nb_conda_store_kernels/tests/assets/jupyter_config.py /home/jovyan/.jupyter/jupyter_config.py

WORKDIR /home/${USER}
USER ${UID}

ENV CONDA_STORE_AUTH=token
ENV CONDA_STORE_URL=https://conda.store

CMD ["jupyter", "lab", "--ip=0.0.0.0"]