[ ![](https://spark.apache.org/images/spark-logo-rev.svg)](https://spark.apache.org/docs/latest/index.html)4.1.2
  * [Overview](https://spark.apache.org/docs/latest/index.html)
  * [Programming Guides](https://spark.apache.org/docs/latest/sparkr.html)
[Quick Start](https://spark.apache.org/docs/latest/quick-start.html) [RDDs, Accumulators, Broadcasts Vars](https://spark.apache.org/docs/latest/rdd-programming-guide.html) [SQL, DataFrames, and Datasets](https://spark.apache.org/docs/latest/sql-programming-guide.html) [Structured Streaming](https://spark.apache.org/docs/latest/streaming/index.html) [Spark Streaming (DStreams)](https://spark.apache.org/docs/latest/streaming-programming-guide.html) [MLlib (Machine Learning)](https://spark.apache.org/docs/latest/ml-guide.html) [GraphX (Graph Processing)](https://spark.apache.org/docs/latest/graphx-programming-guide.html) [SparkR (R on Spark)](https://spark.apache.org/docs/latest/sparkr.html) [PySpark (Python on Spark)](https://spark.apache.org/docs/latest/api/python/getting_started/index.html) [Declarative Pipelines](https://spark.apache.org/docs/latest/declarative-pipelines-programming-guide.html)
  * [API Docs](https://spark.apache.org/docs/latest/sparkr.html)
[Python](https://spark.apache.org/docs/latest/api/python/index.html) [Scala](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html) [Java](https://spark.apache.org/docs/latest/api/java/index.html) [R](https://spark.apache.org/docs/latest/api/R/index.html) [SQL, Built-in Functions](https://spark.apache.org/docs/latest/api/sql/index.html)
  * [Deploying](https://spark.apache.org/docs/latest/sparkr.html)
[Overview](https://spark.apache.org/docs/latest/cluster-overview.html) [Submitting Applications](https://spark.apache.org/docs/latest/submitting-applications.html) [Spark Standalone](https://spark.apache.org/docs/latest/spark-standalone.html) [YARN](https://spark.apache.org/docs/latest/running-on-yarn.html) [Kubernetes](https://spark.apache.org/docs/latest/running-on-kubernetes.html)
  * [More](https://spark.apache.org/docs/latest/sparkr.html)
[Configuration](https://spark.apache.org/docs/latest/configuration.html) [Monitoring](https://spark.apache.org/docs/latest/monitoring.html) [Tuning Guide](https://spark.apache.org/docs/latest/tuning.html) [Job Scheduling](https://spark.apache.org/docs/latest/job-scheduling.html) [Security](https://spark.apache.org/docs/latest/security.html) [Hardware Provisioning](https://spark.apache.org/docs/latest/hardware-provisioning.html) [Migration Guide](https://spark.apache.org/docs/latest/migration-guide.html) [Building Spark](https://spark.apache.org/docs/latest/building-spark.html) [Contributing to Spark](https://spark.apache.org/contributing.html) [Third Party Projects](https://spark.apache.org/third-party-projects.html)
  * 

# SparkR (R on Spark)[](https://spark.apache.org/docs/latest/sparkr.html#sparkr-r-on-spark)
  * [Overview](https://spark.apache.org/docs/latest/sparkr.html#overview)
  * [SparkDataFrame](https://spark.apache.org/docs/latest/sparkr.html#sparkdataframe)
    * [Starting Up: SparkSession](https://spark.apache.org/docs/latest/sparkr.html#starting-up-sparksession)
    * [Starting Up from RStudio](https://spark.apache.org/docs/latest/sparkr.html#starting-up-from-rstudio)
    * [Creating SparkDataFrames](https://spark.apache.org/docs/latest/sparkr.html#creating-sparkdataframes)
      * [From local data frames](https://spark.apache.org/docs/latest/sparkr.html#from-local-data-frames)
      * [From Data Sources](https://spark.apache.org/docs/latest/sparkr.html#from-data-sources)
      * [From Hive tables](https://spark.apache.org/docs/latest/sparkr.html#from-hive-tables)
    * [SparkDataFrame Operations](https://spark.apache.org/docs/latest/sparkr.html#sparkdataframe-operations)
      * [Selecting rows, columns](https://spark.apache.org/docs/latest/sparkr.html#selecting-rows-columns)
      * [Grouping, Aggregation](https://spark.apache.org/docs/latest/sparkr.html#grouping-aggregation)
      * [Operating on Columns](https://spark.apache.org/docs/latest/sparkr.html#operating-on-columns)
      * [Applying User-Defined Function](https://spark.apache.org/docs/latest/sparkr.html#applying-user-defined-function)
        * [Run a given function on a large dataset using `dapply` or `dapplyCollect`](https://spark.apache.org/docs/latest/sparkr.html#run-a-given-function-on-a-large-dataset-using-dapply-or-dapplycollect)
          * [dapply](https://spark.apache.org/docs/latest/sparkr.html#dapply)
          * [dapplyCollect](https://spark.apache.org/docs/latest/sparkr.html#dapplycollect)
        * [Run a given function on a large dataset grouping by input column(s) and using `gapply` or `gapplyCollect`](https://spark.apache.org/docs/latest/sparkr.html#run-a-given-function-on-a-large-dataset-grouping-by-input-columns-and-using-gapply-or-gapplycollect)
          * [gapply](https://spark.apache.org/docs/latest/sparkr.html#gapply)
          * [gapplyCollect](https://spark.apache.org/docs/latest/sparkr.html#gapplycollect)
        * [Run local R functions distributed using `spark.lapply`](https://spark.apache.org/docs/latest/sparkr.html#run-local-r-functions-distributed-using-sparklapply)
          * [spark.lapply](https://spark.apache.org/docs/latest/sparkr.html#sparklapply)
      * [Eager execution](https://spark.apache.org/docs/latest/sparkr.html#eager-execution)
    * [Running SQL Queries from SparkR](https://spark.apache.org/docs/latest/sparkr.html#running-sql-queries-from-sparkr)
  * [Machine Learning](https://spark.apache.org/docs/latest/sparkr.html#machine-learning)
    * [Algorithms](https://spark.apache.org/docs/latest/sparkr.html#algorithms)
      * [Classification](https://spark.apache.org/docs/latest/sparkr.html#classification)
      * [Regression](https://spark.apache.org/docs/latest/sparkr.html#regression)
      * [Tree](https://spark.apache.org/docs/latest/sparkr.html#tree)
      * [Clustering](https://spark.apache.org/docs/latest/sparkr.html#clustering)
      * [Collaborative Filtering](https://spark.apache.org/docs/latest/sparkr.html#collaborative-filtering)
      * [Frequent Pattern Mining](https://spark.apache.org/docs/latest/sparkr.html#frequent-pattern-mining)
      * [Statistics](https://spark.apache.org/docs/latest/sparkr.html#statistics)
    * [Model persistence](https://spark.apache.org/docs/latest/sparkr.html#model-persistence)
  * [Data type mapping between R and Spark](https://spark.apache.org/docs/latest/sparkr.html#data-type-mapping-between-r-and-spark)
  * [Structured Streaming](https://spark.apache.org/docs/latest/sparkr.html#structured-streaming)
  * [Apache Arrow in SparkR](https://spark.apache.org/docs/latest/sparkr.html#apache-arrow-in-sparkr)
    * [Ensure Arrow Installed](https://spark.apache.org/docs/latest/sparkr.html#ensure-arrow-installed)
    * [Enabling for Conversion to/from R DataFrame, `dapply` and `gapply`](https://spark.apache.org/docs/latest/sparkr.html#enabling-for-conversion-tofrom-r-dataframe-dapply-and-gapply)
    * [Supported SQL Types](https://spark.apache.org/docs/latest/sparkr.html#supported-sql-types)
  * [R Function Name Conflicts](https://spark.apache.org/docs/latest/sparkr.html#r-function-name-conflicts)
  * [Migration Guide](https://spark.apache.org/docs/latest/sparkr.html#migration-guide)


SparkR is deprecated from Apache Spark 4.0.0 and will be removed in a future version.
# Overview[](https://spark.apache.org/docs/latest/sparkr.html#overview)
SparkR is an R package that provides a light-weight frontend to use Apache Spark from R. In Spark 4.1.2, SparkR provides a distributed data frame implementation that supports operations like selection, filtering, aggregation etc. (similar to R data frames, [dplyr](https://github.com/hadley/dplyr)) but on large datasets. SparkR also supports distributed machine learning using MLlib.
# SparkDataFrame[](https://spark.apache.org/docs/latest/sparkr.html#sparkdataframe)
A SparkDataFrame is a distributed collection of data organized into named columns. It is conceptually equivalent to a table in a relational database or a data frame in R, but with richer optimizations under the hood. SparkDataFrames can be constructed from a wide array of sources such as: structured data files, tables in Hive, external databases, or existing local R data frames.
All of the examples on this page use sample data included in R or the Spark distribution and can be run using the `./bin/sparkR` shell.
## Starting Up: SparkSession[](https://spark.apache.org/docs/latest/sparkr.html#starting-up-sparksession)
The entry point into SparkR is the `SparkSession` which connects your R program to a Spark cluster. You can create a `SparkSession` using `sparkR.session` and pass in options such as the application name, any spark packages depended on, etc. Further, you can also work with SparkDataFrames via `SparkSession`. If you are working from the `sparkR` shell, the `SparkSession` should already be created for you, and you would not need to call `sparkR.session`.

```
sparkR.session()
```

## Starting Up from RStudio[](https://spark.apache.org/docs/latest/sparkr.html#starting-up-from-rstudio)
You can also start SparkR from RStudio. You can connect your R program to a Spark cluster from RStudio, R shell, Rscript or other R IDEs. To start, make sure SPARK_HOME is set in environment (you can check [Sys.getenv](https://stat.ethz.ch/R-manual/R-devel/library/base/html/Sys.getenv.html)), load the SparkR package, and call `sparkR.session` as below. It will check for the Spark installation, and, if not found, it will be downloaded and cached automatically. Alternatively, you can also run `install.spark` manually.
In addition to calling `sparkR.session`, you could also specify certain Spark driver properties. Normally these [Application properties](https://spark.apache.org/docs/latest/configuration.html#application-properties) and [Runtime Environment](https://spark.apache.org/docs/latest/configuration.html#runtime-environment) cannot be set programmatically, as the driver JVM process would have been started, in this case SparkR takes care of this for you. To set them, pass them as you would other configuration properties in the `sparkConfig` argument to `sparkR.session()`.

```
if (nchar(Sys.getenv("SPARK_HOME")) < 1) {
  Sys.setenv(SPARK_HOME = "/home/spark")
}
library(SparkR, lib.loc = c(file.path(Sys.getenv("SPARK_HOME"), "R", "lib")))
sparkR.session(master = "local[*]", sparkConfig = list(spark.driver.memory = "2g"))
```

The following Spark driver properties can be set in `sparkConfig` with `sparkR.session` from RStudio:  
| Property Name  | Property group  |  `spark-submit` equivalent  |  
| --- | --- | --- |  
| `spark.master`  | Application Properties  | `--master`  |  
| `spark.kerberos.keytab`  | Application Properties  | `--keytab`  |  
| `spark.kerberos.principal`  | Application Properties  | `--principal`  |  
| `spark.driver.memory`  | Application Properties  | `--driver-memory`  |  
| `spark.driver.extraClassPath`  | Runtime Environment  | `--driver-class-path`  |  
| `spark.driver.extraJavaOptions`  | Runtime Environment  | `--driver-java-options`  |  
| `spark.driver.extraLibraryPath`  | Runtime Environment  | `--driver-library-path`  |  
## Creating SparkDataFrames[](https://spark.apache.org/docs/latest/sparkr.html#creating-sparkdataframes)
With a `SparkSession`, applications can create `SparkDataFrame`s from a local R data frame, from a [Hive table](https://spark.apache.org/docs/latest/sql-data-sources-hive-tables.html), or from other [data sources](https://spark.apache.org/docs/latest/sql-data-sources.html).
### From local data frames[](https://spark.apache.org/docs/latest/sparkr.html#from-local-data-frames)
The simplest way to create a data frame is to convert a local R data frame into a SparkDataFrame. Specifically, we can use `as.DataFrame` or `createDataFrame` and pass in the local R data frame to create a SparkDataFrame. As an example, the following creates a `SparkDataFrame` based using the `faithful` dataset from R.

```
df <- as.DataFrame(faithful)

# Displays the first part of the SparkDataFrame
head(df)
##  eruptions waiting
##1     3.600      79
##2     1.800      54
##3     3.333      74
```

### From Data Sources[](https://spark.apache.org/docs/latest/sparkr.html#from-data-sources)
SparkR supports operating on a variety of data sources through the `SparkDataFrame` interface. This section describes the general methods for loading and saving data using Data Sources. You can check the Spark SQL programming guide for more [specific options](https://spark.apache.org/docs/latest/sql-data-sources-load-save-functions.html#manually-specifying-options) that are available for the built-in data sources.
The general method for creating SparkDataFrames from data sources is `read.df`. This method takes in the path for the file to load and the type of data source, and the currently active SparkSession will be used automatically. SparkR supports reading JSON, CSV and Parquet files natively, and through packages available from sources like [Third Party Projects](https://spark.apache.org/third-party-projects.html), you can find data source connectors for popular file formats like Avro. These packages can either be added by specifying `--packages` with `spark-submit` or `sparkR` commands, or if initializing SparkSession with `sparkPackages` parameter when in an interactive R shell or from RStudio.

```
sparkR.session(sparkPackages = "org.apache.spark:spark-avro_2.13:4.1.2")
```

We can see how to use data sources using an example JSON input file. Note that the file that is used here is _not_ a typical JSON file. Each line in the file must contain a separate, self-contained valid JSON object. For more information, please see [JSON Lines text format, also called newline-delimited JSON](http://jsonlines.org/). As a consequence, a regular multi-line JSON file will most often fail.

```
people <- read.df("./examples/src/main/resources/people.json", "json")
head(people)
##  age    name
##1  NA Michael
##2  30    Andy
##3  19  Justin

# SparkR automatically infers the schema from the JSON file
printSchema(people)
# root
#  |-- age: long (nullable = true)
#  |-- name: string (nullable = true)

# Similarly, multiple files can be read with read.json
people <- read.json(c("./examples/src/main/resources/people.json", "./examples/src/main/resources/people2.json"))
```

The data sources API natively supports CSV formatted input files. For more information please refer to SparkR [read.df](https://spark.apache.org/docs/latest/api/R/reference/read.df.html) API documentation.

```
df <- read.df(csvPath, "csv", header = "true", inferSchema = "true", na.strings = "NA")
```

The data sources API can also be used to save out SparkDataFrames into multiple file formats. For example, we can save the SparkDataFrame from the previous example to a Parquet file using `write.df`.

```
write.df(people, path = "people.parquet", source = "parquet", mode = "overwrite")
```

### From Hive tables[](https://spark.apache.org/docs/latest/sparkr.html#from-hive-tables)
You can also create SparkDataFrames from Hive tables. To do this we will need to create a SparkSession with Hive support which can access tables in the Hive MetaStore. Note that Spark should have been built with [Hive support](https://spark.apache.org/docs/latest/building-spark.html#building-with-hive-and-jdbc-support) and more details can be found in the [SQL programming guide](https://spark.apache.org/docs/latest/sql-getting-started.html#starting-point-sparksession). In SparkR, by default it will attempt to create a SparkSession with Hive support enabled (`enableHiveSupport = TRUE`).

```
sparkR.session()

sql("CREATE TABLE IF NOT EXISTS src (key INT, value STRING)")
sql("LOAD DATA LOCAL INPATH 'examples/src/main/resources/kv1.txt' INTO TABLE src")

# Queries can be expressed in HiveQL.
results <- sql("FROM src SELECT key, value")

# results is now a SparkDataFrame
head(results)
##  key   value
## 1 238 val_238
## 2  86  val_86
## 3 311 val_311
```

## SparkDataFrame Operations[](https://spark.apache.org/docs/latest/sparkr.html#sparkdataframe-operations)
SparkDataFrames support a number of functions to do structured data processing. Here we include some basic examples and a complete list can be found in the [API](https://spark.apache.org/docs/latest/api/R/index.html) docs:
### Selecting rows, columns[](https://spark.apache.org/docs/latest/sparkr.html#selecting-rows-columns)

```
# Create the SparkDataFrame
df <- as.DataFrame(faithful)

# Get basic information about the SparkDataFrame
df
## SparkDataFrame[eruptions:double, waiting:double]

# Select only the "eruptions" column
head(select(df, df$eruptions))
##  eruptions
##1     3.600
##2     1.800
##3     3.333

# You can also pass in column name as strings
head(select(df, "eruptions"))

# Filter the SparkDataFrame to only retain rows with wait times shorter than 50 mins
head(filter(df, df$waiting < 50))
##  eruptions waiting
##1     1.750      47
##2     1.750      47
##3     1.867      48
```

### Grouping, Aggregation[](https://spark.apache.org/docs/latest/sparkr.html#grouping-aggregation)
SparkR data frames support a number of commonly used functions to aggregate data after grouping. For example, we can compute a histogram of the `waiting` time in the `faithful` dataset as shown below

```
# We use the `n` operator to count the number of times each waiting time appears
head(summarize(groupBy(df, df$waiting), count = n(df$waiting)))
##  waiting count
##1      70     4
##2      67     1
##3      69     2

# We can also sort the output from the aggregation to get the most common waiting times
waiting_counts <- summarize(groupBy(df, df$waiting), count = n(df$waiting))
head(arrange(waiting_counts, desc(waiting_counts$count)))
##   waiting count
##1      78    15
##2      83    14
##3      81    13
```

In addition to standard aggregations, SparkR supports [OLAP cube](https://en.wikipedia.org/wiki/OLAP_cube) operators `cube`:

```
head(agg(cube(df, "cyl", "disp", "gear"), avg(df$mpg)))
##  cyl  disp gear avg(mpg)
##1  NA 140.8    4     22.8
##2   4  75.7    4     30.4
##3   8 400.0    3     19.2
##4   8 318.0    3     15.5
##5  NA 351.0   NA     15.8
##6  NA 275.8   NA     16.3
```

and `rollup`:

```
head(agg(rollup(df, "cyl", "disp", "gear"), avg(df$mpg)))
##  cyl  disp gear avg(mpg)
##1   4  75.7    4     30.4
##2   8 400.0    3     19.2
##3   8 318.0    3     15.5
##4   4  78.7   NA     32.4
##5   8 304.0    3     15.2
##6   4  79.0   NA     27.3
```

### Operating on Columns[](https://spark.apache.org/docs/latest/sparkr.html#operating-on-columns)
SparkR also provides a number of functions that can be directly applied to columns for data processing and during aggregation. The example below shows the use of basic arithmetic functions.

```
# Convert waiting time from hours to seconds.
# Note that we can assign this to a new column in the same SparkDataFrame
df$waiting_secs <- df$waiting * 60
head(df)
##  eruptions waiting waiting_secs
##1     3.600      79         4740
##2     1.800      54         3240
##3     3.333      74         4440
```

### Applying User-Defined Function[](https://spark.apache.org/docs/latest/sparkr.html#applying-user-defined-function)
In SparkR, we support several kinds of User-Defined Functions:
#### Run a given function on a large dataset using `dapply` or `dapplyCollect`[](https://spark.apache.org/docs/latest/sparkr.html#run-a-given-function-on-a-large-dataset-using-dapply-or-dapplycollect)
##### dapply[](https://spark.apache.org/docs/latest/sparkr.html#dapply)
Apply a function to each partition of a `SparkDataFrame`. The function to be applied to each partition of the `SparkDataFrame` and should have only one parameter, to which a `data.frame` corresponds to each partition will be passed. The output of function should be a `data.frame`. Schema specifies the row format of the resulting a `SparkDataFrame`. It must match to [data types](https://spark.apache.org/docs/latest/sparkr.html#data-type-mapping-between-r-and-spark) of returned value.

```
# Convert waiting time from hours to seconds.
# Note that we can apply UDF to DataFrame.
schema <- structType(structField("eruptions", "double"), structField("waiting", "double"),
                     structField("waiting_secs", "double"))
df1 <- dapply(df, function(x) { x <- cbind(x, x$waiting * 60) }, schema)
head(collect(df1))
##  eruptions waiting waiting_secs
##1     3.600      79         4740
##2     1.800      54         3240
##3     3.333      74         4440
##4     2.283      62         3720
##5     4.533      85         5100
##6     2.883      55         3300
```

##### dapplyCollect[](https://spark.apache.org/docs/latest/sparkr.html#dapplycollect)
Like `dapply`, apply a function to each partition of a `SparkDataFrame` and collect the result back. The output of function should be a `data.frame`. But, Schema is not required to be passed. Note that `dapplyCollect` can fail if the output of UDF run on all the partition cannot be pulled to the driver and fit in driver memory.

```
# Convert waiting time from hours to seconds.
# Note that we can apply UDF to DataFrame and return a R's data.frame
ldf <- dapplyCollect(
         df,
         function(x) {
           x <- cbind(x, "waiting_secs" = x$waiting * 60)
         })
head(ldf, 3)
##  eruptions waiting waiting_secs
##1     3.600      79         4740
##2     1.800      54         3240
##3     3.333      74         4440
```

#### Run a given function on a large dataset grouping by input column(s) and using `gapply` or `gapplyCollect`[](https://spark.apache.org/docs/latest/sparkr.html#run-a-given-function-on-a-large-dataset-grouping-by-input-columns-and-using-gapply-or-gapplycollect)
##### gapply[](https://spark.apache.org/docs/latest/sparkr.html#gapply)
Apply a function to each group of a `SparkDataFrame`. The function is to be applied to each group of the `SparkDataFrame` and should have only two parameters: grouping key and R `data.frame` corresponding to that key. The groups are chosen from `SparkDataFrame`s column(s). The output of function should be a `data.frame`. Schema specifies the row format of the resulting `SparkDataFrame`. It must represent R function’s output schema on the basis of Spark [data types](https://spark.apache.org/docs/latest/sparkr.html#data-type-mapping-between-r-and-spark). The column names of the returned `data.frame` are set by user.

```
# Determine six waiting times with the largest eruption time in minutes.
schema <- structType(structField("waiting", "double"), structField("max_eruption", "double"))
result <- gapply(
    df,
    "waiting",
    function(key, x) {
        y <- data.frame(key, max(x$eruptions))
    },
    schema)
head(collect(arrange(result, "max_eruption", decreasing = TRUE)))

##    waiting   max_eruption
##1      64       5.100
##2      69       5.067
##3      71       5.033
##4      87       5.000
##5      63       4.933
##6      89       4.900
```

##### gapplyCollect[](https://spark.apache.org/docs/latest/sparkr.html#gapplycollect)
Like `gapply`, applies a function to each partition of a `SparkDataFrame` and collect the result back to R data.frame. The output of the function should be a `data.frame`. But, the schema is not required to be passed. Note that `gapplyCollect` can fail if the output of UDF run on all the partition cannot be pulled to the driver and fit in driver memory.

```
# Determine six waiting times with the largest eruption time in minutes.
result <- gapplyCollect(
    df,
    "waiting",
    function(key, x) {
        y <- data.frame(key, max(x$eruptions))
        colnames(y) <- c("waiting", "max_eruption")
        y
    })
head(result[order(result$max_eruption, decreasing = TRUE), ])

##    waiting   max_eruption
##1      64       5.100
##2      69       5.067
##3      71       5.033
##4      87       5.000
##5      63       4.933
##6      89       4.900
```

#### Run local R functions distributed using `spark.lapply`[](https://spark.apache.org/docs/latest/sparkr.html#run-local-r-functions-distributed-using-sparklapply)
##### spark.lapply[](https://spark.apache.org/docs/latest/sparkr.html#sparklapply)
Similar to `lapply` in native R, `spark.lapply` runs a function over a list of elements and distributes the computations with Spark. Applies a function in a manner that is similar to `doParallel` or `lapply` to elements of a list. The results of all the computations should fit in a single machine. If that is not the case they can do something like `df <- createDataFrame(list)` and then use `dapply`

```
# Perform distributed training of multiple models with spark.lapply. Here, we pass
# a read-only list of arguments which specifies family the generalized linear model should be.
families <- c("gaussian", "poisson")
train <- function(family) {
  model <- glm(Sepal.Length ~ Sepal.Width + Species, iris, family = family)
  summary(model)
}
# Return a list of model's summaries
model.summaries <- spark.lapply(families, train)

# Print the summary of each model
print(model.summaries)
```

### Eager execution[](https://spark.apache.org/docs/latest/sparkr.html#eager-execution)
If eager execution is enabled, the data will be returned to R client immediately when the `SparkDataFrame` is created. By default, eager execution is not enabled and can be enabled by setting the configuration property `spark.sql.repl.eagerEval.enabled` to `true` when the `SparkSession` is started up.
Maximum number of rows and maximum number of characters per column of data to display can be controlled by `spark.sql.repl.eagerEval.maxNumRows` and `spark.sql.repl.eagerEval.truncate` configuration properties, respectively. These properties are only effective when eager execution is enabled. If these properties are not set explicitly, by default, data up to 20 rows and up to 20 characters per column will be showed.

```
# Start up spark session with eager execution enabled
sparkR.session(master = "local[*]",
               sparkConfig = list(spark.sql.repl.eagerEval.enabled = "true",
                                  spark.sql.repl.eagerEval.maxNumRows = as.integer(10)))

# Create a grouped and sorted SparkDataFrame
df <- createDataFrame(faithful)
df2 <- arrange(summarize(groupBy(df, df$waiting), count = n(df$waiting)), "waiting")

# Similar to R data.frame, displays the data returned, instead of SparkDataFrame class string
df2

##+-------+-----+
##|waiting|count|
##+-------+-----+
##|   43.0|    1|
##|   45.0|    3|
##|   46.0|    5|
##|   47.0|    4|
##|   48.0|    3|
##|   49.0|    5|
##|   50.0|    5|
##|   51.0|    6|
##|   52.0|    5|
##|   53.0|    7|
##+-------+-----+
##only showing top 10 rows
```

Note that to enable eager execution in `sparkR` shell, add `spark.sql.repl.eagerEval.enabled=true` configuration property to the `--conf` option.
## Running SQL Queries from SparkR[](https://spark.apache.org/docs/latest/sparkr.html#running-sql-queries-from-sparkr)
A SparkDataFrame can also be registered as a temporary view in Spark SQL and that allows you to run SQL queries over its data. The `sql` function enables applications to run SQL queries programmatically and returns the result as a `SparkDataFrame`.

```
# Load a JSON file
people <- read.df("./examples/src/main/resources/people.json", "json")

# Register this SparkDataFrame as a temporary view.
createOrReplaceTempView(people, "people")

# SQL statements can be run by using the sql method
teenagers <- sql("SELECT name FROM people WHERE age >= 13 AND age <= 19")
head(teenagers)
##    name
##1 Justin
```

# Machine Learning[](https://spark.apache.org/docs/latest/sparkr.html#machine-learning)
## Algorithms[](https://spark.apache.org/docs/latest/sparkr.html#algorithms)
SparkR supports the following machine learning algorithms currently:
#### Classification[](https://spark.apache.org/docs/latest/sparkr.html#classification)
  * [`spark.logit`](https://spark.apache.org/docs/latest/api/R/reference/spark.logit.html): [`Logistic Regression`](https://spark.apache.org/docs/latest/ml-classification-regression.html#logistic-regression)
  * [`spark.mlp`](https://spark.apache.org/docs/latest/api/R/reference/spark.mlp.html): [`Multilayer Perceptron (MLP)`](https://spark.apache.org/docs/latest/ml-classification-regression.html#multilayer-perceptron-classifier)
  * [`spark.naiveBayes`](https://spark.apache.org/docs/latest/api/R/reference/spark.naiveBayes.html): [`Naive Bayes`](https://spark.apache.org/docs/latest/ml-classification-regression.html#naive-bayes)
  * [`spark.svmLinear`](https://spark.apache.org/docs/latest/api/R/reference/spark.svmLinear.html): [`Linear Support Vector Machine`](https://spark.apache.org/docs/latest/ml-classification-regression.html#linear-support-vector-machine)
  * [`spark.fmClassifier`](https://spark.apache.org/docs/latest/api/R/reference/fmClassifier.html): [`Factorization Machines classifier`](https://spark.apache.org/docs/latest/ml-classification-regression.html#factorization-machines-classifier)


#### Regression[](https://spark.apache.org/docs/latest/sparkr.html#regression)
  * [`spark.survreg`](https://spark.apache.org/docs/latest/api/R/reference/spark.survreg.html): [`Accelerated Failure Time (AFT) Survival  Model`](https://spark.apache.org/docs/latest/ml-classification-regression.html#survival-regression)
  * [`spark.glm`](https://spark.apache.org/docs/latest/api/R/reference/spark.glm.html) or [`glm`](https://spark.apache.org/docs/latest/api/R/reference/glm.html): [`Generalized Linear Model (GLM)`](https://spark.apache.org/docs/latest/ml-classification-regression.html#generalized-linear-regression)
  * [`spark.isoreg`](https://spark.apache.org/docs/latest/api/R/reference/spark.isoreg.html): [`Isotonic Regression`](https://spark.apache.org/docs/latest/ml-classification-regression.html#isotonic-regression)
  * [`spark.lm`](https://spark.apache.org/docs/latest/api/R/reference/spark.lm.html): [`Linear Regression`](https://spark.apache.org/docs/latest/ml-classification-regression.html#linear-regression)
  * [`spark.fmRegressor`](https://spark.apache.org/docs/latest/api/R/reference/spark.fmRegressor.html): [`Factorization Machines regressor`](https://spark.apache.org/docs/latest/ml-classification-regression.html#factorization-machines-regressor)


#### Tree[](https://spark.apache.org/docs/latest/sparkr.html#tree)
  * [`spark.decisionTree`](https://spark.apache.org/docs/latest/api/R/reference/spark.decisionTree.html): `Decision Tree for` [`Regression`](https://spark.apache.org/docs/latest/ml-classification-regression.html#decision-tree-regression) `and` [`Classification`](https://spark.apache.org/docs/latest/ml-classification-regression.html#decision-tree-classifier)
  * [`spark.gbt`](https://spark.apache.org/docs/latest/api/R/reference/spark.gbt.html): `Gradient Boosted Trees for` [`Regression`](https://spark.apache.org/docs/latest/ml-classification-regression.html#gradient-boosted-tree-regression) `and` [`Classification`](https://spark.apache.org/docs/latest/ml-classification-regression.html#gradient-boosted-tree-classifier)
  * [`spark.randomForest`](https://spark.apache.org/docs/latest/api/R/reference/spark.randomForest.html): `Random Forest for` [`Regression`](https://spark.apache.org/docs/latest/ml-classification-regression.html#random-forest-regression) `and` [`Classification`](https://spark.apache.org/docs/latest/ml-classification-regression.html#random-forest-classifier)


#### Clustering[](https://spark.apache.org/docs/latest/sparkr.html#clustering)
  * [`spark.bisectingKmeans`](https://spark.apache.org/docs/latest/api/R/reference/spark.bisectingKmeans.html): [`Bisecting k-means`](https://spark.apache.org/docs/latest/ml-clustering.html#bisecting-k-means)
  * [`spark.gaussianMixture`](https://spark.apache.org/docs/latest/api/R/reference/spark.gaussianMixture.html): [`Gaussian Mixture Model (GMM)`](https://spark.apache.org/docs/latest/ml-clustering.html#gaussian-mixture-model-gmm)
  * [`spark.kmeans`](https://spark.apache.org/docs/latest/api/R/reference/spark.kmeans.html): [`K-Means`](https://spark.apache.org/docs/latest/ml-clustering.html#k-means)
  * [`spark.lda`](https://spark.apache.org/docs/latest/api/R/reference/spark.lda.html): [`Latent Dirichlet Allocation (LDA)`](https://spark.apache.org/docs/latest/ml-clustering.html#latent-dirichlet-allocation-lda)
  * [`spark.powerIterationClustering (PIC)`](https://spark.apache.org/docs/latest/api/R/reference/spark.powerIterationClustering.html): [`Power Iteration Clustering (PIC)`](https://spark.apache.org/docs/latest/ml-clustering.html#power-iteration-clustering-pic)


#### Collaborative Filtering[](https://spark.apache.org/docs/latest/sparkr.html#collaborative-filtering)
  * [`spark.als`](https://spark.apache.org/docs/latest/api/R/reference/spark.als.html): [`Alternating Least Squares (ALS)`](https://spark.apache.org/docs/latest/ml-collaborative-filtering.html#collaborative-filtering)


#### Frequent Pattern Mining[](https://spark.apache.org/docs/latest/sparkr.html#frequent-pattern-mining)
  * [`spark.fpGrowth`](https://spark.apache.org/docs/latest/api/R/reference/spark.fpGrowth.html) : [`FP-growth`](https://spark.apache.org/docs/latest/ml-frequent-pattern-mining.html#fp-growth)
  * [`spark.prefixSpan`](https://spark.apache.org/docs/latest/api/R/reference/spark.prefixSpan.html) : [`PrefixSpan`](https://spark.apache.org/docs/latest/ml-frequent-pattern-mining.html#prefixspan)


#### Statistics[](https://spark.apache.org/docs/latest/sparkr.html#statistics)
  * [`spark.kstest`](https://spark.apache.org/docs/latest/api/R/reference/spark.kstest.html): `Kolmogorov-Smirnov Test`


Under the hood, SparkR uses MLlib to train the model. Please refer to the corresponding section of MLlib user guide for example code. Users can call `summary` to print a summary of the fitted model, [predict](https://spark.apache.org/docs/latest/api/R/reference/predict.html) to make predictions on new data, and [write.ml](https://spark.apache.org/docs/latest/api/R/reference/write.ml.html)/[read.ml](https://spark.apache.org/docs/latest/api/R/reference/read.ml.html) to save/load fitted models. SparkR supports a subset of the available R formula operators for model fitting, including ‘~’, ‘.’, ‘:’, ‘+’, and ‘-‘.
## Model persistence[](https://spark.apache.org/docs/latest/sparkr.html#model-persistence)
The following example shows how to save/load a MLlib model by SparkR.

```
training <- read.df("data/mllib/sample_multiclass_classification_data.txt", source = "libsvm")
# Fit a generalized linear model of family "gaussian" with spark.glm
df_list <- randomSplit(training, c(7,3), 2)
gaussianDF <- df_list[[1]]
gaussianTestDF <- df_list[[2]]
gaussianGLM <- spark.glm(gaussianDF, label ~ features, family = "gaussian")

# Save and then load a fitted MLlib model
modelPath <- tempfile(pattern = "ml", fileext = ".tmp")
write.ml(gaussianGLM, modelPath)
gaussianGLM2 <- read.ml(modelPath)

# Check model summary
summary(gaussianGLM2)

# Check model prediction
gaussianPredictions <- predict(gaussianGLM2, gaussianTestDF)
head(gaussianPredictions)

unlink(modelPath)
```

Find full example code at "examples/src/main/r/ml/ml.R" in the Spark repo.
# Data type mapping between R and Spark[](https://spark.apache.org/docs/latest/sparkr.html#data-type-mapping-between-r-and-spark)  
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
| [POSIXct](https://stat.ethz.ch/R-manual/R-devel/library/base/html/DateTimeClasses.html)  | timestamp  |  
| [POSIXlt](https://stat.ethz.ch/R-manual/R-devel/library/base/html/DateTimeClasses.html)  | timestamp  |  
| [Date](https://stat.ethz.ch/R-manual/R-devel/library/base/html/Dates.html)  | date  |  
| array  | array  |  
| list  | array  |  
| env  | map  |  
# Structured Streaming[](https://spark.apache.org/docs/latest/sparkr.html#structured-streaming)
SparkR supports the Structured Streaming API. Structured Streaming is a scalable and fault-tolerant stream processing engine built on the Spark SQL engine. For more information see the R API on the [Structured Streaming Programming Guide](https://spark.apache.org/docs/latest/streaming/index.html).
# Apache Arrow in SparkR[](https://spark.apache.org/docs/latest/sparkr.html#apache-arrow-in-sparkr)
Apache Arrow is an in-memory columnar data format that is used in Spark to efficiently transfer data between JVM and R processes. See also PySpark optimization done, [PySpark Usage Guide for Pandas with Apache Arrow](https://spark.apache.org/docs/latest/sql-pyspark-pandas-with-arrow.html). This guide targets to explain how to use Arrow optimization in SparkR with some key points.
## Ensure Arrow Installed[](https://spark.apache.org/docs/latest/sparkr.html#ensure-arrow-installed)
Arrow R library is available on CRAN and it can be installed as below.

```
Rscript -e 'install.packages("arrow", repos="https://cloud.r-project.org/")'

```

Please refer [the official documentation of Apache Arrow](https://arrow.apache.org/docs/r/) for more details.
Note that you must ensure that Arrow R package is installed and available on all cluster nodes. The current supported minimum version is 1.0.0; however, this might change between the minor releases since Arrow optimization in SparkR is experimental.
## Enabling for Conversion to/from R DataFrame, `dapply` and `gapply`[](https://spark.apache.org/docs/latest/sparkr.html#enabling-for-conversion-tofrom-r-dataframe-dapply-and-gapply)
Arrow optimization is available when converting a Spark DataFrame to an R DataFrame using the call `collect(spark_df)`, when creating a Spark DataFrame from an R DataFrame with `createDataFrame(r_df)`, when applying an R native function to each partition via `dapply(...)` and when applying an R native function to grouped data via `gapply(...)`. To use Arrow when executing these, users need to set the Spark configuration ‘spark.sql.execution.arrow.sparkr.enabled’ to ‘true’ first. This is disabled by default.
Whether the optimization is enabled or not, SparkR produces the same results. In addition, the conversion between Spark DataFrame and R DataFrame falls back automatically to non-Arrow optimization implementation when the optimization fails for any reasons before the actual computation.

```
# Start up spark session with Arrow optimization enabled
sparkR.session(master = "local[*]",
               sparkConfig = list(spark.sql.execution.arrow.sparkr.enabled = "true"))

# Converts Spark DataFrame from an R DataFrame
spark_df <- createDataFrame(mtcars)

# Converts Spark DataFrame to an R DataFrame
collect(spark_df)

# Apply an R native function to each partition.
collect(dapply(spark_df, function(rdf) { data.frame(rdf$gear + 1) }, structType("gear double")))

# Apply an R native function to grouped data.
collect(gapply(spark_df,
               "gear",
               function(key, group) {
                 data.frame(gear = key[[1]], disp = mean(group$disp) > group$disp)
               },
               structType("gear double, disp boolean")))
```

Note that even with Arrow, `collect(spark_df)` results in the collection of all records in the DataFrame to the driver program and should be done on a small subset of the data. In addition, the specified output schema in `gapply(...)` and `dapply(...)` should be matched to the R DataFrame’s returned by the given function.
## Supported SQL Types[](https://spark.apache.org/docs/latest/sparkr.html#supported-sql-types)
Currently, all Spark SQL data types are supported by Arrow-based conversion except `FloatType`, `BinaryType`, `ArrayType`, `StructType` and `MapType`.
# R Function Name Conflicts[](https://spark.apache.org/docs/latest/sparkr.html#r-function-name-conflicts)
When loading and attaching a new package in R, it is possible to have a name [conflict](https://stat.ethz.ch/R-manual/R-devel/library/base/html/library.html), where a function is masking another function.
The following functions are masked by the SparkR package:  
| Masked function  | How to Access  |  
| --- | --- |  
|  `cov` in `package:stats`  | `
```
stats::cov(x, y = NULL, use = "everything",
           method = c("pearson", "kendall", "spearman"))
```
`  |  
|  `filter` in `package:stats`  | `
```
stats::filter(x, filter, method = c("convolution", "recursive"),
              sides = 2, circular = FALSE, init)
```
`  |  
|  `sample` in `package:base`  | `base::sample(x, size, replace = FALSE, prob = NULL)`  |  
Since part of SparkR is modeled on the `dplyr` package, certain functions in SparkR share the same names with those in `dplyr`. Depending on the load order of the two packages, some functions from the package loaded first are masked by those in the package loaded after. In such case, prefix such calls with the package name, for instance, `SparkR::cume_dist(x)` or `dplyr::cume_dist(x)`.
You can inspect the search path in R with [`search()`](https://stat.ethz.ch/R-manual/R-devel/library/base/html/search.html)
# Migration Guide[](https://spark.apache.org/docs/latest/sparkr.html#migration-guide)
The migration guide is now archived [on this page](https://spark.apache.org/docs/latest/sparkr-migration-guide.html).
