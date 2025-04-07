FROM quay.io/jupyter/scipy-notebook:2025-04-04
LABEL authors="Tim Dudgeon"

RUN mamba install --yes \
    chemicalite && \
    mamba clean --all -f -y && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"