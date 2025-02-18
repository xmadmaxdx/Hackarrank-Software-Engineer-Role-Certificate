#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getAverageTemperatureForUser' function below.
#
# URL for cut and paste
# https://jsonmock.hackerrank.com/api/medical_records?userId=<userId>&page=<page>
#
# The function is expected to return a String value.
# The function accepts a userId argumnent (Integer).
# In the case of an empty array result, return value '0'
#


# My Solution: 
import requests

def getAverageTemperatureForUser(userId):
    base_url = 'https://jsonmock.hackerrank.com/api/medical_records'
    page = 1
    temperatures = []

    while True:
        response = requests.get(base_url, params={'userId': userId, 'page': page})
        if response.status_code != 200:
            return "0"

        data = response.json()
        records = data.get('data', [])
        if not records:
            return "0"

        for record in records:
            vitals = record.get('vitals', {})
            body_temp = vitals.get('bodyTemperature')
            if body_temp is not None:
                temperatures.append(body_temp)

        if page >= data.get('total_pages', 1):
            break
        page += 1

    if not temperatures:
        return "0"

    return f"{sum(temperatures) / len(temperatures):.1f}"
