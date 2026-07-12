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
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/index.html "Permalink") package util
Spark utilities.
Spark utilities.

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/random/index.html "Permalink") package [random](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/random/index.html "Utilities for random number generation.")
Utilities for random number generation.
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/sketch/index.html "Permalink") package [sketch](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/sketch/index.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html "The base class for accumulators, that can accumulate inputs of type IN, and produce output of type OUT.")[AccumulatorV2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html "The base class for accumulators, that can accumulate inputs of type IN, and produce output of type OUT.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/ChildFirstURLClassLoader.html "A mutable class loader that gives preference to its own URLs over the parent class loader when loading classes and resources.")[ChildFirstURLClassLoader](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/ChildFirstURLClassLoader.html "A mutable class loader that gives preference to its own URLs over the parent class loader when loading classes and resources.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/CollectionAccumulator.html "An accumulator for collecting a list of elements.")[CollectionAccumulator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/CollectionAccumulator.html "An accumulator for collecting a list of elements.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/DoubleAccumulator.html "An accumulator for computing sum, count, and averages for double precision floating numbers.")[DoubleAccumulator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/DoubleAccumulator.html "An accumulator for computing sum, count, and averages for double precision floating numbers.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/EnumUtil.html)[EnumUtil](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/EnumUtil.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/ExposedBufferByteArrayOutputStream.html "Subclass of ByteArrayOutputStream that exposes buf directly.")[ExposedBufferByteArrayOutputStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/ExposedBufferByteArrayOutputStream.html "Subclass of ByteArrayOutputStream that exposes buf directly.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/LexicalThreadLocal.html "Helper trait for defining thread locals with lexical scoping.")[LexicalThreadLocal](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/LexicalThreadLocal.html "Helper trait for defining thread locals with lexical scoping.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/LogUtils$.html ":: : DeveloperApi :: Utils for querying Spark logs with Spark SQL.")[LogUtils](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/LogUtils$.html ":: : DeveloperApi :: Utils for querying Spark logs with Spark SQL.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/LongAccumulator.html "An accumulator for computing sum, count, and average of 64-bit integers.")[LongAccumulator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/LongAccumulator.html "An accumulator for computing sum, count, and average of 64-bit integers.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/MutablePair.html ":: DeveloperApi :: A tuple of 2 elements.")[MutablePair](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/MutablePair.html ":: DeveloperApi :: A tuple of 2 elements.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/MutableURLClassLoader.html "URL class loader that exposes the addURL method in URLClassLoader.")[MutableURLClassLoader](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/MutableURLClassLoader.html "URL class loader that exposes the addURL method in URLClassLoader.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/Pair.html "An immutable pair of values.")[Pair](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/Pair.html "An immutable pair of values.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/ParentClassLoader.html "A class loader which makes some protected methods in ClassLoader accessible.")[ParentClassLoader](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/ParentClassLoader.html "A class loader which makes some protected methods in ClassLoader accessible.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/SerializableConfiguration.html "Hadoop configuration but serializable.")[SerializableConfiguration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/SerializableConfiguration.html "Hadoop configuration but serializable.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/SizeEstimator$.html ":: DeveloperApi :: Estimates the sizes of Java objects \(number of bytes of memory they occupy\), for use in memory-aware caches.")[SizeEstimator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/SizeEstimator$.html ":: DeveloperApi :: Estimates the sizes of Java objects \(number of bytes of memory they occupy\), for use in memory-aware caches.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/SparkEnvUtils$.html)[SparkEnvUtils](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/SparkEnvUtils$.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/SparkSystemUtils$.html)[SparkSystemUtils](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/SparkSystemUtils$.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/StatCounter$.html) [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/StatCounter.html "A class for tracking the statistics of a set of numbers \(count, mean and variance\) in a numerically robust way.")[StatCounter](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/StatCounter.html "A class for tracking the statistics of a set of numbers \(count, mean and variance\) in a numerically robust way.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/TaskCompletionListener.html ":: DeveloperApi ::")[TaskCompletionListener](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/TaskCompletionListener.html ":: DeveloperApi ::")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/TaskFailureListener.html ":: DeveloperApi ::")[TaskFailureListener](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/TaskFailureListener.html ":: DeveloperApi ::")

p
[org](https://spark.apache.org/docs/latest/api/scala/org/index.html "org").[apache](https://spark.apache.org/docs/latest/api/scala/org/apache/index.html "org.apache").[spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
# util[ __](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/index.html "Permalink")
####  package util
Spark utilities.

Source
    [package.scala](https://github.com/apache/spark/tree/v4.1.2/core/src/main/scala/org/apache/spark/util/package.scala)
Linear Supertypes
AnyRef, Any
__ __
Ordering
  1. Alphabetic
  2. By Inheritance

Inherited

  1. util
  2. AnyRef
  3. Any

  1. Hide All
  2. Show All

Visibility
  1. Public
  2. Protected

### Package Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/random/index.html "Permalink") package [random](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/random/index.html "Utilities for random number generation.")
Utilities for random number generation.
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/sketch/index.html "Permalink") package [sketch](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/sketch/index.html)

### Type Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html "Permalink") abstract  class [AccumulatorV2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html "The base class for accumulators, that can accumulate inputs of type IN, and produce output of type OUT.")[IN, OUT] extends Serializable
The base class for accumulators, that can accumulate inputs of type `IN`, and produce output of type `OUT`.
The base class for accumulators, that can accumulate inputs of type `IN`, and produce output of type `OUT`.
`OUT` should be a type that can be read atomically (e.g., Int, Long), or thread-safely (e.g., synchronized collections) because it will be read from other threads.
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/ChildFirstURLClassLoader.html "Permalink") class [ChildFirstURLClassLoader](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/ChildFirstURLClassLoader.html "A mutable class loader that gives preference to its own URLs over the parent class loader when loading classes and resources.") extends [MutableURLClassLoader](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/MutableURLClassLoader.html "org.apache.spark.util.MutableURLClassLoader")
A mutable class loader that gives preference to its own URLs over the parent class loader when loading classes and resources.
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/CollectionAccumulator.html "Permalink") class [CollectionAccumulator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/CollectionAccumulator.html "An accumulator for collecting a list of elements.")[T] extends [AccumulatorV2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html "org.apache.spark.util.AccumulatorV2")[T, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#java.util.List "java.util.List")[T]]
An [accumulator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html "org.apache.spark.util.AccumulatorV2") for collecting a list of elements.
An [accumulator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html "org.apache.spark.util.AccumulatorV2") for collecting a list of elements.

Since

2.0.0
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/DoubleAccumulator.html "Permalink") class [DoubleAccumulator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/DoubleAccumulator.html "An accumulator for computing sum, count, and averages for double precision floating numbers.") extends [AccumulatorV2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html "org.apache.spark.util.AccumulatorV2")[[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html#java.lang.Double "java.lang.Double"), [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html#java.lang.Double "java.lang.Double")]
An [accumulator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html "org.apache.spark.util.AccumulatorV2") for computing sum, count, and averages for double precision floating numbers.
An [accumulator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html "org.apache.spark.util.AccumulatorV2") for computing sum, count, and averages for double precision floating numbers.

Since

2.0.0
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/EnumUtil.html "Permalink") class [EnumUtil](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/EnumUtil.html) extends AnyRef

Annotations
     @Private()
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/ExposedBufferByteArrayOutputStream.html "Permalink") final  class [ExposedBufferByteArrayOutputStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/ExposedBufferByteArrayOutputStream.html "Subclass of ByteArrayOutputStream that exposes buf directly.") extends [ByteArrayOutputStream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/ByteArrayOutputStream.html#java.io.ByteArrayOutputStream "java.io.ByteArrayOutputStream")
Subclass of ByteArrayOutputStream that exposes `buf` directly.
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/LexicalThreadLocal.html "Permalink") trait [LexicalThreadLocal](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/LexicalThreadLocal.html "Helper trait for defining thread locals with lexical scoping.")[T] extends AnyRef
Helper trait for defining thread locals with lexical scoping.
Helper trait for defining thread locals with lexical scoping. With this helper, the thread local is private and can only be set by the [Handle](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/LexicalThreadLocal$Handle.html "org.apache.spark.util.LexicalThreadLocal.Handle"). The [Handle](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/LexicalThreadLocal$Handle.html "org.apache.spark.util.LexicalThreadLocal.Handle") only exposes the thread local value to functions passed into its runWith method. This pattern allows for the lifetime of the thread local value to be strictly controlled.
Rather than calling `tl.set(...)` and `tl.remove()` you would get a handle and execute your code in `handle.runWith { ... }`.
Example:

