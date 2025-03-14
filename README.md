# Fragalysis notebooks

This repo contains a number of Jupyter notebooks that assist with handling [Fragalysis](https://fragalysis.diamond.ac.uk/viewer/react/landing)
data in [Squonk](https://squonk.it/).

## Usage

1. Create or open a Squonk project, presumably (but not necessarily) in the
[Squonk instance](https://data-manager-ui.xchem.diamond.ac.uk/data-manager-ui?project=project-0a4b7618-bbcc-4e72-8c76-8b1fcd7ffd24) at
[Diamond](https://www.diamond.ac.uk/).
2. Launch a Jupyter notebook instance (on the *Apps/Jobs* tab) and open it.
3. Create a new terminal window.
4. In that terminal clone this git repo: `git clone https://github.com/xchem/squonk-fragalysis-notebooks.git`.
5. Start using the notebooks.

To update the notebooks at any stage open a new terminal window and run `git pull`

## Notebooks

1. fragalysis-download.ipynb - allows to download data for a Fragalysis target for your to work with.
2. dependencies-eg.ipynb - a template notebook for loading dependencies.


## Usage

### Organisation of files

Try to keep your top level directory clutter free so that it only contains notebooks or instructions such as this README.
e.g. place your input data and working data in sub-directories.


### Package management

Your Notebook instance should not be considered permanent. You  will almost certainly need to re-create it at times.
Your data will remain in the Squonk project, but the instance and anything you had done to customise it (e.g. install additional packages)
will be lost.
To make it easy to re-instate the conda packages you should create a separate notebook named `dependencies.ipynb` that you can use to re-load
those dependencies. You can use the `dependencies-eg.ipynb` notebook as a starting point.

### Creating your own notebooks

If using these template notebooks, it is probably best to take a copy and edit and use that copy. That makes it easier to update the templates.
Alternatively you might want to create a fork of the repo and clone that so that you can version control your own notebooks.
