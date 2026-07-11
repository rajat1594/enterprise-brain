[ ![](https://spark.apache.org/images/spark-logo-rev.svg)](https://spark.apache.org/docs/latest/index.html)4.1.2
  * [Overview](https://spark.apache.org/docs/latest/index.html)
  * [Programming Guides](https://spark.apache.org/docs/latest/sql-data-sources-load-save-functions.html)
[Quick Start](https://spark.apache.org/docs/latest/quick-start.html) [RDDs, Accumulators, Broadcasts Vars](https://spark.apache.org/docs/latest/rdd-programming-guide.html) [SQL, DataFrames, and Datasets](https://spark.apache.org/docs/latest/sql-programming-guide.html) [Structured Streaming](https://spark.apache.org/docs/latest/streaming/index.html) [Spark Streaming (DStreams)](https://spark.apache.org/docs/latest/streaming-programming-guide.html) [MLlib (Machine Learning)](https://spark.apache.org/docs/latest/ml-guide.html) [GraphX (Graph Processing)](https://spark.apache.org/docs/latest/graphx-programming-guide.html) [SparkR (R on Spark)](https://spark.apache.org/docs/latest/sparkr.html) [PySpark (Python on Spark)](https://spark.apache.org/docs/latest/api/python/getting_started/index.html) [Declarative Pipelines](https://spark.apache.org/docs/latest/declarative-pipelines-programming-guide.html)
  * [API Docs](https://spark.apache.org/docs/latest/sql-data-sources-load-save-functions.html)
[Python](https://spark.apache.org/docs/latest/api/python/index.html) [Scala](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html) [Java](https://spark.apache.org/docs/latest/api/java/index.html) [R](https://spark.apache.org/docs/latest/api/R/index.html) [SQL, Built-in Functions](https://spark.apache.org/docs/latest/api/sql/index.html)
  * [Deploying](https://spark.apache.org/docs/latest/sql-data-sources-load-save-functions.html)
[Overview](https://spark.apache.org/docs/latest/cluster-overview.html) [Submitting Applications](https://spark.apache.org/docs/latest/submitting-applications.html) [Spark Standalone](https://spark.apache.org/docs/latest/spark-standalone.html) [YARN](https://spark.apache.org/docs/latest/running-on-yarn.html) [Kubernetes](https://spark.apache.org/docs/latest/running-on-kubernetes.html)
  * [More](https://spark.apache.org/docs/latest/sql-data-sources-load-save-functions.html)
[Configuration](https://spark.apache.org/docs/latest/configuration.html) [Monitoring](https://spark.apache.org/docs/latest/monitoring.html) [Tuning Guide](https://spark.apache.org/docs/latest/tuning.html) [Job Scheduling](https://spark.apache.org/docs/latest/job-scheduling.html) [Security](https://spark.apache.org/docs/latest/security.html) [Hardware Provisioning](https://spark.apache.org/docs/latest/hardware-provisioning.html) [Migration Guide](https://spark.apache.org/docs/latest/migration-guide.html) [Building Spark](https://spark.apache.org/docs/latest/building-spark.html) [Contributing to Spark](https://spark.apache.org/contributing.html) [Third Party Projects](https://spark.apache.org/third-party-projects.html)
  * 

###  [Spark SQL Guide](https://spark.apache.org/docs/latest/sql-programming-guide.html)[](https://spark.apache.org/docs/latest/sql-data-sources-load-save-functions.html#spark-sql-guide)
  * [ Getting Started ](https://spark.apache.org/docs/latest/sql-getting-started.html)
  * [ Data Sources ](https://spark.apache.org/docs/latest/sql-data-sources.html)
    * [ Generic Load/Save Functions ](https://spark.apache.org/docs/latest/sql-data-sources-load-save-functions.html)
    * [ Generic File Source Options ](https://spark.apache.org/docs/latest/sql-data-sources-generic-options.html)
    * [ Parquet Files ](https://spark.apache.org/docs/latest/sql-data-sources-parquet.html)
    * [ ORC Files ](https://spark.apache.org/docs/latest/sql-data-sources-orc.html)
    * [ JSON Files ](https://spark.apache.org/docs/latest/sql-data-sources-json.html)
    * [ CSV Files ](https://spark.apache.org/docs/latest/sql-data-sources-csv.html)
    * [ Text Files ](https://spark.apache.org/docs/latest/sql-data-sources-text.html)
    * [ XML Files ](https://spark.apache.org/docs/latest/sql-data-sources-xml.html)
    * [ Hive Tables ](https://spark.apache.org/docs/latest/sql-data-sources-hive-tables.html)
    * [ JDBC To Other Databases ](https://spark.apache.org/docs/latest/sql-data-sources-jdbc.html)
    * [ Avro Files ](https://spark.apache.org/docs/latest/sql-data-sources-avro.html)
    * [ Protobuf data ](https://spark.apache.org/docs/latest/sql-data-sources-protobuf.html)
    * [ Whole Binary Files ](https://spark.apache.org/docs/latest/sql-data-sources-binaryFile.html)
    * [ Troubleshooting ](https://spark.apache.org/docs/latest/sql-data-sources-troubleshooting.html)
  * [ Performance Tuning ](https://spark.apache.org/docs/latest/sql-performance-tuning.html)
  * [ Distributed SQL Engine ](https://spark.apache.org/docs/latest/sql-distributed-sql-engine.html)
  * [ PySpark Usage Guide for Pandas with Apache Arrow ](https://spark.apache.org/docs/latest/sql-pyspark-pandas-with-arrow.html)
  * [ Migration Guide ](https://spark.apache.org/docs/latest/sql-migration-guide.html)
  * [ SQL Reference ](https://spark.apache.org/docs/latest/sql-ref.html)
  * [ Error Conditions ](https://spark.apache.org/docs/latest/sql-error-conditions.html)


# Generic Load/Save Functions[](https://spark.apache.org/docs/latest/sql-data-sources-load-save-functions.html#generic-loadsave-functions)
  * [Manually Specifying Options](https://spark.apache.org/docs/latest/sql-data-sources-load-save-functions.html#manually-specifying-options)
  * [Run SQL on files directly](https://spark.apache.org/docs/latest/sql-data-sources-load-save-functions.html#run-sql-on-files-directly)
  * [Save Modes](https://spark.apache.org/docs/latest/sql-data-sources-load-save-functions.html#save-modes)
  * [Saving to Persistent Tables](https://spark.apache.org/docs/latest/sql-data-sources-load-save-functions.html#saving-to-persistent-tables)
  * [Bucketing, Sorting and Partitioning](https://spark.apache.org/docs/latest/sql-data-sources-load-save-functions.html#bucketing-sorting-and-partitioning)


In the simplest form, the default data source (`parquet` unless otherwise configured by `spark.sql.sources.default`) will be used for all operations.
  * **Python**
  * **Scala**
  * **Java**
  * **R**



```
users_df = spark.read.load("examples/src/main/resources/users.parquet")
users_df.select("name", "favorite_color").write.save("namesAndFavColors.parquet")
```

Find full example code at "examples/src/main/python/sql/datasource.py" in the Spark repo.

```
val usersDF = spark.read.load("examples/src/main/resources/users.parquet")
usersDF.select("name", "favorite_color").write.save("namesAndFavColors.parquet")
```

Find full example code at "examples/src/main/scala/org/apache/spark/examples/sql/SQLDataSourceExample.scala" in the Spark repo.

```
Dataset<Row> usersDF = spark.read().load("examples/src/main/resources/users.parquet");
usersDF.select("name", "favorite_color").write().save("namesAndFavColors.parquet");
```

Find full example code at "examples/src/main/java/org/apache/spark/examples/sql/JavaSQLDataSourceExample.java" in the Spark repo.

```
df <- read.df("examples/src/main/resources/users.parquet")
write.df(select(df, "name", "favorite_color"), "namesAndFavColors.parquet")
```

Find full example code at "examples/src/main/r/RSparkSQLExample.R" in the Spark repo.
### Manually Specifying Options[](https://spark.apache.org/docs/latest/sql-data-sources-load-save-functions.html#manually-specifying-options)
You can also manually specify the data source that will be used along with any extra options that you would like to pass to the data source. Data sources are specified by their fully qualified name (i.e., `org.apache.spark.sql.parquet`), but for built-in sources you can also use their short names (`json`, `parquet`, `jdbc`, `orc`, `libsvm`, `csv`, `text`). DataFrames loaded from any data source type can be converted into other types using this syntax.
Please refer the API documentation for available options of built-in sources, for example, `org.apache.spark.sql.DataFrameReader` and `org.apache.spark.sql.DataFrameWriter`. The options documented there should be applicable through non-Scala Spark APIs (e.g. PySpark) as well. For other formats, refer to the API documentation of the particular format.
To load a JSON file you can use:
  * **Python**
  * **Scala**
  * **Java**
  * **R**



```
people_df = spark.read.load("examples/src/main/resources/people.json", format="json")
people_df.select("name", "age").write.save("namesAndAges.parquet", format="parquet")
```

Find full example code at "examples/src/main/python/sql/datasource.py" in the Spark repo.

```
val peopleDF = spark.read.format("json").load("examples/src/main/resources/people.json")
peopleDF.select("name", "age").write.format("parquet").save("namesAndAges.parquet")
```

Find full example code at "examples/src/main/scala/org/apache/spark/examples/sql/SQLDataSourceExample.scala" in the Spark repo.

```
Dataset<Row> peopleDF =
  spark.read().format("json").load("examples/src/main/resources/people.json");
peopleDF.select("name", "age").write().format("parquet").save("namesAndAges.parquet");
```

Find full example code at "examples/src/main/java/org/apache/spark/examples/sql/JavaSQLDataSourceExample.java" in the Spark repo.

```
df <- read.df("examples/src/main/resources/people.json", "json")
namesAndAges <- select(df, "name", "age")
write.df(namesAndAges, "namesAndAges.parquet", "parquet")
```

Find full example code at "examples/src/main/r/RSparkSQLExample.R" in the Spark repo.
To load a CSV file you can use:
  * **Python**
  * **Scala**
  * **Java**
  * **R**



```
people_df = spark.read.load(
    "examples/src/main/resources/people.csv",
    format="csv",
    sep=";",
    inferSchema="true",
    header="true"
)
```

Find full example code at "examples/src/main/python/sql/datasource.py" in the Spark repo.

```
val peopleDFCsv = spark.read.format("csv")
  .option("sep", ";")
  .option("inferSchema", "true")
  .option("header", "true")
  .load("examples/src/main/resources/people.csv")
```

Find full example code at "examples/src/main/scala/org/apache/spark/examples/sql/SQLDataSourceExample.scala" in the Spark repo.

```
Dataset<Row> peopleDFCsv = spark.read().format("csv")
  .option("sep", ";")
  .option("inferSchema", "true")
  .option("header", "true")
  .load("examples/src/main/resources/people.csv");
```

Find full example code at "examples/src/main/java/org/apache/spark/examples/sql/JavaSQLDataSourceExample.java" in the Spark repo.

```
df <- read.df("examples/src/main/resources/people.csv", "csv", sep = ";", inferSchema = TRUE, header = TRUE)
namesAndAges <- select(df, "name", "age")
```

Find full example code at "examples/src/main/r/RSparkSQLExample.R" in the Spark repo.
The extra options are also used during write operation. For example, you can control bloom filters and dictionary encodings for ORC data sources. The following ORC example will create bloom filter and use dictionary encoding only for `favorite_color`. For Parquet, there exists `parquet.bloom.filter.enabled` and `parquet.enable.dictionary`, too. To find more detailed information about the extra ORC/Parquet options, visit the official Apache [ORC](https://orc.apache.org/docs/spark-config.html) / [Parquet](https://github.com/apache/parquet-java/tree/master/parquet-hadoop) websites.
ORC data source:
  * **Python**
  * **Scala**
  * **Java**
  * **R**
  * **SQL**



```
users_df = spark.read.orc("examples/src/main/resources/users.orc")
(users_df.write.format("orc")
    .option("orc.bloom.filter.columns", "favorite_color")
    .option("orc.dictionary.key.threshold", "1.0")
    .option("orc.column.encoding.direct", "name")
    .save("users_with_options.orc"))
```

Find full example code at "examples/src/main/python/sql/datasource.py" in the Spark repo.

```
usersDF.write.format("orc")
  .option("orc.bloom.filter.columns", "favorite_color")
  .option("orc.dictionary.key.threshold", "1.0")
  .option("orc.column.encoding.direct", "name")
  .save("users_with_options.orc")
```

Find full example code at "examples/src/main/scala/org/apache/spark/examples/sql/SQLDataSourceExample.scala" in the Spark repo.

```
usersDF.write().format("orc")
  .option("orc.bloom.filter.columns", "favorite_color")
  .option("orc.dictionary.key.threshold", "1.0")
  .option("orc.column.encoding.direct", "name")
  .save("users_with_options.orc");
```

Find full example code at "examples/src/main/java/org/apache/spark/examples/sql/JavaSQLDataSourceExample.java" in the Spark repo.

```
df <- read.df("examples/src/main/resources/users.orc", "orc")
write.orc(df, "users_with_options.orc", orc.bloom.filter.columns = "favorite_color", orc.dictionary.key.threshold = 1.0, orc.column.encoding.direct = "name")
```

Find full example code at "examples/src/main/r/RSparkSQLExample.R" in the Spark repo.

```
CREATE TABLE users_with_options (
  name STRING,
  favorite_color STRING,
  favorite_numbers array<integer>
) USING ORC
OPTIONS (
  orc.bloom.filter.columns 'favorite_color',
  orc.dictionary.key.threshold '1.0',
  orc.column.encoding.direct 'name'
)
```

Parquet data source:
  * **Python**
  * **Scala**
  * **Java**
  * **R**
  * **SQL**



```
users_df = spark.read.parquet("examples/src/main/resources/users.parquet")
(users_df.write.format("parquet")
    .option("parquet.bloom.filter.enabled#favorite_color", "true")
    .option("parquet.bloom.filter.expected.ndv#favorite_color", "1000000")
    .option("parquet.enable.dictionary", "true")
    .option("parquet.page.write-checksum.enabled", "false")
    .save("users_with_options.parquet"))
```

Find full example code at "examples/src/main/python/sql/datasource.py" in the Spark repo.

```
usersDF.write.format("parquet")
  .option("parquet.bloom.filter.enabled#favorite_color", "true")
  .option("parquet.bloom.filter.expected.ndv#favorite_color", "1000000")
  .option("parquet.enable.dictionary", "true")
  .option("parquet.page.write-checksum.enabled", "false")
  .save("users_with_options.parquet")
```

Find full example code at "examples/src/main/scala/org/apache/spark/examples/sql/SQLDataSourceExample.scala" in the Spark repo.

```
usersDF.write().format("parquet")
    .option("parquet.bloom.filter.enabled#favorite_color", "true")
    .option("parquet.bloom.filter.expected.ndv#favorite_color", "1000000")
    .option("parquet.enable.dictionary", "true")
    .option("parquet.page.write-checksum.enabled", "false")
    .save("users_with_options.parquet");
```

Find full example code at "examples/src/main/java/org/apache/spark/examples/sql/JavaSQLDataSourceExample.java" in the Spark repo.

```
df <- read.df("examples/src/main/resources/users.parquet", "parquet")
write.parquet(df, "users_with_options.parquet", parquet.bloom.filter.enabled#favorite_color = true, parquet.bloom.filter.expected.ndv#favorite_color = 1000000, parquet.enable.dictionary = true, parquet.page.write-checksum.enabled = false)
```

Find full example code at "examples/src/main/r/RSparkSQLExample.R" in the Spark repo.

```
CREATE TABLE users_with_options (
  name STRING,
  favorite_color STRING,
  favorite_numbers array<integer>
) USING parquet
OPTIONS (
  `parquet.bloom.filter.enabled#favorite_color` true,
  `parquet.bloom.filter.expected.ndv#favorite_color` 1000000,
  parquet.enable.dictionary true,
  parquet.page.write-checksum.enabled true
)
```

### Run SQL on files directly[](https://spark.apache.org/docs/latest/sql-data-sources-load-save-functions.html#run-sql-on-files-directly)
Instead of using read API to load a file into DataFrame and query it, you can also query that file directly with SQL.
  * **Python**
  * **Scala**
  * **Java**
  * **R**
  * **SQL**



```
df = spark.sql("SELECT * FROM parquet.`examples/src/main/resources/users.parquet`")
```

Find full example code at "examples/src/main/python/sql/datasource.py" in the Spark repo.

```
val sqlDF = spark.sql("SELECT * FROM parquet.`examples/src/main/resources/users.parquet`")
```

Find full example code at "examples/src/main/scala/org/apache/spark/examples/sql/SQLDataSourceExample.scala" in the Spark repo.

```
Dataset<Row> sqlDF =
  spark.sql("SELECT * FROM parquet.`examples/src/main/resources/users.parquet`");
```

Find full example code at "examples/src/main/java/org/apache/spark/examples/sql/JavaSQLDataSourceExample.java" in the Spark repo.

```
df <- sql("SELECT * FROM parquet.`examples/src/main/resources/users.parquet`")
```

Find full example code at "examples/src/main/r/RSparkSQLExample.R" in the Spark repo.

```
SELECT * FROM parquet.`examples/src/main/resources/users.parquet`
```

### Save Modes[](https://spark.apache.org/docs/latest/sql-data-sources-load-save-functions.html#save-modes)
Save operations can optionally take a `SaveMode`, that specifies how to handle existing data if present. It is important to realize that these save modes do not utilize any locking and are not atomic. Additionally, when performing an `Overwrite`, the data will be deleted before writing out the new data.  
| Scala/Java  | Any Language  | Meaning  |  
| --- | --- | --- |  
|  `SaveMode.ErrorIfExists` (default)  |  `"error" or "errorifexists"` (default)  |  When saving a DataFrame to a data source, if data already exists, an exception is expected to be thrown.   |  
| `SaveMode.Append`  | `"append"`  |  When saving a DataFrame to a data source, if data/table already exists, contents of the DataFrame are expected to be appended to existing data.   |  
| `SaveMode.Overwrite`  | `"overwrite"`  |  Overwrite mode means that when saving a DataFrame to a data source, if data/table already exists, existing data is expected to be overwritten by the contents of the DataFrame.   |  
| `SaveMode.Ignore`  | `"ignore"`  |  Ignore mode means that when saving a DataFrame to a data source, if data already exists, the save operation is expected not to save the contents of the DataFrame and not to change the existing data. This is similar to a `CREATE TABLE IF NOT EXISTS` in SQL.   |  
### Saving to Persistent Tables[](https://spark.apache.org/docs/latest/sql-data-sources-load-save-functions.html#saving-to-persistent-tables)
`DataFrames` can also be saved as persistent tables into Hive metastore using the `saveAsTable` command. Notice that an existing Hive deployment is not necessary to use this feature. Spark will create a default local Hive metastore (using Derby) for you. Unlike the `createOrReplaceTempView` command, `saveAsTable` will materialize the contents of the DataFrame and create a pointer to the data in the Hive metastore. Persistent tables will still exist even after your Spark program has restarted, as long as you maintain your connection to the same metastore. A DataFrame for a persistent table can be created by calling the `table` method on a `SparkSession` with the name of the table.
For file-based data source, e.g. text, parquet, json, etc. you can specify a custom table path via the `path` option, e.g. `df.write.option("path", "/some/path").saveAsTable("t")`. When the table is dropped, the custom table path will not be removed and the table data is still there. If no custom table path is specified, Spark will write data to a default table path under the warehouse directory. When the table is dropped, the default table path will be removed too.
Starting from Spark 2.1, persistent datasource tables have per-partition metadata stored in the Hive metastore. This brings several benefits:
  * Since the metastore can return only necessary partitions for a query, discovering all the partitions on the first query to the table is no longer needed.
  * Hive DDLs such as `ALTER TABLE PARTITION ... SET LOCATION` are now available for tables created with the Datasource API.


Note that partition information is not gathered by default when creating external datasource tables (those with a `path` option). To sync the partition information in the metastore, you can invoke `MSCK REPAIR TABLE`.
### Bucketing, Sorting and Partitioning[](https://spark.apache.org/docs/latest/sql-data-sources-load-save-functions.html#bucketing-sorting-and-partitioning)
For file-based data source, it is also possible to bucket and sort or partition the output. Bucketing and sorting are applicable only to persistent tables:
  * **Python**
  * **Scala**
  * **Java**
  * **SQL**



```
people_df = spark.read.json("examples/src/main/resources/people.json")
people_df.write.bucketBy(42, "name").sortBy("age").saveAsTable("people_bucketed")
```

Find full example code at "examples/src/main/python/sql/datasource.py" in the Spark repo.

```
peopleDF.write.bucketBy(42, "name").sortBy("age").saveAsTable("people_bucketed")
```

Find full example code at "examples/src/main/scala/org/apache/spark/examples/sql/SQLDataSourceExample.scala" in the Spark repo.

```
peopleDF.write().bucketBy(42, "name").sortBy("age").saveAsTable("people_bucketed");
```

Find full example code at "examples/src/main/java/org/apache/spark/examples/sql/JavaSQLDataSourceExample.java" in the Spark repo.

```
CREATE TABLE people_bucketed
USING json
CLUSTERED BY(name) INTO 42 BUCKETS
AS SELECT * FROM json.`examples/src/main/resources/people.json`;
```

while partitioning can be used with both `save` and `saveAsTable` when using the Dataset APIs.
  * **Python**
  * **Scala**
  * **Java**
  * **SQL**



```
users_df = spark.read.load("examples/src/main/resources/users.parquet")
users_df.write.partitionBy("favorite_color").format("parquet").save("namesPartByColor.parquet")
```

Find full example code at "examples/src/main/python/sql/datasource.py" in the Spark repo.

```
usersDF.write.partitionBy("favorite_color").format("parquet").save("namesPartByColor.parquet")
```

Find full example code at "examples/src/main/scala/org/apache/spark/examples/sql/SQLDataSourceExample.scala" in the Spark repo.

```
usersDF
  .write()
  .partitionBy("favorite_color")
  .format("parquet")
  .save("namesPartByColor.parquet");
```

Find full example code at "examples/src/main/java/org/apache/spark/examples/sql/JavaSQLDataSourceExample.java" in the Spark repo.

```
CREATE TABLE users_by_favorite_color
USING parquet
PARTITIONED BY(favorite_color)
AS SELECT * FROM parquet.`examples/src/main/resources/users.parquet`;
```

It is possible to use both partitioning and bucketing for a single table:
  * **Python**
  * **Scala**
  * **Java**
  * **SQL**



```
users_df = spark.read.parquet("examples/src/main/resources/users.parquet")
(users_df.write
    .partitionBy("favorite_color")
    .bucketBy(42, "name")
    .saveAsTable("users_partitioned_bucketed"))
```

Find full example code at "examples/src/main/python/sql/datasource.py" in the Spark repo.

```
usersDF
  .write
  .partitionBy("favorite_color")
  .bucketBy(42, "name")
  .saveAsTable("users_partitioned_bucketed")
```

Find full example code at "examples/src/main/scala/org/apache/spark/examples/sql/SQLDataSourceExample.scala" in the Spark repo.

```
usersDF
  .write()
  .partitionBy("favorite_color")
  .bucketBy(42, "name")
  .saveAsTable("users_partitioned_bucketed");
```

Find full example code at "examples/src/main/java/org/apache/spark/examples/sql/JavaSQLDataSourceExample.java" in the Spark repo.

```
CREATE TABLE users_partitioned_bucketed
USING parquet
PARTITIONED BY (favorite_color)
CLUSTERED BY(name) SORTED BY (favorite_numbers) INTO 42 BUCKETS
AS SELECT * FROM parquet.`examples/src/main/resources/users.parquet`;
```

`partitionBy` creates a directory structure as described in the [Partition Discovery](https://spark.apache.org/docs/latest/sql-data-sources-parquet.html#partition-discovery) section. Thus, it has limited applicability to columns with high cardinality. In contrast `bucketBy` distributes data across a fixed number of buckets and can be used when the number of unique values is unbounded.
