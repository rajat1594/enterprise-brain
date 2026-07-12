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
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/index.html "Permalink") package rdd
Provides several RDD implementations.
Provides several RDD implementations. See [org.apache.spark.rdd.RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD").  

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/AsyncRDDActions.html "A set of asynchronous RDD actions available through an implicit conversion.")[AsyncRDDActions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/AsyncRDDActions.html "A set of asynchronous RDD actions available through an implicit conversion.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/CoGroupedRDD.html ":: DeveloperApi :: An RDD that cogroups its parents.")[CoGroupedRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/CoGroupedRDD.html ":: DeveloperApi :: An RDD that cogroups its parents.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/DeterministicLevel$.html "The deterministic level of RDD's output \(i.e.")[DeterministicLevel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/DeterministicLevel$.html "The deterministic level of RDD's output \(i.e.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/DoubleRDDFunctions.html "Extra functions available on RDDs of Doubles through an implicit conversion.")[DoubleRDDFunctions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/DoubleRDDFunctions.html "Extra functions available on RDDs of Doubles through an implicit conversion.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/HadoopRDD.html ":: DeveloperApi :: An RDD that provides core functionality for reading data stored in Hadoop \(e.g., files in HDFS, sources in HBase, or S3\), using the older MapReduce API \(org.apache.hadoop.mapred\).")[HadoopRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/HadoopRDD.html ":: DeveloperApi :: An RDD that provides core functionality for reading data stored in Hadoop \(e.g., files in HDFS, sources in HBase, or S3\), using the older MapReduce API \(org.apache.hadoop.mapred\).")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/JdbcRDD$.html) [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/JdbcRDD.html "An RDD that executes a SQL query on a JDBC connection and reads results.")[JdbcRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/JdbcRDD.html "An RDD that executes a SQL query on a JDBC connection and reads results.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/NewHadoopRDD.html ":: DeveloperApi :: An RDD that provides core functionality for reading data stored in Hadoop \(e.g., files in HDFS, sources in HBase, or S3\), using the new MapReduce API \(org.apache.hadoop.mapreduce\).")[NewHadoopRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/NewHadoopRDD.html ":: DeveloperApi :: An RDD that provides core functionality for reading data stored in Hadoop \(e.g., files in HDFS, sources in HBase, or S3\), using the new MapReduce API \(org.apache.hadoop.mapreduce\).")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/OrderedRDDFunctions.html "Extra functions available on RDDs of \(key, value\) pairs where the key is sortable through an implicit conversion.")[OrderedRDDFunctions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/OrderedRDDFunctions.html "Extra functions available on RDDs of \(key, value\) pairs where the key is sortable through an implicit conversion.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html "Extra functions available on RDDs of \(key, value\) pairs through an implicit conversion.")[PairRDDFunctions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html "Extra functions available on RDDs of \(key, value\) pairs through an implicit conversion.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PartitionCoalescer.html "::DeveloperApi:: A PartitionCoalescer defines how to coalesce the partitions of a given RDD.")[PartitionCoalescer](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PartitionCoalescer.html "::DeveloperApi:: A PartitionCoalescer defines how to coalesce the partitions of a given RDD.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PartitionGroup.html "::DeveloperApi:: A group of Partitions")[PartitionGroup](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PartitionGroup.html "::DeveloperApi:: A group of Partitions")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PartitionPruningRDD$.html) [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PartitionPruningRDD.html ":: DeveloperApi :: An RDD used to prune RDD partitions/partitions so we can avoid launching tasks on all partitions.")[PartitionPruningRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PartitionPruningRDD.html ":: DeveloperApi :: An RDD used to prune RDD partitions/partitions so we can avoid launching tasks on all partitions.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD$.html "Defines implicit functions that provide extra functionalities on RDDs of specific types.") [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "A Resilient Distributed Dataset \(RDD\), the basic abstraction in Spark.")[RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "A Resilient Distributed Dataset \(RDD\), the basic abstraction in Spark.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDDBarrier.html ":: Experimental :: Wraps an RDD in a barrier stage, which forces Spark to launch tasks of this stage together.")[RDDBarrier](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDDBarrier.html ":: Experimental :: Wraps an RDD in a barrier stage, which forces Spark to launch tasks of this stage together.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/SequenceFileRDDFunctions.html "Extra functions available on RDDs of \(key, value\) pairs to create a Hadoop SequenceFile, through an implicit conversion.")[SequenceFileRDDFunctions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/SequenceFileRDDFunctions.html "Extra functions available on RDDs of \(key, value\) pairs to create a Hadoop SequenceFile, through an implicit conversion.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/ShuffledRDD.html ":: DeveloperApi :: The resulting RDD from a shuffle \(e.g.")[ShuffledRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/ShuffledRDD.html ":: DeveloperApi :: The resulting RDD from a shuffle \(e.g.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/UnionRDD$.html) [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/UnionRDD.html)[UnionRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/UnionRDD.html)
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


p
[org](https://spark.apache.org/docs/latest/api/scala/org/index.html "org").[apache](https://spark.apache.org/docs/latest/api/scala/org/apache/index.html "org.apache").[spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
# rdd[ __](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/index.html "Permalink")
####  package rdd
Provides several RDD implementations. See [org.apache.spark.rdd.RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD").  

Source
    [package.scala](https://github.com/apache/spark/tree/v4.1.2/core/src/main/scala/org/apache/spark/rdd/package.scala)
Linear Supertypes
AnyRef, Any
__ __
Ordering
  1. Alphabetic
  2. By Inheritance


Inherited  

  1. rdd
  2. AnyRef
  3. Any


  1. Hide All
  2. Show All


Visibility
  1. Public
  2. Protected


### Type Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/AsyncRDDActions.html "Permalink") class [AsyncRDDActions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/AsyncRDDActions.html "A set of asynchronous RDD actions available through an implicit conversion.")[T] extends Serializable with Logging
A set of asynchronous RDD actions available through an implicit conversion.
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/CoGroupedRDD.html "Permalink") class [CoGroupedRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/CoGroupedRDD.html ":: DeveloperApi :: An RDD that cogroups its parents.")[K] extends [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, Array[Iterable[_]])]
An RDD that cogroups its parents.
An RDD that cogroups its parents. For each key k in parent RDDs, the resulting RDD contains a tuple with the list of values for that key.  

Annotations
     @DeveloperApi() 

Note
    
This is an internal API. We recommend users use RDD.cogroup(...) instead of instantiating this directly.
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/DoubleRDDFunctions.html "Permalink") class [DoubleRDDFunctions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/DoubleRDDFunctions.html "Extra functions available on RDDs of Doubles through an implicit conversion.") extends Logging with Serializable
Extra functions available on RDDs of Doubles through an implicit conversion.
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/HadoopRDD.html "Permalink") class [HadoopRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/HadoopRDD.html ":: DeveloperApi :: An RDD that provides core functionality for reading data stored in Hadoop \(e.g., files in HDFS, sources in HBase, or S3\), using the older MapReduce API \(org.apache.hadoop.mapred\).")[K, V] extends [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, V)] with Logging
An RDD that provides core functionality for reading data stored in Hadoop (e.g., files in HDFS, sources in HBase, or S3), using the older MapReduce API (`org.apache.hadoop.mapred`).
An RDD that provides core functionality for reading data stored in Hadoop (e.g., files in HDFS, sources in HBase, or S3), using the older MapReduce API (`org.apache.hadoop.mapred`).  

