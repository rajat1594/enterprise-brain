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
# SparkConf[ __](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html "Permalink")
####  class SparkConf extends [ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html "org.apache.spark.ReadOnlySparkConf") with Cloneable with Logging with Serializable
Configuration for a Spark application. Used to set various Spark parameters as key-value pairs.
Most of the time, you would create a SparkConf object with `new SparkConf()`, which will load values from any `spark.*` Java system properties set in your application as well. In this case, parameters you set directly on the `SparkConf` object take priority over system properties.
For unit tests, you can also call `new SparkConf(false)` to skip loading external settings and get the same configuration no matter what the system properties are.
All setter methods in this class support chaining. For example, you can write `new SparkConf().setMaster("local").setAppName("My app")`.

Source
    [SparkConf.scala](https://github.com/apache/spark/tree/v4.1.2/core/src/main/scala/org/apache/spark/SparkConf.scala)

Note

Once a SparkConf object is passed to Spark, it is cloned and can no longer be modified by the user. Spark does not support modifying the configuration at runtime.
Linear Supertypes
[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable"), Logging, [Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html#java.lang.Cloneable "java.lang.Cloneable"), [ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html "org.apache.spark.ReadOnlySparkConf"), AnyRef, Any
__ __
Ordering
  1. Alphabetic
  2. By Inheritance

Inherited

  1. SparkConf
  2. Serializable
  3. Logging
  4. Cloneable
  5. ReadOnlySparkConf
  6. AnyRef
  7. Any

  1. Hide All
  2. Show All

Visibility
  1. Public
  2. Protected

### Instance Constructors
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#<init>\(\):org.apache.spark.SparkConf "Permalink") new SparkConf()
Create a SparkConf that loads defaults from system properties and the classpath
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#<init>\(loadDefaults:Boolean\):org.apache.spark.SparkConf "Permalink") new SparkConf(loadDefaults: Boolean)

loadDefaults

whether to also load values from Java system properties

### Type Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#LogStringContextextendsAnyRef "Permalink") implicit  class LogStringContext extends AnyRef

Definition Classes
    Logging

### Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html###:Int "Permalink") final  def ##: Int

Definition Classes
    AnyRef → Any
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#MDC\(key:org.apache.spark.internal.LogKey,value:Any\):org.apache.spark.internal.MDC "Permalink") def MDC(key: LogKey, value: Any): MDC

Attributes
    protected

Definition Classes
    Logging
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0

Definition Classes
    Any
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#catchIllegalValue\[T\]\(key:String\)\(getValue:=>T\):T "Permalink") def catchIllegalValue[T](key: String)(getValue: => T): T
Wrapper method for get() methods which require some specific value format.
Wrapper method for get() methods which require some specific value format. This catches any NumberFormatException or IllegalArgumentException and re-raises it with the incorrectly configured key in the exception message.

Attributes
    protected

Definition Classes
    [ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html "org.apache.spark.ReadOnlySparkConf")
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#clone\(\):org.apache.spark.SparkConf "Permalink") def clone(): [SparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html "org.apache.spark.SparkConf")
Copy this object
Copy this object

Definition Classes
     [SparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html "org.apache.spark.SparkConf") → AnyRef
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#contains\(key:String\):Boolean "Permalink") def contains(key: String): Boolean
Does the configuration contain a given parameter?
Does the configuration contain a given parameter?

Definition Classes
     [SparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html "org.apache.spark.SparkConf") → [ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html "org.apache.spark.ReadOnlySparkConf")
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#contains\(entry:org.apache.spark.internal.config.ConfigEntry\[_\]\):Boolean "Permalink") def contains(entry: ConfigEntry[_]): Boolean
Does the configuration have the typed config entry?
Does the configuration have the typed config entry?

Definition Classes
    [ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html "org.apache.spark.ReadOnlySparkConf")
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#equals\(x$1:Object\):Boolean "Permalink") def equals(arg0: AnyRef): Boolean

Definition Classes
    AnyRef → Any
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#get\(key:String,defaultValue:String\):String "Permalink") def get(key: String, defaultValue: String): String
Get a parameter, falling back to a default if not set
Get a parameter, falling back to a default if not set

Definition Classes
    [ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html "org.apache.spark.ReadOnlySparkConf")
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#get\(key:String\):String "Permalink") def get(key: String): String
Get a parameter; throws a NoSuchElementException if it's not set
Get a parameter; throws a NoSuchElementException if it's not set

Definition Classes
    [ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html "org.apache.spark.ReadOnlySparkConf")
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#getAll:Array\[\(String,String\)\] "Permalink") def getAll: Array[(String, String)]
Get all parameters as a list of pairs
Get all parameters as a list of pairs

Definition Classes
     [SparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html "org.apache.spark.SparkConf") → [ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html "org.apache.spark.ReadOnlySparkConf")
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#getAllWithPrefix\[K\]\(prefix:String,f:String=>K\):Array\[\(K,String\)\] "Permalink") def getAllWithPrefix[K](prefix: String, f: (String) => K): Array[(K, String)]
Get all parameters that start with `prefix` and apply f.
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#getAllWithPrefix\(prefix:String\):Array\[\(String,String\)\] "Permalink") def getAllWithPrefix(prefix: String): Array[(String, String)]
Get all parameters that start with `prefix`
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#getAppId:String "Permalink") def getAppId: String
Returns the Spark application id, valid in the Driver after TaskScheduler registration and from the start in the Executor.
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#getAvroSchema:Map\[Long,String\] "Permalink") def getAvroSchema: Map[Long, String]
Gets all the avro schemas in the configuration used in the generic Avro record serializer
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#getBoolean\(key:String,defaultValue:Boolean\):Boolean "Permalink") def getBoolean(key: String, defaultValue: Boolean): Boolean
Get a parameter as a boolean, falling back to a default if not set
Get a parameter as a boolean, falling back to a default if not set

Definition Classes
    [ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html "org.apache.spark.ReadOnlySparkConf")

Exceptions thrown

`IllegalArgumentException` If the value cannot be interpreted as a boolean
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef]

Definition Classes
    AnyRef → Any

Annotations
     @IntrinsicCandidate() @native()
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#getDouble\(key:String,defaultValue:Double\):Double "Permalink") def getDouble(key: String, defaultValue: Double): Double
Get a parameter as a double, falling back to a default if not ste
Get a parameter as a double, falling back to a default if not ste

Definition Classes
    [ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html "org.apache.spark.ReadOnlySparkConf")

Exceptions thrown

`NumberFormatException` If the value cannot be interpreted as a double
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#getExecutorEnv:Seq\[\(String,String\)\] "Permalink") def getExecutorEnv: Seq[(String, String)]
Get all executor environment variables set on this SparkConf
  23. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#getInt\(key:String,defaultValue:Int\):Int "Permalink") def getInt(key: String, defaultValue: Int): Int
Get a parameter as an integer, falling back to a default if not set
Get a parameter as an integer, falling back to a default if not set

Definition Classes
    [ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html "org.apache.spark.ReadOnlySparkConf")

Exceptions thrown

`NumberFormatException` If the value cannot be interpreted as an integer
  24. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#getLong\(key:String,defaultValue:Long\):Long "Permalink") def getLong(key: String, defaultValue: Long): Long
Get a parameter as a long, falling back to a default if not set
Get a parameter as a long, falling back to a default if not set

Definition Classes
    [ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html "org.apache.spark.ReadOnlySparkConf")

Exceptions thrown

`NumberFormatException` If the value cannot be interpreted as a long
  25. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#getOption\(key:String\):Option\[String\] "Permalink") def getOption(key: String): Option[String]
Get a parameter as an Option
Get a parameter as an Option

Definition Classes
     [SparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html "org.apache.spark.SparkConf") → [ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html "org.apache.spark.ReadOnlySparkConf")
  26. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#getSizeAsBytes\(key:String,defaultValue:Long\):Long "Permalink") def getSizeAsBytes(key: String, defaultValue: Long): Long
Get a size parameter as bytes, falling back to a default if not set.
Get a size parameter as bytes, falling back to a default if not set.

Definition Classes
    [ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html "org.apache.spark.ReadOnlySparkConf")

Exceptions thrown

`NumberFormatException` If the value cannot be interpreted as bytes
  27. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#getSizeAsBytes\(key:String,defaultValue:String\):Long "Permalink") def getSizeAsBytes(key: String, defaultValue: String): Long
Get a size parameter as bytes, falling back to a default if not set.
Get a size parameter as bytes, falling back to a default if not set. If no suffix is provided then bytes are assumed.

Definition Classes
    [ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html "org.apache.spark.ReadOnlySparkConf")

Exceptions thrown

`NumberFormatException` If the value cannot be interpreted as bytes
  28. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#getSizeAsBytes\(key:String\):Long "Permalink") def getSizeAsBytes(key: String): Long
Get a size parameter as bytes; throws a NoSuchElementException if it's not set.
Get a size parameter as bytes; throws a NoSuchElementException if it's not set. If no suffix is provided then bytes are assumed.

Definition Classes
    [ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html "org.apache.spark.ReadOnlySparkConf")

Exceptions thrown

`NumberFormatException` If the value cannot be interpreted as bytes
[`java.util.NoSuchElementException`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/NoSuchElementException.html "java.util.NoSuchElementException") If the size parameter is not set
  29. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#getSizeAsGb\(key:String,defaultValue:String\):Long "Permalink") def getSizeAsGb(key: String, defaultValue: String): Long
Get a size parameter as Gibibytes, falling back to a default if not set.
Get a size parameter as Gibibytes, falling back to a default if not set. If no suffix is provided then Gibibytes are assumed.

Definition Classes
    [ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html "org.apache.spark.ReadOnlySparkConf")

Exceptions thrown

`NumberFormatException` If the value cannot be interpreted as Gibibytes
  30. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#getSizeAsGb\(key:String\):Long "Permalink") def getSizeAsGb(key: String): Long
Get a size parameter as Gibibytes; throws a NoSuchElementException if it's not set.
Get a size parameter as Gibibytes; throws a NoSuchElementException if it's not set. If no suffix is provided then Gibibytes are assumed.

Definition Classes
    [ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html "org.apache.spark.ReadOnlySparkConf")

Exceptions thrown

`NumberFormatException` If the value cannot be interpreted as Gibibytes
[`java.util.NoSuchElementException`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/NoSuchElementException.html "java.util.NoSuchElementException") If the size parameter is not set
  31. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#getSizeAsKb\(key:String,defaultValue:String\):Long "Permalink") def getSizeAsKb(key: String, defaultValue: String): Long
Get a size parameter as Kibibytes, falling back to a default if not set.
Get a size parameter as Kibibytes, falling back to a default if not set. If no suffix is provided then Kibibytes are assumed.

Definition Classes
    [ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html "org.apache.spark.ReadOnlySparkConf")

Exceptions thrown

`NumberFormatException` If the value cannot be interpreted as Kibibytes
  32. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#getSizeAsKb\(key:String\):Long "Permalink") def getSizeAsKb(key: String): Long
Get a size parameter as Kibibytes; throws a NoSuchElementException if it's not set.
Get a size parameter as Kibibytes; throws a NoSuchElementException if it's not set. If no suffix is provided then Kibibytes are assumed.

Definition Classes
    [ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html "org.apache.spark.ReadOnlySparkConf")

Exceptions thrown

`NumberFormatException` If the value cannot be interpreted as Kibibytes
[`java.util.NoSuchElementException`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/NoSuchElementException.html "java.util.NoSuchElementException") If the size parameter is not set
  33. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#getSizeAsMb\(key:String,defaultValue:String\):Long "Permalink") def getSizeAsMb(key: String, defaultValue: String): Long
Get a size parameter as Mebibytes, falling back to a default if not set.
Get a size parameter as Mebibytes, falling back to a default if not set. If no suffix is provided then Mebibytes are assumed.

Definition Classes
    [ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html "org.apache.spark.ReadOnlySparkConf")

Exceptions thrown

`NumberFormatException` If the value cannot be interpreted as Mebibytes
  34. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#getSizeAsMb\(key:String\):Long "Permalink") def getSizeAsMb(key: String): Long
Get a size parameter as Mebibytes; throws a NoSuchElementException if it's not set.
Get a size parameter as Mebibytes; throws a NoSuchElementException if it's not set. If no suffix is provided then Mebibytes are assumed.

Definition Classes
    [ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html "org.apache.spark.ReadOnlySparkConf")

Exceptions thrown

`NumberFormatException` If the value cannot be interpreted as Mebibytes
[`java.util.NoSuchElementException`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/NoSuchElementException.html "java.util.NoSuchElementException") If the size parameter is not set
  35. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#getTimeAsMs\(key:String,defaultValue:String\):Long "Permalink") def getTimeAsMs(key: String, defaultValue: String): Long
Get a time parameter as milliseconds, falling back to a default if not set.
Get a time parameter as milliseconds, falling back to a default if not set. If no suffix is provided then milliseconds are assumed.

Definition Classes
    [ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html "org.apache.spark.ReadOnlySparkConf")

Exceptions thrown

`NumberFormatException` If the value cannot be interpreted as milliseconds
  36. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#getTimeAsMs\(key:String\):Long "Permalink") def getTimeAsMs(key: String): Long
Get a time parameter as milliseconds; throws a NoSuchElementException if it's not set.
Get a time parameter as milliseconds; throws a NoSuchElementException if it's not set. If no suffix is provided then milliseconds are assumed.

Definition Classes
    [ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html "org.apache.spark.ReadOnlySparkConf")

Exceptions thrown

`NumberFormatException` If the value cannot be interpreted as milliseconds
[`java.util.NoSuchElementException`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/NoSuchElementException.html "java.util.NoSuchElementException") If the time parameter is not set
  37. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#getTimeAsSeconds\(key:String,defaultValue:String\):Long "Permalink") def getTimeAsSeconds(key: String, defaultValue: String): Long
Get a time parameter as seconds, falling back to a default if not set.
Get a time parameter as seconds, falling back to a default if not set. If no suffix is provided then seconds are assumed.

Definition Classes
    [ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html "org.apache.spark.ReadOnlySparkConf")

Exceptions thrown

`NumberFormatException` If the value cannot be interpreted as seconds
  38. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#getTimeAsSeconds\(key:String\):Long "Permalink") def getTimeAsSeconds(key: String): Long
Get a time parameter as seconds; throws a NoSuchElementException if it's not set.
Get a time parameter as seconds; throws a NoSuchElementException if it's not set. If no suffix is provided then seconds are assumed.

Definition Classes
    [ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html "org.apache.spark.ReadOnlySparkConf")

Exceptions thrown

`NumberFormatException` If the value cannot be interpreted as seconds
[`java.util.NoSuchElementException`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/NoSuchElementException.html "java.util.NoSuchElementException") If the time parameter is not set
  39. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#hashCode\(\):Int "Permalink") def hashCode(): Int

Definition Classes
    AnyRef → Any

Annotations
     @IntrinsicCandidate() @native()
  40. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#initializeLogIfNecessary\(isInterpreter:Boolean,silent:Boolean\):Boolean "Permalink") def initializeLogIfNecessary(isInterpreter: Boolean, silent: Boolean): Boolean

Attributes
    protected

Definition Classes
    Logging
  41. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#initializeLogIfNecessary\(isInterpreter:Boolean\):Unit "Permalink") def initializeLogIfNecessary(isInterpreter: Boolean): Unit

Attributes
    protected

Definition Classes
    Logging
  42. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean

Definition Classes
    Any
  43. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#isTraceEnabled\(\):Boolean "Permalink") def isTraceEnabled(): Boolean

Attributes
    protected

Definition Classes
    Logging
  44. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#log:org.slf4j.Logger "Permalink") def log: Logger

Attributes
    protected

Definition Classes
    Logging
  45. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#logBasedOnLevel\(level:org.slf4j.event.Level\)\(f:=>org.apache.spark.internal.MessageWithContext\):Unit "Permalink") def logBasedOnLevel(level: Level)(f: => MessageWithContext): Unit

Attributes
    protected

Definition Classes
    Logging
  46. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#logDebug\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logDebug(msg: => String, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  47. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#logDebug\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logDebug(entry: LogEntry, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  48. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#logDebug\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logDebug(entry: LogEntry): Unit

Attributes
    protected

Definition Classes
    Logging
  49. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#logDebug\(msg:=>String\):Unit "Permalink") def logDebug(msg: => String): Unit

Attributes
    protected

Definition Classes
    Logging
  50. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#logError\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logError(msg: => String, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  51. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#logError\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logError(entry: LogEntry, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  52. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#logError\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logError(entry: LogEntry): Unit

Attributes
    protected

Definition Classes
    Logging
  53. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#logError\(msg:=>String\):Unit "Permalink") def logError(msg: => String): Unit

Attributes
    protected

Definition Classes
    Logging
  54. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#logInfo\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logInfo(msg: => String, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  55. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#logInfo\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logInfo(entry: LogEntry, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  56. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#logInfo\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logInfo(entry: LogEntry): Unit

Attributes
    protected

Definition Classes
    Logging
  57. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#logInfo\(msg:=>String\):Unit "Permalink") def logInfo(msg: => String): Unit

Attributes
    protected

Definition Classes
    Logging
  58. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#logName:String "Permalink") def logName: [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String")

Attributes
    protected

Definition Classes
    Logging
  59. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#logTrace\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logTrace(msg: => String, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  60. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#logTrace\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logTrace(entry: LogEntry, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  61. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#logTrace\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logTrace(entry: LogEntry): Unit

Attributes
    protected

Definition Classes
    Logging
  62. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#logTrace\(msg:=>String\):Unit "Permalink") def logTrace(msg: => String): Unit

Attributes
    protected

Definition Classes
    Logging
  63. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#logWarning\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logWarning(msg: => String, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  64. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#logWarning\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logWarning(entry: LogEntry, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  65. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#logWarning\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logWarning(entry: LogEntry): Unit

Attributes
    protected

Definition Classes
    Logging
  66. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#logWarning\(msg:=>String\):Unit "Permalink") def logWarning(msg: => String): Unit

Attributes
    protected

Definition Classes
    Logging
  67. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  68. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#notify\(\):Unit "Permalink") final  def notify(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  69. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  70. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#registerAvroSchemas\(schemas:org.apache.avro.Schema*\):org.apache.spark.SparkConf "Permalink") def registerAvroSchemas(schemas: Schema*): [SparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html "org.apache.spark.SparkConf")
Use Kryo serialization and register the given set of Avro schemas so that the generic record serializer can decrease network IO
  71. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#registerKryoClasses\(classes:Array\[Class\[_\]\]\):org.apache.spark.SparkConf "Permalink") def registerKryoClasses(classes: Array[Class[_]]): [SparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html "org.apache.spark.SparkConf")
Use Kryo serialization and register the given set of classes with Kryo.
Use Kryo serialization and register the given set of classes with Kryo. If called multiple times, this will append the classes from all calls together.
  72. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#remove\(key:String\):org.apache.spark.SparkConf "Permalink") def remove(key: String): [SparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html "org.apache.spark.SparkConf")
Remove a parameter from the configuration
  73. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#set\(key:String,value:String\):org.apache.spark.SparkConf "Permalink") def set(key: String, value: String): [SparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html "org.apache.spark.SparkConf")
Set a configuration variable.
  74. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#setAll\(settings:Iterable\[\(String,String\)\]\):org.apache.spark.SparkConf "Permalink") def setAll(settings: Iterable[(String, String)]): [SparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html "org.apache.spark.SparkConf")
Set multiple parameters together
  75. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#setAppName\(name:String\):org.apache.spark.SparkConf "Permalink") def setAppName(name: String): [SparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html "org.apache.spark.SparkConf")
Set a name for your application.
Set a name for your application. Shown in the Spark web UI.
  76. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#setExecutorEnv\(variables:Array\[\(String,String\)\]\):org.apache.spark.SparkConf "Permalink") def setExecutorEnv(variables: Array[(String, String)]): [SparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html "org.apache.spark.SparkConf")
Set multiple environment variables to be used when launching executors.
Set multiple environment variables to be used when launching executors. (Java-friendly version.)
  77. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#setExecutorEnv\(variables:Seq\[\(String,String\)\]\):org.apache.spark.SparkConf "Permalink") def setExecutorEnv(variables: Seq[(String, String)]): [SparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html "org.apache.spark.SparkConf")
Set multiple environment variables to be used when launching executors.
Set multiple environment variables to be used when launching executors. These variables are stored as properties of the form spark.executorEnv.VAR_NAME (for example spark.executorEnv.PATH) but this method makes them easier to set.
  78. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#setExecutorEnv\(variable:String,value:String\):org.apache.spark.SparkConf "Permalink") def setExecutorEnv(variable: String, value: String): [SparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html "org.apache.spark.SparkConf")
Set an environment variable to be used when launching executors for this application.
Set an environment variable to be used when launching executors for this application. These variables are stored as properties of the form spark.executorEnv.VAR_NAME (for example spark.executorEnv.PATH) but this method makes them easier to set.
  79. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#setIfMissing\(key:String,value:String\):org.apache.spark.SparkConf "Permalink") def setIfMissing(key: String, value: String): [SparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html "org.apache.spark.SparkConf")
Set a parameter if it isn't already configured
  80. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#setJars\(jars:Array\[String\]\):org.apache.spark.SparkConf "Permalink") def setJars(jars: Array[String]): [SparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html "org.apache.spark.SparkConf")
Set JAR files to distribute to the cluster.
Set JAR files to distribute to the cluster. (Java-friendly version.)
  81. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#setJars\(jars:Seq\[String\]\):org.apache.spark.SparkConf "Permalink") def setJars(jars: Seq[String]): [SparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html "org.apache.spark.SparkConf")
Set JAR files to distribute to the cluster.
  82. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#setMaster\(master:String\):org.apache.spark.SparkConf "Permalink") def setMaster(master: String): [SparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html "org.apache.spark.SparkConf")
The master URL to connect to, such as "local" to run locally with one thread, "local[4]" to run locally with 4 cores, or "spark://master:7077" to run on a Spark standalone cluster.
  83. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#setSparkHome\(home:String\):org.apache.spark.SparkConf "Permalink") def setSparkHome(home: String): [SparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html "org.apache.spark.SparkConf")
Set the location where Spark is installed on worker nodes.
  84. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0

Definition Classes
    AnyRef
  85. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#toDebugString:String "Permalink") def toDebugString: String
Return a string listing all keys and values, one per line.
Return a string listing all keys and values, one per line. This is useful to print the configuration out for debugging.
  86. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#toString\(\):String "Permalink") def toString(): [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String")

Definition Classes
    AnyRef → Any
  87. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])
  88. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  89. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#wait\(\):Unit "Permalink") final  def wait(): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])
  90. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#withLogContext\(context:java.util.Map\[String,String\]\)\(body:=>Unit\):Unit "Permalink") def withLogContext(context: [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#java.util.Map "java.util.Map")[String, String])(body: => Unit): Unit

