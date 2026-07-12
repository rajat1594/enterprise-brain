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
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "Permalink") package [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "Core Spark functionality.")
Core Spark functionality.
Core Spark functionality. [org.apache.spark.SparkContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html "org.apache.spark.SparkContext") serves as the main entry point to Spark, while [org.apache.spark.rdd.RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") is the data type representing a distributed collection, and provides most parallel operations.
In addition, [org.apache.spark.rdd.PairRDDFunctions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html "org.apache.spark.rdd.PairRDDFunctions") contains operations available only on RDDs of key-value pairs, such as `groupByKey` and `join`; [org.apache.spark.rdd.DoubleRDDFunctions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/DoubleRDDFunctions.html "org.apache.spark.rdd.DoubleRDDFunctions") contains operations available only on RDDs of Doubles; and [org.apache.spark.rdd.SequenceFileRDDFunctions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/SequenceFileRDDFunctions.html "org.apache.spark.rdd.SequenceFileRDDFunctions") contains operations available on RDDs that can be saved as SequenceFiles. These operations are automatically available on any RDD of the right type (e.g. RDD[(Int, Int)] through implicit conversions.
Java programmers should reference the [org.apache.spark.api.java](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/index.html "org.apache.spark.api.java") package for Spark programming APIs in Java.
Classes and methods marked with  Experimental are user-facing features which have not been officially adopted by the Spark project. These are subject to change or removal in minor releases.
Classes and methods marked with  Developer API are intended for advanced users want to extend Spark through lower level interfaces. These are subject to changes or removal in minor releases.

Definition Classes
    [apache](https://spark.apache.org/docs/latest/api/scala/org/apache/index.html "org.apache")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/index.html "Permalink") package [api](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/index.html)

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/broadcast/index.html "Permalink") package [broadcast](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/broadcast/index.html "Spark's broadcast variables, used to broadcast immutable datasets to all nodes.")
Spark's broadcast variables, used to broadcast immutable datasets to all nodes.
Spark's broadcast variables, used to broadcast immutable datasets to all nodes.

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html "Permalink") package [graphx](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html "ALPHA COMPONENT GraphX is a graph processing framework built on top of Spark.")
ALPHA COMPONENT GraphX is a graph processing framework built on top of Spark.
ALPHA COMPONENT GraphX is a graph processing framework built on top of Spark.

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/input/index.html "Permalink") package [input](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/input/index.html)

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/index.html "Permalink") package [io](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/index.html "IO codecs used for compression.")
IO codecs used for compression.
IO codecs used for compression. See [org.apache.spark.io.CompressionCodec](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/CompressionCodec.html "org.apache.spark.io.CompressionCodec").

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/launcher/index.html "Permalink") package [launcher](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/launcher/index.html)

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/mapred/index.html "Permalink") package [mapred](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/mapred/index.html)

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/metrics/index.html "Permalink") package [metrics](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/metrics/index.html)

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/index.html "Permalink") package [ml](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/index.html "DataFrame-based machine learning APIs to let users quickly assemble and configure practical machine learning pipelines.")
DataFrame-based machine learning APIs to let users quickly assemble and configure practical machine learning pipelines.
DataFrame-based machine learning APIs to let users quickly assemble and configure practical machine learning pipelines.

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/mllib/index.html "Permalink") package [mllib](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/mllib/index.html "RDD-based machine learning APIs \(in maintenance mode\).")
RDD-based machine learning APIs (in maintenance mode).
RDD-based machine learning APIs (in maintenance mode).
The `spark.mllib` package is in maintenance mode as of the Spark 2.0.0 release to encourage migration to the DataFrame-based APIs under the [org.apache.spark.ml](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/index.html "org.apache.spark.ml") package. While in maintenance mode,
    * no new features in the RDD-based `spark.mllib` package will be accepted, unless they block implementing new features in the DataFrame-based `spark.ml` package;
    * bug fixes in the RDD-based APIs will still be accepted.
The developers will continue adding more features to the DataFrame-based APIs in the 2.x series to reach feature parity with the RDD-based APIs. And once we reach feature parity, this package will be deprecated.

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")

See also

[SPARK-4591](https://issues.apache.org/jira/browse/SPARK-4591) to track the progress of feature parity
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/partial/index.html "Permalink") package [partial](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/partial/index.html "Support for approximate results.")
Support for approximate results.
Support for approximate results. This provides convenient api and also implementation for approximate calculation.

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")

See also

