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
# ContextAwareIterator[ __](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html "Permalink")
####  class ContextAwareIterator[+T] extends Iterator[T]
Developer API
A TaskContext aware iterator.
As the Python evaluation consumes the parent iterator in a separate thread, it could consume more data from the parent even after the task ends and the parent is closed. If an off-heap access exists in the parent iterator, it could cause segmentation fault which crashes the executor. Thus, we should use [ContextAwareIterator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html "org.apache.spark.ContextAwareIterator") to stop consuming after the task ends.  

Annotations
     @DeveloperApi() @deprecated 

Deprecated
    
_(Since version 4.0.0)_ Only usage for Python evaluation is now extinct 

Source
    [ContextAwareIterator.scala](https://github.com/apache/spark/tree/v4.1.2/core/src/main/scala/org/apache/spark/ContextAwareIterator.scala) 

Since
    
3.1.0
Linear Supertypes
Iterator[T], IterableOnceOps[T, Iterator, Iterator[T]], IterableOnce[T], AnyRef, Any
__ __
Ordering
  1. Alphabetic
  2. By Inheritance


Inherited  

  1. ContextAwareIterator
  2. Iterator
  3. IterableOnceOps
  4. IterableOnce
  5. AnyRef
  6. Any


  1. Hide All
  2. Show All


Visibility
  1. Public
  2. Protected


### Instance Constructors
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#<init>\(context:org.apache.spark.TaskContext,delegate:Iterator\[T\]\):org.apache.spark.ContextAwareIterator\[T\] "Permalink") new ContextAwareIterator(context: [TaskContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskContext.html "org.apache.spark.TaskContext"), delegate: Iterator[T]) 

Deprecated
    
since 4.0.0 as its only usage for Python evaluation is now extinct


### Type Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#GroupedIterator\[B>:A\]extendsAbstractIterator\[Seq\[B\]\] "Permalink") class GroupedIterator[B >: A] extends AbstractIterator[Seq[B]] 

Definition Classes
    Iterator


### Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html###:Int "Permalink") final  def ##: Int 

Definition Classes
    AnyRef → Any
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#++\[B>:A\]\(xs:=>scala.collection.IterableOnce\[B\]\):Iterator\[B\] "Permalink") final  def ++[B >: T](xs: => IterableOnce[B]): Iterator[B] 

Definition Classes
    Iterator 

Annotations
     @inline()
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#addString\(b:StringBuilder\):b.type "Permalink") final  def addString(b: StringBuilder): b.type 

Definition Classes
    IterableOnceOps 

Annotations
     @inline()
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#addString\(b:StringBuilder,sep:String\):b.type "Permalink") final  def addString(b: StringBuilder, sep: String): b.type 

Definition Classes
    IterableOnceOps 

Annotations
     @inline()
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#addString\(b:StringBuilder,start:String,sep:String,end:String\):b.type "Permalink") def addString(b: StringBuilder, start: String, sep: String, end: String): b.type 

Definition Classes
    IterableOnceOps
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0 

Definition Classes
    Any
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#buffered:scala.collection.BufferedIterator\[A\] "Permalink") def buffered: BufferedIterator[T] 

Definition Classes
    Iterator
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#clone\(\):Object "Permalink") def clone(): AnyRef 

Attributes
    protected[lang]  

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#collect\[B\]\(pf:PartialFunction\[A,B\]\):Iterator\[B\] "Permalink") def collect[B](pf: PartialFunction[T, B]): Iterator[B] 

Definition Classes
    Iterator → IterableOnceOps
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#collectFirst\[B\]\(pf:PartialFunction\[A,B\]\):Option\[B\] "Permalink") def collectFirst[B](pf: PartialFunction[T, B]): Option[B] 

Definition Classes
    IterableOnceOps
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#concat\[B>:A\]\(xs:=>scala.collection.IterableOnce\[B\]\):Iterator\[B\] "Permalink") def concat[B >: T](xs: => IterableOnce[B]): Iterator[B] 

Definition Classes
    Iterator
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#contains\(elem:Any\):Boolean "Permalink") def contains(elem: Any): Boolean 

Definition Classes
    Iterator
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#context:org.apache.spark.TaskContext "Permalink") val context: [TaskContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskContext.html "org.apache.spark.TaskContext")
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#copyToArray\[B>:A\]\(dest:Array\[B\],start:Int,n:Int\):Int "Permalink") def copyToArray[B >: T](dest: Array[B], start: Int, n: Int): Int 

Definition Classes
    IterableOnceOps
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#copyToArray\[B>:A\]\(dest:Array\[B\],start:Int\):Int "Permalink") def copyToArray[B >: T](dest: Array[B], start: Int): Int 

Definition Classes
    IterableOnceOps 

Annotations
     @deprecatedOverriding()
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#copyToArray\[B>:A\]\(dest:Array\[B\]\):Int "Permalink") def copyToArray[B >: T](dest: Array[B]): Int 

Definition Classes
    IterableOnceOps 

Annotations
     @deprecatedOverriding()
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#corresponds\[B\]\(that:scala.collection.IterableOnce\[B\]\)\(p:\(A,B\)=>Boolean\):Boolean "Permalink") def corresponds[B](that: IterableOnce[B])(p: (T, B) => Boolean): Boolean 

Definition Classes
    IterableOnceOps
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#count\(p:A=>Boolean\):Int "Permalink") def count(p: (T) => Boolean): Int 

Definition Classes
    IterableOnceOps
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#delegate:Iterator\[T\] "Permalink") val delegate: Iterator[T]
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#distinct:Iterator\[A\] "Permalink") def distinct: Iterator[T] 

Definition Classes
    Iterator
  23. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#distinctBy\[B\]\(f:A=>B\):Iterator\[A\] "Permalink") def distinctBy[B](f: (T) => B): Iterator[T] 

Definition Classes
    Iterator
  24. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#drop\(n:Int\):Iterator\[A\] "Permalink") def drop(n: Int): Iterator[T] 

Definition Classes
    Iterator → IterableOnceOps
  25. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#dropWhile\(p:A=>Boolean\):Iterator\[A\] "Permalink") def dropWhile(p: (T) => Boolean): Iterator[T] 

Definition Classes
    Iterator → IterableOnceOps
  26. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#duplicate:\(Iterator\[A\],Iterator\[A\]\) "Permalink") def duplicate: (Iterator[T], Iterator[T]) 

Definition Classes
    Iterator
  27. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  28. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#equals\(x$1:Object\):Boolean "Permalink") def equals(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef → Any
  29. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#exists\(p:A=>Boolean\):Boolean "Permalink") def exists(p: (T) => Boolean): Boolean 

Definition Classes
    IterableOnceOps
  30. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#filter\(p:A=>Boolean\):Iterator\[A\] "Permalink") def filter(p: (T) => Boolean): Iterator[T] 

Definition Classes
    Iterator → IterableOnceOps
  31. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#filterNot\(p:A=>Boolean\):Iterator\[A\] "Permalink") def filterNot(p: (T) => Boolean): Iterator[T] 

Definition Classes
    Iterator → IterableOnceOps
  32. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#find\(p:A=>Boolean\):Option\[A\] "Permalink") def find(p: (T) => Boolean): Option[T] 

Definition Classes
    IterableOnceOps
  33. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#flatMap\[B\]\(f:A=>scala.collection.IterableOnce\[B\]\):Iterator\[B\] "Permalink") def flatMap[B](f: (T) => IterableOnce[B]): Iterator[B] 

Definition Classes
    Iterator → IterableOnceOps
  34. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#flatten\[B\]\(implicitev:A=>scala.collection.IterableOnce\[B\]\):Iterator\[B\] "Permalink") def flatten[B](implicit ev: (T) => IterableOnce[B]): Iterator[B] 

Definition Classes
    Iterator → IterableOnceOps
  35. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#fold\[A1>:A\]\(z:A1\)\(op:\(A1,A1\)=>A1\):A1 "Permalink") def fold[A1 >: T](z: A1)(op: (A1, A1) => A1): A1 

Definition Classes
    IterableOnceOps
  36. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#foldLeft\[B\]\(z:B\)\(op:\(B,A\)=>B\):B "Permalink") def foldLeft[B](z: B)(op: (B, T) => B): B 

Definition Classes
    IterableOnceOps
  37. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#foldRight\[B\]\(z:B\)\(op:\(A,B\)=>B\):B "Permalink") def foldRight[B](z: B)(op: (T, B) => B): B 

Definition Classes
    IterableOnceOps
  38. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#forall\(p:A=>Boolean\):Boolean "Permalink") def forall(p: (T) => Boolean): Boolean 

Definition Classes
    IterableOnceOps
  39. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#foreach\[U\]\(f:A=>U\):Unit "Permalink") def foreach[U](f: (T) => U): Unit 

Definition Classes
    IterableOnceOps
  40. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef] 

Definition Classes
    AnyRef → Any 

Annotations
     @IntrinsicCandidate() @native()
  41. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#grouped\[B>:A\]\(size:Int\):Iterator.this.GroupedIterator\[B\] "Permalink") def grouped[B >: T](size: Int): [GroupedIterator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#GroupedIterator\[B>:A\]extendsAbstractIterator\[Seq\[B\]\])[B] 

