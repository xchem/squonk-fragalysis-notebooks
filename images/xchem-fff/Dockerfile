FROM quay.io/jupyter/minimal-notebook:2025-04-14
LABEL authors="Max Winokan"
    
# Upgrade pip and install JupyterLab
RUN pip install --upgrade pip && pip install hippo-db syndirella typer neo4j black gemmi

RUN mamba install --yes \
    chemicalite=2024.05.1 pdbfixer && \
    mamba clean --all -f -y && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

# patch rich
RUN python -c "import mrich; mrich.patch_rich_jupyter_margins()"

# notebooks
USER 0
RUN mkdir "/home/code" && chown ${NB_USER} "/home/code" && \
    sudo apt update && sudo apt install screen -y
USER ${NB_USER}
WORKDIR "/home/code"
RUN git clone https://github.com/xchem/squonk-fragalysis-notebooks && \
    mv squonk-fragalysis-notebooks templates && \
    cp templates/welcome.ipynb /home/${NB_USER}/welcome.ipynb && \
    mkdir /home/code/copy-to-startup && \
    cp templates/welcome.ipynb /home/code/copy-to-startup/welcome.ipynb

# fragalysis package
WORKDIR "/home/code"
RUN git clone https://github.com/xchem/fragalysis
WORKDIR "/home/code/fragalysis"
RUN pip install -e . --no-deps

# HIPPO dev branch
WORKDIR "/home/code"
RUN git clone https://github.com/mwinokan/HIPPO
WORKDIR "/home/code/HIPPO"
RUN git checkout dev && pip install -e . --no-deps

EXPOSE 8888

WORKDIR "/home/${NB_USER}"