[org.apache.spark.rdd.RDD.countApprox](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html#countApprox\(timeout:Long,confidence:Double\):org.apache.spark.partial.PartialResult\[org.apache.spark.partial.BoundedDouble\])
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/paths/index.html "Permalink") package [paths](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/paths/index.html)

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/index.html "Permalink") package [rdd](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/index.html "Provides several RDD implementations.")
Provides several RDD implementations.
Provides several RDD implementations. See [org.apache.spark.rdd.RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD").

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/resource/index.html "Permalink") package [resource](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/resource/index.html)

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/index.html "Permalink") package [scheduler](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/index.html "Spark's scheduling components.")
Spark's scheduling components.
Spark's scheduling components. This includes the `org.apache.spark.scheduler.DAGScheduler` and lower level `org.apache.spark.scheduler.TaskScheduler`.

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/security/index.html "Permalink") package [security](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/security/index.html)

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/index.html "Permalink") package [serializer](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/index.html "Pluggable serializers for RDD and shuffle data.")
Pluggable serializers for RDD and shuffle data.
Pluggable serializers for RDD and shuffle data.

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")

See also

[org.apache.spark.serializer.Serializer](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/Serializer.html "org.apache.spark.serializer.Serializer")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/shuffle/index.html "Permalink") package [shuffle](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/shuffle/index.html)

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html "Permalink") package [sql](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html "Allows the execution of relational queries, including those expressed in SQL using Spark.")
Allows the execution of relational queries, including those expressed in SQL using Spark.
Allows the execution of relational queries, including those expressed in SQL using Spark.

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/status/index.html "Permalink") package [status](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/status/index.html)

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/index.html "Permalink") package [storage](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/index.html)

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/index.html "Permalink") package [streaming](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/index.html "Spark Streaming functionality.")
Spark Streaming functionality.
Spark Streaming functionality. [org.apache.spark.streaming.StreamingContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html "org.apache.spark.streaming.StreamingContext") serves as the main entry point to Spark Streaming, while [org.apache.spark.streaming.dstream.DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream") is the data type representing a continuous sequence of RDDs, representing a continuous stream of data.
In addition, [org.apache.spark.streaming.dstream.PairDStreamFunctions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html "org.apache.spark.streaming.dstream.PairDStreamFunctions") contains operations available only on DStreams of key-value pairs, such as `groupByKey` and `reduceByKey`. These operations are automatically available on any DStream of the right type (e.g. DStream[(Int, Int)] through implicit conversions.
For the Java API of Spark Streaming, take a look at the [org.apache.spark.streaming.api.java.JavaStreamingContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html "org.apache.spark.streaming.api.java.JavaStreamingContext") which serves as the entry point, and the [org.apache.spark.streaming.api.java.JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream") and the [org.apache.spark.streaming.api.java.JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream") which have the DStream functionality.

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ui/index.html "Permalink") package [ui](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ui/index.html)

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/unsafe/index.html "Permalink") package [unsafe](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/unsafe/index.html)

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/index.html "Permalink") package [util](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/index.html "Spark utilities.")
Spark utilities.
Spark utilities.

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
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