```
object Credentials extends LexicalThreadLocal[Int] {
  def create(creds: Map[String, String]) = new Handle(Some(creds))
}
...
val handle = Credentials.create(Map("key" -> "value"))
assert(Credentials.get() == None)
handle.runWith {
  assert(Credentials.get() == Some(Map("key" -> "value")))
}
```

  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/LongAccumulator.html "Permalink") class [LongAccumulator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/LongAccumulator.html "An accumulator for computing sum, count, and average of 64-bit integers.") extends [AccumulatorV2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html "org.apache.spark.util.AccumulatorV2")[[Long](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html#java.lang.Long "java.lang.Long"), [Long](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html#java.lang.Long "java.lang.Long")]
An [accumulator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html "org.apache.spark.util.AccumulatorV2") for computing sum, count, and average of 64-bit integers.
An [accumulator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html "org.apache.spark.util.AccumulatorV2") for computing sum, count, and average of 64-bit integers.

Since

2.0.0
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/MutablePair.html "Permalink") case class [MutablePair](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/MutablePair.html ":: DeveloperApi :: A tuple of 2 elements.")[T1, T2](_1: T1, _2: T2) extends Product2[T1, T2] with Product with Serializable
A tuple of 2 elements.
A tuple of 2 elements. This can be used as an alternative to Scala's Tuple2 when we want to minimize object allocation.

_1

Element 1 of this MutablePair

_2

Element 2 of this MutablePair

Annotations
     @DeveloperApi()
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/MutableURLClassLoader.html "Permalink") class [MutableURLClassLoader](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/MutableURLClassLoader.html "URL class loader that exposes the addURL method in URLClassLoader.") extends [URLClassLoader](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URLClassLoader.html#java.net.URLClassLoader "java.net.URLClassLoader")
URL class loader that exposes the `addURL` method in URLClassLoader.
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/Pair.html "Permalink") final  class [Pair](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/Pair.html "An immutable pair of values.")[L, R] extends [Record](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Record.html#java.lang.Record "java.lang.Record")
An immutable pair of values.
An immutable pair of values. Note that the fields are intentionally designed to be `getLeft` and `getRight` instead of `left` and `right` in order to mitigate the migration burden from `org.apache.commons.lang3.tuple.Pair`.
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/ParentClassLoader.html "Permalink") class [ParentClassLoader](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/ParentClassLoader.html "A class loader which makes some protected methods in ClassLoader accessible.") extends [ClassLoader](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ClassLoader.html#java.lang.ClassLoader "java.lang.ClassLoader")
A class loader which makes some protected methods in ClassLoader accessible.
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/SerializableConfiguration.html "Permalink") class [SerializableConfiguration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/SerializableConfiguration.html "Hadoop configuration but serializable.") extends Serializable
Hadoop configuration but serializable.
Hadoop configuration but serializable. Use `value` to access the Hadoop configuration.

