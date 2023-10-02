#!/usr/bin/env python
# coding: utf-8

# In[1]:


#*******************************************************************************************
 #
 #  File Name:  WeatherPyAPIFunctions.py 
 #
 #  File Description:
 #      This Python script provides functions for completing API tasks associated
 #      with the Jupyter Notebook, WeatherPy.ipynb.
 #      
 #
 #  Date            Description                             Programmer
 #  ----------      ------------------------------------    ------------------
 #  08/24/2023      Initial Development                     N. James George
 #
 #******************************************************************************************/

import PyFunctions as function
import PyLogSubRoutines as log_subroutine
import WeatherPyConstants as local_constant

import requests

from datetime import datetime
import numpy as np
import pandas as pd

from citipy import citipy
from WeatherPyAPIKeys import weather_api_key
from WeatherPyAPIKeys import geoapify_key


# In[2]:


CONSTANT_LOCAL_FILE_NAME \
    = 'WeatherPyAPIFunctions.py'


# In[3]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnCitiesList
 #
 #  Function Description:
 #      This function returns a list of cities from the citipi API.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  n/a     n/a             n/a
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/26/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/
    
def ReturnCitiesList():

    try:
        
        latitudeAndLongitudesList \
            = []

        citiesListofStrings \
            = []

        
        latitudeRangeTuple \
            = (-90, 90)

        longitudeRangeTuple \
            = (-180, 180)


        randomLatitudeArray \
            = np \
                .random \
                .uniform \
                    (latitudeRangeTuple[0], latitudeRangeTuple[1], 
                     size \
                         = 1500)

        randomLongitudeArray \
            = np \
                .random \
                .uniform \
                    (longitudeRangeTuple[0], longitudeRangeTuple[1], 
                     size \
                         = 1500)


        latitudeAndLongitudeCombinationsZipObject \
            = zip \
                (randomLatitudeArray, 
                 randomLongitudeArray)


        for latitudeAndLongitudeList in latitudeAndLongitudeCombinationsZipObject:
    
            cityNameStringVariable \
                = citipy \
                    .nearest_city \
                        (latitudeAndLongitudeList[0], latitudeAndLongitudeList[1]) \
                    .city_name
    
            if cityNameStringVariable not in citiesListofStrings:
                citiesListofStrings \
                    .append  \
                        (cityNameStringVariable)
        
        
        return \
            citiesListofStrings
        
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The function, ReturnCitiesList, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + f'was unable to return a List of cities to the caller.')
    
        return None


# In[4]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnWeatherDataFrame
 #
 #  Function Description:
 #      This function returns weather information from a weather API 
 #      based on a list of cities.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  List of Strings
 #          citiesListOfStringsParameter
 #                          This parameter is a List of city names.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/26/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnWeatherDataFrame \
        (citiesListOfStringsParameter):
    

    queryURLStringVariable \
        = f'{local_constant.OPEN_WEATHERMAP_WEBSITE}/data/2.5/weather?appid=' \
          + f'{weather_api_key}&units={local_constant.API_DATA_UNITS}&q='


    weatherDataForEachCityList \
        = []


    recordCountIntegerVariable \
        = 1
    
    setOfCitiesCountIntegerVariable \
        = 1
    
    
    log_subroutine \
        .PrintAndLogWriteText \
            ('\nDATA RETRIEVAL FOR CITY WEATHER DATAFRAME BEGINS...\n')


    for index, cityName in enumerate(citiesListOfStringsParameter):
    
        if index % local_constant.SET_OF_CITIES == 0 \
           and index >= local_constant.SET_OF_CITIES:
        
            recordCountIntegerVariable \
                = 0
        
            setOfCitiesCountIntegerVariable \
                += 1

            
        log_subroutine \
            .PrintAndLogWriteText \
                (f'\nPROCESSING RECORD #{recordCountIntegerVariable+1} ' \
                    + f'OF SET {setOfCitiesCountIntegerVariable} FOR CITY, {cityName}.')
            

        cityURLStringVariable \
            = queryURLStringVariable + cityName
            
        recordCountIntegerVariable \
            += 1
        
        
        try:

            cityWeatherDictionary \
                = requests \
                    .get \
                        (cityURLStringVariable) \
                    .json()


            cityLatitudeFloatVariable \
                = cityWeatherDictionary \
                    ['coord'] \
                    ['lat']

            cityLongitudeFloatVariable \
                = cityWeatherDictionary \
                    ['coord'] \
                    ['lon']
        

            cityTemperatureFloatVariable \
                = cityWeatherDictionary \
                    ['main'] \
                    ['temp']

            cityHumidityIntegerVariable \
                = cityWeatherDictionary \
                    ['main'] \
                    ['humidity']

            cityCloudsIntegerVariable \
                = cityWeatherDictionary \
                    ['clouds'] \
                    ['all']

            cityWindFloatVariable \
                = cityWeatherDictionary \
                    ['wind'] \
                    ['speed']
        

            cityCountryStringVariable \
                = cityWeatherDictionary \
                    ['sys'] \
                    ['country']

            cityDateDateTimeVariable \
                = datetime \
                    .fromtimestamp \
                        (cityWeatherDictionary
                            ['dt'])
         

            weatherDataForEachCityList \
                .append \
                    ({'City': 
                            cityName, 
                      'Latitude': 
                            cityLatitudeFloatVariable, 
                      'Longitude': 
                            cityLongitudeFloatVariable, 
                      'Temperature': 
                            cityTemperatureFloatVariable,
                      'Humidity': 
                            cityHumidityIntegerVariable,
                      'Cloudiness': 
                            cityCloudsIntegerVariable,
                      'Wind Speed': 
                            cityWindFloatVariable,
                      'Country': 
                            cityCountryStringVariable,
                      'Date/Time':
                            cityDateDateTimeVariable})

        except:
        
            log_subroutine \
                .PrintAndLogWriteText \
                    (f'\nThe script did not find the city, {cityName}. Skipping...')

            
    log_subroutine \
        .PrintAndLogWriteText \
            (f'\nData Retrieval for city weather DataFrame is complete.') 
    
    
    return \
        pd \
            .DataFrame \
                (weatherDataForEachCityList)