Definition Classes
    Iterator
  42. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#hasNext:Boolean "Permalink") def hasNext: Boolean 

Definition Classes
     [ContextAwareIterator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html "org.apache.spark.ContextAwareIterator") → Iterator
  43. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#hashCode\(\):Int "Permalink") def hashCode(): Int 

Definition Classes
    AnyRef → Any 

Annotations
     @IntrinsicCandidate() @native()
  44. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#indexOf\[B>:A\]\(elem:B,from:Int\):Int "Permalink") def indexOf[B >: T](elem: B, from: Int): Int 

Definition Classes
    Iterator
  45. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#indexOf\[B>:A\]\(elem:B\):Int "Permalink") def indexOf[B >: T](elem: B): Int 

Definition Classes
    Iterator
  46. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#indexWhere\(p:A=>Boolean,from:Int\):Int "Permalink") def indexWhere(p: (T) => Boolean, from: Int): Int 

Definition Classes
    Iterator
  47. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#isEmpty:Boolean "Permalink") def isEmpty: Boolean 

Definition Classes
    Iterator → IterableOnceOps 

Annotations
     @deprecatedOverriding()
  48. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean 

Definition Classes
    Any
  49. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#isTraversableAgain:Boolean "Permalink") def isTraversableAgain: Boolean 

Definition Classes
    IterableOnceOps
  50. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#iterator:Iterator\[A\] "Permalink") final  def iterator: Iterator[T] 

Definition Classes
    Iterator → IterableOnce 

Annotations
     @inline()
  51. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#knownSize:Int "Permalink") def knownSize: Int 

Definition Classes
    IterableOnce
  52. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#length:Int "Permalink") final  def length: Int 

Definition Classes
    Iterator 

Annotations
     @inline()
  53. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#map\[B\]\(f:A=>B\):Iterator\[B\] "Permalink") def map[B](f: (T) => B): Iterator[B] 

Definition Classes
    Iterator → IterableOnceOps
  54. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#max\[B>:A\]\(implicitord:scala.math.Ordering\[B\]\):A "Permalink") def max[B >: T](implicit ord: Ordering[B]): T 

Definition Classes
    IterableOnceOps
  55. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#maxBy\[B\]\(f:A=>B\)\(implicitord:scala.math.Ordering\[B\]\):A "Permalink") def maxBy[B](f: (T) => B)(implicit ord: Ordering[B]): T 

Definition Classes
    IterableOnceOps
  56. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#maxByOption\[B\]\(f:A=>B\)\(implicitord:scala.math.Ordering\[B\]\):Option\[A\] "Permalink") def maxByOption[B](f: (T) => B)(implicit ord: Ordering[B]): Option[T] 

Definition Classes
    IterableOnceOps
  57. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#maxOption\[B>:A\]\(implicitord:scala.math.Ordering\[B\]\):Option\[A\] "Permalink") def maxOption[B >: T](implicit ord: Ordering[B]): Option[T] 

Definition Classes
    IterableOnceOps
  58. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#min\[B>:A\]\(implicitord:scala.math.Ordering\[B\]\):A "Permalink") def min[B >: T](implicit ord: Ordering[B]): T 

Definition Classes
    IterableOnceOps
  59. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#minBy\[B\]\(f:A=>B\)\(implicitord:scala.math.Ordering\[B\]\):A "Permalink") def minBy[B](f: (T) => B)(implicit ord: Ordering[B]): T 

Definition Classes
    IterableOnceOps
  60. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#minByOption\[B\]\(f:A=>B\)\(implicitord:scala.math.Ordering\[B\]\):Option\[A\] "Permalink") def minByOption[B](f: (T) => B)(implicit ord: Ordering[B]): Option[T] 

Definition Classes
    IterableOnceOps
  61. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#minOption\[B>:A\]\(implicitord:scala.math.Ordering\[B\]\):Option\[A\] "Permalink") def minOption[B >: T](implicit ord: Ordering[B]): Option[T] 

Definition Classes
    IterableOnceOps
  62. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#mkString:String "Permalink") final  def mkString: String 

Definition Classes
    IterableOnceOps 

Annotations
     @inline()
  63. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#mkString\(sep:String\):String "Permalink") final  def mkString(sep: String): String 

Definition Classes
    IterableOnceOps 

Annotations
     @inline()
  64. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#mkString\(start:String,sep:String,end:String\):String "Permalink") final  def mkString(start: String, sep: String, end: String): String 

Definition Classes
    IterableOnceOps
  65. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  66. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#next\(\):T "Permalink") def next(): T 

Definition Classes
     [ContextAwareIterator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html "org.apache.spark.ContextAwareIterator") → Iterator
  67. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#nextOption\(\):Option\[A\] "Permalink") def nextOption(): Option[T] 

Definition Classes
    Iterator
  68. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#nonEmpty:Boolean "Permalink") def nonEmpty: Boolean 

Definition Classes
    IterableOnceOps 

Annotations
     @deprecatedOverriding()
  69. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#notify\(\):Unit "Permalink") final  def notify(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  70. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  71. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#padTo\[B>:A\]\(len:Int,elem:B\):Iterator\[B\] "Permalink") def padTo[B >: T](len: Int, elem: B): Iterator[B] 

Definition Classes
    Iterator
  72. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#partition\(p:A=>Boolean\):\(Iterator\[A\],Iterator\[A\]\) "Permalink") def partition(p: (T) => Boolean): (Iterator[T], Iterator[T]) 

Definition Classes
    Iterator
  73. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#patch\[B>:A\]\(from:Int,patchElems:Iterator\[B\],replaced:Int\):Iterator\[B\] "Permalink") def patch[B >: T](from: Int, patchElems: Iterator[B], replaced: Int): Iterator[B] 

Definition Classes
    Iterator
  74. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#product\[B>:A\]\(implicitnum:scala.math.Numeric\[B\]\):B "Permalink") def product[B >: T](implicit num: Numeric[B]): B 

Definition Classes
    IterableOnceOps
  75. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#reduce\[B>:A\]\(op:\(B,B\)=>B\):B "Permalink") def reduce[B >: T](op: (B, B) => B): B 

Definition Classes
    IterableOnceOps
  76. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#reduceLeft\[B>:A\]\(op:\(B,A\)=>B\):B "Permalink") def reduceLeft[B >: T](op: (B, T) => B): B 

Definition Classes
    IterableOnceOps
  77. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#reduceLeftOption\[B>:A\]\(op:\(B,A\)=>B\):Option\[B\] "Permalink") def reduceLeftOption[B >: T](op: (B, T) => B): Option[B] 

Definition Classes
    IterableOnceOps
  78. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#reduceOption\[B>:A\]\(op:\(B,B\)=>B\):Option\[B\] "Permalink") def reduceOption[B >: T](op: (B, B) => B): Option[B] 

Definition Classes
    IterableOnceOps
  79. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#reduceRight\[B>:A\]\(op:\(A,B\)=>B\):B "Permalink") def reduceRight[B >: T](op: (T, B) => B): B 

Definition Classes
    IterableOnceOps
  80. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#reduceRightOption\[B>:A\]\(op:\(A,B\)=>B\):Option\[B\] "Permalink") def reduceRightOption[B >: T](op: (T, B) => B): Option[B] 

Definition Classes
    IterableOnceOps
  81. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#reversed:Iterable\[A\] "Permalink") def reversed: Iterable[T] 

Attributes
    protected  

Definition Classes
    IterableOnceOps
  82. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#sameElements\[B>:A\]\(that:scala.collection.IterableOnce\[B\]\):Boolean "Permalink") def sameElements[B >: T](that: IterableOnce[B]): Boolean 

Definition Classes
    Iterator
  83. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#scanLeft\[B\]\(z:B\)\(op:\(B,A\)=>B\):Iterator\[B\] "Permalink") def scanLeft[B](z: B)(op: (B, T) => B): Iterator[B] 

Definition Classes
    Iterator → IterableOnceOps
  84. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#size:Int "Permalink") def size: Int 

Definition Classes
    IterableOnceOps
  85. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#slice\(from:Int,until:Int\):Iterator\[A\] "Permalink") def slice(from: Int, until: Int): Iterator[T] 

Definition Classes
    Iterator → IterableOnceOps
  86. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#sliceIterator\(from:Int,until:Int\):Iterator\[A\] "Permalink") def sliceIterator(from: Int, until: Int): Iterator[T] 

Attributes
    protected  

Definition Classes
    Iterator
  87. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#sliding\[B>:A\]\(size:Int,step:Int\):Iterator.this.GroupedIterator\[B\] "Permalink") def sliding[B >: T](size: Int, step: Int): [GroupedIterator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#GroupedIterator\[B>:A\]extendsAbstractIterator\[Seq\[B\]\])[B] 

Definition Classes
    Iterator
  88. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#span\(p:A=>Boolean\):\(Iterator\[A\],Iterator\[A\]\) "Permalink") def span(p: (T) => Boolean): (Iterator[T], Iterator[T]) 

Definition Classes
    Iterator → IterableOnceOps
  89. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#splitAt\(n:Int\):\(C,C\) "Permalink") def splitAt(n: Int): (Iterator[T], Iterator[T]) 