Attributes
    protected

Definition Classes
    Logging

### Deprecated Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#finalize\(\):Unit "Permalink") def finalize(): Unit

Attributes
    protected[lang]

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.Throwable]) @Deprecated

Deprecated

_(Since version 9)_

### Inherited from Logging
### Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#MDC\(key:org.apache.spark.internal.LogKey,value:Any\):org.apache.spark.internal.MDC "Permalink") def MDC(key: LogKey, value: Any): MDC

Attributes
    protected

Definition Classes
    Logging
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#initializeLogIfNecessary\(isInterpreter:Boolean,silent:Boolean\):Boolean "Permalink") def initializeLogIfNecessary(isInterpreter: Boolean, silent: Boolean): Boolean

Attributes
    protected

Definition Classes
    Logging
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#initializeLogIfNecessary\(isInterpreter:Boolean\):Unit "Permalink") def initializeLogIfNecessary(isInterpreter: Boolean): Unit

Attributes
    protected

Definition Classes
    Logging
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#isTraceEnabled\(\):Boolean "Permalink") def isTraceEnabled(): Boolean

Attributes
    protected

Definition Classes
    Logging
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#log:org.slf4j.Logger "Permalink") def log: Logger

Attributes
    protected

Definition Classes
    Logging
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#logBasedOnLevel\(level:org.slf4j.event.Level\)\(f:=>org.apache.spark.internal.MessageWithContext\):Unit "Permalink") def logBasedOnLevel(level: Level)(f: => MessageWithContext): Unit

