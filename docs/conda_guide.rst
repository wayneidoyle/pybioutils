How do I make a conda environment for pybioutils?
=================================================
This is a brief guide to setting up a conda environment that will work with pybioutils. If you need help setting up conda on your machine the best resouce is this `guide <https://conda.io/projects/conda/en/latest/user-guide/install/linux.html>`_.

First make sure that your conda is configured for the correct channels ::

    conda config --add channels defaults
    conda config --add channels conda-forge
    conda config --add channels bioconda

Then run the following lines of code::

    conda create --name pybioutils_env python=3.7
    conda activate pybioutils_env
    conda install numpy matplotlib pandas
    conda install -c conda-forge matplotlib-venn
    conda install -c bioconda pybedtools