Definition Classes
    IterableOnceOps
  90. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#stepper\[S<:scala.collection.Stepper\[_\]\]\(implicitshape:scala.collection.StepperShape\[A,S\]\):S "Permalink") def stepper[S <: Stepper[_]](implicit shape: StepperShape[T, S]): S 

Definition Classes
    IterableOnce
  91. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#sum\[B>:A\]\(implicitnum:scala.math.Numeric\[B\]\):B "Permalink") def sum[B >: T](implicit num: Numeric[B]): B 

Definition Classes
    IterableOnceOps
  92. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0 

Definition Classes
    AnyRef
  93. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#take\(n:Int\):Iterator\[A\] "Permalink") def take(n: Int): Iterator[T] 

Definition Classes
    Iterator → IterableOnceOps
  94. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#takeWhile\(p:A=>Boolean\):Iterator\[A\] "Permalink") def takeWhile(p: (T) => Boolean): Iterator[T] 

Definition Classes
    Iterator → IterableOnceOps
  95. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#tapEach\[U\]\(f:A=>U\):Iterator\[A\] "Permalink") def tapEach[U](f: (T) => U): Iterator[T] 

Definition Classes
    Iterator → IterableOnceOps
  96. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#to\[C1\]\(factory:scala.collection.Factory\[A,C1\]\):C1 "Permalink") def to[C1](factory: Factory[T, C1]): C1 

Definition Classes
    IterableOnceOps
  97. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#toArray\[B>:A\]\(implicitevidence$2:scala.reflect.ClassTag\[B\]\):Array\[B\] "Permalink") def toArray[B >: T](implicit arg0: ClassTag[B]): Array[B] 

Definition Classes
    IterableOnceOps
  98. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#toBuffer\[B>:A\]:scala.collection.mutable.Buffer\[B\] "Permalink") final  def toBuffer[B >: T]: Buffer[B] 

Definition Classes
    IterableOnceOps 

Annotations
     @inline()
  99. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#toIndexedSeq:IndexedSeq\[A\] "Permalink") def toIndexedSeq: IndexedSeq[T] 

Definition Classes
    IterableOnceOps
  100. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#toList:List\[A\] "Permalink") def toList: List[T] 

Definition Classes
    IterableOnceOps
  101. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#toMap\[K,V\]\(implicitev:A<:<\(K,V\)\):scala.collection.immutable.Map\[K,V\] "Permalink") def toMap[K, V](implicit ev: <:<[T, (K, V)]): Map[K, V] 

Definition Classes
    IterableOnceOps
  102. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#toSeq:Seq\[A\] "Permalink") def toSeq: Seq[T] 

Definition Classes
    IterableOnceOps
  103. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#toSet\[B>:A\]:scala.collection.immutable.Set\[B\] "Permalink") def toSet[B >: T]: Set[B] 

Definition Classes
    IterableOnceOps
  104. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#toString\(\):String "Permalink") def toString(): [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String") 

Definition Classes
    Iterator → AnyRef → Any
  105. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#toVector:scala.collection.immutable.Vector\[A\] "Permalink") def toVector: Vector[T] 

Definition Classes
    IterableOnceOps
  106. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  107. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  108. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#wait\(\):Unit "Permalink") final  def wait(): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  109. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#withFilter\(p:A=>Boolean\):Iterator\[A\] "Permalink") def withFilter(p: (T) => Boolean): Iterator[T] 

Definition Classes
    Iterator
  110. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#zip\[B\]\(that:scala.collection.IterableOnce\[B\]\):Iterator\[\(A,B\)\] "Permalink") def zip[B](that: IterableOnce[B]): Iterator[(T, B)] 

Definition Classes
    Iterator
  111. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#zipAll\[A1>:A,B\]\(that:scala.collection.IterableOnce\[B\],thisElem:A1,thatElem:B\):Iterator\[\(A1,B\)\] "Permalink") def zipAll[A1 >: T, B](that: IterableOnce[B], thisElem: A1, thatElem: B): Iterator[(A1, B)] 

Definition Classes
    Iterator
  112. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#zipWithIndex:Iterator\[\(A,Int\)\] "Permalink") def zipWithIndex: Iterator[(T, Int)] 

Definition Classes
    Iterator → IterableOnceOps


### Deprecated Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#/:\[B\]\(z:B\)\(op:\(B,A\)=>B\):B "Permalink") final  def /:[B](z: B)(op: (B, T) => B): B 

Definition Classes
    IterableOnceOps 

Annotations
     @deprecated @inline() 

Deprecated
    
_(Since version 2.13.0)_ Use foldLeft instead of /:
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#:\\\[B\]\(z:B\)\(op:\(A,B\)=>B\):B "Permalink") final  def :\[B](z: B)(op: (T, B) => B): B 

Definition Classes
    IterableOnceOps 

Annotations
     @deprecated @inline() 

Deprecated
    
_(Since version 2.13.0)_ Use foldRight instead of :\
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#aggregate\[B\]\(z:=>B\)\(seqop:\(B,A\)=>B,combop:\(B,B\)=>B\):B "Permalink") def aggregate[B](z: => B)(seqop: (B, T) => B, combop: (B, B) => B): B 

Definition Classes
    IterableOnceOps 

Annotations
     @deprecated 

Deprecated
    
_(Since version 2.13.0)_ For sequential collections, prefer `foldLeft(z)(seqop)`. For parallel collections, use `ParIterableLike#aggregate`.
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#copyToBuffer\[B>:A\]\(dest:scala.collection.mutable.Buffer\[B\]\):Unit "Permalink") final  def copyToBuffer[B >: T](dest: Buffer[B]): Unit 

Definition Classes
    IterableOnceOps 

Annotations
     @deprecated @inline() 

Deprecated
    
_(Since version 2.13.0)_ Use `dest ++= coll` instead
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#finalize\(\):Unit "Permalink") def finalize(): Unit 

Attributes
    protected[lang]  

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.Throwable]) @Deprecated 

Deprecated
    
_(Since version 9)_
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#hasDefiniteSize:Boolean "Permalink") final  def hasDefiniteSize: Boolean 

Definition Classes
    Iterator → IterableOnceOps 

Annotations
     @deprecated @inline() 

Deprecated
    
_(Since version 2.13.0)_ hasDefiniteSize on Iterator is the same as isEmpty
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#scanRight\[B\]\(z:B\)\(op:\(A,B\)=>B\):Iterator\[B\] "Permalink") def scanRight[B](z: B)(op: (T, B) => B): Iterator[B] 

Definition Classes
    Iterator 

Annotations
     @deprecated 

Deprecated
    
_(Since version 2.13.0)_ Call scanRight on an Iterable instead.
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#seq:Iterator.this.type "Permalink") def seq: [ContextAwareIterator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html "org.apache.spark.ContextAwareIterator").this.type 

Definition Classes
    Iterator 

Annotations
     @deprecated 

Deprecated
    
_(Since version 2.13.0)_ Iterator.seq always returns the iterator itself
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#toIterator:Iterator\[A\] "Permalink") final  def toIterator: Iterator[T] 

Definition Classes
    IterableOnceOps 

Annotations
     @deprecated @inline() 

Deprecated
    
_(Since version 2.13.0)_ Use .iterator instead of .toIterator
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#toStream:scala.collection.immutable.Stream\[A\] "Permalink") final  def toStream: Stream[T] 

Definition Classes
    IterableOnceOps 

Annotations
     @deprecated @inline() 

Deprecated
    
_(Since version 2.13.0)_ Use .to(LazyList) instead of .toStream


### Inherited from Iterator[T]
### Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#++\[B>:A\]\(xs:=>scala.collection.IterableOnce\[B\]\):Iterator\[B\] "Permalink") final  def ++[B >: T](xs: => IterableOnce[B]): Iterator[B] 

Definition Classes
    Iterator 

Annotations
     @inline()
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#buffered:scala.collection.BufferedIterator\[A\] "Permalink") def buffered: BufferedIterator[T] 

Definition Classes
    Iterator
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#collect\[B\]\(pf:PartialFunction\[A,B\]\):Iterator\[B\] "Permalink") def collect[B](pf: PartialFunction[T, B]): Iterator[B] 

Definition Classes
    Iterator → IterableOnceOps
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#concat\[B>:A\]\(xs:=>scala.collection.IterableOnce\[B\]\):Iterator\[B\] "Permalink") def concat[B >: T](xs: => IterableOnce[B]): Iterator[B] 

Definition Classes
    Iterator
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#contains\(elem:Any\):Boolean "Permalink") def contains(elem: Any): Boolean 

Definition Classes
    Iterator
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#distinct:Iterator\[A\] "Permalink") def distinct: Iterator[T] 

Definition Classes
    Iterator
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#distinctBy\[B\]\(f:A=>B\):Iterator\[A\] "Permalink") def distinctBy[B](f: (T) => B): Iterator[T] 

Definition Classes
    Iterator
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#drop\(n:Int\):Iterator\[A\] "Permalink") def drop(n: Int): Iterator[T] 