Attributes
    protected

Definition Classes
    Logging
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#logDebug\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logDebug(msg: => String, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#logDebug\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logDebug(entry: LogEntry, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#logDebug\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logDebug(entry: LogEntry): Unit

Attributes
    protected

Definition Classes
    Logging
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#logDebug\(msg:=>String\):Unit "Permalink") def logDebug(msg: => String): Unit

Attributes
    protected

Definition Classes
    Logging
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#logError\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logError(msg: => String, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#logError\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logError(entry: LogEntry, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#logError\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logError(entry: LogEntry): Unit

Attributes
    protected

Definition Classes
    Logging
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#logError\(msg:=>String\):Unit "Permalink") def logError(msg: => String): Unit

Attributes
    protected

Definition Classes
    Logging
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#logInfo\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logInfo(msg: => String, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#logInfo\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logInfo(entry: LogEntry, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#logInfo\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logInfo(entry: LogEntry): Unit

Attributes
    protected

Definition Classes
    Logging
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#logInfo\(msg:=>String\):Unit "Permalink") def logInfo(msg: => String): Unit

Attributes
    protected

Definition Classes
    Logging
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#logName:String "Permalink") def logName: [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String")

Attributes
    protected

Definition Classes
    Logging
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#logTrace\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logTrace(msg: => String, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#logTrace\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logTrace(entry: LogEntry, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#logTrace\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logTrace(entry: LogEntry): Unit

