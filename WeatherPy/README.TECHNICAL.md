The IPython notebooks, WeatherPy.ipynb and VacationPy.ipynb, require the following Python scripts with them in the same folder:

PyConstants.py

PyFunctions.py

PyLogConstants.py

PyLogFunctions.py

PyLogSubRoutines.py

PySubroutines.py

WeatherPyAPIFunctions.py

WeatherPyAPIKeys.py

WeatherPyConstants.py

WeatherPyFunctions.py

If the computer has Anaconda, Jupyter Notebook, and a recent version of Python, the IPython notebook already has the following dependencies installed: datetime, io, json, matplotlib, numpy, pandas, pathlib, os, pandas, requests, requests_html, and scipy.

In addition to those modules, the IPython notebook needs the following to execute: citipy, hvplot, panel, geoviews, and geopy.

Here are the requisite Terminal commands for installation of these peripheral modules (in this order):

python3 -m pip install citipy

python3 -m pip install hvplot

python3 -m pip install panel

python3 -m pip install geoviews

python3 -m pip install geopy

For the conda environment, these are the requisite Terminal commands:

conda config --add channels conda-forge

conda config --set channel_priority strict


conda install citipy

conda install hvplot

conda install panel

conda install -c conda-forge geoviews

conda install -c conda-forge geopy

If the folders, Resources, Logs, and Images are not present, the IPython otebook will create them.  Weather.ipynb generates the file in the Resources folder, CitiesWeather.csv, the input file for VacationPy.ipynb.

To place the IPython notebook in log mode, debug mode,or image mode set the parameter forthe appropriate subroutine in cell #2 to True.  In debug mode, the program displays the debug information and writes it to a debug file in the Logs folder; the same is true in log mode for log information sent to a log file in the same folder.  If the program is in log mode but not debug mode, it displays no debug information, but writes that information to the log file. If the program is in image mode, it writes all the plots to png files in the Images folder.