Definition Classes
    Iterator → IterableOnceOps
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#dropWhile\(p:A=>Boolean\):Iterator\[A\] "Permalink") def dropWhile(p: (T) => Boolean): Iterator[T] 

Definition Classes
    Iterator → IterableOnceOps
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#duplicate:\(Iterator\[A\],Iterator\[A\]\) "Permalink") def duplicate: (Iterator[T], Iterator[T]) 

Definition Classes
    Iterator
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#filter\(p:A=>Boolean\):Iterator\[A\] "Permalink") def filter(p: (T) => Boolean): Iterator[T] 

Definition Classes
    Iterator → IterableOnceOps
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#filterNot\(p:A=>Boolean\):Iterator\[A\] "Permalink") def filterNot(p: (T) => Boolean): Iterator[T] 

Definition Classes
    Iterator → IterableOnceOps
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#flatMap\[B\]\(f:A=>scala.collection.IterableOnce\[B\]\):Iterator\[B\] "Permalink") def flatMap[B](f: (T) => IterableOnce[B]): Iterator[B] 

Definition Classes
    Iterator → IterableOnceOps
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#flatten\[B\]\(implicitev:A=>scala.collection.IterableOnce\[B\]\):Iterator\[B\] "Permalink") def flatten[B](implicit ev: (T) => IterableOnce[B]): Iterator[B] 

Definition Classes
    Iterator → IterableOnceOps
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#grouped\[B>:A\]\(size:Int\):Iterator.this.GroupedIterator\[B\] "Permalink") def grouped[B >: T](size: Int): [GroupedIterator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#GroupedIterator\[B>:A\]extendsAbstractIterator\[Seq\[B\]\])[B] 

Definition Classes
    Iterator
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#indexOf\[B>:A\]\(elem:B,from:Int\):Int "Permalink") def indexOf[B >: T](elem: B, from: Int): Int 

Definition Classes
    Iterator
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#indexOf\[B>:A\]\(elem:B\):Int "Permalink") def indexOf[B >: T](elem: B): Int 

Definition Classes
    Iterator
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#indexWhere\(p:A=>Boolean,from:Int\):Int "Permalink") def indexWhere(p: (T) => Boolean, from: Int): Int 

Definition Classes
    Iterator
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#isEmpty:Boolean "Permalink") def isEmpty: Boolean 

Definition Classes
    Iterator → IterableOnceOps 

Annotations
     @deprecatedOverriding()
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#iterator:Iterator\[A\] "Permalink") final  def iterator: Iterator[T] 

Definition Classes
    Iterator → IterableOnce 

Annotations
     @inline()
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#length:Int "Permalink") final  def length: Int 

Definition Classes
    Iterator 

Annotations
     @inline()
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#map\[B\]\(f:A=>B\):Iterator\[B\] "Permalink") def map[B](f: (T) => B): Iterator[B] 

Definition Classes
    Iterator → IterableOnceOps
  23. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#nextOption\(\):Option\[A\] "Permalink") def nextOption(): Option[T] 

Definition Classes
    Iterator
  24. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#padTo\[B>:A\]\(len:Int,elem:B\):Iterator\[B\] "Permalink") def padTo[B >: T](len: Int, elem: B): Iterator[B] 

Definition Classes
    Iterator
  25. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#partition\(p:A=>Boolean\):\(Iterator\[A\],Iterator\[A\]\) "Permalink") def partition(p: (T) => Boolean): (Iterator[T], Iterator[T]) 

Definition Classes
    Iterator
  26. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#patch\[B>:A\]\(from:Int,patchElems:Iterator\[B\],replaced:Int\):Iterator\[B\] "Permalink") def patch[B >: T](from: Int, patchElems: Iterator[B], replaced: Int): Iterator[B] 

Definition Classes
    Iterator
  27. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#sameElements\[B>:A\]\(that:scala.collection.IterableOnce\[B\]\):Boolean "Permalink") def sameElements[B >: T](that: IterableOnce[B]): Boolean 

Definition Classes
    Iterator
  28. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#scanLeft\[B\]\(z:B\)\(op:\(B,A\)=>B\):Iterator\[B\] "Permalink") def scanLeft[B](z: B)(op: (B, T) => B): Iterator[B] 

Definition Classes
    Iterator → IterableOnceOps
  29. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#slice\(from:Int,until:Int\):Iterator\[A\] "Permalink") def slice(from: Int, until: Int): Iterator[T] 

Definition Classes
    Iterator → IterableOnceOps
  30. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#sliceIterator\(from:Int,until:Int\):Iterator\[A\] "Permalink") def sliceIterator(from: Int, until: Int): Iterator[T] 

Attributes
    protected  

Definition Classes
    Iterator
  31. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#sliding\[B>:A\]\(size:Int,step:Int\):Iterator.this.GroupedIterator\[B\] "Permalink") def sliding[B >: T](size: Int, step: Int): [GroupedIterator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#GroupedIterator\[B>:A\]extendsAbstractIterator\[Seq\[B\]\])[B] 

Definition Classes
    Iterator
  32. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#span\(p:A=>Boolean\):\(Iterator\[A\],Iterator\[A\]\) "Permalink") def span(p: (T) => Boolean): (Iterator[T], Iterator[T]) 

Definition Classes
    Iterator → IterableOnceOps
  33. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#take\(n:Int\):Iterator\[A\] "Permalink") def take(n: Int): Iterator[T] 

Definition Classes
    Iterator → IterableOnceOps
  34. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#takeWhile\(p:A=>Boolean\):Iterator\[A\] "Permalink") def takeWhile(p: (T) => Boolean): Iterator[T] 

Definition Classes
    Iterator → IterableOnceOps
  35. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#tapEach\[U\]\(f:A=>U\):Iterator\[A\] "Permalink") def tapEach[U](f: (T) => U): Iterator[T] 

Definition Classes
    Iterator → IterableOnceOps
  36. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#toString\(\):String "Permalink") def toString(): [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String") 

Definition Classes
    Iterator → AnyRef → Any
  37. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#withFilter\(p:A=>Boolean\):Iterator\[A\] "Permalink") def withFilter(p: (T) => Boolean): Iterator[T] 

Definition Classes
    Iterator
  38. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#zip\[B\]\(that:scala.collection.IterableOnce\[B\]\):Iterator\[\(A,B\)\] "Permalink") def zip[B](that: IterableOnce[B]): Iterator[(T, B)] 

Definition Classes
    Iterator
  39. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#zipAll\[A1>:A,B\]\(that:scala.collection.IterableOnce\[B\],thisElem:A1,thatElem:B\):Iterator\[\(A1,B\)\] "Permalink") def zipAll[A1 >: T, B](that: IterableOnce[B], thisElem: A1, thatElem: B): Iterator[(A1, B)] 

Definition Classes
    Iterator
  40. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#zipWithIndex:Iterator\[\(A,Int\)\] "Permalink") def zipWithIndex: Iterator[(T, Int)] 

Definition Classes
    Iterator → IterableOnceOps
  41. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#hasDefiniteSize:Boolean "Permalink") final  def hasDefiniteSize: Boolean 

Definition Classes
    Iterator → IterableOnceOps 

Annotations
     @deprecated @inline() 

Deprecated
    
_(Since version 2.13.0)_ hasDefiniteSize on Iterator is the same as isEmpty
  42. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#scanRight\[B\]\(z:B\)\(op:\(A,B\)=>B\):Iterator\[B\] "Permalink") def scanRight[B](z: B)(op: (T, B) => B): Iterator[B] 

Definition Classes
    Iterator 

Annotations
     @deprecated 

Deprecated
    
_(Since version 2.13.0)_ Call scanRight on an Iterable instead.
  43. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#seq:Iterator.this.type "Permalink") def seq: [ContextAwareIterator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html "org.apache.spark.ContextAwareIterator").this.type 

Definition Classes
    Iterator 

Annotations
     @deprecated 

Deprecated
    
_(Since version 2.13.0)_ Iterator.seq always returns the iterator itself


### Inherited from IterableOnceOps[T, Iterator, Iterator[T]]
### Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#addString\(b:StringBuilder\):b.type "Permalink") final  def addString(b: StringBuilder): b.type 

Definition Classes
    IterableOnceOps 

Annotations
     @inline()
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#addString\(b:StringBuilder,sep:String\):b.type "Permalink") final  def addString(b: StringBuilder, sep: String): b.type 

Definition Classes
    IterableOnceOps 

Annotations
     @inline()
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#addString\(b:StringBuilder,start:String,sep:String,end:String\):b.type "Permalink") def addString(b: StringBuilder, start: String, sep: String, end: String): b.type 

Definition Classes
    IterableOnceOps
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#collectFirst\[B\]\(pf:PartialFunction\[A,B\]\):Option\[B\] "Permalink") def collectFirst[B](pf: PartialFunction[T, B]): Option[B] 

Definition Classes
    IterableOnceOps
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#copyToArray\[B>:A\]\(dest:Array\[B\],start:Int,n:Int\):Int "Permalink") def copyToArray[B >: T](dest: Array[B], start: Int, n: Int): Int 

Definition Classes
    IterableOnceOps
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#copyToArray\[B>:A\]\(dest:Array\[B\],start:Int\):Int "Permalink") def copyToArray[B >: T](dest: Array[B], start: Int): Int 

