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
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/index.html "Permalink") package io
IO codecs used for compression.
IO codecs used for compression. See [org.apache.spark.io.CompressionCodec](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/CompressionCodec.html "org.apache.spark.io.CompressionCodec").

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/CompressionCodec.html ":: DeveloperApi :: CompressionCodec allows the customization of choosing different compression implementations to be used in block storage.")[CompressionCodec](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/CompressionCodec.html ":: DeveloperApi :: CompressionCodec allows the customization of choosing different compression implementations to be used in block storage.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/HadoopCodecStreams$.html "An utility object to look up Hadoop compression codecs and create input streams.")[HadoopCodecStreams](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/HadoopCodecStreams$.html "An utility object to look up Hadoop compression codecs and create input streams.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/LZ4CompressionCodec.html ":: DeveloperApi :: LZ4 implementation of org.apache.spark.io.CompressionCodec.")[LZ4CompressionCodec](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/LZ4CompressionCodec.html ":: DeveloperApi :: LZ4 implementation of org.apache.spark.io.CompressionCodec.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/LZFCompressionCodec.html ":: DeveloperApi :: LZF implementation of org.apache.spark.io.CompressionCodec.")[LZFCompressionCodec](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/LZFCompressionCodec.html ":: DeveloperApi :: LZF implementation of org.apache.spark.io.CompressionCodec.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/NioBufferedFileInputStream.html "InputStream implementation which uses direct buffer to read a file to avoid extra copy of data between Java and native memory which happens when using java.io.BufferedInputStream.")[NioBufferedFileInputStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/NioBufferedFileInputStream.html "InputStream implementation which uses direct buffer to read a file to avoid extra copy of data between Java and native memory which happens when using java.io.BufferedInputStream.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/ReadAheadInputStream.html "InputStream implementation which asynchronously reads ahead from the underlying input stream when specified amount of data has been read from the current buffer.")[ReadAheadInputStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/ReadAheadInputStream.html "InputStream implementation which asynchronously reads ahead from the underlying input stream when specified amount of data has been read from the current buffer.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/SnappyCompressionCodec.html ":: DeveloperApi :: Snappy implementation of org.apache.spark.io.CompressionCodec.")[SnappyCompressionCodec](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/SnappyCompressionCodec.html ":: DeveloperApi :: Snappy implementation of org.apache.spark.io.CompressionCodec.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/ZStdCompressionCodec.html ":: DeveloperApi :: ZStandard implementation of org.apache.spark.io.CompressionCodec.")[ZStdCompressionCodec](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/ZStdCompressionCodec.html ":: DeveloperApi :: ZStandard implementation of org.apache.spark.io.CompressionCodec.")
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

p
[org](https://spark.apache.org/docs/latest/api/scala/org/index.html "org").[apache](https://spark.apache.org/docs/latest/api/scala/org/apache/index.html "org.apache").[spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
# io[ __](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/index.html "Permalink")
####  package io
IO codecs used for compression. See [org.apache.spark.io.CompressionCodec](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/CompressionCodec.html "org.apache.spark.io.CompressionCodec").

Source
    [package.scala](https://github.com/apache/spark/tree/v4.1.2/core/src/main/scala/org/apache/spark/io/package.scala)
Linear Supertypes
AnyRef, Any
__ __
Ordering
  1. Alphabetic
  2. By Inheritance

Inherited

  1. io
  2. AnyRef
  3. Any

  1. Hide All
  2. Show All

Visibility
  1. Public
  2. Protected

### Type Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/CompressionCodec.html "Permalink") trait [CompressionCodec](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/CompressionCodec.html ":: DeveloperApi :: CompressionCodec allows the customization of choosing different compression implementations to be used in block storage.") extends AnyRef
CompressionCodec allows the customization of choosing different compression implementations to be used in block storage.
CompressionCodec allows the customization of choosing different compression implementations to be used in block storage.

Annotations
     @DeveloperApi()

Note

The wire protocol for a codec is not guaranteed compatible across versions of Spark. This is intended for use as an internal compression utility within a single Spark application.
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/LZ4CompressionCodec.html "Permalink") class [LZ4CompressionCodec](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/LZ4CompressionCodec.html ":: DeveloperApi :: LZ4 implementation of org.apache.spark.io.CompressionCodec.") extends [CompressionCodec](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/CompressionCodec.html "org.apache.spark.io.CompressionCodec")
LZ4 implementation of [org.apache.spark.io.CompressionCodec](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/CompressionCodec.html "org.apache.spark.io.CompressionCodec").
LZ4 implementation of [org.apache.spark.io.CompressionCodec](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/CompressionCodec.html "org.apache.spark.io.CompressionCodec"). Block size can be configured by `spark.io.compression.lz4.blockSize`.

Annotations
     @DeveloperApi()

Note

The wire protocol for this codec is not guaranteed to be compatible across versions of Spark. This is intended for use as an internal compression utility within a single Spark application.
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/LZFCompressionCodec.html "Permalink") class [LZFCompressionCodec](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/LZFCompressionCodec.html ":: DeveloperApi :: LZF implementation of org.apache.spark.io.CompressionCodec.") extends [CompressionCodec](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/CompressionCodec.html "org.apache.spark.io.CompressionCodec")
LZF implementation of [org.apache.spark.io.CompressionCodec](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/CompressionCodec.html "org.apache.spark.io.CompressionCodec").
LZF implementation of [org.apache.spark.io.CompressionCodec](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/CompressionCodec.html "org.apache.spark.io.CompressionCodec").

Annotations
     @DeveloperApi()

Note

The wire protocol for this codec is not guaranteed to be compatible across versions of Spark. This is intended for use as an internal compression utility within a single Spark application.
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/NioBufferedFileInputStream.html "Permalink") final  class [NioBufferedFileInputStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/NioBufferedFileInputStream.html "InputStream implementation which uses direct buffer to read a file to avoid extra copy of data between Java and native memory which happens when using java.io.BufferedInputStream.") extends [InputStream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html#java.io.InputStream "java.io.InputStream")
`InputStream` implementation which uses direct buffer to read a file to avoid extra copy of data between Java and native memory which happens when using `java.io.BufferedInputStream[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/BufferedInputStream.html "java.io.BufferedInputStream")`.
`InputStream` implementation which uses direct buffer to read a file to avoid extra copy of data between Java and native memory which happens when using `java.io.BufferedInputStream[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/BufferedInputStream.html "java.io.BufferedInputStream")`. Unfortunately, this is not something already available in JDK, `sun.nio.ch.ChannelInputStream` supports reading a file using nio, but does not support buffering.
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/ReadAheadInputStream.html "Permalink") class [ReadAheadInputStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/ReadAheadInputStream.html "InputStream implementation which asynchronously reads ahead from the underlying input stream when specified amount of data has been read from the current buffer.") extends [InputStream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html#java.io.InputStream "java.io.InputStream")
`InputStream` implementation which asynchronously reads ahead from the underlying input stream when specified amount of data has been read from the current buffer.
`InputStream` implementation which asynchronously reads ahead from the underlying input stream when specified amount of data has been read from the current buffer. It does it by maintaining two buffers - active buffer and read ahead buffer. Active buffer contains data which should be returned when a read() call is issued. The read ahead buffer is used to asynchronously read from the underlying input stream and once the current active buffer is exhausted, we flip the two buffers so that we can start reading from the read ahead buffer without being blocked in disk I/O.
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/SnappyCompressionCodec.html "Permalink") class [SnappyCompressionCodec](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/SnappyCompressionCodec.html ":: DeveloperApi :: Snappy implementation of org.apache.spark.io.CompressionCodec.") extends [CompressionCodec](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/CompressionCodec.html "org.apache.spark.io.CompressionCodec")
Snappy implementation of [org.apache.spark.io.CompressionCodec](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/CompressionCodec.html "org.apache.spark.io.CompressionCodec").
Snappy implementation of [org.apache.spark.io.CompressionCodec](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/CompressionCodec.html "org.apache.spark.io.CompressionCodec"). Block size can be configured by `spark.io.compression.snappy.blockSize`.

