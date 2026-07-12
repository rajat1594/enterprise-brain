Spark 4.1.2 ScalaDoc < Back
 __ __
# Packages
  * [__](https://spark.apache.org/docs/latest/api/scala/index.html "Permalink") package [root](https://spark.apache.org/docs/latest/api/scala/index.html)

Definition Classes
    [root](https://spark.apache.org/docs/latest/api/scala/index.html "_root_")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/index.html "Permalink") package [org](https://spark.apache.org/docs/latest/api/scala/org/index.html)

Definition Classes
    [root](https://spark.apache.org/docs/latest/api/scala/index.html "_root_")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/index.html "Permalink") package [apache](https://spark.apache.org/docs/latest/api/scala/org/apache/index.html)

Definition Classes
    [org](https://spark.apache.org/docs/latest/api/scala/org/index.html "org")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/parquet/index.html "Permalink") package [parquet](https://spark.apache.org/docs/latest/api/scala/org/apache/parquet/index.html)

Definition Classes
    [apache](https://spark.apache.org/docs/latest/api/scala/org/apache/index.html "org.apache")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "Permalink") package spark
Core Spark functionality.
Core Spark functionality. [org.apache.spark.SparkContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html "org.apache.spark.SparkContext") serves as the main entry point to Spark, while [org.apache.spark.rdd.RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") is the data type representing a distributed collection, and provides most parallel operations.
In addition, [org.apache.spark.rdd.PairRDDFunctions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html "org.apache.spark.rdd.PairRDDFunctions") contains operations available only on RDDs of key-value pairs, such as `groupByKey` and `join`; [org.apache.spark.rdd.DoubleRDDFunctions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/DoubleRDDFunctions.html "org.apache.spark.rdd.DoubleRDDFunctions") contains operations available only on RDDs of Doubles; and [org.apache.spark.rdd.SequenceFileRDDFunctions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/SequenceFileRDDFunctions.html "org.apache.spark.rdd.SequenceFileRDDFunctions") contains operations available on RDDs that can be saved as SequenceFiles. These operations are automatically available on any RDD of the right type (e.g. RDD[(Int, Int)] through implicit conversions.
Java programmers should reference the [org.apache.spark.api.java](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/index.html "org.apache.spark.api.java") package for Spark programming APIs in Java.
Classes and methods marked with  Experimental are user-facing features which have not been officially adopted by the Spark project. These are subject to change or removal in minor releases.
Classes and methods marked with  Developer API are intended for advanced users want to extend Spark through lower level interfaces. These are subject to changes or removal in minor releases.

Definition Classes
    [apache](https://spark.apache.org/docs/latest/api/scala/org/apache/index.html "org.apache")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/index.html "Permalink") package [api](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/index.html)
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/broadcast/index.html "Permalink") package [broadcast](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/broadcast/index.html "Spark's broadcast variables, used to broadcast immutable datasets to all nodes.")
Spark's broadcast variables, used to broadcast immutable datasets to all nodes.
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html "Permalink") package [graphx](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html "ALPHA COMPONENT GraphX is a graph processing framework built on top of Spark.")
ALPHA COMPONENT GraphX is a graph processing framework built on top of Spark.
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/input/index.html "Permalink") package [input](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/input/index.html)
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/index.html "Permalink") package [io](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/index.html "IO codecs used for compression.")
IO codecs used for compression.
IO codecs used for compression. See [org.apache.spark.io.CompressionCodec](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/CompressionCodec.html "org.apache.spark.io.CompressionCodec").
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/launcher/index.html "Permalink") package [launcher](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/launcher/index.html)
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/mapred/index.html "Permalink") package [mapred](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/mapred/index.html)
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/metrics/index.html "Permalink") package [metrics](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/metrics/index.html)
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/index.html "Permalink") package [ml](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/index.html "DataFrame-based machine learning APIs to let users quickly assemble and configure practical machine learning pipelines.")
DataFrame-based machine learning APIs to let users quickly assemble and configure practical machine learning pipelines.
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/mllib/index.html "Permalink") package [mllib](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/mllib/index.html "RDD-based machine learning APIs \(in maintenance mode\).")
RDD-based machine learning APIs (in maintenance mode).
RDD-based machine learning APIs (in maintenance mode).
The `spark.mllib` package is in maintenance mode as of the Spark 2.0.0 release to encourage migration to the DataFrame-based APIs under the [org.apache.spark.ml](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/index.html "org.apache.spark.ml") package. While in maintenance mode,
    * no new features in the RDD-based `spark.mllib` package will be accepted, unless they block implementing new features in the DataFrame-based `spark.ml` package;
    * bug fixes in the RDD-based APIs will still be accepted.
The developers will continue adding more features to the DataFrame-based APIs in the 2.x series to reach feature parity with the RDD-based APIs. And once we reach feature parity, this package will be deprecated.

See also

[SPARK-4591](https://issues.apache.org/jira/browse/SPARK-4591) to track the progress of feature parity
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/partial/index.html "Permalink") package [partial](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/partial/index.html "Support for approximate results.")
Support for approximate results.
Support for approximate results. This provides convenient api and also implementation for approximate calculation.

See also

[org.apache.spark.rdd.RDD.countApprox](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html#countApprox\(timeout:Long,confidence:Double\):org.apache.spark.partial.PartialResult\[org.apache.spark.partial.BoundedDouble\])
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/paths/index.html "Permalink") package [paths](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/paths/index.html)
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/index.html "Permalink") package [rdd](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/index.html "Provides several RDD implementations.")
Provides several RDD implementations.
Provides several RDD implementations. See [org.apache.spark.rdd.RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD").
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/resource/index.html "Permalink") package [resource](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/resource/index.html)
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/index.html "Permalink") package [scheduler](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/index.html "Spark's scheduling components.")
Spark's scheduling components.
Spark's scheduling components. This includes the `org.apache.spark.scheduler.DAGScheduler` and lower level `org.apache.spark.scheduler.TaskScheduler`.
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/security/index.html "Permalink") package [security](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/security/index.html)
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/index.html "Permalink") package [serializer](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/index.html "Pluggable serializers for RDD and shuffle data.")
Pluggable serializers for RDD and shuffle data.
Pluggable serializers for RDD and shuffle data.

See also