c
[org](https://spark.apache.org/docs/latest/api/scala/org/index.html "org").[apache](https://spark.apache.org/docs/latest/api/scala/org/apache/index.html "org.apache").[spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
# ComplexFutureAction[ __](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html "Permalink")
####  class ComplexFutureAction[T] extends [FutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/FutureAction.html "org.apache.spark.FutureAction")[T]
Developer API
A [FutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/FutureAction.html "org.apache.spark.FutureAction") for actions that could trigger multiple Spark jobs. Examples include take, takeSample. Cancellation works by setting the cancelled flag to true and cancelling any pending jobs.

Self Type
     [ComplexFutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html "org.apache.spark.ComplexFutureAction")[T]

Annotations
     @DeveloperApi()

Source
    [FutureAction.scala](https://github.com/apache/spark/tree/v4.1.2/core/src/main/scala/org/apache/spark/FutureAction.scala)
Linear Supertypes
[FutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/FutureAction.html "org.apache.spark.FutureAction")[T], Future[T], Awaitable[T], AnyRef, Any
__ __
Ordering
  1. Alphabetic
  2. By Inheritance

Inherited

  1. ComplexFutureAction
  2. FutureAction
  3. Future
  4. Awaitable
  5. AnyRef
  6. Any

  1. Hide All
  2. Show All

Visibility
  1. Public
  2. Protected

### Instance Constructors
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#<init>\(run:org.apache.spark.JobSubmitter=>scala.concurrent.Future\[T\]\):org.apache.spark.ComplexFutureAction\[T\] "Permalink") new ComplexFutureAction(run: ([JobSubmitter](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/JobSubmitter.html "org.apache.spark.JobSubmitter")) => Future[T])

### Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html###:Int "Permalink") final  def ##: Int

Definition Classes
    AnyRef → Any
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#andThen\[U\]\(pf:PartialFunction\[scala.util.Try\[T\],U\]\)\(implicitexecutor:scala.concurrent.ExecutionContext\):scala.concurrent.Future\[T\] "Permalink") def andThen[U](pf: PartialFunction[Try[T], U])(implicit executor: ExecutionContext): Future[T]

Definition Classes
    Future
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0

Definition Classes
    Any
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#cancel\(reason:Option\[String\]\):Unit "Permalink") def cancel(reason: Option[String]): Unit
Cancels the execution of this action with an optional reason.
Cancels the execution of this action with an optional reason.

Definition Classes
     [ComplexFutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html "org.apache.spark.ComplexFutureAction") → [FutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/FutureAction.html "org.apache.spark.FutureAction")
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#cancel\(\):Unit "Permalink") def cancel(): Unit
Cancels the execution of this action.
Cancels the execution of this action.

Definition Classes
    [FutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/FutureAction.html "org.apache.spark.FutureAction")
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#clone\(\):Object "Permalink") def clone(): AnyRef

Attributes
    protected[lang]

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#collect\[S\]\(pf:PartialFunction\[T,S\]\)\(implicitexecutor:scala.concurrent.ExecutionContext\):scala.concurrent.Future\[S\] "Permalink") def collect[S](pf: PartialFunction[T, S])(implicit executor: ExecutionContext): Future[S]

Definition Classes
    Future
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#equals\(x$1:Object\):Boolean "Permalink") def equals(arg0: AnyRef): Boolean

Definition Classes
    AnyRef → Any
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#failed:scala.concurrent.Future\[Throwable\] "Permalink") def failed: Future[Throwable]

Definition Classes
    Future
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#fallbackTo\[U>:T\]\(that:scala.concurrent.Future\[U\]\):scala.concurrent.Future\[U\] "Permalink") def fallbackTo[U >: T](that: Future[U]): Future[U]

Definition Classes
    Future
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#filter\(p:T=>Boolean\)\(implicitexecutor:scala.concurrent.ExecutionContext\):scala.concurrent.Future\[T\] "Permalink") def filter(p: (T) => Boolean)(implicit executor: ExecutionContext): Future[T]

Definition Classes
    Future
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#flatMap\[S\]\(f:T=>scala.concurrent.Future\[S\]\)\(implicitexecutor:scala.concurrent.ExecutionContext\):scala.concurrent.Future\[S\] "Permalink") def flatMap[S](f: (T) => Future[S])(implicit executor: ExecutionContext): Future[S]

Definition Classes
    Future
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#flatten\[S\]\(implicitev:T<:<scala.concurrent.Future\[S\]\):scala.concurrent.Future\[S\] "Permalink") def flatten[S](implicit ev: <:<[T, Future[S]]): Future[S]

Definition Classes
    Future
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#foreach\[U\]\(f:T=>U\)\(implicitexecutor:scala.concurrent.ExecutionContext\):Unit "Permalink") def foreach[U](f: (T) => U)(implicit executor: ExecutionContext): Unit

Definition Classes
    Future
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#get\(\):T "Permalink") def get(): T
Blocks and returns the result of this job.
Blocks and returns the result of this job.

Definition Classes
    [FutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/FutureAction.html "org.apache.spark.FutureAction")

Annotations
     @throws(classOf[SparkException])
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef]

Definition Classes
    AnyRef → Any

Annotations
     @IntrinsicCandidate() @native()
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#hashCode\(\):Int "Permalink") def hashCode(): Int

Definition Classes
    AnyRef → Any

Annotations
     @IntrinsicCandidate() @native()
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#isCancelled:Boolean "Permalink") def isCancelled: Boolean
Returns whether the action has been cancelled.
Returns whether the action has been cancelled.

Definition Classes
     [ComplexFutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html "org.apache.spark.ComplexFutureAction") → [FutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/FutureAction.html "org.apache.spark.FutureAction")
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#isCompleted:Boolean "Permalink") def isCompleted: Boolean
Returns whether the action has already been completed with a value or an exception.
Returns whether the action has already been completed with a value or an exception.

Definition Classes
     [ComplexFutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html "org.apache.spark.ComplexFutureAction") → [FutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/FutureAction.html "org.apache.spark.FutureAction") → Future
  23. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean

Definition Classes
    Any
  24. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#jobIds:Seq\[Int\] "Permalink") def jobIds: Seq[Int]
Returns the job IDs run by the underlying async operation.
Returns the job IDs run by the underlying async operation.
This returns the current snapshot of the job list. Certain operations may run multiple jobs, so multiple calls to this method may return different lists.

Definition Classes
     [ComplexFutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html "org.apache.spark.ComplexFutureAction") → [FutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/FutureAction.html "org.apache.spark.FutureAction")
  25. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#map\[S\]\(f:T=>S\)\(implicitexecutor:scala.concurrent.ExecutionContext\):scala.concurrent.Future\[S\] "Permalink") def map[S](f: (T) => S)(implicit executor: ExecutionContext): Future[S]

Definition Classes
    Future
  26. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#mapTo\[S\]\(implicittag:scala.reflect.ClassTag\[S\]\):scala.concurrent.Future\[S\] "Permalink") def mapTo[S](implicit tag: ClassTag[S]): Future[S]

Definition Classes
    Future
  27. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  28. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#notify\(\):Unit "Permalink") final  def notify(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  29. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  30. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#onComplete\[U\]\(func:scala.util.Try\[T\]=>U\)\(implicitexecutor:scala.concurrent.ExecutionContext\):Unit "Permalink") def onComplete[U](func: (Try[T]) => U)(implicit executor: ExecutionContext): Unit
When this action is completed, either through an exception, or a value, applies the provided function.
When this action is completed, either through an exception, or a value, applies the provided function.

Definition Classes
     [ComplexFutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html "org.apache.spark.ComplexFutureAction") → [FutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/FutureAction.html "org.apache.spark.FutureAction") → Future
  31. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#ready\(atMost:scala.concurrent.duration.Duration\)\(implicitpermit:scala.concurrent.CanAwait\):ComplexFutureAction.this.type "Permalink") def ready(atMost: Duration)(implicit permit: CanAwait): [ComplexFutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html "org.apache.spark.ComplexFutureAction").this.type
Blocks until this action completes.
Blocks until this action completes.

atMost

maximum wait time, which may be negative (no waiting is done), Duration.Inf for unbounded waiting, or a finite positive duration

returns

this FutureAction

Definition Classes
     [ComplexFutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html "org.apache.spark.ComplexFutureAction") → [FutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/FutureAction.html "org.apache.spark.FutureAction") → Awaitable

Annotations
     @throws(classOf[InterruptedException]) @throws(classOf[scala.concurrent.TimeoutException])
  32. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#recover\[U>:T\]\(pf:PartialFunction\[Throwable,U\]\)\(implicitexecutor:scala.concurrent.ExecutionContext\):scala.concurrent.Future\[U\] "Permalink") def recover[U >: T](pf: PartialFunction[Throwable, U])(implicit executor: ExecutionContext): Future[U]

Definition Classes
    Future
  33. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#recoverWith\[U>:T\]\(pf:PartialFunction\[Throwable,scala.concurrent.Future\[U\]\]\)\(implicitexecutor:scala.concurrent.ExecutionContext\):scala.concurrent.Future\[U\] "Permalink") def recoverWith[U >: T](pf: PartialFunction[Throwable, Future[U]])(implicit executor: ExecutionContext): Future[U]

Definition Classes
    Future
  34. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#result\(atMost:scala.concurrent.duration.Duration\)\(implicitpermit:scala.concurrent.CanAwait\):T "Permalink") def result(atMost: Duration)(implicit permit: CanAwait): T
Awaits and returns the result (of type T) of this action.
Awaits and returns the result (of type T) of this action.

atMost

maximum wait time, which may be negative (no waiting is done), Duration.Inf for unbounded waiting, or a finite positive duration

returns

the result value if the action is completed within the specific maximum wait time

Definition Classes
     [ComplexFutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html "org.apache.spark.ComplexFutureAction") → [FutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/FutureAction.html "org.apache.spark.FutureAction") → Awaitable

Annotations
     @throws(classOf[Exception])

Exceptions thrown

`Exception` exception during action execution
  35. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0

Definition Classes
    AnyRef
  36. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#toString\(\):String "Permalink") def toString(): [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String")

Definition Classes
    AnyRef → Any
  37. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#transform\[S\]\(f:scala.util.Try\[T\]=>scala.util.Try\[S\]\)\(implicite:scala.concurrent.ExecutionContext\):scala.concurrent.Future\[S\] "Permalink") def transform[S](f: (Try[T]) => Try[S])(implicit e: ExecutionContext): Future[S]

Definition Classes
     [ComplexFutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html "org.apache.spark.ComplexFutureAction") → Future
  38. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#transform\[S\]\(s:T=>S,f:Throwable=>Throwable\)\(implicitexecutor:scala.concurrent.ExecutionContext\):scala.concurrent.Future\[S\] "Permalink") def transform[S](s: (T) => S, f: (Throwable) => Throwable)(implicit executor: ExecutionContext): Future[S]

Definition Classes
    Future
  39. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#transformWith\[S\]\(f:scala.util.Try\[T\]=>scala.concurrent.Future\[S\]\)\(implicite:scala.concurrent.ExecutionContext\):scala.concurrent.Future\[S\] "Permalink") def transformWith[S](f: (Try[T]) => Future[S])(implicit e: ExecutionContext): Future[S]

Definition Classes
     [ComplexFutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html "org.apache.spark.ComplexFutureAction") → Future
  40. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#value:Option\[scala.util.Try\[T\]\] "Permalink") def value: Option[Try[T]]
The value of this Future.
The value of this Future.
If the future is not completed the returned value will be None. If the future is completed the value will be Some(Success(t)) if it contains a valid result, or Some(Failure(error)) if it contains an exception.

Definition Classes
     [ComplexFutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html "org.apache.spark.ComplexFutureAction") → [FutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/FutureAction.html "org.apache.spark.FutureAction") → Future
  41. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])
  42. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  43. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#wait\(\):Unit "Permalink") final  def wait(): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])
  44. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#withFilter\(p:T=>Boolean\)\(implicitexecutor:scala.concurrent.ExecutionContext\):scala.concurrent.Future\[T\] "Permalink") final  def withFilter(p: (T) => Boolean)(implicit executor: ExecutionContext): Future[T]

