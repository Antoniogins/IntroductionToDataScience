# Introduction to Pandas & NumPy

In this chapter, it is shown and described the process to learn Pandas & NumPy from zero, teaching step-by-step

## 🐼 Pandas 🐼

Pandas is a Python library develop to empower fast data manipulation and analysis. It has 2 main classes to work with: [`Series`](#Series-Section) & [`DataFrames`](#dataframes).

## Series

Series is a one-dimensional labeled array capable of holding any data type (integers, strings, floating point numbers, Python objects, etc.). The axis labels are collectively referred to as the index and are optional.

Full documentation: [pandas.Series](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html)

### Creating a Series

- [Creating a Series from a list](#Creating-a-Series-from-a-list)
- [Creating a Series with custom index](#Creating-a-Series-with-custom-index)
- [Creating a Series from a dictionary](#Creating-a-Series-from-a-dictionary)
- [Accessing Series elements by index](#Accessing-Series-elements-by-index)
- [Slicing Series](#Slicing-Series)
- [Filtering Series](#Filtering-Series)
- [Operations with Series](#Operations-with-Series)
- [Union of two Series](#Union-of-two-Series)
- [Applying functions to Series](#Applying-functions-to-Series)
- [Checking if a value is in the Series](#Checking-if-a-value-is-in-the-Series)
- [Converting Series to dictionary](#Converting-Series-to-dictionary)
- [Converting Series to list](#Converting-Series-to-list)
- [Converting Series to NumPy array](#Converting-Series-to-NumPy-array)
- [Converting Series to DataFrame](#Converting-Series-to-DataFrame)
- [Common functions with Series](#Common-functions-with-Series)
- [Handling missing values in Series](#Handling-missing-values-in-Series)
- [Common statistics with Series](#Common-statistics-with-Series)
- [Plotting Series](#Plotting-Series)
- [Dropping duplicates in Series](#Dropping-duplicates-in-Series)
- [Filling missing values in Series](#Filling-missing-values-in-Series)
- [Dropping missing values in Series](#Dropping-missing-values-in-Series)
- [Filling missing values in Series automatically](#Filling-missing-values-in-Series-automatically)
- [Interpolating missing values in Series](#Interpolating-missing-values-in-Series)
- [Replacing values in Series](#Replacing-values-in-Series)
- [Dropping duplicates in Series](#Dropping-duplicates-in-Series)
- [Common statistics with Series](#Common-statistics-with-Series)

#### Creating a Series from a list

```python
import pandas as pd

# Creating a Series
s = pd.Series([1, 3, 5, 7, 9])
print(s)
```

```plaintext
0    1
1    3
2    5
3    7
4    9
dtype: int64
```

#### Creating a Series with custom index

```python
# Creating a Series with custom index
s = pd.Series(
    [1, 3, 5, 7, 9],
    index=['a', 'b', 'c', 'd', 'e'],
    name='Series 1'
)
print(s)
```

```plaintext
a    1
b    3
c    5
d    7
e    9
Name: Series 1, dtype: int64
```

#### Creating a Series from a dictionary

```python
# Creating a Series from a dictionary
d = {'a': 1, 'b': 3, 'c': 5, 'd': 7, 'e': 9}
s = pd.Series(d)
print(s)
```

```plaintext
a    1
b    3
c    5
d    7
e    9
dtype: int64
```

#### Accessing Series elements by index

```python
# Accessing elements
print(s['a'])
```

```plaintext
1
```

#### Slicing Series

```python
# Slicing
print(s[1:3])
```

```plaintext
b    3
c    5
dtype: int64
```

#### Filtering Series

```python
# Filtering
print(s[s > 5])
```

```plaintext
d    7
e    9
dtype: int64
```

#### Operations with Series

```python
# Operations
print(s + 2)
```

```plaintext
a     3
b     5
c     7
d     9
e    11
dtype: int64
```

#### Union of two Series

```python
# Union of two Series
s1 = pd.Series(
    [1, 2, 3],
    index=['a', 'b', 'c']
)
s2 = pd.Series(
    [4, 5, 6],
    index=['b', 'c', 'd']
)

print(s1 + s2)
```

```plaintext
a    NaN
b    6.0
c    8.0
d    NaN
dtype: float64
```

#### Applying functions to Series

```python
# Applying functions
print(s.apply(lambda x: x ** 2))
```

```plaintext
a     1
b     9
c    25
d    49
e    81
dtype: int64
```

#### Checking if a value is in the Series

```python
# Checking if a value is in the Series
print('a' in s)
```

```plaintext
True
```

#### Converting Series to dictionary

```python
# Converting to a dictionary
print(s.to_dict())
```

```plaintext
{'a': 1, 'b': 3, 'c': 5, 'd': 7, 'e': 9}
```

#### Converting Series to list

```python
# Converting to a list
print(s.tolist())
```

```plaintext
[1, 3, 5, 7, 9]
```

#### Converting Series to NumPy array

```python
# Converting to a numpy array
print(s.to_numpy())
```

```plaintext
[1 3 5 7 9]
```

#### Converting Series to DataFrame

```python
# Converting to a DataFrame
print(s.to_frame())
```

```plaintext
   0
a  1
b  3
c  5
d  7
e  9
```

#### Common functions with Series

#### Describing Series

```python
# Common functions
print(s.describe())
```

```plaintext
count    5.000000
mean     5.000000
std      3.162278
min      1.000000
25%      3.000000
50%      5.000000
75%      7.000000
max      9.000000
Name: Series 1, dtype: float64
```

#### Sorting Series

```python
# Sorting
print(s.sort_values())
```

```plaintext
a    1
b    3
c    5
d    7
e    9
Name: Series 1, dtype: int64
```

#### Plotting Series

```python
# Plotting
s.plot()
```

```plaintext
<matplotlib.axes._subplots.AxesSubplot at 0x7f8e3e3e3f10>
```

#### Handling missing values in Series

#### Filling missing values in Series

```python
# Filling missing values
s1 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
s2 = pd.Series([4, 5, 6], index=['b', 'c', 'd'])

print(s1.add(s2, fill_value=0))
```

```plaintext
a    1.0
b    6.0
c    8.0
d    6.0
dtype: float64
```

#### Dropping missing values in Series

```python
# Dropping missing values
s = pd.Series([1, 2, 3, None, 5])
print(s.dropna())
```

```plaintext
0    1.0
1    2.0
2    3.0
4    5.0
dtype: float64
```

#### Filling missing values in Series automatically
```python
# Filling missing values
print(s.fillna(0))
```

```plaintext
0    1.0
1    2.0
2    3.0
3    0.0
4    5.0
dtype: float64
```

#### Interpolating missing values in Series

```python
# Interpolating missing values
print(s.interpolate())
```

```plaintext
0    1.0
1    2.0
2    3.0
3    4.0
4    5.0
dtype: float64
```

#### Replacing values in Series

```python
# Replacing values
print(s.replace(3, 4))
```

```plaintext
0    1.0
1    2.0
2    4.0
3    NaN
4    5.0
dtype: float64
```

#### Dropping duplicates in Series

```python
# Dropping duplicates
s = pd.Series([1, 2, 3, 3, 4, 5, 5, 6])
print(s.drop_duplicates())
```

```plaintext
0    1
1    2
2    3
4    4
5    5
7    6
dtype: int64
```

#### Common statistics with Series

```python
# Summing values
print(f" - Sum: {s.sum()}")
print(f" - Mean: {s.mean()}")
print(f" - Median: {s.median()}")
print(f" - Mode:{s.mode()}")
print(f" - Standard deviation: {s.std()}")
print(f" - Variance: {s.var()}")
print(f" - Minimum: {s.min()}")
print(f" - Maximum: {s.max()}")
print(f" - Count: {s.count()}")
```

```plaintext
 - Sum: 24
 - Mean: 3.4285714285714284
 - Median: 3.0
 - Mode: 
 0    3
 1    5
 - dtype: int64
 - Standard deviation: 1.7204650534085253
 - Variance: 2.9523809523809526
 - Minimum: 1
 - Maximum: 6
 - Count: 7
```

## DataFrames

A DataFrame is a 2-dimensional labeled data structure with columns of potentially different types. You can think of it like a spreadsheet or SQL table, or a dict of Series objects.

It is commonly thought of as a dict-like container for Series objects. It is the most commonly used pandas object. Each column is a Pandas Series, and the rows are the elements inside the Series, correlating by the index.

Full documentation: [pandas.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html)

```python
import pandas as pd

# Creating Series objects
s1 = pd.Series([1, 2, 3], name='Series 1', index=['a', 'b', 'c'])
s2 = pd.Series([4, 5, 6], name='Series 2', index=['a', 'b', 'c'])
s3 = pd.Series([7, 8, 9], name='Series 3', index=['a', 'b', 'c'])

# Creating DataFrame from Series
df = pd.DataFrame({'Column 1': s1, 'Column 2': s2, 'Column 3': s3})

# Displaying the DataFrame
print(df)
```

```plaintext
   Column 1  Column 2  Column 3
a         1         4         7
b         2         5         8
c         3         6         9
```

Like Series, DataFrame accepts many different kinds of input:

- Vector of data
- Iterable (list, tuple, etc.)
- Dictionary
- Scalar value (which will be broadcasted)
- DataFrame

It can also receive a name for the index and columns, and a name for the DataFrame itself.

```python
# Creating a DataFrame from a dictionary
df = pd.DataFrame(
    {
        'Column 1': [1, 2, 3],
        'Column 2': [4, 5, 6],
        'Column 3': [7, 8, 9],
    },
    index=['a', 'b', 'c'],
    columns=['Column 1', 'Column 2', 'Column 3'],
    name='DataFrame 1',
)
print(df)
```

```plaintext
   Column 1  Column 2  Column 3
a         1         4         7
b         2         5         8
c         3         6         9
```

Some details about the DataFrame:

- If no index is passed, one will be created having values [0, ..., len(data) - 1] `(integer index)`
- It has a `shape` attribute, which is a tuple with the number of rows and columns
- It has an `index` attribute, which is the index of the DataFrame
- It has a `columns` attribute, which is the columns of the DataFrame
- It has a `values` attribute, which is a 2D NumPy array with the values of the DataFrame

Each column in a DataFrame is a Series, and the columns can be accessed by their names.

```python
# Accessing columns
print(df['Column 1'])
```

```plaintext
a    1
b    2
c    3
Name: Column 1, dtype: int64
```

```python
# Accessing rows
print(df.loc['a'])
```

```plaintext
Column 1    1
Column 2    4
Column 3    7
Name: a, dtype: int64
```

```python
# Accessing elements
print(df.at['a', 'Column 1']) # row, column
```

```plaintext
1
```

```python
# Slicing
print(df[1:3]) # rows 1 to 3 (exclusive)
```

```plaintext
   Column 1  Column 2  Column 3
b         2         5         8
c         3         6         9
```

```python
# Filtering
print(df[df['Column 1'] > 1])
```

```plaintext
   Column 1  Column 2  Column 3
b         2         5         8
c         3         6         9
```

Examples of creating DataFrames from different inputs:

```python
# Creating a DataFrame from a list of lists
df = pd.DataFrame(
    [
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9],
    ],
    index=['a', 'b', 'c'],
    columns=['Column 1', 'Column 2', 'Column 3'],
)
print(df)
```

```plaintext
   Column 1  Column 2  Column 3
a         1         4         7
b         2         5         8
c         3         6         9
```

```python
# Creating a DataFrame from a list of dictionaries
df = pd.DataFrame(
    [
        {'Column 1': 1, 'Column 2': 4, 'Column 3': 7},
        {'Column 1': 2, 'Column 2': 5, 'Column 3': 8},
        {'Column 1': 3, 'Column 2': 6, 'Column 3': 9},
    ],
    index=['a', 'b', 'c'],
)
print(df)
```

```plaintext
   Column 1  Column 2  Column 3
a         1         4         7
b         2         5         8
c         3         6         9
```

```python
# Creating a DataFrame from a dictionary of lists
df = pd.DataFrame(
    {
        'Column 1': [1, 2, 3],
        'Column 2': [4, 5, 6],
        'Column 3': [7, 8, 9],
    },
    index=['a', 'b', 'c'],
)
print(df)
```

```plaintext
   Column 1  Column 2  Column 3
a         1         4         7
b         2         5         8
c         3         6         9
```

```python
# Creating a DataFrame from a dictionary of dictionaries
df = pd.DataFrame(
    {
        'Column 1': {'a': 1, 'b': 2, 'c': 3},
        'Column 2': {'a': 4, 'b': 5, 'c': 6},
        'Column 3': {'a': 7, 'b': 8, 'c': 9},
    }
)
print(df)
```

```plaintext
   Column 1  Column 2  Column 3
a         1         4         7
b         2         5         8
c         3         6         9
```

```python
# Creating a DataFrame from a dictionary of Series
s1 = pd.Series([1, 2, 3], name='Column 1', index=['a', 'b', 'c'])
s2 = pd.Series([4, 5, 6], name='Column 2', index=['a', 'b', 'c'])
s3 = pd.Series([7, 8, 9], name='Column 3', index=['a', 'b', 'c'])

df = pd.DataFrame(
    {
        'Column 1': s1,
        'Column 2': s2,
        'Column 3': s3
    }
)
print(df)
```

```plaintext
   Column 1  Column 2  Column 3
a         1         4         7
b         2         5         8
c         3         6         9
```