Attributes
    protected

Definition Classes
    Logging
  23. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#logTrace\(msg:=>String\):Unit "Permalink") def logTrace(msg: => String): Unit

Attributes
    protected

Definition Classes
    Logging
  24. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#logWarning\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logWarning(msg: => String, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  25. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#logWarning\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logWarning(entry: LogEntry, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  26. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#logWarning\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logWarning(entry: LogEntry): Unit

Attributes
    protected

Definition Classes
    Logging
  27. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#logWarning\(msg:=>String\):Unit "Permalink") def logWarning(msg: => String): Unit

Attributes
    protected

Definition Classes
    Logging
  28. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#withLogContext\(context:java.util.Map\[String,String\]\)\(body:=>Unit\):Unit "Permalink") def withLogContext(context: [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#java.util.Map "java.util.Map")[String, String])(body: => Unit): Unit

Attributes
    protected

Definition Classes
    Logging

### Inherited from [ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html "org.apache.spark.ReadOnlySparkConf")
### Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#catchIllegalValue\[T\]\(key:String\)\(getValue:=>T\):T "Permalink") def catchIllegalValue[T](key: String)(getValue: => T): T
Wrapper method for get() methods which require some specific value format.
Wrapper method for get() methods which require some specific value format. This catches any NumberFormatException or IllegalArgumentException and re-raises it with the incorrectly configured key in the exception message.

Attributes
    protected

Definition Classes
    [ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html "org.apache.spark.ReadOnlySparkConf")
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#contains\(entry:org.apache.spark.internal.config.ConfigEntry\[_\]\):Boolean "Permalink") def contains(entry: ConfigEntry[_]): Boolean
Does the configuration have the typed config entry?
Does the configuration have the typed config entry?

Definition Classes
    [ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html "org.apache.spark.ReadOnlySparkConf")
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#get\(key:String,defaultValue:String\):String "Permalink") def get(key: String, defaultValue: String): String
Get a parameter, falling back to a default if not set
Get a parameter, falling back to a default if not set

Definition Classes
    [ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html "org.apache.spark.ReadOnlySparkConf")
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#get\(key:String\):String "Permalink") def get(key: String): String
Get a parameter; throws a NoSuchElementException if it's not set
Get a parameter; throws a NoSuchElementException if it's not set

Definition Classes
    [ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html "org.apache.spark.ReadOnlySparkConf")
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#getBoolean\(key:String,defaultValue:Boolean\):Boolean "Permalink") def getBoolean(key: String, defaultValue: Boolean): Boolean
Get a parameter as a boolean, falling back to a default if not set
Get a parameter as a boolean, falling back to a default if not set

Definition Classes
    [ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html "org.apache.spark.ReadOnlySparkConf")

Exceptions thrown

`IllegalArgumentException` If the value cannot be interpreted as a boolean
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#getDouble\(key:String,defaultValue:Double\):Double "Permalink") def getDouble(key: String, defaultValue: Double): Double
Get a parameter as a double, falling back to a default if not ste
Get a parameter as a double, falling back to a default if not ste

Definition Classes
    [ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html "org.apache.spark.ReadOnlySparkConf")

Exceptions thrown

`NumberFormatException` If the value cannot be interpreted as a double
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#getInt\(key:String,defaultValue:Int\):Int "Permalink") def getInt(key: String, defaultValue: Int): Int
Get a parameter as an integer, falling back to a default if not set
Get a parameter as an integer, falling back to a default if not set

Definition Classes
    [ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html "org.apache.spark.ReadOnlySparkConf")

Exceptions thrown

`NumberFormatException` If the value cannot be interpreted as an integer
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#getLong\(key:String,defaultValue:Long\):Long "Permalink") def getLong(key: String, defaultValue: Long): Long
Get a parameter as a long, falling back to a default if not set
Get a parameter as a long, falling back to a default if not set

