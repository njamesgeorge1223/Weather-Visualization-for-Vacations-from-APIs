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

|&rarr; [./README.md](./README.md)

|&rarr; [./README.TECHNICAL.md](./README.TECHNICAL.md)

|&rarr; [./Table-Of-Contents-WVFVFA.md](./Table-Of-Contents-WVFVFA.md)

|&rarr; [./VacationPy.ipynb](./VacationPy.ipynb)

|&rarr; [./VacationPySubRoutines.py](./VacationPySubRoutines.py)

|&rarr; [./WeatherPy.ipynb](./WeatherPy.ipynb)

|&rarr; [./WeatherPyAPIFunctions.py](./WeatherPyAPIFunctions.py)

|&rarr; [./WeatherPyAPIKeys.py](./WeatherPyAPIKeys.py)

|&rarr; [./WeatherPyConstants.py](./WeatherPyConstants.py)

|&rarr; [./WeatherPyFunctions.py](./WeatherPyFunctions.py)

|&rarr; [./Images/](./Images/)

  &emsp; |&rarr; [./Images/README.md](./Images/README.md)

  &emsp; |&rarr; [./Images/VacationPyFigure13CityWeatherLocations.html](./Images/VacationPyFigure13CityWeatherLocations.html)
  
  &emsp; |&rarr; [./Images/VacationPyFigure24VacationLocations.html](./Images/VacationPyFigure24VacationLocations.html)
  
  &emsp; |&rarr; [./Images/VacationPyFigure34HotelLocations.html](./Images/VacationPyFigure34HotelLocations.html)
  
  &emsp; |&rarr; [./Images/VacationPyFigure44RestaurantLocations.html](./Images/VacationPyFigure44RestaurantLocations.html)
  
  &emsp; |&rarr; [./Images/VacationPyFigure54TourismAttractionLocations.html](./Images/VacationPyFigure54TourismAttractionLocations.html)
  
  &emsp; |&rarr; [./Images/VacationPyTable12CityWeatherInformation.png](./Images/VacationPyTable12CityWeatherInformation.png)
  
  &emsp; |&rarr; [./Images/VacationPyTable23VacationLocations.png](./Images/VacationPyTable23VacationLocations.png)
  
  &emsp; |&rarr; [./Images/VacationPyTable33HotelLocations.png](./Images/VacationPyTable33HotelLocations.png)

  &emsp; |&rarr; [./Images/VacationPyTable43RestaurantLocations.png](./Images/VacationPyTable43RestaurantLocations.png)
  
  &emsp; |&rarr; [./Images/VacationPyTable53TourismAttractionLocations.png](./Images/VacationPyTable53TourismAttractionLocations.png)
  
  &emsp; |&rarr; [./Images/WeatherPyFigure15CityWeatherLocations.html](./Images/WeatherPyFigure15CityWeatherLocations.html)
  
  &emsp; |&rarr; [./Images/WeatherPyFigure19ImportedCityWeatherLocations.html](./Images/WeatherPyFigure19ImportedCityWeatherLocations.html)

  &emsp; |&rarr; [./Images/WeatherPyFigure21TemperatureVsLatitudeScatterPlotwRegression.png](./Images/WeatherPyFigure21TemperatureVsLatitudeScatterPlotwRegression.png)
  
  &emsp; |&rarr; 