Definition Classes
    IterableOnceOps 

Annotations
     @deprecatedOverriding()
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#copyToArray\[B>:A\]\(dest:Array\[B\]\):Int "Permalink") def copyToArray[B >: T](dest: Array[B]): Int 

Definition Classes
    IterableOnceOps 

Annotations
     @deprecatedOverriding()
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#corresponds\[B\]\(that:scala.collection.IterableOnce\[B\]\)\(p:\(A,B\)=>Boolean\):Boolean "Permalink") def corresponds[B](that: IterableOnce[B])(p: (T, B) => Boolean): Boolean 

Definition Classes
    IterableOnceOps
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#count\(p:A=>Boolean\):Int "Permalink") def count(p: (T) => Boolean): Int 

Definition Classes
    IterableOnceOps
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#exists\(p:A=>Boolean\):Boolean "Permalink") def exists(p: (T) => Boolean): Boolean 

Definition Classes
    IterableOnceOps
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#find\(p:A=>Boolean\):Option\[A\] "Permalink") def find(p: (T) => Boolean): Option[T] 

Definition Classes
    IterableOnceOps
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#fold\[A1>:A\]\(z:A1\)\(op:\(A1,A1\)=>A1\):A1 "Permalink") def fold[A1 >: T](z: A1)(op: (A1, A1) => A1): A1 

Definition Classes
    IterableOnceOps
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#foldLeft\[B\]\(z:B\)\(op:\(B,A\)=>B\):B "Permalink") def foldLeft[B](z: B)(op: (B, T) => B): B 

Definition Classes
    IterableOnceOps
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#foldRight\[B\]\(z:B\)\(op:\(A,B\)=>B\):B "Permalink") def foldRight[B](z: B)(op: (T, B) => B): B 

Definition Classes
    IterableOnceOps
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#forall\(p:A=>Boolean\):Boolean "Permalink") def forall(p: (T) => Boolean): Boolean 

Definition Classes
    IterableOnceOps
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#foreach\[U\]\(f:A=>U\):Unit "Permalink") def foreach[U](f: (T) => U): Unit 

Definition Classes
    IterableOnceOps
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#isTraversableAgain:Boolean "Permalink") def isTraversableAgain: Boolean 

Definition Classes
    IterableOnceOps
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#max\[B>:A\]\(implicitord:scala.math.Ordering\[B\]\):A "Permalink") def max[B >: T](implicit ord: Ordering[B]): T 

Definition Classes
    IterableOnceOps
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#maxBy\[B\]\(f:A=>B\)\(implicitord:scala.math.Ordering\[B\]\):A "Permalink") def maxBy[B](f: (T) => B)(implicit ord: Ordering[B]): T 

Definition Classes
    IterableOnceOps
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#maxByOption\[B\]\(f:A=>B\)\(implicitord:scala.math.Ordering\[B\]\):Option\[A\] "Permalink") def maxByOption[B](f: (T) => B)(implicit ord: Ordering[B]): Option[T] 

Definition Classes
    IterableOnceOps
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#maxOption\[B>:A\]\(implicitord:scala.math.Ordering\[B\]\):Option\[A\] "Permalink") def maxOption[B >: T](implicit ord: Ordering[B]): Option[T] 

Definition Classes
    IterableOnceOps
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#min\[B>:A\]\(implicitord:scala.math.Ordering\[B\]\):A "Permalink") def min[B >: T](implicit ord: Ordering[B]): T 

Definition Classes
    IterableOnceOps
  23. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#minBy\[B\]\(f:A=>B\)\(implicitord:scala.math.Ordering\[B\]\):A "Permalink") def minBy[B](f: (T) => B)(implicit ord: Ordering[B]): T 

Definition Classes
    IterableOnceOps
  24. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#minByOption\[B\]\(f:A=>B\)\(implicitord:scala.math.Ordering\[B\]\):Option\[A\] "Permalink") def minByOption[B](f: (T) => B)(implicit ord: Ordering[B]): Option[T] 

Definition Classes
    IterableOnceOps
  25. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#minOption\[B>:A\]\(implicitord:scala.math.Ordering\[B\]\):Option\[A\] "Permalink") def minOption[B >: T](implicit ord: Ordering[B]): Option[T] 

Definition Classes
    IterableOnceOps
  26. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#mkString:String "Permalink") final  def mkString: String 

Definition Classes
    IterableOnceOps 

Annotations
     @inline()
  27. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#mkString\(sep:String\):String "Permalink") final  def mkString(sep: String): String 

Definition Classes
    IterableOnceOps 

Annotations
     @inline()
  28. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#mkString\(start:String,sep:String,end:String\):String "Permalink") final  def mkString(start: String, sep: String, end: String): String 

Definition Classes
    IterableOnceOps
  29. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#nonEmpty:Boolean "Permalink") def nonEmpty: Boolean 

Definition Classes
    IterableOnceOps 

Annotations
     @deprecatedOverriding()
  30. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#product\[B>:A\]\(implicitnum:scala.math.Numeric\[B\]\):B "Permalink") def product[B >: T](implicit num: Numeric[B]): B 

Definition Classes
    IterableOnceOps
  31. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#reduce\[B>:A\]\(op:\(B,B\)=>B\):B "Permalink") def reduce[B >: T](op: (B, B) => B): B 

Definition Classes
    IterableOnceOps
  32. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#reduceLeft\[B>:A\]\(op:\(B,A\)=>B\):B "Permalink") def reduceLeft[B >: T](op: (B, T) => B): B 

Definition Classes
    IterableOnceOps
  33. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#reduceLeftOption\[B>:A\]\(op:\(B,A\)=>B\):Option\[B\] "Permalink") def reduceLeftOption[B >: T](op: (B, T) => B): Option[B] 

Definition Classes
    IterableOnceOps
  34. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#reduceOption\[B>:A\]\(op:\(B,B\)=>B\):Option\[B\] "Permalink") def reduceOption[B >: T](op: (B, B) => B): Option[B] 

Definition Classes
    IterableOnceOps
  35. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#reduceRight\[B>:A\]\(op:\(A,B\)=>B\):B "Permalink") def reduceRight[B >: T](op: (T, B) => B): B 

Definition Classes
    IterableOnceOps
  36. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#reduceRightOption\[B>:A\]\(op:\(A,B\)=>B\):Option\[B\] "Permalink") def reduceRightOption[B >: T](op: (T, B) => B): Option[B] 

Definition Classes
    IterableOnceOps
  37. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#reversed:Iterable\[A\] "Permalink") def reversed: Iterable[T] 

Attributes
    protected  

Definition Classes
    IterableOnceOps
  38. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#size:Int "Permalink") def size: Int 

Definition Classes
    IterableOnceOps
  39. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#splitAt\(n:Int\):\(C,C\) "Permalink") def splitAt(n: Int): (Iterator[T], Iterator[T]) 

Definition Classes
    IterableOnceOps
  40. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#sum\[B>:A\]\(implicitnum:scala.math.Numeric\[B\]\):B "Permalink") def sum[B >: T](implicit num: Numeric[B]): B 

Definition Classes
    IterableOnceOps
  41. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#to\[C1\]\(factory:scala.collection.Factory\[A,C1\]\):C1 "Permalink") def to[C1](factory: Factory[T, C1]): C1 

Definition Classes
    IterableOnceOps
  42. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#toArray\[B>:A\]\(implicitevidence$2:scala.reflect.ClassTag\[B\]\):Array\[B\] "Permalink") def toArray[B >: T](implicit arg0: ClassTag[B]): Array[B] 

Definition Classes
    IterableOnceOps
  43. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#toBuffer\[B>:A\]:scala.collection.mutable.Buffer\[B\] "Permalink") final  def toBuffer[B >: T]: Buffer[B] 

Definition Classes
    IterableOnceOps 

Annotations
     @inline()
  44. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#toIndexedSeq:IndexedSeq\[A\] "Permalink") def toIndexedSeq: IndexedSeq[T] 

Definition Classes
    IterableOnceOps
  45. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#toList:List\[A\] "Permalink") def toList: List[T] 

Definition Classes
    IterableOnceOps
  46. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#toMap\[K,V\]\(implicitev:A<:<\(K,V\)\):scala.collection.immutable.Map\[K,V\] "Permalink") def toMap[K, V](implicit ev: <:<[T, (K, V)]): Map[K, V] 

Definition Classes
    IterableOnceOps
  47. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#toSeq:Seq\[A\] "Permalink") def toSeq: Seq[T] 

Definition Classes
    IterableOnceOps
  48. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#toSet\[B>:A\]:scala.collection.immutable.Set\[B\] "Permalink") def toSet[B >: T]: Set[B] 

Definition Classes
    IterableOnceOps
  49. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#toVector:scala.collection.immutable.Vector\[A\] "Permalink") def toVector: Vector[T] 

Definition Classes
    IterableOnceOps
  50. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#/:\[B\]\(z:B\)\(op:\(B,A\)=>B\):B "Permalink") final  def /:[B](z: B)(op: (B, T) => B): B 

Definition Classes
    IterableOnceOps 

Annotations
     @deprecated @inline() 

Deprecated
    