Annotations
     @DeveloperApi() 

Note
    
Instantiating this class directly is not recommended, please use `org.apache.spark.SparkContext.hadoopRDD()`
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/index.html#IsWritable\[A\]=A=>org.apache.hadoop.io.Writable "Permalink") type IsWritable[A] = (A) => Writable
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/NewHadoopRDD.html "Permalink") class [NewHadoopRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/NewHadoopRDD.html ":: DeveloperApi :: An RDD that provides core functionality for reading data stored in Hadoop \(e.g., files in HDFS, sources in HBase, or S3\), using the new MapReduce API \(org.apache.hadoop.mapreduce\).")[K, V] extends [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, V)] with Logging
An RDD that provides core functionality for reading data stored in Hadoop (e.g., files in HDFS, sources in HBase, or S3), using the new MapReduce API (`org.apache.hadoop.mapreduce`).
An RDD that provides core functionality for reading data stored in Hadoop (e.g., files in HDFS, sources in HBase, or S3), using the new MapReduce API (`org.apache.hadoop.mapreduce`).  

Annotations
     @DeveloperApi() 

Note
    
Instantiating this class directly is not recommended, please use `org.apache.spark.SparkContext.newAPIHadoopRDD()`
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/OrderedRDDFunctions.html "Permalink") class [OrderedRDDFunctions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/OrderedRDDFunctions.html "Extra functions available on RDDs of \(key, value\) pairs where the key is sortable through an implicit conversion.")[K, V, P <: Product2[K, V]] extends Logging with Serializable
Extra functions available on RDDs of (key, value) pairs where the key is sortable through an implicit conversion.
Extra functions available on RDDs of (key, value) pairs where the key is sortable through an implicit conversion. They will work with any key type `K` that has an implicit `Ordering[K]` in scope. Ordering objects already exist for all of the standard primitive types. Users can also define their own orderings for custom types, or to override the default ordering. The implicit ordering that is in the closest scope will be used.