[./Images/WeatherPyFigure22HumidityVsLatitudeScatterPlotwRegression.png](./Images/WeatherPyFigure22HumidityVsLatitudeScatterPlotwRegression.png)

  &emsp; |&rarr; [./Images/WeatherPyFigure23CloudinessVsLatitudeScatterPlotwRegression.png](./Images/WeatherPyFigure23CloudinessVsLatitudeScatterPlotwRegression.png)
  
  &emsp; |&rarr; [./Images/WeatherPyFigure24WindSpeedvsLatitudeScatterPlotwRegression.png](./Images/WeatherPyFigure24WindSpeedvsLatitudeScatterPlotwRegression.png)
  
  &emsp; |&rarr; [./Images/WeatherPyFigure31CityWeatherLocationsNorthernHemisphere.html](./Images/WeatherPyFigure31CityWeatherLocationsNorthernHemisphere.html)
  
  &emsp; |&rarr; [./Images/WeatherPyFigure32CityWeatherLocationsSouthernHemisphere.html](./Images/WeatherPyFigure32CityWeatherLocationsSouthernHemisphere.html)
  
  &emsp; |&rarr; [./Images/WeatherPyFigure33CityWeatherLocationsEasternHemisphere.html](./Images/WeatherPyFigure33CityWeatherLocationsEasternHemisphere.html)
  
  &emsp; |&rarr; [./Images/WeatherPyFigure34CityWeatherLocationsWesternHemisphere.html](./Images/WeatherPyFigure34CityWeatherLocationsWesternHemisphere.html)
  
  &emsp; |&rarr; [./Images/WeatherPyFigure411TemperaturevsLatitudeNorthernHemisphere.png](./Images/WeatherPyFigure411TemperaturevsLatitudeNorthernHemisphere.png)

  &emsp; |&rarr; [./Images/WeatherPyFigure412TemperaturevsLatitudeSouthernHemisphere.png](./Images/WeatherPyFigure412TemperaturevsLatitudeSouthernHemisphere.png)

  &emsp; |&rarr; [./Images/WeatherPyFigure413TemperaturevsLatitudeEasternHemisphere.png](./Images/WeatherPyFigure413TemperaturevsLatitudeEasternHemisphere.png)

  &emsp; |&rarr; [./Images/WeatherPyFigure414TemperaturevsLatitudeWesternHemisphere.png](./Images/WeatherPyFigure414TemperaturevsLatitudeWesternHemisphere.png)

  &emsp; |&rarr; [./Images/WeatherPyFigure421HumidityvsLatitudeNorthernHemisphere.png](./Images/WeatherPyFigure421HumidityvsLatitudeNorthernHemisphere.png)

  &emsp; |&rarr; [./Images/WeatherPyFigure422HumidityvsLatitudeSouthernHemisphere.png](./Images/WeatherPyFigure422HumidityvsLatitudeSouthernHemisphere.png)

  &emsp; |&rarr; [./Images/WeatherPyFigure423HumidityvsLatitudeEasternHemisphere.png](./Images/WeatherPyFigure423HumidityvsLatitudeEasternHemisphere.png)

  &emsp; |&rarr; [./Images/WeatherPyFigure424HumidityvsLatitudeWesternHemisphere.png](./Images/WeatherPyFigure424HumidityvsLatitudeWesternHemisphere.png)

  &emsp; |&rarr; [./Images/WeatherPyFigure431CloudinessvsLatitudeNorthernHemisphere.png](./Images/WeatherPyFigure431CloudinessvsLatitudeNorthernHemisphere.png)

  &emsp; |&rarr; [./Images/WeatherPyFigure432CloudinessvsLatitudeSouthernHemisphere.png](./Images/WeatherPyFigure432CloudinessvsLatitudeSouthernHemisphere.png)

  &emsp; |&rarr; [./Images/WeatherPyFigure433CloudinessvsLatitudeEasternHemisphere.png](./Images/WeatherPyFigure433CloudinessvsLatitudeEasternHemisphere.png)

  &emsp; |&rarr; [./Images/WeatherPyFigure434CloudinessvsLatitudeWesternHemisphere.png](./Images/WeatherPyFigure434CloudinessvsLatitudeWesternHemisphere.png)

  &emsp; |&rarr; [./Images/WeatherPyFigure441WindSpeedvsLatitudeNorthernHemisphere.png](./Images/WeatherPyFigure441WindSpeedvsLatitudeNorthernHemisphere.png)

  &emsp; |&rarr; [./Images/WeatherPyFigure442WindSpeedvsLatitudeSouthernHemisphere.png](./Images/WeatherPyFigure442WindSpeedvsLatitudeSouthernHemisphere.png)

  &emsp; |&rarr; [./Images/WeatherPyFigure443WindSpeedvsLatitudeEasternHemisphere.png](./Images/WeatherPyFigure443WindSpeedvsLatitudeEasternHemisphere.png)

  &emsp; |&rarr; [./Images/WeatherPyFigure444WindSpeedvsLatitudeWesternHemisphere.png](./Images/WeatherPyFigure444WindSpeedvsLatitudeEasternHemisphere.png)

  &emsp; |&rarr; [./Images/WeatherPyFigure511TemperaturevsLongitudeNorthernHemisphere.png](./Images/WeatherPyFigure511TemperaturevsLongitudeNorthernHemisphere.png)

  &emsp; |&rarr; [./Images/WeatherPyFigure512TemperaturevsLongitudeSouthernHemisphere.png](./Images/WeatherPyFigure512TemperaturevsLongitudeSouthernHemisphere.png)

  &emsp; |&rarr; [./Images/WeatherPyFigure513TemperaturevsLongitudeEasternHemisphere.png](./Images/WeatherPyFigure513TemperaturevsLongitudeEasternHemisphere.png)

  &emsp; |&rarr; [./Images/WeatherPyFigure514TemperaturevsLongitudeWesternHemisphere.png](./Images/WeatherPyFigure514TemperaturevsLongitudeWesternHemisphere.png)

  &emsp; |&rarr; [./Images/WeatherPyFigure521HumidityvsLongitudeNorthernHemisphere.png](./Images/WeatherPyFigure521HumidityvsLongitudeNorthernHemisphere.png)

  &emsp; |&rarr; [./Images/WeatherPyFigure522HumidityvsLongitudeSouthernHemisphere.png](./Images/WeatherPyFigure522HumidityvsLongitudeSouthernHemisphere.png)

  &emsp; |&rarr; [./Images/WeatherPyFigure523HumidityvsLongitudeEasternHemisphere.png](./Images/WeatherPyFigure523HumidityvsLongitudeEasternHemisphere.png)

  &emsp; |&rarr; [./Images/WeatherPyFigure524HumidityvsLongitudeWesternHemisphere.png](./Images/WeatherPyFigure524HumidityvsLongitudeWesternHemisphere.png)

  &emsp; |&rarr; [./Images/WeatherPyFigure531CloudinessvsLongitudeNorthernHemisphere.png](./Images/WeatherPyFigure531CloudinessvsLongitudeNorthernHemisphere.png)

  &emsp; |&rarr; [./Images/WeatherPyFigure532CloudinessvsLongitudeSouthernHemisphere.png](./Images/WeatherPyFigure532CloudinessvsLongitudeSouthernHemisphere.png)

  &emsp; |&rarr; [./Images/WeatherPyFigure533CloudinessvsLongitudeEasternHemisphere.png](./Images/WeatherPyFigure533CloudinessvsLongitudeEasternHemisphere.png)

  &emsp; |&rarr; [./Images/WeatherPyFigure534CloudinessvsLongitudeWesternHemisphere.png](./Images/WeatherPyFigure534CloudinessvsLongitudeWesternHemisphere.png)
  
  &emsp; |&rarr; [./Images/WeatherPyFigure541WindSpeedvsLongitudeNorthernHemisphere.png](./Images/WeatherPyFigure541WindSpeedvsLongitudeNorthernHemisphere.png)

  &emsp; |&rarr; [./Images/WeatherPyFigure542WindSpeedvsLongitudeSouthernHemisphere.png](./Images/WeatherPyFigure542WindSpeedvsLongitudeSouthernHemisphere.png)

  &emsp; |&rarr; [./Images/WeatherPyFigure543WindSpeedvsLongitudeEasternHemisphere.png](./Images/WeatherPyFigure543WindSpeedvsLongitudeEasternHemisphere.png)

  &emsp; |&rarr; [./Images/WeatherPyFigure544WindSpeedvsLongitudeWesternHemisphere.png](./Images/WeatherPyFigure544WindSpeedvsLongitudeWesternHemisphere.png)

  &emsp; |&rarr; [./Images/WeatherPyTable14CityWeatherInformation.png](./Images/WeatherPyTable14CityWeatherInformation.png)

  &emsp; |&rarr; [./Images/WeatherPyTable18ImportedCityWeatherInformation.png](./Images/WeatherPyTable18ImportedCityWeatherInformation.png)

|&rarr; [./Logs/](./Logs/)

  &emsp; |&rarr; [./Logs/20231108VacationPyDebug.txt](./Logs/20231108VacationPyDebug.txt)

  &emsp; |&rarr; [./Logs/20231108VacationPyLog.txt](./Logs/20231108VacationPyLog.txt)

  &emsp; |&rarr; [./Logs/20231108WeatherPyDebug.txt](./Logs/20231108WeatherPyDebug.txt)

  &emsp; |&rarr; [./Logs/20231108WeatherPyLog.txt](./Logs/20231108WeatherPyLog.txt)

  &emsp; |&rarr; [./Logs/README.md](./Logs/README.md)

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