Definition Classes
    [ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html "org.apache.spark.ReadOnlySparkConf")

Exceptions thrown

`NumberFormatException` If the value cannot be interpreted as a long
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#getSizeAsBytes\(key:String,defaultValue:Long\):Long "Permalink") def getSizeAsBytes(key: String, defaultValue: Long): Long
Get a size parameter as bytes, falling back to a default if not set.
Get a size parameter as bytes, falling back to a default if not set.

Definition Classes
    [ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html "org.apache.spark.ReadOnlySparkConf")

Exceptions thrown

`NumberFormatException` If the value cannot be interpreted as bytes
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#getSizeAsBytes\(key:String,defaultValue:String\):Long "Permalink") def getSizeAsBytes(key: String, defaultValue: String): Long
Get a size parameter as bytes, falling back to a default if not set.
Get a size parameter as bytes, falling back to a default if not set. If no suffix is provided then bytes are assumed.

Definition Classes
    [ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html "org.apache.spark.ReadOnlySparkConf")

Exceptions thrown

`NumberFormatException` If the value cannot be interpreted as bytes
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#getSizeAsBytes\(key:String\):Long "Permalink") def getSizeAsBytes(key: String): Long
Get a size parameter as bytes; throws a NoSuchElementException if it's not set.
Get a size parameter as bytes; throws a NoSuchElementException if it's not set. If no suffix is provided then bytes are assumed.

Definition Classes
    [ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html "org.apache.spark.ReadOnlySparkConf")

Exceptions thrown

`NumberFormatException` If the value cannot be interpreted as bytes
[`java.util.NoSuchElementException`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/NoSuchElementException.html "java.util.NoSuchElementException") If the size parameter is not set
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#getSizeAsGb\(key:String,defaultValue:String\):Long "Permalink") def getSizeAsGb(key: String, defaultValue: String): Long
Get a size parameter as Gibibytes, falling back to a default if not set.
Get a size parameter as Gibibytes, falling back to a default if not set. If no suffix is provided then Gibibytes are assumed.

Definition Classes
    [ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html "org.apache.spark.ReadOnlySparkConf")

Exceptions thrown

`NumberFormatException` If the value cannot be interpreted as Gibibytes
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#getSizeAsGb\(key:String\):Long "Permalink") def getSizeAsGb(key: String): Long
Get a size parameter as Gibibytes; throws a NoSuchElementException if it's not set.
Get a size parameter as Gibibytes; throws a NoSuchElementException if it's not set. If no suffix is provided then Gibibytes are assumed.

Definition Classes
    [ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html "org.apache.spark.ReadOnlySparkConf")

Exceptions thrown

`NumberFormatException` If the value cannot be interpreted as Gibibytes
[`java.util.NoSuchElementException`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/NoSuchElementException.html "java.util.NoSuchElementException") If the size parameter is not set
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#getSizeAsKb\(key:String,defaultValue:String\):Long "Permalink") def getSizeAsKb(key: String, defaultValue: String): Long
Get a size parameter as Kibibytes, falling back to a default if not set.
Get a size parameter as Kibibytes, falling back to a default if not set. If no suffix is provided then Kibibytes are assumed.

Definition Classes
    [ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html "org.apache.spark.ReadOnlySparkConf")

Exceptions thrown

`NumberFormatException` If the value cannot be interpreted as Kibibytes
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#getSizeAsKb\(key:String\):Long "Permalink") def getSizeAsKb(key: String): Long
Get a size parameter as Kibibytes; throws a NoSuchElementException if it's not set.
Get a size parameter as Kibibytes; throws a NoSuchElementException if it's not set. If no suffix is provided then Kibibytes are assumed.

Definition Classes
    [ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html "org.apache.spark.ReadOnlySparkConf")

Exceptions thrown

`NumberFormatException` If the value cannot be interpreted as Kibibytes
[`java.util.NoSuchElementException`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/NoSuchElementException.html "java.util.NoSuchElementException") If the size parameter is not set
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#getSizeAsMb\(key:String,defaultValue:String\):Long "Permalink") def getSizeAsMb(key: String, defaultValue: String): Long
Get a size parameter as Mebibytes, falling back to a default if not set.
Get a size parameter as Mebibytes, falling back to a default if not set. If no suffix is provided then Mebibytes are assumed.

Definition Classes
    [ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html "org.apache.spark.ReadOnlySparkConf")

Exceptions thrown

`NumberFormatException` If the value cannot be interpreted as Mebibytes
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#getSizeAsMb\(key:String\):Long "Permalink") def getSizeAsMb(key: String): Long
Get a size parameter as Mebibytes; throws a NoSuchElementException if it's not set.
Get a size parameter as Mebibytes; throws a NoSuchElementException if it's not set. If no suffix is provided then Mebibytes are assumed.

Definition Classes
    [ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html "org.apache.spark.ReadOnlySparkConf")

Exceptions thrown

`NumberFormatException` If the value cannot be interpreted as Mebibytes
[`java.util.NoSuchElementException`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/NoSuchElementException.html "java.util.NoSuchElementException") If the size parameter is not set
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#getTimeAsMs\(key:String,defaultValue:String\):Long "Permalink") def getTimeAsMs(key: String, defaultValue: String): Long
Get a time parameter as milliseconds, falling back to a default if not set.
Get a time parameter as milliseconds, falling back to a default if not set. If no suffix is provided then milliseconds are assumed.

Definition Classes
    [ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html "org.apache.spark.ReadOnlySparkConf")

Exceptions thrown

`NumberFormatException` If the value cannot be interpreted as milliseconds
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#getTimeAsMs\(key:String\):Long "Permalink") def getTimeAsMs(key: String): Long
Get a time parameter as milliseconds; throws a NoSuchElementException if it's not set.
Get a time parameter as milliseconds; throws a NoSuchElementException if it's not set. If no suffix is provided then milliseconds are assumed.

Definition Classes
    [ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html "org.apache.spark.ReadOnlySparkConf")

Exceptions thrown

`NumberFormatException` If the value cannot be interpreted as milliseconds
[`java.util.NoSuchElementException`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/NoSuchElementException.html "java.util.NoSuchElementException") If the time parameter is not set
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#getTimeAsSeconds\(key:String,defaultValue:String\):Long "Permalink") def getTimeAsSeconds(key: String, defaultValue: String): Long
Get a time parameter as seconds, falling back to a default if not set.
Get a time parameter as seconds, falling back to a default if not set. If no suffix is provided then seconds are assumed.

Definition Classes
    [ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html "org.apache.spark.ReadOnlySparkConf")

Exceptions thrown

`NumberFormatException` If the value cannot be interpreted as seconds
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#getTimeAsSeconds\(key:String\):Long "Permalink") def getTimeAsSeconds(key: String): Long
Get a time parameter as seconds; throws a NoSuchElementException if it's not set.
Get a time parameter as seconds; throws a NoSuchElementException if it's not set. If no suffix is provided then seconds are assumed.

Definition Classes
    [ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html "org.apache.spark.ReadOnlySparkConf")

Exceptions thrown

`NumberFormatException` If the value cannot be interpreted as seconds
[`java.util.NoSuchElementException`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/NoSuchElementException.html "java.util.NoSuchElementException") If the time parameter is not set

### Inherited from AnyRef
### Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html###:Int "Permalink") final  def ##: Int

Definition Classes
    AnyRef → Any
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#equals\(x$1:Object\):Boolean "Permalink") def equals(arg0: AnyRef): Boolean

