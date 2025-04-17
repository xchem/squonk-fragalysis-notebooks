FROM quay.io/jupyter/minimal-notebook:2025-04-14
LABEL authors="Max Winokan"

RUN mamba install --yes \
    chemicalite pdbfixer && \
    mamba clean --all -f -y && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

# Upgrade pip and install JupyterLab
RUN pip install --upgrade pip && pip install hippo-db syndirella
RUN python -c "import mrich; mrich.patch_rich_jupyter_margins()"
RUN git clone https://github.com/xchem/squonk-fragalysis-notebooks
RUN git clone https://github.com/xchem/fragalysis
WORKDIR "/home/${NB_USER}"/fragalysis
RUN pip install -e .

# Expose the port Jupyter uses
EXPOSE 8888

WORKDIR "/home/${NB_USER}"
# Start JupyterLab (or change to `jupyter notebook` if preferred)
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