Definition Classes
    Future
  45. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#zip\[U\]\(that:scala.concurrent.Future\[U\]\):scala.concurrent.Future\[\(T,U\)\] "Permalink") def zip[U](that: Future[U]): Future[(T, U)]

Definition Classes
    Future
  46. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#zipWith\[U,R\]\(that:scala.concurrent.Future\[U\]\)\(f:\(T,U\)=>R\)\(implicitexecutor:scala.concurrent.ExecutionContext\):scala.concurrent.Future\[R\] "Permalink") def zipWith[U, R](that: Future[U])(f: (T, U) => R)(implicit executor: ExecutionContext): Future[R]

Definition Classes
    Future

### Deprecated Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#finalize\(\):Unit "Permalink") def finalize(): Unit

Attributes
    protected[lang]

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.Throwable]) @Deprecated

Deprecated

_(Since version 9)_

### Inherited from [FutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/FutureAction.html "org.apache.spark.FutureAction")[T]
### Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#cancel\(\):Unit "Permalink") def cancel(): Unit
Cancels the execution of this action.
Cancels the execution of this action.

Definition Classes
    [FutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/FutureAction.html "org.apache.spark.FutureAction")
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#get\(\):T "Permalink") def get(): T
Blocks and returns the result of this job.
Blocks and returns the result of this job.