[org.apache.spark.serializer.Serializer](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/Serializer.html "org.apache.spark.serializer.Serializer")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/shuffle/index.html "Permalink") package [shuffle](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/shuffle/index.html)
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html "Permalink") package [sql](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html "Allows the execution of relational queries, including those expressed in SQL using Spark.")
Allows the execution of relational queries, including those expressed in SQL using Spark.
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/status/index.html "Permalink") package [status](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/status/index.html)
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/index.html "Permalink") package [storage](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/index.html)
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/index.html "Permalink") package [streaming](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/index.html "Spark Streaming functionality.")
Spark Streaming functionality.
Spark Streaming functionality. [org.apache.spark.streaming.StreamingContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html "org.apache.spark.streaming.StreamingContext") serves as the main entry point to Spark Streaming, while [org.apache.spark.streaming.dstream.DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream") is the data type representing a continuous sequence of RDDs, representing a continuous stream of data.
In addition, [org.apache.spark.streaming.dstream.PairDStreamFunctions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html "org.apache.spark.streaming.dstream.PairDStreamFunctions") contains operations available only on DStreams of key-value pairs, such as `groupByKey` and `reduceByKey`. These operations are automatically available on any DStream of the right type (e.g. DStream[(Int, Int)] through implicit conversions.
For the Java API of Spark Streaming, take a look at the [org.apache.spark.streaming.api.java.JavaStreamingContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html "org.apache.spark.streaming.api.java.JavaStreamingContext") which serves as the entry point, and the [org.apache.spark.streaming.api.java.JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream") and the [org.apache.spark.streaming.api.java.JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream") which have the DStream functionality.
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ui/index.html "Permalink") package [ui](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ui/index.html)
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/unsafe/index.html "Permalink") package [unsafe](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/unsafe/index.html)
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/index.html "Permalink") package [util](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/index.html "Spark utilities.")
Spark utilities.
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Aggregator.html ":: DeveloperApi :: A set of functions used to aggregate data.")[Aggregator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Aggregator.html ":: DeveloperApi :: A set of functions used to aggregate data.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/BarrierTaskContext$.html) [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/BarrierTaskContext.html ":: Experimental :: A TaskContext with extra contextual info and tooling for tasks in a barrier stage.")[BarrierTaskContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/BarrierTaskContext.html ":: Experimental :: A TaskContext with extra contextual info and tooling for tasks in a barrier stage.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/BarrierTaskInfo.html ":: Experimental :: Carries all task infos of a barrier task.")[BarrierTaskInfo](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/BarrierTaskInfo.html ":: Experimental :: Carries all task infos of a barrier task.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/BreakingChangeInfo.html "Additional information if the error was caused by a breaking change.")[BreakingChangeInfo](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/BreakingChangeInfo.html "Additional information if the error was caused by a breaking change.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html "A FutureAction for actions that could trigger multiple Spark jobs.")[ComplexFutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html "A FutureAction for actions that could trigger multiple Spark jobs.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html ":: DeveloperApi :: A TaskContext aware iterator.")[ContextAwareIterator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html ":: DeveloperApi :: A TaskContext aware iterator.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Dependency.html ":: DeveloperApi :: Base class for dependencies.")[Dependency](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Dependency.html ":: DeveloperApi :: Base class for dependencies.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ErrorClassesJsonReader.html "A reader to load error information from one or more JSON files.")[ErrorClassesJsonReader](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ErrorClassesJsonReader.html "A reader to load error information from one or more JSON files.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ExceptionFailure.html ":: DeveloperApi :: Task failed due to a runtime exception.")[ExceptionFailure](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ExceptionFailure.html ":: DeveloperApi :: Task failed due to a runtime exception.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ExecutorLostFailure.html ":: DeveloperApi :: The task failed because the executor that it was running on was lost.")[ExecutorLostFailure](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ExecutorLostFailure.html ":: DeveloperApi :: The task failed because the executor that it was running on was lost.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/FetchFailed.html ":: DeveloperApi :: Task failed to fetch shuffle data from a remote node.")[FetchFailed](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/FetchFailed.html ":: DeveloperApi :: Task failed to fetch shuffle data from a remote node.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/FutureAction.html "A future for the result of an action to support cancellation.")[FutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/FutureAction.html "A future for the result of an action to support cancellation.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/HashPartitioner.html "A org.apache.spark.Partitioner that implements hash-based partitioning using Java's Object.hashCode.")[HashPartitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/HashPartitioner.html "A org.apache.spark.Partitioner that implements hash-based partitioning using Java's Object.hashCode.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/InterruptibleIterator.html ":: DeveloperApi :: An iterator that wraps around an existing iterator to provide task killing functionality.")[InterruptibleIterator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/InterruptibleIterator.html ":: DeveloperApi :: An iterator that wraps around an existing iterator to provide task killing functionality.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/JobExecutionStatus.html)[JobExecutionStatus](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/JobExecutionStatus.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/JobSubmitter.html "Handle via which a "run" function passed to a ComplexFutureAction can submit jobs for execution.")[JobSubmitter](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/JobSubmitter.html "Handle via which a "run" function passed to a ComplexFutureAction can submit jobs for execution.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/MitigationConfig.html "A spark config flag that can be used to mitigate a breaking change.")[MitigationConfig](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/MitigationConfig.html "A spark config flag that can be used to mitigate a breaking change.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/NarrowDependency.html ":: DeveloperApi :: Base class for dependencies where each partition of the child RDD depends on a small number of partitions of the parent RDD.")[NarrowDependency](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/NarrowDependency.html ":: DeveloperApi :: Base class for dependencies where each partition of the child RDD depends on a small number of partitions of the parent RDD.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/OneToOneDependency.html ":: DeveloperApi :: Represents a one-to-one dependency between partitions of the parent and child RDDs.")[OneToOneDependency](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/OneToOneDependency.html ":: DeveloperApi :: Represents a one-to-one dependency between partitions of the parent and child RDDs.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partition.html "An identifier for a partition in an RDD.")[Partition](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partition.html "An identifier for a partition in an RDD.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/PartitionEvaluator.html "An evaluator for computing RDD partitions.")[PartitionEvaluator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/PartitionEvaluator.html "An evaluator for computing RDD partitions.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/PartitionEvaluatorFactory.html "A factory to create PartitionEvaluator.")[PartitionEvaluatorFactory](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/PartitionEvaluatorFactory.html "A factory to create PartitionEvaluator.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner$.html) [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "An object that defines how the elements in a key-value pair RDD are partitioned by key.")[Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "An object that defines how the elements in a key-value pair RDD are partitioned by key.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/QueryContext.html "Query context of a SparkThrowable.")[QueryContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/QueryContext.html "Query context of a SparkThrowable.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/QueryContextType.html "The type of QueryContext.")[QueryContextType](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/QueryContextType.html "The type of QueryContext.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/RangeDependency.html ":: DeveloperApi :: Represents a one-to-one dependency between ranges of partitions in the parent and child RDDs.")[RangeDependency](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/RangeDependency.html ":: DeveloperApi :: Represents a one-to-one dependency between ranges of partitions in the parent and child RDDs.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/RangePartitioner.html "A org.apache.spark.Partitioner that partitions sortable records by range into roughly equal ranges.")[RangePartitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/RangePartitioner.html "A org.apache.spark.Partitioner that partitions sortable records by range into roughly equal ranges.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html)[ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Resubmitted$.html ":: DeveloperApi :: A org.apache.spark.scheduler.ShuffleMapTask that completed successfully earlier, but we lost the executor before the stage completed.")[Resubmitted](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Resubmitted$.html ":: DeveloperApi :: A org.apache.spark.scheduler.ShuffleMapTask that completed successfully earlier, but we lost the executor before the stage completed.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SerializableWritable.html)[SerializableWritable](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SerializableWritable.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ShuffleDependency$.html) [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ShuffleDependency.html ":: DeveloperApi :: Represents a dependency on the output of a shuffle stage.")[ShuffleDependency](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ShuffleDependency.html ":: DeveloperApi :: Represents a dependency on the output of a shuffle stage.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ShuffleStatusNotFoundException.html)[ShuffleStatusNotFoundException](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ShuffleStatusNotFoundException.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SimpleFutureAction.html "A FutureAction holding the result of an action that triggers a single job.")[SimpleFutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SimpleFutureAction.html "A FutureAction holding the result of an action that triggers a single job.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html "Configuration for a Spark application.")[SparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html "Configuration for a Spark application.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext$.html "The SparkContext object contains a number of implicit conversions and parameters for use with various Spark features.") [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html "Main entry point for Spark functionality.")[SparkContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html "Main entry point for Spark functionality.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkEnv$.html) [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkEnv.html ":: DeveloperApi :: Holds all the runtime environment objects for a running Spark instance \(either master or worker\), including the serializer, RpcEnv, block manager, map output tracker, etc.")[SparkEnv](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkEnv.html ":: DeveloperApi :: Holds all the runtime environment objects for a running Spark instance \(either master or worker\), including the serializer, RpcEnv, block manager, map output tracker, etc.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkException$.html) [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkException.html)[SparkException](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkException.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkExecutorInfo.html "Exposes information about Spark Executors.")[SparkExecutorInfo](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkExecutorInfo.html "Exposes information about Spark Executors.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkFiles$.html "Resolves paths to files added through SparkContext.addFile\(\).")[SparkFiles](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkFiles$.html "Resolves paths to files added through SparkContext.addFile\(\).")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkFirehoseListener.html "Class that allows users to receive all SparkListener events.")[SparkFirehoseListener](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkFirehoseListener.html "Class that allows users to receive all SparkListener events.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkJobInfo.html "Exposes information about Spark Jobs.")[SparkJobInfo](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkJobInfo.html "Exposes information about Spark Jobs.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkStageInfo.html "Exposes information about Spark Stages.")[SparkStageInfo](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkStageInfo.html "Exposes information about Spark Stages.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkStatusTracker.html "Low-level status reporting APIs for monitoring job and stage progress.")[SparkStatusTracker](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkStatusTracker.html "Low-level status reporting APIs for monitoring job and stage progress.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkThrowable.html "Interface mixed into Throwables thrown from Spark.")[SparkThrowable](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkThrowable.html "Interface mixed into Throwables thrown from Spark.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/StringSubstitutor.html)[StringSubstitutor](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/StringSubstitutor.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Success$.html ":: DeveloperApi :: Task succeeded.")[Success](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Success$.html ":: DeveloperApi :: Task succeeded.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskCommitDenied.html ":: DeveloperApi :: Task requested the driver to commit, but was denied.")[TaskCommitDenied](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskCommitDenied.html ":: DeveloperApi :: Task requested the driver to commit, but was denied.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskContext$.html) [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskContext.html "Contextual information about a task which can be read or mutated during execution.")[TaskContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskContext.html "Contextual information about a task which can be read or mutated during execution.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskEndReason.html ":: DeveloperApi :: Various possible reasons why a task ended.")[TaskEndReason](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskEndReason.html ":: DeveloperApi :: Various possible reasons why a task ended.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskFailedReason.html ":: DeveloperApi :: Various possible reasons why a task failed.")[TaskFailedReason](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskFailedReason.html ":: DeveloperApi :: Various possible reasons why a task failed.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskKilled.html ":: DeveloperApi :: Task was killed intentionally and needs to be rescheduled.")[TaskKilled](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskKilled.html ":: DeveloperApi :: Task was killed intentionally and needs to be rescheduled.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskKilledException.html ":: DeveloperApi :: Exception thrown when a task is explicitly killed \(i.e., task failure is expected\).")[TaskKilledException](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskKilledException.html ":: DeveloperApi :: Exception thrown when a task is explicitly killed \(i.e., task failure is expected\).")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskResultLost$.html ":: DeveloperApi :: The task finished successfully, but the result was lost from the executor's block manager before it was fetched.")[TaskResultLost](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskResultLost$.html ":: DeveloperApi :: The task finished successfully, but the result was lost from the executor's block manager before it was fetched.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/UnknownReason$.html ":: DeveloperApi :: We don't know why the task ended -- for example, because of a ClassNotFound exception when deserializing the task result.")[UnknownReason](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/UnknownReason$.html ":: DeveloperApi :: We don't know why the task ended -- for example, because of a ClassNotFound exception when deserializing the task result.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/WritableConverter$.html)[WritableConverter](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/WritableConverter$.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/WritableFactory$.html)[WritableFactory](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/WritableFactory$.html)