Annotations
     @DeveloperApi()

Note

The wire protocol for this codec is not guaranteed to be compatible across versions of Spark. This is intended for use as an internal compression utility within a single Spark application.
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/ZStdCompressionCodec.html "Permalink") class [ZStdCompressionCodec](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/ZStdCompressionCodec.html ":: DeveloperApi :: ZStandard implementation of org.apache.spark.io.CompressionCodec.") extends [CompressionCodec](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/CompressionCodec.html "org.apache.spark.io.CompressionCodec")
ZStandard implementation of [org.apache.spark.io.CompressionCodec](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/CompressionCodec.html "org.apache.spark.io.CompressionCodec").
ZStandard implementation of [org.apache.spark.io.CompressionCodec](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/CompressionCodec.html "org.apache.spark.io.CompressionCodec"). For more details see - http://facebook.github.io/zstd/

Annotations
     @DeveloperApi()

Note

The wire protocol for this codec is not guaranteed to be compatible across versions of Spark. This is intended for use as an internal compression utility within a single Spark application.

### Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/HadoopCodecStreams$.html "Permalink") object [HadoopCodecStreams](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/HadoopCodecStreams$.html "An utility object to look up Hadoop compression codecs and create input streams.")
An utility object to look up Hadoop compression codecs and create input streams.
An utility object to look up Hadoop compression codecs and create input streams. In addition to standard Hadoop codecs, it also supports Spark's Zstandard codec if Hadopp is not compiled with Zstandard support. Additionally, it supports non-standard file extensions like `.zstd` and `.gzip` for Zstandard and Gzip codecs.