Definition Classes
    [FutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/FutureAction.html "org.apache.spark.FutureAction")

Annotations
     @throws(classOf[SparkException])

### Inherited from Future[T]
### Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#andThen\[U\]\(pf:PartialFunction\[scala.util.Try\[T\],U\]\)\(implicitexecutor:scala.concurrent.ExecutionContext\):scala.concurrent.Future\[T\] "Permalink") def andThen[U](pf: PartialFunction[Try[T], U])(implicit executor: ExecutionContext): Future[T]

Definition Classes
    Future
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#collect\[S\]\(pf:PartialFunction\[T,S\]\)\(implicitexecutor:scala.concurrent.ExecutionContext\):scala.concurrent.Future\[S\] "Permalink") def collect[S](pf: PartialFunction[T, S])(implicit executor: ExecutionContext): Future[S]

Definition Classes
    Future
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#failed:scala.concurrent.Future\[Throwable\] "Permalink") def failed: Future[Throwable]

Definition Classes
    Future
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#fallbackTo\[U>:T\]\(that:scala.concurrent.Future\[U\]\):scala.concurrent.Future\[U\] "Permalink") def fallbackTo[U >: T](that: Future[U]): Future[U]

Definition Classes
    Future
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#filter\(p:T=>Boolean\)\(implicitexecutor:scala.concurrent.ExecutionContext\):scala.concurrent.Future\[T\] "Permalink") def filter(p: (T) => Boolean)(implicit executor: ExecutionContext): Future[T]

Definition Classes
    Future
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#flatMap\[S\]\(f:T=>scala.concurrent.Future\[S\]\)\(implicitexecutor:scala.concurrent.ExecutionContext\):scala.concurrent.Future\[S\] "Permalink") def flatMap[S](f: (T) => Future[S])(implicit executor: ExecutionContext): Future[S]

Definition Classes
    Future
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#flatten\[S\]\(implicitev:T<:<scala.concurrent.Future\[S\]\):scala.concurrent.Future\[S\] "Permalink") def flatten[S](implicit ev: <:<[T, Future[S]]): Future[S]

Definition Classes
    Future
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#foreach\[U\]\(f:T=>U\)\(implicitexecutor:scala.concurrent.ExecutionContext\):Unit "Permalink") def foreach[U](f: (T) => U)(implicit executor: ExecutionContext): Unit

Definition Classes
    Future
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#map\[S\]\(f:T=>S\)\(implicitexecutor:scala.concurrent.ExecutionContext\):scala.concurrent.Future\[S\] "Permalink") def map[S](f: (T) => S)(implicit executor: ExecutionContext): Future[S]

Definition Classes
    Future
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#mapTo\[S\]\(implicittag:scala.reflect.ClassTag\[S\]\):scala.concurrent.Future\[S\] "Permalink") def mapTo[S](implicit tag: ClassTag[S]): Future[S]

Definition Classes
    Future
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#recover\[U>:T\]\(pf:PartialFunction\[Throwable,U\]\)\(implicitexecutor:scala.concurrent.ExecutionContext\):scala.concurrent.Future\[U\] "Permalink") def recover[U >: T](pf: PartialFunction[Throwable, U])(implicit executor: ExecutionContext): Future[U]

