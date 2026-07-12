[Skip to main content](https://spark.apache.org/docs/latest/api/python/getting_started/quickstart_df.html#main-content)
`⌘`+`K`
[ ![Logo image](https://spark.apache.org/images/spark-logo.png) ![Logo image](https://spark.apache.org/images/spark-logo-rev.svg) ](https://spark.apache.org/docs/latest/api/python/index.html)
Site Navigation
  * [ Overview ](https://spark.apache.org/docs/latest/api/python/index.html)
  * [ Getting Started ](https://spark.apache.org/docs/latest/api/python/getting_started/index.html)
  * [ Tutorials ](https://spark.apache.org/docs/latest/api/python/tutorial/index.html)
  * [ User Guide ](https://spark.apache.org/docs/latest/api/python/user_guide/index.html)
  * [ API Reference ](https://spark.apache.org/docs/latest/api/python/reference/index.html)
  * [ Development ](https://spark.apache.org/docs/latest/api/python/development/index.html)
More
  * [ Migration Guides ](https://spark.apache.org/docs/latest/api/python/migration_guide/index.html)

4.1.2
[4.0.1](https://spark.apache.org/docs/4.0.1/api/python/getting_started/quickstart_df.html)[4.0.0](https://spark.apache.org/docs/4.0.0/api/python/getting_started/quickstart_df.html)[3.5.7](https://spark.apache.org/docs/3.5.7/api/python/getting_started/quickstart_df.html)[3.5.5](https://spark.apache.org/docs/3.5.5/api/python/getting_started/quickstart_df.html)[3.5.4](https://spark.apache.org/docs/3.5.4/api/python/getting_started/quickstart_df.html)[3.5.3](https://spark.apache.org/docs/3.5.3/api/python/getting_started/quickstart_df.html)[3.5.2](https://archive.apache.org/dist/spark/docs/3.5.2/api/python/getting_started/quickstart_df.html)[3.5.1](https://archive.apache.org/dist/spark/docs/3.5.1/api/python/getting_started/quickstart_df.html)[3.5.0](https://archive.apache.org/dist/spark/docs/3.5.0/api/python/getting_started/quickstart_df.html)[3.4.4](https://archive.apache.org/dist/spark/docs/3.4.4/api/python/getting_started/quickstart_df.html)[3.4.3](https://archive.apache.org/dist/spark/docs/3.4.3/api/python/getting_started/quickstart_df.html)[3.4.2](https://archive.apache.org/dist/spark/docs/3.4.2/api/python/getting_started/quickstart_df.html)[3.4.1](https://archive.apache.org/dist/spark/docs/3.4.1/api/python/getting_started/quickstart_df.html)[3.4.0](https://archive.apache.org/dist/spark/docs/3.4.0/api/python/getting_started/quickstart_df.html)[3.3.4](https://archive.apache.org/dist/spark/docs/3.3.4/api/python/getting_started/quickstart_df.html)[3.3.3](https://archive.apache.org/dist/spark/docs/3.3.3/api/python/getting_started/quickstart_df.html)[3.3.2](https://archive.apache.org/dist/spark/docs/3.3.2/api/python/getting_started/quickstart_df.html)[3.3.1](https://archive.apache.org/dist/spark/docs/3.3.1/api/python/getting_started/quickstart_df.html)[3.3.0](https://archive.apache.org/dist/spark/docs/3.3.0/api/python/getting_started/quickstart_df.html)
  * [ GitHub](https://github.com/apache/spark)
  * [ PyPI](https://pypi.org/project/pyspark)

Site Navigation
  * [ Overview ](https://spark.apache.org/docs/latest/api/python/index.html)
  * [ Getting Started ](https://spark.apache.org/docs/latest/api/python/getting_started/index.html)
  * [ Tutorials ](https://spark.apache.org/docs/latest/api/python/tutorial/index.html)
  * [ User Guide ](https://spark.apache.org/docs/latest/api/python/user_guide/index.html)
  * [ API Reference ](https://spark.apache.org/docs/latest/api/python/reference/index.html)
  * [ Development ](https://spark.apache.org/docs/latest/api/python/development/index.html)
More
  * [ Migration Guides ](https://spark.apache.org/docs/latest/api/python/migration_guide/index.html)

4.1.2
  * [ GitHub](https://github.com/apache/spark)
  * [ PyPI](https://pypi.org/project/pyspark)

Section Navigation
  * [Installation](https://spark.apache.org/docs/latest/api/python/getting_started/install.html)
  * [Quickstart: DataFrame](https://spark.apache.org/docs/latest/api/python/getting_started/quickstart_df.html)
  * [Quickstart: Spark Connect](https://spark.apache.org/docs/latest/api/python/getting_started/quickstart_connect.html)
  * [Quickstart: Pandas API on Spark](https://spark.apache.org/docs/latest/api/python/getting_started/quickstart_ps.html)
  * [Testing PySpark](https://spark.apache.org/docs/latest/api/python/getting_started/testing_pyspark.html)

  * [ ](https://spark.apache.org/docs/latest/api/python/index.html)
  * [Getting Started](https://spark.apache.org/docs/latest/api/python/getting_started/index.html)
  * Quickstart: DataFrame

# Quickstart: DataFrame[#](https://spark.apache.org/docs/latest/api/python/getting_started/quickstart_df.html#Quickstart:-DataFrame "Permalink to this headline")
This is a short introduction and quickstart for the PySpark DataFrame API. PySpark DataFrames are lazily evaluated. They are implemented on top of [RDD](https://spark.apache.org/docs/latest/rdd-programming-guide.html#overview)s. When Spark [transforms](https://spark.apache.org/docs/latest/rdd-programming-guide.html#transformations) data, it does not immediately compute the transformation but plans how to compute later. When [actions](https://spark.apache.org/docs/latest/rdd-programming-guide.html#actions) such as `collect()` are explicitly called, the computation starts. This notebook shows the basic usages of the DataFrame, geared mainly for new users. You can run the latest version of these examples by yourself in ‘Live Notebook: DataFrame’ at [the quickstart page](https://spark.apache.org/docs/latest/api/python/getting_started/index.html).
There is also other useful information in Apache Spark documentation site, see the latest version of [Spark SQL and DataFrames](https://spark.apache.org/docs/latest/sql-programming-guide.html), [RDD Programming Guide](https://spark.apache.org/docs/latest/rdd-programming-guide.html), [Structured Streaming Programming Guide](https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html), [Spark Streaming Programming Guide](https://spark.apache.org/docs/latest/streaming-programming-guide.html) and [Machine Learning Library (MLlib) Guide](https://spark.apache.org/docs/latest/ml-guide.html).
PySpark applications start with initializing `SparkSession` which is the entry point of PySpark as below. In case of running it in PySpark shell via pyspark executable, the shell automatically creates the session in the variable spark for users.

```
[1]:

```
Copy to clipboard

```
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

```
Copy to clipboard
## DataFrame Creation[#](https://spark.apache.org/docs/latest/api/python/getting_started/quickstart_df.html#DataFrame-Creation "Permalink to this headline")
A PySpark DataFrame can be created via `pyspark.sql.SparkSession.createDataFrame` typically by passing a list of lists, tuples, dictionaries and `pyspark.sql.Row`s, a [pandas DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html) and an RDD consisting of such a list. `pyspark.sql.SparkSession.createDataFrame` takes the `schema` argument to specify the schema of the DataFrame. When it is omitted, PySpark infers the corresponding schema by taking a sample from the data.
Firstly, you can create a PySpark DataFrame from a list of rows

```
[2]:

```
Copy to clipboard

```
from datetime import datetime, date
import pandas as pd
from pyspark.sql import Row

df = spark.createDataFrame([
    Row(a=1, b=2., c='string1', d=date(2000, 1, 1), e=datetime(2000, 1, 1, 12, 0)),
    Row(a=2, b=3., c='string2', d=date(2000, 2, 1), e=datetime(2000, 1, 2, 12, 0)),
    Row(a=4, b=5., c='string3', d=date(2000, 3, 1), e=datetime(2000, 1, 3, 12, 0))
])
df

```
Copy to clipboard

```
[2]:

```
Copy to clipboard

```
DataFrame[a: bigint, b: double, c: string, d: date, e: timestamp]

```
Copy to clipboard
Create a PySpark DataFrame with an explicit schema.

```
[3]:

```
Copy to clipboard

```
df = spark.createDataFrame([
    (1, 2., 'string1', date(2000, 1, 1), datetime(2000, 1, 1, 12, 0)),
    (2, 3., 'string2', date(2000, 2, 1), datetime(2000, 1, 2, 12, 0)),
    (3, 4., 'string3', date(2000, 3, 1), datetime(2000, 1, 3, 12, 0))
], schema='a long, b double, c string, d date, e timestamp')
df

```
Copy to clipboard

```
[3]:

```
Copy to clipboard

```
DataFrame[a: bigint, b: double, c: string, d: date, e: timestamp]

```
Copy to clipboard
Create a PySpark DataFrame from a pandas DataFrame

```
[4]:

```
Copy to clipboard

```
pandas_df = pd.DataFrame({
    'a': [1, 2, 3],
    'b': [2., 3., 4.],
    'c': ['string1', 'string2', 'string3'],
    'd': [date(2000, 1, 1), date(2000, 2, 1), date(2000, 3, 1)],
    'e': [datetime(2000, 1, 1, 12, 0), datetime(2000, 1, 2, 12, 0), datetime(2000, 1, 3, 12, 0)]
})
df = spark.createDataFrame(pandas_df)
df

```
Copy to clipboard

```
[4]:

```
Copy to clipboard

```
DataFrame[a: bigint, b: double, c: string, d: date, e: timestamp]

```
Copy to clipboard
The DataFrames created above all have the same results and schema.

```
[6]:

```
Copy to clipboard

```
# All DataFrames above result same.
df.show()
df.printSchema()

```
Copy to clipboard

```
+---+---+-------+----------+-------------------+
|  a|  b|      c|         d|                  e|
+---+---+-------+----------+-------------------+
|  1|2.0|string1|2000-01-01|2000-01-01 12:00:00|
|  2|3.0|string2|2000-02-01|2000-01-02 12:00:00|
|  3|4.0|string3|2000-03-01|2000-01-03 12:00:00|
+---+---+-------+----------+-------------------+

root
 |-- a: long (nullable = true)
 |-- b: double (nullable = true)
 |-- c: string (nullable = true)
 |-- d: date (nullable = true)
 |-- e: timestamp (nullable = true)

```
Copy to clipboard
## Viewing Data[#](https://spark.apache.org/docs/latest/api/python/getting_started/quickstart_df.html#Viewing-Data "Permalink to this headline")
The top rows of a DataFrame can be displayed using `DataFrame.show()`.

```
[7]:

```
Copy to clipboard

```
df.show(1)

```
Copy to clipboard

```
+---+---+-------+----------+-------------------+
|  a|  b|      c|         d|                  e|
+---+---+-------+----------+-------------------+
|  1|2.0|string1|2000-01-01|2000-01-01 12:00:00|
+---+---+-------+----------+-------------------+
only showing top 1 row

```
Copy to clipboard
Alternatively, you can enable `spark.sql.repl.eagerEval.enabled` configuration for the eager evaluation of PySpark DataFrame in notebooks such as Jupyter. The number of rows to show can be controlled via `spark.sql.repl.eagerEval.maxNumRows` configuration.

```
[8]:

```
Copy to clipboard

```
spark.conf.set('spark.sql.repl.eagerEval.enabled', True)
df

```
Copy to clipboard

```
[8]:

```
Copy to clipboard
| a  | b  | c  | d  | e  |
| --- | --- | --- | --- | --- |
| 1  | 2.0  | string1  | 2000-01-01  | 2000-01-01 12:00:00  |
| 2  | 3.0  | string2  | 2000-02-01  | 2000-01-02 12:00:00  |
| 3  | 4.0  | string3  | 2000-03-01  | 2000-01-03 12:00:00  |
The rows can also be shown vertically. This is useful when rows are too long to show horizontally.

```
[9]:

```
Copy to clipboard

```
df.show(1, vertical=True)

```
Copy to clipboard

```
-RECORD 0------------------
 a   | 1
 b   | 2.0
 c   | string1
 d   | 2000-01-01
 e   | 2000-01-01 12:00:00
only showing top 1 row

```
Copy to clipboard
You can see the DataFrame’s schema and column names as follows:

```
[10]:

```
Copy to clipboard

```
df.columns

```
Copy to clipboard

```
[10]:

```
Copy to clipboard

```
['a', 'b', 'c', 'd', 'e']

```
Copy to clipboard

```
[11]:

```
Copy to clipboard

```
df.printSchema()

```
Copy to clipboard

```
root
 |-- a: long (nullable = true)
 |-- b: double (nullable = true)
 |-- c: string (nullable = true)
 |-- d: date (nullable = true)
 |-- e: timestamp (nullable = true)

```
Copy to clipboard
Show the summary of the DataFrame

```
[12]:

```
Copy to clipboard

```
df.select("a", "b", "c").describe().show()

```
Copy to clipboard

```
+-------+---+---+-------+
|summary|  a|  b|      c|
+-------+---+---+-------+
|  count|  3|  3|      3|
|   mean|2.0|3.0|   null|
| stddev|1.0|1.0|   null|
|    min|  1|2.0|string1|
|    max|  3|4.0|string3|
+-------+---+---+-------+

```
Copy to clipboard
`DataFrame.collect()` collects the distributed data to the driver side as the local data in Python. Note that this can throw an out-of-memory error when the dataset is too large to fit in the driver side because it collects all the data from executors to the driver side.

```
[13]:

```
Copy to clipboard

```
df.collect()

```
Copy to clipboard

```
[13]:

```
Copy to clipboard

```
[Row(a=1, b=2.0, c='string1', d=datetime.date(2000, 1, 1), e=datetime.datetime(2000, 1, 1, 12, 0)),
 Row(a=2, b=3.0, c='string2', d=datetime.date(2000, 2, 1), e=datetime.datetime(2000, 1, 2, 12, 0)),
 Row(a=3, b=4.0, c='string3', d=datetime.date(2000, 3, 1), e=datetime.datetime(2000, 1, 3, 12, 0))]

```
Copy to clipboard
In order to avoid throwing an out-of-memory exception, use `DataFrame.take()` or `DataFrame.tail()`.

```
[14]:

```
Copy to clipboard

```
df.take(1)

```
Copy to clipboard

```
[14]:

```
Copy to clipboard

```
[Row(a=1, b=2.0, c='string1', d=datetime.date(2000, 1, 1), e=datetime.datetime(2000, 1, 1, 12, 0))]

```
Copy to clipboard
PySpark DataFrame also provides the conversion back to a [pandas DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html) to leverage pandas API. Note that `toPandas` also collects all data into the driver side that can easily cause an out-of-memory-error when the data is too large to fit into the driver side.

```
[15]:

```
Copy to clipboard

```
df.toPandas()

```
Copy to clipboard

```
[15]:

```
Copy to clipboard
|   | a  | b  | c  | d  | e  |
| --- | --- | --- | --- | --- | --- |
| 0  | 1  | 2.0  | string1  | 2000-01-01  | 2000-01-01 12:00:00  |
| 1  | 2  | 3.0  | string2  | 2000-02-01  | 2000-01-02 12:00:00  |
| 2  | 3  | 4.0  | string3  | 2000-03-01  | 2000-01-03 12:00:00  |
## Selecting and Accessing Data[#](https://spark.apache.org/docs/latest/api/python/getting_started/quickstart_df.html#Selecting-and-Accessing-Data "Permalink to this headline")
PySpark DataFrame is lazily evaluated and simply selecting a column does not trigger the computation but it returns a `Column` instance.

```
[16]:

```
Copy to clipboard

```
df.a

```
Copy to clipboard

```
[16]:

```
Copy to clipboard

```
Column<b'a'>

```
Copy to clipboard
In fact, most of column-wise operations return `Column`s.

```
[17]:

```
Copy to clipboard

```
from pyspark.sql import Column
from pyspark.sql.functions import upper

type(df.c) == type(upper(df.c)) == type(df.c.isNull())

```
Copy to clipboard

```
[17]:

```
Copy to clipboard

```
True

```
Copy to clipboard
These `Column`s can be used to select the columns from a DataFrame. For example, `DataFrame.select()` takes the `Column` instances that returns another DataFrame.

```
[18]:

```
Copy to clipboard

```
df.select(df.c).show()

```
Copy to clipboard

```
+-------+
|      c|
+-------+
|string1|
|string2|
|string3|
+-------+

```
Copy to clipboard
Assign new `Column` instance.

```
[19]:

```
Copy to clipboard

```
df.withColumn('upper_c', upper(df.c)).show()

```
Copy to clipboard

```
+---+---+-------+----------+-------------------+-------+
|  a|  b|      c|         d|                  e|upper_c|
+---+---+-------+----------+-------------------+-------+
|  1|2.0|string1|2000-01-01|2000-01-01 12:00:00|STRING1|
|  2|3.0|string2|2000-02-01|2000-01-02 12:00:00|STRING2|
|  3|4.0|string3|2000-03-01|2000-01-03 12:00:00|STRING3|
+---+---+-------+----------+-------------------+-------+

```
Copy to clipboard
To select a subset of rows, use `DataFrame.filter()`.

```
[20]:

```
Copy to clipboard

```
df.filter(df.a == 1).show()

```
Copy to clipboard

```
+---+---+-------+----------+-------------------+
|  a|  b|      c|         d|                  e|
+---+---+-------+----------+-------------------+
|  1|2.0|string1|2000-01-01|2000-01-01 12:00:00|
+---+---+-------+----------+-------------------+

```
Copy to clipboard
## Applying a Function[#](https://spark.apache.org/docs/latest/api/python/getting_started/quickstart_df.html#Applying-a-Function "Permalink to this headline")
PySpark supports various UDFs and APIs to allow users to execute Python native functions. See also the latest [Pandas UDFs](https://spark.apache.org/docs/latest/sql-pyspark-pandas-with-arrow.html#pandas-udfs-aka-vectorized-udfs) and [Pandas Function APIs](https://spark.apache.org/docs/latest/sql-pyspark-pandas-with-arrow.html#pandas-function-apis). For instance, the example below allows users to directly use the APIs in [a pandas Series](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html) within Python native function.

```
[21]:

```
Copy to clipboard

```
import pandas as pd
from pyspark.sql.functions import pandas_udf

@pandas_udf('long')
def pandas_plus_one(series: pd.Series) -> pd.Series:
    # Simply plus one by using pandas Series.
    return series + 1

df.select(pandas_plus_one(df.a)).show()

```
Copy to clipboard

```
+------------------+
|pandas_plus_one(a)|
+------------------+
|                 2|
|                 3|
|                 4|
+------------------+

```
Copy to clipboard
Another example is `DataFrame.mapInPandas` which allows users directly use the APIs in a [pandas DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html) without any restrictions such as the result length.

```
[22]:

```
Copy to clipboard

```
def pandas_filter_func(iterator):
    for pandas_df in iterator:
        yield pandas_df[pandas_df.a == 1]

df.mapInPandas(pandas_filter_func, schema=df.schema).show()

```
Copy to clipboard

```
+---+---+-------+----------+-------------------+
|  a|  b|      c|         d|                  e|
+---+---+-------+----------+-------------------+
|  1|2.0|string1|2000-01-01|2000-01-01 12:00:00|
+---+---+-------+----------+-------------------+

```
Copy to clipboard
## Grouping Data[#](https://spark.apache.org/docs/latest/api/python/getting_started/quickstart_df.html#Grouping-Data "Permalink to this headline")
PySpark DataFrame also provides a way of handling grouped data by using the common approach, split-apply-combine strategy. It groups the data by a certain condition applies a function to each group and then combines them back to the DataFrame.

```
[23]:

```
Copy to clipboard

```
df = spark.createDataFrame([
    ['red', 'banana', 1, 10], ['blue', 'banana', 2, 20], ['red', 'carrot', 3, 30],
    ['blue', 'grape', 4, 40], ['red', 'carrot', 5, 50], ['black', 'carrot', 6, 60],
    ['red', 'banana', 7, 70], ['red', 'grape', 8, 80]], schema=['color', 'fruit', 'v1', 'v2'])
df.show()

```
Copy to clipboard

```
+-----+------+---+---+
|color| fruit| v1| v2|
+-----+------+---+---+
|  red|banana|  1| 10|
| blue|banana|  2| 20|
|  red|carrot|  3| 30|
| blue| grape|  4| 40|
|  red|carrot|  5| 50|
|black|carrot|  6| 60|
|  red|banana|  7| 70|
|  red| grape|  8| 80|
+-----+------+---+---+

```
Copy to clipboard
Grouping and then applying the `avg()` function to the resulting groups.

```
[24]:

```
Copy to clipboard

```
df.groupby('color').avg().show()

```
Copy to clipboard

```
+-----+-------+-------+
|color|avg(v1)|avg(v2)|
+-----+-------+-------+
|  red|    4.8|   48.0|
|black|    6.0|   60.0|
| blue|    3.0|   30.0|
+-----+-------+-------+

```
Copy to clipboard
You can also apply a Python native function against each group by using pandas API.

```
[25]:

```
Copy to clipboard

```
def plus_mean(pandas_df):
    return pandas_df.assign(v1=pandas_df.v1 - pandas_df.v1.mean())

df.groupby('color').applyInPandas(plus_mean, schema=df.schema).show()

```
Copy to clipboard

```
+-----+------+---+---+
|color| fruit| v1| v2|
+-----+------+---+---+
|  red|banana| -3| 10|
|  red|carrot| -1| 30|
|  red|carrot|  0| 50|
|  red|banana|  2| 70|
|  red| grape|  3| 80|
|black|carrot|  0| 60|
| blue|banana| -1| 20|
| blue| grape|  1| 40|
+-----+------+---+---+

```
Copy to clipboard
Co-grouping and applying a function.

```
[26]:

```
Copy to clipboard

```
df1 = spark.createDataFrame(
    [(20000101, 1, 1.0), (20000101, 2, 2.0), (20000102, 1, 3.0), (20000102, 2, 4.0)],
    ('time', 'id', 'v1'))

df2 = spark.createDataFrame(
    [(20000101, 1, 'x'), (20000101, 2, 'y')],
    ('time', 'id', 'v2'))

def merge_ordered(l, r):
    return pd.merge_ordered(l, r)

df1.groupby('id').cogroup(df2.groupby('id')).applyInPandas(
    merge_ordered, schema='time int, id int, v1 double, v2 string').show()

```
Copy to clipboard

```
+--------+---+---+---+
|    time| id| v1| v2|
+--------+---+---+---+
|20000101|  1|1.0|  x|
|20000102|  1|3.0|  x|
|20000101|  2|2.0|  y|
|20000102|  2|4.0|  y|
+--------+---+---+---+

```
Copy to clipboard
## Getting Data In/Out[#](https://spark.apache.org/docs/latest/api/python/getting_started/quickstart_df.html#Getting-Data-In/Out "Permalink to this headline")
CSV is straightforward and easy to use. Parquet and ORC are efficient and compact file formats to read and write faster.
There are many other data sources available in PySpark such as JDBC, text, binaryFile, Avro, etc. See also the latest [Spark SQL, DataFrames and Datasets Guide](https://spark.apache.org/docs/latest/sql-programming-guide.html) in Apache Spark documentation.
### CSV[#](https://spark.apache.org/docs/latest/api/python/getting_started/quickstart_df.html#CSV "Permalink to this headline")

```
[27]:

```
Copy to clipboard

```
df.write.csv('foo.csv', header=True)
spark.read.csv('foo.csv', header=True).show()

```
Copy to clipboard

```
+-----+------+---+---+
|color| fruit| v1| v2|
+-----+------+---+---+
|  red|banana|  1| 10|
| blue|banana|  2| 20|
|  red|carrot|  3| 30|
| blue| grape|  4| 40|
|  red|carrot|  5| 50|
|black|carrot|  6| 60|
|  red|banana|  7| 70|
|  red| grape|  8| 80|
+-----+------+---+---+

```
Copy to clipboard
### Parquet[#](https://spark.apache.org/docs/latest/api/python/getting_started/quickstart_df.html#Parquet "Permalink to this headline")

```
[28]:

```
Copy to clipboard

```
df.write.parquet('bar.parquet')
spark.read.parquet('bar.parquet').show()

```
Copy to clipboard

```
+-----+------+---+---+
|color| fruit| v1| v2|
+-----+------+---+---+
|  red|banana|  1| 10|
| blue|banana|  2| 20|
|  red|carrot|  3| 30|
| blue| grape|  4| 40|
|  red|carrot|  5| 50|
|black|carrot|  6| 60|
|  red|banana|  7| 70|
|  red| grape|  8| 80|
+-----+------+---+---+

```
Copy to clipboard
### ORC[#](https://spark.apache.org/docs/latest/api/python/getting_started/quickstart_df.html#ORC "Permalink to this headline")

```
[29]:

```
Copy to clipboard

```
df.write.orc('zoo.orc')
spark.read.orc('zoo.orc').show()

```
Copy to clipboard

```
+-----+------+---+---+
|color| fruit| v1| v2|
+-----+------+---+---+
|  red|banana|  1| 10|
| blue|banana|  2| 20|
|  red|carrot|  3| 30|
| blue| grape|  4| 40|
|  red|carrot|  5| 50|
|black|carrot|  6| 60|
|  red|banana|  7| 70|
|  red| grape|  8| 80|
+-----+------+---+---+

```
Copy to clipboard
## Working with SQL[#](https://spark.apache.org/docs/latest/api/python/getting_started/quickstart_df.html#Working-with-SQL "Permalink to this headline")
DataFrame and Spark SQL share the same execution engine so they can be interchangeably used seamlessly. For example, you can register the DataFrame as a table and run a SQL easily as below:

```
[30]:

```
Copy to clipboard

```
df.createOrReplaceTempView("tableA")
spark.sql("SELECT count(*) from tableA").show()

```
Copy to clipboard

```
+--------+
|count(1)|
+--------+
|       8|
+--------+

```
Copy to clipboard
In addition, UDFs can be registered and invoked in SQL out of the box:

```
[31]:

```
Copy to clipboard

```
@pandas_udf("integer")
def add_one(s: pd.Series) -> pd.Series:
    return s + 1

spark.udf.register("add_one", add_one)
spark.sql("SELECT add_one(v1) FROM tableA").show()

```
Copy to clipboard

```
+-----------+
|add_one(v1)|
+-----------+
|          2|
|          3|
|          4|
|          5|
|          6|
|          7|
|          8|
|          9|
+-----------+

```
Copy to clipboard
These SQL expressions can directly be mixed and used as PySpark columns.

```
[32]:

```
Copy to clipboard

```
from pyspark.sql.functions import expr

df.selectExpr('add_one(v1)').show()
df.select(expr('count(*)') > 0).show()

```
Copy to clipboard

```
+-----------+
|add_one(v1)|
+-----------+
|          2|
|          3|
|          4|
|          5|
|          6|
|          7|
|          8|
|          9|
+-----------+

+--------------+
|(count(1) > 0)|
+--------------+
|          true|
+--------------+

```
Copy to clipboard
[ previous Installation ](https://spark.apache.org/docs/latest/api/python/getting_started/install.html "previous page") [ next Quickstart: Spark Connect ](https://spark.apache.org/docs/latest/api/python/getting_started/quickstart_connect.html "next page")
On this page
  * [DataFrame Creation](https://spark.apache.org/docs/latest/api/python/getting_started/quickstart_df.html#DataFrame-Creation)
  * [Viewing Data](https://spark.apache.org/docs/latest/api/python/getting_started/quickstart_df.html#Viewing-Data)
  * [Selecting and Accessing Data](https://spark.apache.org/docs/latest/api/python/getting_started/quickstart_df.html#Selecting-and-Accessing-Data)
  * [Applying a Function](https://spark.apache.org/docs/latest/api/python/getting_started/quickstart_df.html#Applying-a-Function)
  * [Grouping Data](https://spark.apache.org/docs/latest/api/python/getting_started/quickstart_df.html#Grouping-Data)
  * [Getting Data In/Out](https://spark.apache.org/docs/latest/api/python/getting_started/quickstart_df.html#Getting-Data-In/Out)
    * [CSV](https://spark.apache.org/docs/latest/api/python/getting_started/quickstart_df.html#CSV)
    * [Parquet](https://spark.apache.org/docs/latest/api/python/getting_started/quickstart_df.html#Parquet)
    * [ORC](https://spark.apache.org/docs/latest/api/python/getting_started/quickstart_df.html#ORC)
  * [Working with SQL](https://spark.apache.org/docs/latest/api/python/getting_started/quickstart_df.html#Working-with-SQL)

[ Show Source ](https://spark.apache.org/docs/latest/api/python/_sources/getting_started/quickstart_df.ipynb.txt)
Copyright @ 2026 The Apache Software Foundation, Licensed under the [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0).
Created using [Sphinx](https://www.sphinx-doc.org/) 4.5.0.

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.13.3.