```
import org.apache.spark.SparkContext._

val rdd: RDD[(String, Int)] = ...
implicit val caseInsensitiveOrdering = new Ordering[String] {
  override def compare(a: String, b: String) =
    a.toLowerCase(Locale.ROOT).compare(b.toLowerCase(Locale.ROOT))
}

// Sort by key, using the above case insensitive ordering.
rdd.sortByKey()
```

  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html "Permalink") class [PairRDDFunctions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html "Extra functions available on RDDs of \(key, value\) pairs through an implicit conversion.")[K, V] extends Logging with Serializable
Extra functions available on RDDs of (key, value) pairs through an implicit conversion.
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PartitionCoalescer.html "Permalink") trait [PartitionCoalescer](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PartitionCoalescer.html "::DeveloperApi:: A PartitionCoalescer defines how to coalesce the partitions of a given RDD.") extends AnyRef
::DeveloperApi:: A PartitionCoalescer defines how to coalesce the partitions of a given RDD.
::DeveloperApi:: A PartitionCoalescer defines how to coalesce the partitions of a given RDD.  

Annotations
     @DeveloperApi()
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PartitionGroup.html "Permalink") class [PartitionGroup](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PartitionGroup.html "::DeveloperApi:: A group of Partitions") extends AnyRef
::DeveloperApi:: A group of `Partition`s
::DeveloperApi:: A group of `Partition`s 

Annotations
     @DeveloperApi()
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PartitionPruningRDD.html "Permalink") class [PartitionPruningRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PartitionPruningRDD.html ":: DeveloperApi :: An RDD used to prune RDD partitions/partitions so we can avoid launching tasks on all partitions.")[T] extends [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[T]
An RDD used to prune RDD partitions/partitions so we can avoid launching tasks on all partitions.
An RDD used to prune RDD partitions/partitions so we can avoid launching tasks on all partitions. An example use case: If we know the RDD is partitioned by range, and the execution DAG has a filter on the key, we can avoid launching tasks on partitions that don't have the range covering the key.  

Annotations
     @DeveloperApi()
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "Permalink") abstract  class [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "A Resilient Distributed Dataset \(RDD\), the basic abstraction in Spark.")[T] extends Serializable with Logging
A Resilient Distributed Dataset (RDD), the basic abstraction in Spark.
A Resilient Distributed Dataset (RDD), the basic abstraction in Spark. Represents an immutable, partitioned collection of elements that can be operated on in parallel. This class contains the basic operations available on all RDDs, such as `map`, `filter`, and `persist`. In addition, [org.apache.spark.rdd.PairRDDFunctions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html "org.apache.spark.rdd.PairRDDFunctions") contains operations available only on RDDs of key-value pairs, such as `groupByKey` and `join`; [org.apache.spark.rdd.DoubleRDDFunctions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/DoubleRDDFunctions.html "org.apache.spark.rdd.DoubleRDDFunctions") contains operations available only on RDDs of Doubles; and [org.apache.spark.rdd.SequenceFileRDDFunctions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/SequenceFileRDDFunctions.html "org.apache.spark.rdd.SequenceFileRDDFunctions") contains operations available on RDDs that can be saved as SequenceFiles. All operations are automatically available on any RDD of the right type (e.g. RDD[(Int, Int)]) through implicit.
Internally, each RDD is characterized by five main properties:
     * A list of partitions
     * A function for computing each split
     * A list of dependencies on other RDDs
     * Optionally, a Partitioner for key-value RDDs (e.g. to say that the RDD is hash-partitioned)
     * Optionally, a list of preferred locations to compute each split on (e.g. block locations for an HDFS file)
