[ ![](https://spark.apache.org/images/spark-logo-rev.svg)](https://spark.apache.org/docs/latest/index.html)4.1.2
  * [Overview](https://spark.apache.org/docs/latest/index.html)
  * [Programming Guides](https://spark.apache.org/docs/latest/sql-data-sources-hive-tables.html)
[Quick Start](https://spark.apache.org/docs/latest/quick-start.html) [RDDs, Accumulators, Broadcasts Vars](https://spark.apache.org/docs/latest/rdd-programming-guide.html) [SQL, DataFrames, and Datasets](https://spark.apache.org/docs/latest/sql-programming-guide.html) [Structured Streaming](https://spark.apache.org/docs/latest/streaming/index.html) [Spark Streaming (DStreams)](https://spark.apache.org/docs/latest/streaming-programming-guide.html) [MLlib (Machine Learning)](https://spark.apache.org/docs/latest/ml-guide.html) [GraphX (Graph Processing)](https://spark.apache.org/docs/latest/graphx-programming-guide.html) [SparkR (R on Spark)](https://spark.apache.org/docs/latest/sparkr.html) [PySpark (Python on Spark)](https://spark.apache.org/docs/latest/api/python/getting_started/index.html) [Declarative Pipelines](https://spark.apache.org/docs/latest/declarative-pipelines-programming-guide.html)
  * [API Docs](https://spark.apache.org/docs/latest/sql-data-sources-hive-tables.html)
[Python](https://spark.apache.org/docs/latest/api/python/index.html) [Scala](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html) [Java](https://spark.apache.org/docs/latest/api/java/index.html) [R](https://spark.apache.org/docs/latest/api/R/index.html) [SQL, Built-in Functions](https://spark.apache.org/docs/latest/api/sql/index.html)
  * [Deploying](https://spark.apache.org/docs/latest/sql-data-sources-hive-tables.html)
[Overview](https://spark.apache.org/docs/latest/cluster-overview.html) [Submitting Applications](https://spark.apache.org/docs/latest/submitting-applications.html) [Spark Standalone](https://spark.apache.org/docs/latest/spark-standalone.html) [YARN](https://spark.apache.org/docs/latest/running-on-yarn.html) [Kubernetes](https://spark.apache.org/docs/latest/running-on-kubernetes.html)
  * [More](https://spark.apache.org/docs/latest/sql-data-sources-hive-tables.html)
[Configuration](https://spark.apache.org/docs/latest/configuration.html) [Monitoring](https://spark.apache.org/docs/latest/monitoring.html) [Tuning Guide](https://spark.apache.org/docs/latest/tuning.html) [Job Scheduling](https://spark.apache.org/docs/latest/job-scheduling.html) [Security](https://spark.apache.org/docs/latest/security.html) [Hardware Provisioning](https://spark.apache.org/docs/latest/hardware-provisioning.html) [Migration Guide](https://spark.apache.org/docs/latest/migration-guide.html) [Building Spark](https://spark.apache.org/docs/latest/building-spark.html) [Contributing to Spark](https://spark.apache.org/contributing.html) [Third Party Projects](https://spark.apache.org/third-party-projects.html)
  * 

###  [Spark SQL Guide](https://spark.apache.org/docs/latest/sql-programming-guide.html)[](https://spark.apache.org/docs/latest/sql-data-sources-hive-tables.html#spark-sql-guide)
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


# Hive Tables[](https://spark.apache.org/docs/latest/sql-data-sources-hive-tables.html#hive-tables)
  * [Specifying storage format for Hive tables](https://spark.apache.org/docs/latest/sql-data-sources-hive-tables.html#specifying-storage-format-for-hive-tables)
  * [Interacting with Different Versions of Hive Metastore](https://spark.apache.org/docs/latest/sql-data-sources-hive-tables.html#interacting-with-different-versions-of-hive-metastore)


Spark SQL also supports reading and writing data stored in [Apache Hive](http://hive.apache.org/). However, since Hive has a large number of dependencies, these dependencies are not included in the default Spark distribution. If Hive dependencies can be found on the classpath, Spark will load them automatically. Note that these Hive dependencies must also be present on all of the worker nodes, as they will need access to the Hive serialization and deserialization libraries (SerDes) in order to access data stored in Hive.
Configuration of Hive is done by placing your `hive-site.xml`, `core-site.xml` (for security configuration), and `hdfs-site.xml` (for HDFS configuration) file in `conf/`.
When working with Hive, one must instantiate `SparkSession` with Hive support, including connectivity to a persistent Hive metastore, support for Hive serdes, and Hive user-defined functions. Users who do not have an existing Hive deployment can still enable Hive support. When not configured by the `hive-site.xml`, the context automatically creates `metastore_db` in the current directory and creates a directory configured by `spark.sql.warehouse.dir`, which defaults to the directory `spark-warehouse` in the current directory that the Spark application is started. Note that the `hive.metastore.warehouse.dir` property in `hive-site.xml` is deprecated since Spark 2.0.0. Instead, use `spark.sql.warehouse.dir` to specify the default location of database in warehouse. You may need to grant write privilege to the user who starts the Spark application.
  * **Python**
  * **Scala**
  * **Java**
  * **R**



```
from os.path import abspath

from pyspark.sql import SparkSession
from pyspark.sql import Row

# warehouse_location points to the default location for managed databases and tables
warehouse_location = abspath('spark-warehouse')

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL Hive integration example") \
    .config("spark.sql.warehouse.dir", warehouse_location) \
    .enableHiveSupport() \
    .getOrCreate()

# spark is an existing SparkSession
spark.sql("CREATE TABLE IF NOT EXISTS src (key INT, value STRING) USING hive")
spark.sql("LOAD DATA LOCAL INPATH 'examples/src/main/resources/kv1.txt' INTO TABLE src")

# Queries are expressed in HiveQL
spark.sql("SELECT * FROM src").show()
# +---+-------+
# |key|  value|
# +---+-------+
# |238|val_238|
# | 86| val_86|
# |311|val_311|
# ...

# Aggregation queries are also supported.
spark.sql("SELECT COUNT(*) FROM src").show()
# +--------+
# |count(1)|
# +--------+
# |    500 |
# +--------+

# The results of SQL queries are themselves DataFrames and support all normal functions.
sqlDF = spark.sql("SELECT key, value FROM src WHERE key < 10 ORDER BY key")

# The items in DataFrames are of type Row, which allows you to access each column by ordinal.
stringsDS = sqlDF.rdd.map(lambda row: "Key: %d, Value: %s" % (row.key, row.value))
for record in stringsDS.collect():
    print(record)
# Key: 0, Value: val_0
# Key: 0, Value: val_0
# Key: 0, Value: val_0
# ...

# You can also use DataFrames to create temporary views within a SparkSession.
Record = Row("key", "value")
recordsDF = spark.createDataFrame([Record(i, "val_" + str(i)) for i in range(1, 101)])
recordsDF.createOrReplaceTempView("records")

# Queries can then join DataFrame data with data stored in Hive.
spark.sql("SELECT * FROM records r JOIN src s ON r.key = s.key").show()
# +---+------+---+------+
# |key| value|key| value|
# +---+------+---+------+
# |  2| val_2|  2| val_2|
# |  4| val_4|  4| val_4|
# |  5| val_5|  5| val_5|
# ...
```

Find full example code at "examples/src/main/python/sql/hive.py" in the Spark repo.

```
import java.io.File

import org.apache.spark.sql.{Row, SaveMode, SparkSession}

case class Record(key: Int, value: String)

// warehouseLocation points to the default location for managed databases and tables
val warehouseLocation = new File("spark-warehouse").getAbsolutePath

val spark = SparkSession
  .builder()
  .appName("Spark Hive Example")
  .config("spark.sql.warehouse.dir", warehouseLocation)
  .enableHiveSupport()
  .getOrCreate()

import spark.implicits._
import spark.sql

sql("CREATE TABLE IF NOT EXISTS src (key INT, value STRING) USING hive")
sql("LOAD DATA LOCAL INPATH 'examples/src/main/resources/kv1.txt' INTO TABLE src")

// Queries are expressed in HiveQL
sql("SELECT * FROM src").show()
// +---+-------+
// |key|  value|
// +---+-------+
// |238|val_238|
// | 86| val_86|
// |311|val_311|
// ...

// Aggregation queries are also supported.
sql("SELECT COUNT(*) FROM src").show()
// +--------+
// |count(1)|
// +--------+
// |    500 |
// +--------+

// The results of SQL queries are themselves DataFrames and support all normal functions.
val sqlDF = sql("SELECT key, value FROM src WHERE key < 10 ORDER BY key")

// The items in DataFrames are of type Row, which allows you to access each column by ordinal.
val stringsDS = sqlDF.map {
  case Row(key: Int, value: String) => s"Key: $key, Value: $value"
}
stringsDS.show()
// +--------------------+
// |               value|
// +--------------------+
// |Key: 0, Value: val_0|
// |Key: 0, Value: val_0|
// |Key: 0, Value: val_0|
// ...

// You can also use DataFrames to create temporary views within a SparkSession.
val recordsDF = spark.createDataFrame((1 to 100).map(i => Record(i, s"val_$i")))
recordsDF.createOrReplaceTempView("records")

// Queries can then join DataFrame data with data stored in Hive.
sql("SELECT * FROM records r JOIN src s ON r.key = s.key").show()
// +---+------+---+------+
// |key| value|key| value|
// +---+------+---+------+
// |  2| val_2|  2| val_2|
// |  4| val_4|  4| val_4|
// |  5| val_5|  5| val_5|
// ...

// Create a Hive managed Parquet table, with HQL syntax instead of the Spark SQL native syntax
// `USING hive`
sql("CREATE TABLE hive_records(key int, value string) STORED AS PARQUET")
// Save DataFrame to the Hive managed table
val df = spark.table("src")
df.write.mode(SaveMode.Overwrite).saveAsTable("hive_records")
// After insertion, the Hive managed table has data now
sql("SELECT * FROM hive_records").show()
// +---+-------+
// |key|  value|
// +---+-------+
// |238|val_238|
// | 86| val_86|
// |311|val_311|
// ...

// Prepare a Parquet data directory
val dataDir = "/tmp/parquet_data"
spark.range(10).write.parquet(dataDir)
// Create a Hive external Parquet table
sql(s"CREATE EXTERNAL TABLE hive_bigints(id bigint) STORED AS PARQUET LOCATION '$dataDir'")
// The Hive external table should already have data
sql("SELECT * FROM hive_bigints").show()
// +---+
// | id|
// +---+
// |  0|
// |  1|
// |  2|
// ... Order may vary, as spark processes the partitions in parallel.

// Turn on flag for Hive Dynamic Partitioning
spark.conf.set("hive.exec.dynamic.partition", "true")
spark.conf.set("hive.exec.dynamic.partition.mode", "nonstrict")
// Create a Hive partitioned table using DataFrame API
df.write.partitionBy("key").format("hive").saveAsTable("hive_part_tbl")
// Partitioned column `key` will be moved to the end of the schema.
sql("SELECT * FROM hive_part_tbl").show()
// +-------+---+
// |  value|key|
// +-------+---+
// |val_238|238|
// | val_86| 86|
// |val_311|311|
// ...

spark.stop()
```

Find full example code at "examples/src/main/scala/org/apache/spark/examples/sql/hive/SparkHiveExample.scala" in the Spark repo.

```
import java.io.File;
import java.io.Serializable;
import java.util.ArrayList;
import java.util.List;

import org.apache.spark.api.java.function.MapFunction;
import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Encoders;
import org.apache.spark.sql.Row;
import org.apache.spark.sql.SparkSession;

public static class Record implements Serializable {
  private int key;
  private String value;

  public int getKey() {
    return key;
  }

  public void setKey(int key) {
    this.key = key;
  }

  public String getValue() {
    return value;
  }

  public void setValue(String value) {
    this.value = value;
  }
}

// warehouseLocation points to the default location for managed databases and tables
String warehouseLocation = new File("spark-warehouse").getAbsolutePath();
SparkSession spark = SparkSession
  .builder()
  .appName("Java Spark Hive Example")
  .config("spark.sql.warehouse.dir", warehouseLocation)
  .enableHiveSupport()
  .getOrCreate();

spark.sql("CREATE TABLE IF NOT EXISTS src (key INT, value STRING) USING hive");
spark.sql("LOAD DATA LOCAL INPATH 'examples/src/main/resources/kv1.txt' INTO TABLE src");

// Queries are expressed in HiveQL
spark.sql("SELECT * FROM src").show();
// +---+-------+
// |key|  value|
// +---+-------+
// |238|val_238|
// | 86| val_86|
// |311|val_311|
// ...

// Aggregation queries are also supported.
spark.sql("SELECT COUNT(*) FROM src").show();
// +--------+
// |count(1)|
// +--------+
// |    500 |
// +--------+

// The results of SQL queries are themselves DataFrames and support all normal functions.
Dataset<Row> sqlDF = spark.sql("SELECT key, value FROM src WHERE key < 10 ORDER BY key");

// The items in DataFrames are of type Row, which lets you to access each column by ordinal.
Dataset<String> stringsDS = sqlDF.map(
    (MapFunction<Row, String>) row -> "Key: " + row.get(0) + ", Value: " + row.get(1),
    Encoders.STRING());
stringsDS.show();
// +--------------------+
// |               value|
// +--------------------+
// |Key: 0, Value: val_0|
// |Key: 0, Value: val_0|
// |Key: 0, Value: val_0|
// ...

// You can also use DataFrames to create temporary views within a SparkSession.
List<Record> records = new ArrayList<>();
for (int key = 1; key < 100; key++) {
  Record record = new Record();
  record.setKey(key);
  record.setValue("val_" + key);
  records.add(record);
}
Dataset<Row> recordsDF = spark.createDataFrame(records, Record.class);
recordsDF.createOrReplaceTempView("records");

// Queries can then join DataFrames data with data stored in Hive.
spark.sql("SELECT * FROM records r JOIN src s ON r.key = s.key").show();
// +---+------+---+------+
// |key| value|key| value|
// +---+------+---+------+
// |  2| val_2|  2| val_2|
// |  2| val_2|  2| val_2|
// |  4| val_4|  4| val_4|
// ...
```

Find full example code at "examples/src/main/java/org/apache/spark/examples/sql/hive/JavaSparkHiveExample.java" in the Spark repo.
When working with Hive one must instantiate `SparkSession` with Hive support. This adds support for finding tables in the MetaStore and writing queries using HiveQL.

```
# enableHiveSupport defaults to TRUE
sparkR.session(enableHiveSupport = TRUE)
sql("CREATE TABLE IF NOT EXISTS src (key INT, value STRING) USING hive")
sql("LOAD DATA LOCAL INPATH 'examples/src/main/resources/kv1.txt' INTO TABLE src")

# Queries can be expressed in HiveQL.
results <- collect(sql("FROM src SELECT key, value"))
```

Find full example code at "examples/src/main/r/RSparkSQLExample.R" in the Spark repo.
### Specifying storage format for Hive tables[](https://spark.apache.org/docs/latest/sql-data-sources-hive-tables.html#specifying-storage-format-for-hive-tables)
When you create a Hive table, you need to define how this table should read/write data from/to file system, i.e. the “input format” and “output format”. You also need to define how this table should deserialize the data to rows, or serialize rows to data, i.e. the “serde”. The following options can be used to specify the storage format(“serde”, “input format”, “output format”), e.g. `CREATE TABLE src(id int) USING hive OPTIONS(fileFormat 'parquet')`. By default, we will read the table files as plain text. Note that, Hive storage handler is not supported yet when creating table, you can create a table using storage handler at Hive side, and use Spark SQL to read it.  
| Property Name  | Meaning  |  
| --- | --- |  
| `fileFormat`  |  A fileFormat is kind of a package of storage format specifications, including "serde", "input format" and "output format". Currently we support 6 fileFormats: 'sequencefile', 'rcfile', 'orc', 'parquet', 'textfile' and 'avro'.   |  
| `inputFormat, outputFormat`  |  These 2 options specify the name of a corresponding `InputFormat` and `OutputFormat` class as a string literal, e.g. `org.apache.hadoop.hive.ql.io.orc.OrcInputFormat`. These 2 options must be appeared in a pair, and you can not specify them if you already specified the `fileFormat` option.   |  
| `serde`  |  This option specifies the name of a serde class. When the `fileFormat` option is specified, do not specify this option if the given `fileFormat` already include the information of serde. Currently "sequencefile", "textfile" and "rcfile" don't include the serde information and you can use this option with these 3 fileFormats.   |  
| `fieldDelim, escapeDelim, collectionDelim, mapkeyDelim, lineDelim`  |  These options can only be used with "textfile" fileFormat. They define how to read delimited files into rows.   |  
All other properties defined with `OPTIONS` will be regarded as Hive serde properties.
### Interacting with Different Versions of Hive Metastore[](https://spark.apache.org/docs/latest/sql-data-sources-hive-tables.html#interacting-with-different-versions-of-hive-metastore)
One of the most important pieces of Spark SQL’s Hive support is interaction with Hive metastore, which enables Spark SQL to access metadata of Hive tables. Starting from Spark 1.4.0, a single binary build of Spark SQL can be used to query different versions of Hive metastores, using the configuration described below. Note that independent of the version of Hive that is being used to talk to the metastore, internally Spark SQL will compile against built-in Hive and use those classes for internal execution (serdes, UDFs, UDAFs, etc).
The following options can be used to configure the version of Hive that is used to retrieve metadata:  
| Property Name  | Default  | Meaning  | Since Version  |  
| --- | --- | --- | --- |  
| `spark.sql.hive.metastore.version`  | `2.3.10`  |  Version of the Hive metastore. Available options are `2.0.0` through `2.3.10`, `3.0.0` through `3.1.3`, and `4.0.0` through `4.1.0`.   | 1.4.0  |  
| `spark.sql.hive.metastore.jars`  | `builtin`  |  Location of the jars that should be used to instantiate the HiveMetastoreClient. This property can be one of four options: 
  1. `builtin`
Use Hive 2.3.10, which is bundled with the Spark assembly when `-Phive` is enabled. When this option is chosen, `spark.sql.hive.metastore.version` must be either `2.3.10` or not defined. 
  2. `maven`
Use Hive jars of specified version downloaded from Maven repositories. This configuration is not generally recommended for production deployments. 
  3. `path`
Use Hive jars configured by `spark.sql.hive.metastore.jars.path` in comma separated format. Support both local or remote paths. The provided jars should be the same version as `spark.sql.hive.metastore.version`. 
  4. A classpath in the standard format for the JVM. This classpath must include all of Hive and its dependencies, including the correct version of Hadoop. The provided jars should be the same version as `spark.sql.hive.metastore.version`. These jars only need to be present on the driver, but if you are running in yarn cluster mode then you must ensure they are packaged with your application.

 | 1.4.0  |  
| `spark.sql.hive.metastore.jars.path`  | `(empty)`  |  Comma-separated paths of the jars that used to instantiate the HiveMetastoreClient. This configuration is useful only when `spark.sql.hive.metastore.jars` is set as `path`.   
The paths can be any of the following format: 
  1. `file://path/to/jar/foo.jar`
  2. `hdfs://nameservice/path/to/jar/foo.jar`
  3. `/path/to/jar/`(path without URI scheme follow conf `fs.defaultFS`'s URI schema)
  4. `[http/https/ftp]://path/to/jar/foo.jar`

Note that 1, 2, and 3 support wildcard. For example: 
  1. `file://path/to/jar/*,file://path2/to/jar/*/*.jar`
  2. `hdfs://nameservice/path/to/jar/*,hdfs://nameservice2/path/to/jar/*/*.jar`

 | 3.1.0  |  
| `spark.sql.hive.metastore.sharedPrefixes`  | `com.mysql.jdbc,  
org.postgresql,  
com.microsoft.sqlserver,  
oracle.jdbc`  |  A comma-separated list of class prefixes that should be loaded using the classloader that is shared between Spark SQL and a specific version of Hive. An example of classes that should be shared is JDBC drivers that are needed to talk to the metastore. Other classes that need to be shared are those that interact with classes that are already shared. For example, custom appenders that are used by log4j.   | 1.4.0  |  
| `spark.sql.hive.metastore.barrierPrefixes`  | `(empty)`  |  A comma separated list of class prefixes that should explicitly be reloaded for each version of Hive that Spark SQL is communicating with. For example, Hive UDFs that are declared in a prefix that typically would be shared (i.e. `org.apache.spark.*`).   | 1.4.0  |