# In[5]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnUpdatedLocationDataFrame
 #
 #  Function Description:
 #      This function takes a ocation DataFrame, populates the location name column,
 #      and returns the updated DataFrame to the caller.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  DataFrame
 #          inputDataFrameParameter
 #                          This parameter is the input DataFrame.
 #  List of Strings
 #          categoriesStringOrListParameter
 #                          This parameter is a String or List of search categories.
 #  Integer
 #          radiusIntegerParameter
 #                          This parameter is the radius of search.
 #  Integer
 #          limitIntegerParameter
 #                          This parameter is a limit on the number of results.    
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/26/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnUpdatedLocationDataFrame \
        (inputDataFrameParameter,
         columnNameString,
         categoriesStringOrListParameter \
            ='accommodation.hotel',
         radiusIntegerParameter \
            = 10000,
         limitIntegerParameter \
            = 20):
    
    inputDataFrame \
        = inputDataFrameParameter.copy()
    
    
    parameterDictionary \
        = {'categories': categoriesStringOrListParameter,
           'filter': '',
           'bias': '',
           'limit': limitIntegerParameter,
           'lang': 'en',
           'apiKey': geoapify_key}

    if categoriesStringOrListParameter == 'accommodation.hotel':
        
        categoryNameString = 'hotel'
    
    elif categoriesStringOrListParameter == 'catering.restaurant':
        
        categoryNameString = 'restaurant'
        
    elif categoriesStringOrListParameter == 'tourism.attraction':
        
        categoryNameString = 'tourism attraction'
        
    else:
        
        return \
            inputDataFrame
        
    
    log_subroutine \
        .PrintAndLogWriteText \
            (f'Starting {categoryNameString} search...\n\n')

             
    citiesStringList \
        = []

    locationNameStringList \
        = []


    for index, row in inputDataFrame.iterrows():

        latitudeStringVariable \
            = inputDataFrame['Latitude'][index]
    
        longitudeStringVariable \
            = inputDataFrame['Longitude'][index]

    
        parameterDictionary \
            ['filter'] \
                 = f'circle:{longitudeStringVariable},{latitudeStringVariable},{radiusIntegerParameter}'
             
        parameterDictionary \
            ['bias'] \
                 = f'proximity:{longitudeStringVariable},{latitudeStringVariable}'
    

        urlStringVariable \
                 = 'https://api.geoapify.com/v2/places'
    
        
        responseObject \
            = requests \
                 .get \
                     (url = urlStringVariable,
                      params = parameterDictionary) \
                 .json()


        if len( responseObject['features'] ) == 0:
        
            continue
        
        
        for locationIndex, location in enumerate( responseObject['features'] ):
        
            try:
                
                locationNameString \
                    = location['properties']['name']

                locationNameStringList \
                    .append \
                        (locationNameString)
                
                log_subroutine \
                    .PrintAndLogWriteText \
                        (f'Located the following {categoryNameString}...' \
                         + f'{locationNameString} ' \
                         + f"in {inputDataFrame['City'][index]}, " \
                         + f"{inputDataFrame['Country'][index]}\n\n")

                break
            
            except:
             
                continue
        
        
        citiesStringList.append(row['City'])


    tempDataFrame \
        = function \
            .ReturnDataFrameRowsWithValue \
                    (inputDataFrame,
                     'City',
                     citiesStringList)

    tempDataFrame \
        .reset_index \
            (drop = True, 
             inplace = True)
             
    tempDataFrame \
        [columnNameString] \
            = pd.Series \
                (locationNameStringList)
    
    
    log_subroutine \
        .PrintAndLogWriteText \
            (f'{categoryNameString} search complete\n\n')
            
             
    return \
        tempDataFrame


# In[ ]:




