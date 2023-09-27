# **Weather Visualization for Ideal vacations from APIs**

----

### **Installation:**

----

If the computer has Anaconda, Jupyter Notebook, and a recent version of Python, the IPython notebook already has the following dependencies installed: datetime, io, json, matplotlib, numpy, pandas, pathlib, os, pandas, requests, requests_html, and scipy.

In addition to those modules, the Jupyter Notebook requires the following to execute: holoviews, hvplot, geoviews, geopy, aspose-words, dataframe-image, citypy.

Here are the requisite Terminal commands for the installation of these peripheral modules:

python3 -m pip install holoviews

python3 -m pip install hvplot

python3 -m pip install geoviews

python3 -m pip install geopy

python3 -m pip install aspose-words

python3 -m pip install dataframe-image

python3 -m pip install citypy

----

### **Usage:**

----

The IPython notebook, WeatherPy.ipynb, generates the CSV file, CitiesWeather.csv, which acts as input to VacationPy.ipynb.  These IPython Notebooks must have the following Python scripts in the same folder with it:

PyConstants.py

PyFunctions.py

PyLogConstants.py

PyLogFunctions.py

PySubroutines.py

WeatherPyAPIFunctions.py

WeatherPyAPIKeys.py

WeatherPyConstants.py

WeatherPyFunctions.py

If the folders, Resources, Logs, and Images are not present, an IPython notebook will create them.  The Resources folder contains the output file from WeatherPy.ipynb, CitiesWeather.csv, which is the input file for VacationPy.ipynb; the Logs folder contains debug and log files from testing the IPython Notebooks; and the Images folder has the PNG image files of the IPython Notebooks' tables and plots.

To place the IPython notebook in Log Mode, Debug Mode, or Image Mode set the parameter for the appropriate subroutine in coding cell #2 to True. In Debug Mode, the program displays the debug information and writes it to a debug file in the Logs folder; the same is true in Log Mode for log information sent to a log file. If the program is in Log Mode but NOT Debug Mode, it displays no debug information, but writes that information to the log file. If the program is in Image Mode, it writes all DataFrames, hvplot maps, and matplotlib plots to PNG files in the Images Folder.

----

### **Resource Summary:**

----

#### Source code

WeatherPy.ipynb, VacationPy.ipynb, PyConstants.py, PyFunctions.py, PyLogConstants.py, PyLogFunctions.py, PySubroutines.py, WeatherPyAPIFunctions.py, WeatherPyAPIKeys.py, WeatherPyConstants.py, WeatherPyFunctions.py

#### Input files

CitiesWeather.csv (VacationPy.ipynb)

#### Output files

CitiesWeather.csv (WeatherPy.ipynb)

#### SQL script

n/a

#### Software

Jupyter Notebook, Pandas, Python 3.11.4

