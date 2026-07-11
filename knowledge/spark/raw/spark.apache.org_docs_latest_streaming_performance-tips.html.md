[ ![](https://spark.apache.org/images/spark-logo-rev.svg)](https://spark.apache.org/docs/latest/index.html)4.1.2
  * [Overview](https://spark.apache.org/docs/latest/index.html)
  * [Programming Guides](https://spark.apache.org/docs/latest/streaming/performance-tips.html)
[Quick Start](https://spark.apache.org/docs/latest/quick-start.html) [RDDs, Accumulators, Broadcasts Vars](https://spark.apache.org/docs/latest/rdd-programming-guide.html) [SQL, DataFrames, and Datasets](https://spark.apache.org/docs/latest/sql-programming-guide.html) [Structured Streaming](https://spark.apache.org/docs/latest/streaming/index.html) [Spark Streaming (DStreams)](https://spark.apache.org/docs/latest/streaming-programming-guide.html) [MLlib (Machine Learning)](https://spark.apache.org/docs/latest/ml-guide.html) [GraphX (Graph Processing)](https://spark.apache.org/docs/latest/graphx-programming-guide.html) [SparkR (R on Spark)](https://spark.apache.org/docs/latest/sparkr.html) [PySpark (Python on Spark)](https://spark.apache.org/docs/latest/api/python/getting_started/index.html) [Declarative Pipelines](https://spark.apache.org/docs/latest/declarative-pipelines-programming-guide.html)
  * [API Docs](https://spark.apache.org/docs/latest/streaming/performance-tips.html)
[Python](https://spark.apache.org/docs/latest/api/python/index.html) [Scala](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html) [Java](https://spark.apache.org/docs/latest/api/java/index.html) [R](https://spark.apache.org/docs/latest/api/R/index.html) [SQL, Built-in Functions](https://spark.apache.org/docs/latest/api/sql/index.html)
  * [Deploying](https://spark.apache.org/docs/latest/streaming/performance-tips.html)
[Overview](https://spark.apache.org/docs/latest/cluster-overview.html) [Submitting Applications](https://spark.apache.org/docs/latest/submitting-applications.html) [Spark Standalone](https://spark.apache.org/docs/latest/spark-standalone.html) [YARN](https://spark.apache.org/docs/latest/running-on-yarn.html) [Kubernetes](https://spark.apache.org/docs/latest/running-on-kubernetes.html)
  * [More](https://spark.apache.org/docs/latest/streaming/performance-tips.html)
[Configuration](https://spark.apache.org/docs/latest/configuration.html) [Monitoring](https://spark.apache.org/docs/latest/monitoring.html) [Tuning Guide](https://spark.apache.org/docs/latest/tuning.html) [Job Scheduling](https://spark.apache.org/docs/latest/job-scheduling.html) [Security](https://spark.apache.org/docs/latest/security.html) [Hardware Provisioning](https://spark.apache.org/docs/latest/hardware-provisioning.html) [Migration Guide](https://spark.apache.org/docs/latest/migration-guide.html) [Building Spark](https://spark.apache.org/docs/latest/building-spark.html) [Contributing to Spark](https://spark.apache.org/contributing.html) [Third Party Projects](https://spark.apache.org/third-party-projects.html)
  * 

###  [Structured Streaming Programming Guide](https://spark.apache.org/docs/latest/streaming/index.html)[](https://spark.apache.org/docs/latest/streaming/performance-tips.html#structured-streaming-programming-guide)
  * [ Overview ](https://spark.apache.org/docs/latest/streaming/index.html)
  * [ Getting Started ](https://spark.apache.org/docs/latest/streaming/getting-started.html)
  * [ APIs on DataFrames and Datasets ](https://spark.apache.org/docs/latest/streaming/apis-on-dataframes-and-datasets.html)
  * [ Performance Tips ](https://spark.apache.org/docs/latest/streaming/performance-tips.html)
    * [ Asynchronous Progress Tracking ](https://spark.apache.org/docs/latest/streaming/performance-tips.html#asynchronous-progress-tracking)
    * [ Continuous Processing ](https://spark.apache.org/docs/latest/streaming/performance-tips.html#continuous-processing)
  * [ Additional Information ](https://spark.apache.org/docs/latest/streaming/additional-information.html)


# Structured Streaming Programming Guide[](https://spark.apache.org/docs/latest/streaming/performance-tips.html#structured-streaming-programming-guide-1)
  * Table of contents


# Asynchronous Progress Tracking[](https://spark.apache.org/docs/latest/streaming/performance-tips.html#asynchronous-progress-tracking)
## What is it?[](https://spark.apache.org/docs/latest/streaming/performance-tips.html#what-is-it)
Asynchronous progress tracking allows streaming queries to checkpoint progress asynchronously and in parallel to the actual data processing within a micro-batch, reducing latency associated with maintaining the offset log and commit log.
![Async Progress Tracking](https://spark.apache.org/docs/latest/img/async-progress.png)
## How does it work?[](https://spark.apache.org/docs/latest/streaming/performance-tips.html#how-does-it-work)
Structured Streaming relies on persisting and managing offsets as progress indicators for query processing. Offset management operation directly impacts processing latency, because no data processing can occur until these operations are complete. Asynchronous progress tracking enables streaming queries to checkpoint progress without being impacted by these offset management operations.
## How to use it?[](https://spark.apache.org/docs/latest/streaming/performance-tips.html#how-to-use-it)
The code snippet below provides an example of how to use this feature:

```
val stream = spark.readStream
      .format("kafka")
      .option("kafka.bootstrap.servers", "host1:port1,host2:port2")
      .option("subscribe", "in")
      .load()
val query = stream.writeStream
     .format("kafka")
     .option("topic", "out")
     .option("checkpointLocation", "/tmp/checkpoint")
     .option("asyncProgressTrackingEnabled", "true")
     .start()

```

The table below describes the configurations for this feature and default values associated with them.  
| Option  | Value  | Default  | Description  |  
| --- | --- | --- | --- |  
| asyncProgressTrackingEnabled  | true/false  | false  | enable or disable asynchronous progress tracking  |  
| asyncProgressTrackingCheckpointIntervalMs  | millisecond  | 1000  | the interval in which we commit offsets and completion commits  |  
## Limitations[](https://spark.apache.org/docs/latest/streaming/performance-tips.html#limitations)
The initial version of the feature has the following limitations:
  * Asynchronous progress tracking is only supported in stateless queries using Kafka Sink
  * Exactly once end-to-end processing will not be supported with this asynchronous progress tracking because offset ranges for batch can be changed in case of failure. Though many sinks, such as Kafka sink, do not support writing exactly once anyways.


## Switching the setting off[](https://spark.apache.org/docs/latest/streaming/performance-tips.html#switching-the-setting-off)
Turning the async progress tracking off may cause the following exception to be thrown

```
java.lang.IllegalStateException: batch x doesn't exist

```

Also the following error message may be printed in the driver logs:

```
The offset log for batch x doesn't exist, which is required to restart the query from the latest batch x from the offset log. Please ensure there are two subsequent offset logs available for the latest batch via manually deleting the offset file(s). Please also ensure the latest batch for commit log is equal or one batch earlier than the latest batch for offset log.

```

This is caused by the fact that when async progress tracking is enabled, the framework will not checkpoint progress for every batch as would be done if async progress tracking is not used. To solve this problem simply re-enable “asyncProgressTrackingEnabled” and set “asyncProgressTrackingCheckpointIntervalMs” to 0 and run the streaming query until at least two micro-batches have been processed. Async progress tracking can be now safely disabled and restarting query should proceed normally.
# Continuous Processing[](https://spark.apache.org/docs/latest/streaming/performance-tips.html#continuous-processing)
## [Experimental][](https://spark.apache.org/docs/latest/streaming/performance-tips.html#experimental)
**Continuous processing** is a new, experimental streaming execution mode introduced in Spark 2.3 that enables low (~1 ms) end-to-end latency with at-least-once fault-tolerance guarantees. Compare this with the default _micro-batch processing_ engine which can achieve exactly-once guarantees but achieve latencies of ~100ms at best. For some types of queries (discussed below), you can choose which mode to execute them in without modifying the application logic (i.e. without changing the DataFrame/Dataset operations).
To run a supported query in continuous processing mode, all you need to do is specify a **continuous trigger** with the desired checkpoint interval as a parameter. For example,
  * **Python**
  * **Scala**
  * **Java**



```
spark \
  .readStream \
  .format("kafka") \
  .option("kafka.bootstrap.servers", "host1:port1,host2:port2") \
  .option("subscribe", "topic1") \
  .load() \
  .selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)") \
  .writeStream \
  .format("kafka") \
  .option("kafka.bootstrap.servers", "host1:port1,host2:port2") \
  .option("topic", "topic1") \
  .trigger(continuous="1 second") \     # only change in query
  .start()
```


```
import org.apache.spark.sql.streaming.Trigger

spark
  .readStream
  .format("kafka")
  .option("kafka.bootstrap.servers", "host1:port1,host2:port2")
  .option("subscribe", "topic1")
  .load()
  .selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")
  .writeStream
  .format("kafka")
  .option("kafka.bootstrap.servers", "host1:port1,host2:port2")
  .option("topic", "topic1")
  .trigger(Trigger.Continuous("1 second"))  // only change in query
  .start()
```


```
import org.apache.spark.sql.streaming.Trigger;

spark
  .readStream
  .format("kafka")
  .option("kafka.bootstrap.servers", "host1:port1,host2:port2")
  .option("subscribe", "topic1")
  .load()
  .selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")
  .writeStream
  .format("kafka")
  .option("kafka.bootstrap.servers", "host1:port1,host2:port2")
  .option("topic", "topic1")
  .trigger(Trigger.Continuous("1 second"))  // only change in query
  .start();
```

A checkpoint interval of 1 second means that the continuous processing engine will record the progress of the query every second. The resulting checkpoints are in a format compatible with the micro-batch engine, hence any query can be restarted with any trigger. For example, a supported query started with the micro-batch mode can be restarted in continuous mode, and vice versa. Note that any time you switch to continuous mode, you will get at-least-once fault-tolerance guarantees.
## Supported Queries[](https://spark.apache.org/docs/latest/streaming/performance-tips.html#supported-queries)
As of Spark 2.4, only the following type of queries are supported in the continuous processing mode.
  * _Operations_ : Only map-like Dataset/DataFrame operations are supported in continuous mode, that is, only projections (`select`, `map`, `flatMap`, `mapPartitions`, etc.) and selections (`where`, `filter`, etc.). 
    * All SQL functions are supported except aggregation functions (since aggregations are not yet supported), `current_timestamp()` and `current_date()` (deterministic computations using time is challenging).
  * _Sources_ : 
    * Kafka source: All options are supported.
    * Rate source: Good for testing. Only options that are supported in the continuous mode are `numPartitions` and `rowsPerSecond`.
  * _Sinks_ : 
    * Kafka sink: All options are supported.
    * Memory sink: Good for debugging.
    * Console sink: Good for debugging. All options are supported. Note that the console will print every checkpoint interval that you have specified in the continuous trigger.


See [Input Sources](https://spark.apache.org/docs/latest/streaming/apis-on-dataframes-and-datasets.html#input-sources) and [Output Sinks](https://spark.apache.org/docs/latest/streaming/apis-on-dataframes-and-datasets.html#output-sinks) sections for more details on them. While the console sink is good for testing, the end-to-end low-latency processing can be best observed with Kafka as the source and sink, as this allows the engine to process the data and make the results available in the output topic within milliseconds of the input data being available in the input topic.
## Caveats[](https://spark.apache.org/docs/latest/streaming/performance-tips.html#caveats)
  * Continuous processing engine launches multiple long-running tasks that continuously read data from sources, process it and continuously write to sinks. The number of tasks required by the query depends on how many partitions the query can read from the sources in parallel. Therefore, before starting a continuous processing query, you must ensure there are enough cores in the cluster to all the tasks in parallel. For example, if you are reading from a Kafka topic that has 10 partitions, then the cluster must have at least 10 cores for the query to make progress.
  * Stopping a continuous processing stream may produce spurious task termination warnings. These can be safely ignored.
  * There are currently no automatic retries of failed tasks. Any failure will lead to the query being stopped and it needs to be manually restarted from the checkpoint.