p
[org](https://spark.apache.org/docs/latest/api/scala/org/index.html "org").[apache](https://spark.apache.org/docs/latest/api/scala/org/apache/index.html "org.apache")
# spark[ __](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "Permalink")
####  package spark
Core Spark functionality. [org.apache.spark.SparkContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html "org.apache.spark.SparkContext") serves as the main entry point to Spark, while [org.apache.spark.rdd.RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") is the data type representing a distributed collection, and provides most parallel operations.
In addition, [org.apache.spark.rdd.PairRDDFunctions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html "org.apache.spark.rdd.PairRDDFunctions") contains operations available only on RDDs of key-value pairs, such as `groupByKey` and `join`; [org.apache.spark.rdd.DoubleRDDFunctions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/DoubleRDDFunctions.html "org.apache.spark.rdd.DoubleRDDFunctions") contains operations available only on RDDs of Doubles; and [org.apache.spark.rdd.SequenceFileRDDFunctions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/SequenceFileRDDFunctions.html "org.apache.spark.rdd.SequenceFileRDDFunctions") contains operations available on RDDs that can be saved as SequenceFiles. These operations are automatically available on any RDD of the right type (e.g. RDD[(Int, Int)] through implicit conversions.
Java programmers should reference the [org.apache.spark.api.java](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/index.html "org.apache.spark.api.java") package for Spark programming APIs in Java.
Classes and methods marked with  Experimental are user-facing features which have not been officially adopted by the Spark project. These are subject to change or removal in minor releases.
Classes and methods marked with  Developer API are intended for advanced users want to extend Spark through lower level interfaces. These are subject to changes or removal in minor releases.

Source
    [package.scala](https://github.com/apache/spark/tree/v4.1.2/core/src/main/scala/org/apache/spark/package.scala)
Linear Supertypes
AnyRef, Any
__ __
Ordering
  1. Alphabetic
  2. By Inheritance

Inherited

  1. spark
  2. AnyRef
  3. Any

  1. Hide All
  2. Show All

Visibility
  1. Public
  2. Protected

### Package Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/index.html "Permalink") package [api](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/index.html)
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/broadcast/index.html "Permalink") package [broadcast](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/broadcast/index.html "Spark's broadcast variables, used to broadcast immutable datasets to all nodes.")
Spark's broadcast variables, used to broadcast immutable datasets to all nodes.
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html "Permalink") package [graphx](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html "ALPHA COMPONENT GraphX is a graph processing framework built on top of Spark.")
ALPHA COMPONENT GraphX is a graph processing framework built on top of Spark.
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/input/index.html "Permalink") package [input](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/input/index.html)
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/index.html "Permalink") package [io](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/index.html "IO codecs used for compression.")
IO codecs used for compression.
IO codecs used for compression. See [org.apache.spark.io.CompressionCodec](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/CompressionCodec.html "org.apache.spark.io.CompressionCodec").
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/launcher/index.html "Permalink") package [launcher](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/launcher/index.html)
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/mapred/index.html "Permalink") package [mapred](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/mapred/index.html)
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/metrics/index.html "Permalink") package [metrics](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/metrics/index.html)
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/index.html "Permalink") package [ml](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/index.html "DataFrame-based machine learning APIs to let users quickly assemble and configure practical machine learning pipelines.")
DataFrame-based machine learning APIs to let users quickly assemble and configure practical machine learning pipelines.
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/mllib/index.html "Permalink") package [mllib](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/mllib/index.html "RDD-based machine learning APIs \(in maintenance mode\).")
RDD-based machine learning APIs (in maintenance mode).
RDD-based machine learning APIs (in maintenance mode).
The `spark.mllib` package is in maintenance mode as of the Spark 2.0.0 release to encourage migration to the DataFrame-based APIs under the [org.apache.spark.ml](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/index.html "org.apache.spark.ml") package. While in maintenance mode,
     * no new features in the RDD-based `spark.mllib` package will be accepted, unless they block implementing new features in the DataFrame-based `spark.ml` package;
     * bug fixes in the RDD-based APIs will still be accepted.
The developers will continue adding more features to the DataFrame-based APIs in the 2.x series to reach feature parity with the RDD-based APIs. And once we reach feature parity, this package will be deprecated.

See also

[SPARK-4591](https://issues.apache.org/jira/browse/SPARK-4591) to track the progress of feature parity
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/partial/index.html "Permalink") package [partial](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/partial/index.html "Support for approximate results.")
Support for approximate results.
Support for approximate results. This provides convenient api and also implementation for approximate calculation.

See also

[org.apache.spark.rdd.RDD.countApprox](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html#countApprox\(timeout:Long,confidence:Double\):org.apache.spark.partial.PartialResult\[org.apache.spark.partial.BoundedDouble\])
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/paths/index.html "Permalink") package [paths](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/paths/index.html)
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/index.html "Permalink") package [rdd](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/index.html "Provides several RDD implementations.")
Provides several RDD implementations.
Provides several RDD implementations. See [org.apache.spark.rdd.RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD").
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/resource/index.html "Permalink") package [resource](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/resource/index.html)
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/index.html "Permalink") package [scheduler](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/index.html "Spark's scheduling components.")
Spark's scheduling components.
Spark's scheduling components. This includes the `org.apache.spark.scheduler.DAGScheduler` and lower level `org.apache.spark.scheduler.TaskScheduler`.
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/security/index.html "Permalink") package [security](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/security/index.html)
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/index.html "Permalink") package [serializer](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/index.html "Pluggable serializers for RDD and shuffle data.")
Pluggable serializers for RDD and shuffle data.
Pluggable serializers for RDD and shuffle data.

See also

[org.apache.spark.serializer.Serializer](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/Serializer.html "org.apache.spark.serializer.Serializer")
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/shuffle/index.html "Permalink") package [shuffle](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/shuffle/index.html)
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html "Permalink") package [sql](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html "Allows the execution of relational queries, including those expressed in SQL using Spark.")
Allows the execution of relational queries, including those expressed in SQL using Spark.
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/status/index.html "Permalink") package [status](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/status/index.html)
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/index.html "Permalink") package [storage](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/index.html)
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/index.html "Permalink") package [streaming](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/index.html "Spark Streaming functionality.")
Spark Streaming functionality.
Spark Streaming functionality. [org.apache.spark.streaming.StreamingContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html "org.apache.spark.streaming.StreamingContext") serves as the main entry point to Spark Streaming, while [org.apache.spark.streaming.dstream.DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream") is the data type representing a continuous sequence of RDDs, representing a continuous stream of data.
In addition, [org.apache.spark.streaming.dstream.PairDStreamFunctions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html "org.apache.spark.streaming.dstream.PairDStreamFunctions") contains operations available only on DStreams of key-value pairs, such as `groupByKey` and `reduceByKey`. These operations are automatically available on any DStream of the right type (e.g. DStream[(Int, Int)] through implicit conversions.
For the Java API of Spark Streaming, take a look at the [org.apache.spark.streaming.api.java.JavaStreamingContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html "org.apache.spark.streaming.api.java.JavaStreamingContext") which serves as the entry point, and the [org.apache.spark.streaming.api.java.JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream") and the [org.apache.spark.streaming.api.java.JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream") which have the DStream functionality.
  23. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ui/index.html "Permalink") package [ui](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ui/index.html)
  24. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/unsafe/index.html "Permalink") package [unsafe](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/unsafe/index.html)
  25. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/index.html "Permalink") package [util](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/index.html "Spark utilities.")
Spark utilities.

### Type Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Aggregator.html "Permalink") case class [Aggregator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Aggregator.html ":: DeveloperApi :: A set of functions used to aggregate data.")[K, V, C](createCombiner: (V) => C, mergeValue: (C, V) => C, mergeCombiners: (C, C) => C) extends Product with Serializable
A set of functions used to aggregate data.
A set of functions used to aggregate data.

createCombiner

function to create the initial value of the aggregation.

mergeValue

function to merge a new value into the aggregation result.

mergeCombiners

function to merge outputs from multiple mergeValue function.

Annotations
     @DeveloperApi()
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/BarrierTaskContext.html "Permalink") class [BarrierTaskContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/BarrierTaskContext.html ":: Experimental :: A TaskContext with extra contextual info and tooling for tasks in a barrier stage.") extends [TaskContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskContext.html "org.apache.spark.TaskContext") with Logging
A [TaskContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskContext.html "org.apache.spark.TaskContext") with extra contextual info and tooling for tasks in a barrier stage.
A [TaskContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskContext.html "org.apache.spark.TaskContext") with extra contextual info and tooling for tasks in a barrier stage. Use [BarrierTaskContext#get](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/BarrierTaskContext$.html#get\(\):org.apache.spark.BarrierTaskContext) to obtain the barrier context for a running barrier task.

Annotations
     @Experimental() @Since("2.4.0")
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/BarrierTaskInfo.html "Permalink") class [BarrierTaskInfo](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/BarrierTaskInfo.html ":: Experimental :: Carries all task infos of a barrier task.") extends AnyRef
Carries all task infos of a barrier task.
Carries all task infos of a barrier task.

Annotations
     @Experimental() @Since("2.4.0")
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/BreakingChangeInfo.html "Permalink") class [BreakingChangeInfo](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/BreakingChangeInfo.html "Additional information if the error was caused by a breaking change.") extends AnyRef
Additional information if the error was caused by a breaking change.
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html "Permalink") class [ComplexFutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html "A FutureAction for actions that could trigger multiple Spark jobs.")[T] extends [FutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/FutureAction.html "org.apache.spark.FutureAction")[T]
A [FutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/FutureAction.html "org.apache.spark.FutureAction") for actions that could trigger multiple Spark jobs.
A [FutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/FutureAction.html "org.apache.spark.FutureAction") for actions that could trigger multiple Spark jobs. Examples include take, takeSample. Cancellation works by setting the cancelled flag to true and cancelling any pending jobs.

Annotations
     @DeveloperApi()
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Dependency.html "Permalink") abstract  class [Dependency](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Dependency.html ":: DeveloperApi :: Base class for dependencies.")[T] extends Serializable
Base class for dependencies.
Base class for dependencies.

Annotations
     @DeveloperApi()
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ErrorClassesJsonReader.html "Permalink") class [ErrorClassesJsonReader](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ErrorClassesJsonReader.html "A reader to load error information from one or more JSON files.") extends AnyRef
A reader to load error information from one or more JSON files.
A reader to load error information from one or more JSON files. Note that, if one error appears in more than one JSON files, the latter wins. Please read common/utils/src/main/resources/error/README.md for more details.

