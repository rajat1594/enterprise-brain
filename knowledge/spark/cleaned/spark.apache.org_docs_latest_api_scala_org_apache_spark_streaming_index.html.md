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
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/index.html "Permalink") package streaming
Spark Streaming functionality.
Spark Streaming functionality. [org.apache.spark.streaming.StreamingContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html "org.apache.spark.streaming.StreamingContext") serves as the main entry point to Spark Streaming, while [org.apache.spark.streaming.dstream.DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream") is the data type representing a continuous sequence of RDDs, representing a continuous stream of data.
In addition, [org.apache.spark.streaming.dstream.PairDStreamFunctions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html "org.apache.spark.streaming.dstream.PairDStreamFunctions") contains operations available only on DStreams of key-value pairs, such as `groupByKey` and `reduceByKey`. These operations are automatically available on any DStream of the right type (e.g. DStream[(Int, Int)] through implicit conversions.
For the Java API of Spark Streaming, take a look at the [org.apache.spark.streaming.api.java.JavaStreamingContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html "org.apache.spark.streaming.api.java.JavaStreamingContext") which serves as the entry point, and the [org.apache.spark.streaming.api.java.JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream") and the [org.apache.spark.streaming.api.java.JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream") which have the DStream functionality.

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/index.html "Permalink") package [api](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/index.html)
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/index.html "Permalink") package [dstream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/index.html "Various implementations of DStream's.")
Various implementations of DStream's.
Various implementations of DStream's.

See also

[org.apache.spark.streaming.dstream.DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/kinesis/index.html "Permalink") package [kinesis](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/kinesis/index.html)
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/index.html "Permalink") package [receiver](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/index.html)
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/index.html "Permalink") package [scheduler](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/index.html)
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/util/index.html "Permalink") package [util](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/util/index.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html)[Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Durations$.html)[Durations](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Durations$.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Milliseconds$.html "Helper object that creates instance of org.apache.spark.streaming.Duration representing a given number of milliseconds.")[Milliseconds](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Milliseconds$.html "Helper object that creates instance of org.apache.spark.streaming.Duration representing a given number of milliseconds.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Minutes$.html "Helper object that creates instance of org.apache.spark.streaming.Duration representing a given number of minutes.")[Minutes](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Minutes$.html "Helper object that creates instance of org.apache.spark.streaming.Duration representing a given number of minutes.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Seconds$.html "Helper object that creates instance of org.apache.spark.streaming.Duration representing a given number of seconds.")[Seconds](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Seconds$.html "Helper object that creates instance of org.apache.spark.streaming.Duration representing a given number of seconds.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/State.html ":: Experimental :: Abstract class for getting and updating the state in mapping function used in the mapWithState operation of a pair DStream \(Scala\) or a JavaPairDStream \(Java\).")[State](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/State.html ":: Experimental :: Abstract class for getting and updating the state in mapping function used in the mapWithState operation of a pair DStream \(Scala\) or a JavaPairDStream \(Java\).")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StateSpec$.html ":: Experimental :: Builder object for creating instances of org.apache.spark.streaming.StateSpec that is used for specifying the parameters of the DStream transformation mapWithState that is used for specifying the parameters of the DStream transformation mapWithState operation of a pair DStream \(Scala\) or a JavaPairDStream \(Java\).") [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StateSpec.html ":: Experimental :: Abstract class representing all the specifications of the DStream transformation mapWithState operation of a pair DStream \(Scala\) or a JavaPairDStream \(Java\).")[StateSpec](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StateSpec.html ":: Experimental :: Abstract class representing all the specifications of the DStream transformation mapWithState operation of a pair DStream \(Scala\) or a JavaPairDStream \(Java\).")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingConf$.html)[StreamingConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingConf$.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext$.html "StreamingContext object contains a number of utility functions related to the StreamingContext class.") [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html "Main entry point for Spark Streaming functionality.")[StreamingContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html "Main entry point for Spark Streaming functionality.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContextState.html ":: DeveloperApi ::")[StreamingContextState](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContextState.html ":: DeveloperApi ::")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time$.html) [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "This is a simple class that represents an absolute instant of time.")[Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "This is a simple class that represents an absolute instant of time.")
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
# streaming[ __](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/index.html "Permalink")
####  package streaming
Spark Streaming functionality. [org.apache.spark.streaming.StreamingContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html "org.apache.spark.streaming.StreamingContext") serves as the main entry point to Spark Streaming, while [org.apache.spark.streaming.dstream.DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream") is the data type representing a continuous sequence of RDDs, representing a continuous stream of data.
In addition, [org.apache.spark.streaming.dstream.PairDStreamFunctions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html "org.apache.spark.streaming.dstream.PairDStreamFunctions") contains operations available only on DStreams of key-value pairs, such as `groupByKey` and `reduceByKey`. These operations are automatically available on any DStream of the right type (e.g. DStream[(Int, Int)] through implicit conversions.
For the Java API of Spark Streaming, take a look at the [org.apache.spark.streaming.api.java.JavaStreamingContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html "org.apache.spark.streaming.api.java.JavaStreamingContext") which serves as the entry point, and the [org.apache.spark.streaming.api.java.JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream") and the [org.apache.spark.streaming.api.java.JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream") which have the DStream functionality.

Source
    [package.scala](https://github.com/apache/spark/tree/v4.1.2/streaming/src/main/scala/org/apache/spark/streaming/package.scala)
Linear Supertypes
AnyRef, Any
__ __
Ordering
  1. Alphabetic
  2. By Inheritance

Inherited

  1. streaming
  2. AnyRef
  3. Any

  1. Hide All
  2. Show All

Visibility
  1. Public
  2. Protected

### Package Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/index.html "Permalink") package [api](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/index.html)
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/index.html "Permalink") package [dstream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/index.html "Various implementations of DStream's.")
Various implementations of DStream's.
Various implementations of DStream's.

See also

[org.apache.spark.streaming.dstream.DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/kinesis/index.html "Permalink") package [kinesis](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/kinesis/index.html)
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/index.html "Permalink") package [receiver](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/index.html)
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/index.html "Permalink") package [scheduler](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/index.html)
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/util/index.html "Permalink") package [util](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/util/index.html)