Definition Classes
    Future
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#recoverWith\[U>:T\]\(pf:PartialFunction\[Throwable,scala.concurrent.Future\[U\]\]\)\(implicitexecutor:scala.concurrent.ExecutionContext\):scala.concurrent.Future\[U\] "Permalink") def recoverWith[U >: T](pf: PartialFunction[Throwable, Future[U]])(implicit executor: ExecutionContext): Future[U]

Definition Classes
    Future
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#transform\[S\]\(s:T=>S,f:Throwable=>Throwable\)\(implicitexecutor:scala.concurrent.ExecutionContext\):scala.concurrent.Future\[S\] "Permalink") def transform[S](s: (T) => S, f: (Throwable) => Throwable)(implicit executor: ExecutionContext): Future[S]

Definition Classes
    Future
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#withFilter\(p:T=>Boolean\)\(implicitexecutor:scala.concurrent.ExecutionContext\):scala.concurrent.Future\[T\] "Permalink") final  def withFilter(p: (T) => Boolean)(implicit executor: ExecutionContext): Future[T]

Definition Classes
    Future
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#zip\[U\]\(that:scala.concurrent.Future\[U\]\):scala.concurrent.Future\[\(T,U\)\] "Permalink") def zip[U](that: Future[U]): Future[(T, U)]

Definition Classes
    Future
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#zipWith\[U,R\]\(that:scala.concurrent.Future\[U\]\)\(f:\(T,U\)=>R\)\(implicitexecutor:scala.concurrent.ExecutionContext\):scala.concurrent.Future\[R\] "Permalink") def zipWith[U, R](that: Future[U])(f: (T, U) => R)(implicit executor: ExecutionContext): Future[R]

Definition Classes
    Future

### Inherited from AnyRef
### Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html###:Int "Permalink") final  def ##: Int

Definition Classes
    AnyRef → Any
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#clone\(\):Object "Permalink") def clone(): AnyRef

Attributes
    protected[lang]

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#equals\(x$1:Object\):Boolean "Permalink") def equals(arg0: AnyRef): Boolean

Definition Classes
    AnyRef → Any
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef]

Definition Classes
    AnyRef → Any

Annotations
     @IntrinsicCandidate() @native()
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#hashCode\(\):Int "Permalink") def hashCode(): Int

Definition Classes
    AnyRef → Any

Annotations
     @IntrinsicCandidate() @native()
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#notify\(\):Unit "Permalink") final  def notify(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0

Definition Classes
    AnyRef
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#toString\(\):String "Permalink") def toString(): [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String")

Definition Classes
    AnyRef → Any
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#wait\(\):Unit "Permalink") final  def wait(): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#finalize\(\):Unit "Permalink") def finalize(): Unit

Attributes
    protected[lang]

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.Throwable]) @Deprecated

Deprecated

_(Since version 9)_

### Inherited from Any
### Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0

Definition Classes
    Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean

Definition Classes
    Any

### Ungrouped
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html###:Int "Permalink") final  def ##: Int

Definition Classes
    AnyRef → Any
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#andThen\[U\]\(pf:PartialFunction\[scala.util.Try\[T\],U\]\)\(implicitexecutor:scala.concurrent.ExecutionContext\):scala.concurrent.Future\[T\] "Permalink") def andThen[U](pf: PartialFunction[Try[T], U])(implicit executor: ExecutionContext): Future[T]

Definition Classes
    Future
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0

Definition Classes
    Any
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#cancel\(reason:Option\[String\]\):Unit "Permalink") def cancel(reason: Option[String]): Unit
Cancels the execution of this action with an optional reason.
Cancels the execution of this action with an optional reason.

Definition Classes
     [ComplexFutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html "org.apache.spark.ComplexFutureAction") → [FutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/FutureAction.html "org.apache.spark.FutureAction")
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#cancel\(\):Unit "Permalink") def cancel(): Unit
Cancels the execution of this action.
Cancels the execution of this action.

Definition Classes
    [FutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/FutureAction.html "org.apache.spark.FutureAction")
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#clone\(\):Object "Permalink") def clone(): AnyRef

Attributes
    protected[lang]

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#collect\[S\]\(pf:PartialFunction\[T,S\]\)\(implicitexecutor:scala.concurrent.ExecutionContext\):scala.concurrent.Future\[S\] "Permalink") def collect[S](pf: PartialFunction[T, S])(implicit executor: ExecutionContext): Future[S]

Definition Classes
    Future
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#equals\(x$1:Object\):Boolean "Permalink") def equals(arg0: AnyRef): Boolean

Definition Classes
    AnyRef → Any
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#failed:scala.concurrent.Future\[Throwable\] "Permalink") def failed: Future[Throwable]