_(Since version 2.13.0)_ Use foldLeft instead of /:
  51. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#:\\\[B\]\(z:B\)\(op:\(A,B\)=>B\):B "Permalink") final  def :\[B](z: B)(op: (T, B) => B): B 

Definition Classes
    IterableOnceOps 

Annotations
     @deprecated @inline() 

Deprecated
    
_(Since version 2.13.0)_ Use foldRight instead of :\
  52. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#aggregate\[B\]\(z:=>B\)\(seqop:\(B,A\)=>B,combop:\(B,B\)=>B\):B "Permalink") def aggregate[B](z: => B)(seqop: (B, T) => B, combop: (B, B) => B): B 

Definition Classes
    IterableOnceOps 

Annotations
     @deprecated 

Deprecated
    
_(Since version 2.13.0)_ For sequential collections, prefer `foldLeft(z)(seqop)`. For parallel collections, use `ParIterableLike#aggregate`.
  53. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#copyToBuffer\[B>:A\]\(dest:scala.collection.mutable.Buffer\[B\]\):Unit "Permalink") final  def copyToBuffer[B >: T](dest: Buffer[B]): Unit 

Definition Classes
    IterableOnceOps 

Annotations
     @deprecated @inline() 

Deprecated
    
_(Since version 2.13.0)_ Use `dest ++= coll` instead
  54. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#toIterator:Iterator\[A\] "Permalink") final  def toIterator: Iterator[T] 

Definition Classes
    IterableOnceOps 

Annotations
     @deprecated @inline() 

Deprecated
    
_(Since version 2.13.0)_ Use .iterator instead of .toIterator
  55. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#toStream:scala.collection.immutable.Stream\[A\] "Permalink") final  def toStream: Stream[T] 

Definition Classes
    IterableOnceOps 

Annotations
     @deprecated @inline() 

Deprecated
    
_(Since version 2.13.0)_ Use .to(LazyList) instead of .toStream


### Inherited from IterableOnce[T]
### Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#knownSize:Int "Permalink") def knownSize: Int 

Definition Classes
    IterableOnce
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#stepper\[S<:scala.collection.Stepper\[_\]\]\(implicitshape:scala.collection.StepperShape\[A,S\]\):S "Permalink") def stepper[S <: Stepper[_]](implicit shape: StepperShape[T, S]): S 

Definition Classes
    IterableOnce


### Inherited from AnyRef
### Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html###:Int "Permalink") final  def ##: Int 

Definition Classes
    AnyRef → Any
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#clone\(\):Object "Permalink") def clone(): AnyRef 

Attributes
    protected[lang]  

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#equals\(x$1:Object\):Boolean "Permalink") def equals(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef → Any
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef] 

Definition Classes
    AnyRef → Any 

Annotations
     @IntrinsicCandidate() @native()
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#hashCode\(\):Int "Permalink") def hashCode(): Int 

Definition Classes
    AnyRef → Any 

Annotations
     @IntrinsicCandidate() @native()
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#notify\(\):Unit "Permalink") final  def notify(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0 

Definition Classes
    AnyRef
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#wait\(\):Unit "Permalink") final  def wait(): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#finalize\(\):Unit "Permalink") def finalize(): Unit 

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
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0 

Definition Classes
    Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean 

Definition Classes
    Any


### Ungrouped
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#GroupedIterator\[B>:A\]extendsAbstractIterator\[Seq\[B\]\] "Permalink") class GroupedIterator[B >: A] extends AbstractIterator[Seq[B]] 

Definition Classes
    Iterator


  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html###:Int "Permalink") final  def ##: Int 

Definition Classes
    AnyRef → Any
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#++\[B>:A\]\(xs:=>scala.collection.IterableOnce\[B\]\):Iterator\[B\] "Permalink") final  def ++[B >: T](xs: => IterableOnce[B]): Iterator[B] 

Definition Classes
    Iterator 

Annotations
     @inline()
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#addString\(b:StringBuilder\):b.type "Permalink") final  def addString(b: StringBuilder): b.type 

Definition Classes
    IterableOnceOps 

Annotations
     @inline()
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#addString\(b:StringBuilder,sep:String\):b.type "Permalink") final  def addString(b: StringBuilder, sep: String): b.type 

Definition Classes
    IterableOnceOps 

Annotations
     @inline()
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#addString\(b:StringBuilder,start:String,sep:String,end:String\):b.type "Permalink") def addString(b: StringBuilder, start: String, sep: String, end: String): b.type 

Definition Classes
    IterableOnceOps
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0 

Definition Classes
    Any
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#buffered:scala.collection.BufferedIterator\[A\] "Permalink") def buffered: BufferedIterator[T] 

Definition Classes
    Iterator
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#clone\(\):Object "Permalink") def clone(): AnyRef 

Attributes
    protected[lang]  

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#collect\[B\]\(pf:PartialFunction\[A,B\]\):Iterator\[B\] "Permalink") def collect[B](pf: PartialFunction[T, B]): Iterator[B] 

Definition Classes
    Iterator → IterableOnceOps
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#collectFirst\[B\]\(pf:PartialFunction\[A,B\]\):Option\[B\] "Permalink") def collectFirst[B](pf: PartialFunction[T, B]): Option[B] 

Definition Classes
    IterableOnceOps
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#concat\[B>:A\]\(xs:=>scala.collection.IterableOnce\[B\]\):Iterator\[B\] "Permalink") def concat[B >: T](xs: => IterableOnce[B]): Iterator[B] 

Definition Classes
    Iterator
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#contains\(elem:Any\):Boolean "Permalink") def contains(elem: Any): Boolean 

Definition Classes
    Iterator
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#context:org.apache.spark.TaskContext "Permalink") val context: [TaskContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskContext.html "org.apache.spark.TaskContext")
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#copyToArray\[B>:A\]\(dest:Array\[B\],start:Int,n:Int\):Int "Permalink") def copyToArray[B >: T](dest: Array[B], start: Int, n: Int): Int 

Definition Classes
    IterableOnceOps
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#copyToArray\[B>:A\]\(dest:Array\[B\],start:Int\):Int "Permalink") def copyToArray[B >: T](dest: Array[B], start: Int): Int 

Definition Classes
    IterableOnceOps 

Annotations
     @deprecatedOverriding()
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#copyToArray\[B>:A\]\(dest:Array\[B\]\):Int "Permalink") def copyToArray[B >: T](dest: Array[B]): Int 

Definition Classes
    IterableOnceOps 

Annotations
     @deprecatedOverriding()
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#corresponds\[B\]\(that:scala.collection.IterableOnce\[B\]\)\(p:\(A,B\)=>Boolean\):Boolean "Permalink") def corresponds[B](that: IterableOnce[B])(p: (T, B) => Boolean): Boolean 

Definition Classes
    IterableOnceOps
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#count\(p:A=>Boolean\):Int "Permalink") def count(p: (T) => Boolean): Int 

Definition Classes
    IterableOnceOps
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#delegate:Iterator\[T\] "Permalink") val delegate: Iterator[T]
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#distinct:Iterator\[A\] "Permalink") def distinct: Iterator[T] 

Definition Classes
    Iterator
  23. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#distinctBy\[B\]\(f:A=>B\):Iterator\[A\] "Permalink") def distinctBy[B](f: (T) => B): Iterator[T] 

Definition Classes
    Iterator
  24. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#drop\(n:Int\):Iterator\[A\] "Permalink") def drop(n: Int): Iterator[T] 

Definition Classes
    Iterator → IterableOnceOps
  25. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#dropWhile\(p:A=>Boolean\):Iterator\[A\] "Permalink") def dropWhile(p: (T) => Boolean): Iterator[T] 

Definition Classes
    Iterator → IterableOnceOps
  26. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#duplicate:\(Iterator\[A\],Iterator\[A\]\) "Permalink") def duplicate: (Iterator[T], Iterator[T]) 

Definition Classes
    Iterator
  27. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  28. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#equals\(x$1:Object\):Boolean "Permalink") def equals(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef → Any
  29. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#exists\(p:A=>Boolean\):Boolean "Permalink") def exists(p: (T) => Boolean): Boolean 

Definition Classes
    IterableOnceOps
  30. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#filter\(p:A=>Boolean\):Iterator\[A\] "Permalink") def filter(p: (T) => Boolean): Iterator[T] 

Definition Classes
    Iterator → IterableOnceOps
  31. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#filterNot\(p:A=>Boolean\):Iterator\[A\] "Permalink") def filterNot(p: (T) => Boolean): Iterator[T] 

Definition Classes
    Iterator → IterableOnceOps
  32. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#find\(p:A=>Boolean\):Option\[A\] "Permalink") def find(p: (T) => Boolean): Option[T] 

Definition Classes
    IterableOnceOps
  33. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#flatMap\[B\]\(f:A=>scala.collection.IterableOnce\[B\]\):Iterator\[B\] "Permalink") def flatMap[B](f: (T) => IterableOnce[B]): Iterator[B] 

Definition Classes
    Iterator → IterableOnceOps
  34. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#flatten\[B\]\(implicitev:A=>scala.collection.IterableOnce\[B\]\):Iterator\[B\] "Permalink") def flatten[B](implicit ev: (T) => IterableOnce[B]): Iterator[B] 