Annotations
     @DeveloperApi()
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ExceptionFailure.html "Permalink") case class [ExceptionFailure](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ExceptionFailure.html ":: DeveloperApi :: Task failed due to a runtime exception.")(className: String, description: String, stackTrace: Array[[StackTraceElement](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/StackTraceElement.html#java.lang.StackTraceElement "java.lang.StackTraceElement")], fullStackTrace: String, exceptionWrapper: Option[ThrowableSerializationWrapper], accumUpdates: Seq[[AccumulableInfo](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/AccumulableInfo.html "org.apache.spark.scheduler.AccumulableInfo")] = Seq.empty, accums: Seq[[AccumulatorV2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html "org.apache.spark.util.AccumulatorV2")[_, _]] = Nil, metricPeaks: Seq[Long] = Seq.empty) extends [TaskFailedReason](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskFailedReason.html "org.apache.spark.TaskFailedReason") with Product with Serializable
Task failed due to a runtime exception.
Task failed due to a runtime exception. This is the most common failure case and also captures user program exceptions.
`stackTrace` contains the stack trace of the exception itself. It still exists for backward compatibility. It's better to use `this(e: Throwable, metrics: Option[TaskMetrics])` to create `ExceptionFailure` as it will handle the backward compatibility properly.
`fullStackTrace` is a better representation of the stack trace because it contains the whole stack trace including the exception and its causes
`exception` is the actual exception that caused the task to fail. It may be `None` in the case that the exception is not in fact serializable. If a task fails more than once (due to retries), `exception` is that one that caused the last failure.

Annotations
     @DeveloperApi()
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ExecutorLostFailure.html "Permalink") case class [ExecutorLostFailure](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ExecutorLostFailure.html ":: DeveloperApi :: The task failed because the executor that it was running on was lost.")(execId: String, exitCausedByApp: Boolean = true, reason: Option[String]) extends [TaskFailedReason](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskFailedReason.html "org.apache.spark.TaskFailedReason") with Product with Serializable
The task failed because the executor that it was running on was lost.
The task failed because the executor that it was running on was lost. This may happen because the task crashed the JVM.

Annotations
     @DeveloperApi()
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/FetchFailed.html "Permalink") case class [FetchFailed](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/FetchFailed.html ":: DeveloperApi :: Task failed to fetch shuffle data from a remote node.")(bmAddress: [BlockManagerId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html "org.apache.spark.storage.BlockManagerId"), shuffleId: Int, mapId: Long, mapIndex: Int, reduceId: Int, message: String) extends [TaskFailedReason](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskFailedReason.html "org.apache.spark.TaskFailedReason") with Product with Serializable
Task failed to fetch shuffle data from a remote node.
Task failed to fetch shuffle data from a remote node. Probably means we have lost the remote executors the task is trying to fetch from, and thus need to rerun the previous stage.

Annotations
     @DeveloperApi()
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/FutureAction.html "Permalink") trait [FutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/FutureAction.html "A future for the result of an action to support cancellation.")[T] extends Future[T]
A future for the result of an action to support cancellation.
A future for the result of an action to support cancellation. This is an extension of the Scala Future interface to support cancellation.
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/HashPartitioner.html "Permalink") class [HashPartitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/HashPartitioner.html "A org.apache.spark.Partitioner that implements hash-based partitioning using Java's Object.hashCode.") extends [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner")
A [org.apache.spark.Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner") that implements hash-based partitioning using Java's `Object.hashCode`.
A [org.apache.spark.Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner") that implements hash-based partitioning using Java's `Object.hashCode`.
Java arrays have hashCodes that are based on the arrays' identities rather than their contents, so attempting to partition an RDD[Array[_]] or RDD[(Array[_], _)] using a HashPartitioner will produce an unexpected or incorrect result.
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/InterruptibleIterator.html "Permalink") class [InterruptibleIterator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/InterruptibleIterator.html ":: DeveloperApi :: An iterator that wraps around an existing iterator to provide task killing functionality.")[+T] extends Iterator[T]
An iterator that wraps around an existing iterator to provide task killing functionality.
An iterator that wraps around an existing iterator to provide task killing functionality. It works by checking the interrupted flag in [TaskContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskContext.html "org.apache.spark.TaskContext").

Annotations
     @DeveloperApi()
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/JobExecutionStatus.html "Permalink") sealed final  class [JobExecutionStatus](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/JobExecutionStatus.html) extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#java.lang.Enum "java.lang.Enum")[[JobExecutionStatus](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/JobExecutionStatus.html "org.apache.spark.JobExecutionStatus")]
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/JobSubmitter.html "Permalink") trait [JobSubmitter](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/JobSubmitter.html "Handle via which a "run" function passed to a ComplexFutureAction can submit jobs for execution.") extends AnyRef
Handle via which a "run" function passed to a [ComplexFutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html "org.apache.spark.ComplexFutureAction") can submit jobs for execution.
Handle via which a "run" function passed to a [ComplexFutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html "org.apache.spark.ComplexFutureAction") can submit jobs for execution.

Annotations
     @DeveloperApi()
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/MitigationConfig.html "Permalink") class [MitigationConfig](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/MitigationConfig.html "A spark config flag that can be used to mitigate a breaking change.") extends AnyRef
A spark config flag that can be used to mitigate a breaking change.
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/NarrowDependency.html "Permalink") abstract  class [NarrowDependency](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/NarrowDependency.html ":: DeveloperApi :: Base class for dependencies where each partition of the child RDD depends on a small number of partitions of the parent RDD.")[T] extends [Dependency](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Dependency.html "org.apache.spark.Dependency")[T]
Base class for dependencies where each partition of the child RDD depends on a small number of partitions of the parent RDD.
Base class for dependencies where each partition of the child RDD depends on a small number of partitions of the parent RDD. Narrow dependencies allow for pipelined execution.

Annotations
     @DeveloperApi()
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/OneToOneDependency.html "Permalink") class [OneToOneDependency](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/OneToOneDependency.html ":: DeveloperApi :: Represents a one-to-one dependency between partitions of the parent and child RDDs.")[T] extends [NarrowDependency](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/NarrowDependency.html "org.apache.spark.NarrowDependency")[T]
Represents a one-to-one dependency between partitions of the parent and child RDDs.
Represents a one-to-one dependency between partitions of the parent and child RDDs.

Annotations
     @DeveloperApi()
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partition.html "Permalink") trait [Partition](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partition.html "An identifier for a partition in an RDD.") extends Serializable
An identifier for a partition in an RDD.
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/PartitionEvaluator.html "Permalink") trait [PartitionEvaluator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/PartitionEvaluator.html "An evaluator for computing RDD partitions.")[T, U] extends AnyRef
An evaluator for computing RDD partitions.
An evaluator for computing RDD partitions. Spark serializes and sends [PartitionEvaluatorFactory](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/PartitionEvaluatorFactory.html "org.apache.spark.PartitionEvaluatorFactory") to executors, and then creates [PartitionEvaluator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/PartitionEvaluator.html "org.apache.spark.PartitionEvaluator") via the factory at the executor side.

Annotations
     @DeveloperApi() @Since("3.5.0")
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/PartitionEvaluatorFactory.html "Permalink") trait [PartitionEvaluatorFactory](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/PartitionEvaluatorFactory.html "A factory to create PartitionEvaluator.")[T, U] extends [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable")
A factory to create [PartitionEvaluator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/PartitionEvaluator.html "org.apache.spark.PartitionEvaluator").
A factory to create [PartitionEvaluator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/PartitionEvaluator.html "org.apache.spark.PartitionEvaluator"). Spark serializes and sends [PartitionEvaluatorFactory](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/PartitionEvaluatorFactory.html "org.apache.spark.PartitionEvaluatorFactory") to executors, and then creates [PartitionEvaluator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/PartitionEvaluator.html "org.apache.spark.PartitionEvaluator") via the factory at the executor side.

Annotations
     @DeveloperApi() @Since("3.5.0")
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "Permalink") abstract  class [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "An object that defines how the elements in a key-value pair RDD are partitioned by key.") extends Serializable
An object that defines how the elements in a key-value pair RDD are partitioned by key.
An object that defines how the elements in a key-value pair RDD are partitioned by key. Maps each key to a partition ID, from 0 to `numPartitions - 1`.
Note that, partitioner must be deterministic, i.e. it must return the same partition id given the same partition key.
  23. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/QueryContext.html "Permalink") trait [QueryContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/QueryContext.html "Query context of a SparkThrowable.") extends AnyRef
Query context of a `SparkThrowable[](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkThrowable.html "org.apache.spark.SparkThrowable")`.
Query context of a `SparkThrowable[](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkThrowable.html "org.apache.spark.SparkThrowable")`. It helps users understand where error occur while executing queries.

Annotations
     @Evolving()

Since

3.4.0
  24. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/QueryContextType.html "Permalink") sealed final  class [QueryContextType](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/QueryContextType.html "The type of QueryContext.") extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#java.lang.Enum "java.lang.Enum")[[QueryContextType](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/QueryContextType.html "org.apache.spark.QueryContextType")]
The type of `QueryContext[](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/QueryContext.html "org.apache.spark.QueryContext")`.
The type of `QueryContext[](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/QueryContext.html "org.apache.spark.QueryContext")`.

Annotations
     @Evolving()

Since

4.0.0
  25. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/RangeDependency.html "Permalink") class [RangeDependency](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/RangeDependency.html ":: DeveloperApi :: Represents a one-to-one dependency between ranges of partitions in the parent and child RDDs.")[T] extends [NarrowDependency](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/NarrowDependency.html "org.apache.spark.NarrowDependency")[T]
Represents a one-to-one dependency between ranges of partitions in the parent and child RDDs.
Represents a one-to-one dependency between ranges of partitions in the parent and child RDDs.

Annotations
     @DeveloperApi()
  26. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/RangePartitioner.html "Permalink") class [RangePartitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/RangePartitioner.html "A org.apache.spark.Partitioner that partitions sortable records by range into roughly equal ranges.")[K, V] extends [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner")
A [org.apache.spark.Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner") that partitions sortable records by range into roughly equal ranges.
A [org.apache.spark.Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner") that partitions sortable records by range into roughly equal ranges. The ranges are determined by sampling the content of the RDD passed in.

Note

The actual number of partitions created by the RangePartitioner might not be the same as the `partitions` parameter, in the case where the number of sampled records is less than the value of `partitions`.
  27. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html "Permalink") trait [ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html) extends AnyRef
  28. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SerializableWritable.html "Permalink") class [SerializableWritable](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SerializableWritable.html)[T <: Writable] extends [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable")

Annotations
     @DeveloperApi()
  29. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ShuffleDependency.html "Permalink") class [ShuffleDependency](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ShuffleDependency.html ":: DeveloperApi :: Represents a dependency on the output of a shuffle stage.")[K, V, C] extends [Dependency](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Dependency.html "org.apache.spark.Dependency")[Product2[K, V]] with Logging
Represents a dependency on the output of a shuffle stage.
Represents a dependency on the output of a shuffle stage. Note that in the case of shuffle, the RDD is transient since we don't need it on the executor side.

Annotations
     @DeveloperApi()
  30. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ShuffleStatusNotFoundException.html "Permalink") case class [ShuffleStatusNotFoundException](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ShuffleStatusNotFoundException.html)(shuffleId: Int, methodName: String) extends [SparkException](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkException.html "org.apache.spark.SparkException") with Product with Serializable
  31. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SimpleFutureAction.html "Permalink") class [SimpleFutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SimpleFutureAction.html "A FutureAction holding the result of an action that triggers a single job.")[T] extends [FutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/FutureAction.html "org.apache.spark.FutureAction")[T]
A [FutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/FutureAction.html "org.apache.spark.FutureAction") holding the result of an action that triggers a single job.
A [FutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/FutureAction.html "org.apache.spark.FutureAction") holding the result of an action that triggers a single job. Examples include count, collect, reduce.