Definition Classes
    Future
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#fallbackTo\[U>:T\]\(that:scala.concurrent.Future\[U\]\):scala.concurrent.Future\[U\] "Permalink") def fallbackTo[U >: T](that: Future[U]): Future[U]

Definition Classes
    Future
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#filter\(p:T=>Boolean\)\(implicitexecutor:scala.concurrent.ExecutionContext\):scala.concurrent.Future\[T\] "Permalink") def filter(p: (T) => Boolean)(implicit executor: ExecutionContext): Future[T]

Definition Classes
    Future
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#flatMap\[S\]\(f:T=>scala.concurrent.Future\[S\]\)\(implicitexecutor:scala.concurrent.ExecutionContext\):scala.concurrent.Future\[S\] "Permalink") def flatMap[S](f: (T) => Future[S])(implicit executor: ExecutionContext): Future[S]

Definition Classes
    Future
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#flatten\[S\]\(implicitev:T<:<scala.concurrent.Future\[S\]\):scala.concurrent.Future\[S\] "Permalink") def flatten[S](implicit ev: <:<[T, Future[S]]): Future[S]

Definition Classes
    Future
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#foreach\[U\]\(f:T=>U\)\(implicitexecutor:scala.concurrent.ExecutionContext\):Unit "Permalink") def foreach[U](f: (T) => U)(implicit executor: ExecutionContext): Unit

Definition Classes
    Future
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#get\(\):T "Permalink") def get(): T
Blocks and returns the result of this job.
Blocks and returns the result of this job.

Definition Classes
    [FutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/FutureAction.html "org.apache.spark.FutureAction")

Annotations
     @throws(classOf[SparkException])
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef]

Definition Classes
    AnyRef → Any

Annotations
     @IntrinsicCandidate() @native()
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#hashCode\(\):Int "Permalink") def hashCode(): Int

Definition Classes
    AnyRef → Any

Annotations
     @IntrinsicCandidate() @native()
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#isCancelled:Boolean "Permalink") def isCancelled: Boolean
Returns whether the action has been cancelled.
Returns whether the action has been cancelled.

Definition Classes
     [ComplexFutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html "org.apache.spark.ComplexFutureAction") → [FutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/FutureAction.html "org.apache.spark.FutureAction")
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#isCompleted:Boolean "Permalink") def isCompleted: Boolean
Returns whether the action has already been completed with a value or an exception.
Returns whether the action has already been completed with a value or an exception.

Definition Classes
     [ComplexFutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html "org.apache.spark.ComplexFutureAction") → [FutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/FutureAction.html "org.apache.spark.FutureAction") → Future
  23. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean

Definition Classes
    Any
  24. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#jobIds:Seq\[Int\] "Permalink") def jobIds: Seq[Int]
Returns the job IDs run by the underlying async operation.
Returns the job IDs run by the underlying async operation.
This returns the current snapshot of the job list. Certain operations may run multiple jobs, so multiple calls to this method may return different lists.

Definition Classes
     [ComplexFutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html "org.apache.spark.ComplexFutureAction") → [FutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/FutureAction.html "org.apache.spark.FutureAction")
  25. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#map\[S\]\(f:T=>S\)\(implicitexecutor:scala.concurrent.ExecutionContext\):scala.concurrent.Future\[S\] "Permalink") def map[S](f: (T) => S)(implicit executor: ExecutionContext): Future[S]

Definition Classes
    Future
  26. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#mapTo\[S\]\(implicittag:scala.reflect.ClassTag\[S\]\):scala.concurrent.Future\[S\] "Permalink") def mapTo[S](implicit tag: ClassTag[S]): Future[S]

Definition Classes
    Future
  27. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  28. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#notify\(\):Unit "Permalink") final  def notify(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  29. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  30. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#onComplete\[U\]\(func:scala.util.Try\[T\]=>U\)\(implicitexecutor:scala.concurrent.ExecutionContext\):Unit "Permalink") def onComplete[U](func: (Try[T]) => U)(implicit executor: ExecutionContext): Unit
When this action is completed, either through an exception, or a value, applies the provided function.
When this action is completed, either through an exception, or a value, applies the provided function.

Definition Classes
     [ComplexFutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html "org.apache.spark.ComplexFutureAction") → [FutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/FutureAction.html "org.apache.spark.FutureAction") → Future
  31. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#ready\(atMost:scala.concurrent.duration.Duration\)\(implicitpermit:scala.concurrent.CanAwait\):ComplexFutureAction.this.type "Permalink") def ready(atMost: Duration)(implicit permit: CanAwait): [ComplexFutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html "org.apache.spark.ComplexFutureAction").this.type
Blocks until this action completes.
Blocks until this action completes.

atMost

maximum wait time, which may be negative (no waiting is done), Duration.Inf for unbounded waiting, or a finite positive duration

returns

this FutureAction

Definition Classes
     [ComplexFutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html "org.apache.spark.ComplexFutureAction") → [FutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/FutureAction.html "org.apache.spark.FutureAction") → Awaitable