Definition Classes
    AnyRef → Any
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef]

Definition Classes
    AnyRef → Any

Annotations
     @IntrinsicCandidate() @native()
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#hashCode\(\):Int "Permalink") def hashCode(): Int

Definition Classes
    AnyRef → Any

Annotations
     @IntrinsicCandidate() @native()
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#notify\(\):Unit "Permalink") final  def notify(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0

Definition Classes
    AnyRef
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#toString\(\):String "Permalink") def toString(): [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String")

Definition Classes
    AnyRef → Any
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#wait\(\):Unit "Permalink") final  def wait(): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#finalize\(\):Unit "Permalink") def finalize(): Unit

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
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0

Definition Classes
    Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean

Definition Classes
    Any

### Ungrouped
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#LogStringContextextendsAnyRef "Permalink") implicit  class LogStringContext extends AnyRef

Definition Classes
    Logging

  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html###:Int "Permalink") final  def ##: Int

Definition Classes
    AnyRef → Any
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#MDC\(key:org.apache.spark.internal.LogKey,value:Any\):org.apache.spark.internal.MDC "Permalink") def MDC(key: LogKey, value: Any): MDC

Attributes
    protected

Definition Classes
    Logging
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0

Definition Classes
    Any
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#catchIllegalValue\[T\]\(key:String\)\(getValue:=>T\):T "Permalink") def catchIllegalValue[T](key: String)(getValue: => T): T
Wrapper method for get() methods which require some specific value format.
Wrapper method for get() methods which require some specific value format. This catches any NumberFormatException or IllegalArgumentException and re-raises it with the incorrectly configured key in the exception message.

Attributes
    protected

Definition Classes
    [ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html "org.apache.spark.ReadOnlySparkConf")
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#clone\(\):org.apache.spark.SparkConf "Permalink") def clone(): [SparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html "org.apache.spark.SparkConf")
Copy this object
Copy this object

Definition Classes
     [SparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html "org.apache.spark.SparkConf") → AnyRef
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#contains\(key:String\):Boolean "Permalink") def contains(key: String): Boolean
Does the configuration contain a given parameter?
Does the configuration contain a given parameter?

Definition Classes
     [SparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html "org.apache.spark.SparkConf") → [ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html "org.apache.spark.ReadOnlySparkConf")
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#contains\(entry:org.apache.spark.internal.config.ConfigEntry\[_\]\):Boolean "Permalink") def contains(entry: ConfigEntry[_]): Boolean
Does the configuration have the typed config entry?
Does the configuration have the typed config entry?

Definition Classes
    [ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html "org.apache.spark.ReadOnlySparkConf")
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#equals\(x$1:Object\):Boolean "Permalink") def equals(arg0: AnyRef): Boolean

Definition Classes
    AnyRef → Any
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#get\(key:String,defaultValue:String\):String "Permalink") def get(key: String, defaultValue: String): String
Get a parameter, falling back to a default if not set
Get a parameter, falling back to a default if not set

Definition Classes
    [ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html "org.apache.spark.ReadOnlySparkConf")
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#get\(key:String\):String "Permalink") def get(key: String): String
Get a parameter; throws a NoSuchElementException if it's not set
Get a parameter; throws a NoSuchElementException if it's not set

Definition Classes
    [ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html "org.apache.spark.ReadOnlySparkConf")
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#getAll:Array\[\(String,String\)\] "Permalink") def getAll: Array[(String, String)]
Get all parameters as a list of pairs
Get all parameters as a list of pairs

Definition Classes
     [SparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html "org.apache.spark.SparkConf") → [ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html "org.apache.spark.ReadOnlySparkConf")
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#getAllWithPrefix\[K\]\(prefix:String,f:String=>K\):Array\[\(K,String\)\] "Permalink") def getAllWithPrefix[K](prefix: String, f: (String) => K): Array[(K, String)]
Get all parameters that start with `prefix` and apply f.
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#getAllWithPrefix\(prefix:String\):Array\[\(String,String\)\] "Permalink") def getAllWithPrefix(prefix: String): Array[(String, String)]
Get all parameters that start with `prefix`
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#getAppId:String "Permalink") def getAppId: String
Returns the Spark application id, valid in the Driver after TaskScheduler registration and from the start in the Executor.
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#getAvroSchema:Map\[Long,String\] "Permalink") def getAvroSchema: Map[Long, String]
Gets all the avro schemas in the configuration used in the generic Avro record serializer
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#getBoolean\(key:String,defaultValue:Boolean\):Boolean "Permalink") def getBoolean(key: String, defaultValue: Boolean): Boolean
Get a parameter as a boolean, falling back to a default if not set
Get a parameter as a boolean, falling back to a default if not set

Definition Classes
    [ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html "org.apache.spark.ReadOnlySparkConf")

Exceptions thrown

`IllegalArgumentException` If the value cannot be interpreted as a boolean
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef]

Definition Classes
    AnyRef → Any

Annotations
     @IntrinsicCandidate() @native()
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#getDouble\(key:String,defaultValue:Double\):Double "Permalink") def getDouble(key: String, defaultValue: Double): Double
Get a parameter as a double, falling back to a default if not ste
Get a parameter as a double, falling back to a default if not ste

Definition Classes
    [ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html "org.apache.spark.ReadOnlySparkConf")

Exceptions thrown

`NumberFormatException` If the value cannot be interpreted as a double
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#getExecutorEnv:Seq\[\(String,String\)\] "Permalink") def getExecutorEnv: Seq[(String, String)]
Get all executor environment variables set on this SparkConf
  23. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#getInt\(key:String,defaultValue:Int\):Int "Permalink") def getInt(key: String, defaultValue: Int): Int
Get a parameter as an integer, falling back to a default if not set
Get a parameter as an integer, falling back to a default if not set

Definition Classes
    [ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html "org.apache.spark.ReadOnlySparkConf")

Exceptions thrown

`NumberFormatException` If the value cannot be interpreted as an integer
  24. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#getLong\(key:String,defaultValue:Long\):Long "Permalink") def getLong(key: String, defaultValue: Long): Long
Get a parameter as a long, falling back to a default if not set
Get a parameter as a long, falling back to a default if not set

Definition Classes
    [ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html "org.apache.spark.ReadOnlySparkConf")

Exceptions thrown

`NumberFormatException` If the value cannot be interpreted as a long
  25. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#getOption\(key:String\):Option\[String\] "Permalink") def getOption(key: String): Option[String]
Get a parameter as an Option
Get a parameter as an Option

Definition Classes
     [SparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html "org.apache.spark.SparkConf") → [ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html "org.apache.spark.ReadOnlySparkConf")
  26. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#getSizeAsBytes\(key:String,defaultValue:Long\):Long "Permalink") def getSizeAsBytes(key: String, defaultValue: Long): Long
Get a size parameter as bytes, falling back to a default if not set.
Get a size parameter as bytes, falling back to a default if not set.

Definition Classes
    [ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html "org.apache.spark.ReadOnlySparkConf")

Exceptions thrown

`NumberFormatException` If the value cannot be interpreted as bytes
  27. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#getSizeAsBytes\(key:String,defaultValue:String\):Long "Permalink") def getSizeAsBytes(key: String, defaultValue: String): Long
Get a size parameter as bytes, falling back to a default if not set.
Get a size parameter as bytes, falling back to a default if not set. If no suffix is provided then bytes are assumed.

Definition Classes
    [ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html "org.apache.spark.ReadOnlySparkConf")

