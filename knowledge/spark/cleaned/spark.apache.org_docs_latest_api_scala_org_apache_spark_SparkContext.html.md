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

[c](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext$.html "See companion object")
[org](https://spark.apache.org/docs/latest/api/scala/org/index.html "org").[apache](https://spark.apache.org/docs/latest/api/scala/org/apache/index.html "org.apache").[spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
#  [SparkContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext$.html "See companion object")[ __](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html "Permalink")
###
Companion [object SparkContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext$.html "See companion object")
####  class SparkContext extends Logging
Main entry point for Spark functionality. A SparkContext represents the connection to a Spark cluster, and can be used to create RDDs, accumulators and broadcast variables on that cluster.

Source
    [SparkContext.scala](https://github.com/apache/spark/tree/v4.1.2/core/src/main/scala/org/apache/spark/SparkContext.scala)

Note

Only one `SparkContext` should be active per JVM. You must `stop()` the active `SparkContext` before creating a new one.
Linear Supertypes
Logging, AnyRef, Any
__ __
Ordering
  1. Alphabetic
  2. By Inheritance

Inherited

  1. SparkContext
  2. Logging
  3. AnyRef
  4. Any

  1. Hide All
  2. Show All

Visibility
  1. Public
  2. Protected

### Instance Constructors
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#<init>\(master:String,appName:String,sparkHome:String,jars:Seq\[String\],environment:scala.collection.Map\[String,String\]\):org.apache.spark.SparkContext "Permalink") new SparkContext(master: String, appName: String, sparkHome: String = null, jars: Seq[String] = Nil, environment: Map[String, String] = Map())
Alternative constructor that allows setting common Spark properties directly
Alternative constructor that allows setting common Spark properties directly

master

Cluster URL to connect to (e.g. spark://host:port, local[4]).

appName

A name for your application, to display on the cluster web UI.

sparkHome

Location where Spark is installed on cluster nodes.

jars

Collection of JARs to send to the cluster. These can be paths on the local file system or HDFS, HTTP, HTTPS, or FTP URLs.

environment

Environment variables to set on worker nodes.
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#<init>\(master:String,appName:String,conf:org.apache.spark.SparkConf\):org.apache.spark.SparkContext "Permalink") new SparkContext(master: String, appName: String, conf: [SparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html "org.apache.spark.SparkConf"))
Alternative constructor that allows setting common Spark properties directly
Alternative constructor that allows setting common Spark properties directly

master

Cluster URL to connect to (e.g. spark://host:port, local[4]).

appName

A name for your application, to display on the cluster web UI

conf

a [org.apache.spark.SparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html "org.apache.spark.SparkConf") object specifying other Spark parameters
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#<init>\(\):org.apache.spark.SparkContext "Permalink") new SparkContext()
Create a SparkContext that loads settings from system properties (for instance, when launching with ./bin/spark-submit).
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#<init>\(config:org.apache.spark.SparkConf\):org.apache.spark.SparkContext "Permalink") new SparkContext(config: [SparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html "org.apache.spark.SparkConf"))

config

a Spark Config object describing the application configuration. Any settings in this config overrides the default configs as well as system properties.

### Type Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#LogStringContextextendsAnyRef "Permalink") implicit  class LogStringContext extends AnyRef

Definition Classes
    Logging

### Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html###:Int "Permalink") final  def ##: Int

Definition Classes
    AnyRef → Any
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#MDC\(key:org.apache.spark.internal.LogKey,value:Any\):org.apache.spark.internal.MDC "Permalink") def MDC(key: LogKey, value: Any): MDC

Attributes
    protected

Definition Classes
    Logging
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#addArchive\(path:String\):Unit "Permalink") def addArchive(path: String): Unit
Add an archive to be downloaded and unpacked with this Spark job on every node.
Add an archive to be downloaded and unpacked with this Spark job on every node.
If an archive is added during execution, it will not be available until the next TaskSet starts.

path

can be either a local file, a file in HDFS (or other Hadoop-supported filesystems), or an HTTP, HTTPS or FTP URI. To access the file in Spark jobs, use `SparkFiles.get(paths-to-files)` to find its download/unpacked location. The given path should be one of .zip, .tar, .tar.gz, .tgz and .jar.

Annotations
     @Experimental()

Since

3.1.0

Note

A path can be added only once. Subsequent additions of the same path are ignored.
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#addFile\(path:String,recursive:Boolean\):Unit "Permalink") def addFile(path: String, recursive: Boolean): Unit
Add a file to be downloaded with this Spark job on every node.
Add a file to be downloaded with this Spark job on every node.
If a file is added during execution, it will not be available until the next TaskSet starts.

path

can be either a local file, a file in HDFS (or other Hadoop-supported filesystems), or an HTTP, HTTPS or FTP URI. To access the file in Spark jobs, use `SparkFiles.get(fileName)` to find its download location.

recursive

if true, a directory can be given in `path`. Currently directories are only supported for Hadoop-supported filesystems.

Note

A path can be added only once. Subsequent additions of the same path are ignored.
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#addFile\(path:String\):Unit "Permalink") def addFile(path: String): Unit
Add a file to be downloaded with this Spark job on every node.
Add a file to be downloaded with this Spark job on every node.
If a file is added during execution, it will not be available until the next TaskSet starts.

path

can be either a local file, a file in HDFS (or other Hadoop-supported filesystems), or an HTTP, HTTPS or FTP URI. To access the file in Spark jobs, use `SparkFiles.get(fileName)` to find its download location.

Note

A path can be added only once. Subsequent additions of the same path are ignored.
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#addJar\(path:String\):Unit "Permalink") def addJar(path: String): Unit
Adds a JAR dependency for all tasks to be executed on this `SparkContext` in the future.
Adds a JAR dependency for all tasks to be executed on this `SparkContext` in the future.
If a jar is added during execution, it will not be available until the next TaskSet starts.

path

can be either a local file, a file in HDFS (or other Hadoop-supported filesystems), an HTTP, HTTPS or FTP URI, or local:/path for a file on every worker node.

Note

A path can be added only once. Subsequent additions of the same path are ignored.
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#addJobTag\(tag:String\):Unit "Permalink") def addJobTag(tag: String): Unit
Add a tag to be assigned to all the jobs started by this thread.
Add a tag to be assigned to all the jobs started by this thread.
Often, a unit of execution in an application consists of multiple Spark actions or jobs. Application programmers can use this method to group all those jobs together and give a group tag. The application can use `org.apache.spark.sql.SparkSession.interruptTag` to cancel all running executions with this tag. For example:

```
// In the main thread:
sc.addJobTag("myjobs")
sc.parallelize(1 to 10000, 2).map { i => Thread.sleep(10); i }.count()

// In a separate thread:
spark.cancelJobsWithTag("myjobs")
```

There may be multiple tags present at the same time, so different parts of application may use different tags to perform cancellation at different levels of granularity.

tag

The tag to be added. Cannot contain ',' (comma) character.

Since

3.5.0
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#addJobTags\(tags:Set\[String\]\):Unit "Permalink") def addJobTags(tags: Set[String]): Unit
Add multiple tags to be assigned to all the jobs started by this thread.
Add multiple tags to be assigned to all the jobs started by this thread. See [addJobTag](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#addJobTag\(tag:String\):Unit) for more details.

tags

The tags to be added. Cannot contain ',' (comma) character.

Since

4.0.0
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#addSparkListener\(listener:org.apache.spark.scheduler.SparkListenerInterface\):Unit "Permalink") def addSparkListener(listener: SparkListenerInterface): Unit
Register a listener to receive up-calls from events that happen during execution.
Register a listener to receive up-calls from events that happen during execution.

Annotations
     @DeveloperApi()
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#appName:String "Permalink") def appName: String
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#applicationAttemptId:Option\[String\] "Permalink") def applicationAttemptId: Option[String]
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#applicationId:String "Permalink") def applicationId: String
A unique identifier for the Spark application.
A unique identifier for the Spark application. Its format depends on the scheduler implementation. (i.e. in case of local spark app something like 'local-1433865536131' in case of YARN something like 'application_1433865536131_34483' )
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#archives:Seq\[String\] "Permalink") def archives: Seq[String]
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0

Definition Classes
    Any
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#binaryFiles\(path:String,minPartitions:Int\):org.apache.spark.rdd.RDD\[\(String,org.apache.spark.input.PortableDataStream\)\] "Permalink") def binaryFiles(path: String, minPartitions: Int = [defaultMinPartitions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#defaultMinPartitions:Int)): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(String, [PortableDataStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/input/PortableDataStream.html "org.apache.spark.input.PortableDataStream"))]
Get an RDD for a Hadoop-readable dataset as PortableDataStream for each file (useful for binary data)
Get an RDD for a Hadoop-readable dataset as PortableDataStream for each file (useful for binary data)
For example, if you have the following files:

```
hdfs://a-hdfs-path/part-00000
hdfs://a-hdfs-path/part-00001
...
hdfs://a-hdfs-path/part-nnnnn
```

Do `val rdd = sparkContext.binaryFiles("hdfs://a-hdfs-path")`,
then `rdd` contains

```
(a-hdfs-path/part-00000, its content)
(a-hdfs-path/part-00001, its content)
...
(a-hdfs-path/part-nnnnn, its content)
```

path

Directory to the input data files, the path can be comma separated paths as the list of inputs.

minPartitions

A suggestion value of the minimal splitting number for input data.

returns

RDD representing tuples of file path and corresponding file content

Note

Small files are preferred; very large files may cause bad performance.
,
On some filesystems, `.../path/*` can be a more efficient way to read all files in a directory rather than `.../path/` or `.../path`
,
Partitioning is determined by data locality. This may result in too few partitions by default.
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#binaryRecords\(path:String,recordLength:Int,conf:org.apache.hadoop.conf.Configuration\):org.apache.spark.rdd.RDD\[Array\[Byte\]\] "Permalink") def binaryRecords(path: String, recordLength: Int, conf: Configuration = [hadoopConfiguration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#hadoopConfiguration:org.apache.hadoop.conf.Configuration)): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[Array[Byte]]
Load data from a flat binary file, assuming the length of each record is constant.
Load data from a flat binary file, assuming the length of each record is constant.

path

Directory to the input data files, the path can be comma separated paths as the list of inputs.

recordLength

The length at which to split the records

conf

Configuration for setting up the dataset.

returns

An RDD of data with values, represented as byte arrays

Note

We ensure that the byte array for each record in the resulting RDD has the provided record length.
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#broadcast\[T\]\(value:T\)\(implicitevidence$9:scala.reflect.ClassTag\[T\]\):org.apache.spark.broadcast.Broadcast\[T\] "Permalink") def broadcast[T](value: T)(implicit arg0: ClassTag[T]): [Broadcast](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/broadcast/Broadcast.html "org.apache.spark.broadcast.Broadcast")[T]
Broadcast a read-only variable to the cluster, returning a [org.apache.spark.broadcast.Broadcast](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/broadcast/Broadcast.html "org.apache.spark.broadcast.Broadcast") object for reading it in distributed functions.
Broadcast a read-only variable to the cluster, returning a [org.apache.spark.broadcast.Broadcast](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/broadcast/Broadcast.html "org.apache.spark.broadcast.Broadcast") object for reading it in distributed functions. The variable will be sent to each executor only once.

value

value to broadcast to the Spark nodes

returns

`Broadcast` object, a read-only variable cached on each machine
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#cancelAllJobs\(\):Unit "Permalink") def cancelAllJobs(): Unit
Cancel all jobs that have been scheduled or are running.
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#cancelJob\(jobId:Int\):Unit "Permalink") def cancelJob(jobId: Int): Unit
Cancel a given job if it's scheduled or running.
Cancel a given job if it's scheduled or running.

jobId

the job ID to cancel

Note

Throws `InterruptedException` if the cancel message cannot be sent
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#cancelJob\(jobId:Int,reason:String\):Unit "Permalink") def cancelJob(jobId: Int, reason: String): Unit
Cancel a given job if it's scheduled or running.
Cancel a given job if it's scheduled or running.

jobId

the job ID to cancel

reason

reason for cancellation

Note

Throws `InterruptedException` if the cancel message cannot be sent
  23. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#cancelJobGroup\(groupId:String\):Unit "Permalink") def cancelJobGroup(groupId: String): Unit
Cancel active jobs for the specified group.
Cancel active jobs for the specified group. See `org.apache.spark.SparkContext.setJobGroup` for more information.

groupId

the group ID to cancel
  24. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#cancelJobGroup\(groupId:String,reason:String\):Unit "Permalink") def cancelJobGroup(groupId: String, reason: String): Unit
Cancel active jobs for the specified group.
Cancel active jobs for the specified group. See `org.apache.spark.SparkContext.setJobGroup` for more information.

groupId

the group ID to cancel

reason

reason for cancellation

Since

4.0.0
  25. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#cancelJobGroupAndFutureJobs\(groupId:String\):Unit "Permalink") def cancelJobGroupAndFutureJobs(groupId: String): Unit
Cancel active jobs for the specified group, as well as the future jobs in this job group.
Cancel active jobs for the specified group, as well as the future jobs in this job group. Note: the maximum number of job groups that can be tracked is set by 'spark.scheduler.numCancelledJobGroupsToTrack'. Once the limit is reached and a new job group is to be added, the oldest job group tracked will be discarded.

groupId

the group ID to cancel
  26. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#cancelJobGroupAndFutureJobs\(groupId:String,reason:String\):Unit "Permalink") def cancelJobGroupAndFutureJobs(groupId: String, reason: String): Unit
Cancel active jobs for the specified group, as well as the future jobs in this job group.
Cancel active jobs for the specified group, as well as the future jobs in this job group. Note: the maximum number of job groups that can be tracked is set by 'spark.scheduler.numCancelledJobGroupsToTrack'. Once the limit is reached and a new job group is to be added, the oldest job group tracked will be discarded.

groupId

the group ID to cancel

reason

reason for cancellation

Since

4.0.0
  27. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#cancelJobsWithTag\(tag:String\):Unit "Permalink") def cancelJobsWithTag(tag: String): Unit
Cancel active jobs that have the specified tag.
Cancel active jobs that have the specified tag. See `org.apache.spark.SparkContext.addJobTag`.

tag

The tag to be cancelled. Cannot contain ',' (comma) character.

Since

3.5.0
  28. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#cancelJobsWithTag\(tag:String,reason:String\):Unit "Permalink") def cancelJobsWithTag(tag: String, reason: String): Unit
Cancel active jobs that have the specified tag.
Cancel active jobs that have the specified tag. See `org.apache.spark.SparkContext.addJobTag`.

tag

The tag to be cancelled. Cannot contain ',' (comma) character.

reason

reason for cancellation

Since

4.0.0
  29. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#cancelStage\(stageId:Int\):Unit "Permalink") def cancelStage(stageId: Int): Unit
Cancel a given stage and all jobs associated with it.
Cancel a given stage and all jobs associated with it.

stageId

the stage ID to cancel

Note

Throws `InterruptedException` if the cancel message cannot be sent
  30. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#cancelStage\(stageId:Int,reason:String\):Unit "Permalink") def cancelStage(stageId: Int, reason: String): Unit
Cancel a given stage and all jobs associated with it.
Cancel a given stage and all jobs associated with it.

stageId

the stage ID to cancel

reason

reason for cancellation

Note

Throws `InterruptedException` if the cancel message cannot be sent
  31. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#checkpointFile\[T\]\(path:String\)\(implicitevidence$5:scala.reflect.ClassTag\[T\]\):org.apache.spark.rdd.RDD\[T\] "Permalink") def checkpointFile[T](path: String)(implicit arg0: ClassTag[T]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[T]

Attributes
    protected[[spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")]
  32. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#clearCallSite\(\):Unit "Permalink") def clearCallSite(): Unit
Clear the thread-local property for overriding the call sites of actions and RDDs.
  33. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#clearJobGroup\(\):Unit "Permalink") def clearJobGroup(): Unit
Clear the current thread's job group ID and its description.
  34. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#clearJobTags\(\):Unit "Permalink") def clearJobTags(): Unit
Clear the current thread's job tags.
Clear the current thread's job tags.

Since

3.5.0
  35. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#clone\(\):Object "Permalink") def clone(): AnyRef

Attributes
    protected[lang]

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  36. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#collectionAccumulator\[T\]\(name:String\):org.apache.spark.util.CollectionAccumulator\[T\] "Permalink") def collectionAccumulator[T](name: String): [CollectionAccumulator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/CollectionAccumulator.html "org.apache.spark.util.CollectionAccumulator")[T]
Create and register a `CollectionAccumulator`, which starts with empty list and accumulates inputs by adding them into the list.
  37. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#collectionAccumulator\[T\]:org.apache.spark.util.CollectionAccumulator\[T\] "Permalink") def collectionAccumulator[T]: [CollectionAccumulator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/CollectionAccumulator.html "org.apache.spark.util.CollectionAccumulator")[T]
Create and register a `CollectionAccumulator`, which starts with empty list and accumulates inputs by adding them into the list.
  38. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#defaultMinPartitions:Int "Permalink") def defaultMinPartitions: Int
Default min number of partitions for Hadoop RDDs when not given by user Notice that we use math.min so the "defaultMinPartitions" cannot be higher than 2.
Default min number of partitions for Hadoop RDDs when not given by user Notice that we use math.min so the "defaultMinPartitions" cannot be higher than 2. For large files, the Hadoop InputFormat library always creates more partitions even though defaultMinPartitions is 2. For small files, it can be good to process small files quickly. However, usually when Spark joins a small table with a big one, we'll still spend most of time on the map part of the big one anyway.
  39. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#defaultParallelism:Int "Permalink") def defaultParallelism: Int
Default level of parallelism to use when not given by user (e.g.
Default level of parallelism to use when not given by user (e.g. parallelize and makeRDD).
  40. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#deployMode:String "Permalink") def deployMode: String
  41. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#doubleAccumulator\(name:String\):org.apache.spark.util.DoubleAccumulator "Permalink") def doubleAccumulator(name: String): [DoubleAccumulator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/DoubleAccumulator.html "org.apache.spark.util.DoubleAccumulator")
Create and register a double accumulator, which starts with 0 and accumulates inputs by `add`.
  42. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#doubleAccumulator:org.apache.spark.util.DoubleAccumulator "Permalink") def doubleAccumulator: [DoubleAccumulator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/DoubleAccumulator.html "org.apache.spark.util.DoubleAccumulator")
Create and register a double accumulator, which starts with 0 and accumulates inputs by `add`.
  43. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#emptyRDD\[T\]\(implicitevidence$8:scala.reflect.ClassTag\[T\]\):org.apache.spark.rdd.RDD\[T\] "Permalink") def emptyRDD[T](implicit arg0: ClassTag[T]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[T]
Get an RDD that has no partitions or elements.
  44. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  45. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#equals\(x$1:Object\):Boolean "Permalink") def equals(arg0: AnyRef): Boolean

Definition Classes
    AnyRef → Any
  46. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#files:Seq\[String\] "Permalink") def files: Seq[String]
  47. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#getAllPools:Seq\[org.apache.spark.scheduler.Schedulable\] "Permalink") def getAllPools: Seq[Schedulable]
Return pools for fair scheduler
Return pools for fair scheduler

Annotations
     @DeveloperApi()
  48. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#getCheckpointDir:Option\[String\] "Permalink") def getCheckpointDir: Option[String]
  49. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef]

Definition Classes
    AnyRef → Any

Annotations
     @IntrinsicCandidate() @native()
  50. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#getConf:org.apache.spark.SparkConf "Permalink") def getConf: [SparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html "org.apache.spark.SparkConf")
Return a copy of this SparkContext's configuration.
Return a copy of this SparkContext's configuration. The configuration _cannot_ be changed at runtime.
  51. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#getExecutorMemoryStatus:scala.collection.Map\[String,\(Long,Long\)\] "Permalink") def getExecutorMemoryStatus: Map[String, (Long, Long)]
Return a map from the block manager to the max memory available for caching and the remaining memory available for caching.
  52. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#getJobTags\(\):Set\[String\] "Permalink") def getJobTags(): Set[String]
Get the tags that are currently set to be assigned to all the jobs started by this thread.
Get the tags that are currently set to be assigned to all the jobs started by this thread.

Since

3.5.0
  53. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#getLocalProperty\(key:String\):String "Permalink") def getLocalProperty(key: String): String
Get a local property set in this thread, or null if it is missing.
Get a local property set in this thread, or null if it is missing. See `org.apache.spark.SparkContext.setLocalProperty`.
  54. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#getPersistentRDDs:scala.collection.Map\[Int,org.apache.spark.rdd.RDD\[_\]\] "Permalink") def getPersistentRDDs: Map[Int, [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[_]]
Returns an immutable map of RDDs that have marked themselves as persistent via cache() call.
Returns an immutable map of RDDs that have marked themselves as persistent via cache() call.

Note

This does not necessarily mean the caching or computation was successful.
  55. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#getPoolForName\(pool:String\):Option\[org.apache.spark.scheduler.Schedulable\] "Permalink") def getPoolForName(pool: String): Option[Schedulable]
Return the pool associated with the given name, if one exists
Return the pool associated with the given name, if one exists

Annotations
     @DeveloperApi()
  56. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#getRDDStorageInfo:Array\[org.apache.spark.storage.RDDInfo\] "Permalink") def getRDDStorageInfo: Array[[RDDInfo](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/RDDInfo.html "org.apache.spark.storage.RDDInfo")]
Return information about what RDDs are cached, if they are in mem or on disk, how much space they take, etc.
Return information about what RDDs are cached, if they are in mem or on disk, how much space they take, etc.

Annotations
     @DeveloperApi()
  57. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#getReadOnlyConf:org.apache.spark.ReadOnlySparkConf "Permalink") def getReadOnlyConf: [ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html "org.apache.spark.ReadOnlySparkConf")
Get a read-only reference to the spark conf.
Get a read-only reference to the spark conf. This is preferred version over [getConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#getConf:org.apache.spark.SparkConf).
  58. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#getSchedulingMode:org.apache.spark.scheduler.SchedulingMode.SchedulingMode "Permalink") def getSchedulingMode: [SchedulingMode](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SchedulingMode$.html#SchedulingMode=org.apache.spark.scheduler.SchedulingMode.Value)
Return current scheduling mode
  59. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#hadoopConfiguration:org.apache.hadoop.conf.Configuration "Permalink") def hadoopConfiguration: Configuration
A default Hadoop Configuration for the Hadoop code (e.g.
A default Hadoop Configuration for the Hadoop code (e.g. file systems) that we reuse.

Note

As it will be reused in all Hadoop RDDs, it's better not to modify it unless you plan to set some global configurations for all Hadoop RDDs.
  60. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#hadoopFile\[K,V,F<:org.apache.hadoop.mapred.InputFormat\[K,V\]\]\(path:String\)\(implicitkm:scala.reflect.ClassTag\[K\],implicitvm:scala.reflect.ClassTag\[V\],implicitfm:scala.reflect.ClassTag\[F\]\):org.apache.spark.rdd.RDD\[\(K,V\)\] "Permalink") def hadoopFile[K, V, F <: InputFormat[K, V]](path: String)(implicit km: ClassTag[K], vm: ClassTag[V], fm: ClassTag[F]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, V)]
Smarter version of hadoopFile() that uses class tags to figure out the classes of keys, values and the InputFormat so that users don't need to pass them directly.
Smarter version of hadoopFile() that uses class tags to figure out the classes of keys, values and the InputFormat so that users don't need to pass them directly. Instead, callers can just write, for example,

```
val file = sparkContext.hadoopFile[LongWritable, Text, TextInputFormat](path)
```

path

directory to the input data files, the path can be comma separated paths as a list of inputs

returns

RDD of tuples of key and corresponding value

Note

Because Hadoop's RecordReader class re-uses the same Writable object for each record, directly caching the returned RDD or directly passing it to an aggregation or shuffle operation will create many references to the same object. If you plan to directly cache, sort, or aggregate Hadoop writable objects, you should first copy them using a `map` function.
  61. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#hadoopFile\[K,V,F<:org.apache.hadoop.mapred.InputFormat\[K,V\]\]\(path:String,minPartitions:Int\)\(implicitkm:scala.reflect.ClassTag\[K\],implicitvm:scala.reflect.ClassTag\[V\],implicitfm:scala.reflect.ClassTag\[F\]\):org.apache.spark.rdd.RDD\[\(K,V\)\] "Permalink") def hadoopFile[K, V, F <: InputFormat[K, V]](path: String, minPartitions: Int)(implicit km: ClassTag[K], vm: ClassTag[V], fm: ClassTag[F]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, V)]
Smarter version of hadoopFile() that uses class tags to figure out the classes of keys, values and the InputFormat so that users don't need to pass them directly.
Smarter version of hadoopFile() that uses class tags to figure out the classes of keys, values and the InputFormat so that users don't need to pass them directly. Instead, callers can just write, for example,

```
val file = sparkContext.hadoopFile[LongWritable, Text, TextInputFormat](path, minPartitions)
```

path

directory to the input data files, the path can be comma separated paths as a list of inputs

minPartitions

suggested minimum number of partitions for the resulting RDD

returns

RDD of tuples of key and corresponding value

Note

Because Hadoop's RecordReader class re-uses the same Writable object for each record, directly caching the returned RDD or directly passing it to an aggregation or shuffle operation will create many references to the same object. If you plan to directly cache, sort, or aggregate Hadoop writable objects, you should first copy them using a `map` function.
  62. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#hadoopFile\[K,V\]\(path:String,inputFormatClass:Class\[_<:org.apache.hadoop.mapred.InputFormat\[K,V\]\],keyClass:Class\[K\],valueClass:Class\[V\],minPartitions:Int\):org.apache.spark.rdd.RDD\[\(K,V\)\] "Permalink") def hadoopFile[K, V](path: String, inputFormatClass: Class[_ <: InputFormat[K, V]], keyClass: Class[K], valueClass: Class[V], minPartitions: Int = [defaultMinPartitions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#defaultMinPartitions:Int)): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, V)]
Get an RDD for a Hadoop file with an arbitrary InputFormat
Get an RDD for a Hadoop file with an arbitrary InputFormat

path

directory to the input data files, the path can be comma separated paths as a list of inputs

inputFormatClass

storage format of the data to be read

keyClass

`Class` of the key associated with the `inputFormatClass` parameter

valueClass

`Class` of the value associated with the `inputFormatClass` parameter

minPartitions

suggested minimum number of partitions for the resulting RDD

returns

RDD of tuples of key and corresponding value

Note

Because Hadoop's RecordReader class re-uses the same Writable object for each record, directly caching the returned RDD or directly passing it to an aggregation or shuffle operation will create many references to the same object. If you plan to directly cache, sort, or aggregate Hadoop writable objects, you should first copy them using a `map` function.
  63. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#hadoopRDD\[K,V\]\(conf:org.apache.hadoop.mapred.JobConf,inputFormatClass:Class\[_<:org.apache.hadoop.mapred.InputFormat\[K,V\]\],keyClass:Class\[K\],valueClass:Class\[V\],minPartitions:Int\):org.apache.spark.rdd.RDD\[\(K,V\)\] "Permalink") def hadoopRDD[K, V](conf: JobConf, inputFormatClass: Class[_ <: InputFormat[K, V]], keyClass: Class[K], valueClass: Class[V], minPartitions: Int = [defaultMinPartitions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#defaultMinPartitions:Int)): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, V)]
Get an RDD for a Hadoop-readable dataset from a Hadoop JobConf given its InputFormat and other necessary info (e.g.
Get an RDD for a Hadoop-readable dataset from a Hadoop JobConf given its InputFormat and other necessary info (e.g. file name for a filesystem-based dataset, table name for HyperTable), using the older MapReduce API (`org.apache.hadoop.mapred`).

conf

JobConf for setting up the dataset. Note: This will be put into a Broadcast. Therefore if you plan to reuse this conf to create multiple RDDs, you need to make sure you won't modify the conf. A safe approach is always creating a new conf for a new RDD.

inputFormatClass

storage format of the data to be read

keyClass

`Class` of the key associated with the `inputFormatClass` parameter

valueClass

`Class` of the value associated with the `inputFormatClass` parameter

minPartitions

Minimum number of Hadoop Splits to generate.

returns

RDD of tuples of key and corresponding value

Note

Because Hadoop's RecordReader class re-uses the same Writable object for each record, directly caching the returned RDD or directly passing it to an aggregation or shuffle operation will create many references to the same object. If you plan to directly cache, sort, or aggregate Hadoop writable objects, you should first copy them using a `map` function.
  64. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#hashCode\(\):Int "Permalink") def hashCode(): Int

Definition Classes
    AnyRef → Any

Annotations
     @IntrinsicCandidate() @native()
  65. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#initializeLogIfNecessary\(isInterpreter:Boolean,silent:Boolean\):Boolean "Permalink") def initializeLogIfNecessary(isInterpreter: Boolean, silent: Boolean): Boolean

Attributes
    protected

Definition Classes
    Logging
  66. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#initializeLogIfNecessary\(isInterpreter:Boolean\):Unit "Permalink") def initializeLogIfNecessary(isInterpreter: Boolean): Unit

Attributes
    protected

Definition Classes
    Logging
  67. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean

Definition Classes
    Any
  68. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#isLocal:Boolean "Permalink") def isLocal: Boolean
  69. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#isStopped:Boolean "Permalink") def isStopped: Boolean

returns

true if context is stopped or in the midst of stopping.
  70. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#isTraceEnabled\(\):Boolean "Permalink") def isTraceEnabled(): Boolean

Attributes
    protected

Definition Classes
    Logging
  71. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#jars:Seq\[String\] "Permalink") def jars: Seq[String]
  72. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#killExecutor\(executorId:String\):Boolean "Permalink") def killExecutor(executorId: String): Boolean
Request that the cluster manager kill the specified executor.
Request that the cluster manager kill the specified executor.

returns

whether the request is received.

Annotations
     @DeveloperApi()

Note

This is an indication to the cluster manager that the application wishes to adjust its resource usage downwards. If the application wishes to replace the executor it kills through this method with a new one, it should follow up explicitly with a call to {{SparkContext#requestExecutors}}.
  73. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#killExecutors\(executorIds:Seq\[String\]\):Boolean "Permalink") def killExecutors(executorIds: Seq[String]): Boolean
Request that the cluster manager kill the specified executors.
Request that the cluster manager kill the specified executors.
This is not supported when dynamic allocation is turned on.

returns

whether the request is received.

Annotations
     @DeveloperApi()

Note

This is an indication to the cluster manager that the application wishes to adjust its resource usage downwards. If the application wishes to replace the executors it kills through this method with new ones, it should follow up explicitly with a call to {{SparkContext#requestExecutors}}.
  74. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#killTaskAttempt\(taskId:Long,interruptThread:Boolean,reason:String\):Boolean "Permalink") def killTaskAttempt(taskId: Long, interruptThread: Boolean = true, reason: String = "killed via SparkContext.killTaskAttempt"): Boolean
Kill and reschedule the given task attempt.
Kill and reschedule the given task attempt. Task ids can be obtained from the Spark UI or through SparkListener.onTaskStart.

taskId

the task ID to kill. This id uniquely identifies the task attempt.

interruptThread

whether to interrupt the thread running the task.

reason

the reason for killing the task, which should be a short string. If a task is killed multiple times with different reasons, only one reason will be reported.

returns

Whether the task was successfully killed.
  75. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#listArchives\(\):Seq\[String\] "Permalink") def listArchives(): Seq[String]
Returns a list of archive paths that are added to resources.
Returns a list of archive paths that are added to resources.

Annotations
     @Experimental()

Since

3.1.0
  76. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#listFiles\(\):Seq\[String\] "Permalink") def listFiles(): Seq[String]
Returns a list of file paths that are added to resources.
  77. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#listJars\(\):Seq\[String\] "Permalink") def listJars(): Seq[String]
Returns a list of jar files that are added to resources.
  78. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#localProperties:InheritableThreadLocal\[java.util.Properties\] "Permalink") val localProperties: [InheritableThreadLocal](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InheritableThreadLocal.html#java.lang.InheritableThreadLocal "java.lang.InheritableThreadLocal")[[Properties](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Properties.html#java.util.Properties "java.util.Properties")]

Attributes
    protected[[spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")]
  79. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#log:org.slf4j.Logger "Permalink") def log: Logger

Attributes
    protected

Definition Classes
    Logging
  80. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#logBasedOnLevel\(level:org.slf4j.event.Level\)\(f:=>org.apache.spark.internal.MessageWithContext\):Unit "Permalink") def logBasedOnLevel(level: Level)(f: => MessageWithContext): Unit

Attributes
    protected

Definition Classes
    Logging
  81. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#logDebug\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logDebug(msg: => String, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  82. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#logDebug\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logDebug(entry: LogEntry, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  83. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#logDebug\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logDebug(entry: LogEntry): Unit

Attributes
    protected

Definition Classes
    Logging
  84. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#logDebug\(msg:=>String\):Unit "Permalink") def logDebug(msg: => String): Unit

Attributes
    protected

Definition Classes
    Logging
  85. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#logError\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logError(msg: => String, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  86. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#logError\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logError(entry: LogEntry, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  87. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#logError\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logError(entry: LogEntry): Unit

Attributes
    protected

Definition Classes
    Logging
  88. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#logError\(msg:=>String\):Unit "Permalink") def logError(msg: => String): Unit

Attributes
    protected

Definition Classes
    Logging
  89. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#logInfo\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logInfo(msg: => String, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  90. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#logInfo\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logInfo(entry: LogEntry, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  91. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#logInfo\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logInfo(entry: LogEntry): Unit

Attributes
    protected

Definition Classes
    Logging
  92. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#logInfo\(msg:=>String\):Unit "Permalink") def logInfo(msg: => String): Unit

Attributes
    protected

Definition Classes
    Logging
  93. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#logName:String "Permalink") def logName: [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String")

Attributes
    protected

Definition Classes
    Logging
  94. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#logTrace\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logTrace(msg: => String, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  95. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#logTrace\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logTrace(entry: LogEntry, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  96. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#logTrace\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logTrace(entry: LogEntry): Unit

Attributes
    protected

Definition Classes
    Logging
  97. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#logTrace\(msg:=>String\):Unit "Permalink") def logTrace(msg: => String): Unit

Attributes
    protected

Definition Classes
    Logging
  98. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#logWarning\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logWarning(msg: => String, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  99. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#logWarning\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logWarning(entry: LogEntry, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  100. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#logWarning\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logWarning(entry: LogEntry): Unit

Attributes
    protected

Definition Classes
    Logging
  101. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#logWarning\(msg:=>String\):Unit "Permalink") def logWarning(msg: => String): Unit

Attributes
    protected

Definition Classes
    Logging
  102. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#longAccumulator\(name:String\):org.apache.spark.util.LongAccumulator "Permalink") def longAccumulator(name: String): [LongAccumulator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/LongAccumulator.html "org.apache.spark.util.LongAccumulator")
Create and register a long accumulator, which starts with 0 and accumulates inputs by `add`.
  103. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#longAccumulator:org.apache.spark.util.LongAccumulator "Permalink") def longAccumulator: [LongAccumulator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/LongAccumulator.html "org.apache.spark.util.LongAccumulator")
Create and register a long accumulator, which starts with 0 and accumulates inputs by `add`.
  104. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#makeRDD\[T\]\(seq:Seq\[\(T,Seq\[String\]\)\]\)\(implicitevidence$3:scala.reflect.ClassTag\[T\]\):org.apache.spark.rdd.RDD\[T\] "Permalink") def makeRDD[T](seq: Seq[(T, Seq[String])])(implicit arg0: ClassTag[T]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[T]
Distribute a local Scala collection to form an RDD, with one or more location preferences (hostnames of Spark nodes) for each object.
Distribute a local Scala collection to form an RDD, with one or more location preferences (hostnames of Spark nodes) for each object. Create a new partition for each collection item.

seq

list of tuples of data and location preferences (hostnames of Spark nodes)

returns

RDD representing data partitioned according to location preferences
  105. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#makeRDD\[T\]\(seq:Seq\[T\],numSlices:Int\)\(implicitevidence$2:scala.reflect.ClassTag\[T\]\):org.apache.spark.rdd.RDD\[T\] "Permalink") def makeRDD[T](seq: Seq[T], numSlices: Int = [defaultParallelism](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#defaultParallelism:Int))(implicit arg0: ClassTag[T]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[T]
Distribute a local Scala collection to form an RDD.
Distribute a local Scala collection to form an RDD.
This method is identical to `parallelize`.

seq

Scala collection to distribute

numSlices

number of partitions to divide the collection into

returns

RDD representing distributed collection
  106. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#master:String "Permalink") def master: String
  107. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  108. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#newAPIHadoopFile\[K,V,F<:org.apache.hadoop.mapreduce.InputFormat\[K,V\]\]\(path:String,fClass:Class\[F\],kClass:Class\[K\],vClass:Class\[V\],conf:org.apache.hadoop.conf.Configuration\):org.apache.spark.rdd.RDD\[\(K,V\)\] "Permalink") def newAPIHadoopFile[K, V, F <: InputFormat[K, V]](path: String, fClass: Class[F], kClass: Class[K], vClass: Class[V], conf: Configuration = [hadoopConfiguration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#hadoopConfiguration:org.apache.hadoop.conf.Configuration)): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, V)]
Get an RDD for a given Hadoop file with an arbitrary new API InputFormat and extra configuration options to pass to the input format.
Get an RDD for a given Hadoop file with an arbitrary new API InputFormat and extra configuration options to pass to the input format.

path

directory to the input data files, the path can be comma separated paths as a list of inputs

fClass

storage format of the data to be read

kClass

`Class` of the key associated with the `fClass` parameter

vClass

`Class` of the value associated with the `fClass` parameter

conf

Hadoop configuration

returns

RDD of tuples of key and corresponding value

Note

Because Hadoop's RecordReader class re-uses the same Writable object for each record, directly caching the returned RDD or directly passing it to an aggregation or shuffle operation will create many references to the same object. If you plan to directly cache, sort, or aggregate Hadoop writable objects, you should first copy them using a `map` function.
  109. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#newAPIHadoopFile\[K,V,F<:org.apache.hadoop.mapreduce.InputFormat\[K,V\]\]\(path:String\)\(implicitkm:scala.reflect.ClassTag\[K\],implicitvm:scala.reflect.ClassTag\[V\],implicitfm:scala.reflect.ClassTag\[F\]\):org.apache.spark.rdd.RDD\[\(K,V\)\] "Permalink") def newAPIHadoopFile[K, V, F <: InputFormat[K, V]](path: String)(implicit km: ClassTag[K], vm: ClassTag[V], fm: ClassTag[F]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, V)]
Smarter version of `newApiHadoopFile` that uses class tags to figure out the classes of keys, values and the `org.apache.hadoop.mapreduce.InputFormat` (new MapReduce API) so that user don't need to pass them directly.
Smarter version of `newApiHadoopFile` that uses class tags to figure out the classes of keys, values and the `org.apache.hadoop.mapreduce.InputFormat` (new MapReduce API) so that user don't need to pass them directly. Instead, callers can just write, for example: ``` val file = sparkContext.hadoopFile[LongWritable, Text, TextInputFormat](path) ``` ``````

path

directory to the input data files, the path can be comma separated paths as a list of inputs

returns

RDD of tuples of key and corresponding value

Note

Because Hadoop's RecordReader class re-uses the same Writable object for each record, directly caching the returned RDD or directly passing it to an aggregation or shuffle operation will create many references to the same object. If you plan to directly cache, sort, or aggregate Hadoop writable objects, you should first copy them using a `map` function.
  110. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#newAPIHadoopRDD\[K,V,F<:org.apache.hadoop.mapreduce.InputFormat\[K,V\]\]\(conf:org.apache.hadoop.conf.Configuration,fClass:Class\[F\],kClass:Class\[K\],vClass:Class\[V\]\):org.apache.spark.rdd.RDD\[\(K,V\)\] "Permalink") def newAPIHadoopRDD[K, V, F <: InputFormat[K, V]](conf: Configuration = [hadoopConfiguration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#hadoopConfiguration:org.apache.hadoop.conf.Configuration), fClass: Class[F], kClass: Class[K], vClass: Class[V]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, V)]
Get an RDD for a given Hadoop file with an arbitrary new API InputFormat and extra configuration options to pass to the input format.
Get an RDD for a given Hadoop file with an arbitrary new API InputFormat and extra configuration options to pass to the input format.

conf

Configuration for setting up the dataset. Note: This will be put into a Broadcast. Therefore if you plan to reuse this conf to create multiple RDDs, you need to make sure you won't modify the conf. A safe approach is always creating a new conf for a new RDD.

fClass

storage format of the data to be read

kClass

`Class` of the key associated with the `fClass` parameter

vClass

`Class` of the value associated with the `fClass` parameter

Note

Because Hadoop's RecordReader class re-uses the same Writable object for each record, directly caching the returned RDD or directly passing it to an aggregation or shuffle operation will create many references to the same object. If you plan to directly cache, sort, or aggregate Hadoop writable objects, you should first copy them using a `map` function.
  111. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#notify\(\):Unit "Permalink") final  def notify(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  112. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  113. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#objectFile\[T\]\(path:String,minPartitions:Int\)\(implicitevidence$4:scala.reflect.ClassTag\[T\]\):org.apache.spark.rdd.RDD\[T\] "Permalink") def objectFile[T](path: String, minPartitions: Int = [defaultMinPartitions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#defaultMinPartitions:Int))(implicit arg0: ClassTag[T]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[T]
Load an RDD saved as a SequenceFile containing serialized objects, with NullWritable keys and BytesWritable values that contain a serialized partition.
Load an RDD saved as a SequenceFile containing serialized objects, with NullWritable keys and BytesWritable values that contain a serialized partition. This is still an experimental storage format and may not be supported exactly as is in future Spark releases. It will also be pretty slow if you use the default serializer (Java serialization), though the nice thing about it is that there's very little effort required to save arbitrary objects.

path

directory to the input data files, the path can be comma separated paths as a list of inputs

minPartitions

suggested minimum number of partitions for the resulting RDD

returns

RDD representing deserialized data from the file(s)
  114. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#parallelize\[T\]\(seq:Seq\[T\],numSlices:Int\)\(implicitevidence$1:scala.reflect.ClassTag\[T\]\):org.apache.spark.rdd.RDD\[T\] "Permalink") def parallelize[T](seq: Seq[T], numSlices: Int = [defaultParallelism](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#defaultParallelism:Int))(implicit arg0: ClassTag[T]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[T]
Distribute a local Scala collection to form an RDD.
Distribute a local Scala collection to form an RDD.

seq

Scala collection to distribute

numSlices

number of partitions to divide the collection into

returns

RDD representing distributed collection

Note

Parallelize acts lazily. If `seq` is a mutable collection and is altered after the call to parallelize and before the first action on the RDD, the resultant RDD will reflect the modified collection. Pass a copy of the argument to avoid this.
,
avoid using `parallelize(Seq())` to create an empty `RDD`. Consider `emptyRDD` for an RDD with no partitions, or `parallelize(Seq[T]())` for an RDD of `T` with empty partitions.
  115. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#range\(start:Long,end:Long,step:Long,numSlices:Int\):org.apache.spark.rdd.RDD\[Long\] "Permalink") def range(start: Long, end: Long, step: Long = 1, numSlices: Int = [defaultParallelism](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#defaultParallelism:Int)): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[Long]
Creates a new RDD[Long] containing elements from `start` to `end`(exclusive), increased by `step` every element.
Creates a new RDD[Long] containing elements from `start` to `end`(exclusive), increased by `step` every element.

start

the start value.

end

the end value.

step

the incremental step

numSlices

number of partitions to divide the collection into

returns

RDD representing distributed range

Note

if we need to cache this RDD, we should make sure each partition does not exceed limit.
  116. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#register\(acc:org.apache.spark.util.AccumulatorV2\[_,_\],name:String\):Unit "Permalink") def register(acc: [AccumulatorV2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html "org.apache.spark.util.AccumulatorV2")[_, _], name: String): Unit
Register the given accumulator with given name.
Register the given accumulator with given name.

Note

Accumulators must be registered before use, or it will throw exception.
  117. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#register\(acc:org.apache.spark.util.AccumulatorV2\[_,_\]\):Unit "Permalink") def register(acc: [AccumulatorV2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html "org.apache.spark.util.AccumulatorV2")[_, _]): Unit
Register the given accumulator.
Register the given accumulator.

Note

Accumulators must be registered before use, or it will throw exception.
  118. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#removeJobTag\(tag:String\):Unit "Permalink") def removeJobTag(tag: String): Unit
Remove a tag previously added to be assigned to all the jobs started by this thread.
Remove a tag previously added to be assigned to all the jobs started by this thread. Noop if such a tag was not added earlier.

tag

The tag to be removed. Cannot contain ',' (comma) character.

Since

3.5.0
  119. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#removeJobTags\(tags:Set\[String\]\):Unit "Permalink") def removeJobTags(tags: Set[String]): Unit
Remove multiple tags to be assigned to all the jobs started by this thread.
Remove multiple tags to be assigned to all the jobs started by this thread. See [removeJobTag](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#removeJobTag\(tag:String\):Unit) for more details.

tags

The tags to be removed. Cannot contain ',' (comma) character.

Since

4.0.0
  120. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#removeSparkListener\(listener:org.apache.spark.scheduler.SparkListenerInterface\):Unit "Permalink") def removeSparkListener(listener: SparkListenerInterface): Unit
Deregister the listener from Spark's listener bus.
Deregister the listener from Spark's listener bus.

Annotations
     @DeveloperApi()
  121. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#requestExecutors\(numAdditionalExecutors:Int\):Boolean "Permalink") def requestExecutors(numAdditionalExecutors: Int): Boolean
Request an additional number of executors from the cluster manager.
Request an additional number of executors from the cluster manager.

returns

whether the request is received.

Annotations
     @DeveloperApi()
  122. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#requestTotalExecutors\(numExecutors:Int,localityAwareTasks:Int,hostToLocalTaskCount:scala.collection.immutable.Map\[String,Int\]\):Boolean "Permalink") def requestTotalExecutors(numExecutors: Int, localityAwareTasks: Int, hostToLocalTaskCount: Map[String, Int]): Boolean
Update the cluster manager on our scheduling needs.
Update the cluster manager on our scheduling needs. Three bits of information are included to help it make decisions. This applies to the default ResourceProfile.

numExecutors

The total number of executors we'd like to have. The cluster manager shouldn't kill any running executor to reach this number, but, if all existing executors were to die, this is the number of executors we'd want to be allocated.

localityAwareTasks

The number of tasks in all active stages that have a locality preferences. This includes running, pending, and completed tasks.

hostToLocalTaskCount

A map of hosts to the number of tasks from all active stages that would like to like to run on that host. This includes running, pending, and completed tasks.

returns

whether the request is acknowledged by the cluster manager.

Annotations
     @DeveloperApi()
  123. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#resources:scala.collection.Map\[String,org.apache.spark.resource.ResourceInformation\] "Permalink") def resources: Map[String, [ResourceInformation](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/resource/ResourceInformation.html "org.apache.spark.resource.ResourceInformation")]
  124. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#runApproximateJob\[T,U,R\]\(rdd:org.apache.spark.rdd.RDD\[T\],func:\(org.apache.spark.TaskContext,Iterator\[T\]\)=>U,evaluator:org.apache.spark.partial.ApproximateEvaluator\[U,R\],timeout:Long\):org.apache.spark.partial.PartialResult\[R\] "Permalink") def runApproximateJob[T, U, R](rdd: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[T], func: ([TaskContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskContext.html "org.apache.spark.TaskContext"), Iterator[T]) => U, evaluator: ApproximateEvaluator[U, R], timeout: Long): [PartialResult](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/partial/PartialResult.html "org.apache.spark.partial.PartialResult")[R]
Run a job that can return approximate results.
Run a job that can return approximate results.

rdd

target RDD to run tasks on

func

a function to run on each partition of the RDD

evaluator

`ApproximateEvaluator` to receive the partial results

timeout

maximum time to wait for the job, in milliseconds

returns

partial result (how partial depends on whether the job was finished before or after timeout)

Annotations
     @DeveloperApi()
  125. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#runJob\[T,U\]\(rdd:org.apache.spark.rdd.RDD\[T\],processPartition:Iterator\[T\]=>U,resultHandler:\(Int,U\)=>Unit\)\(implicitevidence$17:scala.reflect.ClassTag\[U\]\):Unit "Permalink") def runJob[T, U](rdd: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[T], processPartition: (Iterator[T]) => U, resultHandler: (Int, U) => Unit)(implicit arg0: ClassTag[U]): Unit
Run a job on all partitions in an RDD and pass the results to a handler function.
Run a job on all partitions in an RDD and pass the results to a handler function.

rdd

target RDD to run tasks on

processPartition

a function to run on each partition of the RDD

resultHandler

callback to pass each result to
  126. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#runJob\[T,U\]\(rdd:org.apache.spark.rdd.RDD\[T\],processPartition:\(org.apache.spark.TaskContext,Iterator\[T\]\)=>U,resultHandler:\(Int,U\)=>Unit\)\(implicitevidence$16:scala.reflect.ClassTag\[U\]\):Unit "Permalink") def runJob[T, U](rdd: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[T], processPartition: ([TaskContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskContext.html "org.apache.spark.TaskContext"), Iterator[T]) => U, resultHandler: (Int, U) => Unit)(implicit arg0: ClassTag[U]): Unit
Run a job on all partitions in an RDD and pass the results to a handler function.
Run a job on all partitions in an RDD and pass the results to a handler function. The function that is run against each partition additionally takes `TaskContext` argument.

rdd

target RDD to run tasks on

processPartition

a function to run on each partition of the RDD

resultHandler

callback to pass each result to
  127. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#runJob\[T,U\]\(rdd:org.apache.spark.rdd.RDD\[T\],func:Iterator\[T\]=>U\)\(implicitevidence$15:scala.reflect.ClassTag\[U\]\):Array\[U\] "Permalink") def runJob[T, U](rdd: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[T], func: (Iterator[T]) => U)(implicit arg0: ClassTag[U]): Array[U]
Run a job on all partitions in an RDD and return the results in an array.
Run a job on all partitions in an RDD and return the results in an array.

rdd

target RDD to run tasks on

func

a function to run on each partition of the RDD

returns

in-memory collection with a result of the job (each collection element will contain a result from one partition)
  128. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#runJob\[T,U\]\(rdd:org.apache.spark.rdd.RDD\[T\],func:\(org.apache.spark.TaskContext,Iterator\[T\]\)=>U\)\(implicitevidence$14:scala.reflect.ClassTag\[U\]\):Array\[U\] "Permalink") def runJob[T, U](rdd: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[T], func: ([TaskContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskContext.html "org.apache.spark.TaskContext"), Iterator[T]) => U)(implicit arg0: ClassTag[U]): Array[U]
Run a job on all partitions in an RDD and return the results in an array.
Run a job on all partitions in an RDD and return the results in an array. The function that is run against each partition additionally takes `TaskContext` argument.

rdd

target RDD to run tasks on

func

a function to run on each partition of the RDD

returns

in-memory collection with a result of the job (each collection element will contain a result from one partition)
  129. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#runJob\[T,U\]\(rdd:org.apache.spark.rdd.RDD\[T\],func:Iterator\[T\]=>U,partitions:Seq\[Int\]\)\(implicitevidence$13:scala.reflect.ClassTag\[U\]\):Array\[U\] "Permalink") def runJob[T, U](rdd: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[T], func: (Iterator[T]) => U, partitions: Seq[Int])(implicit arg0: ClassTag[U]): Array[U]
Run a function on a given set of partitions in an RDD and return the results as an array.
Run a function on a given set of partitions in an RDD and return the results as an array.

rdd

target RDD to run tasks on

func

a function to run on each partition of the RDD

partitions

set of partitions to run on; some jobs may not want to compute on all partitions of the target RDD, e.g. for operations like `first()`

returns

in-memory collection with a result of the job (each collection element will contain a result from one partition)
  130. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#runJob\[T,U\]\(rdd:org.apache.spark.rdd.RDD\[T\],func:\(org.apache.spark.TaskContext,Iterator\[T\]\)=>U,partitions:Seq\[Int\]\)\(implicitevidence$12:scala.reflect.ClassTag\[U\]\):Array\[U\] "Permalink") def runJob[T, U](rdd: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[T], func: ([TaskContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskContext.html "org.apache.spark.TaskContext"), Iterator[T]) => U, partitions: Seq[Int])(implicit arg0: ClassTag[U]): Array[U]
Run a function on a given set of partitions in an RDD and return the results as an array.
Run a function on a given set of partitions in an RDD and return the results as an array. The function that is run against each partition additionally takes `TaskContext` argument.

rdd

target RDD to run tasks on

func

a function to run on each partition of the RDD

partitions

set of partitions to run on; some jobs may not want to compute on all partitions of the target RDD, e.g. for operations like `first()`

returns

in-memory collection with a result of the job (each collection element will contain a result from one partition)
  131. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#runJob\[T,U\]\(rdd:org.apache.spark.rdd.RDD\[T\],func:\(org.apache.spark.TaskContext,Iterator\[T\]\)=>U,partitions:Seq\[Int\],resultHandler:\(Int,U\)=>Unit\)\(implicitevidence$11:scala.reflect.ClassTag\[U\]\):Unit "Permalink") def runJob[T, U](rdd: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[T], func: ([TaskContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskContext.html "org.apache.spark.TaskContext"), Iterator[T]) => U, partitions: Seq[Int], resultHandler: (Int, U) => Unit)(implicit arg0: ClassTag[U]): Unit
Run a function on a given set of partitions in an RDD and pass the results to the given handler function.
Run a function on a given set of partitions in an RDD and pass the results to the given handler function. This is the main entry point for all actions in Spark.

rdd

target RDD to run tasks on

func

a function to run on each partition of the RDD

partitions

set of partitions to run on; some jobs may not want to compute on all partitions of the target RDD, e.g. for operations like `first()`

resultHandler

callback to pass each result to
  132. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#sequenceFile\[K,V\]\(path:String,minPartitions:Int\)\(implicitkm:scala.reflect.ClassTag\[K\],implicitvm:scala.reflect.ClassTag\[V\],implicitkcf:\(\)=>org.apache.spark.WritableConverter\[K\],implicitvcf:\(\)=>org.apache.spark.WritableConverter\[V\]\):org.apache.spark.rdd.RDD\[\(K,V\)\] "Permalink") def sequenceFile[K, V](path: String, minPartitions: Int = [defaultMinPartitions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#defaultMinPartitions:Int))(implicit km: ClassTag[K], vm: ClassTag[V], kcf: () => WritableConverter[K], vcf: () => WritableConverter[V]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, V)]
Version of sequenceFile() for types implicitly convertible to Writables through a WritableConverter.
Version of sequenceFile() for types implicitly convertible to Writables through a WritableConverter. For example, to access a SequenceFile where the keys are Text and the values are IntWritable, you could simply write

```
sparkContext.sequenceFile[String, Int](path, ...)
```

WritableConverters are provided in a somewhat strange way (by an implicit function) to support both subclasses of Writable and types for which we define a converter (e.g. Int to IntWritable). The most natural thing would've been to have implicit objects for the converters, but then we couldn't have an object for every subclass of Writable (you can't have a parameterized singleton object). We use functions instead to create a new converter for the appropriate type. In addition, we pass the converter a ClassTag of its type to allow it to figure out the Writable class to use in the subclass case.

path

directory to the input data files, the path can be comma separated paths as a list of inputs

minPartitions

suggested minimum number of partitions for the resulting RDD

returns

RDD of tuples of key and corresponding value

Note

Because Hadoop's RecordReader class re-uses the same Writable object for each record, directly caching the returned RDD or directly passing it to an aggregation or shuffle operation will create many references to the same object. If you plan to directly cache, sort, or aggregate Hadoop writable objects, you should first copy them using a `map` function.
  133. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#sequenceFile\[K,V\]\(path:String,keyClass:Class\[K\],valueClass:Class\[V\]\):org.apache.spark.rdd.RDD\[\(K,V\)\] "Permalink") def sequenceFile[K, V](path: String, keyClass: Class[K], valueClass: Class[V]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, V)]
Get an RDD for a Hadoop SequenceFile with given key and value types.
Get an RDD for a Hadoop SequenceFile with given key and value types.

path

directory to the input data files, the path can be comma separated paths as a list of inputs

keyClass

`Class` of the key associated with `SequenceFileInputFormat`

valueClass

`Class` of the value associated with `SequenceFileInputFormat`

returns

RDD of tuples of key and corresponding value

Note

Because Hadoop's RecordReader class re-uses the same Writable object for each record, directly caching the returned RDD or directly passing it to an aggregation or shuffle operation will create many references to the same object. If you plan to directly cache, sort, or aggregate Hadoop writable objects, you should first copy them using a `map` function.
  134. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#sequenceFile\[K,V\]\(path:String,keyClass:Class\[K\],valueClass:Class\[V\],minPartitions:Int\):org.apache.spark.rdd.RDD\[\(K,V\)\] "Permalink") def sequenceFile[K, V](path: String, keyClass: Class[K], valueClass: Class[V], minPartitions: Int): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, V)]
Get an RDD for a Hadoop SequenceFile with given key and value types.
Get an RDD for a Hadoop SequenceFile with given key and value types.

path

directory to the input data files, the path can be comma separated paths as a list of inputs

keyClass

`Class` of the key associated with `SequenceFileInputFormat`

valueClass

`Class` of the value associated with `SequenceFileInputFormat`

minPartitions

suggested minimum number of partitions for the resulting RDD

returns

RDD of tuples of key and corresponding value

Note

Because Hadoop's RecordReader class re-uses the same Writable object for each record, directly caching the returned RDD or directly passing it to an aggregation or shuffle operation will create many references to the same object. If you plan to directly cache, sort, or aggregate Hadoop writable objects, you should first copy them using a `map` function.
  135. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#setCallSite\(shortCallSite:String\):Unit "Permalink") def setCallSite(shortCallSite: String): Unit
Set the thread-local property for overriding the call sites of actions and RDDs.
  136. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#setCheckpointDir\(directory:String\):Unit "Permalink") def setCheckpointDir(directory: String): Unit
Set the directory under which RDDs are going to be checkpointed.
Set the directory under which RDDs are going to be checkpointed.

directory

path to the directory where checkpoint files will be stored (must be HDFS path if running in cluster)
  137. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#setInterruptOnCancel\(interruptOnCancel:Boolean\):Unit "Permalink") def setInterruptOnCancel(interruptOnCancel: Boolean): Unit
Set the behavior of job cancellation from jobs started in this thread.
Set the behavior of job cancellation from jobs started in this thread.

interruptOnCancel

If true, then job cancellation will result in `Thread.interrupt()` being called on the job's executor threads. This is useful to help ensure that the tasks are actually stopped in a timely manner, but is off by default due to HDFS-1208, where HDFS may respond to Thread.interrupt() by marking nodes as dead.

Since

3.5.0
  138. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#setJobDescription\(value:String\):Unit "Permalink") def setJobDescription(value: String): Unit
Set a human readable description of the current job.
  139. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#setJobGroup\(groupId:String,description:String,interruptOnCancel:Boolean\):Unit "Permalink") def setJobGroup(groupId: String, description: String, interruptOnCancel: Boolean = false): Unit
Assigns a group ID to all the jobs started by this thread until the group ID is set to a different value or cleared.
Assigns a group ID to all the jobs started by this thread until the group ID is set to a different value or cleared.
Often, a unit of execution in an application consists of multiple Spark actions or jobs. Application programmers can use this method to group all those jobs together and give a group description. Once set, the Spark web UI will associate such jobs with this group.
The application can also use `org.apache.spark.SparkContext.cancelJobGroup` to cancel all running jobs in this group. For example,

```
// In the main thread:
sc.setJobGroup("some_job_to_cancel", "some job description")
sc.parallelize(1 to 10000, 2).map { i => Thread.sleep(10); i }.count()

// In a separate thread:
sc.cancelJobGroup("some_job_to_cancel")
```

interruptOnCancel

If true, then job cancellation will result in `Thread.interrupt()` being called on the job's executor threads. This is useful to help ensure that the tasks are actually stopped in a timely manner, but is off by default due to HDFS-1208, where HDFS may respond to Thread.interrupt() by marking nodes as dead.
  140. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#setLocalProperty\(key:String,value:String\):Unit "Permalink") def setLocalProperty(key: String, value: String): Unit
Set a local property that affects jobs submitted from this thread, such as the Spark fair scheduler pool.
Set a local property that affects jobs submitted from this thread, such as the Spark fair scheduler pool. User-defined properties may also be set here. These properties are propagated through to worker tasks and can be accessed there via [org.apache.spark.TaskContext#getLocalProperty](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskContext.html#getLocalProperty\(key:String\):String).
These properties are inherited by child threads spawned from this thread. This may have unexpected consequences when working with thread pools. The standard java implementation of thread pools have worker threads spawn other worker threads. As a result, local properties may propagate unpredictably.
To remove/unset property simply set `value` to null e.g. sc.setLocalProperty("key", null)
  141. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#setLogLevel\(logLevel:String\):Unit "Permalink") def setLogLevel(logLevel: String): Unit
Control our logLevel.
Control our logLevel. This overrides any user-defined log settings.

logLevel

The desired log level as a string. Valid log levels include: ALL, DEBUG, ERROR, FATAL, INFO, OFF, TRACE, WARN
  142. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#sparkUser:String "Permalink") val sparkUser: String
  143. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#startTime:Long "Permalink") val startTime: Long
  144. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#statusTracker:org.apache.spark.SparkStatusTracker "Permalink") def statusTracker: [SparkStatusTracker](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkStatusTracker.html "org.apache.spark.SparkStatusTracker")
  145. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#stop\(exitCode:Int\):Unit "Permalink") def stop(exitCode: Int): Unit
Shut down the SparkContext with exit code that will passed to scheduler backend.
Shut down the SparkContext with exit code that will passed to scheduler backend. In client mode, client side may call `SparkContext.stop()` to clean up but exit with code not equal to 0. This behavior cause resource scheduler such as `ApplicationMaster` exit with success status but client side exited with failed status. Spark can call this method to stop SparkContext and pass client side correct exit code to scheduler backend. Then scheduler backend should send the exit code to corresponding resource scheduler to keep consistent.

exitCode

Specified exit code that will passed to scheduler backend in client mode.
  146. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#stop\(\):Unit "Permalink") def stop(): Unit
Shut down the SparkContext.
  147. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#submitJob\[T,U,R\]\(rdd:org.apache.spark.rdd.RDD\[T\],processPartition:Iterator\[T\]=>U,partitions:Seq\[Int\],resultHandler:\(Int,U\)=>Unit,resultFunc:=>R\):org.apache.spark.SimpleFutureAction\[R\] "Permalink") def submitJob[T, U, R](rdd: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[T], processPartition: (Iterator[T]) => U, partitions: Seq[Int], resultHandler: (Int, U) => Unit, resultFunc: => R): [SimpleFutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SimpleFutureAction.html "org.apache.spark.SimpleFutureAction")[R]
Submit a job for execution and return a FutureJob holding the result.
Submit a job for execution and return a FutureJob holding the result.

rdd

target RDD to run tasks on

processPartition

a function to run on each partition of the RDD

partitions

set of partitions to run on; some jobs may not want to compute on all partitions of the target RDD, e.g. for operations like `first()`

resultHandler

callback to pass each result to

resultFunc

function to be executed when the result is ready
  148. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0

Definition Classes
    AnyRef
  149. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#textFile\(path:String,minPartitions:Int\):org.apache.spark.rdd.RDD\[String\] "Permalink") def textFile(path: String, minPartitions: Int = [defaultMinPartitions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#defaultMinPartitions:Int)): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[String]
Read a text file from HDFS, a local file system (available on all nodes), or any Hadoop-supported file system URI, and return it as an RDD of Strings.
Read a text file from HDFS, a local file system (available on all nodes), or any Hadoop-supported file system URI, and return it as an RDD of Strings. The text files must be encoded as UTF-8.

path

path to the text file on a supported file system

minPartitions

suggested minimum number of partitions for the resulting RDD

returns

RDD of lines of the text file
  150. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#toString\(\):String "Permalink") def toString(): [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String")

Definition Classes
    AnyRef → Any
  151. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#uiWebUrl:Option\[String\] "Permalink") def uiWebUrl: Option[String]
  152. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#union\[T\]\(first:org.apache.spark.rdd.RDD\[T\],rest:org.apache.spark.rdd.RDD\[T\]*\)\(implicitevidence$7:scala.reflect.ClassTag\[T\]\):org.apache.spark.rdd.RDD\[T\] "Permalink") def union[T](first: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[T], rest: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[T]*)(implicit arg0: ClassTag[T]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[T]
Build the union of a list of RDDs passed as variable-length arguments.
  153. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#union\[T\]\(rdds:Seq\[org.apache.spark.rdd.RDD\[T\]\]\)\(implicitevidence$6:scala.reflect.ClassTag\[T\]\):org.apache.spark.rdd.RDD\[T\] "Permalink") def union[T](rdds: Seq[[RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[T]])(implicit arg0: ClassTag[T]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[T]
Build the union of a list of RDDs.
  154. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#version:String "Permalink") def version: String
The version of Spark on which this application is running.
  155. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])
  156. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  157. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#wait\(\):Unit "Permalink") final  def wait(): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])
  158. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#wholeTextFiles\(path:String,minPartitions:Int\):org.apache.spark.rdd.RDD\[\(String,String\)\] "Permalink") def wholeTextFiles(path: String, minPartitions: Int = [defaultMinPartitions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#defaultMinPartitions:Int)): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(String, String)]
Read a directory of text files from HDFS, a local file system (available on all nodes), or any Hadoop-supported file system URI.
Read a directory of text files from HDFS, a local file system (available on all nodes), or any Hadoop-supported file system URI. Each file is read as a single record and returned in a key-value pair, where the key is the path of each file, the value is the content of each file. The text files must be encoded as UTF-8.
For example, if you have the following files:

```
hdfs://a-hdfs-path/part-00000
hdfs://a-hdfs-path/part-00001
...
hdfs://a-hdfs-path/part-nnnnn
```

Do `val rdd = sparkContext.wholeTextFile("hdfs://a-hdfs-path")`,
then `rdd` contains

```
(a-hdfs-path/part-00000, its content)
(a-hdfs-path/part-00001, its content)
...
(a-hdfs-path/part-nnnnn, its content)
```

path

Directory to the input data files, the path can be comma separated paths as the list of inputs.

minPartitions

A suggestion value of the minimal splitting number for input data.

returns

RDD representing tuples of file path and the corresponding file content

Note

Small files are preferred, large file is also allowable, but may cause bad performance.
,
On some filesystems, `.../path/*` can be a more efficient way to read all files in a directory rather than `.../path/` or `.../path`
,
Partitioning is determined by data locality. This may result in too few partitions by default.
  159. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#withLogContext\(context:java.util.Map\[String,String\]\)\(body:=>Unit\):Unit "Permalink") def withLogContext(context: [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#java.util.Map "java.util.Map")[String, String])(body: => Unit): Unit

Attributes
    protected

Definition Classes
    Logging

### Deprecated Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#finalize\(\):Unit "Permalink") def finalize(): Unit

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
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#MDC\(key:org.apache.spark.internal.LogKey,value:Any\):org.apache.spark.internal.MDC "Permalink") def MDC(key: LogKey, value: Any): MDC

Attributes
    protected

Definition Classes
    Logging
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#initializeLogIfNecessary\(isInterpreter:Boolean,silent:Boolean\):Boolean "Permalink") def initializeLogIfNecessary(isInterpreter: Boolean, silent: Boolean): Boolean

Attributes
    protected

Definition Classes
    Logging
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#initializeLogIfNecessary\(isInterpreter:Boolean\):Unit "Permalink") def initializeLogIfNecessary(isInterpreter: Boolean): Unit

Attributes
    protected

Definition Classes
    Logging
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#isTraceEnabled\(\):Boolean "Permalink") def isTraceEnabled(): Boolean

Attributes
    protected

Definition Classes
    Logging
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#log:org.slf4j.Logger "Permalink") def log: Logger

Attributes
    protected

Definition Classes
    Logging
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#logBasedOnLevel\(level:org.slf4j.event.Level\)\(f:=>org.apache.spark.internal.MessageWithContext\):Unit "Permalink") def logBasedOnLevel(level: Level)(f: => MessageWithContext): Unit

Attributes
    protected

Definition Classes
    Logging
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#logDebug\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logDebug(msg: => String, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#logDebug\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logDebug(entry: LogEntry, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#logDebug\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logDebug(entry: LogEntry): Unit

Attributes
    protected

Definition Classes
    Logging
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#logDebug\(msg:=>String\):Unit "Permalink") def logDebug(msg: => String): Unit

Attributes
    protected

Definition Classes
    Logging
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#logError\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logError(msg: => String, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#logError\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logError(entry: LogEntry, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#logError\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logError(entry: LogEntry): Unit

Attributes
    protected

Definition Classes
    Logging
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#logError\(msg:=>String\):Unit "Permalink") def logError(msg: => String): Unit

Attributes
    protected

Definition Classes
    Logging
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#logInfo\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logInfo(msg: => String, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#logInfo\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logInfo(entry: LogEntry, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#logInfo\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logInfo(entry: LogEntry): Unit

Attributes
    protected

Definition Classes
    Logging
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#logInfo\(msg:=>String\):Unit "Permalink") def logInfo(msg: => String): Unit

Attributes
    protected

Definition Classes
    Logging
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#logName:String "Permalink") def logName: [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String")

Attributes
    protected

Definition Classes
    Logging
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#logTrace\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logTrace(msg: => String, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#logTrace\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logTrace(entry: LogEntry, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#logTrace\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logTrace(entry: LogEntry): Unit

Attributes
    protected

Definition Classes
    Logging
  23. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#logTrace\(msg:=>String\):Unit "Permalink") def logTrace(msg: => String): Unit

Attributes
    protected

Definition Classes
    Logging
  24. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#logWarning\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logWarning(msg: => String, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  25. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#logWarning\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logWarning(entry: LogEntry, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  26. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#logWarning\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logWarning(entry: LogEntry): Unit

Attributes
    protected

Definition Classes
    Logging
  27. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#logWarning\(msg:=>String\):Unit "Permalink") def logWarning(msg: => String): Unit

Attributes
    protected

Definition Classes
    Logging
  28. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#withLogContext\(context:java.util.Map\[String,String\]\)\(body:=>Unit\):Unit "Permalink") def withLogContext(context: [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#java.util.Map "java.util.Map")[String, String])(body: => Unit): Unit

Attributes
    protected

Definition Classes
    Logging

### Inherited from AnyRef
### Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html###:Int "Permalink") final  def ##: Int

Definition Classes
    AnyRef → Any
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#clone\(\):Object "Permalink") def clone(): AnyRef

Attributes
    protected[lang]

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#equals\(x$1:Object\):Boolean "Permalink") def equals(arg0: AnyRef): Boolean

Definition Classes
    AnyRef → Any
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef]

Definition Classes
    AnyRef → Any

Annotations
     @IntrinsicCandidate() @native()
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#hashCode\(\):Int "Permalink") def hashCode(): Int

Definition Classes
    AnyRef → Any

Annotations
     @IntrinsicCandidate() @native()
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#notify\(\):Unit "Permalink") final  def notify(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0

Definition Classes
    AnyRef
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#toString\(\):String "Permalink") def toString(): [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String")

Definition Classes
    AnyRef → Any
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#wait\(\):Unit "Permalink") final  def wait(): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#finalize\(\):Unit "Permalink") def finalize(): Unit

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
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0

Definition Classes
    Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean

Definition Classes
    Any

### Ungrouped
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#LogStringContextextendsAnyRef "Permalink") implicit  class LogStringContext extends AnyRef

Definition Classes
    Logging

  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html###:Int "Permalink") final  def ##: Int

Definition Classes
    AnyRef → Any
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#MDC\(key:org.apache.spark.internal.LogKey,value:Any\):org.apache.spark.internal.MDC "Permalink") def MDC(key: LogKey, value: Any): MDC

Attributes
    protected

Definition Classes
    Logging
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#addArchive\(path:String\):Unit "Permalink") def addArchive(path: String): Unit
Add an archive to be downloaded and unpacked with this Spark job on every node.
Add an archive to be downloaded and unpacked with this Spark job on every node.
If an archive is added during execution, it will not be available until the next TaskSet starts.

path

can be either a local file, a file in HDFS (or other Hadoop-supported filesystems), or an HTTP, HTTPS or FTP URI. To access the file in Spark jobs, use `SparkFiles.get(paths-to-files)` to find its download/unpacked location. The given path should be one of .zip, .tar, .tar.gz, .tgz and .jar.

Annotations
     @Experimental()

Since

3.1.0

Note

A path can be added only once. Subsequent additions of the same path are ignored.
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#addFile\(path:String,recursive:Boolean\):Unit "Permalink") def addFile(path: String, recursive: Boolean): Unit
Add a file to be downloaded with this Spark job on every node.
Add a file to be downloaded with this Spark job on every node.
If a file is added during execution, it will not be available until the next TaskSet starts.

path

can be either a local file, a file in HDFS (or other Hadoop-supported filesystems), or an HTTP, HTTPS or FTP URI. To access the file in Spark jobs, use `SparkFiles.get(fileName)` to find its download location.

recursive

if true, a directory can be given in `path`. Currently directories are only supported for Hadoop-supported filesystems.

Note

A path can be added only once. Subsequent additions of the same path are ignored.
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#addFile\(path:String\):Unit "Permalink") def addFile(path: String): Unit
Add a file to be downloaded with this Spark job on every node.
Add a file to be downloaded with this Spark job on every node.
If a file is added during execution, it will not be available until the next TaskSet starts.

path

can be either a local file, a file in HDFS (or other Hadoop-supported filesystems), or an HTTP, HTTPS or FTP URI. To access the file in Spark jobs, use `SparkFiles.get(fileName)` to find its download location.

Note

A path can be added only once. Subsequent additions of the same path are ignored.
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#addJar\(path:String\):Unit "Permalink") def addJar(path: String): Unit
Adds a JAR dependency for all tasks to be executed on this `SparkContext` in the future.
Adds a JAR dependency for all tasks to be executed on this `SparkContext` in the future.
If a jar is added during execution, it will not be available until the next TaskSet starts.

path

can be either a local file, a file in HDFS (or other Hadoop-supported filesystems), an HTTP, HTTPS or FTP URI, or local:/path for a file on every worker node.

Note

A path can be added only once. Subsequent additions of the same path are ignored.
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#addJobTag\(tag:String\):Unit "Permalink") def addJobTag(tag: String): Unit
Add a tag to be assigned to all the jobs started by this thread.
Add a tag to be assigned to all the jobs started by this thread.
Often, a unit of execution in an application consists of multiple Spark actions or jobs. Application programmers can use this method to group all those jobs together and give a group tag. The application can use `org.apache.spark.sql.SparkSession.interruptTag` to cancel all running executions with this tag. For example:

```
// In the main thread:
sc.addJobTag("myjobs")
sc.parallelize(1 to 10000, 2).map { i => Thread.sleep(10); i }.count()

// In a separate thread:
spark.cancelJobsWithTag("myjobs")
```

There may be multiple tags present at the same time, so different parts of application may use different tags to perform cancellation at different levels of granularity.

tag

The tag to be added. Cannot contain ',' (comma) character.

Since

3.5.0
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#addJobTags\(tags:Set\[String\]\):Unit "Permalink") def addJobTags(tags: Set[String]): Unit
Add multiple tags to be assigned to all the jobs started by this thread.
Add multiple tags to be assigned to all the jobs started by this thread. See [addJobTag](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#addJobTag\(tag:String\):Unit) for more details.

tags

The tags to be added. Cannot contain ',' (comma) character.

Since

4.0.0
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#addSparkListener\(listener:org.apache.spark.scheduler.SparkListenerInterface\):Unit "Permalink") def addSparkListener(listener: SparkListenerInterface): Unit
Register a listener to receive up-calls from events that happen during execution.
Register a listener to receive up-calls from events that happen during execution.

Annotations
     @DeveloperApi()
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#appName:String "Permalink") def appName: String
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#applicationAttemptId:Option\[String\] "Permalink") def applicationAttemptId: Option[String]
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#applicationId:String "Permalink") def applicationId: String
A unique identifier for the Spark application.
A unique identifier for the Spark application. Its format depends on the scheduler implementation. (i.e. in case of local spark app something like 'local-1433865536131' in case of YARN something like 'application_1433865536131_34483' )
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#archives:Seq\[String\] "Permalink") def archives: Seq[String]
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0

Definition Classes
    Any
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#binaryFiles\(path:String,minPartitions:Int\):org.apache.spark.rdd.RDD\[\(String,org.apache.spark.input.PortableDataStream\)\] "Permalink") def binaryFiles(path: String, minPartitions: Int = [defaultMinPartitions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#defaultMinPartitions:Int)): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(String, [PortableDataStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/input/PortableDataStream.html "org.apache.spark.input.PortableDataStream"))]
Get an RDD for a Hadoop-readable dataset as PortableDataStream for each file (useful for binary data)
Get an RDD for a Hadoop-readable dataset as PortableDataStream for each file (useful for binary data)
For example, if you have the following files:

```
hdfs://a-hdfs-path/part-00000
hdfs://a-hdfs-path/part-00001
...
hdfs://a-hdfs-path/part-nnnnn
```

Do `val rdd = sparkContext.binaryFiles("hdfs://a-hdfs-path")`,
then `rdd` contains

```
(a-hdfs-path/part-00000, its content)
(a-hdfs-path/part-00001, its content)
...
(a-hdfs-path/part-nnnnn, its content)
```

path

Directory to the input data files, the path can be comma separated paths as the list of inputs.

minPartitions

A suggestion value of the minimal splitting number for input data.

returns

RDD representing tuples of file path and corresponding file content

Note

Small files are preferred; very large files may cause bad performance.
,
On some filesystems, `.../path/*` can be a more efficient way to read all files in a directory rather than `.../path/` or `.../path`
,
Partitioning is determined by data locality. This may result in too few partitions by default.
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#binaryRecords\(path:String,recordLength:Int,conf:org.apache.hadoop.conf.Configuration\):org.apache.spark.rdd.RDD\[Array\[Byte\]\] "Permalink") def binaryRecords(path: String, recordLength: Int, conf: Configuration = [hadoopConfiguration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#hadoopConfiguration:org.apache.hadoop.conf.Configuration)): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[Array[Byte]]
Load data from a flat binary file, assuming the length of each record is constant.
Load data from a flat binary file, assuming the length of each record is constant.

path

Directory to the input data files, the path can be comma separated paths as the list of inputs.

recordLength

The length at which to split the records

conf

Configuration for setting up the dataset.

returns

An RDD of data with values, represented as byte arrays

Note

We ensure that the byte array for each record in the resulting RDD has the provided record length.
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#broadcast\[T\]\(value:T\)\(implicitevidence$9:scala.reflect.ClassTag\[T\]\):org.apache.spark.broadcast.Broadcast\[T\] "Permalink") def broadcast[T](value: T)(implicit arg0: ClassTag[T]): [Broadcast](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/broadcast/Broadcast.html "org.apache.spark.broadcast.Broadcast")[T]
Broadcast a read-only variable to the cluster, returning a [org.apache.spark.broadcast.Broadcast](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/broadcast/Broadcast.html "org.apache.spark.broadcast.Broadcast") object for reading it in distributed functions.
Broadcast a read-only variable to the cluster, returning a [org.apache.spark.broadcast.Broadcast](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/broadcast/Broadcast.html "org.apache.spark.broadcast.Broadcast") object for reading it in distributed functions. The variable will be sent to each executor only once.

value

value to broadcast to the Spark nodes

returns

`Broadcast` object, a read-only variable cached on each machine
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#cancelAllJobs\(\):Unit "Permalink") def cancelAllJobs(): Unit
Cancel all jobs that have been scheduled or are running.
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#cancelJob\(jobId:Int\):Unit "Permalink") def cancelJob(jobId: Int): Unit
Cancel a given job if it's scheduled or running.
Cancel a given job if it's scheduled or running.

jobId

the job ID to cancel

Note

Throws `InterruptedException` if the cancel message cannot be sent
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#cancelJob\(jobId:Int,reason:String\):Unit "Permalink") def cancelJob(jobId: Int, reason: String): Unit
Cancel a given job if it's scheduled or running.
Cancel a given job if it's scheduled or running.

jobId

the job ID to cancel

reason

reason for cancellation

Note

Throws `InterruptedException` if the cancel message cannot be sent
  23. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#cancelJobGroup\(groupId:String\):Unit "Permalink") def cancelJobGroup(groupId: String): Unit
Cancel active jobs for the specified group.
Cancel active jobs for the specified group. See `org.apache.spark.SparkContext.setJobGroup` for more information.

groupId

the group ID to cancel
  24. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#cancelJobGroup\(groupId:String,reason:String\):Unit "Permalink") def cancelJobGroup(groupId: String, reason: String): Unit
Cancel active jobs for the specified group.
Cancel active jobs for the specified group. See `org.apache.spark.SparkContext.setJobGroup` for more information.

groupId

the group ID to cancel

reason

reason for cancellation

Since

4.0.0
  25. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#cancelJobGroupAndFutureJobs\(groupId:String\):Unit "Permalink") def cancelJobGroupAndFutureJobs(groupId: String): Unit
Cancel active jobs for the specified group, as well as the future jobs in this job group.
Cancel active jobs for the specified group, as well as the future jobs in this job group. Note: the maximum number of job groups that can be tracked is set by 'spark.scheduler.numCancelledJobGroupsToTrack'. Once the limit is reached and a new job group is to be added, the oldest job group tracked will be discarded.

groupId

the group ID to cancel
  26. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#cancelJobGroupAndFutureJobs\(groupId:String,reason:String\):Unit "Permalink") def cancelJobGroupAndFutureJobs(groupId: String, reason: String): Unit
Cancel active jobs for the specified group, as well as the future jobs in this job group.
Cancel active jobs for the specified group, as well as the future jobs in this job group. Note: the maximum number of job groups that can be tracked is set by 'spark.scheduler.numCancelledJobGroupsToTrack'. Once the limit is reached and a new job group is to be added, the oldest job group tracked will be discarded.

groupId

the group ID to cancel

reason

reason for cancellation

Since

4.0.0
  27. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#cancelJobsWithTag\(tag:String\):Unit "Permalink") def cancelJobsWithTag(tag: String): Unit
Cancel active jobs that have the specified tag.
Cancel active jobs that have the specified tag. See `org.apache.spark.SparkContext.addJobTag`.

tag

The tag to be cancelled. Cannot contain ',' (comma) character.

Since

3.5.0
  28. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#cancelJobsWithTag\(tag:String,reason:String\):Unit "Permalink") def cancelJobsWithTag(tag: String, reason: String): Unit
Cancel active jobs that have the specified tag.
Cancel active jobs that have the specified tag. See `org.apache.spark.SparkContext.addJobTag`.

tag

The tag to be cancelled. Cannot contain ',' (comma) character.

reason

reason for cancellation

Since

4.0.0
  29. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#cancelStage\(stageId:Int\):Unit "Permalink") def cancelStage(stageId: Int): Unit
Cancel a given stage and all jobs associated with it.
Cancel a given stage and all jobs associated with it.

stageId

the stage ID to cancel

Note

Throws `InterruptedException` if the cancel message cannot be sent
  30. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#cancelStage\(stageId:Int,reason:String\):Unit "Permalink") def cancelStage(stageId: Int, reason: String): Unit
Cancel a given stage and all jobs associated with it.
Cancel a given stage and all jobs associated with it.

stageId

the stage ID to cancel

reason

reason for cancellation

Note

Throws `InterruptedException` if the cancel message cannot be sent
  31. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#checkpointFile\[T\]\(path:String\)\(implicitevidence$5:scala.reflect.ClassTag\[T\]\):org.apache.spark.rdd.RDD\[T\] "Permalink") def checkpointFile[T](path: String)(implicit arg0: ClassTag[T]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[T]

Attributes
    protected[[spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")]
  32. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#clearCallSite\(\):Unit "Permalink") def clearCallSite(): Unit
Clear the thread-local property for overriding the call sites of actions and RDDs.
  33. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#clearJobGroup\(\):Unit "Permalink") def clearJobGroup(): Unit
Clear the current thread's job group ID and its description.
  34. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#clearJobTags\(\):Unit "Permalink") def clearJobTags(): Unit
Clear the current thread's job tags.
Clear the current thread's job tags.

Since

3.5.0
  35. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#clone\(\):Object "Permalink") def clone(): AnyRef

Attributes
    protected[lang]

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  36. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#collectionAccumulator\[T\]\(name:String\):org.apache.spark.util.CollectionAccumulator\[T\] "Permalink") def collectionAccumulator[T](name: String): [CollectionAccumulator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/CollectionAccumulator.html "org.apache.spark.util.CollectionAccumulator")[T]
Create and register a `CollectionAccumulator`, which starts with empty list and accumulates inputs by adding them into the list.
  37. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#collectionAccumulator\[T\]:org.apache.spark.util.CollectionAccumulator\[T\] "Permalink") def collectionAccumulator[T]: [CollectionAccumulator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/CollectionAccumulator.html "org.apache.spark.util.CollectionAccumulator")[T]
Create and register a `CollectionAccumulator`, which starts with empty list and accumulates inputs by adding them into the list.
  38. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#defaultMinPartitions:Int "Permalink") def defaultMinPartitions: Int
Default min number of partitions for Hadoop RDDs when not given by user Notice that we use math.min so the "defaultMinPartitions" cannot be higher than 2.
Default min number of partitions for Hadoop RDDs when not given by user Notice that we use math.min so the "defaultMinPartitions" cannot be higher than 2. For large files, the Hadoop InputFormat library always creates more partitions even though defaultMinPartitions is 2. For small files, it can be good to process small files quickly. However, usually when Spark joins a small table with a big one, we'll still spend most of time on the map part of the big one anyway.
  39. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#defaultParallelism:Int "Permalink") def defaultParallelism: Int
Default level of parallelism to use when not given by user (e.g.
Default level of parallelism to use when not given by user (e.g. parallelize and makeRDD).
  40. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#deployMode:String "Permalink") def deployMode: String
  41. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#doubleAccumulator\(name:String\):org.apache.spark.util.DoubleAccumulator "Permalink") def doubleAccumulator(name: String): [DoubleAccumulator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/DoubleAccumulator.html "org.apache.spark.util.DoubleAccumulator")
Create and register a double accumulator, which starts with 0 and accumulates inputs by `add`.
  42. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#doubleAccumulator:org.apache.spark.util.DoubleAccumulator "Permalink") def doubleAccumulator: [DoubleAccumulator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/DoubleAccumulator.html "org.apache.spark.util.DoubleAccumulator")
Create and register a double accumulator, which starts with 0 and accumulates inputs by `add`.
  43. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#emptyRDD\[T\]\(implicitevidence$8:scala.reflect.ClassTag\[T\]\):org.apache.spark.rdd.RDD\[T\] "Permalink") def emptyRDD[T](implicit arg0: ClassTag[T]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[T]
Get an RDD that has no partitions or elements.
  44. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  45. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#equals\(x$1:Object\):Boolean "Permalink") def equals(arg0: AnyRef): Boolean

Definition Classes
    AnyRef → Any
  46. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#files:Seq\[String\] "Permalink") def files: Seq[String]
  47. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#getAllPools:Seq\[org.apache.spark.scheduler.Schedulable\] "Permalink") def getAllPools: Seq[Schedulable]
Return pools for fair scheduler
Return pools for fair scheduler

Annotations
     @DeveloperApi()
  48. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#getCheckpointDir:Option\[String\] "Permalink") def getCheckpointDir: Option[String]
  49. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef]

Definition Classes
    AnyRef → Any

Annotations
     @IntrinsicCandidate() @native()
  50. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#getConf:org.apache.spark.SparkConf "Permalink") def getConf: [SparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html "org.apache.spark.SparkConf")
Return a copy of this SparkContext's configuration.
Return a copy of this SparkContext's configuration. The configuration _cannot_ be changed at runtime.
  51. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#getExecutorMemoryStatus:scala.collection.Map\[String,\(Long,Long\)\] "Permalink") def getExecutorMemoryStatus: Map[String, (Long, Long)]
Return a map from the block manager to the max memory available for caching and the remaining memory available for caching.
  52. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#getJobTags\(\):Set\[String\] "Permalink") def getJobTags(): Set[String]
Get the tags that are currently set to be assigned to all the jobs started by this thread.
Get the tags that are currently set to be assigned to all the jobs started by this thread.

Since

3.5.0
  53. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#getLocalProperty\(key:String\):String "Permalink") def getLocalProperty(key: String): String
Get a local property set in this thread, or null if it is missing.
Get a local property set in this thread, or null if it is missing. See `org.apache.spark.SparkContext.setLocalProperty`.
  54. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#getPersistentRDDs:scala.collection.Map\[Int,org.apache.spark.rdd.RDD\[_\]\] "Permalink") def getPersistentRDDs: Map[Int, [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[_]]
Returns an immutable map of RDDs that have marked themselves as persistent via cache() call.
Returns an immutable map of RDDs that have marked themselves as persistent via cache() call.

Note

This does not necessarily mean the caching or computation was successful.
  55. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#getPoolForName\(pool:String\):Option\[org.apache.spark.scheduler.Schedulable\] "Permalink") def getPoolForName(pool: String): Option[Schedulable]
Return the pool associated with the given name, if one exists
Return the pool associated with the given name, if one exists

Annotations
     @DeveloperApi()
  56. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#getRDDStorageInfo:Array\[org.apache.spark.storage.RDDInfo\] "Permalink") def getRDDStorageInfo: Array[[RDDInfo](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/RDDInfo.html "org.apache.spark.storage.RDDInfo")]
Return information about what RDDs are cached, if they are in mem or on disk, how much space they take, etc.
Return information about what RDDs are cached, if they are in mem or on disk, how much space they take, etc.

Annotations
     @DeveloperApi()
  57. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#getReadOnlyConf:org.apache.spark.ReadOnlySparkConf "Permalink") def getReadOnlyConf: [ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html "org.apache.spark.ReadOnlySparkConf")
Get a read-only reference to the spark conf.
Get a read-only reference to the spark conf. This is preferred version over [getConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#getConf:org.apache.spark.SparkConf).
  58. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#getSchedulingMode:org.apache.spark.scheduler.SchedulingMode.SchedulingMode "Permalink") def getSchedulingMode: [SchedulingMode](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SchedulingMode$.html#SchedulingMode=org.apache.spark.scheduler.SchedulingMode.Value)
Return current scheduling mode
  59. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#hadoopConfiguration:org.apache.hadoop.conf.Configuration "Permalink") def hadoopConfiguration: Configuration
A default Hadoop Configuration for the Hadoop code (e.g.
A default Hadoop Configuration for the Hadoop code (e.g. file systems) that we reuse.

Note

As it will be reused in all Hadoop RDDs, it's better not to modify it unless you plan to set some global configurations for all Hadoop RDDs.
  60. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#hadoopFile\[K,V,F<:org.apache.hadoop.mapred.InputFormat\[K,V\]\]\(path:String\)\(implicitkm:scala.reflect.ClassTag\[K\],implicitvm:scala.reflect.ClassTag\[V\],implicitfm:scala.reflect.ClassTag\[F\]\):org.apache.spark.rdd.RDD\[\(K,V\)\] "Permalink") def hadoopFile[K, V, F <: InputFormat[K, V]](path: String)(implicit km: ClassTag[K], vm: ClassTag[V], fm: ClassTag[F]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, V)]
Smarter version of hadoopFile() that uses class tags to figure out the classes of keys, values and the InputFormat so that users don't need to pass them directly.
Smarter version of hadoopFile() that uses class tags to figure out the classes of keys, values and the InputFormat so that users don't need to pass them directly. Instead, callers can just write, for example,

```
val file = sparkContext.hadoopFile[LongWritable, Text, TextInputFormat](path)
```

path

directory to the input data files, the path can be comma separated paths as a list of inputs

returns

RDD of tuples of key and corresponding value

Note

Because Hadoop's RecordReader class re-uses the same Writable object for each record, directly caching the returned RDD or directly passing it to an aggregation or shuffle operation will create many references to the same object. If you plan to directly cache, sort, or aggregate Hadoop writable objects, you should first copy them using a `map` function.
  61. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#hadoopFile\[K,V,F<:org.apache.hadoop.mapred.InputFormat\[K,V\]\]\(path:String,minPartitions:Int\)\(implicitkm:scala.reflect.ClassTag\[K\],implicitvm:scala.reflect.ClassTag\[V\],implicitfm:scala.reflect.ClassTag\[F\]\):org.apache.spark.rdd.RDD\[\(K,V\)\] "Permalink") def hadoopFile[K, V, F <: InputFormat[K, V]](path: String, minPartitions: Int)(implicit km: ClassTag[K], vm: ClassTag[V], fm: ClassTag[F]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, V)]
Smarter version of hadoopFile() that uses class tags to figure out the classes of keys, values and the InputFormat so that users don't need to pass them directly.
Smarter version of hadoopFile() that uses class tags to figure out the classes of keys, values and the InputFormat so that users don't need to pass them directly. Instead, callers can just write, for example,

```
val file = sparkContext.hadoopFile[LongWritable, Text, TextInputFormat](path, minPartitions)
```

path

directory to the input data files, the path can be comma separated paths as a list of inputs

minPartitions

suggested minimum number of partitions for the resulting RDD

returns

RDD of tuples of key and corresponding value

Note

Because Hadoop's RecordReader class re-uses the same Writable object for each record, directly caching the returned RDD or directly passing it to an aggregation or shuffle operation will create many references to the same object. If you plan to directly cache, sort, or aggregate Hadoop writable objects, you should first copy them using a `map` function.
  62. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#hadoopFile\[K,V\]\(path:String,inputFormatClass:Class\[_<:org.apache.hadoop.mapred.InputFormat\[K,V\]\],keyClass:Class\[K\],valueClass:Class\[V\],minPartitions:Int\):org.apache.spark.rdd.RDD\[\(K,V\)\] "Permalink") def hadoopFile[K, V](path: String, inputFormatClass: Class[_ <: InputFormat[K, V]], keyClass: Class[K], valueClass: Class[V], minPartitions: Int = [defaultMinPartitions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#defaultMinPartitions:Int)): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, V)]
Get an RDD for a Hadoop file with an arbitrary InputFormat
Get an RDD for a Hadoop file with an arbitrary InputFormat

path

directory to the input data files, the path can be comma separated paths as a list of inputs

inputFormatClass

storage format of the data to be read

keyClass

`Class` of the key associated with the `inputFormatClass` parameter

valueClass

`Class` of the value associated with the `inputFormatClass` parameter

minPartitions

suggested minimum number of partitions for the resulting RDD

returns

RDD of tuples of key and corresponding value

Note

Because Hadoop's RecordReader class re-uses the same Writable object for each record, directly caching the returned RDD or directly passing it to an aggregation or shuffle operation will create many references to the same object. If you plan to directly cache, sort, or aggregate Hadoop writable objects, you should first copy them using a `map` function.
  63. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#hadoopRDD\[K,V\]\(conf:org.apache.hadoop.mapred.JobConf,inputFormatClass:Class\[_<:org.apache.hadoop.mapred.InputFormat\[K,V\]\],keyClass:Class\[K\],valueClass:Class\[V\],minPartitions:Int\):org.apache.spark.rdd.RDD\[\(K,V\)\] "Permalink") def hadoopRDD[K, V](conf: JobConf, inputFormatClass: Class[_ <: InputFormat[K, V]], keyClass: Class[K], valueClass: Class[V], minPartitions: Int = [defaultMinPartitions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#defaultMinPartitions:Int)): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, V)]
Get an RDD for a Hadoop-readable dataset from a Hadoop JobConf given its InputFormat and other necessary info (e.g.
Get an RDD for a Hadoop-readable dataset from a Hadoop JobConf given its InputFormat and other necessary info (e.g. file name for a filesystem-based dataset, table name for HyperTable), using the older MapReduce API (`org.apache.hadoop.mapred`).

conf

JobConf for setting up the dataset. Note: This will be put into a Broadcast. Therefore if you plan to reuse this conf to create multiple RDDs, you need to make sure you won't modify the conf. A safe approach is always creating a new conf for a new RDD.

inputFormatClass

storage format of the data to be read

keyClass

`Class` of the key associated with the `inputFormatClass` parameter

valueClass

`Class` of the value associated with the `inputFormatClass` parameter

minPartitions

Minimum number of Hadoop Splits to generate.

returns

RDD of tuples of key and corresponding value

Note

Because Hadoop's RecordReader class re-uses the same Writable object for each record, directly caching the returned RDD or directly passing it to an aggregation or shuffle operation will create many references to the same object. If you plan to directly cache, sort, or aggregate Hadoop writable objects, you should first copy them using a `map` function.
  64. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#hashCode\(\):Int "Permalink") def hashCode(): Int

Definition Classes
    AnyRef → Any

Annotations
     @IntrinsicCandidate() @native()
  65. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#initializeLogIfNecessary\(isInterpreter:Boolean,silent:Boolean\):Boolean "Permalink") def initializeLogIfNecessary(isInterpreter: Boolean, silent: Boolean): Boolean

Attributes
    protected

Definition Classes
    Logging
  66. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#initializeLogIfNecessary\(isInterpreter:Boolean\):Unit "Permalink") def initializeLogIfNecessary(isInterpreter: Boolean): Unit

Attributes
    protected

Definition Classes
    Logging
  67. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean

Definition Classes
    Any
  68. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#isLocal:Boolean "Permalink") def isLocal: Boolean
  69. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#isStopped:Boolean "Permalink") def isStopped: Boolean

returns

true if context is stopped or in the midst of stopping.
  70. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#isTraceEnabled\(\):Boolean "Permalink") def isTraceEnabled(): Boolean

Attributes
    protected

Definition Classes
    Logging
  71. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#jars:Seq\[String\] "Permalink") def jars: Seq[String]
  72. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#killExecutor\(executorId:String\):Boolean "Permalink") def killExecutor(executorId: String): Boolean
Request that the cluster manager kill the specified executor.
Request that the cluster manager kill the specified executor.

returns

whether the request is received.

Annotations
     @DeveloperApi()

Note

This is an indication to the cluster manager that the application wishes to adjust its resource usage downwards. If the application wishes to replace the executor it kills through this method with a new one, it should follow up explicitly with a call to {{SparkContext#requestExecutors}}.
  73. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#killExecutors\(executorIds:Seq\[String\]\):Boolean "Permalink") def killExecutors(executorIds: Seq[String]): Boolean
Request that the cluster manager kill the specified executors.
Request that the cluster manager kill the specified executors.
This is not supported when dynamic allocation is turned on.

returns

whether the request is received.

Annotations
     @DeveloperApi()

Note

This is an indication to the cluster manager that the application wishes to adjust its resource usage downwards. If the application wishes to replace the executors it kills through this method with new ones, it should follow up explicitly with a call to {{SparkContext#requestExecutors}}.
  74. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#killTaskAttempt\(taskId:Long,interruptThread:Boolean,reason:String\):Boolean "Permalink") def killTaskAttempt(taskId: Long, interruptThread: Boolean = true, reason: String = "killed via SparkContext.killTaskAttempt"): Boolean
Kill and reschedule the given task attempt.
Kill and reschedule the given task attempt. Task ids can be obtained from the Spark UI or through SparkListener.onTaskStart.

taskId

the task ID to kill. This id uniquely identifies the task attempt.

interruptThread

whether to interrupt the thread running the task.

reason

the reason for killing the task, which should be a short string. If a task is killed multiple times with different reasons, only one reason will be reported.

returns

Whether the task was successfully killed.
  75. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#listArchives\(\):Seq\[String\] "Permalink") def listArchives(): Seq[String]
Returns a list of archive paths that are added to resources.
Returns a list of archive paths that are added to resources.

Annotations
     @Experimental()

Since

3.1.0
  76. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#listFiles\(\):Seq\[String\] "Permalink") def listFiles(): Seq[String]
Returns a list of file paths that are added to resources.
  77. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#listJars\(\):Seq\[String\] "Permalink") def listJars(): Seq[String]
Returns a list of jar files that are added to resources.
  78. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#localProperties:InheritableThreadLocal\[java.util.Properties\] "Permalink") val localProperties: [InheritableThreadLocal](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InheritableThreadLocal.html#java.lang.InheritableThreadLocal "java.lang.InheritableThreadLocal")[[Properties](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Properties.html#java.util.Properties "java.util.Properties")]

Attributes
    protected[[spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")]
  79. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#log:org.slf4j.Logger "Permalink") def log: Logger

Attributes
    protected

Definition Classes
    Logging
  80. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#logBasedOnLevel\(level:org.slf4j.event.Level\)\(f:=>org.apache.spark.internal.MessageWithContext\):Unit "Permalink") def logBasedOnLevel(level: Level)(f: => MessageWithContext): Unit

Attributes
    protected

Definition Classes
    Logging
  81. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#logDebug\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logDebug(msg: => String, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  82. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#logDebug\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logDebug(entry: LogEntry, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  83. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#logDebug\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logDebug(entry: LogEntry): Unit

Attributes
    protected

Definition Classes
    Logging
  84. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#logDebug\(msg:=>String\):Unit "Permalink") def logDebug(msg: => String): Unit

Attributes
    protected

Definition Classes
    Logging
  85. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#logError\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logError(msg: => String, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  86. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#logError\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logError(entry: LogEntry, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  87. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#logError\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logError(entry: LogEntry): Unit

Attributes
    protected

Definition Classes
    Logging
  88. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#logError\(msg:=>String\):Unit "Permalink") def logError(msg: => String): Unit

Attributes
    protected

Definition Classes
    Logging
  89. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#logInfo\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logInfo(msg: => String, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  90. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#logInfo\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logInfo(entry: LogEntry, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  91. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#logInfo\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logInfo(entry: LogEntry): Unit

Attributes
    protected

Definition Classes
    Logging
  92. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#logInfo\(msg:=>String\):Unit "Permalink") def logInfo(msg: => String): Unit

Attributes
    protected

Definition Classes
    Logging
  93. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#logName:String "Permalink") def logName: [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String")

Attributes
    protected

Definition Classes
    Logging
  94. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#logTrace\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logTrace(msg: => String, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  95. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#logTrace\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logTrace(entry: LogEntry, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  96. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#logTrace\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logTrace(entry: LogEntry): Unit

Attributes
    protected

Definition Classes
    Logging
  97. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#logTrace\(msg:=>String\):Unit "Permalink") def logTrace(msg: => String): Unit

Attributes
    protected

Definition Classes
    Logging
  98. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#logWarning\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logWarning(msg: => String, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  99. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#logWarning\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logWarning(entry: LogEntry, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  100. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#logWarning\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logWarning(entry: LogEntry): Unit

Attributes
    protected

Definition Classes
    Logging
  101. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#logWarning\(msg:=>String\):Unit "Permalink") def logWarning(msg: => String): Unit

Attributes
    protected

Definition Classes
    Logging
  102. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#longAccumulator\(name:String\):org.apache.spark.util.LongAccumulator "Permalink") def longAccumulator(name: String): [LongAccumulator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/LongAccumulator.html "org.apache.spark.util.LongAccumulator")
Create and register a long accumulator, which starts with 0 and accumulates inputs by `add`.
  103. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#longAccumulator:org.apache.spark.util.LongAccumulator "Permalink") def longAccumulator: [LongAccumulator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/LongAccumulator.html "org.apache.spark.util.LongAccumulator")
Create and register a long accumulator, which starts with 0 and accumulates inputs by `add`.
  104. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#makeRDD\[T\]\(seq:Seq\[\(T,Seq\[String\]\)\]\)\(implicitevidence$3:scala.reflect.ClassTag\[T\]\):org.apache.spark.rdd.RDD\[T\] "Permalink") def makeRDD[T](seq: Seq[(T, Seq[String])])(implicit arg0: ClassTag[T]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[T]
Distribute a local Scala collection to form an RDD, with one or more location preferences (hostnames of Spark nodes) for each object.
Distribute a local Scala collection to form an RDD, with one or more location preferences (hostnames of Spark nodes) for each object. Create a new partition for each collection item.

seq

list of tuples of data and location preferences (hostnames of Spark nodes)

returns

RDD representing data partitioned according to location preferences
  105. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#makeRDD\[T\]\(seq:Seq\[T\],numSlices:Int\)\(implicitevidence$2:scala.reflect.ClassTag\[T\]\):org.apache.spark.rdd.RDD\[T\] "Permalink") def makeRDD[T](seq: Seq[T], numSlices: Int = [defaultParallelism](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#defaultParallelism:Int))(implicit arg0: ClassTag[T]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[T]
Distribute a local Scala collection to form an RDD.
Distribute a local Scala collection to form an RDD.
This method is identical to `parallelize`.

seq

Scala collection to distribute

numSlices

number of partitions to divide the collection into

returns

RDD representing distributed collection
  106. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#master:String "Permalink") def master: String
  107. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  108. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#newAPIHadoopFile\[K,V,F<:org.apache.hadoop.mapreduce.InputFormat\[K,V\]\]\(path:String,fClass:Class\[F\],kClass:Class\[K\],vClass:Class\[V\],conf:org.apache.hadoop.conf.Configuration\):org.apache.spark.rdd.RDD\[\(K,V\)\] "Permalink") def newAPIHadoopFile[K, V, F <: InputFormat[K, V]](path: String, fClass: Class[F], kClass: Class[K], vClass: Class[V], conf: Configuration = [hadoopConfiguration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#hadoopConfiguration:org.apache.hadoop.conf.Configuration)): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, V)]
Get an RDD for a given Hadoop file with an arbitrary new API InputFormat and extra configuration options to pass to the input format.
Get an RDD for a given Hadoop file with an arbitrary new API InputFormat and extra configuration options to pass to the input format.

path

directory to the input data files, the path can be comma separated paths as a list of inputs

fClass

storage format of the data to be read

kClass

`Class` of the key associated with the `fClass` parameter

vClass

`Class` of the value associated with the `fClass` parameter

conf

Hadoop configuration

returns

RDD of tuples of key and corresponding value

Note

Because Hadoop's RecordReader class re-uses the same Writable object for each record, directly caching the returned RDD or directly passing it to an aggregation or shuffle operation will create many references to the same object. If you plan to directly cache, sort, or aggregate Hadoop writable objects, you should first copy them using a `map` function.
  109. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#newAPIHadoopFile\[K,V,F<:org.apache.hadoop.mapreduce.InputFormat\[K,V\]\]\(path:String\)\(implicitkm:scala.reflect.ClassTag\[K\],implicitvm:scala.reflect.ClassTag\[V\],implicitfm:scala.reflect.ClassTag\[F\]\):org.apache.spark.rdd.RDD\[\(K,V\)\] "Permalink") def newAPIHadoopFile[K, V, F <: InputFormat[K, V]](path: String)(implicit km: ClassTag[K], vm: ClassTag[V], fm: ClassTag[F]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, V)]
Smarter version of `newApiHadoopFile` that uses class tags to figure out the classes of keys, values and the `org.apache.hadoop.mapreduce.InputFormat` (new MapReduce API) so that user don't need to pass them directly.
Smarter version of `newApiHadoopFile` that uses class tags to figure out the classes of keys, values and the `org.apache.hadoop.mapreduce.InputFormat` (new MapReduce API) so that user don't need to pass them directly. Instead, callers can just write, for example: ``` val file = sparkContext.hadoopFile[LongWritable, Text, TextInputFormat](path) ``` ``````

path

directory to the input data files, the path can be comma separated paths as a list of inputs

returns

RDD of tuples of key and corresponding value

Note

Because Hadoop's RecordReader class re-uses the same Writable object for each record, directly caching the returned RDD or directly passing it to an aggregation or shuffle operation will create many references to the same object. If you plan to directly cache, sort, or aggregate Hadoop writable objects, you should first copy them using a `map` function.
  110. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#newAPIHadoopRDD\[K,V,F<:org.apache.hadoop.mapreduce.InputFormat\[K,V\]\]\(conf:org.apache.hadoop.conf.Configuration,fClass:Class\[F\],kClass:Class\[K\],vClass:Class\[V\]\):org.apache.spark.rdd.RDD\[\(K,V\)\] "Permalink") def newAPIHadoopRDD[K, V, F <: InputFormat[K, V]](conf: Configuration = [hadoopConfiguration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#hadoopConfiguration:org.apache.hadoop.conf.Configuration), fClass: Class[F], kClass: Class[K], vClass: Class[V]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, V)]
Get an RDD for a given Hadoop file with an arbitrary new API InputFormat and extra configuration options to pass to the input format.
Get an RDD for a given Hadoop file with an arbitrary new API InputFormat and extra configuration options to pass to the input format.

conf

Configuration for setting up the dataset. Note: This will be put into a Broadcast. Therefore if you plan to reuse this conf to create multiple RDDs, you need to make sure you won't modify the conf. A safe approach is always creating a new conf for a new RDD.

fClass

storage format of the data to be read

kClass

`Class` of the key associated with the `fClass` parameter

vClass

`Class` of the value associated with the `fClass` parameter

Note

Because Hadoop's RecordReader class re-uses the same Writable object for each record, directly caching the returned RDD or directly passing it to an aggregation or shuffle operation will create many references to the same object. If you plan to directly cache, sort, or aggregate Hadoop writable objects, you should first copy them using a `map` function.
  111. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#notify\(\):Unit "Permalink") final  def notify(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  112. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  113. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#objectFile\[T\]\(path:String,minPartitions:Int\)\(implicitevidence$4:scala.reflect.ClassTag\[T\]\):org.apache.spark.rdd.RDD\[T\] "Permalink") def objectFile[T](path: String, minPartitions: Int = [defaultMinPartitions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#defaultMinPartitions:Int))(implicit arg0: ClassTag[T]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[T]
Load an RDD saved as a SequenceFile containing serialized objects, with NullWritable keys and BytesWritable values that contain a serialized partition.
Load an RDD saved as a SequenceFile containing serialized objects, with NullWritable keys and BytesWritable values that contain a serialized partition. This is still an experimental storage format and may not be supported exactly as is in future Spark releases. It will also be pretty slow if you use the default serializer (Java serialization), though the nice thing about it is that there's very little effort required to save arbitrary objects.

path

directory to the input data files, the path can be comma separated paths as a list of inputs

minPartitions

suggested minimum number of partitions for the resulting RDD

returns

RDD representing deserialized data from the file(s)
  114. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#parallelize\[T\]\(seq:Seq\[T\],numSlices:Int\)\(implicitevidence$1:scala.reflect.ClassTag\[T\]\):org.apache.spark.rdd.RDD\[T\] "Permalink") def parallelize[T](seq: Seq[T], numSlices: Int = [defaultParallelism](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#defaultParallelism:Int))(implicit arg0: ClassTag[T]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[T]
Distribute a local Scala collection to form an RDD.
Distribute a local Scala collection to form an RDD.

seq

Scala collection to distribute

numSlices

number of partitions to divide the collection into

returns

RDD representing distributed collection

Note

Parallelize acts lazily. If `seq` is a mutable collection and is altered after the call to parallelize and before the first action on the RDD, the resultant RDD will reflect the modified collection. Pass a copy of the argument to avoid this.
,
avoid using `parallelize(Seq())` to create an empty `RDD`. Consider `emptyRDD` for an RDD with no partitions, or `parallelize(Seq[T]())` for an RDD of `T` with empty partitions.
  115. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#range\(start:Long,end:Long,step:Long,numSlices:Int\):org.apache.spark.rdd.RDD\[Long\] "Permalink") def range(start: Long, end: Long, step: Long = 1, numSlices: Int = [defaultParallelism](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#defaultParallelism:Int)): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[Long]
Creates a new RDD[Long] containing elements from `start` to `end`(exclusive), increased by `step` every element.
Creates a new RDD[Long] containing elements from `start` to `end`(exclusive), increased by `step` every element.

start

the start value.

end

the end value.

step

the incremental step

numSlices

number of partitions to divide the collection into

returns

RDD representing distributed range

Note

if we need to cache this RDD, we should make sure each partition does not exceed limit.
  116. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#register\(acc:org.apache.spark.util.AccumulatorV2\[_,_\],name:String\):Unit "Permalink") def register(acc: [AccumulatorV2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html "org.apache.spark.util.AccumulatorV2")[_, _], name: String): Unit
Register the given accumulator with given name.
Register the given accumulator with given name.

Note

Accumulators must be registered before use, or it will throw exception.
  117. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#register\(acc:org.apache.spark.util.AccumulatorV2\[_,_\]\):Unit "Permalink") def register(acc: [AccumulatorV2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html "org.apache.spark.util.AccumulatorV2")[_, _]): Unit
Register the given accumulator.
Register the given accumulator.

Note

Accumulators must be registered before use, or it will throw exception.
  118. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#removeJobTag\(tag:String\):Unit "Permalink") def removeJobTag(tag: String): Unit
Remove a tag previously added to be assigned to all the jobs started by this thread.
Remove a tag previously added to be assigned to all the jobs started by this thread. Noop if such a tag was not added earlier.

tag

The tag to be removed. Cannot contain ',' (comma) character.

Since

3.5.0
  119. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#removeJobTags\(tags:Set\[String\]\):Unit "Permalink") def removeJobTags(tags: Set[String]): Unit
Remove multiple tags to be assigned to all the jobs started by this thread.
Remove multiple tags to be assigned to all the jobs started by this thread. See [removeJobTag](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#removeJobTag\(tag:String\):Unit) for more details.

tags

The tags to be removed. Cannot contain ',' (comma) character.

Since

4.0.0
  120. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#removeSparkListener\(listener:org.apache.spark.scheduler.SparkListenerInterface\):Unit "Permalink") def removeSparkListener(listener: SparkListenerInterface): Unit
Deregister the listener from Spark's listener bus.
Deregister the listener from Spark's listener bus.

Annotations
     @DeveloperApi()
  121. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#requestExecutors\(numAdditionalExecutors:Int\):Boolean "Permalink") def requestExecutors(numAdditionalExecutors: Int): Boolean
Request an additional number of executors from the cluster manager.
Request an additional number of executors from the cluster manager.

returns

whether the request is received.

Annotations
     @DeveloperApi()
  122. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#requestTotalExecutors\(numExecutors:Int,localityAwareTasks:Int,hostToLocalTaskCount:scala.collection.immutable.Map\[String,Int\]\):Boolean "Permalink") def requestTotalExecutors(numExecutors: Int, localityAwareTasks: Int, hostToLocalTaskCount: Map[String, Int]): Boolean
Update the cluster manager on our scheduling needs.
Update the cluster manager on our scheduling needs. Three bits of information are included to help it make decisions. This applies to the default ResourceProfile.

numExecutors

The total number of executors we'd like to have. The cluster manager shouldn't kill any running executor to reach this number, but, if all existing executors were to die, this is the number of executors we'd want to be allocated.

localityAwareTasks

The number of tasks in all active stages that have a locality preferences. This includes running, pending, and completed tasks.

hostToLocalTaskCount

A map of hosts to the number of tasks from all active stages that would like to like to run on that host. This includes running, pending, and completed tasks.

returns

whether the request is acknowledged by the cluster manager.

Annotations
     @DeveloperApi()
  123. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#resources:scala.collection.Map\[String,org.apache.spark.resource.ResourceInformation\] "Permalink") def resources: Map[String, [ResourceInformation](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/resource/ResourceInformation.html "org.apache.spark.resource.ResourceInformation")]
  124. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#runApproximateJob\[T,U,R\]\(rdd:org.apache.spark.rdd.RDD\[T\],func:\(org.apache.spark.TaskContext,Iterator\[T\]\)=>U,evaluator:org.apache.spark.partial.ApproximateEvaluator\[U,R\],timeout:Long\):org.apache.spark.partial.PartialResult\[R\] "Permalink") def runApproximateJob[T, U, R](rdd: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[T], func: ([TaskContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskContext.html "org.apache.spark.TaskContext"), Iterator[T]) => U, evaluator: ApproximateEvaluator[U, R], timeout: Long): [PartialResult](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/partial/PartialResult.html "org.apache.spark.partial.PartialResult")[R]
Run a job that can return approximate results.
Run a job that can return approximate results.

rdd

target RDD to run tasks on

func

a function to run on each partition of the RDD

evaluator

`ApproximateEvaluator` to receive the partial results

timeout

maximum time to wait for the job, in milliseconds

returns

partial result (how partial depends on whether the job was finished before or after timeout)

Annotations
     @DeveloperApi()
  125. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#runJob\[T,U\]\(rdd:org.apache.spark.rdd.RDD\[T\],processPartition:Iterator\[T\]=>U,resultHandler:\(Int,U\)=>Unit\)\(implicitevidence$17:scala.reflect.ClassTag\[U\]\):Unit "Permalink") def runJob[T, U](rdd: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[T], processPartition: (Iterator[T]) => U, resultHandler: (Int, U) => Unit)(implicit arg0: ClassTag[U]): Unit
Run a job on all partitions in an RDD and pass the results to a handler function.
Run a job on all partitions in an RDD and pass the results to a handler function.

rdd

target RDD to run tasks on

processPartition

a function to run on each partition of the RDD

resultHandler

callback to pass each result to
  126. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#runJob\[T,U\]\(rdd:org.apache.spark.rdd.RDD\[T\],processPartition:\(org.apache.spark.TaskContext,Iterator\[T\]\)=>U,resultHandler:\(Int,U\)=>Unit\)\(implicitevidence$16:scala.reflect.ClassTag\[U\]\):Unit "Permalink") def runJob[T, U](rdd: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[T], processPartition: ([TaskContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskContext.html "org.apache.spark.TaskContext"), Iterator[T]) => U, resultHandler: (Int, U) => Unit)(implicit arg0: ClassTag[U]): Unit
Run a job on all partitions in an RDD and pass the results to a handler function.
Run a job on all partitions in an RDD and pass the results to a handler function. The function that is run against each partition additionally takes `TaskContext` argument.

rdd

target RDD to run tasks on

processPartition

a function to run on each partition of the RDD

resultHandler

callback to pass each result to
  127. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#runJob\[T,U\]\(rdd:org.apache.spark.rdd.RDD\[T\],func:Iterator\[T\]=>U\)\(implicitevidence$15:scala.reflect.ClassTag\[U\]\):Array\[U\] "Permalink") def runJob[T, U](rdd: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[T], func: (Iterator[T]) => U)(implicit arg0: ClassTag[U]): Array[U]
Run a job on all partitions in an RDD and return the results in an array.
Run a job on all partitions in an RDD and return the results in an array.

rdd

target RDD to run tasks on

func

a function to run on each partition of the RDD

returns

in-memory collection with a result of the job (each collection element will contain a result from one partition)
  128. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#runJob\[T,U\]\(rdd:org.apache.spark.rdd.RDD\[T\],func:\(org.apache.spark.TaskContext,Iterator\[T\]\)=>U\)\(implicitevidence$14:scala.reflect.ClassTag\[U\]\):Array\[U\] "Permalink") def runJob[T, U](rdd: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[T], func: ([TaskContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskContext.html "org.apache.spark.TaskContext"), Iterator[T]) => U)(implicit arg0: ClassTag[U]): Array[U]
Run a job on all partitions in an RDD and return the results in an array.
Run a job on all partitions in an RDD and return the results in an array. The function that is run against each partition additionally takes `TaskContext` argument.

rdd

target RDD to run tasks on

func

a function to run on each partition of the RDD

returns

in-memory collection with a result of the job (each collection element will contain a result from one partition)
  129. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#runJob\[T,U\]\(rdd:org.apache.spark.rdd.RDD\[T\],func:Iterator\[T\]=>U,partitions:Seq\[Int\]\)\(implicitevidence$13:scala.reflect.ClassTag\[U\]\):Array\[U\] "Permalink") def runJob[T, U](rdd: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[T], func: (Iterator[T]) => U, partitions: Seq[Int])(implicit arg0: ClassTag[U]): Array[U]
Run a function on a given set of partitions in an RDD and return the results as an array.
Run a function on a given set of partitions in an RDD and return the results as an array.

rdd

target RDD to run tasks on

func

a function to run on each partition of the RDD

partitions

set of partitions to run on; some jobs may not want to compute on all partitions of the target RDD, e.g. for operations like `first()`

returns

in-memory collection with a result of the job (each collection element will contain a result from one partition)
  130. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#runJob\[T,U\]\(rdd:org.apache.spark.rdd.RDD\[T\],func:\(org.apache.spark.TaskContext,Iterator\[T\]\)=>U,partitions:Seq\[Int\]\)\(implicitevidence$12:scala.reflect.ClassTag\[U\]\):Array\[U\] "Permalink") def runJob[T, U](rdd: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[T], func: ([TaskContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskContext.html "org.apache.spark.TaskContext"), Iterator[T]) => U, partitions: Seq[Int])(implicit arg0: ClassTag[U]): Array[U]
Run a function on a given set of partitions in an RDD and return the results as an array.
Run a function on a given set of partitions in an RDD and return the results as an array. The function that is run against each partition additionally takes `TaskContext` argument.

rdd

target RDD to run tasks on

func

a function to run on each partition of the RDD

partitions

set of partitions to run on; some jobs may not want to compute on all partitions of the target RDD, e.g. for operations like `first()`

returns

in-memory collection with a result of the job (each collection element will contain a result from one partition)
  131. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#runJob\[T,U\]\(rdd:org.apache.spark.rdd.RDD\[T\],func:\(org.apache.spark.TaskContext,Iterator\[T\]\)=>U,partitions:Seq\[Int\],resultHandler:\(Int,U\)=>Unit\)\(implicitevidence$11:scala.reflect.ClassTag\[U\]\):Unit "Permalink") def runJob[T, U](rdd: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[T], func: ([TaskContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskContext.html "org.apache.spark.TaskContext"), Iterator[T]) => U, partitions: Seq[Int], resultHandler: (Int, U) => Unit)(implicit arg0: ClassTag[U]): Unit
Run a function on a given set of partitions in an RDD and pass the results to the given handler function.
Run a function on a given set of partitions in an RDD and pass the results to the given handler function. This is the main entry point for all actions in Spark.

rdd

target RDD to run tasks on

func

a function to run on each partition of the RDD

partitions

set of partitions to run on; some jobs may not want to compute on all partitions of the target RDD, e.g. for operations like `first()`

resultHandler

callback to pass each result to
  132. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#sequenceFile\[K,V\]\(path:String,minPartitions:Int\)\(implicitkm:scala.reflect.ClassTag\[K\],implicitvm:scala.reflect.ClassTag\[V\],implicitkcf:\(\)=>org.apache.spark.WritableConverter\[K\],implicitvcf:\(\)=>org.apache.spark.WritableConverter\[V\]\):org.apache.spark.rdd.RDD\[\(K,V\)\] "Permalink") def sequenceFile[K, V](path: String, minPartitions: Int = [defaultMinPartitions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#defaultMinPartitions:Int))(implicit km: ClassTag[K], vm: ClassTag[V], kcf: () => WritableConverter[K], vcf: () => WritableConverter[V]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, V)]
Version of sequenceFile() for types implicitly convertible to Writables through a WritableConverter.
Version of sequenceFile() for types implicitly convertible to Writables through a WritableConverter. For example, to access a SequenceFile where the keys are Text and the values are IntWritable, you could simply write

```
sparkContext.sequenceFile[String, Int](path, ...)
```

WritableConverters are provided in a somewhat strange way (by an implicit function) to support both subclasses of Writable and types for which we define a converter (e.g. Int to IntWritable). The most natural thing would've been to have implicit objects for the converters, but then we couldn't have an object for every subclass of Writable (you can't have a parameterized singleton object). We use functions instead to create a new converter for the appropriate type. In addition, we pass the converter a ClassTag of its type to allow it to figure out the Writable class to use in the subclass case.

path

directory to the input data files, the path can be comma separated paths as a list of inputs

minPartitions

suggested minimum number of partitions for the resulting RDD

returns

RDD of tuples of key and corresponding value

Note

Because Hadoop's RecordReader class re-uses the same Writable object for each record, directly caching the returned RDD or directly passing it to an aggregation or shuffle operation will create many references to the same object. If you plan to directly cache, sort, or aggregate Hadoop writable objects, you should first copy them using a `map` function.
  133. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#sequenceFile\[K,V\]\(path:String,keyClass:Class\[K\],valueClass:Class\[V\]\):org.apache.spark.rdd.RDD\[\(K,V\)\] "Permalink") def sequenceFile[K, V](path: String, keyClass: Class[K], valueClass: Class[V]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, V)]
Get an RDD for a Hadoop SequenceFile with given key and value types.
Get an RDD for a Hadoop SequenceFile with given key and value types.

path

directory to the input data files, the path can be comma separated paths as a list of inputs

keyClass

`Class` of the key associated with `SequenceFileInputFormat`

valueClass

`Class` of the value associated with `SequenceFileInputFormat`

returns

RDD of tuples of key and corresponding value

Note

Because Hadoop's RecordReader class re-uses the same Writable object for each record, directly caching the returned RDD or directly passing it to an aggregation or shuffle operation will create many references to the same object. If you plan to directly cache, sort, or aggregate Hadoop writable objects, you should first copy them using a `map` function.
  134. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#sequenceFile\[K,V\]\(path:String,keyClass:Class\[K\],valueClass:Class\[V\],minPartitions:Int\):org.apache.spark.rdd.RDD\[\(K,V\)\] "Permalink") def sequenceFile[K, V](path: String, keyClass: Class[K], valueClass: Class[V], minPartitions: Int): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, V)]
Get an RDD for a Hadoop SequenceFile with given key and value types.
Get an RDD for a Hadoop SequenceFile with given key and value types.

path

directory to the input data files, the path can be comma separated paths as a list of inputs

keyClass

`Class` of the key associated with `SequenceFileInputFormat`

valueClass

`Class` of the value associated with `SequenceFileInputFormat`

minPartitions

suggested minimum number of partitions for the resulting RDD

returns

RDD of tuples of key and corresponding value

Note

Because Hadoop's RecordReader class re-uses the same Writable object for each record, directly caching the returned RDD or directly passing it to an aggregation or shuffle operation will create many references to the same object. If you plan to directly cache, sort, or aggregate Hadoop writable objects, you should first copy them using a `map` function.
  135. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#setCallSite\(shortCallSite:String\):Unit "Permalink") def setCallSite(shortCallSite: String): Unit
Set the thread-local property for overriding the call sites of actions and RDDs.
  136. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#setCheckpointDir\(directory:String\):Unit "Permalink") def setCheckpointDir(directory: String): Unit
Set the directory under which RDDs are going to be checkpointed.
Set the directory under which RDDs are going to be checkpointed.

directory

path to the directory where checkpoint files will be stored (must be HDFS path if running in cluster)
  137. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#setInterruptOnCancel\(interruptOnCancel:Boolean\):Unit "Permalink") def setInterruptOnCancel(interruptOnCancel: Boolean): Unit
Set the behavior of job cancellation from jobs started in this thread.
Set the behavior of job cancellation from jobs started in this thread.

interruptOnCancel

If true, then job cancellation will result in `Thread.interrupt()` being called on the job's executor threads. This is useful to help ensure that the tasks are actually stopped in a timely manner, but is off by default due to HDFS-1208, where HDFS may respond to Thread.interrupt() by marking nodes as dead.

Since

3.5.0
  138. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#setJobDescription\(value:String\):Unit "Permalink") def setJobDescription(value: String): Unit
Set a human readable description of the current job.
  139. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#setJobGroup\(groupId:String,description:String,interruptOnCancel:Boolean\):Unit "Permalink") def setJobGroup(groupId: String, description: String, interruptOnCancel: Boolean = false): Unit
Assigns a group ID to all the jobs started by this thread until the group ID is set to a different value or cleared.
Assigns a group ID to all the jobs started by this thread until the group ID is set to a different value or cleared.
Often, a unit of execution in an application consists of multiple Spark actions or jobs. Application programmers can use this method to group all those jobs together and give a group description. Once set, the Spark web UI will associate such jobs with this group.
The application can also use `org.apache.spark.SparkContext.cancelJobGroup` to cancel all running jobs in this group. For example,

```
// In the main thread:
sc.setJobGroup("some_job_to_cancel", "some job description")
sc.parallelize(1 to 10000, 2).map { i => Thread.sleep(10); i }.count()

// In a separate thread:
sc.cancelJobGroup("some_job_to_cancel")
```

interruptOnCancel

If true, then job cancellation will result in `Thread.interrupt()` being called on the job's executor threads. This is useful to help ensure that the tasks are actually stopped in a timely manner, but is off by default due to HDFS-1208, where HDFS may respond to Thread.interrupt() by marking nodes as dead.
  140. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#setLocalProperty\(key:String,value:String\):Unit "Permalink") def setLocalProperty(key: String, value: String): Unit
Set a local property that affects jobs submitted from this thread, such as the Spark fair scheduler pool.
Set a local property that affects jobs submitted from this thread, such as the Spark fair scheduler pool. User-defined properties may also be set here. These properties are propagated through to worker tasks and can be accessed there via [org.apache.spark.TaskContext#getLocalProperty](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskContext.html#getLocalProperty\(key:String\):String).
These properties are inherited by child threads spawned from this thread. This may have unexpected consequences when working with thread pools. The standard java implementation of thread pools have worker threads spawn other worker threads. As a result, local properties may propagate unpredictably.
To remove/unset property simply set `value` to null e.g. sc.setLocalProperty("key", null)
  141. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#setLogLevel\(logLevel:String\):Unit "Permalink") def setLogLevel(logLevel: String): Unit
Control our logLevel.
Control our logLevel. This overrides any user-defined log settings.

logLevel

The desired log level as a string. Valid log levels include: ALL, DEBUG, ERROR, FATAL, INFO, OFF, TRACE, WARN
  142. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#sparkUser:String "Permalink") val sparkUser: String
  143. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#startTime:Long "Permalink") val startTime: Long
  144. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#statusTracker:org.apache.spark.SparkStatusTracker "Permalink") def statusTracker: [SparkStatusTracker](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkStatusTracker.html "org.apache.spark.SparkStatusTracker")
  145. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#stop\(exitCode:Int\):Unit "Permalink") def stop(exitCode: Int): Unit
Shut down the SparkContext with exit code that will passed to scheduler backend.
Shut down the SparkContext with exit code that will passed to scheduler backend. In client mode, client side may call `SparkContext.stop()` to clean up but exit with code not equal to 0. This behavior cause resource scheduler such as `ApplicationMaster` exit with success status but client side exited with failed status. Spark can call this method to stop SparkContext and pass client side correct exit code to scheduler backend. Then scheduler backend should send the exit code to corresponding resource scheduler to keep consistent.

exitCode

Specified exit code that will passed to scheduler backend in client mode.
  146. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#stop\(\):Unit "Permalink") def stop(): Unit
Shut down the SparkContext.
  147. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#submitJob\[T,U,R\]\(rdd:org.apache.spark.rdd.RDD\[T\],processPartition:Iterator\[T\]=>U,partitions:Seq\[Int\],resultHandler:\(Int,U\)=>Unit,resultFunc:=>R\):org.apache.spark.SimpleFutureAction\[R\] "Permalink") def submitJob[T, U, R](rdd: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[T], processPartition: (Iterator[T]) => U, partitions: Seq[Int], resultHandler: (Int, U) => Unit, resultFunc: => R): [SimpleFutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SimpleFutureAction.html "org.apache.spark.SimpleFutureAction")[R]
Submit a job for execution and return a FutureJob holding the result.
Submit a job for execution and return a FutureJob holding the result.

rdd

target RDD to run tasks on

processPartition

a function to run on each partition of the RDD

partitions

set of partitions to run on; some jobs may not want to compute on all partitions of the target RDD, e.g. for operations like `first()`

resultHandler

callback to pass each result to

resultFunc

function to be executed when the result is ready
  148. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0

Definition Classes
    AnyRef
  149. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#textFile\(path:String,minPartitions:Int\):org.apache.spark.rdd.RDD\[String\] "Permalink") def textFile(path: String, minPartitions: Int = [defaultMinPartitions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#defaultMinPartitions:Int)): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[String]
Read a text file from HDFS, a local file system (available on all nodes), or any Hadoop-supported file system URI, and return it as an RDD of Strings.
Read a text file from HDFS, a local file system (available on all nodes), or any Hadoop-supported file system URI, and return it as an RDD of Strings. The text files must be encoded as UTF-8.

path

path to the text file on a supported file system

minPartitions

suggested minimum number of partitions for the resulting RDD

returns

RDD of lines of the text file
  150. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#toString\(\):String "Permalink") def toString(): [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String")

Definition Classes
    AnyRef → Any
  151. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#uiWebUrl:Option\[String\] "Permalink") def uiWebUrl: Option[String]
  152. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#union\[T\]\(first:org.apache.spark.rdd.RDD\[T\],rest:org.apache.spark.rdd.RDD\[T\]*\)\(implicitevidence$7:scala.reflect.ClassTag\[T\]\):org.apache.spark.rdd.RDD\[T\] "Permalink") def union[T](first: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[T], rest: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[T]*)(implicit arg0: ClassTag[T]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[T]
Build the union of a list of RDDs passed as variable-length arguments.
  153. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#union\[T\]\(rdds:Seq\[org.apache.spark.rdd.RDD\[T\]\]\)\(implicitevidence$6:scala.reflect.ClassTag\[T\]\):org.apache.spark.rdd.RDD\[T\] "Permalink") def union[T](rdds: Seq[[RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[T]])(implicit arg0: ClassTag[T]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[T]
Build the union of a list of RDDs.
  154. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#version:String "Permalink") def version: String
The version of Spark on which this application is running.
  155. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])
  156. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  157. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#wait\(\):Unit "Permalink") final  def wait(): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])
  158. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#wholeTextFiles\(path:String,minPartitions:Int\):org.apache.spark.rdd.RDD\[\(String,String\)\] "Permalink") def wholeTextFiles(path: String, minPartitions: Int = [defaultMinPartitions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#defaultMinPartitions:Int)): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(String, String)]
Read a directory of text files from HDFS, a local file system (available on all nodes), or any Hadoop-supported file system URI.
Read a directory of text files from HDFS, a local file system (available on all nodes), or any Hadoop-supported file system URI. Each file is read as a single record and returned in a key-value pair, where the key is the path of each file, the value is the content of each file. The text files must be encoded as UTF-8.
For example, if you have the following files:

```
hdfs://a-hdfs-path/part-00000
hdfs://a-hdfs-path/part-00001
...
hdfs://a-hdfs-path/part-nnnnn
```

Do `val rdd = sparkContext.wholeTextFile("hdfs://a-hdfs-path")`,
then `rdd` contains

```
(a-hdfs-path/part-00000, its content)
(a-hdfs-path/part-00001, its content)
...
(a-hdfs-path/part-nnnnn, its content)
```

path

Directory to the input data files, the path can be comma separated paths as the list of inputs.

minPartitions

A suggestion value of the minimal splitting number for input data.

returns

RDD representing tuples of file path and the corresponding file content

Note

Small files are preferred, large file is also allowable, but may cause bad performance.
,
On some filesystems, `.../path/*` can be a more efficient way to read all files in a directory rather than `.../path/` or `.../path`
,
Partitioning is determined by data locality. This may result in too few partitions by default.
  159. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#withLogContext\(context:java.util.Map\[String,String\]\)\(body:=>Unit\):Unit "Permalink") def withLogContext(context: [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#java.util.Map "java.util.Map")[String, String])(body: => Unit): Unit

Attributes
    protected

Definition Classes
    Logging
  160. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#finalize\(\):Unit "Permalink") def finalize(): Unit

Attributes
    protected[lang]

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.Throwable]) @Deprecated

Deprecated

_(Since version 9)_
