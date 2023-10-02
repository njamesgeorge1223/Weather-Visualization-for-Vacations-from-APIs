#!/usr/bin/env python
# coding: utf-8

# In[1]:


#*******************************************************************************************
#
#  File Name:  VacationPySubRoutines.py 
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

import WeatherPyConstants as local_constant


# In[2]:


CONSTANT_LOCAL_FILE_NAME \
    = 'VacationPySubRoutines.py'


# In[3]:


#*******************************************************************************************
 #
 #  Subroutine Name:  SetVacationTemperatureRange
 #
 #  Subroutine Description:
 #      This subroutine sets the vacation temperature range.
 #
 #
 #  Subroutine Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  Integer
 #          minimumTemperatureInteger
 #                          This parameter is the minimum vacation maximum temperature.
 #  Integer
 #          maximumTemperatureInteger
 #                          This parameter is the maximum vacation maximum temperature.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/26/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def SetVacationTemperatureRange \
        (minimumTemperatureInteger,
         maximumTemperatureInteger):
    
    try:
        
        minimumTemperatureInteger \
            = int(minimumTemperatureInteger)
        
        maximumTemperatureInteger \
            = int(maximumTemperatureInteger)
        
        
        if minimumTemperatureInteger < 0:
            
            minimumTemperatureInteger = 0
            
        if maximumTemperatureInteger > 120:
            
            maximumTemperatureInteger = 120
            
            
        if minimumTemperatureInteger <= maximumTemperatureInteger:
        
            local_constant \
                .weatherConditionsDictionary \
                    ['temperatureIntegerList'][0] \
                        = minimumTemperatureInteger
        
            local_constant \
                .weatherConditionsDictionary \
                    ['temperatureIntegerList'][1] \
                        = maximumTemperatureInteger
        
        else:
            
            local_constant \
                .weatherConditionsDictionary \
                    ['temperatureIntegerList'][0] \
                        = maximumTemperatureInteger
        
            local_constant \
                .weatherConditionsDictionary \
                    ['temperatureIntegerList'][1] \
                        = minimumTemperatureInteger
        
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The subroutine, SetVacationTemperatureRange, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + f'was unable set the vacation temperature range.')


# In[4]:


#*******************************************************************************************
 #
 #  Subroutine Name:  SetVacationHumidityRange
 #
 #  Subroutine Description:
 #      This subroutine sets the vacation humidity range.
 #
 #
 #  Subroutine Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  Integer
 #          minimumHumidityInteger
 #                          This parameter is the minimum vacation humidity.
 #  Integer
 #          maximumHumidityInteger
 #                          This parameter is the maximum vacation humidity.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/26/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def SetVacationHumidityRange \
        (minimumHumidityInteger,
         maximumHumidityInteger):

    try:
        
        minimumHumidityInteger \
            = int(minimumHumidityInteger)
        
        maximumHumidityInteger \
            = int(maximumHumidityInteger)
        
        
        if minimumHumidityInteger < 0:
            
            minimumHumidityInteger = 0
            
        if maximumHumidityInteger > 100:
            
            maximumHumidityInteger = 100
            
            
        if minimumHumidityInteger <= maximumHumidityInteger:
        
            local_constant \
                .weatherConditionsDictionary \
                    ['humidityIntegerList'][0] \
                        = minimumHumidityInteger
        
            local_constant \
                .weatherConditionsDictionary \
                    ['humidityIntegerList'][1] \
                        = maximumHumidityInteger
        else:
            
            local_constant \
                .weatherConditionsDictionary \
                    ['humidityIntegerList'][0] \
                        = maximumHumidityInteger
        
            local_constant \
                .weatherConditionsDictionary \
                    ['humidityIntegerList'][1] \
                        = minimumHumidityInteger

    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The subroutine, SetVacationHumidityRange, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + f'was unable set the vacation humidity range.')


# In[5]:


#*******************************************************************************************
 #
 #  Subroutine Name:  SetVacationCloudinessRange
 #
 #  Subroutine Description:
 #      This subroutine sets the vacation cloudiness range.
 #
 #
 #  Subroutine Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  Integer
 #          minimumCloudinessInteger
 #                          This parameter is the minimum vacation cloudiness.
 #  Integer
 #          maximumCloudinessInteger
 #                          This parameter is the maximum vacation cloudiness.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/26/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def SetVacationCloudinessRange \
        (minimumCloudinessInteger,
         maximumCloudinessInteger):

    try:
        
        minimumCloudinessInteger \
            = int(minimumCloudinessInteger)
        
        maximumCloudinessInteger \
            = int(maximumCloudinessInteger)
        
        
        if minimumCloudinessInteger < 0:
            
            minimumCloudinessInteger = 0
            
        if maximumCloudinessInteger > 100:
            
            maximumCloudinessInteger = 100
            

        if minimumCloudinessInteger <= maximumCloudinessInteger:
            
            local_constant \
                .weatherConditionsDictionary \
                    ['cloudinessIntegerList'][0] \
                        = minimumCloudinessInteger
        
            local_constant \
                .weatherConditionsDictionary \
                    ['cloudinessIntegerList'][1] \
                        = maximumCloudinessInteger
            
        else:
            
            local_constant \
                .weatherConditionsDictionary \
                    ['cloudinessIntegerList'][0] \
                        = maximumCloudinessInteger
        
            local_constant \
                .weatherConditionsDictionary \
                    ['cloudinessIntegerList'][1] \
                        = minimumCloudinessInteger            
        
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The subroutine, SetVacationCloudinessRange, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + f'was unable set the vacation cloudiness range.')


# In[6]:


#*******************************************************************************************
 #
 #  Subroutine Name:  SetVacationWindPSpeedRange
 #
 #  Subroutine Description:
 #      This subroutine sets the vacation wind speed range.
 #
 #
 #  Subroutine Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  Integer
 #          minimumWindSpeedInteger
 #                          This parameter is the minimum vacation wind speed.
 #  Integer
 #          maximumWindSpeedInteger
 #                          This parameter is the maximum vacation wind speed.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/26/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def SetVacationWindPSpeedRange \
        (minimumWindSpeedInteger,
         maximumWindSpeedInteger):

    try:
        
        minimumWindSpeedInteger \
            = int(minimumWindSpeedInteger)
        
        maximumWindSpeedInteger \
            = int(maximumWindSpeedInteger)
        
        
        if minimumWindSpeedInteger < 0:
            
            minimumWindSpeedInteger = 0
            
        if maximumWindSpeedInteger > 100:
            
            maximumWindSpeedInteger = 100
        
        
        if minimumWindSpeedInteger <= maximumWindSpeedInteger:

            local_constant \
                .weatherConditionsDictionary \
                ['windSpeedIntegerList'][0] \
                    = minimumWindSpeedInteger
        
            local_constant \
                .weatherConditionsDictionary \
                    ['windSpeedIntegerList'][1] \
                        = maximumWindSpeedInteger
            
        else:
            
            local_constant \
                .weatherConditionsDictionary \
                ['windSpeedIntegerList'][0] \
                    = maximumWindSpeedInteger
        
            local_constant \
                .weatherConditionsDictionary \
                    ['windSpeedIntegerList'][1] \
                        = minimumWindSpeedInteger       
        
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The subroutine, SetVacationWindPSpeedRange, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + f'was unable set the vacation wind speed range.')