### Ungrouped
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/CompressionCodec.html "Permalink") trait [CompressionCodec](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/CompressionCodec.html ":: DeveloperApi :: CompressionCodec allows the customization of choosing different compression implementations to be used in block storage.") extends AnyRef
CompressionCodec allows the customization of choosing different compression implementations to be used in block storage.
CompressionCodec allows the customization of choosing different compression implementations to be used in block storage.

Annotations
     @DeveloperApi()

Note

The wire protocol for a codec is not guaranteed compatible across versions of Spark. This is intended for use as an internal compression utility within a single Spark application.
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/LZ4CompressionCodec.html "Permalink") class [LZ4CompressionCodec](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/LZ4CompressionCodec.html ":: DeveloperApi :: LZ4 implementation of org.apache.spark.io.CompressionCodec.") extends [CompressionCodec](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/CompressionCodec.html "org.apache.spark.io.CompressionCodec")
LZ4 implementation of [org.apache.spark.io.CompressionCodec](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/CompressionCodec.html "org.apache.spark.io.CompressionCodec").
LZ4 implementation of [org.apache.spark.io.CompressionCodec](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/CompressionCodec.html "org.apache.spark.io.CompressionCodec"). Block size can be configured by `spark.io.compression.lz4.blockSize`.

Annotations
     @DeveloperApi()

Note

The wire protocol for this codec is not guaranteed to be compatible across versions of Spark. This is intended for use as an internal compression utility within a single Spark application.
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/LZFCompressionCodec.html "Permalink") class [LZFCompressionCodec](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/LZFCompressionCodec.html ":: DeveloperApi :: LZF implementation of org.apache.spark.io.CompressionCodec.") extends [CompressionCodec](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/CompressionCodec.html "org.apache.spark.io.CompressionCodec")
LZF implementation of [org.apache.spark.io.CompressionCodec](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/CompressionCodec.html "org.apache.spark.io.CompressionCodec").
LZF implementation of [org.apache.spark.io.CompressionCodec](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/CompressionCodec.html "org.apache.spark.io.CompressionCodec").

Annotations
     @DeveloperApi()

Note

