#!/usr/bin/env python
# coding: utf-8

# In[1]:


#*******************************************************************************************
#
#  File Name:  WeatherPyFunctions.py 
#
#  File Description:
#      This Python script provides functions for completing tasks associated with
#      the Jupyter Notebook, WeatherPy.ipynb.
#      
#
#  Date            Description                             Programmer
#  ----------      ------------------------------------    ------------------
#  08/26/2023      Initial Development                     N. James George
#
#******************************************************************************************/

import PyConstants as constant


# In[2]:


CONSTANT_LOCAL_FILE_NAME \
    = 'WeatherPyFunctions.py'


# In[ ]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnCityWeatherStylerObjectStandardFormat
 #
 #  Function Description:
 #      This function receives a city Weather DataFrame, formats a copy of it 
 #      as a Styler Object, and returns it to the caller.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  DataFrame
 #          inputDataFrameParameter
 #                          This parameter is the input DataFrame.
 #  String
 #          captionStringParameter
 #                          This parameter is the table title.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/26/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnCityWeatherStylerObjectStandardFormat \
        (inputDataFrameParameter,
         captionStringParameter):
    
    try:
        
        inputDataFrame \
            = inputDataFrameParameter \
                .copy()
    
        inputDataFrame \
            .index \
            .name \
                = None

        return \
            inputDataFrame \
                .style \
                .set_caption \
                    (captionStringParameter) \
                .set_table_styles \
                    ([{'selector': 
                           'caption', 
                       'props':
                            [('color', 
                                  'black'), 
                             ('font-size', 
                                  '20px'),
                             ('font-style', 
                                  'bold'),
                             ('text-align', 
                                  'center')]}]) \
                .set_properties \
                    (**{'text-align':
                            'center',
                        'border':
                            '1.3px solid red',
                        'color':
                            'blue'}) \
                .format \
                    ({'City':
                        constant.GENERAL_TEXT_FORMAT, 
                      'Latitude':
                        constant.FLOAT_FORMAT, 
                      'Longitude':
                        constant.FLOAT_FORMAT,
                      'Temperature':
                        constant.TEMPERATURE_FLOAT_FORMAT,
                      'Humidity':
                        constant.PERCENT_INTEGER_FORMAT,
                      'Cloudiness':
                        constant.PERCENT_INTEGER_FORMAT,
                      'Wind Speed':
                        constant.FLOAT_FORMAT,
                      'Country':
                        constant.GENERAL_TEXT_FORMAT}) \
                .highlight_max \
                    (subset \
                        = ['Temperature',
                           'Humidity',
                           'Cloudiness',
                           'Wind Speed'],
                     color='lime') \
                .highlight_min \
                    (subset \
                        = ['Temperature',
                           'Humidity',
                           'Cloudiness',
                           'Wind Speed'],
                     color='yellow') \
                .hide()
    except:
                
        log_subroutine \
            .PrintAndLogWriteText \
                ('The function, ReturnCityWeatherStylerObjectStandardFormat, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + 'was unable to format a city weather DataFrame.')
        
        return \
            None