Annotations
     @DeveloperApi() @Unstable()
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/StatCounter.html "Permalink") class [StatCounter](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/StatCounter.html "A class for tracking the statistics of a set of numbers \(count, mean and variance\) in a numerically robust way.") extends Serializable
A class for tracking the statistics of a set of numbers (count, mean and variance) in a numerically robust way.
A class for tracking the statistics of a set of numbers (count, mean and variance) in a numerically robust way. Includes support for merging two StatCounters. Based on Welford and Chan's [ algorithms](http://en.wikipedia.org/wiki/Algorithms_for_calculating_variance) for running variance.
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/TaskCompletionListener.html "Permalink") trait [TaskCompletionListener](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/TaskCompletionListener.html ":: DeveloperApi ::") extends [EventListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EventListener.html#java.util.EventListener "java.util.EventListener")
Listener providing a callback function to invoke when a task's execution completes.

Annotations
     @DeveloperApi()
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/TaskFailureListener.html "Permalink") trait [TaskFailureListener](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/TaskFailureListener.html ":: DeveloperApi ::") extends [EventListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EventListener.html#java.util.EventListener "java.util.EventListener")
Listener providing a callback function to invoke when a task's execution encounters an error. Operations defined here must be idempotent, as `onTaskFailure` can be called multiple times.

Annotations
     @DeveloperApi()

### Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/LogUtils$.html "Permalink") object [LogUtils](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/LogUtils$.html ":: : DeveloperApi :: Utils for querying Spark logs with Spark SQL.")
:: : DeveloperApi :: Utils for querying Spark logs with Spark SQL.
:: : DeveloperApi :: Utils for querying Spark logs with Spark SQL.

Annotations
     @DeveloperApi()

Since

4.0.0
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/SizeEstimator$.html "Permalink") object [SizeEstimator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/SizeEstimator$.html ":: DeveloperApi :: Estimates the sizes of Java objects \(number of bytes of memory they occupy\), for use in memory-aware caches.") extends Logging
Estimates the sizes of Java objects (number of bytes of memory they occupy), for use in memory-aware caches.
Estimates the sizes of Java objects (number of bytes of memory they occupy), for use in memory-aware caches.
Based on the following JavaWorld article: https://www.infoworld.com/article/2077408/sizeof-for-java.html

