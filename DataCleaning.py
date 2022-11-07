# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 12:37:47 2022

@author: Harpreet Singh
"""


import pandas as pd 
import os  



#This cleans data, but its not applicable for all the dataframes 
def dataclean(df): 
    df["Time"] =  df.iloc[:, 0].apply(lambda x:x.split(';')[0])
    df["frequency - 50"] = df.iloc[:, 0].apply(lambda y:y.split(';')[1])
    df.drop(columns=df.columns[0], axis=1, inplace=True)
    df['Time'] =  pd.to_datetime(df['Time'], format="%Y-%m-%d %H:%M:%S")
    #df = df.set_index(['Time'])
    return df 

#This cleans data, but its applicable only for  the dataframes 'SICILY','KK','LAURIS','SPLIT','PETE' (Im taking the 4th column values )

def datacleaner(df): 
    df["Time"] =  df.iloc[:, 0].apply(lambda x:x.split(';')[0])
    df["frequency - 50"] = df.iloc[:, 0].apply(lambda y:y.split(';')[3])
    df.drop(columns=df.columns[0], axis=1, inplace=True)
    df['Time'] =  pd.to_datetime(df['Time'], format="%Y-%m-%d %H:%M:%S")
    df = df.set_index(['Time'])
    return df 


lis = [ "Cape Town","College Station, Texas","Las Palmas de Gran Canaria, Canary Islands","Lisbon","London","Palma de Mallorca, Balearic Islands","Reykjavík","Salt Lake City, Utah","Stockholm","Tallinn","Vestmanna"]
names = ['CAPE','TEXAS','CANARY','LISBON','LONDON','BAL','REYK','SALT','STOCK','TALLIN','VEST']

#For the following the data has nan values, taking the second column values #I realised it later

list1 = [ "Erice, Sicily","Krakau","Lauris","Split","St. Petersburg"]
names1 = ['SICILY','KK','LAURIS','SPLIT','PETE']


count = 0 
location = r'C:\\Users\\Harpreet Singh\\Downloads\\'             #Sets the location 
for i,j in zip(lis,names):                                       #loop to import and assign their respective names to the dataframes 
    globals()[j] = pd.read_csv(location+ lis[count] +'.csv')
    count = count + 1 
    
count = 0 
for i,j in zip(list1,names1): 
    globals()[j] = pd.read_csv(location+ list1[count] +'.csv')
    count = count + 1 
    
dfnames1 = [SICILY,KK,LAURIS,SPLIT,PETE]
    
dfnames = [CAPE,TEXAS,CANARY,LISBON,LONDON,BAL,SALT,STOCK,TALLIN,VEST] #REYK is removed because it does not need cleaning


for i in range(len(dfnames)):
    dataclean(dfnames[i])          #Data Cleaned for every dataframe except for REYK 
    
    
for i in range(len(dfnames1)):   #Need to optimize the code later
    datacleaner(dfnames1[i]) 
    
#FInd a way to optimize this, tried but didnot work 

#In this im just takin 11th hour of any random day whichever is available in order to draw soem comparison 

CAPE = CAPE.set_index(['Time'])
CAPE = CAPE[(CAPE.index.day == 20) & (CAPE.index.hour == 11 )] 

TEXAS = TEXAS.set_index(['Time'])
TEXAS = TEXAS[(TEXAS.index.day == 15) & (TEXAS.index.hour == 11)] 


CANARY = CANARY.set_index(['Time'])
CANARY = CANARY[(CANARY.index.day == 4) & (CANARY.index.hour == 11)] 


LISBON = LISBON.set_index(['Time'])
LISBON = LISBON[(LISBON.index.day == 20) & (LISBON.index.hour == 11)] 


LONDON = LONDON.set_index(['Time'])
LONDON = LONDON[(LONDON.index.day == 4) & (LONDON.index.hour == 11)] 

BAL = BAL.set_index(['Time'])
BAL = BAL[(BAL.index.day == 31) & (BAL.index.hour == 11)] 


SALT = SALT.set_index(['Time'])
SALT = SALT[(SALT.index.day == 20) & (SALT.index.hour == 11)] 

STOCK = STOCK.set_index(['Time'])
STOCK = STOCK[(STOCK.index.day == 12) & (STOCK.index.hour == 11)] 

TALLIN = TALLIN.set_index(['Time'])
TALLIN = TALLIN[(TALLIN.index.day == 26) & (TALLIN.index.hour == 11)] 

VEST = VEST.set_index(['Time'])
VEST = VEST[(VEST.index.day == 4) & (VEST.index.hour == 11)] 


SICILY = SICILY.set_index(['Time'])
SICILY = SICILY[(SICILY.index.day == 2) & (SICILY.index.hour == 11)] 

KK = KK.set_index(['Time'])
KK = KK[(KK.index.day == 4) & (KK.index.hour == 11)] 

LAURIS = LAURIS.set_index(['Time'])
LAURIS = LAURIS[(LAURIS.index.day == 27) & (LAURIS.index.hour == 11)] 

SPLIT = SPLIT.set_index(['Time'])
SPLIT = SPLIT[(SPLIT.index.day == 12) & (SPLIT.index.hour == 11)] 

PETE = PETE.set_index(['Time'])
PETE = PETE[(PETE.index.day == 12) & (PETE.index.hour == 11)] 

#Only BAL has 7200 rows so not considering it 
REYK = pd.to_datetime(REYK['Time'], format="%d-%m-%Y %H:%M")

#DATA CLEANING FOR REYK

REYK = pd.read_csv('C:\\Users\\Harpreet Singh\\Downloads\\Reykjavík.csv')
REYK['Time'] =  pd.to_datetime(REYK['Time'], format="%d-%m-%Y %H:%M")
REYK = REYK.set_index(['Time'])
REYK = REYK[(REYK.index.day == 19) & (REYK.index.hour == 11)] 

CAPE['TIME'] = CAPE.index.time
CAPE = CAPE.reset_index() 

CAPE = CAPE.drop('Time', axis = 1)


CAPE['Freq-50'] = CAPE['frequency - 50']


CAPE = CAPE.drop('frequency - 50', axis = 1)


result_df = pd.concat([CAPE.reset_index(),TEXAS.reset_index().iloc[:,1],CANARY.reset_index().iloc[:,1],LISBON.reset_index().iloc[:,1],SALT.reset_index().iloc[:,1],STOCK.reset_index().iloc[:,1],TALLIN.reset_index().iloc[:,1],VEST.reset_index().iloc[:,1],REYK.reset_index().iloc[:,1],LONDON.reset_index().iloc[:,1]], axis=1)

result_df1 = pd.concat([SICILY.reset_index().iloc[:,1],KK.reset_index().iloc[:,1],LAURIS.reset_index().iloc[:,1],SPLIT.reset_index().iloc[:,1],PETE.reset_index().iloc[:,1]], axis=1)

result_final = pd.concat([result_df, result_df1],axis=1)



os.makedirs('folder/subfolder', exist_ok=True)  

result_final.to_csv('folder/subfolder/final1.csv')  