Definition Classes
    Iterator → IterableOnceOps
  35. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#fold\[A1>:A\]\(z:A1\)\(op:\(A1,A1\)=>A1\):A1 "Permalink") def fold[A1 >: T](z: A1)(op: (A1, A1) => A1): A1 

Definition Classes
    IterableOnceOps
  36. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#foldLeft\[B\]\(z:B\)\(op:\(B,A\)=>B\):B "Permalink") def foldLeft[B](z: B)(op: (B, T) => B): B 

Definition Classes
    IterableOnceOps
  37. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#foldRight\[B\]\(z:B\)\(op:\(A,B\)=>B\):B "Permalink") def foldRight[B](z: B)(op: (T, B) => B): B 

Definition Classes
    IterableOnceOps
  38. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#forall\(p:A=>Boolean\):Boolean "Permalink") def forall(p: (T) => Boolean): Boolean 

Definition Classes
    IterableOnceOps
  39. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#foreach\[U\]\(f:A=>U\):Unit "Permalink") def foreach[U](f: (T) => U): Unit 

Definition Classes
    IterableOnceOps
  40. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef] 

Definition Classes
    AnyRef → Any 

Annotations
     @IntrinsicCandidate() @native()
  41. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#grouped\[B>:A\]\(size:Int\):Iterator.this.GroupedIterator\[B\] "Permalink") def grouped[B >: T](size: Int): [GroupedIterator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#GroupedIterator\[B>:A\]extendsAbstractIterator\[Seq\[B\]\])[B] 

Definition Classes
    Iterator
  42. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#hasNext:Boolean "Permalink") def hasNext: Boolean 

Definition Classes
     [ContextAwareIterator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html "org.apache.spark.ContextAwareIterator") → Iterator
  43. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#hashCode\(\):Int "Permalink") def hashCode(): Int 

Definition Classes
    AnyRef → Any 

Annotations
     @IntrinsicCandidate() @native()
  44. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#indexOf\[B>:A\]\(elem:B,from:Int\):Int "Permalink") def indexOf[B >: T](elem: B, from: Int): Int 

Definition Classes
    Iterator
  45. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#indexOf\[B>:A\]\(elem:B\):Int "Permalink") def indexOf[B >: T](elem: B): Int 

Definition Classes
    Iterator
  46. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#indexWhere\(p:A=>Boolean,from:Int\):Int "Permalink") def indexWhere(p: (T) => Boolean, from: Int): Int 

Definition Classes
    Iterator
  47. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#isEmpty:Boolean "Permalink") def isEmpty: Boolean 

Definition Classes
    Iterator → IterableOnceOps 

Annotations
     @deprecatedOverriding()
  48. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean 

Definition Classes
    Any
  49. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#isTraversableAgain:Boolean "Permalink") def isTraversableAgain: Boolean 

Definition Classes
    IterableOnceOps
  50. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#iterator:Iterator\[A\] "Permalink") final  def iterator: Iterator[T] 

Definition Classes
    Iterator → IterableOnce 

Annotations
     @inline()
  51. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#knownSize:Int "Permalink") def knownSize: Int 

Definition Classes
    IterableOnce
  52. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#length:Int "Permalink") final  def length: Int 

Definition Classes
    Iterator 

Annotations
     @inline()
  53. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#map\[B\]\(f:A=>B\):Iterator\[B\] "Permalink") def map[B](f: (T) => B): Iterator[B] 

Definition Classes
    Iterator → IterableOnceOps
  54. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#max\[B>:A\]\(implicitord:scala.math.Ordering\[B\]\):A "Permalink") def max[B >: T](implicit ord: Ordering[B]): T 

Definition Classes
    IterableOnceOps
  55. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#maxBy\[B\]\(f:A=>B\)\(implicitord:scala.math.Ordering\[B\]\):A "Permalink") def maxBy[B](f: (T) => B)(implicit ord: Ordering[B]): T 

Definition Classes
    IterableOnceOps
  56. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#maxByOption\[B\]\(f:A=>B\)\(implicitord:scala.math.Ordering\[B\]\):Option\[A\] "Permalink") def maxByOption[B](f: (T) => B)(implicit ord: Ordering[B]): Option[T] 

Definition Classes
    IterableOnceOps
  57. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#maxOption\[B>:A\]\(implicitord:scala.math.Ordering\[B\]\):Option\[A\] "Permalink") def maxOption[B >: T](implicit ord: Ordering[B]): Option[T] 

Definition Classes
    IterableOnceOps
  58. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#min\[B>:A\]\(implicitord:scala.math.Ordering\[B\]\):A "Permalink") def min[B >: T](implicit ord: Ordering[B]): T 

Definition Classes
    IterableOnceOps
  59. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#minBy\[B\]\(f:A=>B\)\(implicitord:scala.math.Ordering\[B\]\):A "Permalink") def minBy[B](f: (T) => B)(implicit ord: Ordering[B]): T 

Definition Classes
    IterableOnceOps
  60. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#minByOption\[B\]\(f:A=>B\)\(implicitord:scala.math.Ordering\[B\]\):Option\[A\] "Permalink") def minByOption[B](f: (T) => B)(implicit ord: Ordering[B]): Option[T] 

Definition Classes
    IterableOnceOps
  61. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#minOption\[B>:A\]\(implicitord:scala.math.Ordering\[B\]\):Option\[A\] "Permalink") def minOption[B >: T](implicit ord: Ordering[B]): Option[T] 

Definition Classes
    IterableOnceOps
  62. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#mkString:String "Permalink") final  def mkString: String 

Definition Classes
    IterableOnceOps 

Annotations
     @inline()
  63. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#mkString\(sep:String\):String "Permalink") final  def mkString(sep: String): String 

Definition Classes
    IterableOnceOps 

Annotations
     @inline()
  64. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#mkString\(start:String,sep:String,end:String\):String "Permalink") final  def mkString(start: String, sep: String, end: String): String 

Definition Classes
    IterableOnceOps
  65. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  66. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#next\(\):T "Permalink") def next(): T 

Definition Classes
     [ContextAwareIterator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html "org.apache.spark.ContextAwareIterator") → Iterator
  67. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#nextOption\(\):Option\[A\] "Permalink") def nextOption(): Option[T] 

Definition Classes
    Iterator
  68. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#nonEmpty:Boolean "Permalink") def nonEmpty: Boolean 

Definition Classes
    IterableOnceOps 

Annotations
     @deprecatedOverriding()
  69. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#notify\(\):Unit "Permalink") final  def notify(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  70. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  71. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#padTo\[B>:A\]\(len:Int,elem:B\):Iterator\[B\] "Permalink") def padTo[B >: T](len: Int, elem: B): Iterator[B] 

Definition Classes
    Iterator
  72. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#partition\(p:A=>Boolean\):\(Iterator\[A\],Iterator\[A\]\) "Permalink") def partition(p: (T) => Boolean): (Iterator[T], Iterator[T]) 

Definition Classes
    Iterator
  73. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#patch\[B>:A\]\(from:Int,patchElems:Iterator\[B\],replaced:Int\):Iterator\[B\] "Permalink") def patch[B >: T](from: Int, patchElems: Iterator[B], replaced: Int): Iterator[B] 

Definition Classes
    Iterator
  74. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#product\[B>:A\]\(implicitnum:scala.math.Numeric\[B\]\):B "Permalink") def product[B >: T](implicit num: Numeric[B]): B 

Definition Classes
    IterableOnceOps
  75. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#reduce\[B>:A\]\(op:\(B,B\)=>B\):B "Permalink") def reduce[B >: T](op: (B, B) => B): B 

Definition Classes
    IterableOnceOps
  76. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#reduceLeft\[B>:A\]\(op:\(B,A\)=>B\):B "Permalink") def reduceLeft[B >: T](op: (B, T) => B): B 

Definition Classes
    IterableOnceOps
  77. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#reduceLeftOption\[B>:A\]\(op:\(B,A\)=>B\):Option\[B\] "Permalink") def reduceLeftOption[B >: T](op: (B, T) => B): Option[B] 

Definition Classes
    IterableOnceOps
  78. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#reduceOption\[B>:A\]\(op:\(B,B\)=>B\):Option\[B\] "Permalink") def reduceOption[B >: T](op: (B, B) => B): Option[B] 

Definition Classes
    IterableOnceOps
  79. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#reduceRight\[B>:A\]\(op:\(A,B\)=>B\):B "Permalink") def reduceRight[B >: T](op: (T, B) => B): B 

Definition Classes
    IterableOnceOps
  80. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#reduceRightOption\[B>:A\]\(op:\(A,B\)=>B\):Option\[B\] "Permalink") def reduceRightOption[B >: T](op: (T, B) => B): Option[B] 

Definition Classes
    IterableOnceOps
  81. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#reversed:Iterable\[A\] "Permalink") def reversed: Iterable[T] 

Attributes
    protected  

Definition Classes
    IterableOnceOps
  82. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#sameElements\[B>:A\]\(that:scala.collection.IterableOnce\[B\]\):Boolean "Permalink") def sameElements[B >: T](that: IterableOnce[B]): Boolean 

