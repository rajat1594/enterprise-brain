[Skip to contents](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html#main)
[ ![](https://spark.apache.org/images/spark-logo-rev.svg)](https://spark.apache.org/) [SparkR](https://spark.apache.org/docs/latest/api/R/index.html) 4.1.2
  * [Reference](https://spark.apache.org/docs/latest/api/R/reference/index.html)
  * [Articles](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html)
[SparkR - Practical Guide](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html)


  * 

![](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html)
# SparkR - Practical Guide
`sparkr-vignettes.Rmd`
SparkR is deprecated from Apache Spark 4.0.0 and will be removed in a future version.
## Overview[](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html#overview)
SparkR is an R package that provides a light-weight frontend to use Apache Spark from R. With Spark 4.1.2, SparkR provides a distributed data frame implementation that supports data processing operations like selection, filtering, aggregation etc. and distributed machine learning using [MLlib](https://spark.apache.org/mllib/).
## Getting Started[](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html#getting-started)
We begin with an example running on the local machine and provide an overview of the use of SparkR: data ingestion, data processing and machine learning.
First, let’s load and attach the package.

```
library[](https://rdrr.io/r/base/library.html)(SparkR[](https://www.apache.org))
```

`SparkSession` is the entry point into SparkR which connects your R program to a Spark cluster. You can create a `SparkSession` using `sparkR.session` and pass in options such as the application name, any Spark packages depended on, etc.
We use default settings in which it runs in local mode. It auto downloads Spark package in the background if no previous installation is found. For more details about setup, see [Spark Session](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html#SetupSparkSession).

```
sparkR.session[](https://spark.apache.org/docs/latest/api/R/reference/sparkR.session.html)()
```

The operations in SparkR are centered around an R class called `SparkDataFrame`. It is a distributed collection of data organized into named columns, which is conceptually equivalent to a table in a relational database or a data frame in R, but with richer optimizations under the hood.
`SparkDataFrame` can be constructed from a wide array of sources such as: structured data files, tables in Hive, external databases, or existing local R data frames. For example, we create a `SparkDataFrame` from a local R data frame,

```
cars <- cbind[](https://rdrr.io/r/base/cbind.html)(model = rownames[](https://rdrr.io/r/base/colnames.html)(mtcars), mtcars)
carsDF <- createDataFrame[](https://spark.apache.org/docs/latest/api/R/reference/createDataFrame.html)(cars)
```

We can view the first few rows of the `SparkDataFrame` by `head` or `showDF` function.

```
head[](https://spark.apache.org/docs/latest/api/R/reference/head.html)(carsDF)
```

Common data processing operations such as `filter` and `select` are supported on the `SparkDataFrame`.

```
carsSubDF <- select[](https://spark.apache.org/docs/latest/api/R/reference/select.html)(carsDF, "model", "mpg", "hp")
carsSubDF <- filter[](https://spark.apache.org/docs/latest/api/R/reference/filter.html)(carsSubDF, carsSubDF$hp >= 200)
head[](https://spark.apache.org/docs/latest/api/R/reference/head.html)(carsSubDF)
```

SparkR can use many common aggregation functions after grouping.

```
carsGPDF <- summarize[](https://spark.apache.org/docs/latest/api/R/reference/summarize.html)(groupBy[](https://spark.apache.org/docs/latest/api/R/reference/groupBy.html)(carsDF, carsDF$gear), count = n[](https://spark.apache.org/docs/latest/api/R/reference/count.html)(carsDF$gear))
head[](https://spark.apache.org/docs/latest/api/R/reference/head.html)(carsGPDF)
```

The results `carsDF` and `carsSubDF` are `SparkDataFrame` objects. To convert back to R `data.frame`, we can use `collect`. **Caution** : This can cause your interactive environment to run out of memory, though, because `collect()[](https://spark.apache.org/docs/latest/api/R/reference/collect.html)` fetches the entire distributed `DataFrame` to your client, which is acting as a Spark driver.

```
carsGP <- collect[](https://spark.apache.org/docs/latest/api/R/reference/collect.html)(carsGPDF)
class[](https://rdrr.io/r/base/class.html)(carsGP)
```

SparkR supports a number of commonly used machine learning algorithms. Under the hood, SparkR uses MLlib to train the model. Users can call `summary` to print a summary of the fitted model, `predict` to make predictions on new data, and `write.ml`/`read.ml` to save/load fitted models.
SparkR supports a subset of R formula operators for model fitting, including ‘~’, ‘.’, ‘:’, ‘+’, and ‘-‘. We use linear regression as an example.

```
model <- spark.glm[](https://spark.apache.org/docs/latest/api/R/reference/spark.glm.html)(carsDF, mpg ~ wt + cyl)
```

The result matches that returned by R `glm` function applied to the corresponding `data.frame` `mtcars` of `carsDF`. In fact, for Generalized Linear Model, we specifically expose `glm` for `SparkDataFrame` as well so that the above is equivalent to `model <- glm(mpg ~ wt + cyl, data = carsDF)`.

```
summary[](https://spark.apache.org/docs/latest/api/R/reference/summary.html)(model)
```

The model can be saved by `write.ml` and loaded back using `read.ml`.

```
write.ml[](https://spark.apache.org/docs/latest/api/R/reference/write.ml.html)(model, path = "/HOME/tmp/mlModel/glmModel")
```

In the end, we can stop Spark Session by running

```
sparkR.session.stop[](https://spark.apache.org/docs/latest/api/R/reference/sparkR.session.stop.html)()
```

## Setup[](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html#setup)
### Installation[](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html#installation)
Different from many other R packages, to use SparkR, you need an additional installation of Apache Spark. The Spark installation will be used to run a backend process that will compile and execute SparkR programs.
After installing the SparkR package, you can call `sparkR.session` as explained in the previous section to start and it will check for the Spark installation. If you are working with SparkR from an interactive shell (e.g. R, RStudio) then Spark is downloaded and cached automatically if it is not found. Alternatively, we provide an easy-to-use function `install.spark` for running this manually. If you don’t have Spark installed on the computer, you may download it from [Apache Spark Website](https://spark.apache.org/downloads.html).

```
install.spark[](https://spark.apache.org/docs/latest/api/R/reference/install.spark.html)()
```

If you already have Spark installed, you don’t have to install again and can pass the `sparkHome` argument to `sparkR.session` to let SparkR know where the existing Spark installation is.

```
sparkR.session[](https://spark.apache.org/docs/latest/api/R/reference/sparkR.session.html)(sparkHome = "/HOME/spark")
```

### Spark Session[](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html#SetupSparkSession)
In addition to `sparkHome`, many other options can be specified in `sparkR.session`. For a complete list, see [Starting up: SparkSession](https://spark.apache.org/docs/latest/sparkr.html#starting-up-sparksession) and [SparkR API doc](https://spark.apache.org/docs/latest/api/R/reference/sparkR.session.html).
In particular, the following Spark driver properties can be set in `sparkConfig`.  
| Property Name  | Property group  | spark-submit equivalent  |  
| --- | --- | --- |  
| `spark.driver.memory`  | Application Properties  | `--driver-memory`  |  
| `spark.driver.extraClassPath`  | Runtime Environment  | `--driver-class-path`  |  
| `spark.driver.extraJavaOptions`  | Runtime Environment  | `--driver-java-options`  |  
| `spark.driver.extraLibraryPath`  | Runtime Environment  | `--driver-library-path`  |  
| `spark.kerberos.keytab`  | Application Properties  | `--keytab`  |  
| `spark.kerberos.principal`  | Application Properties  | `--principal`  |  
**For Windows users** : Due to different file prefixes across operating systems, to avoid the issue of potential wrong prefix, a current workaround is to specify `spark.sql.warehouse.dir` when starting the `SparkSession`.

```
spark_warehouse_path <- file.path[](https://rdrr.io/r/base/file.path.html)(path.expand[](https://rdrr.io/r/base/path.expand.html)('~'), "spark-warehouse")
sparkR.session[](https://spark.apache.org/docs/latest/api/R/reference/sparkR.session.html)(spark.sql.warehouse.dir = spark_warehouse_path)
```

#### Cluster Mode[](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html#cluster-mode)
SparkR can connect to remote Spark clusters. [Cluster Mode Overview](https://spark.apache.org/docs/latest/cluster-overview.html) is a good introduction to different Spark cluster modes.
When connecting SparkR to a remote Spark cluster, make sure that the Spark version and Hadoop version on the machine match the corresponding versions on the cluster. Current SparkR package is compatible with
It should be used both on the local computer and on the remote cluster.
To connect, pass the URL of the master node to `sparkR.session`. A complete list can be seen in [Spark Master URLs](https://spark.apache.org/docs/latest/submitting-applications.html#master-urls). For example, to connect to a local standalone Spark master, we can call

```
sparkR.session[](https://spark.apache.org/docs/latest/api/R/reference/sparkR.session.html)(master = "spark://local:7077")
```

For YARN cluster, SparkR supports the client mode with the master set as “yarn”.

```
sparkR.session[](https://spark.apache.org/docs/latest/api/R/reference/sparkR.session.html)(master = "yarn")
```

Yarn cluster mode is not supported in the current version.
## Data Import[](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html#data-import)
### Local Data Frame[](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html#local-data-frame)
The simplest way is to convert a local R data frame into a `SparkDataFrame`. Specifically we can use `as.DataFrame` or `createDataFrame` and pass in the local R data frame to create a `SparkDataFrame`. As an example, the following creates a `SparkDataFrame` based using the `faithful` dataset from R.

```
df <- as.DataFrame[](https://spark.apache.org/docs/latest/api/R/reference/createDataFrame.html)(faithful)
head[](https://spark.apache.org/docs/latest/api/R/reference/head.html)(df)
```

### Data Sources[](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html#data-sources)
SparkR supports operating on a variety of data sources through the `SparkDataFrame` interface. You can check the Spark SQL Programming Guide for more [specific options](https://spark.apache.org/docs/latest/sql-programming-guide.html#manually-specifying-options) that are available for the built-in data sources.
The general method for creating `SparkDataFrame` from data sources is `read.df`. This method takes in the path for the file to load and the type of data source, and the currently active Spark Session will be used automatically. SparkR supports reading CSV, JSON and Parquet files natively and through Spark Packages you can find data source connectors for popular file formats like Avro. These packages can be added with `sparkPackages` parameter when initializing SparkSession using `sparkR.session`.

```
sparkR.session[](https://spark.apache.org/docs/latest/api/R/reference/sparkR.session.html)(sparkPackages = "com.databricks:spark-avro_2.12:3.0.0")
```

We can see how to use data sources using an example CSV input file. For more information please refer to SparkR [read.df](https://spark.apache.org/docs/latest/api/R/reference/read.df.html) API documentation.

```
df <- read.df[](https://spark.apache.org/docs/latest/api/R/reference/read.df.html)(csvPath, "csv", header = "true", inferSchema = "true", na.strings = "NA")
```

The data sources API natively supports JSON formatted input files. Note that the file that is used here is not a typical JSON file. Each line in the file must contain a separate, self-contained valid JSON object. As a consequence, a regular multi-line JSON file will most often fail.
Let’s take a look at the first two lines of the raw JSON file used here.

```
filePath <- paste0[](https://rdrr.io/r/base/paste.html)(sparkR.conf[](https://spark.apache.org/docs/latest/api/R/reference/sparkR.conf.html)("spark.home"),
                         "/examples/src/main/resources/people.json")
readLines[](https://rdrr.io/r/base/readLines.html)(filePath, n = 2L)
```

We use `read.df` to read that into a `SparkDataFrame`.

```
people <- read.df[](https://spark.apache.org/docs/latest/api/R/reference/read.df.html)(filePath, "json")
count[](https://spark.apache.org/docs/latest/api/R/reference/count.html)(people)
head[](https://spark.apache.org/docs/latest/api/R/reference/head.html)(people)
```

SparkR automatically infers the schema from the JSON file.

```
printSchema[](https://spark.apache.org/docs/latest/api/R/reference/printSchema.html)(people)
```

If we want to read multiple JSON files, `read.json` can be used.

```
people <- read.json[](https://spark.apache.org/docs/latest/api/R/reference/read.json.html)(paste0[](https://rdrr.io/r/base/paste.html)(Sys.getenv[](https://rdrr.io/r/base/Sys.getenv.html)("SPARK_HOME"),
                           c[](https://rdrr.io/r/base/c.html)("/examples/src/main/resources/people.json",
                             "/examples/src/main/resources/people.json")))
count[](https://spark.apache.org/docs/latest/api/R/reference/count.html)(people)
```

The data sources API can also be used to save out `SparkDataFrames` into multiple file formats. For example we can save the `SparkDataFrame` from the previous example to a Parquet file using `write.df`.

```
write.df[](https://spark.apache.org/docs/latest/api/R/reference/write.df.html)(people, path = "people.parquet", source = "parquet", mode = "overwrite")
```

### Hive Tables[](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html#hive-tables)
You can also create SparkDataFrames from Hive tables. To do this we will need to create a SparkSession with Hive support which can access tables in the Hive MetaStore. Note that Spark should have been built with Hive support and more details can be found in the [SQL Programming Guide](https://spark.apache.org/docs/latest/sql-programming-guide.html). In SparkR, by default it will attempt to create a SparkSession with Hive support enabled (`enableHiveSupport = TRUE`).

```
sql[](https://spark.apache.org/docs/latest/api/R/reference/sql.html)("CREATE TABLE IF NOT EXISTS src (key INT, value STRING)")

txtPath <- paste0[](https://rdrr.io/r/base/paste.html)(sparkR.conf[](https://spark.apache.org/docs/latest/api/R/reference/sparkR.conf.html)("spark.home"), "/examples/src/main/resources/kv1.txt")
sqlCMD <- sprintf[](https://rdrr.io/r/base/sprintf.html)("LOAD DATA LOCAL INPATH '%s' INTO TABLE src", txtPath)
sql[](https://spark.apache.org/docs/latest/api/R/reference/sql.html)(sqlCMD)

results <- sql[](https://spark.apache.org/docs/latest/api/R/reference/sql.html)("FROM src SELECT key, value")

# results is now a SparkDataFrame
head[](https://spark.apache.org/docs/latest/api/R/reference/head.html)(results)
```

## Data Processing[](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html#data-processing)
**To dplyr users** : SparkR has similar interface as dplyr in data processing. However, some noticeable differences are worth mentioning in the first place. We use `df` to represent a `SparkDataFrame` and `col` to represent the name of column here.
  1. indicate columns. SparkR uses either a character string of the column name or a Column object constructed with `$` to indicate a column. For example, to select `col` in `df`, we can write `select(df, "col")` or `select(df, df$col)`.
  2. describe conditions. In SparkR, the Column object representation can be inserted into the condition directly, or we can use a character string to describe the condition, without referring to the `SparkDataFrame` used. For example, to select rows with value > 1, we can write `filter(df, df$col > 1)` or `filter(df, "col > 1")`.


Here are more concrete examples.  
| dplyr  | SparkR  |  
| --- | --- |  
| `select(mtcars, mpg, hp)`  | `select(carsDF, "mpg", "hp")`  |  
| `filter(mtcars, mpg > 20, hp > 100)`  | `filter(carsDF, carsDF$mpg > 20, carsDF$hp > 100)`  |  
Other differences will be mentioned in the specific methods.
We use the `SparkDataFrame` `carsDF` created above. We can get basic information about the `SparkDataFrame`.

```
carsDF
```

Print out the schema in tree format.

```
printSchema[](https://spark.apache.org/docs/latest/api/R/reference/printSchema.html)(carsDF)
```

### SparkDataFrame Operations[](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html#sparkdataframe-operations)
#### Selecting rows, columns[](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html#selecting-rows-columns)
SparkDataFrames support a number of functions to do structured data processing. Here we include some basic examples and a complete list can be found in the [API](https://spark.apache.org/docs/latest/api/R/index.html) docs:
You can also pass in column name as strings.

```
head[](https://spark.apache.org/docs/latest/api/R/reference/head.html)(select[](https://spark.apache.org/docs/latest/api/R/reference/select.html)(carsDF, "mpg"))
```

Filter the SparkDataFrame to only retain rows with mpg less than 20 miles/gallon.

```
head[](https://spark.apache.org/docs/latest/api/R/reference/head.html)(filter[](https://spark.apache.org/docs/latest/api/R/reference/filter.html)(carsDF, carsDF$mpg < 20))
```

#### Grouping, Aggregation[](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html#grouping-aggregation)
A common flow of grouping and aggregation is
  1. Use `groupBy` or `group_by` with respect to some grouping variables to create a `GroupedData` object
  2. Feed the `GroupedData` object to `agg` or `summarize` functions, with some provided aggregation functions to compute a number within each group.


A number of widely used functions are supported to aggregate data after grouping, including `avg`, `count_distinct`, `count`, `first`, `kurtosis`, `last`, `max`, `mean`, `min`, `sd`, `skewness`, `stddev_pop`, `stddev_samp`, `sum_distinct`, `sum`, `var_pop`, `var_samp`, `var`. See the [API doc for aggregate functions](https://spark.apache.org/docs/latest/api/R/reference/column_aggregate_functions.html) linked there.
For example we can compute a histogram of the number of cylinders in the `mtcars` dataset as shown below.

```
numCyl <- summarize[](https://spark.apache.org/docs/latest/api/R/reference/summarize.html)(groupBy[](https://spark.apache.org/docs/latest/api/R/reference/groupBy.html)(carsDF, carsDF$cyl), count = n[](https://spark.apache.org/docs/latest/api/R/reference/count.html)(carsDF$cyl))
head[](https://spark.apache.org/docs/latest/api/R/reference/head.html)(numCyl)
```

Use `cube` or `rollup` to compute subtotals across multiple dimensions.

```
mean[](https://spark.apache.org/docs/latest/api/R/reference/column_aggregate_functions.html)(cube[](https://spark.apache.org/docs/latest/api/R/reference/cube.html)(carsDF, "cyl", "gear", "am"), "mpg")
```

generates groupings for {(`cyl`, `gear`, `am`), (`cyl`, `gear`), (`cyl`), ()}, while

```
mean[](https://spark.apache.org/docs/latest/api/R/reference/column_aggregate_functions.html)(rollup[](https://spark.apache.org/docs/latest/api/R/reference/rollup.html)(carsDF, "cyl", "gear", "am"), "mpg")
```

generates groupings for all possible combinations of grouping columns.
#### Operating on Columns[](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html#operating-on-columns)
SparkR also provides a number of functions that can directly applied to columns for data processing and during aggregation. The example below shows the use of basic arithmetic functions.

```
carsDF_km <- carsDF
carsDF_km$kmpg <- carsDF_km$mpg * 1.61
head[](https://spark.apache.org/docs/latest/api/R/reference/head.html)(select[](https://spark.apache.org/docs/latest/api/R/reference/select.html)(carsDF_km, "model", "mpg", "kmpg"))
```

### Window Functions[](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html#window-functions)
A window function is a variation of aggregation function. In simple words,
  * aggregation function: `n` to `1` mapping - returns a single value for a group of entries. Examples include `sum`, `count`, `max`.
  * window function: `n` to `n` mapping - returns one value for each entry in the group, but the value may depend on all the entries of the _group_. Examples include `rank`, `lead`, `lag`.


Formally, the _group_ mentioned above is called the _frame_. Every input row can have a unique frame associated with it and the output of the window function on that row is based on the rows confined in that frame.
Window functions are often used in conjunction with the following functions: `windowPartitionBy`, `windowOrderBy`, `partitionBy`, `orderBy`, `over`. To illustrate this we next look at an example.
We still use the `mtcars` dataset. The corresponding `SparkDataFrame` is `carsDF`. Suppose for each number of cylinders, we want to calculate the rank of each car in `mpg` within the group.

```
carsSubDF <- select[](https://spark.apache.org/docs/latest/api/R/reference/select.html)(carsDF, "model", "mpg", "cyl")
ws <- orderBy[](https://spark.apache.org/docs/latest/api/R/reference/orderBy.html)(windowPartitionBy[](https://spark.apache.org/docs/latest/api/R/reference/windowPartitionBy.html)("cyl"), "mpg")
carsRank <- withColumn[](https://spark.apache.org/docs/latest/api/R/reference/withColumn.html)(carsSubDF, "rank", over[](https://spark.apache.org/docs/latest/api/R/reference/over.html)(rank[](https://spark.apache.org/docs/latest/api/R/reference/column_window_functions.html)(), ws))
head[](https://spark.apache.org/docs/latest/api/R/reference/head.html)(carsRank, n = 20L)
```

We explain in detail the above steps.
  * `windowPartitionBy` creates a window specification object `WindowSpec` that defines the partition. It controls which rows will be in the same partition as the given row. In this case, rows with the same value in `cyl` will be put in the same partition. `orderBy` further defines the ordering - the position a given row is in the partition. The resulting `WindowSpec` is returned as `ws`.


More window specification methods include `rangeBetween`, which can define boundaries of the frame by value, and `rowsBetween`, which can define the boundaries by row indices.
  * `withColumn` appends a Column called `rank` to the `SparkDataFrame`. `over` returns a windowing column. The first argument is usually a Column returned by window function(s) such as `rank()[](https://spark.apache.org/docs/latest/api/R/reference/column_window_functions.html)`, `lead(carsDF$wt)`. That calculates the corresponding values according to the partitioned-and-ordered table.


### User-Defined Function[](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html#user-defined-function)
In SparkR, we support several kinds of user-defined functions (UDFs).
#### Apply by Partition[](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html#apply-by-partition)
`dapply` can apply a function to each partition of a `SparkDataFrame`. The function to be applied to each partition of the `SparkDataFrame` should have only one parameter, a `data.frame` corresponding to a partition, and the output should be a `data.frame` as well. Schema specifies the row format of the resulting a `SparkDataFrame`. It must match to data types of returned value. See [here](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html#DataTypes) for mapping between R and Spark.
We convert `mpg` to `kmpg` (kilometers per gallon). `carsSubDF` is a `SparkDataFrame` with a subset of `carsDF` columns.

```
carsSubDF <- select[](https://spark.apache.org/docs/latest/api/R/reference/select.html)(carsDF, "model", "mpg")
schema <- "model STRING, mpg DOUBLE, kmpg DOUBLE"
out <- dapply[](https://spark.apache.org/docs/latest/api/R/reference/dapply.html)(carsSubDF, function(x) { x <- cbind[](https://rdrr.io/r/base/cbind.html)(x, x$mpg * 1.61) }, schema)
head[](https://spark.apache.org/docs/latest/api/R/reference/head.html)(collect[](https://spark.apache.org/docs/latest/api/R/reference/collect.html)(out))
```

Like `dapply`, `dapplyCollect` can apply a function to each partition of a `SparkDataFrame` and collect the result back. The output of the function should be a `data.frame`, but no schema is required in this case. Note that `dapplyCollect` can fail if the output of the UDF on all partitions cannot be pulled into the driver’s memory.

```
out <- dapplyCollect[](https://spark.apache.org/docs/latest/api/R/reference/dapplyCollect.html)(
         carsSubDF,
         function(x) {
           x <- cbind[](https://rdrr.io/r/base/cbind.html)(x, "kmpg" = x$mpg * 1.61)
         })
head[](https://spark.apache.org/docs/latest/api/R/reference/head.html)(out, 3)
```

#### Apply by Group[](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html#apply-by-group)
`gapply` can apply a function to each group of a `SparkDataFrame`. The function is to be applied to each group of the `SparkDataFrame` and should have only two parameters: grouping key and R `data.frame` corresponding to that key. The groups are chosen from `SparkDataFrames` column(s). The output of function should be a `data.frame`. Schema specifies the row format of the resulting `SparkDataFrame`. It must represent R function’s output schema on the basis of Spark data types. The column names of the returned `data.frame` are set by user. See [here](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html#DataTypes) for mapping between R and Spark.

```
schema <- structType[](https://spark.apache.org/docs/latest/api/R/reference/structType.html)(structField[](https://spark.apache.org/docs/latest/api/R/reference/structField.html)("cyl", "double"), structField[](https://spark.apache.org/docs/latest/api/R/reference/structField.html)("max_mpg", "double"))
result <- gapply[](https://spark.apache.org/docs/latest/api/R/reference/gapply.html)(
    carsDF,
    "cyl",
    function(key, x) {
        y <- data.frame[](https://rdrr.io/r/base/data.frame.html)(key, max[](https://spark.apache.org/docs/latest/api/R/reference/column_aggregate_functions.html)(x$mpg))
    },
    schema)
head[](https://spark.apache.org/docs/latest/api/R/reference/head.html)(arrange[](https://spark.apache.org/docs/latest/api/R/reference/arrange.html)(result, "max_mpg", decreasing = TRUE))
```

Like `gapply`, `gapplyCollect` can apply a function to each partition of a `SparkDataFrame` and collect the result back to R `data.frame`. The output of the function should be a `data.frame` but no schema is required in this case. Note that `gapplyCollect` can fail if the output of the UDF on all partitions cannot be pulled into the driver’s memory.

```
result <- gapplyCollect[](https://spark.apache.org/docs/latest/api/R/reference/gapplyCollect.html)(
    carsDF,
    "cyl",
    function(key, x) {
         y <- data.frame[](https://rdrr.io/r/base/data.frame.html)(key, max[](https://spark.apache.org/docs/latest/api/R/reference/column_aggregate_functions.html)(x$mpg))
        colnames[](https://spark.apache.org/docs/latest/api/R/reference/columns.html)(y) <- c[](https://rdrr.io/r/base/c.html)("cyl", "max_mpg")
        y
    })
head[](https://spark.apache.org/docs/latest/api/R/reference/head.html)(result[order[](https://rdrr.io/r/base/order.html)(result$max_mpg, decreasing = TRUE), ])
```

#### Distribute Local Functions[](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html#distribute-local-functions)
Similar to `lapply` in native R, `spark.lapply` runs a function over a list of elements and distributes the computations with Spark. `spark.lapply` works in a manner that is similar to `doParallel` or `lapply` to elements of a list. The results of all the computations should fit in a single machine. If that is not the case you can do something like `df <- createDataFrame(list)` and then use `dapply`.
We use `svm` in package `e1071` as an example. We use all default settings except for varying costs of constraints violation. `spark.lapply` can train those different models in parallel.

```
costs <- exp[](https://spark.apache.org/docs/latest/api/R/reference/column_math_functions.html)(seq[](https://rdrr.io/r/base/seq.html)(from = log[](https://spark.apache.org/docs/latest/api/R/reference/column_math_functions.html)(1), to = log[](https://spark.apache.org/docs/latest/api/R/reference/column_math_functions.html)(1000), length.out = 5))
train <- function(cost) {
  stopifnot[](https://rdrr.io/r/base/stopifnot.html)(requireNamespace[](https://rdrr.io/r/base/ns-load.html)("e1071", quietly = TRUE))
  model <- e1071::svm[](https://rdrr.io/pkg/e1071/man/svm.html)(Species ~ ., data = iris, cost = cost)
  summary[](https://spark.apache.org/docs/latest/api/R/reference/summary.html)(model)
}
```

Return a list of model’s summaries.

```
model.summaries <- spark.lapply[](https://spark.apache.org/docs/latest/api/R/reference/spark.lapply.html)(costs, train)
```


```
class[](https://rdrr.io/r/base/class.html)(model.summaries)
```

To avoid lengthy display, we only present the partial result of the second fitted model. You are free to inspect other models as well.

```
print[](https://rdrr.io/r/base/print.html)(model.summaries[[2]])
```

### SQL Queries[](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html#sql-queries)
A `SparkDataFrame` can also be registered as a temporary view in Spark SQL so that one can run SQL queries over its data. The sql function enables applications to run SQL queries programmatically and returns the result as a `SparkDataFrame`.

```
people <- read.df[](https://spark.apache.org/docs/latest/api/R/reference/read.df.html)(paste0[](https://rdrr.io/r/base/paste.html)(sparkR.conf[](https://spark.apache.org/docs/latest/api/R/reference/sparkR.conf.html)("spark.home"),
                         "/examples/src/main/resources/people.json"), "json")
```

Register this `SparkDataFrame` as a temporary view.

```
createOrReplaceTempView[](https://spark.apache.org/docs/latest/api/R/reference/createOrReplaceTempView.html)(people, "people")
```

SQL statements can be run using the sql method.

```
teenagers <- sql[](https://spark.apache.org/docs/latest/api/R/reference/sql.html)("SELECT name FROM people WHERE age >= 13 AND age <= 19")
head[](https://spark.apache.org/docs/latest/api/R/reference/head.html)(teenagers)
```

## Machine Learning[](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html#machine-learning)
SparkR supports the following machine learning models and algorithms.
#### Classification[](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html#classification)
  * Linear Support Vector Machine (SVM) Classifier
  * Logistic Regression
  * Multilayer Perceptron (MLP)
  * Naive Bayes
  * Factorization Machines (FM) Classifier


#### Regression[](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html#regression)
  * Accelerated Failure Time (AFT) Survival Model
  * Generalized Linear Model (GLM)
  * Isotonic Regression
  * Linear Regression
  * Factorization Machines (FM) Regressor


#### Tree - Classification and Regression[](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html#tree---classification-and-regression)
  * Decision Tree
  * Gradient-Boosted Trees (GBT)
  * Random Forest


#### Clustering[](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html#clustering)
  * Bisecting \\(k\\)-means
  * Gaussian Mixture Model (GMM)
  * \\(k\\)-means Clustering
  * Latent Dirichlet Allocation (LDA)
  * Power Iteration Clustering (PIC)


#### Collaborative Filtering[](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html#collaborative-filtering)
  * Alternating Least Squares (ALS)


#### Frequent Pattern Mining[](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html#frequent-pattern-mining)
  * FP-growth
  * PrefixSpan


#### Statistics[](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html#statistics)
  * Kolmogorov-Smirnov Test


### R Formula[](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html#r-formula)
For most above, SparkR supports **R formula operators** , including `~`, `.`, `:`, `+` and `-` for model fitting. This makes it a similar experience as using R functions.
### Training and Test Sets[](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html#training-and-test-sets)
We can easily split `SparkDataFrame` into random training and test sets by the `randomSplit` function. It returns a list of split `SparkDataFrames` with provided `weights`. We use `carsDF` as an example and want to have about \\(70%\\) training data and \\(30%\\) test data.

```
splitDF_list <- randomSplit[](https://spark.apache.org/docs/latest/api/R/reference/randomSplit.html)(carsDF, c[](https://rdrr.io/r/base/c.html)(0.7, 0.3), seed = 0)
carsDF_train <- splitDF_list[[1]]
carsDF_test <- splitDF_list[[2]]
```


```
count[](https://spark.apache.org/docs/latest/api/R/reference/count.html)(carsDF_train)
head[](https://spark.apache.org/docs/latest/api/R/reference/head.html)(carsDF_train)
```


```
count[](https://spark.apache.org/docs/latest/api/R/reference/count.html)(carsDF_test)
head[](https://spark.apache.org/docs/latest/api/R/reference/head.html)(carsDF_test)
```

### Models and Algorithms[](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html#models-and-algorithms)
#### Linear Support Vector Machine (SVM) Classifier[](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html#linear-support-vector-machine-svm-classifier)
[Linear Support Vector Machine (SVM)](https://en.wikipedia.org/wiki/Support_vector_machine#Linear_SVM) classifier is an SVM classifier with linear kernels. This is a binary classifier. We use a simple example to show how to use `spark.svmLinear` for binary classification.

```
# load training data and create a DataFrame
t <- as.data.frame[](https://spark.apache.org/docs/latest/api/R/reference/as.data.frame.html)(Titanic)
training <- createDataFrame[](https://spark.apache.org/docs/latest/api/R/reference/createDataFrame.html)(t)
# fit a Linear SVM classifier model
model <- spark.svmLinear[](https://spark.apache.org/docs/latest/api/R/reference/spark.svmLinear.html)(training,  Survived ~ ., regParam = 0.01, maxIter = 10)
summary[](https://spark.apache.org/docs/latest/api/R/reference/summary.html)(model)
```

Predict values on training data

```
prediction <- predict[](https://spark.apache.org/docs/latest/api/R/reference/predict.html)(model, training)
head[](https://spark.apache.org/docs/latest/api/R/reference/head.html)(select[](https://spark.apache.org/docs/latest/api/R/reference/select.html)(prediction, "Class", "Sex", "Age", "Freq", "Survived", "prediction"))
```

#### Logistic Regression[](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html#logistic-regression)
[Logistic regression](https://en.wikipedia.org/wiki/Logistic_regression) is a widely-used model when the response is categorical. It can be seen as a special case of the [Generalized Linear Predictive Model](https://en.wikipedia.org/wiki/Generalized_linear_model). We provide `spark.logit` on top of `spark.glm` to support logistic regression with advanced hyper-parameters. It supports both binary and multiclass classification with elastic-net regularization and feature standardization, similar to `glmnet`.
We use a simple example to demonstrate `spark.logit` usage. In general, there are three steps of using `spark.logit`: 1). Create a dataframe from a proper data source; 2). Fit a logistic regression model using `spark.logit` with a proper parameter setting; and 3). Obtain the coefficient matrix of the fitted model using `summary` and use the model for prediction with `predict`.
Binomial logistic regression

```
t <- as.data.frame[](https://spark.apache.org/docs/latest/api/R/reference/as.data.frame.html)(Titanic)
training <- createDataFrame[](https://spark.apache.org/docs/latest/api/R/reference/createDataFrame.html)(t)
model <- spark.logit[](https://spark.apache.org/docs/latest/api/R/reference/spark.logit.html)(training, Survived ~ ., regParam = 0.04741301)
summary[](https://spark.apache.org/docs/latest/api/R/reference/summary.html)(model)
```

Predict values on training data

```
fitted <- predict[](https://spark.apache.org/docs/latest/api/R/reference/predict.html)(model, training)
head[](https://spark.apache.org/docs/latest/api/R/reference/head.html)(select[](https://spark.apache.org/docs/latest/api/R/reference/select.html)(fitted, "Class", "Sex", "Age", "Freq", "Survived", "prediction"))
```

Multinomial logistic regression against three classes

```
t <- as.data.frame[](https://spark.apache.org/docs/latest/api/R/reference/as.data.frame.html)(Titanic)
training <- createDataFrame[](https://spark.apache.org/docs/latest/api/R/reference/createDataFrame.html)(t)
# Note in this case, Spark infers it is multinomial logistic regression, so family = "multinomial" is optional.
model <- spark.logit[](https://spark.apache.org/docs/latest/api/R/reference/spark.logit.html)(training, Class ~ ., regParam = 0.07815179)
summary[](https://spark.apache.org/docs/latest/api/R/reference/summary.html)(model)
```

#### Multilayer Perceptron[](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html#multilayer-perceptron)
Multilayer perceptron classifier (MLPC) is a classifier based on the [feedforward artificial neural network](https://en.wikipedia.org/wiki/Feedforward_neural_network). MLPC consists of multiple layers of nodes. Each layer is fully connected to the next layer in the network. Nodes in the input layer represent the input data. All other nodes map inputs to outputs by a linear combination of the inputs with the node’s weights \\(w\\) and bias \\(b\\) and applying an activation function. This can be written in matrix form for MLPC with \\(K+1\\) layers as follows: \\[ y(x)=f_K(\ldots f_2(w_2^T f_1(w_1^T x + b_1) + b_2) \ldots + b_K). \\]
Nodes in intermediate layers use sigmoid (logistic) function: \\[ f(z_i) = \frac{1}{1+e^{-z_i}}. \\]
Nodes in the output layer use softmax function: \\[ f(z_i) = \frac{e^{z_i}}{\sum_{k=1}^N e^{z_k}}. \\]
The number of nodes \\(N\\) in the output layer corresponds to the number of classes.
MLPC employs backpropagation for learning the model. We use the logistic loss function for optimization and L-BFGS as an optimization routine.
`spark.mlp` requires at least two columns in `data`: one named `"label"` and the other one `"features"`. The `"features"` column should be in libSVM-format.
We use Titanic data set to show how to use `spark.mlp` in classification.

```
t <- as.data.frame[](https://spark.apache.org/docs/latest/api/R/reference/as.data.frame.html)(Titanic)
training <- createDataFrame[](https://spark.apache.org/docs/latest/api/R/reference/createDataFrame.html)(t)
# fit a Multilayer Perceptron Classification Model
model <- spark.mlp[](https://spark.apache.org/docs/latest/api/R/reference/spark.mlp.html)(training, Survived ~ Age + Sex, blockSize = 128, layers = c[](https://rdrr.io/r/base/c.html)(2, 2), solver = "l-bfgs", maxIter = 100, tol = 0.5, stepSize = 1, seed = 1, initialWeights = c[](https://rdrr.io/r/base/c.html)( 0, 0, 5, 5, 9, 9))
```

To avoid lengthy display, we only present partial results of the model summary. You can check the full result from your sparkR shell.

```
# check the summary of the fitted model
summary[](https://spark.apache.org/docs/latest/api/R/reference/summary.html)(model)
```


```
# make predictions use the fitted model
predictions <- predict[](https://spark.apache.org/docs/latest/api/R/reference/predict.html)(model, training)
head[](https://spark.apache.org/docs/latest/api/R/reference/head.html)(select[](https://spark.apache.org/docs/latest/api/R/reference/select.html)(predictions, predictions$prediction))
```

#### Naive Bayes[](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html#naive-bayes)
Naive Bayes model assumes independence among the features. `spark.naiveBayes` fits a [Bernoulli naive Bayes model](https://en.wikipedia.org/wiki/Naive_Bayes_classifier#Bernoulli_naive_Bayes) against a SparkDataFrame. The data should be all categorical. These models are often used for document classification.

```
titanic <- as.data.frame[](https://spark.apache.org/docs/latest/api/R/reference/as.data.frame.html)(Titanic)
titanicDF <- createDataFrame[](https://spark.apache.org/docs/latest/api/R/reference/createDataFrame.html)(titanic[titanic$Freq > 0, -5])
naiveBayesModel <- spark.naiveBayes[](https://spark.apache.org/docs/latest/api/R/reference/spark.naiveBayes.html)(titanicDF, Survived ~ Class + Sex + Age)
summary[](https://spark.apache.org/docs/latest/api/R/reference/summary.html)(naiveBayesModel)
naiveBayesPrediction <- predict[](https://spark.apache.org/docs/latest/api/R/reference/predict.html)(naiveBayesModel, titanicDF)
head[](https://spark.apache.org/docs/latest/api/R/reference/head.html)(select[](https://spark.apache.org/docs/latest/api/R/reference/select.html)(naiveBayesPrediction, "Class", "Sex", "Age", "Survived", "prediction"))
```

#### Factorization Machines Classifier[](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html#factorization-machines-classifier)
Factorization Machines for classification problems.
For background and details about the implementation of factorization machines, refer to the [Factorization Machines section](https://spark.apache.org/docs/latest/ml-classification-regression.html#factorization-machines).

```
t <- as.data.frame[](https://spark.apache.org/docs/latest/api/R/reference/as.data.frame.html)(Titanic)
training <- createDataFrame[](https://spark.apache.org/docs/latest/api/R/reference/createDataFrame.html)(t)

model <- spark.fmClassifier[](https://spark.apache.org/docs/latest/api/R/reference/spark.fmClassifier.html)(training, Survived ~ Age + Sex)
summary[](https://spark.apache.org/docs/latest/api/R/reference/summary.html)(model)

predictions <- predict[](https://spark.apache.org/docs/latest/api/R/reference/predict.html)(model, training)
head[](https://spark.apache.org/docs/latest/api/R/reference/head.html)(select[](https://spark.apache.org/docs/latest/api/R/reference/select.html)(predictions, predictions$prediction))
```

#### Accelerated Failure Time Survival Model[](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html#accelerated-failure-time-survival-model)
Survival analysis studies the expected duration of time until an event happens, and often the relationship with risk factors or treatment taken on the subject. In contrast to standard regression analysis, survival modeling has to deal with special characteristics in the data including non-negative survival time and censoring.
Accelerated Failure Time (AFT) model is a parametric survival model for censored data that assumes the effect of a covariate is to accelerate or decelerate the life course of an event by some constant. For more information, refer to the Wikipedia page [AFT Model](https://en.wikipedia.org/wiki/Accelerated_failure_time_model) and the references there. Different from a [Proportional Hazards Model](https://en.wikipedia.org/wiki/Proportional_hazards_model) designed for the same purpose, the AFT model is easier to parallelize because each instance contributes to the objective function independently.

```
library[](https://rdrr.io/r/base/library.html)(survival[](https://github.com/therneau/survival))
ovarianDF <- createDataFrame[](https://spark.apache.org/docs/latest/api/R/reference/createDataFrame.html)(ovarian)
aftModel <- spark.survreg[](https://spark.apache.org/docs/latest/api/R/reference/spark.survreg.html)(ovarianDF, Surv[](https://rdrr.io/pkg/survival/man/Surv.html)(futime, fustat) ~ ecog_ps + rx)
summary[](https://spark.apache.org/docs/latest/api/R/reference/summary.html)(aftModel)
aftPredictions <- predict[](https://spark.apache.org/docs/latest/api/R/reference/predict.html)(aftModel, ovarianDF)
head[](https://spark.apache.org/docs/latest/api/R/reference/head.html)(aftPredictions)
```

#### Generalized Linear Model[](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html#generalized-linear-model)
The main function is `spark.glm`. The following families and link functions are supported. The default is gaussian.  
| Family  | Link Function  |  
| --- | --- |  
| gaussian  | identity, log, inverse  |  
| binomial  | logit, probit, cloglog (complementary log-log)  |  
| poisson  | log, identity, sqrt  |  
| gamma  | inverse, identity, log  |  
| tweedie  | power link function  |  
There are three ways to specify the `family` argument.
  * Family name as a character string, e.g. `family = "gaussian"`.
  * Family function, e.g. `family = binomial`.
  * Result returned by a family function, e.g. `family = poisson(link = log)`.
  * Note that there are two ways to specify the tweedie family:
    1. Set `family = "tweedie"` and specify the `var.power` and `link.power`
    2. When package `statmod` is loaded, the tweedie family is specified using the family definition therein, i.e., `tweedie()[](https://rdrr.io/pkg/statmod/man/tweedie.html)`.


For more information regarding the families and their link functions, see the Wikipedia page [Generalized Linear Model](https://en.wikipedia.org/wiki/Generalized_linear_model).
We use the `mtcars` dataset as an illustration. The corresponding `SparkDataFrame` is `carsDF`. After fitting the model, we print out a summary and see the fitted values by making predictions on the original dataset. We can also pass into a new `SparkDataFrame` of same schema to predict on new data.

```
gaussianGLM <- spark.glm[](https://spark.apache.org/docs/latest/api/R/reference/spark.glm.html)(carsDF, mpg ~ wt + hp)
summary[](https://spark.apache.org/docs/latest/api/R/reference/summary.html)(gaussianGLM)
```

When doing prediction, a new column called `prediction` will be appended. Let’s look at only a subset of columns here.

```
gaussianFitted <- predict[](https://spark.apache.org/docs/latest/api/R/reference/predict.html)(gaussianGLM, carsDF)
head[](https://spark.apache.org/docs/latest/api/R/reference/head.html)(select[](https://spark.apache.org/docs/latest/api/R/reference/select.html)(gaussianFitted, "model", "prediction", "mpg", "wt", "hp"))
```

The following is the same fit using the tweedie family:

```
tweedieGLM1 <- spark.glm[](https://spark.apache.org/docs/latest/api/R/reference/spark.glm.html)(carsDF, mpg ~ wt + hp, family = "tweedie", var.power = 0.0)
summary[](https://spark.apache.org/docs/latest/api/R/reference/summary.html)(tweedieGLM1)
```

We can try other distributions in the tweedie family, for example, a compound Poisson distribution with a log link:

```
tweedieGLM2 <- spark.glm[](https://spark.apache.org/docs/latest/api/R/reference/spark.glm.html)(carsDF, mpg ~ wt + hp, family = "tweedie",
                         var.power = 1.2, link.power = 0.0)
summary[](https://spark.apache.org/docs/latest/api/R/reference/summary.html)(tweedieGLM2)
```

#### Isotonic Regression[](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html#isotonic-regression)
`spark.isoreg` fits an [Isotonic Regression](https://en.wikipedia.org/wiki/Isotonic_regression) model against a `SparkDataFrame`. It solves a weighted univariate a regression problem under a complete order constraint. Specifically, given a set of real observed responses \\(y_1, \ldots, y_n\\), corresponding real features \\(x_1, \ldots, x_n\\), and optionally positive weights \\(w_1, \ldots, w_n\\), we want to find a monotone (piecewise linear) function \\(f\\) to minimize \\[ \ell(f) = \sum_{i=1}^n w_i (y_i - f(x_i))^2. \\]
There are a few more arguments that may be useful.
  * `weightCol`: a character string specifying the weight column.
  * `isotonic`: logical value indicating whether the output sequence should be isotonic/increasing (`TRUE`) or antitonic/decreasing (`FALSE`).
  * `featureIndex`: the index of the feature on the right hand side of the formula if it is a vector column (default: 0), no effect otherwise.


We use an artificial example to show the use.

```
y <- c[](https://rdrr.io/r/base/c.html)(3.0, 6.0, 8.0, 5.0, 7.0)
x <- c[](https://rdrr.io/r/base/c.html)(1.0, 2.0, 3.5, 3.0, 4.0)
w <- rep[](https://rdrr.io/r/base/rep.html)(1.0, 5)
data <- data.frame[](https://rdrr.io/r/base/data.frame.html)(y = y, x = x, w = w)
df <- createDataFrame[](https://spark.apache.org/docs/latest/api/R/reference/createDataFrame.html)(data)
isoregModel <- spark.isoreg[](https://spark.apache.org/docs/latest/api/R/reference/spark.isoreg.html)(df, y ~ x, weightCol = "w")
isoregFitted <- predict[](https://spark.apache.org/docs/latest/api/R/reference/predict.html)(isoregModel, df)
head[](https://spark.apache.org/docs/latest/api/R/reference/head.html)(select[](https://spark.apache.org/docs/latest/api/R/reference/select.html)(isoregFitted, "x", "y", "prediction"))
```

In the prediction stage, based on the fitted monotone piecewise function, the rules are:
  * If the prediction input exactly matches a training feature then associated prediction is returned. In case there are multiple predictions with the same feature then one of them is returned. Which one is undefined.
  * If the prediction input is lower or higher than all training features then prediction with lowest or highest feature is returned respectively. In case there are multiple predictions with the same feature then the lowest or highest is returned respectively.
  * If the prediction input falls between two training features then prediction is treated as piecewise linear function and interpolated value is calculated from the predictions of the two closest features. In case there are multiple values with the same feature then the same rules as in previous point are used.


For example, when the input is \\(3.2\\), the two closest feature values are \\(3.0\\) and \\(3.5\\), then predicted value would be a linear interpolation between the predicted values at \\(3.0\\) and \\(3.5\\).

```
newDF <- createDataFrame[](https://spark.apache.org/docs/latest/api/R/reference/createDataFrame.html)(data.frame[](https://rdrr.io/r/base/data.frame.html)(x = c[](https://rdrr.io/r/base/c.html)(1.5, 3.2)))
head[](https://spark.apache.org/docs/latest/api/R/reference/head.html)(predict[](https://spark.apache.org/docs/latest/api/R/reference/predict.html)(isoregModel, newDF))
```

#### Linear Regression[](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html#linear-regression)
Linear regression model.

```
model <- spark.lm[](https://spark.apache.org/docs/latest/api/R/reference/spark.lm.html)(carsDF, mpg ~ wt + hp)

summary[](https://spark.apache.org/docs/latest/api/R/reference/summary.html)(model)
predictions <- predict[](https://spark.apache.org/docs/latest/api/R/reference/predict.html)(model, carsDF)
head[](https://spark.apache.org/docs/latest/api/R/reference/head.html)(select[](https://spark.apache.org/docs/latest/api/R/reference/select.html)(predictions, predictions$prediction))
```

#### Factorization Machines Regressor[](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html#factorization-machines-regressor)
Factorization Machines for regression problems.
For background and details about the implementation of factorization machines, refer to the [Factorization Machines section](https://spark.apache.org/docs/latest/ml-classification-regression.html#factorization-machines).

```
model <- spark.fmRegressor[](https://spark.apache.org/docs/latest/api/R/reference/spark.fmRegressor.html)(carsDF, mpg ~ wt + hp)
summary[](https://spark.apache.org/docs/latest/api/R/reference/summary.html)(model)
predictions <- predict[](https://spark.apache.org/docs/latest/api/R/reference/predict.html)(model, carsDF)
head[](https://spark.apache.org/docs/latest/api/R/reference/head.html)(select[](https://spark.apache.org/docs/latest/api/R/reference/select.html)(predictions, predictions$prediction))
```

#### Decision Tree[](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html#decision-tree)
`spark.decisionTree` fits a [decision tree](https://en.wikipedia.org/wiki/Decision_tree_learning) classification or regression model on a `SparkDataFrame`. Users can call `summary` to get a summary of the fitted model, `predict` to make predictions, and `write.ml`/`read.ml` to save/load fitted models.
We use the `Titanic` dataset to train a decision tree and make predictions:

```
t <- as.data.frame[](https://spark.apache.org/docs/latest/api/R/reference/as.data.frame.html)(Titanic)
df <- createDataFrame[](https://spark.apache.org/docs/latest/api/R/reference/createDataFrame.html)(t)
dtModel <- spark.decisionTree[](https://spark.apache.org/docs/latest/api/R/reference/spark.decisionTree.html)(df, Survived ~ ., type = "classification", maxDepth = 2)
summary[](https://spark.apache.org/docs/latest/api/R/reference/summary.html)(dtModel)
predictions <- predict[](https://spark.apache.org/docs/latest/api/R/reference/predict.html)(dtModel, df)
head[](https://spark.apache.org/docs/latest/api/R/reference/head.html)(select[](https://spark.apache.org/docs/latest/api/R/reference/select.html)(predictions, "Class", "Sex", "Age", "Freq", "Survived", "prediction"))
```

#### Gradient-Boosted Trees[](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html#gradient-boosted-trees)
`spark.gbt` fits a [gradient-boosted tree](https://en.wikipedia.org/wiki/Gradient_boosting) classification or regression model on a `SparkDataFrame`. Users can call `summary` to get a summary of the fitted model, `predict` to make predictions, and `write.ml`/`read.ml` to save/load fitted models.
We use the `Titanic` dataset to train a gradient-boosted tree and make predictions:

```
t <- as.data.frame[](https://spark.apache.org/docs/latest/api/R/reference/as.data.frame.html)(Titanic)
df <- createDataFrame[](https://spark.apache.org/docs/latest/api/R/reference/createDataFrame.html)(t)
gbtModel <- spark.gbt[](https://spark.apache.org/docs/latest/api/R/reference/spark.gbt.html)(df, Survived ~ ., type = "classification", maxDepth = 2, maxIter = 2)
summary[](https://spark.apache.org/docs/latest/api/R/reference/summary.html)(gbtModel)
predictions <- predict[](https://spark.apache.org/docs/latest/api/R/reference/predict.html)(gbtModel, df)
head[](https://spark.apache.org/docs/latest/api/R/reference/head.html)(select[](https://spark.apache.org/docs/latest/api/R/reference/select.html)(predictions, "Class", "Sex", "Age", "Freq", "Survived", "prediction"))
```

#### Random Forest[](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html#random-forest)
`spark.randomForest` fits a [random forest](https://en.wikipedia.org/wiki/Random_forest) classification or regression model on a `SparkDataFrame`. Users can call `summary` to get a summary of the fitted model, `predict` to make predictions, and `write.ml`/`read.ml` to save/load fitted models.
In the following example, we use the `Titanic` dataset to train a random forest and make predictions:

```
t <- as.data.frame[](https://spark.apache.org/docs/latest/api/R/reference/as.data.frame.html)(Titanic)
df <- createDataFrame[](https://spark.apache.org/docs/latest/api/R/reference/createDataFrame.html)(t)
rfModel <- spark.randomForest[](https://spark.apache.org/docs/latest/api/R/reference/spark.randomForest.html)(df, Survived ~ ., type = "classification", maxDepth = 2, numTrees = 2)
summary[](https://spark.apache.org/docs/latest/api/R/reference/summary.html)(rfModel)
predictions <- predict[](https://spark.apache.org/docs/latest/api/R/reference/predict.html)(rfModel, df)
head[](https://spark.apache.org/docs/latest/api/R/reference/head.html)(select[](https://spark.apache.org/docs/latest/api/R/reference/select.html)(predictions, "Class", "Sex", "Age", "Freq", "Survived", "prediction"))
```

#### Bisecting k-Means[](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html#bisecting-k-means)
`spark.bisectingKmeans` is a kind of [hierarchical clustering](https://en.wikipedia.org/wiki/Hierarchical_clustering) using a divisive (or “top-down”) approach: all observations start in one cluster, and splits are performed recursively as one moves down the hierarchy.

```
t <- as.data.frame[](https://spark.apache.org/docs/latest/api/R/reference/as.data.frame.html)(Titanic)
training <- createDataFrame[](https://spark.apache.org/docs/latest/api/R/reference/createDataFrame.html)(t)
model <- spark.bisectingKmeans[](https://spark.apache.org/docs/latest/api/R/reference/spark.bisectingKmeans.html)(training, Class ~ Survived, k = 4)
summary[](https://spark.apache.org/docs/latest/api/R/reference/summary.html)(model)
fitted <- predict[](https://spark.apache.org/docs/latest/api/R/reference/predict.html)(model, training)
head[](https://spark.apache.org/docs/latest/api/R/reference/head.html)(select[](https://spark.apache.org/docs/latest/api/R/reference/select.html)(fitted, "Class", "prediction"))
```

#### Gaussian Mixture Model[](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html#gaussian-mixture-model)
`spark.gaussianMixture` fits multivariate [Gaussian Mixture Model](https://en.wikipedia.org/wiki/Mixture_model#Multivariate_Gaussian_mixture_model) (GMM) against a `SparkDataFrame`. [Expectation-Maximization](https://en.wikipedia.org/wiki/Expectation%E2%80%93maximization_algorithm) (EM) is used to approximate the maximum likelihood estimator (MLE) of the model.
We use a simulated example to demonstrate the usage.

```
X1 <- data.frame[](https://rdrr.io/r/base/data.frame.html)(V1 = rnorm[](https://rdrr.io/r/stats/Normal.html)(4), V2 = rnorm[](https://rdrr.io/r/stats/Normal.html)(4))
X2 <- data.frame[](https://rdrr.io/r/base/data.frame.html)(V1 = rnorm[](https://rdrr.io/r/stats/Normal.html)(6, 3), V2 = rnorm[](https://rdrr.io/r/stats/Normal.html)(6, 4))
data <- rbind[](https://spark.apache.org/docs/latest/api/R/reference/rbind.html)(X1, X2)
df <- createDataFrame[](https://spark.apache.org/docs/latest/api/R/reference/createDataFrame.html)(data)
gmmModel <- spark.gaussianMixture[](https://spark.apache.org/docs/latest/api/R/reference/spark.gaussianMixture.html)(df, ~ V1 + V2, k = 2)
summary[](https://spark.apache.org/docs/latest/api/R/reference/summary.html)(gmmModel)
gmmFitted <- predict[](https://spark.apache.org/docs/latest/api/R/reference/predict.html)(gmmModel, df)
head[](https://spark.apache.org/docs/latest/api/R/reference/head.html)(select[](https://spark.apache.org/docs/latest/api/R/reference/select.html)(gmmFitted, "V1", "V2", "prediction"))
```

#### k-Means Clustering[](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html#k-means-clustering)
`spark.kmeans` fits a \\(k\\)-means clustering model against a `SparkDataFrame`. As an unsupervised learning method, we don’t need a response variable. Hence, the left hand side of the R formula should be left blank. The clustering is based only on the variables on the right hand side.

```
kmeansModel <- spark.kmeans[](https://spark.apache.org/docs/latest/api/R/reference/spark.kmeans.html)(carsDF, ~ mpg + hp + wt, k = 3)
summary[](https://spark.apache.org/docs/latest/api/R/reference/summary.html)(kmeansModel)
kmeansPredictions <- predict[](https://spark.apache.org/docs/latest/api/R/reference/predict.html)(kmeansModel, carsDF)
head[](https://spark.apache.org/docs/latest/api/R/reference/head.html)(select[](https://spark.apache.org/docs/latest/api/R/reference/select.html)(kmeansPredictions, "model", "mpg", "hp", "wt", "prediction"), n = 20L)
```

#### Latent Dirichlet Allocation[](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html#latent-dirichlet-allocation)
`spark.lda` fits a [Latent Dirichlet Allocation](https://en.wikipedia.org/wiki/Latent_Dirichlet_allocation) model on a `SparkDataFrame`. It is often used in topic modeling in which topics are inferred from a collection of text documents. LDA can be thought of as a clustering algorithm as follows:
  * Topics correspond to cluster centers, and documents correspond to examples (rows) in a dataset.
  * Topics and documents both exist in a feature space, where feature vectors are vectors of word counts (bag of words).
  * Rather than clustering using a traditional distance, LDA uses a function based on a statistical model of how text documents are generated.


To use LDA, we need to specify a `features` column in `data` where each entry represents a document. There are two options for the column:
  * character string: This can be a string of the whole document. It will be parsed automatically. Additional stop words can be added in `customizedStopWords`.
  * libSVM: Each entry is a collection of words and will be processed directly.


Two more functions are provided for the fitted model.
  * `spark.posterior` returns a `SparkDataFrame` containing a column of posterior probabilities vectors named “topicDistribution”.
  * `spark.perplexity` returns the log perplexity of given `SparkDataFrame`, or the log perplexity of the training data if missing argument `data`.


For more information, see the help document `?spark.lda[](https://spark.apache.org/docs/latest/api/R/reference/spark.lda.html)`.
Let’s look an artificial example.

```
corpus <- data.frame[](https://rdrr.io/r/base/data.frame.html)(features = c[](https://rdrr.io/r/base/c.html)(
  "1 2 6 0 2 3 1 1 0 0 3",
  "1 3 0 1 3 0 0 2 0 0 1",
  "1 4 1 0 0 4 9 0 1 2 0",
  "2 1 0 3 0 0 5 0 2 3 9",
  "3 1 1 9 3 0 2 0 0 1 3",
  "4 2 0 3 4 5 1 1 1 4 0",
  "2 1 0 3 0 0 5 0 2 2 9",
  "1 1 1 9 2 1 2 0 0 1 3",
  "4 4 0 3 4 2 1 3 0 0 0",
  "2 8 2 0 3 0 2 0 2 7 2",
  "1 1 1 9 0 2 2 0 0 3 3",
  "4 1 0 0 4 5 1 3 0 1 0"))
corpusDF <- createDataFrame[](https://spark.apache.org/docs/latest/api/R/reference/createDataFrame.html)(corpus)
model <- spark.lda[](https://spark.apache.org/docs/latest/api/R/reference/spark.lda.html)(data = corpusDF, k = 5, optimizer = "em")
summary[](https://spark.apache.org/docs/latest/api/R/reference/summary.html)(model)
```


```
posterior <- spark.posterior[](https://spark.apache.org/docs/latest/api/R/reference/spark.lda.html)(model, corpusDF)
head[](https://spark.apache.org/docs/latest/api/R/reference/head.html)(posterior)
```


```
perplexity <- spark.perplexity[](https://spark.apache.org/docs/latest/api/R/reference/spark.lda.html)(model, corpusDF)
perplexity
```

#### Alternating Least Squares[](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html#alternating-least-squares)
`spark.als` learns latent factors in [collaborative filtering](https://en.wikipedia.org/wiki/Recommender_system#Collaborative_filtering) via [alternating least squares](https://dl.acm.org/doi/10.1109/MC.2009.263).
There are multiple options that can be configured in `spark.als`, including `rank`, `reg`, and `nonnegative`. For a complete list, refer to the help file.

```
ratings <- list[](https://rdrr.io/r/base/list.html)(list[](https://rdrr.io/r/base/list.html)(0, 0, 4.0), list[](https://rdrr.io/r/base/list.html)(0, 1, 2.0), list[](https://rdrr.io/r/base/list.html)(1, 1, 3.0), list[](https://rdrr.io/r/base/list.html)(1, 2, 4.0),
                list[](https://rdrr.io/r/base/list.html)(2, 1, 1.0), list[](https://rdrr.io/r/base/list.html)(2, 2, 5.0))
df <- createDataFrame[](https://spark.apache.org/docs/latest/api/R/reference/createDataFrame.html)(ratings, c[](https://rdrr.io/r/base/c.html)("user", "item", "rating"))
model <- spark.als[](https://spark.apache.org/docs/latest/api/R/reference/spark.als.html)(df, "rating", "user", "item", rank = 10, reg = 0.1, nonnegative = TRUE)
```

Extract latent factors.

```
stats <- summary[](https://spark.apache.org/docs/latest/api/R/reference/summary.html)(model)
userFactors <- stats$userFactors
itemFactors <- stats$itemFactors
head[](https://spark.apache.org/docs/latest/api/R/reference/head.html)(userFactors)
head[](https://spark.apache.org/docs/latest/api/R/reference/head.html)(itemFactors)
```

Make predictions.

```
predicted <- predict[](https://spark.apache.org/docs/latest/api/R/reference/predict.html)(model, df)
head[](https://spark.apache.org/docs/latest/api/R/reference/head.html)(predicted)
```

#### Power Iteration Clustering[](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html#power-iteration-clustering)
Power Iteration Clustering (PIC) is a scalable graph clustering algorithm. `spark.assignClusters` method runs the PIC algorithm and returns a cluster assignment for each input vertex.

```
df <- createDataFrame[](https://spark.apache.org/docs/latest/api/R/reference/createDataFrame.html)(list[](https://rdrr.io/r/base/list.html)(list[](https://rdrr.io/r/base/list.html)(0L, 1L, 1.0), list[](https://rdrr.io/r/base/list.html)(0L, 2L, 1.0),
                           list[](https://rdrr.io/r/base/list.html)(1L, 2L, 1.0), list[](https://rdrr.io/r/base/list.html)(3L, 4L, 1.0),
                           list[](https://rdrr.io/r/base/list.html)(4L, 0L, 0.1)),
                      schema = c[](https://rdrr.io/r/base/c.html)("src", "dst", "weight"))
head[](https://spark.apache.org/docs/latest/api/R/reference/head.html)(spark.assignClusters[](https://spark.apache.org/docs/latest/api/R/reference/spark.powerIterationClustering.html)(df, initMode = "degree", weightCol = "weight"))
```

#### FP-growth[](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html#fp-growth)
`spark.fpGrowth` executes FP-growth algorithm to mine frequent itemsets on a `SparkDataFrame`. `itemsCol` should be an array of values.

```
df <- selectExpr[](https://spark.apache.org/docs/latest/api/R/reference/selectExpr.html)(createDataFrame[](https://spark.apache.org/docs/latest/api/R/reference/createDataFrame.html)(data.frame[](https://rdrr.io/r/base/data.frame.html)(rawItems = c[](https://rdrr.io/r/base/c.html)(
  "T,R,U", "T,S", "V,R", "R,U,T,V", "R,S", "V,S,U", "U,R", "S,T", "V,R", "V,U,S",
  "T,V,U", "R,V", "T,S", "T,S", "S,T", "S,U", "T,R", "V,R", "S,V", "T,S,U"
))), "split(rawItems, ',') AS items")

fpm <- spark.fpGrowth[](https://spark.apache.org/docs/latest/api/R/reference/spark.fpGrowth.html)(df, minSupport = 0.2, minConfidence = 0.5)
```

`spark.freqItemsets` method can be used to retrieve a `SparkDataFrame` with the frequent itemsets.

```
head[](https://spark.apache.org/docs/latest/api/R/reference/head.html)(spark.freqItemsets[](https://spark.apache.org/docs/latest/api/R/reference/spark.fpGrowth.html)(fpm))
```

`spark.associationRules` returns a `SparkDataFrame` with the association rules.

```
head[](https://spark.apache.org/docs/latest/api/R/reference/head.html)(spark.associationRules[](https://spark.apache.org/docs/latest/api/R/reference/spark.fpGrowth.html)(fpm))
```

We can make predictions based on the `antecedent`.

```
head[](https://spark.apache.org/docs/latest/api/R/reference/head.html)(predict[](https://spark.apache.org/docs/latest/api/R/reference/predict.html)(fpm, df))
```

#### PrefixSpan[](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html#prefixspan)
`spark.findFrequentSequentialPatterns` method can be used to find the complete set of frequent sequential patterns in the input sequences of itemsets.

```
df <- createDataFrame[](https://spark.apache.org/docs/latest/api/R/reference/createDataFrame.html)(list[](https://rdrr.io/r/base/list.html)(list[](https://rdrr.io/r/base/list.html)(list[](https://rdrr.io/r/base/list.html)(list[](https://rdrr.io/r/base/list.html)(1L, 2L), list[](https://rdrr.io/r/base/list.html)(3L))),
                           list[](https://rdrr.io/r/base/list.html)(list[](https://rdrr.io/r/base/list.html)(list[](https://rdrr.io/r/base/list.html)(1L), list[](https://rdrr.io/r/base/list.html)(3L, 2L), list[](https://rdrr.io/r/base/list.html)(1L, 2L))),
                           list[](https://rdrr.io/r/base/list.html)(list[](https://rdrr.io/r/base/list.html)(list[](https://rdrr.io/r/base/list.html)(1L, 2L), list[](https://rdrr.io/r/base/list.html)(5L))),
                           list[](https://rdrr.io/r/base/list.html)(list[](https://rdrr.io/r/base/list.html)(list[](https://rdrr.io/r/base/list.html)(6L)))),
                      schema = c[](https://rdrr.io/r/base/c.html)("sequence"))
head[](https://spark.apache.org/docs/latest/api/R/reference/head.html)(spark.findFrequentSequentialPatterns[](https://spark.apache.org/docs/latest/api/R/reference/spark.prefixSpan.html)(df, minSupport = 0.5, maxPatternLength = 5L))
```

#### Kolmogorov-Smirnov Test[](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html#kolmogorov-smirnov-test)
`spark.kstest` runs a two-sided, one-sample [Kolmogorov-Smirnov (KS) test](https://en.wikipedia.org/wiki/Kolmogorov%E2%80%93Smirnov_test). Given a `SparkDataFrame`, the test compares continuous data in a given column `testCol` with the theoretical distribution specified by parameter `nullHypothesis`. Users can call `summary` to get a summary of the test results.
In the following example, we test whether the `Titanic` dataset’s `Freq` column follows a normal distribution. We set the parameters of the normal distribution using the mean and standard deviation of the sample.

```
t <- as.data.frame[](https://spark.apache.org/docs/latest/api/R/reference/as.data.frame.html)(Titanic)
df <- createDataFrame[](https://spark.apache.org/docs/latest/api/R/reference/createDataFrame.html)(t)
freqStats <- head[](https://spark.apache.org/docs/latest/api/R/reference/head.html)(select[](https://spark.apache.org/docs/latest/api/R/reference/select.html)(df, mean[](https://spark.apache.org/docs/latest/api/R/reference/column_aggregate_functions.html)(df$Freq), sd[](https://spark.apache.org/docs/latest/api/R/reference/column_aggregate_functions.html)(df$Freq)))
freqMean <- freqStats[1]
freqStd <- freqStats[2]

test <- spark.kstest[](https://spark.apache.org/docs/latest/api/R/reference/spark.kstest.html)(df, "Freq", "norm", c[](https://rdrr.io/r/base/c.html)(freqMean, freqStd))
testSummary <- summary[](https://spark.apache.org/docs/latest/api/R/reference/summary.html)(test)
testSummary
```

### Model Persistence[](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html#model-persistence)
The following example shows how to save/load an ML model in SparkR.

```
t <- as.data.frame[](https://spark.apache.org/docs/latest/api/R/reference/as.data.frame.html)(Titanic)
training <- createDataFrame[](https://spark.apache.org/docs/latest/api/R/reference/createDataFrame.html)(t)
gaussianGLM <- spark.glm[](https://spark.apache.org/docs/latest/api/R/reference/spark.glm.html)(training, Freq ~ Sex + Age, family = "gaussian")

# Save and then load a fitted MLlib model
modelPath <- tempfile[](https://rdrr.io/r/base/tempfile.html)(pattern = "ml", fileext = ".tmp")
write.ml[](https://spark.apache.org/docs/latest/api/R/reference/write.ml.html)(gaussianGLM, modelPath)
gaussianGLM2 <- read.ml[](https://spark.apache.org/docs/latest/api/R/reference/read.ml.html)(modelPath)

# Check model summary
summary[](https://spark.apache.org/docs/latest/api/R/reference/summary.html)(gaussianGLM2)

# Check model prediction
gaussianPredictions <- predict[](https://spark.apache.org/docs/latest/api/R/reference/predict.html)(gaussianGLM2, training)
head[](https://spark.apache.org/docs/latest/api/R/reference/head.html)(gaussianPredictions)

unlink[](https://rdrr.io/r/base/unlink.html)(modelPath)
```

## Structured Streaming[](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html#structured-streaming)
SparkR supports the Structured Streaming API.
You can check the Structured Streaming Programming Guide for [an introduction](https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html#programming-model) to its programming model and basic concepts.
### Simple Source and Sink[](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html#simple-source-and-sink)
Spark has a few built-in input sources. As an example, to test with a socket source reading text into words and displaying the computed word counts:

```
# Create DataFrame representing the stream of input lines from connection
lines <- read.stream[](https://spark.apache.org/docs/latest/api/R/reference/read.stream.html)("socket", host = hostname, port = port)

# Split the lines into words
words <- selectExpr[](https://spark.apache.org/docs/latest/api/R/reference/selectExpr.html)(lines, "explode(split(value, ' ')) as word")

# Generate running word count
wordCounts <- count[](https://spark.apache.org/docs/latest/api/R/reference/count.html)(groupBy[](https://spark.apache.org/docs/latest/api/R/reference/groupBy.html)(words, "word"))

# Start running the query that prints the running counts to the console
query <- write.stream[](https://spark.apache.org/docs/latest/api/R/reference/write.stream.html)(wordCounts, "console", outputMode = "complete")
```

### Kafka Source[](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html#kafka-source)
It is simple to read data from Kafka. For more information, see [Input Sources](https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html#input-sources) supported by Structured Streaming.

```
topic <- read.stream[](https://spark.apache.org/docs/latest/api/R/reference/read.stream.html)("kafka",
                     kafka.bootstrap.servers = "host1:port1,host2:port2",
                     subscribe = "topic1")
keyvalue <- selectExpr[](https://spark.apache.org/docs/latest/api/R/reference/selectExpr.html)(topic, "CAST(key AS STRING)", "CAST(value AS STRING)")
```

### Operations and Sinks[](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html#operations-and-sinks)
Most of the common operations on `SparkDataFrame` are supported for streaming, including selection, projection, and aggregation. Once you have defined the final result, to start the streaming computation, you will call the `write.stream` method setting a sink and `outputMode`.
A streaming `SparkDataFrame` can be written for debugging to the console, to a temporary in-memory table, or for further processing in a fault-tolerant manner to a File Sink in different formats.

```
noAggDF <- select[](https://spark.apache.org/docs/latest/api/R/reference/select.html)(where[](https://spark.apache.org/docs/latest/api/R/reference/filter.html)(deviceDataStreamingDf, "signal > 10"), "device")

# Print new data to console
write.stream[](https://spark.apache.org/docs/latest/api/R/reference/write.stream.html)(noAggDF, "console")

# Write new data to Parquet files
write.stream[](https://spark.apache.org/docs/latest/api/R/reference/write.stream.html)(noAggDF,
             "parquet",
             path = "path/to/destination/dir",
             checkpointLocation = "path/to/checkpoint/dir")

# Aggregate
aggDF <- count[](https://spark.apache.org/docs/latest/api/R/reference/count.html)(groupBy[](https://spark.apache.org/docs/latest/api/R/reference/groupBy.html)(noAggDF, "device"))

# Print updated aggregations to console
write.stream[](https://spark.apache.org/docs/latest/api/R/reference/write.stream.html)(aggDF, "console", outputMode = "complete")

# Have all the aggregates in an in memory table. The query name will be the table name
write.stream[](https://spark.apache.org/docs/latest/api/R/reference/write.stream.html)(aggDF, "memory", queryName = "aggregates", outputMode = "complete")

head[](https://spark.apache.org/docs/latest/api/R/reference/head.html)(sql[](https://spark.apache.org/docs/latest/api/R/reference/sql.html)("select * from aggregates"))
```

## Advanced Topics[](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html#advanced-topics)
### SparkR Object Classes[](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html#sparkr-object-classes)
There are three main object classes in SparkR you may be working with.
  * `SparkDataFrame`: the central component of SparkR. It is an S4 class representing distributed collection of data organized into named columns, which is conceptually equivalent to a table in a relational database or a data frame in R. It has two slots `sdf` and `env`.
    * `sdf` stores a reference to the corresponding Spark Dataset in the Spark JVM backend.
    * `env` saves the meta-information of the object such as `isCached`.
It can be created by data import methods or by transforming an existing `SparkDataFrame`. We can manipulate `SparkDataFrame` by numerous data processing functions and feed that into machine learning algorithms.
  * `Column`: an S4 class representing a column of `SparkDataFrame`. The slot `jc` saves a reference to the corresponding `Column` object in the Spark JVM backend.
It can be obtained from a `SparkDataFrame` by `$` operator, e.g., `df$col`. More often, it is used together with other functions, for example, with `select` to select particular columns, with `filter` and constructed conditions to select rows, with aggregation functions to compute aggregate statistics for each group.
  * `GroupedData`: an S4 class representing grouped data created by `groupBy` or by transforming other `GroupedData`. Its `sgd` slot saves a reference to a `RelationalGroupedDataset` object in the backend.
This is often an intermediate object with group information and followed up by aggregation operations.


### Architecture[](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html#architecture)
A complete description of architecture can be seen in the references, in particular the paper _SparkR: Scaling R Programs with Spark_.
Under the hood of SparkR is Spark SQL engine. This avoids the overheads of running interpreted R code, and the optimized SQL execution engine in Spark uses structural information about data and computation flow to perform a bunch of optimizations to speed up the computation.
The main method calls of actual computation happen in the Spark JVM of the driver. We have a socket-based SparkR API that allows us to invoke functions on the JVM from R. We use a SparkR JVM backend that listens on a Netty-based socket server.
Two kinds of RPCs are supported in the SparkR JVM backend: method invocation and creating new objects. Method invocation can be done in two ways.
  * `sparkR.callJMethod` takes a reference to an existing Java object and a list of arguments to be passed on to the method.
  * `sparkR.callJStatic` takes a class name for static method and a list of arguments to be passed on to the method.


The arguments are serialized using our custom wire format which is then deserialized on the JVM side. We then use Java reflection to invoke the appropriate method.
To create objects, `sparkR.newJObject` is used and then similarly the appropriate constructor is invoked with provided arguments.
Finally, we use a new R class `jobj` that refers to a Java object existing in the backend. These references are tracked on the Java side and are automatically garbage collected when they go out of scope on the R side.
## Appendix[](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html#appendix)
### R and Spark Data Types[](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html#DataTypes)  
| R  | Spark  |  
| --- | --- |  
| byte  | byte  |  
| integer  | integer  |  
| float  | float  |  
| double  | double  |  
| numeric  | double  |  
| character  | string  |  
| string  | string  |  
| binary  | binary  |  
| raw  | binary  |  
| logical  | boolean  |  
| POSIXct  | timestamp  |  
| POSIXlt  | timestamp  |  
| Date  | date  |  
| array  | array  |  
| list  | array  |  
| env  | map  |  
## References[](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html#references)
  * [Spark Cluster Mode Overview](https://spark.apache.org/docs/latest/cluster-overview.html)
  * [Submitting Spark Applications](https://spark.apache.org/docs/latest/submitting-applications.html)
  * [Machine Learning Library Guide (MLlib)](https://spark.apache.org/docs/latest/ml-guide.html)
  * [SparkR: Scaling R Programs with Spark](https://people.csail.mit.edu/matei/papers/2016/sigmod_sparkr.pdf), Shivaram Venkataraman, Zongheng Yang, Davies Liu, Eric Liang, Hossein Falaki, Xiangrui Meng, Reynold Xin, Ali Ghodsi, Michael Franklin, Ion Stoica, and Matei Zaharia. SIGMOD 2016. June 2016.


## On this page
Developed by [ The Apache Software Foundation](https://www.apache.org/).
Site built with [pkgdown](https://pkgdown.r-lib.org/) 2.0.1.
Using [preferably](https://preferably.amirmasoudabdol.name/?source=footer) template.