Exceptions thrown

`NumberFormatException` If the value cannot be interpreted as bytes
  28. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#getSizeAsBytes\(key:String\):Long "Permalink") def getSizeAsBytes(key: String): Long
Get a size parameter as bytes; throws a NoSuchElementException if it's not set.
Get a size parameter as bytes; throws a NoSuchElementException if it's not set. If no suffix is provided then bytes are assumed.

Definition Classes
    [ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html "org.apache.spark.ReadOnlySparkConf")

Exceptions thrown

`NumberFormatException` If the value cannot be interpreted as bytes
[`java.util.NoSuchElementException`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/NoSuchElementException.html "java.util.NoSuchElementException") If the size parameter is not set
  29. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#getSizeAsGb\(key:String,defaultValue:String\):Long "Permalink") def getSizeAsGb(key: String, defaultValue: String): Long
Get a size parameter as Gibibytes, falling back to a default if not set.
Get a size parameter as Gibibytes, falling back to a default if not set. If no suffix is provided then Gibibytes are assumed.

Definition Classes
    [ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html "org.apache.spark.ReadOnlySparkConf")

Exceptions thrown

`NumberFormatException` If the value cannot be interpreted as Gibibytes
  30. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#getSizeAsGb\(key:String\):Long "Permalink") def getSizeAsGb(key: String): Long
Get a size parameter as Gibibytes; throws a NoSuchElementException if it's not set.
Get a size parameter as Gibibytes; throws a NoSuchElementException if it's not set. If no suffix is provided then Gibibytes are assumed.

Definition Classes
    [ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html "org.apache.spark.ReadOnlySparkConf")

Exceptions thrown

`NumberFormatException` If the value cannot be interpreted as Gibibytes
[`java.util.NoSuchElementException`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/NoSuchElementException.html "java.util.NoSuchElementException") If the size parameter is not set
  31. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#getSizeAsKb\(key:String,defaultValue:String\):Long "Permalink") def getSizeAsKb(key: String, defaultValue: String): Long
Get a size parameter as Kibibytes, falling back to a default if not set.
Get a size parameter as Kibibytes, falling back to a default if not set. If no suffix is provided then Kibibytes are assumed.

Definition Classes
    [ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html "org.apache.spark.ReadOnlySparkConf")

Exceptions thrown

`NumberFormatException` If the value cannot be interpreted as Kibibytes
  32. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#getSizeAsKb\(key:String\):Long "Permalink") def getSizeAsKb(key: String): Long
Get a size parameter as Kibibytes; throws a NoSuchElementException if it's not set.
Get a size parameter as Kibibytes; throws a NoSuchElementException if it's not set. If no suffix is provided then Kibibytes are assumed.

Definition Classes
    [ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html "org.apache.spark.ReadOnlySparkConf")

Exceptions thrown

`NumberFormatException` If the value cannot be interpreted as Kibibytes
[`java.util.NoSuchElementException`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/NoSuchElementException.html "java.util.NoSuchElementException") If the size parameter is not set
  33. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#getSizeAsMb\(key:String,defaultValue:String\):Long "Permalink") def getSizeAsMb(key: String, defaultValue: String): Long
Get a size parameter as Mebibytes, falling back to a default if not set.
Get a size parameter as Mebibytes, falling back to a default if not set. If no suffix is provided then Mebibytes are assumed.

Definition Classes
    [ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html "org.apache.spark.ReadOnlySparkConf")

Exceptions thrown

`NumberFormatException` If the value cannot be interpreted as Mebibytes
  34. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#getSizeAsMb\(key:String\):Long "Permalink") def getSizeAsMb(key: String): Long
Get a size parameter as Mebibytes; throws a NoSuchElementException if it's not set.
Get a size parameter as Mebibytes; throws a NoSuchElementException if it's not set. If no suffix is provided then Mebibytes are assumed.

Definition Classes
    [ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html "org.apache.spark.ReadOnlySparkConf")

Exceptions thrown

`NumberFormatException` If the value cannot be interpreted as Mebibytes
[`java.util.NoSuchElementException`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/NoSuchElementException.html "java.util.NoSuchElementException") If the size parameter is not set
  35. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#getTimeAsMs\(key:String,defaultValue:String\):Long "Permalink") def getTimeAsMs(key: String, defaultValue: String): Long
Get a time parameter as milliseconds, falling back to a default if not set.
Get a time parameter as milliseconds, falling back to a default if not set. If no suffix is provided then milliseconds are assumed.

Definition Classes
    [ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html "org.apache.spark.ReadOnlySparkConf")

Exceptions thrown

`NumberFormatException` If the value cannot be interpreted as milliseconds
  36. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#getTimeAsMs\(key:String\):Long "Permalink") def getTimeAsMs(key: String): Long
Get a time parameter as milliseconds; throws a NoSuchElementException if it's not set.
Get a time parameter as milliseconds; throws a NoSuchElementException if it's not set. If no suffix is provided then milliseconds are assumed.

Definition Classes
    [ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html "org.apache.spark.ReadOnlySparkConf")

Exceptions thrown

`NumberFormatException` If the value cannot be interpreted as milliseconds
[`java.util.NoSuchElementException`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/NoSuchElementException.html "java.util.NoSuchElementException") If the time parameter is not set
  37. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#getTimeAsSeconds\(key:String,defaultValue:String\):Long "Permalink") def getTimeAsSeconds(key: String, defaultValue: String): Long
Get a time parameter as seconds, falling back to a default if not set.
Get a time parameter as seconds, falling back to a default if not set. If no suffix is provided then seconds are assumed.

Definition Classes
    [ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html "org.apache.spark.ReadOnlySparkConf")

Exceptions thrown

`NumberFormatException` If the value cannot be interpreted as seconds
  38. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#getTimeAsSeconds\(key:String\):Long "Permalink") def getTimeAsSeconds(key: String): Long
Get a time parameter as seconds; throws a NoSuchElementException if it's not set.
Get a time parameter as seconds; throws a NoSuchElementException if it's not set. If no suffix is provided then seconds are assumed.

Definition Classes
    [ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html "org.apache.spark.ReadOnlySparkConf")

Exceptions thrown

`NumberFormatException` If the value cannot be interpreted as seconds
[`java.util.NoSuchElementException`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/NoSuchElementException.html "java.util.NoSuchElementException") If the time parameter is not set
  39. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#hashCode\(\):Int "Permalink") def hashCode(): Int

Definition Classes
    AnyRef → Any

Annotations
     @IntrinsicCandidate() @native()
  40. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#initializeLogIfNecessary\(isInterpreter:Boolean,silent:Boolean\):Boolean "Permalink") def initializeLogIfNecessary(isInterpreter: Boolean, silent: Boolean): Boolean

Attributes
    protected

Definition Classes
    Logging
  41. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#initializeLogIfNecessary\(isInterpreter:Boolean\):Unit "Permalink") def initializeLogIfNecessary(isInterpreter: Boolean): Unit

Attributes
    protected

Definition Classes
    Logging
  42. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean

Definition Classes
    Any
  43. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#isTraceEnabled\(\):Boolean "Permalink") def isTraceEnabled(): Boolean

Attributes
    protected

Definition Classes
    Logging
  44. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#log:org.slf4j.Logger "Permalink") def log: Logger

Attributes
    protected

Definition Classes
    Logging
  45. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#logBasedOnLevel\(level:org.slf4j.event.Level\)\(f:=>org.apache.spark.internal.MessageWithContext\):Unit "Permalink") def logBasedOnLevel(level: Level)(f: => MessageWithContext): Unit