All of the scheduling and execution in Spark is done based on these methods, allowing each RDD to implement its own way of computing itself. Indeed, users can implement custom RDDs (e.g. for reading data from a new storage system) by overriding these functions. Please refer to the [Spark paper](http://people.csail.mit.edu/matei/papers/2012/nsdi_spark.pdf) for more details on RDD internals. 
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDDBarrier.html "Permalink") class [RDDBarrier](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDDBarrier.html ":: Experimental :: Wraps an RDD in a barrier stage, which forces Spark to launch tasks of this stage together.")[T] extends AnyRef
Wraps an RDD in a barrier stage, which forces Spark to launch tasks of this stage together.
Wraps an RDD in a barrier stage, which forces Spark to launch tasks of this stage together. [org.apache.spark.rdd.RDDBarrier](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDDBarrier.html "org.apache.spark.rdd.RDDBarrier") instances are created by [org.apache.spark.rdd.RDD#barrier](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html#barrier\(\):org.apache.spark.rdd.RDDBarrier\[T\]).  

Annotations
     @Experimental() @Since("2.4.0")
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/SequenceFileRDDFunctions.html "Permalink") class [SequenceFileRDDFunctions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/SequenceFileRDDFunctions.html "Extra functions available on RDDs of \(key, value\) pairs to create a Hadoop SequenceFile, through an implicit conversion.")[K, V] extends Logging with Serializable
Extra functions available on RDDs of (key, value) pairs to create a Hadoop SequenceFile, through an implicit conversion.
Extra functions available on RDDs of (key, value) pairs to create a Hadoop SequenceFile, through an implicit conversion.  

Note
    
This can't be part of PairRDDFunctions because we need more implicit parameters to convert our keys and values to Writable.
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/ShuffledRDD.html "Permalink") class [ShuffledRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/ShuffledRDD.html ":: DeveloperApi :: The resulting RDD from a shuffle \(e.g.")[K, V, C] extends [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, C)]
The resulting RDD from a shuffle (e.g.
The resulting RDD from a shuffle (e.g. repartitioning of data). 

K
    
the key class. 

V
    
the value class. 

C
    
the combiner class. 

Annotations
     @DeveloperApi()
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/UnionRDD.html "Permalink") class [UnionRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/UnionRDD.html)[T] extends [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[T] 

Annotations
     @DeveloperApi()


### Deprecated Type Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/JdbcRDD.html "Permalink") class [JdbcRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/JdbcRDD.html "An RDD that executes a SQL query on a JDBC connection and reads results.")[T] extends [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[T] with Logging
An RDD that executes a SQL query on a JDBC connection and reads results.
An RDD that executes a SQL query on a JDBC connection and reads results. For usage example, see test case JdbcRDDSuite.  

Annotations
     @deprecated 

Deprecated
    
_(Since version 4.1.0)_ Jdbc RDD is deprecated, consider using JDBC data source instead.


### Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/DeterministicLevel$.html "Permalink") object [DeterministicLevel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/DeterministicLevel$.html "The deterministic level of RDD's output \(i.e.") extends Enumeration
The deterministic level of RDD's output (i.e.
The deterministic level of RDD's output (i.e. what `RDD#compute` returns). This explains how the output will diff when Spark reruns the tasks for the RDD. There are 3 deterministic levels: 1. DETERMINATE: The RDD output is always the same data set in the same order after a rerun. 2. UNORDERED: The RDD output is always the same data set but the order can be different after a rerun. 3. INDETERMINATE. The RDD output can be different after a rerun.
Note that, the output of an RDD usually relies on the parent RDDs. When the parent RDD's output is INDETERMINATE, it's very likely the RDD's output is also INDETERMINATE.  

Annotations
     @DeveloperApi()
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/JdbcRDD$.html "Permalink") object [JdbcRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/JdbcRDD$.html) extends [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable")
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PartitionPruningRDD$.html "Permalink") object [PartitionPruningRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PartitionPruningRDD$.html) extends [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable") 

Annotations
     @DeveloperApi()
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD$.html "Permalink") object [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD$.html "Defines implicit functions that provide extra functionalities on RDDs of specific types.") extends [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable")
Defines implicit functions that provide extra functionalities on RDDs of specific types.
Defines implicit functions that provide extra functionalities on RDDs of specific types.
For example, [RDD.rddToPairRDDFunctions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD$.html#rddToPairRDDFunctions\[K,V\]\(rdd:org.apache.spark.rdd.RDD\[\(K,V\)\]\)\(implicitkt:scala.reflect.ClassTag\[K\],implicitvt:scala.reflect.ClassTag\[V\],implicitord:Ordering\[K\]\):org.apache.spark.rdd.PairRDDFunctions\[K,V\]) converts an RDD into a [PairRDDFunctions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html "org.apache.spark.rdd.PairRDDFunctions") for key-value-pair RDDs, and enabling extra functionalities such as `PairRDDFunctions.reduceByKey`. 
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/UnionRDD$.html "Permalink") object [UnionRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/UnionRDD$.html) extends [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable")


### Ungrouped
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/AsyncRDDActions.html "Permalink") class [AsyncRDDActions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/AsyncRDDActions.html "A set of asynchronous RDD actions available through an implicit conversion.")[T] extends Serializable with Logging
A set of asynchronous RDD actions available through an implicit conversion.
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/CoGroupedRDD.html "Permalink") class [CoGroupedRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/CoGroupedRDD.html ":: DeveloperApi :: An RDD that cogroups its parents.")[K] extends [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, Array[Iterable[_]])]
An RDD that cogroups its parents.
An RDD that cogroups its parents. For each key k in parent RDDs, the resulting RDD contains a tuple with the list of values for that key.  

