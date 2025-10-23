FROM quay.io/jupyter/minimal-notebook:2025-04-14
LABEL authors="Max Winokan"

# Upgrade pip and install JupyterLab
RUN pip install --upgrade pip && pip install hippo-db typer neo4j black gemmi

RUN mamba install --yes \
    chemicalite=2024.05.1 pdbfixer && \
    mamba clean --all -f -y && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

# patch rich
RUN python -c "import mrich; mrich.patch_rich_jupyter_margins()"

# install Chrome for plotly/kaleido
RUN python -c "import plotly.io as pio; pio.get_chrome()"

# Install Kaleido / Chromium dependencies
USER root
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        alsa-utils \
        libasound2-data \
        libnss3 \
        libatk-bridge2.0-0 \
        libcups2 \
        libxcomposite1 \
        libxdamage1 \
        libxfixes3 \
        libxrandr2 \
        libgbm1 \
        libxkbcommon0 \
        libpango-1.0-0 \
        libcairo2 \
        libgtk-3-0 \
        libx11-6 \
        libxext6 \
        libxrender1 \
        libxi6 \
        fonts-liberation \
        libappindicator3-1 \
        lsb-release \
        xdg-utils \
        wget

# set user
USER 0

# notebooks
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