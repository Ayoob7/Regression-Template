# Pandas is a library used to load and manipulate data, it has many statistical functions like, mean , moving averages etc
# It also has its own Plotting library called pandasplotlib
from os import path
import pandas as pd

fName = path.expanduser("track.csv")

openFile = pd.read_csv(fName)

#Open File
print(openFile)

#Print columns
print(openFile.columns)

# print Info
print(openFile.info())

# print header
print(openFile.head())

#When writing time use a known format ex - RFC 3339 to parse time use the following and give the coloumn name
df = pd.read_csv(fName,parse_dates=['time'])

#take index of the table as the time column
df.index = df['time']

# Data types in the file
print(df.dtypes)

#picking columns from the table
print(df[['lat','lng']])

#picking columns from the table and selected rows
print(df[['lat','lng']][2:27])

#picking columns from the table
print("Taking values")
print(df.loc['2015-08-20 03:48'])

#import pytz to change the TimeZone of the time column
import pytz

# changing UTC time to Sri Lankan time
ts = df['time']
localizedTime = ts.tz_localize(pytz.UTC)
sriLankanTime = localizedTime.tz_convert(pytz.timezone('Asia/Colombo'))
print(sriLankanTime)