Annotations
     @DeveloperApi() 

Note
    
This is an internal API. We recommend users use RDD.cogroup(...) instead of instantiating this directly.
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/DoubleRDDFunctions.html "Permalink") class [DoubleRDDFunctions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/DoubleRDDFunctions.html "Extra functions available on RDDs of Doubles through an implicit conversion.") extends Logging with Serializable
Extra functions available on RDDs of Doubles through an implicit conversion.
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/HadoopRDD.html "Permalink") class [HadoopRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/HadoopRDD.html ":: DeveloperApi :: An RDD that provides core functionality for reading data stored in Hadoop \(e.g., files in HDFS, sources in HBase, or S3\), using the older MapReduce API \(org.apache.hadoop.mapred\).")[K, V] extends [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, V)] with Logging
An RDD that provides core functionality for reading data stored in Hadoop (e.g., files in HDFS, sources in HBase, or S3), using the older MapReduce API (`org.apache.hadoop.mapred`).
An RDD that provides core functionality for reading data stored in Hadoop (e.g., files in HDFS, sources in HBase, or S3), using the older MapReduce API (`org.apache.hadoop.mapred`).  

Annotations
     @DeveloperApi() 

Note
    
Instantiating this class directly is not recommended, please use `org.apache.spark.SparkContext.hadoopRDD()`
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/index.html#IsWritable\[A\]=A=>org.apache.hadoop.io.Writable "Permalink") type IsWritable[A] = (A) => Writable
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/NewHadoopRDD.html "Permalink") class [NewHadoopRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/NewHadoopRDD.html ":: DeveloperApi :: An RDD that provides core functionality for reading data stored in Hadoop \(e.g., files in HDFS, sources in HBase, or S3\), using the new MapReduce API \(org.apache.hadoop.mapreduce\).")[K, V] extends [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, V)] with Logging
An RDD that provides core functionality for reading data stored in Hadoop (e.g., files in HDFS, sources in HBase, or S3), using the new MapReduce API (`org.apache.hadoop.mapreduce`).
An RDD that provides core functionality for reading data stored in Hadoop (e.g., files in HDFS, sources in HBase, or S3), using the new MapReduce API (`org.apache.hadoop.mapreduce`).  

Annotations
     @DeveloperApi() 

Note
    
Instantiating this class directly is not recommended, please use `org.apache.spark.SparkContext.newAPIHadoopRDD()`
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/OrderedRDDFunctions.html "Permalink") class [OrderedRDDFunctions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/OrderedRDDFunctions.html "Extra functions available on RDDs of \(key, value\) pairs where the key is sortable through an implicit conversion.")[K, V, P <: Product2[K, V]] extends Logging with Serializable
Extra functions available on RDDs of (key, value) pairs where the key is sortable through an implicit conversion.
Extra functions available on RDDs of (key, value) pairs where the key is sortable through an implicit conversion. They will work with any key type `K` that has an implicit `Ordering[K]` in scope. Ordering objects already exist for all of the standard primitive types. Users can also define their own orderings for custom types, or to override the default ordering. The implicit ordering that is in the closest scope will be used.