Annotations
     @DeveloperApi()
  32. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html "Permalink") class [SparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html "Configuration for a Spark application.") extends [ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html "org.apache.spark.ReadOnlySparkConf") with Cloneable with Logging with Serializable
Configuration for a Spark application.
Configuration for a Spark application. Used to set various Spark parameters as key-value pairs.
Most of the time, you would create a SparkConf object with `new SparkConf()`, which will load values from any `spark.*` Java system properties set in your application as well. In this case, parameters you set directly on the `SparkConf` object take priority over system properties.
For unit tests, you can also call `new SparkConf(false)` to skip loading external settings and get the same configuration no matter what the system properties are.
All setter methods in this class support chaining. For example, you can write `new SparkConf().setMaster("local").setAppName("My app")`.

Note

Once a SparkConf object is passed to Spark, it is cloned and can no longer be modified by the user. Spark does not support modifying the configuration at runtime.
  33. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html "Permalink") class [SparkContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html "Main entry point for Spark functionality.") extends Logging
Main entry point for Spark functionality.
Main entry point for Spark functionality. A SparkContext represents the connection to a Spark cluster, and can be used to create RDDs, accumulators and broadcast variables on that cluster.

Note

Only one `SparkContext` should be active per JVM. You must `stop()` the active `SparkContext` before creating a new one.
  34. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkEnv.html "Permalink") class [SparkEnv](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkEnv.html ":: DeveloperApi :: Holds all the runtime environment objects for a running Spark instance \(either master or worker\), including the serializer, RpcEnv, block manager, map output tracker, etc.") extends Logging
Holds all the runtime environment objects for a running Spark instance (either master or worker), including the serializer, RpcEnv, block manager, map output tracker, etc.
Holds all the runtime environment objects for a running Spark instance (either master or worker), including the serializer, RpcEnv, block manager, map output tracker, etc. Currently Spark code finds the SparkEnv through a global variable, so all the threads can access the same SparkEnv. It can be accessed by SparkEnv.get (e.g. after creating a SparkContext).

Annotations
     @DeveloperApi()
  35. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkException.html "Permalink") class [SparkException](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkException.html) extends Exception with [SparkThrowable](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkThrowable.html "org.apache.spark.SparkThrowable")
  36. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkExecutorInfo.html "Permalink") trait [SparkExecutorInfo](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkExecutorInfo.html "Exposes information about Spark Executors.") extends [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable")
Exposes information about Spark Executors.
Exposes information about Spark Executors.
This interface is not designed to be implemented outside of Spark. We may add additional methods which may break binary compatibility with outside implementations.
  37. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkFirehoseListener.html "Permalink") class [SparkFirehoseListener](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkFirehoseListener.html "Class that allows users to receive all SparkListener events.") extends SparkListenerInterface
Class that allows users to receive all SparkListener events.
Class that allows users to receive all SparkListener events. Users should override the onEvent method.
This is a concrete Java class in order to ensure that we don't forget to update it when adding new methods to SparkListener: forgetting to add a method will result in a compilation error (if this was a concrete Scala class, default implementations of new event handlers would be inherited from the SparkListener trait).
Please note until Spark 3.1.0 this was missing the DevelopApi annotation, this needs to be taken into account if changing this API before a major release.

Annotations
     @DeveloperApi()
  38. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkJobInfo.html "Permalink") trait [SparkJobInfo](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkJobInfo.html "Exposes information about Spark Jobs.") extends [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable")
Exposes information about Spark Jobs.
Exposes information about Spark Jobs.
This interface is not designed to be implemented outside of Spark. We may add additional methods which may break binary compatibility with outside implementations.
  39. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkStageInfo.html "Permalink") trait [SparkStageInfo](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkStageInfo.html "Exposes information about Spark Stages.") extends [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable")
Exposes information about Spark Stages.
Exposes information about Spark Stages.
This interface is not designed to be implemented outside of Spark. We may add additional methods which may break binary compatibility with outside implementations.
  40. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkStatusTracker.html "Permalink") class [SparkStatusTracker](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkStatusTracker.html "Low-level status reporting APIs for monitoring job and stage progress.") extends AnyRef
Low-level status reporting APIs for monitoring job and stage progress.
Low-level status reporting APIs for monitoring job and stage progress.
These APIs intentionally provide very weak consistency semantics; consumers of these APIs should be prepared to handle empty / missing information. For example, a job's stage ids may be known but the status API may not have any information about the details of those stages, so `getStageInfo` could potentially return `None` for a valid stage id.
To limit memory usage, these APIs only provide information on recent jobs / stages. These APIs will provide information for the last `spark.ui.retainedStages` stages and `spark.ui.retainedJobs` jobs.
NOTE: this class's constructor should be considered private and may be subject to change.
  41. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkThrowable.html "Permalink") trait [SparkThrowable](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkThrowable.html "Interface mixed into Throwables thrown from Spark.") extends AnyRef
Interface mixed into Throwables thrown from Spark.
Interface mixed into Throwables thrown from Spark.
- For backwards compatibility, existing Throwable types can be thrown with an arbitrary error message with a null error class. See [SparkException](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkException.html "org.apache.spark.SparkException"). - To promote standardization, Throwables should be thrown with an error class and message parameters to construct an error message with SparkThrowableHelper.getMessage(). New Throwable types should not accept arbitrary error messages. See SparkArithmeticException.

Annotations
     @Evolving()

Since

3.2.0
  42. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/StringSubstitutor.html "Permalink") class [StringSubstitutor](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/StringSubstitutor.html) extends AnyRef
  43. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskCommitDenied.html "Permalink") case class [TaskCommitDenied](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskCommitDenied.html ":: DeveloperApi :: Task requested the driver to commit, but was denied.")(jobID: Int, partitionID: Int, attemptNumber: Int) extends [TaskFailedReason](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskFailedReason.html "org.apache.spark.TaskFailedReason") with Product with Serializable
Task requested the driver to commit, but was denied.
Task requested the driver to commit, but was denied.

Annotations
     @DeveloperApi()
  44. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskContext.html "Permalink") abstract  class [TaskContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskContext.html "Contextual information about a task which can be read or mutated during execution.") extends Serializable
Contextual information about a task which can be read or mutated during execution.
Contextual information about a task which can be read or mutated during execution. To access the TaskContext for a running task, use:

```
org.apache.spark.TaskContext.get()
```

  45. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskEndReason.html "Permalink") sealed  trait [TaskEndReason](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskEndReason.html ":: DeveloperApi :: Various possible reasons why a task ended.") extends AnyRef
Various possible reasons why a task ended.
Various possible reasons why a task ended. The low-level TaskScheduler is supposed to retry tasks several times for "ephemeral" failures, and only report back failures that require some old stages to be resubmitted, such as shuffle map fetch failures.

Annotations
     @DeveloperApi()
  46. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskFailedReason.html "Permalink") sealed  trait [TaskFailedReason](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskFailedReason.html ":: DeveloperApi :: Various possible reasons why a task failed.") extends [TaskEndReason](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskEndReason.html "org.apache.spark.TaskEndReason")
Various possible reasons why a task failed.
Various possible reasons why a task failed.

Annotations
     @DeveloperApi()
  47. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskKilled.html "Permalink") case class [TaskKilled](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskKilled.html ":: DeveloperApi :: Task was killed intentionally and needs to be rescheduled.")(reason: String, accumUpdates: Seq[[AccumulableInfo](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/AccumulableInfo.html "org.apache.spark.scheduler.AccumulableInfo")] = Seq.empty, accums: Seq[[AccumulatorV2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html "org.apache.spark.util.AccumulatorV2")[_, _]] = Nil, metricPeaks: Seq[Long] = Seq.empty) extends [TaskFailedReason](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskFailedReason.html "org.apache.spark.TaskFailedReason") with Product with Serializable
Task was killed intentionally and needs to be rescheduled.
Task was killed intentionally and needs to be rescheduled.

Annotations
     @DeveloperApi()
  48. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskKilledException.html "Permalink") class [TaskKilledException](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskKilledException.html ":: DeveloperApi :: Exception thrown when a task is explicitly killed \(i.e., task failure is expected\).") extends RuntimeException
Exception thrown when a task is explicitly killed (i.e., task failure is expected).
Exception thrown when a task is explicitly killed (i.e., task failure is expected).

Annotations
     @DeveloperApi()

### Deprecated Type Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html "Permalink") class [ContextAwareIterator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html ":: DeveloperApi :: A TaskContext aware iterator.")[+T] extends Iterator[T]
A TaskContext aware iterator.
A TaskContext aware iterator.
As the Python evaluation consumes the parent iterator in a separate thread, it could consume more data from the parent even after the task ends and the parent is closed. If an off-heap access exists in the parent iterator, it could cause segmentation fault which crashes the executor. Thus, we should use [ContextAwareIterator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html "org.apache.spark.ContextAwareIterator") to stop consuming after the task ends.

Annotations
     @DeveloperApi() @deprecated

Deprecated

_(Since version 4.0.0)_ Only usage for Python evaluation is now extinct

Since

3.1.0

### Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html#SPARK_BRANCH:String "Permalink") val SPARK_BRANCH: String
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html#SPARK_BUILD_DATE:String "Permalink") val SPARK_BUILD_DATE: String
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html#SPARK_BUILD_USER:String "Permalink") val SPARK_BUILD_USER: String
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html#SPARK_DOC_ROOT:String "Permalink") val SPARK_DOC_ROOT: String
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html#SPARK_REPO_URL:String "Permalink") val SPARK_REPO_URL: String
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html#SPARK_REVISION:String "Permalink") val SPARK_REVISION: String
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html#SPARK_VERSION:String "Permalink") val SPARK_VERSION: String
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html#SPARK_VERSION_SHORT:String "Permalink") val SPARK_VERSION_SHORT: String
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/BarrierTaskContext$.html "Permalink") object [BarrierTaskContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/BarrierTaskContext$.html) extends [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable")

Annotations
     @Experimental() @Since("2.4.0")
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner$.html "Permalink") object [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner$.html) extends [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable")
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Resubmitted$.html "Permalink") case object [Resubmitted](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Resubmitted$.html ":: DeveloperApi :: A org.apache.spark.scheduler.ShuffleMapTask that completed successfully earlier, but we lost the executor before the stage completed.") extends [TaskFailedReason](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskFailedReason.html "org.apache.spark.TaskFailedReason") with Product with Serializable
A `org.apache.spark.scheduler.ShuffleMapTask` that completed successfully earlier, but we lost the executor before the stage completed.
A `org.apache.spark.scheduler.ShuffleMapTask` that completed successfully earlier, but we lost the executor before the stage completed. This means Spark needs to reschedule the task to be re-executed on a different executor.