Annotations
     @throws(classOf[InterruptedException]) @throws(classOf[scala.concurrent.TimeoutException])
  32. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#recover\[U>:T\]\(pf:PartialFunction\[Throwable,U\]\)\(implicitexecutor:scala.concurrent.ExecutionContext\):scala.concurrent.Future\[U\] "Permalink") def recover[U >: T](pf: PartialFunction[Throwable, U])(implicit executor: ExecutionContext): Future[U]

Definition Classes
    Future
  33. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#recoverWith\[U>:T\]\(pf:PartialFunction\[Throwable,scala.concurrent.Future\[U\]\]\)\(implicitexecutor:scala.concurrent.ExecutionContext\):scala.concurrent.Future\[U\] "Permalink") def recoverWith[U >: T](pf: PartialFunction[Throwable, Future[U]])(implicit executor: ExecutionContext): Future[U]

Definition Classes
    Future
  34. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#result\(atMost:scala.concurrent.duration.Duration\)\(implicitpermit:scala.concurrent.CanAwait\):T "Permalink") def result(atMost: Duration)(implicit permit: CanAwait): T
Awaits and returns the result (of type T) of this action.
Awaits and returns the result (of type T) of this action.

atMost

maximum wait time, which may be negative (no waiting is done), Duration.Inf for unbounded waiting, or a finite positive duration

returns

the result value if the action is completed within the specific maximum wait time

Definition Classes
     [ComplexFutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html "org.apache.spark.ComplexFutureAction") → [FutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/FutureAction.html "org.apache.spark.FutureAction") → Awaitable

Annotations
     @throws(classOf[Exception])

Exceptions thrown

`Exception` exception during action execution
  35. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0

Definition Classes
    AnyRef
  36. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#toString\(\):String "Permalink") def toString(): [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String")

Definition Classes
    AnyRef → Any
  37. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#transform\[S\]\(f:scala.util.Try\[T\]=>scala.util.Try\[S\]\)\(implicite:scala.concurrent.ExecutionContext\):scala.concurrent.Future\[S\] "Permalink") def transform[S](f: (Try[T]) => Try[S])(implicit e: ExecutionContext): Future[S]

Definition Classes
     [ComplexFutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html "org.apache.spark.ComplexFutureAction") → Future
  38. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#transform\[S\]\(s:T=>S,f:Throwable=>Throwable\)\(implicitexecutor:scala.concurrent.ExecutionContext\):scala.concurrent.Future\[S\] "Permalink") def transform[S](s: (T) => S, f: (Throwable) => Throwable)(implicit executor: ExecutionContext): Future[S]

Definition Classes
    Future
  39. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#transformWith\[S\]\(f:scala.util.Try\[T\]=>scala.concurrent.Future\[S\]\)\(implicite:scala.concurrent.ExecutionContext\):scala.concurrent.Future\[S\] "Permalink") def transformWith[S](f: (Try[T]) => Future[S])(implicit e: ExecutionContext): Future[S]

Definition Classes
     [ComplexFutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html "org.apache.spark.ComplexFutureAction") → Future
  40. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#value:Option\[scala.util.Try\[T\]\] "Permalink") def value: Option[Try[T]]
The value of this Future.
The value of this Future.
If the future is not completed the returned value will be None. If the future is completed the value will be Some(Success(t)) if it contains a valid result, or Some(Failure(error)) if it contains an exception.

Definition Classes
     [ComplexFutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html "org.apache.spark.ComplexFutureAction") → [FutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/FutureAction.html "org.apache.spark.FutureAction") → Future
  41. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])
  42. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  43. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#wait\(\):Unit "Permalink") final  def wait(): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])
  44. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#withFilter\(p:T=>Boolean\)\(implicitexecutor:scala.concurrent.ExecutionContext\):scala.concurrent.Future\[T\] "Permalink") final  def withFilter(p: (T) => Boolean)(implicit executor: ExecutionContext): Future[T]

Definition Classes
    Future
  45. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#zip\[U\]\(that:scala.concurrent.Future\[U\]\):scala.concurrent.Future\[\(T,U\)\] "Permalink") def zip[U](that: Future[U]): Future[(T, U)]

Definition Classes
    Future
  46. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#zipWith\[U,R\]\(that:scala.concurrent.Future\[U\]\)\(f:\(T,U\)=>R\)\(implicitexecutor:scala.concurrent.ExecutionContext\):scala.concurrent.Future\[R\] "Permalink") def zipWith[U, R](that: Future[U])(f: (T, U) => R)(implicit executor: ExecutionContext): Future[R]

Definition Classes
    Future
  47. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ComplexFutureAction.html#finalize\(\):Unit "Permalink") def finalize(): Unit

Attributes
    protected[lang]

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.Throwable]) @Deprecated

Deprecated

_(Since version 9)_
