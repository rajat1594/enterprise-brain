[ ![](https://spark.apache.org/images/spark-logo-rev.svg)](https://spark.apache.org/docs/latest/index.html)4.1.2
  * [Overview](https://spark.apache.org/docs/latest/index.html)
  * [Programming Guides](https://spark.apache.org/docs/latest/streaming/additional-information.html)
[Quick Start](https://spark.apache.org/docs/latest/quick-start.html) [RDDs, Accumulators, Broadcasts Vars](https://spark.apache.org/docs/latest/rdd-programming-guide.html) [SQL, DataFrames, and Datasets](https://spark.apache.org/docs/latest/sql-programming-guide.html) [Structured Streaming](https://spark.apache.org/docs/latest/streaming/index.html) [Spark Streaming (DStreams)](https://spark.apache.org/docs/latest/streaming-programming-guide.html) [MLlib (Machine Learning)](https://spark.apache.org/docs/latest/ml-guide.html) [GraphX (Graph Processing)](https://spark.apache.org/docs/latest/graphx-programming-guide.html) [SparkR (R on Spark)](https://spark.apache.org/docs/latest/sparkr.html) [PySpark (Python on Spark)](https://spark.apache.org/docs/latest/api/python/getting_started/index.html) [Declarative Pipelines](https://spark.apache.org/docs/latest/declarative-pipelines-programming-guide.html)
  * [API Docs](https://spark.apache.org/docs/latest/streaming/additional-information.html)
[Python](https://spark.apache.org/docs/latest/api/python/index.html) [Scala](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html) [Java](https://spark.apache.org/docs/latest/api/java/index.html) [R](https://spark.apache.org/docs/latest/api/R/index.html) [SQL, Built-in Functions](https://spark.apache.org/docs/latest/api/sql/index.html)
  * [Deploying](https://spark.apache.org/docs/latest/streaming/additional-information.html)
[Overview](https://spark.apache.org/docs/latest/cluster-overview.html) [Submitting Applications](https://spark.apache.org/docs/latest/submitting-applications.html) [Spark Standalone](https://spark.apache.org/docs/latest/spark-standalone.html) [YARN](https://spark.apache.org/docs/latest/running-on-yarn.html) [Kubernetes](https://spark.apache.org/docs/latest/running-on-kubernetes.html)
  * [More](https://spark.apache.org/docs/latest/streaming/additional-information.html)
[Configuration](https://spark.apache.org/docs/latest/configuration.html) [Monitoring](https://spark.apache.org/docs/latest/monitoring.html) [Tuning Guide](https://spark.apache.org/docs/latest/tuning.html) [Job Scheduling](https://spark.apache.org/docs/latest/job-scheduling.html) [Security](https://spark.apache.org/docs/latest/security.html) [Hardware Provisioning](https://spark.apache.org/docs/latest/hardware-provisioning.html) [Migration Guide](https://spark.apache.org/docs/latest/migration-guide.html) [Building Spark](https://spark.apache.org/docs/latest/building-spark.html) [Contributing to Spark](https://spark.apache.org/contributing.html) [Third Party Projects](https://spark.apache.org/third-party-projects.html)
  *

###  [Structured Streaming Programming Guide](https://spark.apache.org/docs/latest/streaming/index.html)[](https://spark.apache.org/docs/latest/streaming/additional-information.html#structured-streaming-programming-guide)
  * [ Overview ](https://spark.apache.org/docs/latest/streaming/index.html)
  * [ Getting Started ](https://spark.apache.org/docs/latest/streaming/getting-started.html)
  * [ APIs on DataFrames and Datasets ](https://spark.apache.org/docs/latest/streaming/apis-on-dataframes-and-datasets.html)
  * [ Performance Tips ](https://spark.apache.org/docs/latest/streaming/performance-tips.html)
  * [ Additional Information ](https://spark.apache.org/docs/latest/streaming/additional-information.html)
    * [ Miscellaneous Notes ](https://spark.apache.org/docs/latest/streaming/additional-information.html#miscellaneous-notes)
    * [ Related Resources ](https://spark.apache.org/docs/latest/streaming/additional-information.html#related-resources)
    * [ Migration Guide ](https://spark.apache.org/docs/latest/streaming/additional-information.html#migration-guide)

# Structured Streaming Programming Guide[](https://spark.apache.org/docs/latest/streaming/additional-information.html#structured-streaming-programming-guide-1)
# Miscellaneous Notes[](https://spark.apache.org/docs/latest/streaming/additional-information.html#miscellaneous-notes)
  * Several configurations are not modifiable after the query has run. To change them, discard the checkpoint and start a new query. These configurations include:
    * `spark.sql.shuffle.partitions`
      * This is due to the physical partitioning of state: state is partitioned via applying hash function to key, hence the number of partitions for state should be unchanged.
      * If you want to run fewer tasks for stateful operations, `coalesce` would help with avoiding unnecessary repartitioning.
        * After `coalesce`, the number of (reduced) tasks will be kept unless another shuffle happens.
    * `spark.sql.streaming.stateStore.providerClass`: To read the previous state of the query properly, the class of state store provider should be unchanged.
    * `spark.sql.streaming.multipleWatermarkPolicy`: Modification of this would lead inconsistent watermark value when query contains multiple watermarks, hence the policy should be unchanged.

# Related Resources[](https://spark.apache.org/docs/latest/streaming/additional-information.html#related-resources)
## Further Reading[](https://spark.apache.org/docs/latest/streaming/additional-information.html#further-reading)
  * See and run the [Python](https://github.com/apache/spark/tree/v4.1.2/examples/src/main/python/sql/streaming)/[Scala](https://github.com/apache/spark/tree/v4.1.2/examples/src/main/scala/org/apache/spark/examples/sql/streaming)/[Java](https://github.com/apache/spark/tree/v4.1.2/examples/src/main/java/org/apache/spark/examples/sql/streaming)/[R](https://github.com/apache/spark/tree/v4.1.2/examples/src/main/r/streaming) examples.
    * [Instructions](https://spark.apache.org/docs/latest/index.html#running-the-examples-and-shell) on how to run Spark examples
  * Read about integrating with Kafka in the [Structured Streaming Kafka Integration Guide](https://spark.apache.org/docs/latest/streaming/structured-streaming-kafka-integration.html)
  * Read more details about using DataFrames/Datasets in the [Spark SQL Programming Guide](https://spark.apache.org/docs/latest/sql-programming-guide.html)
  * Third-party Blog Posts
    * [Real-time Streaming ETL with Structured Streaming in Apache Spark 2.1 (Databricks Blog)](https://databricks.com/blog/2017/01/19/real-time-streaming-etl-structured-streaming-apache-spark-2-1.html)
    * [Real-Time End-to-End Integration with Apache Kafka in Apache Spark’s Structured Streaming (Databricks Blog)](https://databricks.com/blog/2017/04/04/real-time-end-to-end-integration-with-apache-kafka-in-apache-sparks-structured-streaming.html)
    * [Event-time Aggregation and Watermarking in Apache Spark’s Structured Streaming (Databricks Blog)](https://databricks.com/blog/2017/05/08/event-time-aggregation-watermarking-apache-sparks-structured-streaming.html)

## Talks[](https://spark.apache.org/docs/latest/streaming/additional-information.html#talks)
  * Spark Summit Europe 2017
    * Easy, Scalable, Fault-tolerant Stream Processing with Structured Streaming in Apache Spark - [Part 1 slides/video](https://databricks.com/session/easy-scalable-fault-tolerant-stream-processing-with-structured-streaming-in-apache-spark), [Part 2 slides/video](https://databricks.com/session/easy-scalable-fault-tolerant-stream-processing-with-structured-streaming-in-apache-spark-continues)
    * Deep Dive into Stateful Stream Processing in Structured Streaming - [slides/video](https://databricks.com/session/deep-dive-into-stateful-stream-processing-in-structured-streaming)
  * Spark Summit 2016
    * A Deep Dive into Structured Streaming - [slides/video](https://spark-summit.org/2016/events/a-deep-dive-into-structured-streaming/)

# Migration Guide[](https://spark.apache.org/docs/latest/streaming/additional-information.html#migration-guide)
The migration guide is now archived [on this page](https://spark.apache.org/docs/latest/streaming/ss-migration-guide.html).
