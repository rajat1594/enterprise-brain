[ ![](https://spark.apache.org/images/spark-logo-rev.svg)](https://spark.apache.org/docs/latest/index.html)4.1.2
  * [Overview](https://spark.apache.org/docs/latest/index.html)
  * [Programming Guides](https://spark.apache.org/docs/latest/sparkr-migration-guide.html)
[Quick Start](https://spark.apache.org/docs/latest/quick-start.html) [RDDs, Accumulators, Broadcasts Vars](https://spark.apache.org/docs/latest/rdd-programming-guide.html) [SQL, DataFrames, and Datasets](https://spark.apache.org/docs/latest/sql-programming-guide.html) [Structured Streaming](https://spark.apache.org/docs/latest/streaming/index.html) [Spark Streaming (DStreams)](https://spark.apache.org/docs/latest/streaming-programming-guide.html) [MLlib (Machine Learning)](https://spark.apache.org/docs/latest/ml-guide.html) [GraphX (Graph Processing)](https://spark.apache.org/docs/latest/graphx-programming-guide.html) [SparkR (R on Spark)](https://spark.apache.org/docs/latest/sparkr.html) [PySpark (Python on Spark)](https://spark.apache.org/docs/latest/api/python/getting_started/index.html) [Declarative Pipelines](https://spark.apache.org/docs/latest/declarative-pipelines-programming-guide.html)
  * [API Docs](https://spark.apache.org/docs/latest/sparkr-migration-guide.html)
[Python](https://spark.apache.org/docs/latest/api/python/index.html) [Scala](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html) [Java](https://spark.apache.org/docs/latest/api/java/index.html) [R](https://spark.apache.org/docs/latest/api/R/index.html) [SQL, Built-in Functions](https://spark.apache.org/docs/latest/api/sql/index.html)
  * [Deploying](https://spark.apache.org/docs/latest/sparkr-migration-guide.html)
[Overview](https://spark.apache.org/docs/latest/cluster-overview.html) [Submitting Applications](https://spark.apache.org/docs/latest/submitting-applications.html) [Spark Standalone](https://spark.apache.org/docs/latest/spark-standalone.html) [YARN](https://spark.apache.org/docs/latest/running-on-yarn.html) [Kubernetes](https://spark.apache.org/docs/latest/running-on-kubernetes.html)
  * [More](https://spark.apache.org/docs/latest/sparkr-migration-guide.html)
[Configuration](https://spark.apache.org/docs/latest/configuration.html) [Monitoring](https://spark.apache.org/docs/latest/monitoring.html) [Tuning Guide](https://spark.apache.org/docs/latest/tuning.html) [Job Scheduling](https://spark.apache.org/docs/latest/job-scheduling.html) [Security](https://spark.apache.org/docs/latest/security.html) [Hardware Provisioning](https://spark.apache.org/docs/latest/hardware-provisioning.html) [Migration Guide](https://spark.apache.org/docs/latest/migration-guide.html) [Building Spark](https://spark.apache.org/docs/latest/building-spark.html) [Contributing to Spark](https://spark.apache.org/contributing.html) [Third Party Projects](https://spark.apache.org/third-party-projects.html)
  *

# Migration Guide: SparkR (R on Spark)[](https://spark.apache.org/docs/latest/sparkr-migration-guide.html#migration-guide-sparkr-r-on-spark)
  * [Upgrading from SparkR 3.5 to 4.0](https://spark.apache.org/docs/latest/sparkr-migration-guide.html#upgrading-from-sparkr-35-to-40)
  * [Upgrading from SparkR 3.1 to 3.2](https://spark.apache.org/docs/latest/sparkr-migration-guide.html#upgrading-from-sparkr-31-to-32)
  * [Upgrading from SparkR 2.4 to 3.0](https://spark.apache.org/docs/latest/sparkr-migration-guide.html#upgrading-from-sparkr-24-to-30)
  * [Upgrading from SparkR 2.3 to 2.4](https://spark.apache.org/docs/latest/sparkr-migration-guide.html#upgrading-from-sparkr-23-to-24)
  * [Upgrading from SparkR 2.3 to 2.3.1 and above](https://spark.apache.org/docs/latest/sparkr-migration-guide.html#upgrading-from-sparkr-23-to-231-and-above)
  * [Upgrading from SparkR 2.2 to 2.3](https://spark.apache.org/docs/latest/sparkr-migration-guide.html#upgrading-from-sparkr-22-to-23)
  * [Upgrading from SparkR 2.1 to 2.2](https://spark.apache.org/docs/latest/sparkr-migration-guide.html#upgrading-from-sparkr-21-to-22)
  * [Upgrading from SparkR 2.0 to 3.1](https://spark.apache.org/docs/latest/sparkr-migration-guide.html#upgrading-from-sparkr-20-to-31)
  * [Upgrading from SparkR 1.6 to 2.0](https://spark.apache.org/docs/latest/sparkr-migration-guide.html#upgrading-from-sparkr-16-to-20)
  * [Upgrading from SparkR 1.5 to 1.6](https://spark.apache.org/docs/latest/sparkr-migration-guide.html#upgrading-from-sparkr-15-to-16)

Note that this migration guide describes the items specific to SparkR. Many items of SQL migration can be applied when migrating SparkR to higher versions. Please refer [Migration Guide: SQL, Datasets and DataFrame](https://spark.apache.org/docs/latest/sql-migration-guide.html).
## Upgrading from SparkR 3.5 to 4.0[](https://spark.apache.org/docs/latest/sparkr-migration-guide.html#upgrading-from-sparkr-35-to-40)
  * In Spark 4.0, SparkR is deprecated and will be removed in a future version.

## Upgrading from SparkR 3.1 to 3.2[](https://spark.apache.org/docs/latest/sparkr-migration-guide.html#upgrading-from-sparkr-31-to-32)
  * Previously, SparkR automatically downloaded and installed the Spark distribution in user’s cache directory to complete SparkR installation when SparkR runs in a plain R shell or Rscript, and the Spark distribution cannot be found. Now, it asks if users want to download and install or not. To restore the previous behavior, set `SPARKR_ASK_INSTALLATION` environment variable to `FALSE`.

## Upgrading from SparkR 2.4 to 3.0[](https://spark.apache.org/docs/latest/sparkr-migration-guide.html#upgrading-from-sparkr-24-to-30)
  * The deprecated methods `parquetFile`, `saveAsParquetFile`, `jsonFile`, `jsonRDD` have been removed. Use `read.parquet`, `write.parquet`, `read.json` instead.

## Upgrading from SparkR 2.3 to 2.4[](https://spark.apache.org/docs/latest/sparkr-migration-guide.html#upgrading-from-sparkr-23-to-24)
  * Previously, we don’t check the validity of the size of the last layer in `spark.mlp`. For example, if the training data only has two labels, a `layers` param like `c(1, 3)` doesn’t cause an error previously, now it does.

## Upgrading from SparkR 2.3 to 2.3.1 and above[](https://spark.apache.org/docs/latest/sparkr-migration-guide.html#upgrading-from-sparkr-23-to-231-and-above)
  * In SparkR 2.3.0 and earlier, the `start` parameter of `substr` method was wrongly subtracted by one and considered as 0-based. This can lead to inconsistent substring results and also does not match with the behaviour with `substr` in R. In version 2.3.1 and later, it has been fixed so the `start` parameter of `substr` method is now 1-based. As an example, `substr(lit('abcdef'), 2, 4))` would result to `abc` in SparkR 2.3.0, and the result would be `bcd` in SparkR 2.3.1.

## Upgrading from SparkR 2.2 to 2.3[](https://spark.apache.org/docs/latest/sparkr-migration-guide.html#upgrading-from-sparkr-22-to-23)
  * The `stringsAsFactors` parameter was previously ignored with `collect`, for example, in `collect(createDataFrame(iris), stringsAsFactors = TRUE))`. It has been corrected.
  * For `summary`, option for statistics to compute has been added. Its output is changed from that from `describe`.
  * A warning can be raised if versions of SparkR package and the Spark JVM do not match.

## Upgrading from SparkR 2.1 to 2.2[](https://spark.apache.org/docs/latest/sparkr-migration-guide.html#upgrading-from-sparkr-21-to-22)
  * A `numPartitions` parameter has been added to `createDataFrame` and `as.DataFrame`. When splitting the data, the partition position calculation has been made to match the one in Scala.
  * The method `createExternalTable` has been deprecated to be replaced by `createTable`. Either methods can be called to create external or managed table. Additional catalog methods have also been added.
  * By default, derby.log is now saved to `tempdir()`. This will be created when instantiating the SparkSession with `enableHiveSupport` set to `TRUE`.
  * `spark.lda` was not setting the optimizer correctly. It has been corrected.
  * Several model summary outputs are updated to have `coefficients` as `matrix`. This includes `spark.logit`, `spark.kmeans`, `spark.glm`. Model summary outputs for `spark.gaussianMixture` have added log-likelihood as `loglik`.

## Upgrading from SparkR 2.0 to 3.1[](https://spark.apache.org/docs/latest/sparkr-migration-guide.html#upgrading-from-sparkr-20-to-31)
  * `join` no longer performs Cartesian Product by default, use `crossJoin` instead.

## Upgrading from SparkR 1.6 to 2.0[](https://spark.apache.org/docs/latest/sparkr-migration-guide.html#upgrading-from-sparkr-16-to-20)
  * The method `table` has been removed and replaced by `tableToDF`.
  * The class `DataFrame` has been renamed to `SparkDataFrame` to avoid name conflicts.
  * Spark’s `SQLContext` and `HiveContext` have been deprecated to be replaced by `SparkSession`. Instead of `sparkR.init()`, call `sparkR.session()` in its place to instantiate the SparkSession. Once that is done, that currently active SparkSession will be used for SparkDataFrame operations.
  * The parameter `sparkExecutorEnv` is not supported by `sparkR.session`. To set environment for the executors, set Spark config properties with the prefix “spark.executorEnv.VAR_NAME”, for example, “spark.executorEnv.PATH”
  * The `sqlContext` parameter is no longer required for these functions: `createDataFrame`, `as.DataFrame`, `read.json`, `jsonFile`, `read.parquet`, `parquetFile`, `read.text`, `sql`, `tables`, `tableNames`, `cacheTable`, `uncacheTable`, `clearCache`, `dropTempTable`, `read.df`, `loadDF`, `createExternalTable`.
  * The method `registerTempTable` has been deprecated to be replaced by `createOrReplaceTempView`.
  * The method `dropTempTable` has been deprecated to be replaced by `dropTempView`.
  * The `sc` SparkContext parameter is no longer required for these functions: `setJobGroup`, `clearJobGroup`, `cancelJobGroup`

## Upgrading from SparkR 1.5 to 1.6[](https://spark.apache.org/docs/latest/sparkr-migration-guide.html#upgrading-from-sparkr-15-to-16)
  * Before Spark 1.6.0, the default mode for writes was `append`. It was changed in Spark 1.6.0 to `error` to match the Scala API.
  * SparkSQL converts `NA` in R to `null` and vice-versa.
  * Since 1.6.1, withColumn method in SparkR supports adding a new column to or replacing existing columns of the same name of a DataFrame.
