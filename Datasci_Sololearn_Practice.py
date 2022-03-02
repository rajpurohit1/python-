#numpy libraries
# you can also use indexing in numpy array 
import numpy as np

x = np.arange(1, 10)

print(x[0:2])
print(x[5:])
print(x[:2])
print(x[-3:])


# Also use condintion in the arry 

print(x[x<4])

print(x[(x>5) & (x%2==0)])

# There is many array operation so you can use them for small mathematics opration 
print(x.sum())
print(x.min())
print(x.max())
#print(x.pop())  # it will give an error because it is not under numpy L
print(x)

#Dataframe is one of  the importent concept of the Pandas libraries
#we can create data frame by dictionery and made a dataframe 
#dataframes is collection of series
#dataframe gives you a mulltidimentional table with by default index
import pandas as pd

data = {
   'ages': [14, 18, 24, 42],
   'heights': [165, 180, 176, 184]
}

df = pd.DataFrame(data)
print(df)


#you can use indexing in the table 

print("print ages row:")

print(df["ages"],df['heights'])

#Also we can add our own index in the table 

df = pd.DataFrame(data, index=['James', 'Bob', 'Amy', 'Dave'])

print(df[["ages", "heights"]])

#pandas use iloc d=function for slicing in the table 



# third row
print(df.iloc[2])

#first 3 rows
print(df.iloc[:3])

# rows 2 to 3
print(df.iloc[1:3])

#we can also give conditions to table and extract the data from table

print(df[(df['ages']>18) | (df['heights']>180)])
print(df[(df['ages']>18) & (df['heights']>180)])
#print(df[(df['ages']>18) - (df['heights']>180)]) you can use - opration in the table as per now i am not sure about it 

# we can read data from CSV file by using read_csv() function

#df = pd.read_csv("path")

import pandas as pd

df = pd.read_csv("https://www.sololearn.com/uploads/ca-covid.csv")

print(df)

#if we just want starting 10 data so we can use head() function and just extract 10 data from the file 

print(df.head())

#similer we can use tail() funtion for the last rowa of the data 

print(df.tail())

print(df[["date","state"]])

#now know about info() it will give you essential data about dataset like : 
#such as number of rows, columns, data types, etc:
    
print(df.info())

# we can also auto genrate our dataset index by using set_index() function

df.set_index("date",inplace=True)
print(df)