Definition Classes
    Iterator
  83. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#scanLeft\[B\]\(z:B\)\(op:\(B,A\)=>B\):Iterator\[B\] "Permalink") def scanLeft[B](z: B)(op: (B, T) => B): Iterator[B] 

Definition Classes
    Iterator → IterableOnceOps
  84. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#size:Int "Permalink") def size: Int 

Definition Classes
    IterableOnceOps
  85. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#slice\(from:Int,until:Int\):Iterator\[A\] "Permalink") def slice(from: Int, until: Int): Iterator[T] 

Definition Classes
    Iterator → IterableOnceOps
  86. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#sliceIterator\(from:Int,until:Int\):Iterator\[A\] "Permalink") def sliceIterator(from: Int, until: Int): Iterator[T] 

Attributes
    protected  

Definition Classes
    Iterator
  87. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#sliding\[B>:A\]\(size:Int,step:Int\):Iterator.this.GroupedIterator\[B\] "Permalink") def sliding[B >: T](size: Int, step: Int): [GroupedIterator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#GroupedIterator\[B>:A\]extendsAbstractIterator\[Seq\[B\]\])[B] 

Definition Classes
    Iterator
  88. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#span\(p:A=>Boolean\):\(Iterator\[A\],Iterator\[A\]\) "Permalink") def span(p: (T) => Boolean): (Iterator[T], Iterator[T]) 

Definition Classes
    Iterator → IterableOnceOps
  89. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#splitAt\(n:Int\):\(C,C\) "Permalink") def splitAt(n: Int): (Iterator[T], Iterator[T]) 

Definition Classes
    IterableOnceOps
  90. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#stepper\[S<:scala.collection.Stepper\[_\]\]\(implicitshape:scala.collection.StepperShape\[A,S\]\):S "Permalink") def stepper[S <: Stepper[_]](implicit shape: StepperShape[T, S]): S 

Definition Classes
    IterableOnce
  91. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#sum\[B>:A\]\(implicitnum:scala.math.Numeric\[B\]\):B "Permalink") def sum[B >: T](implicit num: Numeric[B]): B 

Definition Classes
    IterableOnceOps
  92. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0 

Definition Classes
    AnyRef
  93. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#take\(n:Int\):Iterator\[A\] "Permalink") def take(n: Int): Iterator[T] 

Definition Classes
    Iterator → IterableOnceOps
  94. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#takeWhile\(p:A=>Boolean\):Iterator\[A\] "Permalink") def takeWhile(p: (T) => Boolean): Iterator[T] 

Definition Classes
    Iterator → IterableOnceOps
  95. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#tapEach\[U\]\(f:A=>U\):Iterator\[A\] "Permalink") def tapEach[U](f: (T) => U): Iterator[T] 

Definition Classes
    Iterator → IterableOnceOps
  96. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#to\[C1\]\(factory:scala.collection.Factory\[A,C1\]\):C1 "Permalink") def to[C1](factory: Factory[T, C1]): C1 

Definition Classes
    IterableOnceOps
  97. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#toArray\[B>:A\]\(implicitevidence$2:scala.reflect.ClassTag\[B\]\):Array\[B\] "Permalink") def toArray[B >: T](implicit arg0: ClassTag[B]): Array[B] 

Definition Classes
    IterableOnceOps
  98. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#toBuffer\[B>:A\]:scala.collection.mutable.Buffer\[B\] "Permalink") final  def toBuffer[B >: T]: Buffer[B] 

Definition Classes
    IterableOnceOps 

Annotations
     @inline()
  99. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#toIndexedSeq:IndexedSeq\[A\] "Permalink") def toIndexedSeq: IndexedSeq[T] 

Definition Classes
    IterableOnceOps
  100. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#toList:List\[A\] "Permalink") def toList: List[T] 

Definition Classes
    IterableOnceOps
  101. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#toMap\[K,V\]\(implicitev:A<:<\(K,V\)\):scala.collection.immutable.Map\[K,V\] "Permalink") def toMap[K, V](implicit ev: <:<[T, (K, V)]): Map[K, V] 

Definition Classes
    IterableOnceOps
  102. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#toSeq:Seq\[A\] "Permalink") def toSeq: Seq[T] 

Definition Classes
    IterableOnceOps
  103. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#toSet\[B>:A\]:scala.collection.immutable.Set\[B\] "Permalink") def toSet[B >: T]: Set[B] 

Definition Classes
    IterableOnceOps
  104. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#toString\(\):String "Permalink") def toString(): [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String") 

Definition Classes
    Iterator → AnyRef → Any
  105. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#toVector:scala.collection.immutable.Vector\[A\] "Permalink") def toVector: Vector[T] 

Definition Classes
    IterableOnceOps
  106. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  107. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  108. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#wait\(\):Unit "Permalink") final  def wait(): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  109. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#withFilter\(p:A=>Boolean\):Iterator\[A\] "Permalink") def withFilter(p: (T) => Boolean): Iterator[T] 

Definition Classes
    Iterator
  110. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#zip\[B\]\(that:scala.collection.IterableOnce\[B\]\):Iterator\[\(A,B\)\] "Permalink") def zip[B](that: IterableOnce[B]): Iterator[(T, B)] 

Definition Classes
    Iterator
  111. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#zipAll\[A1>:A,B\]\(that:scala.collection.IterableOnce\[B\],thisElem:A1,thatElem:B\):Iterator\[\(A1,B\)\] "Permalink") def zipAll[A1 >: T, B](that: IterableOnce[B], thisElem: A1, thatElem: B): Iterator[(A1, B)] 

Definition Classes
    Iterator
  112. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#zipWithIndex:Iterator\[\(A,Int\)\] "Permalink") def zipWithIndex: Iterator[(T, Int)] 

Definition Classes
    Iterator → IterableOnceOps
  113. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#/:\[B\]\(z:B\)\(op:\(B,A\)=>B\):B "Permalink") final  def /:[B](z: B)(op: (B, T) => B): B 

Definition Classes
    IterableOnceOps 

Annotations
     @deprecated @inline() 

Deprecated
    
_(Since version 2.13.0)_ Use foldLeft instead of /:
  114. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#:\\\[B\]\(z:B\)\(op:\(A,B\)=>B\):B "Permalink") final  def :\[B](z: B)(op: (T, B) => B): B 

Definition Classes
    IterableOnceOps 

Annotations
     @deprecated @inline() 

Deprecated
    
_(Since version 2.13.0)_ Use foldRight instead of :\
  115. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#aggregate\[B\]\(z:=>B\)\(seqop:\(B,A\)=>B,combop:\(B,B\)=>B\):B "Permalink") def aggregate[B](z: => B)(seqop: (B, T) => B, combop: (B, B) => B): B 

Definition Classes
    IterableOnceOps 

Annotations
     @deprecated 

Deprecated
    
_(Since version 2.13.0)_ For sequential collections, prefer `foldLeft(z)(seqop)`. For parallel collections, use `ParIterableLike#aggregate`.
  116. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#copyToBuffer\[B>:A\]\(dest:scala.collection.mutable.Buffer\[B\]\):Unit "Permalink") final  def copyToBuffer[B >: T](dest: Buffer[B]): Unit 

Definition Classes
    IterableOnceOps 

Annotations
     @deprecated @inline() 

Deprecated
    
_(Since version 2.13.0)_ Use `dest ++= coll` instead
  117. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#finalize\(\):Unit "Permalink") def finalize(): Unit 

Attributes
    protected[lang]  

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.Throwable]) @Deprecated 

Deprecated
    
_(Since version 9)_
  118. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#hasDefiniteSize:Boolean "Permalink") final  def hasDefiniteSize: Boolean 

Definition Classes
    Iterator → IterableOnceOps 

Annotations
     @deprecated @inline() 

Deprecated
    
_(Since version 2.13.0)_ hasDefiniteSize on Iterator is the same as isEmpty
  119. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#scanRight\[B\]\(z:B\)\(op:\(A,B\)=>B\):Iterator\[B\] "Permalink") def scanRight[B](z: B)(op: (T, B) => B): Iterator[B] 

Definition Classes
    Iterator 

Annotations
     @deprecated 

Deprecated
    
_(Since version 2.13.0)_ Call scanRight on an Iterable instead.
  120. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#seq:Iterator.this.type "Permalink") def seq: [ContextAwareIterator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html "org.apache.spark.ContextAwareIterator").this.type 

Definition Classes
    Iterator 

Annotations
     @deprecated 

Deprecated
    
_(Since version 2.13.0)_ Iterator.seq always returns the iterator itself
  121. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#toIterator:Iterator\[A\] "Permalink") final  def toIterator: Iterator[T] 

Definition Classes
    IterableOnceOps 

Annotations
     @deprecated @inline() 

Deprecated
    
_(Since version 2.13.0)_ Use .iterator instead of .toIterator
  122. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ContextAwareIterator.html#toStream:scala.collection.immutable.Stream\[A\] "Permalink") final  def toStream: Stream[T] 

Definition Classes
    IterableOnceOps 

Annotations
     @deprecated @inline() 

Deprecated
    
_(Since version 2.13.0)_ Use .to(LazyList) instead of .toStream


