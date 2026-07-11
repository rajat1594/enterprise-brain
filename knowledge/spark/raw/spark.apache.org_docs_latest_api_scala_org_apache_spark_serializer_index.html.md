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
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/index.html "Permalink") package serializer
Pluggable serializers for RDD and shuffle data.
Pluggable serializers for RDD and shuffle data.  

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark") 

See also
    
[org.apache.spark.serializer.Serializer](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/Serializer.html "org.apache.spark.serializer.Serializer")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/DeserializationStream.html ":: DeveloperApi :: A stream for reading serialized objects.")[DeserializationStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/DeserializationStream.html ":: DeveloperApi :: A stream for reading serialized objects.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/DummySerializerInstance.html "Unfortunately, we need a serializer instance in order to construct a DiskBlockObjectWriter.")[DummySerializerInstance](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/DummySerializerInstance.html "Unfortunately, we need a serializer instance in order to construct a DiskBlockObjectWriter.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/JavaSerializer.html ":: DeveloperApi :: A Spark serializer that uses Java's built-in serialization.")[JavaSerializer](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/JavaSerializer.html ":: DeveloperApi :: A Spark serializer that uses Java's built-in serialization.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/KryoRegistrator.html "Interface implemented by clients to register their classes with Kryo when using Kryo serialization.")[KryoRegistrator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/KryoRegistrator.html "Interface implemented by clients to register their classes with Kryo when using Kryo serialization.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/KryoSerializer.html "A Spark serializer that uses the Kryo serialization library.")[KryoSerializer](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/KryoSerializer.html "A Spark serializer that uses the Kryo serialization library.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/SerializationStream.html ":: DeveloperApi :: A stream for writing serialized objects.")[SerializationStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/SerializationStream.html ":: DeveloperApi :: A stream for writing serialized objects.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/Serializer.html ":: DeveloperApi :: A serializer.")[Serializer](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/Serializer.html ":: DeveloperApi :: A serializer.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/SerializerInstance.html ":: DeveloperApi :: An instance of a serializer, for use by one thread at a time.")[SerializerInstance](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/SerializerInstance.html ":: DeveloperApi :: An instance of a serializer, for use by one thread at a time.")
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
# serializer[ __](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/index.html "Permalink")
####  package serializer
Pluggable serializers for RDD and shuffle data.  

Source
    [package.scala](https://github.com/apache/spark/tree/v4.1.2/core/src/main/scala/org/apache/spark/serializer/package.scala) 

See also
    
[org.apache.spark.serializer.Serializer](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/Serializer.html "org.apache.spark.serializer.Serializer")
Linear Supertypes
AnyRef, Any
### Type Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/DeserializationStream.html "Permalink") abstract  class [DeserializationStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/DeserializationStream.html ":: DeveloperApi :: A stream for reading serialized objects.") extends [Closeable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Closeable.html#java.io.Closeable "java.io.Closeable")
A stream for reading serialized objects.
A stream for reading serialized objects.  

Annotations
     @DeveloperApi()
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/DummySerializerInstance.html "Permalink") final  class [DummySerializerInstance](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/DummySerializerInstance.html "Unfortunately, we need a serializer instance in order to construct a DiskBlockObjectWriter.") extends [SerializerInstance](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/SerializerInstance.html "org.apache.spark.serializer.SerializerInstance")
Unfortunately, we need a serializer instance in order to construct a DiskBlockObjectWriter.
Unfortunately, we need a serializer instance in order to construct a DiskBlockObjectWriter. Our shuffle write path doesn't actually use this serializer (since we end up calling the `write() OutputStream methods), but DiskBlockObjectWriter still calls some methods on it. To work around this, we pass a dummy no-op serializer. ` 

Annotations
     @Private()
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/JavaSerializer.html "Permalink") class [JavaSerializer](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/JavaSerializer.html ":: DeveloperApi :: A Spark serializer that uses Java's built-in serialization.") extends [Serializer](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/Serializer.html "org.apache.spark.serializer.Serializer") with [Externalizable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Externalizable.html#java.io.Externalizable "java.io.Externalizable")
A Spark serializer that uses Java's built-in serialization.
A Spark serializer that uses Java's built-in serialization.  

Annotations
     @DeveloperApi() 

Note
    
This serializer is not guaranteed to be wire-compatible across different versions of Spark. It is intended to be used to serialize/de-serialize data within a single Spark application.
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/KryoRegistrator.html "Permalink") trait [KryoRegistrator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/KryoRegistrator.html "Interface implemented by clients to register their classes with Kryo when using Kryo serialization.") extends AnyRef
Interface implemented by clients to register their classes with Kryo when using Kryo serialization.
Interface implemented by clients to register their classes with Kryo when using Kryo serialization.  