```
import org.apache.spark.SparkContext._

val rdd: RDD[(String, Int)] = ...
implicit val caseInsensitiveOrdering = new Ordering[String] {
  override def compare(a: String, b: String) =
    a.toLowerCase(Locale.ROOT).compare(b.toLowerCase(Locale.ROOT))
}

// Sort by key, using the above case insensitive ordering.
rdd.sortByKey()
```

  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html "Permalink") class [PairRDDFunctions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html "Extra functions available on RDDs of \(key, value\) pairs through an implicit conversion.")[K, V] extends Logging with Serializable
Extra functions available on RDDs of (key, value) pairs through an implicit conversion.
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PartitionCoalescer.html "Permalink") trait [PartitionCoalescer](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PartitionCoalescer.html "::DeveloperApi:: A PartitionCoalescer defines how to coalesce the partitions of a given RDD.") extends AnyRef
::DeveloperApi:: A PartitionCoalescer defines how to coalesce the partitions of a given RDD.
::DeveloperApi:: A PartitionCoalescer defines how to coalesce the partitions of a given RDD.  

Annotations
     @DeveloperApi()
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PartitionGroup.html "Permalink") class [PartitionGroup](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PartitionGroup.html "::DeveloperApi:: A group of Partitions") extends AnyRef
::DeveloperApi:: A group of `Partition`s
::DeveloperApi:: A group of `Partition`s 

Annotations
     @DeveloperApi()
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PartitionPruningRDD.html "Permalink") class [PartitionPruningRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PartitionPruningRDD.html ":: DeveloperApi :: An RDD used to prune RDD partitions/partitions so we can avoid launching tasks on all partitions.")[T] extends [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[T]
An RDD used to prune RDD partitions/partitions so we can avoid launching tasks on all partitions.
An RDD used to prune RDD partitions/partitions so we can avoid launching tasks on all partitions. An example use case: If we know the RDD is partitioned by range, and the execution DAG has a filter on the key, we can avoid launching tasks on partitions that don't have the range covering the key.  

Annotations
     @DeveloperApi()
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "Permalink") abstract  class [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "A Resilient Distributed Dataset \(RDD\), the basic abstraction in Spark.")[T] extends Serializable with Logging
A Resilient Distributed Dataset (RDD), the basic abstraction in Spark.
A Resilient Distributed Dataset (RDD), the basic abstraction in Spark. Represents an immutable, partitioned collection of elements that can be operated on in parallel. This class contains the basic operations available on all RDDs, such as `map`, `filter`, and `persist`. In addition, [org.apache.spark.rdd.PairRDDFunctions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html "org.apache.spark.rdd.PairRDDFunctions") contains operations available only on RDDs of key-value pairs, such as `groupByKey` and `join`; [org.apache.spark.rdd.DoubleRDDFunctions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/DoubleRDDFunctions.html "org.apache.spark.rdd.DoubleRDDFunctions") contains operations available only on RDDs of Doubles; and [org.apache.spark.rdd.SequenceFileRDDFunctions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/SequenceFileRDDFunctions.html "org.apache.spark.rdd.SequenceFileRDDFunctions") contains operations available on RDDs that can be saved as SequenceFiles. All operations are automatically available on any RDD of the right type (e.g. RDD[(Int, Int)]) through implicit.
Internally, each RDD is characterized by five main properties:
     * A list of partitions
     * A function for computing each split
     * A list of dependencies on other RDDs
     * Optionally, a Partitioner for key-value RDDs (e.g. to say that the RDD is hash-partitioned)
     * Optionally, a list of preferred locations to compute each split on (e.g. block locations for an HDFS file)