The wire protocol for this codec is not guaranteed to be compatible across versions of Spark. This is intended for use as an internal compression utility within a single Spark application.
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/NioBufferedFileInputStream.html "Permalink") final  class [NioBufferedFileInputStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/NioBufferedFileInputStream.html "InputStream implementation which uses direct buffer to read a file to avoid extra copy of data between Java and native memory which happens when using java.io.BufferedInputStream.") extends [InputStream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html#java.io.InputStream "java.io.InputStream")
`InputStream` implementation which uses direct buffer to read a file to avoid extra copy of data between Java and native memory which happens when using `java.io.BufferedInputStream[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/BufferedInputStream.html "java.io.BufferedInputStream")`.
`InputStream` implementation which uses direct buffer to read a file to avoid extra copy of data between Java and native memory which happens when using `java.io.BufferedInputStream[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/BufferedInputStream.html "java.io.BufferedInputStream")`. Unfortunately, this is not something already available in JDK, `sun.nio.ch.ChannelInputStream` supports reading a file using nio, but does not support buffering.
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/ReadAheadInputStream.html "Permalink") class [ReadAheadInputStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/ReadAheadInputStream.html "InputStream implementation which asynchronously reads ahead from the underlying input stream when specified amount of data has been read from the current buffer.") extends [InputStream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html#java.io.InputStream "java.io.InputStream")
`InputStream` implementation which asynchronously reads ahead from the underlying input stream when specified amount of data has been read from the current buffer.
`InputStream` implementation which asynchronously reads ahead from the underlying input stream when specified amount of data has been read from the current buffer. It does it by maintaining two buffers - active buffer and read ahead buffer. Active buffer contains data which should be returned when a read() call is issued. The read ahead buffer is used to asynchronously read from the underlying input stream and once the current active buffer is exhausted, we flip the two buffers so that we can start reading from the read ahead buffer without being blocked in disk I/O.
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/SnappyCompressionCodec.html "Permalink") class [SnappyCompressionCodec](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/SnappyCompressionCodec.html ":: DeveloperApi :: Snappy implementation of org.apache.spark.io.CompressionCodec.") extends [CompressionCodec](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/CompressionCodec.html "org.apache.spark.io.CompressionCodec")
Snappy implementation of [org.apache.spark.io.CompressionCodec](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/CompressionCodec.html "org.apache.spark.io.CompressionCodec").
Snappy implementation of [org.apache.spark.io.CompressionCodec](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/CompressionCodec.html "org.apache.spark.io.CompressionCodec"). Block size can be configured by `spark.io.compression.snappy.blockSize`.

Annotations
     @DeveloperApi()

Note

The wire protocol for this codec is not guaranteed to be compatible across versions of Spark. This is intended for use as an internal compression utility within a single Spark application.
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/ZStdCompressionCodec.html "Permalink") class [ZStdCompressionCodec](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/ZStdCompressionCodec.html ":: DeveloperApi :: ZStandard implementation of org.apache.spark.io.CompressionCodec.") extends [CompressionCodec](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/CompressionCodec.html "org.apache.spark.io.CompressionCodec")
ZStandard implementation of [org.apache.spark.io.CompressionCodec](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/CompressionCodec.html "org.apache.spark.io.CompressionCodec").
ZStandard implementation of [org.apache.spark.io.CompressionCodec](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/CompressionCodec.html "org.apache.spark.io.CompressionCodec"). For more details see - http://facebook.github.io/zstd/

Annotations
     @DeveloperApi()

Note

The wire protocol for this codec is not guaranteed to be compatible across versions of Spark. This is intended for use as an internal compression utility within a single Spark application.

  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/HadoopCodecStreams$.html "Permalink") object [HadoopCodecStreams](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/HadoopCodecStreams$.html "An utility object to look up Hadoop compression codecs and create input streams.")
An utility object to look up Hadoop compression codecs and create input streams.
An utility object to look up Hadoop compression codecs and create input streams. In addition to standard Hadoop codecs, it also supports Spark's Zstandard codec if Hadopp is not compiled with Zstandard support. Additionally, it supports non-standard file extensions like `.zstd` and `.gzip` for Zstandard and Gzip codecs.
