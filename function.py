# -*- coding: utf-8 -*-
"""Function.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1i_sLmXu2ymE1UUGsDKFnCWzkyCfEFK6T
"""

from google.colab import files
uploaded = files.upload()
import numpy as np
import pandas as pd

Adf = pd.read_excel("Mumbai1.xlsx")

SortedPrice = Adf.sort_values(by='Price',ascending=False)
SortedPrice

SortedArea =Adf.sort_values(by='Area',ascending=True)
SortedArea

def Fetch(PredictedPrice,m_area,m_bed):
  PredictedPrice=int(PredictedPrice)
  status = True
  
  for i in range(len(SortedPrice)):
    if SortedPrice.loc[i]['Price']==PredictedPrice*10000:# or SortedPrice.loc[i]['Price']>PredictedPrice*10000:
      fetch_on_price(i)
    else:
      status = False
  if status == False:
    print("#")
    Fetch2(m_area,m_bed)

Fetch(1067.36,5000,3)

"""**For Area and Bed**"""

def Fetch2(area,bed):
  
  
  for i in range(len(SortedArea)):
    if SortedArea.loc[i]['Area']==area:
      item_found=1
      if item_found==1:
        fetch_features(i)
    if SortedArea.loc[i]['No._of_Bedrooms']==int(bed):
      fetch_features(i)

Fetch2(5000,3)

def fetch_on_price(i):
      if SortedPrice.loc[i]['Resale']==1:
        print("Resaleable House")
      else:
        print("Resale-Null")

      if SortedPrice.loc[i]['Gymnasium']==1:
        print("Gym Available")
      else:
        print("Gym-Null")

      if SortedPrice.loc[i]['Lift']==1:
        print("Lift Available")
      else:
        print("Lift-Null")

      if SortedPrice.loc[i]['Maintenance']==1:
        print("Staff for Maintenance")
      else:
        print("Maintanance-Null")

      if SortedPrice.loc[i]['Security']==1:
        print("Security 24*7")
      else:
        print("Security-Null")

      if SortedPrice.loc[i]['Intercom']==1:
        print("Intercom Authentication")
      else:
        print("Intercom-Null")

      if SortedPrice.loc[i]['Gas_Conn']==1:
        print("Gas Connection available")
      else:
        print("Gas Connection-Null")

      print("Price: "+ str(SortedPrice.loc[i]['Price']))
      print("Area:"+str(SortedPrice.loc[i]['Area'])+" Sqft")
      print(str(SortedPrice.loc[i]['No._of_Bedrooms'])+" BHK")
      print("Locattion"+str(SortedPrice.loc[i]['Location']))
      print("------------------------------------------------------------")

"""**For Price**"""

def fetch_features(i):
      if SortedArea.loc[i]['Resale']==1:
        print("Resaleable House")
      else:
        print("Resale-Null")

      if SortedArea.loc[i]['Gymnasium']==1:
        print("Gym Available")
      else:
        print("Gym-Null")

      if SortedArea.loc[i]['Lift']==1:
        print("Lift Available")
      else:
        print("Lift-Null")

      if SortedArea.loc[i]['Maintenance']==1:
        print("Staff for Maintenance")
      else:
        print("Maintanance-Null")

      if SortedArea.loc[i]['Security']==1:
        print("Security 24*7")
      else:
        print("Security-Null")

      if SortedArea.loc[i]['Intercom']==1:
        print("Intercom Authentication")
      else:
        print("Intercom-Null")

      if SortedArea.loc[i]['Gas_Conn']==1:
        print("Gas Connection available")
      else:
        print("Gas Connection-Null")

      print("Price: "+ str(SortedArea.loc[i]['Price']))
      print("Area:"+str(SortedArea.loc[i]['Area'])+" Sqft")
      print(str(SortedArea.loc[i]['No._of_Bedrooms'])+" BHK")
      print("Locattion: "+str(SortedArea.loc[i]['Location']))
      print("------------------------------------------------------------")