Annotations
     @DeveloperApi()
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/SparkEnvUtils$.html "Permalink") object [SparkEnvUtils](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/SparkEnvUtils$.html) extends SparkEnvUtils
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/SparkSystemUtils$.html "Permalink") object [SparkSystemUtils](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/SparkSystemUtils$.html) extends SparkSystemUtils
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/StatCounter$.html "Permalink") object [StatCounter](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/StatCounter$.html) extends [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable")

### Ungrouped
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html "Permalink") abstract  class [AccumulatorV2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html "The base class for accumulators, that can accumulate inputs of type IN, and produce output of type OUT.")[IN, OUT] extends Serializable
The base class for accumulators, that can accumulate inputs of type `IN`, and produce output of type `OUT`.
The base class for accumulators, that can accumulate inputs of type `IN`, and produce output of type `OUT`.
`OUT` should be a type that can be read atomically (e.g., Int, Long), or thread-safely (e.g., synchronized collections) because it will be read from other threads.
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/ChildFirstURLClassLoader.html "Permalink") class [ChildFirstURLClassLoader](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/ChildFirstURLClassLoader.html "A mutable class loader that gives preference to its own URLs over the parent class loader when loading classes and resources.") extends [MutableURLClassLoader](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/MutableURLClassLoader.html "org.apache.spark.util.MutableURLClassLoader")
A mutable class loader that gives preference to its own URLs over the parent class loader when loading classes and resources.
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/CollectionAccumulator.html "Permalink") class [CollectionAccumulator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/CollectionAccumulator.html "An accumulator for collecting a list of elements.")[T] extends [AccumulatorV2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html "org.apache.spark.util.AccumulatorV2")[T, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#java.util.List "java.util.List")[T]]
An [accumulator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html "org.apache.spark.util.AccumulatorV2") for collecting a list of elements.
An [accumulator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html "org.apache.spark.util.AccumulatorV2") for collecting a list of elements.

Since

2.0.0
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/DoubleAccumulator.html "Permalink") class [DoubleAccumulator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/DoubleAccumulator.html "An accumulator for computing sum, count, and averages for double precision floating numbers.") extends [AccumulatorV2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html "org.apache.spark.util.AccumulatorV2")[[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html#java.lang.Double "java.lang.Double"), [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html#java.lang.Double "java.lang.Double")]
An [accumulator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html "org.apache.spark.util.AccumulatorV2") for computing sum, count, and averages for double precision floating numbers.
An [accumulator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html "org.apache.spark.util.AccumulatorV2") for computing sum, count, and averages for double precision floating numbers.

Since

2.0.0
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/EnumUtil.html "Permalink") class [EnumUtil](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/EnumUtil.html) extends AnyRef

Annotations
     @Private()
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/ExposedBufferByteArrayOutputStream.html "Permalink") final  class [ExposedBufferByteArrayOutputStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/ExposedBufferByteArrayOutputStream.html "Subclass of ByteArrayOutputStream that exposes buf directly.") extends [ByteArrayOutputStream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/ByteArrayOutputStream.html#java.io.ByteArrayOutputStream "java.io.ByteArrayOutputStream")
Subclass of ByteArrayOutputStream that exposes `buf` directly.
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/LexicalThreadLocal.html "Permalink") trait [LexicalThreadLocal](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/LexicalThreadLocal.html "Helper trait for defining thread locals with lexical scoping.")[T] extends AnyRef
Helper trait for defining thread locals with lexical scoping.
Helper trait for defining thread locals with lexical scoping. With this helper, the thread local is private and can only be set by the [Handle](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/LexicalThreadLocal$Handle.html "org.apache.spark.util.LexicalThreadLocal.Handle"). The [Handle](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/LexicalThreadLocal$Handle.html "org.apache.spark.util.LexicalThreadLocal.Handle") only exposes the thread local value to functions passed into its runWith method. This pattern allows for the lifetime of the thread local value to be strictly controlled.
Rather than calling `tl.set(...)` and `tl.remove()` you would get a handle and execute your code in `handle.runWith { ... }`.
Example:

```
object Credentials extends LexicalThreadLocal[Int] {
  def create(creds: Map[String, String]) = new Handle(Some(creds))
}
...
val handle = Credentials.create(Map("key" -> "value"))
assert(Credentials.get() == None)
handle.runWith {
  assert(Credentials.get() == Some(Map("key" -> "value")))
}
```

  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/LongAccumulator.html "Permalink") class [LongAccumulator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/LongAccumulator.html "An accumulator for computing sum, count, and average of 64-bit integers.") extends [AccumulatorV2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html "org.apache.spark.util.AccumulatorV2")[[Long](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html#java.lang.Long "java.lang.Long"), [Long](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html#java.lang.Long "java.lang.Long")]
An [accumulator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html "org.apache.spark.util.AccumulatorV2") for computing sum, count, and average of 64-bit integers.
An [accumulator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html "org.apache.spark.util.AccumulatorV2") for computing sum, count, and average of 64-bit integers.

Since

2.0.0
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/MutablePair.html "Permalink") case class [MutablePair](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/MutablePair.html ":: DeveloperApi :: A tuple of 2 elements.")[T1, T2](_1: T1, _2: T2) extends Product2[T1, T2] with Product with Serializable
A tuple of 2 elements.
A tuple of 2 elements. This can be used as an alternative to Scala's Tuple2 when we want to minimize object allocation.

_1

Element 1 of this MutablePair

_2

Element 2 of this MutablePair

Annotations
     @DeveloperApi()
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/MutableURLClassLoader.html "Permalink") class [MutableURLClassLoader](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/MutableURLClassLoader.html "URL class loader that exposes the addURL method in URLClassLoader.") extends [URLClassLoader](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URLClassLoader.html#java.net.URLClassLoader "java.net.URLClassLoader")
URL class loader that exposes the `addURL` method in URLClassLoader.
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/Pair.html "Permalink") final  class [Pair](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/Pair.html "An immutable pair of values.")[L, R] extends [Record](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Record.html#java.lang.Record "java.lang.Record")
An immutable pair of values.
An immutable pair of values. Note that the fields are intentionally designed to be `getLeft` and `getRight` instead of `left` and `right` in order to mitigate the migration burden from `org.apache.commons.lang3.tuple.Pair`.
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/ParentClassLoader.html "Permalink") class [ParentClassLoader](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/ParentClassLoader.html "A class loader which makes some protected methods in ClassLoader accessible.") extends [ClassLoader](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ClassLoader.html#java.lang.ClassLoader "java.lang.ClassLoader")
A class loader which makes some protected methods in ClassLoader accessible.
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/SerializableConfiguration.html "Permalink") class [SerializableConfiguration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/SerializableConfiguration.html "Hadoop configuration but serializable.") extends Serializable
Hadoop configuration but serializable.
Hadoop configuration but serializable. Use `value` to access the Hadoop configuration.