![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

----

### **GitHub Repository Branches:**

----

#### main branch 

|&rarr; [./PyConstants.py](./PyConstants.py)

|&rarr; [./PyFunctions.py](./PyFunctions.py)

|&rarr; [./PyLogConstants.py](./PyLogConstants.py)

|&rarr; [./PyLogFunctions.py](./PyLogFunctions.py)

|&rarr; [./PyLogSubRoutines.py](./PyLogSubRoutines.py)

|&rarr; [./PySubRoutines.py](./PySubRoutines.py)

|&rarr; [./README.TECHNICAL.md](./README.TECHNICAL.md)

|&rarr; [./README.md](./README.md)

|&rarr; [./VacationPy.ipynb](./VacationPy.ipynb)

|&rarr; [./WeatherPy.ipynb](./WeatherPy.ipynb)

|&rarr; [./WeatherPyAPIFunctions.py](./WeatherPyAPIFunctions.py)

|&rarr; [./WeatherPyAPIKeys.py](./WeatherPyAPIKeys.py)

|&rarr; [./WeatherPyConstants.py](./WeatherPyConstants.py)

|&rarr; [./WeatherPyFunctions.py](./WeatherPyFunctions.py)

|&rarr; [./Images/](./Images/)

  &emsp; |&rarr; [./Images/README.md](./Images/README.md)

  &emsp; |&rarr; [./Images/VacationPyFigure11CityWeatherInformationonMap.png](./Images/VacationPyFigure11CityWeatherInformationonMap.png)
  
  &emsp; |&rarr; [./Images/VacationPyFigure21IdealVacationLocations.png](./Images/VacationPyFigure21IdealVacationLocations.png)
  
  &emsp; |&rarr; [./Images/VacationPyFigure31HotelLocations.png](./Images/VacationPyFigure31HotelLocations.png)
  
  &emsp; |&rarr; [./Images/VacationPyTable11CityWeatherInformation.png](./Images/VacationPyTable11CityWeatherInformation.png)
  
  &emsp; |&rarr; [./Images/VacationPyTable21IdealVacationLocations.png](./Images/VacationPyTable21IdealVacationLocations.png)
  
  &emsp; |&rarr; [./Images/VacationPyTable31HotelLocations.png](./Images/VacationPyTable31HotelLocations.png)
  
  &emsp; |&rarr; [./Images/WeatherPyFigure121TemperatureVsLatitudeScatterPlot.png](./Images/WeatherPyFigure121TemperatureVsLatitudeScatterPlot.png)
  
  &emsp; |&rarr; [./Images/WeatherPyFigure122HumidityVsLatitudeScatterPlot.png](./Images/WeatherPyFigure122HumidityVsLatitudeScatterPlot.png)

  &emsp; |&rarr; [./Images/WeatherPyFigure123CloudinessVsLatitudeScatterPlot.png](./Images/WeatherPyFigure123CloudinessVsLatitudeScatterPlot.png)
  
  &emsp; |&rarr; [./Images/WeatherPyFigure124WindSpeedvsLatitudeScatterPlot.png](./Images/WeatherPyFigure124WindSpeedvsLatitudeScatterPlot.png)
  
  &emsp; |&rarr; [./Images/WeatherPyFigure131TemperaturevsLatitudeNorthernHemisphere.png](./Images/WeatherPyFigure131TemperaturevsLatitudeNorthernHemisphere.png)
  
  &emsp; |&rarr; [./Images/WeatherPyFigure132TemperaturevsLatitudeSouthernHemisphere.png](./Images/WeatherPyFigure132TemperaturevsLatitudeSouthernHemisphere.png)

  &emsp; |&rarr; [./Images/WeatherPyFigure133HumidityvsLatitudeNorthernHemisphere.png](./Images/WeatherPyFigure133HumidityvsLatitudeNorthernHemisphere.png)
  
  &emsp; |&rarr; 
[./Images/WeatherPyFigure134HumidityvsLatitudeSouthernHemisphere.png](./Images/WeatherPyFigure134HumidityvsLatitudeSouthernHemisphere.png)

  &emsp; |&rarr; [./Images/WeatherPyFigure135CloudinessvsLatitudeNorthernHemisphere.png](./Images/WeatherPyFigure135CloudinessvsLatitudeNorthernHemisphere.png)
  
  &emsp; |&rarr; [./Images/WeatherPyFigure136CloudinessvsLatitudeSouthernHemisphere.png](./Images/WeatherPyFigure136CloudinessvsLatitudeSouthernHemisphere.png)
  
  &emsp; |&rarr; [./Images/WeatherPyFigure137WindSpeedvsLatitudeNorthernHemisphere.png](./Images/WeatherPyFigure137WindSpeedvsLatitudeNorthernHemisphere.png)
  
  &emsp; |&rarr; [./Images/WeatherPyFigure138WindSpeedvsLatitudeSouthernHemisphere.png](./Images/WeatherPyFigure138WindSpeedvsLatitudeSouthernHemisphere.png)
  
  &emsp; |&rarr; [./Images/WeatherPyFigure1211TemperatureVsLatitudeScatterPlotwRegression.png](./Images/WeatherPyFigure1211TemperatureVsLatitudeScatterPlotwRegression.png)
  
  &emsp; |&rarr; [./Images/WeatherPyTable111CityWeatherInformation.png](./Images/WeatherPyTable111CityWeatherInformation.png)
  
  &emsp; |&rarr; [./Images/WeatherPyTable112CityWeatherInformation.png](./Images/WeatherPyTable112CityWeatherInformation.png)

|&rarr; [./Logs/](./Logs/)

  &emsp; |&rarr; [./Logs/README.md](./Logs/README.md)

  &emsp; |&rarr; [./Logs/20230922VacationPyDebug.txt](./Logs/20230922VacationPyDebug.txt)

  &emsp; |&rarr; [./Logs/20230922VacationPyLog.txt](./Logs/20230922VacationPyLog.txt)

  &emsp; |&rarr; [./Logs/20230922WeatherPyDebug.txt](./Logs/20230922WeatherPyDebug.txt)

  &emsp; |&rarr; [./Logs/20230922WeatherPyLog.txt](./Logs/20230922WeatherPyLog.txt)

|&rarr; [./Resources/](./Resources/)

  &emsp; |&rarr; [./Resources/CitiesWeather.csv](./Resources/CitiesWeather.csv)

  &emsp; |&rarr; [./Resources/README.md](./Resources/README.md)

----

### **References:**

----

[Jupyter Notebook Documentation](https://jupyter-notebook.readthedocs.io/en/stable/)

[Pandas User Guide](https://pandas.pydata.org/docs/user_guide/index.html)

[Python Documentation](https://docs.python.org/3/contents.html)

----

### **Authors and Acknowledgment:**

----

### Copyright

N. James George © 2023. All Rights Reserved.