Annotations
     @DeveloperApi()
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ShuffleDependency$.html "Permalink") object [ShuffleDependency](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ShuffleDependency$.html) extends [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable")
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext$.html "Permalink") object [SparkContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext$.html "The SparkContext object contains a number of implicit conversions and parameters for use with various Spark features.") extends Logging
The SparkContext object contains a number of implicit conversions and parameters for use with various Spark features.
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkEnv$.html "Permalink") object [SparkEnv](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkEnv$.html) extends Logging
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkException$.html "Permalink") object [SparkException](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkException$.html) extends [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable")
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkFiles$.html "Permalink") object [SparkFiles](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkFiles$.html "Resolves paths to files added through SparkContext.addFile\(\).")
Resolves paths to files added through `SparkContext.addFile()`.
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Success$.html "Permalink") case object [Success](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Success$.html ":: DeveloperApi :: Task succeeded.") extends [TaskEndReason](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskEndReason.html "org.apache.spark.TaskEndReason") with Product with Serializable
Task succeeded.
Task succeeded.

Annotations
     @DeveloperApi()
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskContext$.html "Permalink") object [TaskContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskContext$.html) extends [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable")
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskResultLost$.html "Permalink") case object [TaskResultLost](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskResultLost$.html ":: DeveloperApi :: The task finished successfully, but the result was lost from the executor's block manager before it was fetched.") extends [TaskFailedReason](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskFailedReason.html "org.apache.spark.TaskFailedReason") with Product with Serializable
The task finished successfully, but the result was lost from the executor's block manager before it was fetched.
The task finished successfully, but the result was lost from the executor's block manager before it was fetched.

Annotations
     @DeveloperApi()
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/UnknownReason$.html "Permalink") case object [UnknownReason](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/UnknownReason$.html ":: DeveloperApi :: We don't know why the task ended -- for example, because of a ClassNotFound exception when deserializing the task result.") extends [TaskFailedReason](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskFailedReason.html "org.apache.spark.TaskFailedReason") with Product with Serializable
We don't know why the task ended -- for example, because of a ClassNotFound exception when deserializing the task result.
We don't know why the task ended -- for example, because of a ClassNotFound exception when deserializing the task result.

Annotations
     @DeveloperApi()
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/WritableConverter$.html "Permalink") object [WritableConverter](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/WritableConverter$.html) extends [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable")
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/WritableFactory$.html "Permalink") object [WritableFactory](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/WritableFactory$.html) extends [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable")

### Ungrouped
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Aggregator.html "Permalink") case class [Aggregator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Aggregator.html ":: DeveloperApi :: A set of functions used to aggregate data.")[K, V, C](createCombiner: (V) => C, mergeValue: (C, V) => C, mergeCombiners: (C, C) => C) extends Product with Serializable
A set of functions used to aggregate data.
A set of functions used to aggregate data.

createCombiner

function to create the initial value of the aggregation.

mergeValue

function to merge a new value into the aggregation result.

mergeCombiners

function to merge outputs from multiple mergeValue function.

Annotations
     @DeveloperApi()
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/BarrierTaskContext.html "Permalink") class [BarrierTaskContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/BarrierTaskContext.html ":: Experimental :: A TaskContext with extra contextual info and tooling for tasks in a barrier stage.") extends [TaskContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskContext.html "org.apache.spark.TaskContext") with Logging
A [TaskContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskContext.html "org.apache.spark.TaskContext") with extra contextual info and tooling for tasks in a barrier stage.
A [TaskContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskContext.html "org.apache.spark.TaskContext") with extra contextual info and tooling for tasks in a barrier stage. Use [BarrierTaskContext#get](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/BarrierTaskContext$.html#get\(\):org.apache.spark.BarrierTaskContext) to obtain the barrier context for a running barrier task.

Annotations
     @Experimental() @Since("2.4.0")
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/BarrierTaskInfo.html "Permalink") class [BarrierTaskInfo](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/BarrierTaskInfo.html ":: Experimental :: Carries all task infos of a barrier task.") extends AnyRef
Carries all task infos of a barrier task.
Carries all task infos of a barrier task.

Annotations
     @Experimental() @Since("2.4.0")
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/BreakingChangeInfo.html "Permalink") class [BreakingChangeInfo](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/BreakingChangeInfo.html "Additional information if the error was caused by a breaking change.") extends AnyRef
Additional information if the error was caused by a breaking change.
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html "Permalink") class [ComplexFutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html "A FutureAction for actions that could trigger multiple Spark jobs.")[T] extends [FutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/FutureAction.html "org.apache.spark.FutureAction")[T]
A [FutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/FutureAction.html "org.apache.spark.FutureAction") for actions that could trigger multiple Spark jobs.
A [FutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/FutureAction.html "org.apache.spark.FutureAction") for actions that could trigger multiple Spark jobs. Examples include take, takeSample. Cancellation works by setting the cancelled flag to true and cancelling any pending jobs.

Annotations
     @DeveloperApi()
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Dependency.html "Permalink") abstract  class [Dependency](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Dependency.html ":: DeveloperApi :: Base class for dependencies.")[T] extends Serializable
Base class for dependencies.
Base class for dependencies.

Annotations
     @DeveloperApi()
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ErrorClassesJsonReader.html "Permalink") class [ErrorClassesJsonReader](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ErrorClassesJsonReader.html "A reader to load error information from one or more JSON files.") extends AnyRef
A reader to load error information from one or more JSON files.
A reader to load error information from one or more JSON files. Note that, if one error appears in more than one JSON files, the latter wins. Please read common/utils/src/main/resources/error/README.md for more details.

Annotations
     @DeveloperApi()
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ExceptionFailure.html "Permalink") case class [ExceptionFailure](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ExceptionFailure.html ":: DeveloperApi :: Task failed due to a runtime exception.")(className: String, description: String, stackTrace: Array[[StackTraceElement](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/StackTraceElement.html#java.lang.StackTraceElement "java.lang.StackTraceElement")], fullStackTrace: String, exceptionWrapper: Option[ThrowableSerializationWrapper], accumUpdates: Seq[[AccumulableInfo](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/AccumulableInfo.html "org.apache.spark.scheduler.AccumulableInfo")] = Seq.empty, accums: Seq[[AccumulatorV2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html "org.apache.spark.util.AccumulatorV2")[_, _]] = Nil, metricPeaks: Seq[Long] = Seq.empty) extends [TaskFailedReason](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskFailedReason.html "org.apache.spark.TaskFailedReason") with Product with Serializable
Task failed due to a runtime exception.
Task failed due to a runtime exception. This is the most common failure case and also captures user program exceptions.
`stackTrace` contains the stack trace of the exception itself. It still exists for backward compatibility. It's better to use `this(e: Throwable, metrics: Option[TaskMetrics])` to create `ExceptionFailure` as it will handle the backward compatibility properly.
`fullStackTrace` is a better representation of the stack trace because it contains the whole stack trace including the exception and its causes
`exception` is the actual exception that caused the task to fail. It may be `None` in the case that the exception is not in fact serializable. If a task fails more than once (due to retries), `exception` is that one that caused the last failure.

Annotations
     @DeveloperApi()
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ExecutorLostFailure.html "Permalink") case class [ExecutorLostFailure](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ExecutorLostFailure.html ":: DeveloperApi :: The task failed because the executor that it was running on was lost.")(execId: String, exitCausedByApp: Boolean = true, reason: Option[String]) extends [TaskFailedReason](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskFailedReason.html "org.apache.spark.TaskFailedReason") with Product with Serializable
The task failed because the executor that it was running on was lost.
The task failed because the executor that it was running on was lost. This may happen because the task crashed the JVM.

Annotations
     @DeveloperApi()
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/FetchFailed.html "Permalink") case class [FetchFailed](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/FetchFailed.html ":: DeveloperApi :: Task failed to fetch shuffle data from a remote node.")(bmAddress: [BlockManagerId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html "org.apache.spark.storage.BlockManagerId"), shuffleId: Int, mapId: Long, mapIndex: Int, reduceId: Int, message: String) extends [TaskFailedReason](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskFailedReason.html "org.apache.spark.TaskFailedReason") with Product with Serializable
Task failed to fetch shuffle data from a remote node.
Task failed to fetch shuffle data from a remote node. Probably means we have lost the remote executors the task is trying to fetch from, and thus need to rerun the previous stage.

Annotations
     @DeveloperApi()
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/FutureAction.html "Permalink") trait [FutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/FutureAction.html "A future for the result of an action to support cancellation.")[T] extends Future[T]
A future for the result of an action to support cancellation.
A future for the result of an action to support cancellation. This is an extension of the Scala Future interface to support cancellation.
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/HashPartitioner.html "Permalink") class [HashPartitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/HashPartitioner.html "A org.apache.spark.Partitioner that implements hash-based partitioning using Java's Object.hashCode.") extends [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner")
A [org.apache.spark.Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner") that implements hash-based partitioning using Java's `Object.hashCode`.
A [org.apache.spark.Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner") that implements hash-based partitioning using Java's `Object.hashCode`.
Java arrays have hashCodes that are based on the arrays' identities rather than their contents, so attempting to partition an RDD[Array[_]] or RDD[(Array[_], _)] using a HashPartitioner will produce an unexpected or incorrect result.
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/InterruptibleIterator.html "Permalink") class [InterruptibleIterator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/InterruptibleIterator.html ":: DeveloperApi :: An iterator that wraps around an existing iterator to provide task killing functionality.")[+T] extends Iterator[T]
An iterator that wraps around an existing iterator to provide task killing functionality.
An iterator that wraps around an existing iterator to provide task killing functionality. It works by checking the interrupted flag in [TaskContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskContext.html "org.apache.spark.TaskContext").

Annotations
     @DeveloperApi()
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/JobExecutionStatus.html "Permalink") sealed final  class [JobExecutionStatus](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/JobExecutionStatus.html) extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#java.lang.Enum "java.lang.Enum")[[JobExecutionStatus](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/JobExecutionStatus.html "org.apache.spark.JobExecutionStatus")]
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/JobSubmitter.html "Permalink") trait [JobSubmitter](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/JobSubmitter.html "Handle via which a "run" function passed to a ComplexFutureAction can submit jobs for execution.") extends AnyRef
Handle via which a "run" function passed to a [ComplexFutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html "org.apache.spark.ComplexFutureAction") can submit jobs for execution.
Handle via which a "run" function passed to a [ComplexFutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html "org.apache.spark.ComplexFutureAction") can submit jobs for execution.

