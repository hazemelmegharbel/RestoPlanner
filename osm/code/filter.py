import sys
import pandas as pd
import numpy as np
import json
from pandas import json_normalize

#def filter():


def ffilter(in_d):
    df = pd.read_json(in_d, lines=True)
    print(df)
    ch=input("Please enter the number of the way to filter the list by amenity: (1)enter one or more amenities, (2)enter the start of the amenity, (3)enter the contain value of the amenity: ")
    if ch=="1":
       am=input("Input the name(s) separated by space:")
       aml=am.lower()
       am_l=aml.split(" ")
       print(df[df.amenity.isin(am_l)])
    elif ch=="2":
       am2=input("Input:")
       aml2=am2.lower()
       print(df[df.amenity.str.startswith(aml2)])
    elif ch=="3":
       am3=input("Input:")
       aml3=am3.lower()
       print(df[df.amenity.str.contains(aml3)])
    else: 
       print("Sorry I don't understand.")











if __name__ == '__main__':
    in_d= sys.argv[1]
    ffilter(in_d)


