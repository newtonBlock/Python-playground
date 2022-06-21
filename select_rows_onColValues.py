import pandas as pd 

raw_data = {
    'name': ['William Morris', 'Al Jennings', 'Omar Mullins', 'Spencer McDaniel'],
    'age': [20, 19, 22, 21],
    'favorite_color': ['blue', 'yellow', 'green', 'yellow'],
    'grade': [88, 92, 95, 70],
    'sex': ['male', 'female', 'male', 'female']
} 

df = pd.DataFrame(raw_data)
tmp = df.head()

df2 = pd.DataFrame(raw_data)

#select rows based on column value
tmp = df.loc[df['favorite_color'] == 'yellow']

print(tmp)

#merge(join) two data frames on multiple columns
new_df = pd.merge(df, df2, how = 'left', left_on=['name', 'age'], right_on = [
    'name', 'age'])

#get dataframe all kinds of size
df.info()
list1 = []
tmp = len(df)
list1.append(tmp)
tmp = len(df.columns)
list1.append(tmp)
tmp = df.shape
list1.append(tmp)
tmp = df.size
list1.append(tmp)

print(list1)