Annotations
     @DeveloperApi()
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/KryoSerializer.html "Permalink") class [KryoSerializer](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/KryoSerializer.html "A Spark serializer that uses the Kryo serialization library.") extends [Serializer](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/Serializer.html "org.apache.spark.serializer.Serializer") with Logging with [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable")
A Spark serializer that uses the [ Kryo serialization library](https://code.google.com/p/kryo/).
A Spark serializer that uses the [ Kryo serialization library](https://code.google.com/p/kryo/).  

Note
    
This serializer is not guaranteed to be wire-compatible across different versions of Spark. It is intended to be used to serialize/de-serialize data within a single Spark application.
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/SerializationStream.html "Permalink") abstract  class [SerializationStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/SerializationStream.html ":: DeveloperApi :: A stream for writing serialized objects.") extends [Closeable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Closeable.html#java.io.Closeable "java.io.Closeable")
A stream for writing serialized objects.
A stream for writing serialized objects.  

Annotations
     @DeveloperApi()
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/Serializer.html "Permalink") abstract  class [Serializer](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/Serializer.html ":: DeveloperApi :: A serializer.") extends AnyRef
A serializer.
A serializer. Because some serialization libraries are not thread safe, this class is used to create [org.apache.spark.serializer.SerializerInstance](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/SerializerInstance.html "org.apache.spark.serializer.SerializerInstance") objects that do the actual serialization and are guaranteed to only be called from one thread at a time.
Implementations of this trait should implement:
1. a zero-arg constructor or a constructor that accepts a [org.apache.spark.SparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html "org.apache.spark.SparkConf") as parameter. If both constructors are defined, the latter takes precedence.
2. Java serialization interface.  

Annotations
     @DeveloperApi() 

Note
    
Serializers are not required to be wire-compatible across different versions of Spark. They are intended to be used to serialize/de-serialize data within a single Spark application.
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/SerializerInstance.html "Permalink") abstract  class [SerializerInstance](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/SerializerInstance.html ":: DeveloperApi :: An instance of a serializer, for use by one thread at a time.") extends AnyRef
An instance of a serializer, for use by one thread at a time.
An instance of a serializer, for use by one thread at a time.
It is legal to create multiple serialization / deserialization streams from the same SerializerInstance as long as those streams are all used within the same thread.  

Annotations
     @DeveloperApi() @NotThreadSafe()


### Ungrouped
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/DeserializationStream.html "Permalink") abstract  class [DeserializationStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/DeserializationStream.html ":: DeveloperApi :: A stream for reading serialized objects.") extends [Closeable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Closeable.html#java.io.Closeable "java.io.Closeable")
A stream for reading serialized objects.
A stream for reading serialized objects.  

Annotations
     @DeveloperApi()
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/DummySerializerInstance.html "Permalink") final  class [DummySerializerInstance](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/DummySerializerInstance.html "Unfortunately, we need a serializer instance in order to construct a DiskBlockObjectWriter.") extends [SerializerInstance](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/SerializerInstance.html "org.apache.spark.serializer.SerializerInstance")
Unfortunately, we need a serializer instance in order to construct a DiskBlockObjectWriter.
Unfortunately, we need a serializer instance in order to construct a DiskBlockObjectWriter. Our shuffle write path doesn't actually use this serializer (since we end up calling the `write() OutputStream methods), but DiskBlockObjectWriter still calls some methods on it. To work around this, we pass a dummy no-op serializer. ` 

Annotations
     @Private()
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/JavaSerializer.html "Permalink") class [JavaSerializer](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/JavaSerializer.html ":: DeveloperApi :: A Spark serializer that uses Java's built-in serialization.") extends [Serializer](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/Serializer.html "org.apache.spark.serializer.Serializer") with [Externalizable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Externalizable.html#java.io.Externalizable "java.io.Externalizable")
A Spark serializer that uses Java's built-in serialization.
A Spark serializer that uses Java's built-in serialization.  

Annotations
     @DeveloperApi() 

Note
    
This serializer is not guaranteed to be wire-compatible across different versions of Spark. It is intended to be used to serialize/de-serialize data within a single Spark application.
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/KryoRegistrator.html "Permalink") trait [KryoRegistrator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/KryoRegistrator.html "Interface implemented by clients to register their classes with Kryo when using Kryo serialization.") extends AnyRef
Interface implemented by clients to register their classes with Kryo when using Kryo serialization.
Interface implemented by clients to register their classes with Kryo when using Kryo serialization.  

Annotations
     @DeveloperApi()
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/KryoSerializer.html "Permalink") class [KryoSerializer](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/KryoSerializer.html "A Spark serializer that uses the Kryo serialization library.") extends [Serializer](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/Serializer.html "org.apache.spark.serializer.Serializer") with Logging with [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable")
A Spark serializer that uses the [ Kryo serialization library](https://code.google.com/p/kryo/).
A Spark serializer that uses the [ Kryo serialization library](https://code.google.com/p/kryo/).  

Note
    
This serializer is not guaranteed to be wire-compatible across different versions of Spark. It is intended to be used to serialize/de-serialize data within a single Spark application.
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/SerializationStream.html "Permalink") abstract  class [SerializationStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/SerializationStream.html ":: DeveloperApi :: A stream for writing serialized objects.") extends [Closeable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Closeable.html#java.io.Closeable "java.io.Closeable")
A stream for writing serialized objects.
A stream for writing serialized objects.  

Annotations
     @DeveloperApi()
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/Serializer.html "Permalink") abstract  class [Serializer](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/Serializer.html ":: DeveloperApi :: A serializer.") extends AnyRef
A serializer.
A serializer. Because some serialization libraries are not thread safe, this class is used to create [org.apache.spark.serializer.SerializerInstance](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/SerializerInstance.html "org.apache.spark.serializer.SerializerInstance") objects that do the actual serialization and are guaranteed to only be called from one thread at a time.
Implementations of this trait should implement:
1. a zero-arg constructor or a constructor that accepts a [org.apache.spark.SparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html "org.apache.spark.SparkConf") as parameter. If both constructors are defined, the latter takes precedence.
2. Java serialization interface.  

Annotations
     @DeveloperApi() 

Note
    
Serializers are not required to be wire-compatible across different versions of Spark. They are intended to be used to serialize/de-serialize data within a single Spark application.
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/SerializerInstance.html "Permalink") abstract  class [SerializerInstance](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/SerializerInstance.html ":: DeveloperApi :: An instance of a serializer, for use by one thread at a time.") extends AnyRef
An instance of a serializer, for use by one thread at a time.
An instance of a serializer, for use by one thread at a time.
It is legal to create multiple serialization / deserialization streams from the same SerializerInstance as long as those streams are all used within the same thread.  

Annotations
     @DeveloperApi() @NotThreadSafe()