Attributes
    protected

Definition Classes
    Logging
  46. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#logDebug\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logDebug(msg: => String, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  47. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#logDebug\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logDebug(entry: LogEntry, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  48. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#logDebug\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logDebug(entry: LogEntry): Unit

Attributes
    protected

Definition Classes
    Logging
  49. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#logDebug\(msg:=>String\):Unit "Permalink") def logDebug(msg: => String): Unit

Attributes
    protected

Definition Classes
    Logging
  50. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#logError\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logError(msg: => String, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  51. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#logError\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logError(entry: LogEntry, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  52. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#logError\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logError(entry: LogEntry): Unit

Attributes
    protected

Definition Classes
    Logging
  53. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#logError\(msg:=>String\):Unit "Permalink") def logError(msg: => String): Unit

Attributes
    protected

Definition Classes
    Logging
  54. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#logInfo\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logInfo(msg: => String, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  55. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#logInfo\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logInfo(entry: LogEntry, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  56. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#logInfo\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logInfo(entry: LogEntry): Unit

Attributes
    protected

Definition Classes
    Logging
  57. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#logInfo\(msg:=>String\):Unit "Permalink") def logInfo(msg: => String): Unit

Attributes
    protected

Definition Classes
    Logging
  58. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#logName:String "Permalink") def logName: [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String")

Attributes
    protected

Definition Classes
    Logging
  59. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#logTrace\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logTrace(msg: => String, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  60. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#logTrace\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logTrace(entry: LogEntry, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  61. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#logTrace\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logTrace(entry: LogEntry): Unit

Attributes
    protected

Definition Classes
    Logging
  62. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#logTrace\(msg:=>String\):Unit "Permalink") def logTrace(msg: => String): Unit

Attributes
    protected

Definition Classes
    Logging
  63. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#logWarning\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logWarning(msg: => String, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  64. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#logWarning\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logWarning(entry: LogEntry, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  65. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#logWarning\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logWarning(entry: LogEntry): Unit

Attributes
    protected

Definition Classes
    Logging
  66. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#logWarning\(msg:=>String\):Unit "Permalink") def logWarning(msg: => String): Unit

Attributes
    protected

Definition Classes
    Logging
  67. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  68. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#notify\(\):Unit "Permalink") final  def notify(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  69. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  70. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#registerAvroSchemas\(schemas:org.apache.avro.Schema*\):org.apache.spark.SparkConf "Permalink") def registerAvroSchemas(schemas: Schema*): [SparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html "org.apache.spark.SparkConf")
Use Kryo serialization and register the given set of Avro schemas so that the generic record serializer can decrease network IO
  71. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#registerKryoClasses\(classes:Array\[Class\[_\]\]\):org.apache.spark.SparkConf "Permalink") def registerKryoClasses(classes: Array[Class[_]]): [SparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html "org.apache.spark.SparkConf")
Use Kryo serialization and register the given set of classes with Kryo.
Use Kryo serialization and register the given set of classes with Kryo. If called multiple times, this will append the classes from all calls together.
  72. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#remove\(key:String\):org.apache.spark.SparkConf "Permalink") def remove(key: String): [SparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html "org.apache.spark.SparkConf")
Remove a parameter from the configuration
  73. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#set\(key:String,value:String\):org.apache.spark.SparkConf "Permalink") def set(key: String, value: String): [SparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html "org.apache.spark.SparkConf")
Set a configuration variable.
  74. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#setAll\(settings:Iterable\[\(String,String\)\]\):org.apache.spark.SparkConf "Permalink") def setAll(settings: Iterable[(String, String)]): [SparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html "org.apache.spark.SparkConf")
Set multiple parameters together
  75. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#setAppName\(name:String\):org.apache.spark.SparkConf "Permalink") def setAppName(name: String): [SparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html "org.apache.spark.SparkConf")
Set a name for your application.
Set a name for your application. Shown in the Spark web UI.
  76. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#setExecutorEnv\(variables:Array\[\(String,String\)\]\):org.apache.spark.SparkConf "Permalink") def setExecutorEnv(variables: Array[(String, String)]): [SparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html "org.apache.spark.SparkConf")
Set multiple environment variables to be used when launching executors.
Set multiple environment variables to be used when launching executors. (Java-friendly version.)
  77. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#setExecutorEnv\(variables:Seq\[\(String,String\)\]\):org.apache.spark.SparkConf "Permalink") def setExecutorEnv(variables: Seq[(String, String)]): [SparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html "org.apache.spark.SparkConf")
Set multiple environment variables to be used when launching executors.
Set multiple environment variables to be used when launching executors. These variables are stored as properties of the form spark.executorEnv.VAR_NAME (for example spark.executorEnv.PATH) but this method makes them easier to set.
  78. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#setExecutorEnv\(variable:String,value:String\):org.apache.spark.SparkConf "Permalink") def setExecutorEnv(variable: String, value: String): [SparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html "org.apache.spark.SparkConf")
Set an environment variable to be used when launching executors for this application.
Set an environment variable to be used when launching executors for this application. These variables are stored as properties of the form spark.executorEnv.VAR_NAME (for example spark.executorEnv.PATH) but this method makes them easier to set.
  79. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#setIfMissing\(key:String,value:String\):org.apache.spark.SparkConf "Permalink") def setIfMissing(key: String, value: String): [SparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html "org.apache.spark.SparkConf")
Set a parameter if it isn't already configured
  80. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#setJars\(jars:Array\[String\]\):org.apache.spark.SparkConf "Permalink") def setJars(jars: Array[String]): [SparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html "org.apache.spark.SparkConf")
Set JAR files to distribute to the cluster.
Set JAR files to distribute to the cluster. (Java-friendly version.)
  81. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#setJars\(jars:Seq\[String\]\):org.apache.spark.SparkConf "Permalink") def setJars(jars: Seq[String]): [SparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html "org.apache.spark.SparkConf")
Set JAR files to distribute to the cluster.
  82. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#setMaster\(master:String\):org.apache.spark.SparkConf "Permalink") def setMaster(master: String): [SparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html "org.apache.spark.SparkConf")
The master URL to connect to, such as "local" to run locally with one thread, "local[4]" to run locally with 4 cores, or "spark://master:7077" to run on a Spark standalone cluster.
  83. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#setSparkHome\(home:String\):org.apache.spark.SparkConf "Permalink") def setSparkHome(home: String): [SparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html "org.apache.spark.SparkConf")
Set the location where Spark is installed on worker nodes.
  84. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0

Definition Classes
    AnyRef
  85. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#toDebugString:String "Permalink") def toDebugString: String
Return a string listing all keys and values, one per line.
Return a string listing all keys and values, one per line. This is useful to print the configuration out for debugging.
  86. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#toString\(\):String "Permalink") def toString(): [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String")

Definition Classes
    AnyRef → Any
  87. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])
  88. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  89. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#wait\(\):Unit "Permalink") final  def wait(): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])
  90. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#withLogContext\(context:java.util.Map\[String,String\]\)\(body:=>Unit\):Unit "Permalink") def withLogContext(context: [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#java.util.Map "java.util.Map")[String, String])(body: => Unit): Unit

Attributes
    protected

Definition Classes
    Logging
  91. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html#finalize\(\):Unit "Permalink") def finalize(): Unit

Attributes
    protected[lang]

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.Throwable]) @Deprecated

Deprecated

_(Since version 9)_