All of the scheduling and execution in Spark is done based on these methods, allowing each RDD to implement its own way of computing itself. Indeed, users can implement custom RDDs (e.g. for reading data from a new storage system) by overriding these functions. Please refer to the [Spark paper](http://people.csail.mit.edu/matei/papers/2012/nsdi_spark.pdf) for more details on RDD internals. 
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDDBarrier.html "Permalink") class [RDDBarrier](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDDBarrier.html ":: Experimental :: Wraps an RDD in a barrier stage, which forces Spark to launch tasks of this stage together.")[T] extends AnyRef
Wraps an RDD in a barrier stage, which forces Spark to launch tasks of this stage together.
Wraps an RDD in a barrier stage, which forces Spark to launch tasks of this stage together. [org.apache.spark.rdd.RDDBarrier](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDDBarrier.html "org.apache.spark.rdd.RDDBarrier") instances are created by [org.apache.spark.rdd.RDD#barrier](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html#barrier\(\):org.apache.spark.rdd.RDDBarrier\[T\]).  

Annotations
     @Experimental() @Since("2.4.0")
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/SequenceFileRDDFunctions.html "Permalink") class [SequenceFileRDDFunctions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/SequenceFileRDDFunctions.html "Extra functions available on RDDs of \(key, value\) pairs to create a Hadoop SequenceFile, through an implicit conversion.")[K, V] extends Logging with Serializable
Extra functions available on RDDs of (key, value) pairs to create a Hadoop SequenceFile, through an implicit conversion.
Extra functions available on RDDs of (key, value) pairs to create a Hadoop SequenceFile, through an implicit conversion.  

Note
    
This can't be part of PairRDDFunctions because we need more implicit parameters to convert our keys and values to Writable.
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/ShuffledRDD.html "Permalink") class [ShuffledRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/ShuffledRDD.html ":: DeveloperApi :: The resulting RDD from a shuffle \(e.g.")[K, V, C] extends [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, C)]
The resulting RDD from a shuffle (e.g.
The resulting RDD from a shuffle (e.g. repartitioning of data). 

K
    
the key class. 

V
    
the value class. 

C
    
the combiner class. 

Annotations
     @DeveloperApi()
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/UnionRDD.html "Permalink") class [UnionRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/UnionRDD.html)[T] extends [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[T] 

Annotations
     @DeveloperApi()
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/JdbcRDD.html "Permalink") class [JdbcRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/JdbcRDD.html "An RDD that executes a SQL query on a JDBC connection and reads results.")[T] extends [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[T] with Logging
An RDD that executes a SQL query on a JDBC connection and reads results.
An RDD that executes a SQL query on a JDBC connection and reads results. For usage example, see test case JdbcRDDSuite.  

Annotations
     @deprecated 

Deprecated
    
_(Since version 4.1.0)_ Jdbc RDD is deprecated, consider using JDBC data source instead.


  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/DeterministicLevel$.html "Permalink") object [DeterministicLevel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/DeterministicLevel$.html "The deterministic level of RDD's output \(i.e.") extends Enumeration
The deterministic level of RDD's output (i.e.
The deterministic level of RDD's output (i.e. what `RDD#compute` returns). This explains how the output will diff when Spark reruns the tasks for the RDD. There are 3 deterministic levels: 1. DETERMINATE: The RDD output is always the same data set in the same order after a rerun. 2. UNORDERED: The RDD output is always the same data set but the order can be different after a rerun. 3. INDETERMINATE. The RDD output can be different after a rerun.
Note that, the output of an RDD usually relies on the parent RDDs. When the parent RDD's output is INDETERMINATE, it's very likely the RDD's output is also INDETERMINATE.  

Annotations
     @DeveloperApi()
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/JdbcRDD$.html "Permalink") object [JdbcRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/JdbcRDD$.html) extends [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable")
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PartitionPruningRDD$.html "Permalink") object [PartitionPruningRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PartitionPruningRDD$.html) extends [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable") 

Annotations
     @DeveloperApi()
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD$.html "Permalink") object [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD$.html "Defines implicit functions that provide extra functionalities on RDDs of specific types.") extends [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable")
Defines implicit functions that provide extra functionalities on RDDs of specific types.
Defines implicit functions that provide extra functionalities on RDDs of specific types.
For example, [RDD.rddToPairRDDFunctions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD$.html#rddToPairRDDFunctions\[K,V\]\(rdd:org.apache.spark.rdd.RDD\[\(K,V\)\]\)\(implicitkt:scala.reflect.ClassTag\[K\],implicitvt:scala.reflect.ClassTag\[V\],implicitord:Ordering\[K\]\):org.apache.spark.rdd.PairRDDFunctions\[K,V\]) converts an RDD into a [PairRDDFunctions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html "org.apache.spark.rdd.PairRDDFunctions") for key-value-pair RDDs, and enabling extra functionalities such as `PairRDDFunctions.reduceByKey`. 
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/UnionRDD$.html "Permalink") object [UnionRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/UnionRDD$.html) extends [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable")