Annotations
     @DeveloperApi()
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/MitigationConfig.html "Permalink") class [MitigationConfig](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/MitigationConfig.html "A spark config flag that can be used to mitigate a breaking change.") extends AnyRef
A spark config flag that can be used to mitigate a breaking change.
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/NarrowDependency.html "Permalink") abstract  class [NarrowDependency](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/NarrowDependency.html ":: DeveloperApi :: Base class for dependencies where each partition of the child RDD depends on a small number of partitions of the parent RDD.")[T] extends [Dependency](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Dependency.html "org.apache.spark.Dependency")[T]
Base class for dependencies where each partition of the child RDD depends on a small number of partitions of the parent RDD.
Base class for dependencies where each partition of the child RDD depends on a small number of partitions of the parent RDD. Narrow dependencies allow for pipelined execution.

Annotations
     @DeveloperApi()
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/OneToOneDependency.html "Permalink") class [OneToOneDependency](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/OneToOneDependency.html ":: DeveloperApi :: Represents a one-to-one dependency between partitions of the parent and child RDDs.")[T] extends [NarrowDependency](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/NarrowDependency.html "org.apache.spark.NarrowDependency")[T]
Represents a one-to-one dependency between partitions of the parent and child RDDs.
Represents a one-to-one dependency between partitions of the parent and child RDDs.

Annotations
     @DeveloperApi()
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partition.html "Permalink") trait [Partition](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partition.html "An identifier for a partition in an RDD.") extends Serializable
An identifier for a partition in an RDD.
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/PartitionEvaluator.html "Permalink") trait [PartitionEvaluator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/PartitionEvaluator.html "An evaluator for computing RDD partitions.")[T, U] extends AnyRef
An evaluator for computing RDD partitions.
An evaluator for computing RDD partitions. Spark serializes and sends [PartitionEvaluatorFactory](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/PartitionEvaluatorFactory.html "org.apache.spark.PartitionEvaluatorFactory") to executors, and then creates [PartitionEvaluator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/PartitionEvaluator.html "org.apache.spark.PartitionEvaluator") via the factory at the executor side.

Annotations
     @DeveloperApi() @Since("3.5.0")
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/PartitionEvaluatorFactory.html "Permalink") trait [PartitionEvaluatorFactory](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/PartitionEvaluatorFactory.html "A factory to create PartitionEvaluator.")[T, U] extends [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable")
A factory to create [PartitionEvaluator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/PartitionEvaluator.html "org.apache.spark.PartitionEvaluator").
A factory to create [PartitionEvaluator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/PartitionEvaluator.html "org.apache.spark.PartitionEvaluator"). Spark serializes and sends [PartitionEvaluatorFactory](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/PartitionEvaluatorFactory.html "org.apache.spark.PartitionEvaluatorFactory") to executors, and then creates [PartitionEvaluator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/PartitionEvaluator.html "org.apache.spark.PartitionEvaluator") via the factory at the executor side.

Annotations
     @DeveloperApi() @Since("3.5.0")
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "Permalink") abstract  class [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "An object that defines how the elements in a key-value pair RDD are partitioned by key.") extends Serializable
An object that defines how the elements in a key-value pair RDD are partitioned by key.
An object that defines how the elements in a key-value pair RDD are partitioned by key. Maps each key to a partition ID, from 0 to `numPartitions - 1`.
Note that, partitioner must be deterministic, i.e. it must return the same partition id given the same partition key.
  23. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/QueryContext.html "Permalink") trait [QueryContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/QueryContext.html "Query context of a SparkThrowable.") extends AnyRef
Query context of a `SparkThrowable[](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkThrowable.html "org.apache.spark.SparkThrowable")`.
Query context of a `SparkThrowable[](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkThrowable.html "org.apache.spark.SparkThrowable")`. It helps users understand where error occur while executing queries.

Annotations
     @Evolving()

Since

3.4.0
  24. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/QueryContextType.html "Permalink") sealed final  class [QueryContextType](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/QueryContextType.html "The type of QueryContext.") extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#java.lang.Enum "java.lang.Enum")[[QueryContextType](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/QueryContextType.html "org.apache.spark.QueryContextType")]
The type of `QueryContext[](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/QueryContext.html "org.apache.spark.QueryContext")`.
The type of `QueryContext[](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/QueryContext.html "org.apache.spark.QueryContext")`.

Annotations
     @Evolving()

Since

4.0.0
  25. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/RangeDependency.html "Permalink") class [RangeDependency](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/RangeDependency.html ":: DeveloperApi :: Represents a one-to-one dependency between ranges of partitions in the parent and child RDDs.")[T] extends [NarrowDependency](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/NarrowDependency.html "org.apache.spark.NarrowDependency")[T]
Represents a one-to-one dependency between ranges of partitions in the parent and child RDDs.
Represents a one-to-one dependency between ranges of partitions in the parent and child RDDs.

Annotations
     @DeveloperApi()
  26. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/RangePartitioner.html "Permalink") class [RangePartitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/RangePartitioner.html "A org.apache.spark.Partitioner that partitions sortable records by range into roughly equal ranges.")[K, V] extends [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner")
A [org.apache.spark.Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner") that partitions sortable records by range into roughly equal ranges.
A [org.apache.spark.Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner") that partitions sortable records by range into roughly equal ranges. The ranges are determined by sampling the content of the RDD passed in.

Note

The actual number of partitions created by the RangePartitioner might not be the same as the `partitions` parameter, in the case where the number of sampled records is less than the value of `partitions`.
  27. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html "Permalink") trait [ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html) extends AnyRef
  28. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SerializableWritable.html "Permalink") class [SerializableWritable](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SerializableWritable.html)[T <: Writable] extends [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable")

Annotations
     @DeveloperApi()
  29. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ShuffleDependency.html "Permalink") class [ShuffleDependency](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ShuffleDependency.html ":: DeveloperApi :: Represents a dependency on the output of a shuffle stage.")[K, V, C] extends [Dependency](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Dependency.html "org.apache.spark.Dependency")[Product2[K, V]] with Logging
Represents a dependency on the output of a shuffle stage.
Represents a dependency on the output of a shuffle stage. Note that in the case of shuffle, the RDD is transient since we don't need it on the executor side.

Annotations
     @DeveloperApi()
  30. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ShuffleStatusNotFoundException.html "Permalink") case class [ShuffleStatusNotFoundException](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ShuffleStatusNotFoundException.html)(shuffleId: Int, methodName: String) extends [SparkException](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkException.html "org.apache.spark.SparkException") with Product with Serializable
  31. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SimpleFutureAction.html "Permalink") class [SimpleFutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SimpleFutureAction.html "A FutureAction holding the result of an action that triggers a single job.")[T] extends [FutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/FutureAction.html "org.apache.spark.FutureAction")[T]
A [FutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/FutureAction.html "org.apache.spark.FutureAction") holding the result of an action that triggers a single job.
A [FutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/FutureAction.html "org.apache.spark.FutureAction") holding the result of an action that triggers a single job. Examples include count, collect, reduce.

Annotations
     @DeveloperApi()
  32. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html "Permalink") class [SparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html "Configuration for a Spark application.") extends [ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html "org.apache.spark.ReadOnlySparkConf") with Cloneable with Logging with Serializable
Configuration for a Spark application.
Configuration for a Spark application. Used to set various Spark parameters as key-value pairs.
Most of the time, you would create a SparkConf object with `new SparkConf()`, which will load values from any `spark.*` Java system properties set in your application as well. In this case, parameters you set directly on the `SparkConf` object take priority over system properties.
For unit tests, you can also call `new SparkConf(false)` to skip loading external settings and get the same configuration no matter what the system properties are.
All setter methods in this class support chaining. For example, you can write `new SparkConf().setMaster("local").setAppName("My app")`.

Note

Once a SparkConf object is passed to Spark, it is cloned and can no longer be modified by the user. Spark does not support modifying the configuration at runtime.
  33. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html "Permalink") class [SparkContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html "Main entry point for Spark functionality.") extends Logging
Main entry point for Spark functionality.
Main entry point for Spark functionality. A SparkContext represents the connection to a Spark cluster, and can be used to create RDDs, accumulators and broadcast variables on that cluster.

Note

Only one `SparkContext` should be active per JVM. You must `stop()` the active `SparkContext` before creating a new one.
  34. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkEnv.html "Permalink") class [SparkEnv](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkEnv.html ":: DeveloperApi :: Holds all the runtime environment objects for a running Spark instance \(either master or worker\), including the serializer, RpcEnv, block manager, map output tracker, etc.") extends Logging
Holds all the runtime environment objects for a running Spark instance (either master or worker), including the serializer, RpcEnv, block manager, map output tracker, etc.
Holds all the runtime environment objects for a running Spark instance (either master or worker), including the serializer, RpcEnv, block manager, map output tracker, etc. Currently Spark code finds the SparkEnv through a global variable, so all the threads can access the same SparkEnv. It can be accessed by SparkEnv.get (e.g. after creating a SparkContext).

Annotations
     @DeveloperApi()
  35. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkException.html "Permalink") class [SparkException](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkException.html) extends Exception with [SparkThrowable](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkThrowable.html "org.apache.spark.SparkThrowable")
  36. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkExecutorInfo.html "Permalink") trait [SparkExecutorInfo](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkExecutorInfo.html "Exposes information about Spark Executors.") extends [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable")
Exposes information about Spark Executors.
Exposes information about Spark Executors.
This interface is not designed to be implemented outside of Spark. We may add additional methods which may break binary compatibility with outside implementations.
  37. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkFirehoseListener.html "Permalink") class [SparkFirehoseListener](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkFirehoseListener.html "Class that allows users to receive all SparkListener events.") extends SparkListenerInterface
