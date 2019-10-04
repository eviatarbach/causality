# Code for "Local atmosphere–ocean predictability: dynamical origins, lead times, and seasonality"

This repository contains the code for the paper "Local atmosphere–ocean predictability: dynamical origins, lead times, and seasonality" by Eviatar Bach, Safa Motesharrei, Eugenia Kalnay, and Alfredo Ruiz-Barradas.

All the code was written by Eviatar Bach, except for the anomaly time-series code which was written by Alfredo Ruiz-Barradas. All code by Eviatar Bach is licensed under the GNU Public License v3.0.

The Granger causality analysis is done using the MVGC Matlab library, and plotting is done in Python.

You can contact me with any questions at eviatarbach@protonmail.com.

## Libraries used

Matlab:
- [MVGC](http://users.sussex.ac.uk/~lionelb/MVGC/html/mvgchelp.html)

Python:
- [cartopy](http://scitools.org.uk/cartopy/)
- [cmocean](https://matplotlib.org/cmocean/)
- [ecmwfapi](https://pypi.org/project/ecmwf-api-client/)
- [hdf5storage](https://pythonhosted.org/hdf5storage/)
- [Matplotlib](https://matplotlib.org/)
- [NumPy](http://www.numpy.org/)
- [pandas](https://pandas.pydata.org/)
- [pygrib](https://github.com/jswhit/pygrib)
- [pyresample](https://pyresample.readthedocs.io/en/latest/)
- [SciPy](https://scipy.org/scipylib/index.html)
- [statsmodels](https://www.statsmodels.org/stable/index.html)
- [xarray](http://xarray.pydata.org/en/stable/)

You also need [Jupyter](https://jupyter.org/) for the notebook that generates the plots.

## Description of files

The files are listed in the order that they should be run:

- **daily_data.py**: Takes daily means of the reanalysis data and removes leap days.
- **retrieve_data.py**: Retrieves the reanalysis data (ERA-Interim) from ECMWF.
- **variance.py**: Computes the variance of the SST data as well as the generalized variance of the atmospheric variables.
- **Plots.ipynb**: Jupyter notebook that generates all the figures in the paper (except the diagram).
