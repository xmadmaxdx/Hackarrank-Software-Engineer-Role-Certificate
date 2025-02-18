#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'priceCheck' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY products
#  2. FLOAT_ARRAY productPrices
#  3. STRING_ARRAY productSold
#  4. FLOAT_ARRAY soldPrice
#

# My Answer:
def priceCheck(products, productPrices, productSold, soldPrice):
    price_map = {}
    for i in range(len(products)):
        price_map[products[i]] = productPrices[i]
    
    errors = 0

    for i in range(len(productSold)):
        product = productSold[i]
        actual_price = soldPrice[i]
        expected_price = price_map.get(product, None)
        
        if expected_price is None:
            errors += 1
        elif actual_price != expected_price:
            errors += 1
    
    return errors