Class that allows users to receive all SparkListener events.
Class that allows users to receive all SparkListener events. Users should override the onEvent method.
This is a concrete Java class in order to ensure that we don't forget to update it when adding new methods to SparkListener: forgetting to add a method will result in a compilation error (if this was a concrete Scala class, default implementations of new event handlers would be inherited from the SparkListener trait).
Please note until Spark 3.1.0 this was missing the DevelopApi annotation, this needs to be taken into account if changing this API before a major release.

Annotations
     @DeveloperApi()
  38. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkJobInfo.html "Permalink") trait [SparkJobInfo](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkJobInfo.html "Exposes information about Spark Jobs.") extends [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable")
Exposes information about Spark Jobs.
Exposes information about Spark Jobs.
This interface is not designed to be implemented outside of Spark. We may add additional methods which may break binary compatibility with outside implementations.
  39. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkStageInfo.html "Permalink") trait [SparkStageInfo](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkStageInfo.html "Exposes information about Spark Stages.") extends [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable")
Exposes information about Spark Stages.
Exposes information about Spark Stages.
This interface is not designed to be implemented outside of Spark. We may add additional methods which may break binary compatibility with outside implementations.
  40. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkStatusTracker.html "Permalink") class [SparkStatusTracker](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkStatusTracker.html "Low-level status reporting APIs for monitoring job and stage progress.") extends AnyRef
Low-level status reporting APIs for monitoring job and stage progress.
Low-level status reporting APIs for monitoring job and stage progress.
These APIs intentionally provide very weak consistency semantics; consumers of these APIs should be prepared to handle empty / missing information. For example, a job's stage ids may be known but the status API may not have any information about the details of those stages, so `getStageInfo` could potentially return `None` for a valid stage id.
To limit memory usage, these APIs only provide information on recent jobs / stages. These APIs will provide information for the last `spark.ui.retainedStages` stages and `spark.ui.retainedJobs` jobs.
NOTE: this class's constructor should be considered private and may be subject to change.
  41. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkThrowable.html "Permalink") trait [SparkThrowable](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkThrowable.html "Interface mixed into Throwables thrown from Spark.") extends AnyRef
Interface mixed into Throwables thrown from Spark.
Interface mixed into Throwables thrown from Spark.
- For backwards compatibility, existing Throwable types can be thrown with an arbitrary error message with a null error class. See [SparkException](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkException.html "org.apache.spark.SparkException"). - To promote standardization, Throwables should be thrown with an error class and message parameters to construct an error message with SparkThrowableHelper.getMessage(). New Throwable types should not accept arbitrary error messages. See SparkArithmeticException.

Annotations
     @Evolving()

Since

3.2.0
  42. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/StringSubstitutor.html "Permalink") class [StringSubstitutor](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/StringSubstitutor.html) extends AnyRef
  43. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskCommitDenied.html "Permalink") case class [TaskCommitDenied](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskCommitDenied.html ":: DeveloperApi :: Task requested the driver to commit, but was denied.")(jobID: Int, partitionID: Int, attemptNumber: Int) extends [TaskFailedReason](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskFailedReason.html "org.apache.spark.TaskFailedReason") with Product with Serializable
Task requested the driver to commit, but was denied.
Task requested the driver to commit, but was denied.

Annotations
     @DeveloperApi()
  44. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskContext.html "Permalink") abstract  class [TaskContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskContext.html "Contextual information about a task which can be read or mutated during execution.") extends Serializable
Contextual information about a task which can be read or mutated during execution.
Contextual information about a task which can be read or mutated during execution. To access the TaskContext for a running task, use:

```
org.apache.spark.TaskContext.get()
```

  45. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskEndReason.html "Permalink") sealed  trait [TaskEndReason](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskEndReason.html ":: DeveloperApi :: Various possible reasons why a task ended.") extends AnyRef
Various possible reasons why a task ended.
Various possible reasons why a task ended. The low-level TaskScheduler is supposed to retry tasks several times for "ephemeral" failures, and only report back failures that require some old stages to be resubmitted, such as shuffle map fetch failures.

Annotations
     @DeveloperApi()
  46. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskFailedReason.html "Permalink") sealed  trait [TaskFailedReason](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskFailedReason.html ":: DeveloperApi :: Various possible reasons why a task failed.") extends [TaskEndReason](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskEndReason.html "org.apache.spark.TaskEndReason")
Various possible reasons why a task failed.
Various possible reasons why a task failed.

Annotations
     @DeveloperApi()
  47. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskKilled.html "Permalink") case class [TaskKilled](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskKilled.html ":: DeveloperApi :: Task was killed intentionally and needs to be rescheduled.")(reason: String, accumUpdates: Seq[[AccumulableInfo](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/AccumulableInfo.html "org.apache.spark.scheduler.AccumulableInfo")] = Seq.empty, accums: Seq[[AccumulatorV2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html "org.apache.spark.util.AccumulatorV2")[_, _]] = Nil, metricPeaks: Seq[Long] = Seq.empty) extends [TaskFailedReason](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskFailedReason.html "org.apache.spark.TaskFailedReason") with Product with Serializable
Task was killed intentionally and needs to be rescheduled.
Task was killed intentionally and needs to be rescheduled.

Annotations
     @DeveloperApi()
  48. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskKilledException.html "Permalink") class [TaskKilledException](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskKilledException.html ":: DeveloperApi :: Exception thrown when a task is explicitly killed \(i.e., task failure is expected\).") extends RuntimeException
Exception thrown when a task is explicitly killed (i.e., task failure is expected).
Exception thrown when a task is explicitly killed (i.e., task failure is expected).

Annotations
     @DeveloperApi()
  49. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html "Permalink") class [ContextAwareIterator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html ":: DeveloperApi :: A TaskContext aware iterator.")[+T] extends Iterator[T]
A TaskContext aware iterator.
A TaskContext aware iterator.
As the Python evaluation consumes the parent iterator in a separate thread, it could consume more data from the parent even after the task ends and the parent is closed. If an off-heap access exists in the parent iterator, it could cause segmentation fault which crashes the executor. Thus, we should use [ContextAwareIterator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html "org.apache.spark.ContextAwareIterator") to stop consuming after the task ends.

Annotations
     @DeveloperApi() @deprecated

Deprecated

_(Since version 4.0.0)_ Only usage for Python evaluation is now extinct

Since

3.1.0

  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html#SPARK_BRANCH:String "Permalink") val SPARK_BRANCH: String
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html#SPARK_BUILD_DATE:String "Permalink") val SPARK_BUILD_DATE: String
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html#SPARK_BUILD_USER:String "Permalink") val SPARK_BUILD_USER: String
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html#SPARK_DOC_ROOT:String "Permalink") val SPARK_DOC_ROOT: String
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html#SPARK_REPO_URL:String "Permalink") val SPARK_REPO_URL: String
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html#SPARK_REVISION:String "Permalink") val SPARK_REVISION: String
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html#SPARK_VERSION:String "Permalink") val SPARK_VERSION: String
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html#SPARK_VERSION_SHORT:String "Permalink") val SPARK_VERSION_SHORT: String
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/BarrierTaskContext$.html "Permalink") object [BarrierTaskContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/BarrierTaskContext$.html) extends [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable")

Annotations
     @Experimental() @Since("2.4.0")
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner$.html "Permalink") object [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner$.html) extends [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable")
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Resubmitted$.html "Permalink") case object [Resubmitted](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Resubmitted$.html ":: DeveloperApi :: A org.apache.spark.scheduler.ShuffleMapTask that completed successfully earlier, but we lost the executor before the stage completed.") extends [TaskFailedReason](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskFailedReason.html "org.apache.spark.TaskFailedReason") with Product with Serializable
A `org.apache.spark.scheduler.ShuffleMapTask` that completed successfully earlier, but we lost the executor before the stage completed.
A `org.apache.spark.scheduler.ShuffleMapTask` that completed successfully earlier, but we lost the executor before the stage completed. This means Spark needs to reschedule the task to be re-executed on a different executor.

Annotations
     @DeveloperApi()
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ShuffleDependency$.html "Permalink") object [ShuffleDependency](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ShuffleDependency$.html) extends [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable")
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext$.html "Permalink") object [SparkContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext$.html "The SparkContext object contains a number of implicit conversions and parameters for use with various Spark features.") extends Logging
The SparkContext object contains a number of implicit conversions and parameters for use with various Spark features.
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkEnv$.html "Permalink") object [SparkEnv](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkEnv$.html) extends Logging
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkException$.html "Permalink") object [SparkException](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkException$.html) extends [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable")
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkFiles$.html "Permalink") object [SparkFiles](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkFiles$.html "Resolves paths to files added through SparkContext.addFile\(\).")
Resolves paths to files added through `SparkContext.addFile()`.
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Success$.html "Permalink") case object [Success](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Success$.html ":: DeveloperApi :: Task succeeded.") extends [TaskEndReason](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskEndReason.html "org.apache.spark.TaskEndReason") with Product with Serializable
Task succeeded.
Task succeeded.

Annotations
     @DeveloperApi()
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskContext$.html "Permalink") object [TaskContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskContext$.html) extends [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable")
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskResultLost$.html "Permalink") case object [TaskResultLost](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskResultLost$.html ":: DeveloperApi :: The task finished successfully, but the result was lost from the executor's block manager before it was fetched.") extends [TaskFailedReason](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskFailedReason.html "org.apache.spark.TaskFailedReason") with Product with Serializable
The task finished successfully, but the result was lost from the executor's block manager before it was fetched.
The task finished successfully, but the result was lost from the executor's block manager before it was fetched.

Annotations
     @DeveloperApi()
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/UnknownReason$.html "Permalink") case object [UnknownReason](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/UnknownReason$.html ":: DeveloperApi :: We don't know why the task ended -- for example, because of a ClassNotFound exception when deserializing the task result.") extends [TaskFailedReason](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskFailedReason.html "org.apache.spark.TaskFailedReason") with Product with Serializable
We don't know why the task ended -- for example, because of a ClassNotFound exception when deserializing the task result.
We don't know why the task ended -- for example, because of a ClassNotFound exception when deserializing the task result.

Annotations
     @DeveloperApi()
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/WritableConverter$.html "Permalink") object [WritableConverter](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/WritableConverter$.html) extends [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable")
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/WritableFactory$.html "Permalink") object [WritableFactory](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/WritableFactory$.html) extends [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable")