Annotations
     @DeveloperApi() @Unstable()
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/StatCounter.html "Permalink") class [StatCounter](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/StatCounter.html "A class for tracking the statistics of a set of numbers \(count, mean and variance\) in a numerically robust way.") extends Serializable
A class for tracking the statistics of a set of numbers (count, mean and variance) in a numerically robust way.
A class for tracking the statistics of a set of numbers (count, mean and variance) in a numerically robust way. Includes support for merging two StatCounters. Based on Welford and Chan's [ algorithms](http://en.wikipedia.org/wiki/Algorithms_for_calculating_variance) for running variance.
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/TaskCompletionListener.html "Permalink") trait [TaskCompletionListener](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/TaskCompletionListener.html ":: DeveloperApi ::") extends [EventListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EventListener.html#java.util.EventListener "java.util.EventListener")
Listener providing a callback function to invoke when a task's execution completes.

Annotations
     @DeveloperApi()
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/TaskFailureListener.html "Permalink") trait [TaskFailureListener](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/TaskFailureListener.html ":: DeveloperApi ::") extends [EventListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EventListener.html#java.util.EventListener "java.util.EventListener")
Listener providing a callback function to invoke when a task's execution encounters an error. Operations defined here must be idempotent, as `onTaskFailure` can be called multiple times.

Annotations
     @DeveloperApi()

  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/LogUtils$.html "Permalink") object [LogUtils](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/LogUtils$.html ":: : DeveloperApi :: Utils for querying Spark logs with Spark SQL.")
:: : DeveloperApi :: Utils for querying Spark logs with Spark SQL.
:: : DeveloperApi :: Utils for querying Spark logs with Spark SQL.

Annotations
     @DeveloperApi()

Since

4.0.0
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/SizeEstimator$.html "Permalink") object [SizeEstimator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/SizeEstimator$.html ":: DeveloperApi :: Estimates the sizes of Java objects \(number of bytes of memory they occupy\), for use in memory-aware caches.") extends Logging
Estimates the sizes of Java objects (number of bytes of memory they occupy), for use in memory-aware caches.
Estimates the sizes of Java objects (number of bytes of memory they occupy), for use in memory-aware caches.
Based on the following JavaWorld article: https://www.infoworld.com/article/2077408/sizeof-for-java.html

Annotations
     @DeveloperApi()
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/SparkEnvUtils$.html "Permalink") object [SparkEnvUtils](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/SparkEnvUtils$.html) extends SparkEnvUtils
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/SparkSystemUtils$.html "Permalink") object [SparkSystemUtils](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/SparkSystemUtils$.html) extends SparkSystemUtils
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/StatCounter$.html "Permalink") object [StatCounter](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/StatCounter$.html) extends [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable")