### Type Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "Permalink") case class [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html)(millis: Long) extends Product with Serializable
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/State.html "Permalink") sealed abstract  class [State](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/State.html ":: Experimental :: Abstract class for getting and updating the state in mapping function used in the mapWithState operation of a pair DStream \(Scala\) or a JavaPairDStream \(Java\).")[S] extends AnyRef
Abstract class for getting and updating the state in mapping function used in the `mapWithState` operation of a [pair DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html "org.apache.spark.streaming.dstream.PairDStreamFunctions") (Scala) or a [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream") (Java).
Abstract class for getting and updating the state in mapping function used in the `mapWithState` operation of a [pair DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html "org.apache.spark.streaming.dstream.PairDStreamFunctions") (Scala) or a [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream") (Java).
Scala example of using `State`:

```
// A mapping function that maintains an integer state and returns a String
def mappingFunction(key: String, value: Option[Int], state: State[Int]): Option[String] = {
  // Check if state exists
  if (state.exists) {
    val existingState = state.get  // Get the existing state
    val shouldRemove = ...         // Decide whether to remove the state
    if (shouldRemove) {
      state.remove()     // Remove the state
    } else {
      val newState = ...
      state.update(newState)    // Set the new state
    }
  } else {
    val initialState = ...
    state.update(initialState)  // Set the initial state
  }
  ... // return something
}
```

Java example of using `State`:

```
// A mapping function that maintains an integer state and returns a String
Function3<String, Optional<Integer>, State<Integer>, String> mappingFunction =
   new Function3<String, Optional<Integer>, State<Integer>, String>() {

     @Override
     public String call(String key, Optional<Integer> value, State<Integer> state) {
       if (state.exists()) {
         int existingState = state.get(); // Get the existing state
         boolean shouldRemove = ...; // Decide whether to remove the state
         if (shouldRemove) {
           state.remove(); // Remove the state
         } else {
           int newState = ...;
           state.update(newState); // Set the new state
         }
       } else {
         int initialState = ...; // Set the initial state
         state.update(initialState);
       }
       // return something
     }
   };
```

S

Class of the state

Annotations
     @Experimental()
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StateSpec.html "Permalink") sealed abstract  class [StateSpec](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StateSpec.html ":: Experimental :: Abstract class representing all the specifications of the DStream transformation mapWithState operation of a pair DStream \(Scala\) or a JavaPairDStream \(Java\).")[KeyType, ValueType, StateType, MappedType] extends Serializable
Abstract class representing all the specifications of the DStream transformation `mapWithState` operation of a [pair DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html "org.apache.spark.streaming.dstream.PairDStreamFunctions") (Scala) or a [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream") (Java).
Abstract class representing all the specifications of the DStream transformation `mapWithState` operation of a [pair DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html "org.apache.spark.streaming.dstream.PairDStreamFunctions") (Scala) or a [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream") (Java). Use `org.apache.spark.streaming.StateSpec.function()` factory methods to create instances of this class.
Example in Scala:

```
// A mapping function that maintains an integer state and return a String
def mappingFunction(key: String, value: Option[Int], state: State[Int]): Option[String] = {
  // Use state.exists(), state.get(), state.update() and state.remove()
  // to manage state, and return the necessary string
}

val spec = StateSpec.function(mappingFunction).numPartitions(10)

val mapWithStateDStream = keyValueDStream.mapWithState[StateType, MappedType](spec)
```

Example in Java:

```
// A mapping function that maintains an integer state and return a string
Function3<String, Optional<Integer>, State<Integer>, String> mappingFunction =
    new Function3<String, Optional<Integer>, State<Integer>, String>() {
        @Override
        public Optional<String> call(Optional<Integer> value, State<Integer> state) {
            // Use state.exists(), state.get(), state.update() and state.remove()
            // to manage state, and return the necessary string
        }
    };

 JavaMapWithStateDStream<String, Integer, Integer, String> mapWithStateDStream =
     keyValueDStream.mapWithState(StateSpec.function(mappingFunc));
```

KeyType

Class of the state key

ValueType

Class of the state value

StateType

Class of the state data

MappedType

Class of the mapped elements

Annotations
     @Experimental()
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContextState.html "Permalink") sealed final  class [StreamingContextState](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContextState.html ":: DeveloperApi ::") extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#java.lang.Enum "java.lang.Enum")[[StreamingContextState](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContextState.html "org.apache.spark.streaming.StreamingContextState")]
Represents the state of a StreamingContext.

Annotations
     @DeveloperApi()
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "Permalink") case class [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "This is a simple class that represents an absolute instant of time.")(millis: Long) extends Product with Serializable
This is a simple class that represents an absolute instant of time.
This is a simple class that represents an absolute instant of time. Internally, it represents time as the difference, measured in milliseconds, between the current time and midnight, January 1, 1970 UTC. This is the same format as what is returned by System.currentTimeMillis.

### Deprecated Type Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html "Permalink") class [StreamingContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html "Main entry point for Spark Streaming functionality.") extends Logging
Main entry point for Spark Streaming functionality.
Main entry point for Spark Streaming functionality. It provides methods used to create [org.apache.spark.streaming.dstream.DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")s from various input sources. It can be either created by providing a Spark master URL and an appName, or from a org.apache.spark.SparkConf configuration (see core Spark documentation), or from an existing org.apache.spark.SparkContext. The associated SparkContext can be accessed using `context.sparkContext`. After creating and transforming DStreams, the streaming computation can be started and stopped using `context.start()` and `context.stop()`, respectively. `context.awaitTermination()` allows the current thread to wait for the termination of the context by `stop()` or by an exception.

Annotations
     @deprecated

Deprecated

_(Since version Spark 3.4.0)_ DStream is deprecated. Migrate to Structured Streaming.

### Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Durations$.html "Permalink") object [Durations](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Durations$.html)
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Milliseconds$.html "Permalink") object [Milliseconds](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Milliseconds$.html "Helper object that creates instance of org.apache.spark.streaming.Duration representing a given number of milliseconds.")
Helper object that creates instance of [org.apache.spark.streaming.Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration") representing a given number of milliseconds.
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Minutes$.html "Permalink") object [Minutes](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Minutes$.html "Helper object that creates instance of org.apache.spark.streaming.Duration representing a given number of minutes.")
Helper object that creates instance of [org.apache.spark.streaming.Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration") representing a given number of minutes.
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Seconds$.html "Permalink") object [Seconds](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Seconds$.html "Helper object that creates instance of org.apache.spark.streaming.Duration representing a given number of seconds.")
Helper object that creates instance of [org.apache.spark.streaming.Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration") representing a given number of seconds.
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StateSpec$.html "Permalink") object [StateSpec](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StateSpec$.html ":: Experimental :: Builder object for creating instances of org.apache.spark.streaming.StateSpec that is used for specifying the parameters of the DStream transformation mapWithState that is used for specifying the parameters of the DStream transformation mapWithState operation of a pair DStream \(Scala\) or a JavaPairDStream \(Java\).") extends [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable")
Builder object for creating instances of `org.apache.spark.streaming.StateSpec` that is used for specifying the parameters of the DStream transformation `mapWithState` that is used for specifying the parameters of the DStream transformation `mapWithState` operation of a [pair DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html "org.apache.spark.streaming.dstream.PairDStreamFunctions") (Scala) or a [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream") (Java).
Builder object for creating instances of `org.apache.spark.streaming.StateSpec` that is used for specifying the parameters of the DStream transformation `mapWithState` that is used for specifying the parameters of the DStream transformation `mapWithState` operation of a [pair DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html "org.apache.spark.streaming.dstream.PairDStreamFunctions") (Scala) or a [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream") (Java).
Example in Scala:

```
// A mapping function that maintains an integer state and return a String
def mappingFunction(key: String, value: Option[Int], state: State[Int]): Option[String] = {
  // Use state.exists(), state.get(), state.update() and state.remove()
  // to manage state, and return the necessary string
}

val spec = StateSpec.function(mappingFunction).numPartitions(10)

val mapWithStateDStream = keyValueDStream.mapWithState[StateType, MappedType](spec)
```

Example in Java:

```
// A mapping function that maintains an integer state and return a string
Function3<String, Optional<Integer>, State<Integer>, String> mappingFunction =
    new Function3<String, Optional<Integer>, State<Integer>, String>() {
        @Override
        public Optional<String> call(Optional<Integer> value, State<Integer> state) {
            // Use state.exists(), state.get(), state.update() and state.remove()
            // to manage state, and return the necessary string
        }
    };

 JavaMapWithStateDStream<String, Integer, Integer, String> mapWithStateDStream =
     keyValueDStream.mapWithState(StateSpec.function(mappingFunc));
```

Annotations
     @Experimental()
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingConf$.html "Permalink") object [StreamingConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingConf$.html)
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time$.html "Permalink") object [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time$.html) extends [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable")

### Deprecated Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext$.html "Permalink") object [StreamingContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext$.html "StreamingContext object contains a number of utility functions related to the StreamingContext class.") extends Logging
StreamingContext object contains a number of utility functions related to the StreamingContext class.
StreamingContext object contains a number of utility functions related to the StreamingContext class.

Annotations
     @deprecated

Deprecated

_(Since version Spark 3.4.0)_ DStream is deprecated. Migrate to Structured Streaming.

### Ungrouped
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "Permalink") case class [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html)(millis: Long) extends Product with Serializable
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/State.html "Permalink") sealed abstract  class [State](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/State.html ":: Experimental :: Abstract class for getting and updating the state in mapping function used in the mapWithState operation of a pair DStream \(Scala\) or a JavaPairDStream \(Java\).")[S] extends AnyRef
Abstract class for getting and updating the state in mapping function used in the `mapWithState` operation of a [pair DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html "org.apache.spark.streaming.dstream.PairDStreamFunctions") (Scala) or a [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream") (Java).
Abstract class for getting and updating the state in mapping function used in the `mapWithState` operation of a [pair DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html "org.apache.spark.streaming.dstream.PairDStreamFunctions") (Scala) or a [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream") (Java).
Scala example of using `State`:

```
// A mapping function that maintains an integer state and returns a String
def mappingFunction(key: String, value: Option[Int], state: State[Int]): Option[String] = {
  // Check if state exists
  if (state.exists) {
    val existingState = state.get  // Get the existing state
    val shouldRemove = ...         // Decide whether to remove the state
    if (shouldRemove) {
      state.remove()     // Remove the state
    } else {
      val newState = ...
      state.update(newState)    // Set the new state
    }
  } else {
    val initialState = ...
    state.update(initialState)  // Set the initial state
  }
  ... // return something
}
```

Java example of using `State`:

```
// A mapping function that maintains an integer state and returns a String
Function3<String, Optional<Integer>, State<Integer>, String> mappingFunction =
   new Function3<String, Optional<Integer>, State<Integer>, String>() {

     @Override
     public String call(String key, Optional<Integer> value, State<Integer> state) {
       if (state.exists()) {
         int existingState = state.get(); // Get the existing state
         boolean shouldRemove = ...; // Decide whether to remove the state
         if (shouldRemove) {
           state.remove(); // Remove the state
         } else {
           int newState = ...;
           state.update(newState); // Set the new state
         }
       } else {
         int initialState = ...; // Set the initial state
         state.update(initialState);
       }
       // return something
     }
   };
```

S

Class of the state

Annotations
     @Experimental()
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StateSpec.html "Permalink") sealed abstract  class [StateSpec](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StateSpec.html ":: Experimental :: Abstract class representing all the specifications of the DStream transformation mapWithState operation of a pair DStream \(Scala\) or a JavaPairDStream \(Java\).")[KeyType, ValueType, StateType, MappedType] extends Serializable
Abstract class representing all the specifications of the DStream transformation `mapWithState` operation of a [pair DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html "org.apache.spark.streaming.dstream.PairDStreamFunctions") (Scala) or a [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream") (Java).
Abstract class representing all the specifications of the DStream transformation `mapWithState` operation of a [pair DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html "org.apache.spark.streaming.dstream.PairDStreamFunctions") (Scala) or a [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream") (Java). Use `org.apache.spark.streaming.StateSpec.function()` factory methods to create instances of this class.
Example in Scala:

```
// A mapping function that maintains an integer state and return a String
def mappingFunction(key: String, value: Option[Int], state: State[Int]): Option[String] = {
  // Use state.exists(), state.get(), state.update() and state.remove()
  // to manage state, and return the necessary string
}

val spec = StateSpec.function(mappingFunction).numPartitions(10)

val mapWithStateDStream = keyValueDStream.mapWithState[StateType, MappedType](spec)
```

Example in Java:

```
// A mapping function that maintains an integer state and return a string
Function3<String, Optional<Integer>, State<Integer>, String> mappingFunction =
    new Function3<String, Optional<Integer>, State<Integer>, String>() {
        @Override
        public Optional<String> call(Optional<Integer> value, State<Integer> state) {
            // Use state.exists(), state.get(), state.update() and state.remove()
            // to manage state, and return the necessary string
        }
    };

 JavaMapWithStateDStream<String, Integer, Integer, String> mapWithStateDStream =
     keyValueDStream.mapWithState(StateSpec.function(mappingFunc));
```

KeyType

Class of the state key

ValueType

Class of the state value

StateType

Class of the state data

MappedType

Class of the mapped elements

Annotations
     @Experimental()
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContextState.html "Permalink") sealed final  class [StreamingContextState](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContextState.html ":: DeveloperApi ::") extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#java.lang.Enum "java.lang.Enum")[[StreamingContextState](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContextState.html "org.apache.spark.streaming.StreamingContextState")]
Represents the state of a StreamingContext.

Annotations
     @DeveloperApi()
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "Permalink") case class [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "This is a simple class that represents an absolute instant of time.")(millis: Long) extends Product with Serializable
This is a simple class that represents an absolute instant of time.
This is a simple class that represents an absolute instant of time. Internally, it represents time as the difference, measured in milliseconds, between the current time and midnight, January 1, 1970 UTC. This is the same format as what is returned by System.currentTimeMillis.
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html "Permalink") class [StreamingContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html "Main entry point for Spark Streaming functionality.") extends Logging
Main entry point for Spark Streaming functionality.
Main entry point for Spark Streaming functionality. It provides methods used to create [org.apache.spark.streaming.dstream.DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")s from various input sources. It can be either created by providing a Spark master URL and an appName, or from a org.apache.spark.SparkConf configuration (see core Spark documentation), or from an existing org.apache.spark.SparkContext. The associated SparkContext can be accessed using `context.sparkContext`. After creating and transforming DStreams, the streaming computation can be started and stopped using `context.start()` and `context.stop()`, respectively. `context.awaitTermination()` allows the current thread to wait for the termination of the context by `stop()` or by an exception.

Annotations
     @deprecated

Deprecated

_(Since version Spark 3.4.0)_ DStream is deprecated. Migrate to Structured Streaming.

  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Durations$.html "Permalink") object [Durations](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Durations$.html)
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Milliseconds$.html "Permalink") object [Milliseconds](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Milliseconds$.html "Helper object that creates instance of org.apache.spark.streaming.Duration representing a given number of milliseconds.")
Helper object that creates instance of [org.apache.spark.streaming.Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration") representing a given number of milliseconds.
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Minutes$.html "Permalink") object [Minutes](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Minutes$.html "Helper object that creates instance of org.apache.spark.streaming.Duration representing a given number of minutes.")
Helper object that creates instance of [org.apache.spark.streaming.Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration") representing a given number of minutes.
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Seconds$.html "Permalink") object [Seconds](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Seconds$.html "Helper object that creates instance of org.apache.spark.streaming.Duration representing a given number of seconds.")
Helper object that creates instance of [org.apache.spark.streaming.Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration") representing a given number of seconds.
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StateSpec$.html "Permalink") object [StateSpec](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StateSpec$.html ":: Experimental :: Builder object for creating instances of org.apache.spark.streaming.StateSpec that is used for specifying the parameters of the DStream transformation mapWithState that is used for specifying the parameters of the DStream transformation mapWithState operation of a pair DStream \(Scala\) or a JavaPairDStream \(Java\).") extends [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable")
Builder object for creating instances of `org.apache.spark.streaming.StateSpec` that is used for specifying the parameters of the DStream transformation `mapWithState` that is used for specifying the parameters of the DStream transformation `mapWithState` operation of a [pair DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html "org.apache.spark.streaming.dstream.PairDStreamFunctions") (Scala) or a [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream") (Java).
Builder object for creating instances of `org.apache.spark.streaming.StateSpec` that is used for specifying the parameters of the DStream transformation `mapWithState` that is used for specifying the parameters of the DStream transformation `mapWithState` operation of a [pair DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html "org.apache.spark.streaming.dstream.PairDStreamFunctions") (Scala) or a [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream") (Java).
Example in Scala:

```
// A mapping function that maintains an integer state and return a String
def mappingFunction(key: String, value: Option[Int], state: State[Int]): Option[String] = {
  // Use state.exists(), state.get(), state.update() and state.remove()
  // to manage state, and return the necessary string
}

val spec = StateSpec.function(mappingFunction).numPartitions(10)

val mapWithStateDStream = keyValueDStream.mapWithState[StateType, MappedType](spec)
```

Example in Java:

```
// A mapping function that maintains an integer state and return a string
Function3<String, Optional<Integer>, State<Integer>, String> mappingFunction =
    new Function3<String, Optional<Integer>, State<Integer>, String>() {
        @Override
        public Optional<String> call(Optional<Integer> value, State<Integer> state) {
            // Use state.exists(), state.get(), state.update() and state.remove()
            // to manage state, and return the necessary string
        }
    };

 JavaMapWithStateDStream<String, Integer, Integer, String> mapWithStateDStream =
     keyValueDStream.mapWithState(StateSpec.function(mappingFunc));
```

Annotations
     @Experimental()
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingConf$.html "Permalink") object [StreamingConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingConf$.html)
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time$.html "Permalink") object [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time$.html) extends [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable")
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext$.html "Permalink") object [StreamingContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext$.html "StreamingContext object contains a number of utility functions related to the StreamingContext class.") extends Logging
StreamingContext object contains a number of utility functions related to the StreamingContext class.
StreamingContext object contains a number of utility functions related to the StreamingContext class.

Annotations
     @deprecated

Deprecated

_(Since version Spark 3.4.0)_ DStream is deprecated. Migrate to Structured Streaming.
