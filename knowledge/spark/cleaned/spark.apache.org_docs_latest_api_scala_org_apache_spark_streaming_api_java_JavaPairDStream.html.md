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
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/index.html "Permalink") package [streaming](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/index.html "Spark Streaming functionality.")
Spark Streaming functionality.
Spark Streaming functionality. [org.apache.spark.streaming.StreamingContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html "org.apache.spark.streaming.StreamingContext") serves as the main entry point to Spark Streaming, while [org.apache.spark.streaming.dstream.DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream") is the data type representing a continuous sequence of RDDs, representing a continuous stream of data.
In addition, [org.apache.spark.streaming.dstream.PairDStreamFunctions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html "org.apache.spark.streaming.dstream.PairDStreamFunctions") contains operations available only on DStreams of key-value pairs, such as `groupByKey` and `reduceByKey`. These operations are automatically available on any DStream of the right type (e.g. DStream[(Int, Int)] through implicit conversions.
For the Java API of Spark Streaming, take a look at the [org.apache.spark.streaming.api.java.JavaStreamingContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html "org.apache.spark.streaming.api.java.JavaStreamingContext") which serves as the entry point, and the [org.apache.spark.streaming.api.java.JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream") and the [org.apache.spark.streaming.api.java.JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream") which have the DStream functionality.

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/index.html "Permalink") package [api](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/index.html)

Definition Classes
    [streaming](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/index.html "org.apache.spark.streaming")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/index.html "Permalink") package [java](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/index.html "Spark streaming's Java API.")
Spark streaming's Java API.
Spark streaming's Java API.

Definition Classes
    [api](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/index.html "org.apache.spark.streaming.api")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream$.html) [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "A Java-friendly interface to org.apache.spark.streaming.dstream.DStream, the basic abstraction in Spark Streaming that represents a continuous stream of data.")[JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "A Java-friendly interface to org.apache.spark.streaming.dstream.DStream, the basic abstraction in Spark Streaming that represents a continuous stream of data.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html)[JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaInputDStream$.html) [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaInputDStream.html "A Java-friendly interface to org.apache.spark.streaming.dstream.InputDStream.")[JavaInputDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaInputDStream.html "A Java-friendly interface to org.apache.spark.streaming.dstream.InputDStream.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaMapWithStateDStream.html "DStream representing the stream of data generated by mapWithState operation on a JavaPairDStream.")[JavaMapWithStateDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaMapWithStateDStream.html "DStream representing the stream of data generated by mapWithState operation on a JavaPairDStream.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream$.html) [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "A Java-friendly interface to a DStream of key-value pairs, which provides extra methods like reduceByKey and join.")[JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "A Java-friendly interface to a DStream of key-value pairs, which provides extra methods like reduceByKey and join.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairInputDStream$.html) [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairInputDStream.html "A Java-friendly interface to org.apache.spark.streaming.dstream.InputDStream of key-value pairs.")[JavaPairInputDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairInputDStream.html "A Java-friendly interface to org.apache.spark.streaming.dstream.InputDStream of key-value pairs.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairReceiverInputDStream$.html) [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairReceiverInputDStream.html "A Java-friendly interface to org.apache.spark.streaming.dstream.ReceiverInputDStream, the abstract class for defining any input stream that receives data over the network.")[JavaPairReceiverInputDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairReceiverInputDStream.html "A Java-friendly interface to org.apache.spark.streaming.dstream.ReceiverInputDStream, the abstract class for defining any input stream that receives data over the network.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaReceiverInputDStream$.html) [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaReceiverInputDStream.html "A Java-friendly interface to org.apache.spark.streaming.dstream.ReceiverInputDStream, the abstract class for defining any input stream that receives data over the network.")[JavaReceiverInputDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaReceiverInputDStream.html "A Java-friendly interface to org.apache.spark.streaming.dstream.ReceiverInputDStream, the abstract class for defining any input stream that receives data over the network.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext$.html "JavaStreamingContext object contains a number of utility functions.") [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html "A Java-friendly version of org.apache.spark.streaming.StreamingContext which is the main entry point for Spark Streaming functionality.")[JavaStreamingContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html "A Java-friendly version of org.apache.spark.streaming.StreamingContext which is the main entry point for Spark Streaming functionality.")

[c](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream$.html "See companion object")
[org](https://spark.apache.org/docs/latest/api/scala/org/index.html "org").[apache](https://spark.apache.org/docs/latest/api/scala/org/apache/index.html "org.apache").[spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark").[streaming](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/index.html "org.apache.spark.streaming").[api](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/index.html "org.apache.spark.streaming.api").[java](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/index.html "org.apache.spark.streaming.api.java")
#  [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream$.html "See companion object")[ __](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "Permalink")
###
Companion [object JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream$.html "See companion object")
####  class JavaPairDStream[K, V] extends AbstractJavaDStreamLike[(K, V), [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, V], [JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K, V]]
A Java-friendly interface to a DStream of key-value pairs, which provides extra methods like `reduceByKey` and `join`.

Source
    [JavaPairDStream.scala](https://github.com/apache/spark/tree/v4.1.2/streaming/src/main/scala/org/apache/spark/streaming/api/java/JavaPairDStream.scala)
Linear Supertypes
AbstractJavaDStreamLike[(K, V), [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, V], [JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K, V]], [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")[(K, V), [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, V], [JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K, V]], [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable"), AnyRef, Any
Known Subclasses
[JavaPairInputDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairInputDStream.html "org.apache.spark.streaming.api.java.JavaPairInputDStream"), [JavaPairReceiverInputDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairReceiverInputDStream.html "org.apache.spark.streaming.api.java.JavaPairReceiverInputDStream")
__ __
Ordering
  1. Alphabetic
  2. By Inheritance

Inherited

  1. JavaPairDStream
  2. AbstractJavaDStreamLike
  3. JavaDStreamLike
  4. Serializable
  5. AnyRef
  6. Any

  1. Hide All
  2. Show All

Visibility
  1. Public
  2. Protected

### Instance Constructors
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#<init>\(dstream:org.apache.spark.streaming.dstream.DStream\[\(K,V\)\]\)\(implicitkManifest:scala.reflect.ClassTag\[K\],implicitvManifest:scala.reflect.ClassTag\[V\]\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,V\] "Permalink") new JavaPairDStream(dstream: [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, V)])(implicit kManifest: ClassTag[K], vManifest: ClassTag[V])

### Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html###:Int "Permalink") final  def ##: Int

Definition Classes
    AnyRef → Any
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0

Definition Classes
    Any
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#cache\(\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,V\] "Permalink") def cache(): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, V]
Persist RDDs of this DStream with the default storage level (MEMORY_ONLY_SER)
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#checkpoint\(interval:org.apache.spark.streaming.Duration\):org.apache.spark.streaming.dstream.DStream\[T\] "Permalink") def checkpoint(interval: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration")): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, V)]
Enable periodic checkpointing of RDDs of this DStream.
Enable periodic checkpointing of RDDs of this DStream.

interval

Time interval after which generated RDD will be checkpointed

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#classTag:scala.reflect.ClassTag\[\(K,V\)\] "Permalink") val classTag: ClassTag[(K, V)]

Definition Classes
     [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream") → [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#clone\(\):Object "Permalink") def clone(): AnyRef

Attributes
    protected[lang]

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#cogroup\[W\]\(other:org.apache.spark.streaming.api.java.JavaPairDStream\[K,W\],partitioner:org.apache.spark.Partitioner\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,\(Iterable\[V\],Iterable\[W\]\)\] "Permalink") def cogroup[W](other: [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, W], partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner")): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, ([Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html#java.lang.Iterable "java.lang.Iterable")[V], [Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html#java.lang.Iterable "java.lang.Iterable")[W])]
Return a new DStream by applying 'cogroup' between RDDs of `this` DStream and `other` DStream.
Return a new DStream by applying 'cogroup' between RDDs of `this` DStream and `other` DStream. Hash partitioning is used to generate the RDDs with `numPartitions` partitions.
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#cogroup\[W\]\(other:org.apache.spark.streaming.api.java.JavaPairDStream\[K,W\],numPartitions:Int\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,\(Iterable\[V\],Iterable\[W\]\)\] "Permalink") def cogroup[W](other: [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, W], numPartitions: Int): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, ([Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html#java.lang.Iterable "java.lang.Iterable")[V], [Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html#java.lang.Iterable "java.lang.Iterable")[W])]
Return a new DStream by applying 'cogroup' between RDDs of `this` DStream and `other` DStream.
Return a new DStream by applying 'cogroup' between RDDs of `this` DStream and `other` DStream. Hash partitioning is used to generate the RDDs with `numPartitions` partitions.
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#cogroup\[W\]\(other:org.apache.spark.streaming.api.java.JavaPairDStream\[K,W\]\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,\(Iterable\[V\],Iterable\[W\]\)\] "Permalink") def cogroup[W](other: [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, W]): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, ([Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html#java.lang.Iterable "java.lang.Iterable")[V], [Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html#java.lang.Iterable "java.lang.Iterable")[W])]
Return a new DStream by applying 'cogroup' between RDDs of `this` DStream and `other` DStream.
Return a new DStream by applying 'cogroup' between RDDs of `this` DStream and `other` DStream. Hash partitioning is used to generate the RDDs with Spark's default number of partitions.
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#combineByKey\[C\]\(createCombiner:org.apache.spark.api.java.function.Function\[V,C\],mergeValue:org.apache.spark.api.java.function.Function2\[C,V,C\],mergeCombiners:org.apache.spark.api.java.function.Function2\[C,C,C\],partitioner:org.apache.spark.Partitioner,mapSideCombine:Boolean\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,C\] "Permalink") def combineByKey[C](createCombiner: [Function](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function.html "org.apache.spark.api.java.function.Function")[V, C], mergeValue: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[C, V, C], mergeCombiners: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[C, C, C], partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner"), mapSideCombine: Boolean): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, C]
Combine elements of each key in DStream's RDDs using custom function.
Combine elements of each key in DStream's RDDs using custom function. This is similar to the combineByKey for RDDs. Please refer to combineByKey in org.apache.spark.rdd.PairRDDFunctions for more information.
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#combineByKey\[C\]\(createCombiner:org.apache.spark.api.java.function.Function\[V,C\],mergeValue:org.apache.spark.api.java.function.Function2\[C,V,C\],mergeCombiners:org.apache.spark.api.java.function.Function2\[C,C,C\],partitioner:org.apache.spark.Partitioner\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,C\] "Permalink") def combineByKey[C](createCombiner: [Function](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function.html "org.apache.spark.api.java.function.Function")[V, C], mergeValue: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[C, V, C], mergeCombiners: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[C, C, C], partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner")): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, C]
Combine elements of each key in DStream's RDDs using custom function.
Combine elements of each key in DStream's RDDs using custom function. This is similar to the combineByKey for RDDs. Please refer to combineByKey in org.apache.spark.rdd.PairRDDFunctions for more information.
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#compute\(validTime:org.apache.spark.streaming.Time\):org.apache.spark.api.java.JavaPairRDD\[K,V\] "Permalink") def compute(validTime: [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time")): [JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K, V]
Method that generates an RDD for the given Duration
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#context\(\):org.apache.spark.streaming.StreamingContext "Permalink") def context(): [StreamingContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html "org.apache.spark.streaming.StreamingContext")
Return the [org.apache.spark.streaming.StreamingContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html "org.apache.spark.streaming.StreamingContext") associated with this DStream
Return the [org.apache.spark.streaming.StreamingContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html "org.apache.spark.streaming.StreamingContext") associated with this DStream

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#count\(\):org.apache.spark.streaming.api.java.JavaDStream\[Long\] "Permalink") def count(): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[[Long](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html#java.lang.Long "java.lang.Long")]
Return a new DStream in which each RDD has a single element generated by counting each RDD of this DStream.
Return a new DStream in which each RDD has a single element generated by counting each RDD of this DStream.

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#countByValue\(numPartitions:Int\):org.apache.spark.streaming.api.java.JavaPairDStream\[T,Long\] "Permalink") def countByValue(numPartitions: Int): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[(K, V), [Long](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html#java.lang.Long "java.lang.Long")]
Return a new DStream in which each RDD contains the counts of each distinct value in each RDD of this DStream.
Return a new DStream in which each RDD contains the counts of each distinct value in each RDD of this DStream. Hash partitioning is used to generate the RDDs with `numPartitions` partitions.

numPartitions

number of partitions of each RDD in the new DStream.

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#countByValue\(\):org.apache.spark.streaming.api.java.JavaPairDStream\[T,Long\] "Permalink") def countByValue(): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[(K, V), [Long](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html#java.lang.Long "java.lang.Long")]
Return a new DStream in which each RDD contains the counts of each distinct value in each RDD of this DStream.
Return a new DStream in which each RDD contains the counts of each distinct value in each RDD of this DStream. Hash partitioning is used to generate the RDDs with Spark's default number of partitions.

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#countByValueAndWindow\(windowDuration:org.apache.spark.streaming.Duration,slideDuration:org.apache.spark.streaming.Duration,numPartitions:Int\):org.apache.spark.streaming.api.java.JavaPairDStream\[T,Long\] "Permalink") def countByValueAndWindow(windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), numPartitions: Int): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[(K, V), [Long](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html#java.lang.Long "java.lang.Long")]
Return a new DStream in which each RDD contains the count of distinct elements in RDDs in a sliding window over this DStream.
Return a new DStream in which each RDD contains the count of distinct elements in RDDs in a sliding window over this DStream. Hash partitioning is used to generate the RDDs with `numPartitions` partitions.

windowDuration

width of the window; must be a multiple of this DStream's batching interval

slideDuration

sliding interval of the window (i.e., the interval after which the new DStream will generate RDDs); must be a multiple of this DStream's batching interval

numPartitions

number of partitions of each RDD in the new DStream.

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#countByValueAndWindow\(windowDuration:org.apache.spark.streaming.Duration,slideDuration:org.apache.spark.streaming.Duration\):org.apache.spark.streaming.api.java.JavaPairDStream\[T,Long\] "Permalink") def countByValueAndWindow(windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration")): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[(K, V), [Long](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html#java.lang.Long "java.lang.Long")]
Return a new DStream in which each RDD contains the count of distinct elements in RDDs in a sliding window over this DStream.
Return a new DStream in which each RDD contains the count of distinct elements in RDDs in a sliding window over this DStream. Hash partitioning is used to generate the RDDs with Spark's default number of partitions.

windowDuration

width of the window; must be a multiple of this DStream's batching interval

slideDuration

sliding interval of the window (i.e., the interval after which the new DStream will generate RDDs); must be a multiple of this DStream's batching interval

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#countByWindow\(windowDuration:org.apache.spark.streaming.Duration,slideDuration:org.apache.spark.streaming.Duration\):org.apache.spark.streaming.api.java.JavaDStream\[Long\] "Permalink") def countByWindow(windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration")): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[[Long](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html#java.lang.Long "java.lang.Long")]
Return a new DStream in which each RDD has a single element generated by counting the number of elements in a window over this DStream.
Return a new DStream in which each RDD has a single element generated by counting the number of elements in a window over this DStream. windowDuration and slideDuration are as defined in the window() operation. This is equivalent to window(windowDuration, slideDuration).count()

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#dstream:org.apache.spark.streaming.dstream.DStream\[\(K,V\)\] "Permalink") val dstream: [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, V)]

Definition Classes
     [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream") → [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  23. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  24. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#equals\(x$1:Object\):Boolean "Permalink") def equals(arg0: AnyRef): Boolean

Definition Classes
    AnyRef → Any
  25. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#filter\(f:org.apache.spark.api.java.function.Function\[\(K,V\),Boolean\]\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,V\] "Permalink") def filter(f: [Function](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function.html "org.apache.spark.api.java.function.Function")[(K, V), [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html#java.lang.Boolean "java.lang.Boolean")]): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, V]
Return a new DStream containing only the elements that satisfy a predicate.
  26. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#flatMap\[U\]\(f:org.apache.spark.api.java.function.FlatMapFunction\[T,U\]\):org.apache.spark.streaming.api.java.JavaDStream\[U\] "Permalink") def flatMap[U](f: [FlatMapFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction.html "org.apache.spark.api.java.function.FlatMapFunction")[(K, V), U]): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[U]
Return a new DStream by applying a function to all elements of this DStream, and then flattening the results
Return a new DStream by applying a function to all elements of this DStream, and then flattening the results

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  27. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#flatMapToPair\[K2,V2\]\(f:org.apache.spark.api.java.function.PairFlatMapFunction\[T,K2,V2\]\):org.apache.spark.streaming.api.java.JavaPairDStream\[K2,V2\] "Permalink") def flatMapToPair[K2, V2](f: [PairFlatMapFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/PairFlatMapFunction.html "org.apache.spark.api.java.function.PairFlatMapFunction")[(K, V), K2, V2]): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K2, V2]
Return a new DStream by applying a function to all elements of this DStream, and then flattening the results
Return a new DStream by applying a function to all elements of this DStream, and then flattening the results

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  28. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#flatMapValues\[U\]\(f:org.apache.spark.api.java.function.FlatMapFunction\[V,U\]\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,U\] "Permalink") def flatMapValues[U](f: [FlatMapFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction.html "org.apache.spark.api.java.function.FlatMapFunction")[V, U]): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, U]
Return a new DStream by applying a flatmap function to the value of each key-value pairs in 'this' DStream without changing the key.
  29. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#foreachRDD\(foreachFunc:org.apache.spark.api.java.function.VoidFunction2\[R,org.apache.spark.streaming.Time\]\):Unit "Permalink") def foreachRDD(foreachFunc: [VoidFunction2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/VoidFunction2.html "org.apache.spark.api.java.function.VoidFunction2")[[JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K, V], [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time")]): Unit
Apply a function to each RDD in this DStream.
Apply a function to each RDD in this DStream. This is an output operator, so 'this' DStream will be registered as an output stream and therefore materialized.

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  30. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#foreachRDD\(foreachFunc:org.apache.spark.api.java.function.VoidFunction\[R\]\):Unit "Permalink") def foreachRDD(foreachFunc: [VoidFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/VoidFunction.html "org.apache.spark.api.java.function.VoidFunction")[[JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K, V]]): Unit
Apply a function to each RDD in this DStream.
Apply a function to each RDD in this DStream. This is an output operator, so 'this' DStream will be registered as an output stream and therefore materialized.

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  31. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#fullOuterJoin\[W\]\(other:org.apache.spark.streaming.api.java.JavaPairDStream\[K,W\],partitioner:org.apache.spark.Partitioner\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,\(org.apache.spark.api.java.Optional\[V\],org.apache.spark.api.java.Optional\[W\]\)\] "Permalink") def fullOuterJoin[W](other: [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, W], partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner")): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, ([Optional](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/Optional.html "org.apache.spark.api.java.Optional")[V], [Optional](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/Optional.html "org.apache.spark.api.java.Optional")[W])]
Return a new DStream by applying 'full outer join' between RDDs of `this` DStream and `other` DStream.
Return a new DStream by applying 'full outer join' between RDDs of `this` DStream and `other` DStream. The supplied org.apache.spark.Partitioner is used to control the partitioning of each RDD.
  32. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#fullOuterJoin\[W\]\(other:org.apache.spark.streaming.api.java.JavaPairDStream\[K,W\],numPartitions:Int\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,\(org.apache.spark.api.java.Optional\[V\],org.apache.spark.api.java.Optional\[W\]\)\] "Permalink") def fullOuterJoin[W](other: [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, W], numPartitions: Int): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, ([Optional](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/Optional.html "org.apache.spark.api.java.Optional")[V], [Optional](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/Optional.html "org.apache.spark.api.java.Optional")[W])]
Return a new DStream by applying 'full outer join' between RDDs of `this` DStream and `other` DStream.
Return a new DStream by applying 'full outer join' between RDDs of `this` DStream and `other` DStream. Hash partitioning is used to generate the RDDs with `numPartitions` partitions.
  33. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#fullOuterJoin\[W\]\(other:org.apache.spark.streaming.api.java.JavaPairDStream\[K,W\]\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,\(org.apache.spark.api.java.Optional\[V\],org.apache.spark.api.java.Optional\[W\]\)\] "Permalink") def fullOuterJoin[W](other: [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, W]): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, ([Optional](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/Optional.html "org.apache.spark.api.java.Optional")[V], [Optional](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/Optional.html "org.apache.spark.api.java.Optional")[W])]
Return a new DStream by applying 'full outer join' between RDDs of `this` DStream and `other` DStream.
Return a new DStream by applying 'full outer join' between RDDs of `this` DStream and `other` DStream. Hash partitioning is used to generate the RDDs with Spark's default number of partitions.
  34. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef]

Definition Classes
    AnyRef → Any

Annotations
     @IntrinsicCandidate() @native()
  35. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#glom\(\):org.apache.spark.streaming.api.java.JavaDStream\[java.util.List\[T\]\] "Permalink") def glom(): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#java.util.List "java.util.List")[(K, V)]]
Return a new DStream in which each RDD is generated by applying glom() to each RDD of this DStream.
Return a new DStream in which each RDD is generated by applying glom() to each RDD of this DStream. Applying glom() to an RDD coalesces all elements within each partition into an array.

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  36. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#groupByKey\(partitioner:org.apache.spark.Partitioner\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,Iterable\[V\]\] "Permalink") def groupByKey(partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner")): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, [Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html#java.lang.Iterable "java.lang.Iterable")[V]]
Return a new DStream by applying `groupByKey` on each RDD of `this` DStream.
Return a new DStream by applying `groupByKey` on each RDD of `this` DStream. Therefore, the values for each key in `this` DStream's RDDs are grouped into a single sequence to generate the RDDs of the new DStream. org.apache.spark.Partitioner is used to control the partitioning of each RDD.
  37. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#groupByKey\(numPartitions:Int\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,Iterable\[V\]\] "Permalink") def groupByKey(numPartitions: Int): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, [Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html#java.lang.Iterable "java.lang.Iterable")[V]]
Return a new DStream by applying `groupByKey` to each RDD.
Return a new DStream by applying `groupByKey` to each RDD. Hash partitioning is used to generate the RDDs with `numPartitions` partitions.
  38. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#groupByKey\(\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,Iterable\[V\]\] "Permalink") def groupByKey(): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, [Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html#java.lang.Iterable "java.lang.Iterable")[V]]
Return a new DStream by applying `groupByKey` to each RDD.
Return a new DStream by applying `groupByKey` to each RDD. Hash partitioning is used to generate the RDDs with Spark's default number of partitions.
  39. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#groupByKeyAndWindow\(windowDuration:org.apache.spark.streaming.Duration,slideDuration:org.apache.spark.streaming.Duration,partitioner:org.apache.spark.Partitioner\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,Iterable\[V\]\] "Permalink") def groupByKeyAndWindow(windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner")): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, [Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html#java.lang.Iterable "java.lang.Iterable")[V]]
Return a new DStream by applying `groupByKey` over a sliding window on `this` DStream.
Return a new DStream by applying `groupByKey` over a sliding window on `this` DStream. Similar to `DStream.groupByKey()`, but applies it over a sliding window.

windowDuration

width of the window; must be a multiple of this DStream's batching interval

slideDuration

sliding interval of the window (i.e., the interval after which the new DStream will generate RDDs); must be a multiple of this DStream's batching interval

partitioner

Partitioner for controlling the partitioning of each RDD in the new DStream.
  40. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#groupByKeyAndWindow\(windowDuration:org.apache.spark.streaming.Duration,slideDuration:org.apache.spark.streaming.Duration,numPartitions:Int\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,Iterable\[V\]\] "Permalink") def groupByKeyAndWindow(windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), numPartitions: Int): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, [Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html#java.lang.Iterable "java.lang.Iterable")[V]]
Return a new DStream by applying `groupByKey` over a sliding window on `this` DStream.
Return a new DStream by applying `groupByKey` over a sliding window on `this` DStream. Similar to `DStream.groupByKey()`, but applies it over a sliding window. Hash partitioning is used to generate the RDDs with `numPartitions` partitions.

windowDuration

width of the window; must be a multiple of this DStream's batching interval

slideDuration

sliding interval of the window (i.e., the interval after which the new DStream will generate RDDs); must be a multiple of this DStream's batching interval

numPartitions

Number of partitions of each RDD in the new DStream.
  41. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#groupByKeyAndWindow\(windowDuration:org.apache.spark.streaming.Duration,slideDuration:org.apache.spark.streaming.Duration\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,Iterable\[V\]\] "Permalink") def groupByKeyAndWindow(windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration")): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, [Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html#java.lang.Iterable "java.lang.Iterable")[V]]
Return a new DStream by applying `groupByKey` over a sliding window.
Return a new DStream by applying `groupByKey` over a sliding window. Similar to `DStream.groupByKey()`, but applies it over a sliding window. Hash partitioning is used to generate the RDDs with Spark's default number of partitions.

windowDuration

width of the window; must be a multiple of this DStream's batching interval

slideDuration

sliding interval of the window (i.e., the interval after which the new DStream will generate RDDs); must be a multiple of this DStream's batching interval
  42. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#groupByKeyAndWindow\(windowDuration:org.apache.spark.streaming.Duration\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,Iterable\[V\]\] "Permalink") def groupByKeyAndWindow(windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration")): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, [Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html#java.lang.Iterable "java.lang.Iterable")[V]]
Return a new DStream by applying `groupByKey` over a sliding window.
Return a new DStream by applying `groupByKey` over a sliding window. This is similar to `DStream.groupByKey()` but applies it over a sliding window. The new DStream generates RDDs with the same interval as this DStream. Hash partitioning is used to generate the RDDs with Spark's default number of partitions.

windowDuration

width of the window; must be a multiple of this DStream's batching interval
  43. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#hashCode\(\):Int "Permalink") def hashCode(): Int

Definition Classes
    AnyRef → Any

Annotations
     @IntrinsicCandidate() @native()
  44. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean

Definition Classes
    Any
  45. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#join\[W\]\(other:org.apache.spark.streaming.api.java.JavaPairDStream\[K,W\],partitioner:org.apache.spark.Partitioner\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,\(V,W\)\] "Permalink") def join[W](other: [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, W], partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner")): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, (V, W)]
Return a new DStream by applying 'join' between RDDs of `this` DStream and `other` DStream.
Return a new DStream by applying 'join' between RDDs of `this` DStream and `other` DStream. The supplied org.apache.spark.Partitioner is used to control the partitioning of each RDD.
  46. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#join\[W\]\(other:org.apache.spark.streaming.api.java.JavaPairDStream\[K,W\],numPartitions:Int\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,\(V,W\)\] "Permalink") def join[W](other: [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, W], numPartitions: Int): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, (V, W)]
Return a new DStream by applying 'join' between RDDs of `this` DStream and `other` DStream.
Return a new DStream by applying 'join' between RDDs of `this` DStream and `other` DStream. Hash partitioning is used to generate the RDDs with `numPartitions` partitions.
  47. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#join\[W\]\(other:org.apache.spark.streaming.api.java.JavaPairDStream\[K,W\]\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,\(V,W\)\] "Permalink") def join[W](other: [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, W]): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, (V, W)]
Return a new DStream by applying 'join' between RDDs of `this` DStream and `other` DStream.
Return a new DStream by applying 'join' between RDDs of `this` DStream and `other` DStream. Hash partitioning is used to generate the RDDs with Spark's default number of partitions.
  48. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#kManifest:scala.reflect.ClassTag\[K\] "Permalink") implicit  val kManifest: ClassTag[K]
  49. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#leftOuterJoin\[W\]\(other:org.apache.spark.streaming.api.java.JavaPairDStream\[K,W\],partitioner:org.apache.spark.Partitioner\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,\(V,org.apache.spark.api.java.Optional\[W\]\)\] "Permalink") def leftOuterJoin[W](other: [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, W], partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner")): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, (V, [Optional](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/Optional.html "org.apache.spark.api.java.Optional")[W])]
Return a new DStream by applying 'left outer join' between RDDs of `this` DStream and `other` DStream.
Return a new DStream by applying 'left outer join' between RDDs of `this` DStream and `other` DStream. The supplied org.apache.spark.Partitioner is used to control the partitioning of each RDD.
  50. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#leftOuterJoin\[W\]\(other:org.apache.spark.streaming.api.java.JavaPairDStream\[K,W\],numPartitions:Int\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,\(V,org.apache.spark.api.java.Optional\[W\]\)\] "Permalink") def leftOuterJoin[W](other: [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, W], numPartitions: Int): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, (V, [Optional](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/Optional.html "org.apache.spark.api.java.Optional")[W])]
Return a new DStream by applying 'left outer join' between RDDs of `this` DStream and `other` DStream.
Return a new DStream by applying 'left outer join' between RDDs of `this` DStream and `other` DStream. Hash partitioning is used to generate the RDDs with `numPartitions` partitions.
  51. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#leftOuterJoin\[W\]\(other:org.apache.spark.streaming.api.java.JavaPairDStream\[K,W\]\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,\(V,org.apache.spark.api.java.Optional\[W\]\)\] "Permalink") def leftOuterJoin[W](other: [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, W]): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, (V, [Optional](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/Optional.html "org.apache.spark.api.java.Optional")[W])]
Return a new DStream by applying 'left outer join' between RDDs of `this` DStream and `other` DStream.
Return a new DStream by applying 'left outer join' between RDDs of `this` DStream and `other` DStream. Hash partitioning is used to generate the RDDs with Spark's default number of partitions.
  52. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#map\[U\]\(f:org.apache.spark.api.java.function.Function\[T,U\]\):org.apache.spark.streaming.api.java.JavaDStream\[U\] "Permalink") def map[U](f: [Function](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function.html "org.apache.spark.api.java.function.Function")[(K, V), U]): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[U]
Return a new DStream by applying a function to all elements of this DStream.
Return a new DStream by applying a function to all elements of this DStream.

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  53. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#mapPartitions\[U\]\(f:org.apache.spark.api.java.function.FlatMapFunction\[java.util.Iterator\[T\],U\]\):org.apache.spark.streaming.api.java.JavaDStream\[U\] "Permalink") def mapPartitions[U](f: [FlatMapFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction.html "org.apache.spark.api.java.function.FlatMapFunction")[[Iterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html#java.util.Iterator "java.util.Iterator")[(K, V)], U]): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[U]
Return a new DStream in which each RDD is generated by applying mapPartitions() to each RDDs of this DStream.
Return a new DStream in which each RDD is generated by applying mapPartitions() to each RDDs of this DStream. Applying mapPartitions() to an RDD applies a function to each partition of the RDD.

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  54. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#mapPartitionsToPair\[K2,V2\]\(f:org.apache.spark.api.java.function.PairFlatMapFunction\[java.util.Iterator\[T\],K2,V2\]\):org.apache.spark.streaming.api.java.JavaPairDStream\[K2,V2\] "Permalink") def mapPartitionsToPair[K2, V2](f: [PairFlatMapFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/PairFlatMapFunction.html "org.apache.spark.api.java.function.PairFlatMapFunction")[[Iterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html#java.util.Iterator "java.util.Iterator")[(K, V)], K2, V2]): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K2, V2]
Return a new DStream in which each RDD is generated by applying mapPartitions() to each RDDs of this DStream.
Return a new DStream in which each RDD is generated by applying mapPartitions() to each RDDs of this DStream. Applying mapPartitions() to an RDD applies a function to each partition of the RDD.

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  55. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#mapToPair\[K2,V2\]\(f:org.apache.spark.api.java.function.PairFunction\[T,K2,V2\]\):org.apache.spark.streaming.api.java.JavaPairDStream\[K2,V2\] "Permalink") def mapToPair[K2, V2](f: [PairFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/PairFunction.html "org.apache.spark.api.java.function.PairFunction")[(K, V), K2, V2]): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K2, V2]
Return a new DStream by applying a function to all elements of this DStream.
Return a new DStream by applying a function to all elements of this DStream.

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  56. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#mapValues\[U\]\(f:org.apache.spark.api.java.function.Function\[V,U\]\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,U\] "Permalink") def mapValues[U](f: [Function](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function.html "org.apache.spark.api.java.function.Function")[V, U]): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, U]
Return a new DStream by applying a map function to the value of each key-value pairs in 'this' DStream without changing the key.
  57. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#mapWithState\[StateType,MappedType\]\(spec:org.apache.spark.streaming.StateSpec\[K,V,StateType,MappedType\]\):org.apache.spark.streaming.api.java.JavaMapWithStateDStream\[K,V,StateType,MappedType\] "Permalink") def mapWithState[StateType, MappedType](spec: [StateSpec](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StateSpec.html "org.apache.spark.streaming.StateSpec")[K, V, StateType, MappedType]): [JavaMapWithStateDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaMapWithStateDStream.html "org.apache.spark.streaming.api.java.JavaMapWithStateDStream")[K, V, StateType, MappedType]
Return a [JavaMapWithStateDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaMapWithStateDStream.html "org.apache.spark.streaming.api.java.JavaMapWithStateDStream") by applying a function to every key-value element of `this` stream, while maintaining some state data for each unique key.
Return a [JavaMapWithStateDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaMapWithStateDStream.html "org.apache.spark.streaming.api.java.JavaMapWithStateDStream") by applying a function to every key-value element of `this` stream, while maintaining some state data for each unique key. The mapping function and other specification (e.g. partitioners, timeouts, initial state data, etc.) of this transformation can be specified using `StateSpec` class. The state data is accessible in as a parameter of type `State` in the mapping function.
Example of using `mapWithState`:

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

StateType

Class type of the state data

MappedType

Class type of the mapped data

spec

Specification of this transformation
  58. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  59. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#notify\(\):Unit "Permalink") final  def notify(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  60. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  61. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#persist\(storageLevel:org.apache.spark.storage.StorageLevel\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,V\] "Permalink") def persist(storageLevel: [StorageLevel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StorageLevel.html "org.apache.spark.storage.StorageLevel")): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, V]
Persist the RDDs of this DStream with the given storage level
  62. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#persist\(\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,V\] "Permalink") def persist(): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, V]
Persist RDDs of this DStream with the default storage level (MEMORY_ONLY_SER)
  63. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#print\(num:Int\):Unit "Permalink") def print(num: Int): Unit
Print the first num elements of each RDD generated in this DStream.
Print the first num elements of each RDD generated in this DStream. This is an output operator, so this DStream will be registered as an output stream and there materialized.

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  64. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#print\(\):Unit "Permalink") def print(): Unit
Print the first ten elements of each RDD generated in this DStream.
Print the first ten elements of each RDD generated in this DStream. This is an output operator, so this DStream will be registered as an output stream and there materialized.

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  65. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#reduce\(f:org.apache.spark.api.java.function.Function2\[T,T,T\]\):org.apache.spark.streaming.api.java.JavaDStream\[T\] "Permalink") def reduce(f: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[(K, V), (K, V), (K, V)]): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[(K, V)]
Return a new DStream in which each RDD has a single element generated by reducing each RDD of this DStream.
Return a new DStream in which each RDD has a single element generated by reducing each RDD of this DStream.

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  66. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#reduceByKey\(func:org.apache.spark.api.java.function.Function2\[V,V,V\],partitioner:org.apache.spark.Partitioner\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,V\] "Permalink") def reduceByKey(func: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[V, V, V], partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner")): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, V]
Return a new DStream by applying `reduceByKey` to each RDD.
Return a new DStream by applying `reduceByKey` to each RDD. The values for each key are merged using the supplied reduce function. org.apache.spark.Partitioner is used to control the partitioning of each RDD.
  67. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#reduceByKey\(func:org.apache.spark.api.java.function.Function2\[V,V,V\],numPartitions:Int\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,V\] "Permalink") def reduceByKey(func: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[V, V, V], numPartitions: Int): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, V]
Return a new DStream by applying `reduceByKey` to each RDD.
Return a new DStream by applying `reduceByKey` to each RDD. The values for each key are merged using the supplied reduce function. Hash partitioning is used to generate the RDDs with `numPartitions` partitions.
  68. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#reduceByKey\(func:org.apache.spark.api.java.function.Function2\[V,V,V\]\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,V\] "Permalink") def reduceByKey(func: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[V, V, V]): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, V]
Return a new DStream by applying `reduceByKey` to each RDD.
Return a new DStream by applying `reduceByKey` to each RDD. The values for each key are merged using the associative and commutative reduce function. Hash partitioning is used to generate the RDDs with Spark's default number of partitions.
  69. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#reduceByKeyAndWindow\(reduceFunc:org.apache.spark.api.java.function.Function2\[V,V,V\],invReduceFunc:org.apache.spark.api.java.function.Function2\[V,V,V\],windowDuration:org.apache.spark.streaming.Duration,slideDuration:org.apache.spark.streaming.Duration,partitioner:org.apache.spark.Partitioner,filterFunc:org.apache.spark.api.java.function.Function\[\(K,V\),Boolean\]\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,V\] "Permalink") def reduceByKeyAndWindow(reduceFunc: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[V, V, V], invReduceFunc: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[V, V, V], windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner"), filterFunc: [Function](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function.html "org.apache.spark.api.java.function.Function")[(K, V), [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html#java.lang.Boolean "java.lang.Boolean")]): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, V]
Return a new DStream by applying incremental `reduceByKey` over a sliding window.
Return a new DStream by applying incremental `reduceByKey` over a sliding window. The reduced value of over a new window is calculated using the old window's reduce value :
    1. reduce the new values that entered the window (e.g., adding new counts) 2. "inverse reduce" the old values that left the window (e.g., subtracting old counts) This is more efficient that reduceByKeyAndWindow without "inverse reduce" function. However, it is applicable to only "invertible reduce functions".

reduceFunc

associative and commutative reduce function

invReduceFunc

inverse function

windowDuration

width of the window; must be a multiple of this DStream's batching interval

slideDuration

sliding interval of the window (i.e., the interval after which the new DStream will generate RDDs); must be a multiple of this DStream's batching interval

partitioner

Partitioner for controlling the partitioning of each RDD in the new DStream.

filterFunc

function to filter expired key-value pairs; only pairs that satisfy the function are retained set this to null if you do not want to filter
  70. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#reduceByKeyAndWindow\(reduceFunc:org.apache.spark.api.java.function.Function2\[V,V,V\],invReduceFunc:org.apache.spark.api.java.function.Function2\[V,V,V\],windowDuration:org.apache.spark.streaming.Duration,slideDuration:org.apache.spark.streaming.Duration,numPartitions:Int,filterFunc:org.apache.spark.api.java.function.Function\[\(K,V\),Boolean\]\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,V\] "Permalink") def reduceByKeyAndWindow(reduceFunc: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[V, V, V], invReduceFunc: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[V, V, V], windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), numPartitions: Int, filterFunc: [Function](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function.html "org.apache.spark.api.java.function.Function")[(K, V), [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html#java.lang.Boolean "java.lang.Boolean")]): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, V]
Return a new DStream by applying incremental `reduceByKey` over a sliding window.
Return a new DStream by applying incremental `reduceByKey` over a sliding window. The reduced value of over a new window is calculated using the old window's reduce value :
    1. reduce the new values that entered the window (e.g., adding new counts) 2. "inverse reduce" the old values that left the window (e.g., subtracting old counts) This is more efficient that reduceByKeyAndWindow without "inverse reduce" function. However, it is applicable to only "invertible reduce functions". Hash partitioning is used to generate the RDDs with `numPartitions` partitions.

reduceFunc

associative and commutative reduce function

invReduceFunc

inverse function

windowDuration

width of the window; must be a multiple of this DStream's batching interval

slideDuration

sliding interval of the window (i.e., the interval after which the new DStream will generate RDDs); must be a multiple of this DStream's batching interval

numPartitions

number of partitions of each RDD in the new DStream.

filterFunc

function to filter expired key-value pairs; only pairs that satisfy the function are retained set this to null if you do not want to filter
  71. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#reduceByKeyAndWindow\(reduceFunc:org.apache.spark.api.java.function.Function2\[V,V,V\],invReduceFunc:org.apache.spark.api.java.function.Function2\[V,V,V\],windowDuration:org.apache.spark.streaming.Duration,slideDuration:org.apache.spark.streaming.Duration\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,V\] "Permalink") def reduceByKeyAndWindow(reduceFunc: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[V, V, V], invReduceFunc: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[V, V, V], windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration")): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, V]
Return a new DStream by reducing over a using incremental computation.
Return a new DStream by reducing over a using incremental computation. The reduced value of over a new window is calculated using the old window's reduce value :
    1. reduce the new values that entered the window (e.g., adding new counts) 2. "inverse reduce" the old values that left the window (e.g., subtracting old counts) This is more efficient that reduceByKeyAndWindow without "inverse reduce" function. However, it is applicable to only "invertible reduce functions". Hash partitioning is used to generate the RDDs with Spark's default number of partitions.

reduceFunc

associative and commutative reduce function

invReduceFunc

inverse function; such that for all y, invertible x: `invReduceFunc(reduceFunc(x, y), x) = y`

windowDuration

width of the window; must be a multiple of this DStream's batching interval

slideDuration

sliding interval of the window (i.e., the interval after which the new DStream will generate RDDs); must be a multiple of this DStream's batching interval
  72. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#reduceByKeyAndWindow\(reduceFunc:org.apache.spark.api.java.function.Function2\[V,V,V\],windowDuration:org.apache.spark.streaming.Duration,slideDuration:org.apache.spark.streaming.Duration,partitioner:org.apache.spark.Partitioner\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,V\] "Permalink") def reduceByKeyAndWindow(reduceFunc: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[V, V, V], windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner")): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, V]
Return a new DStream by applying `reduceByKey` over a sliding window.
Return a new DStream by applying `reduceByKey` over a sliding window. Similar to `DStream.reduceByKey()`, but applies it over a sliding window.

reduceFunc

associative rand commutative educe function

windowDuration

width of the window; must be a multiple of this DStream's batching interval

slideDuration

sliding interval of the window (i.e., the interval after which the new DStream will generate RDDs); must be a multiple of this DStream's batching interval

partitioner

Partitioner for controlling the partitioning of each RDD in the new DStream.
  73. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#reduceByKeyAndWindow\(reduceFunc:org.apache.spark.api.java.function.Function2\[V,V,V\],windowDuration:org.apache.spark.streaming.Duration,slideDuration:org.apache.spark.streaming.Duration,numPartitions:Int\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,V\] "Permalink") def reduceByKeyAndWindow(reduceFunc: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[V, V, V], windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), numPartitions: Int): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, V]
Return a new DStream by applying `reduceByKey` over a sliding window.
Return a new DStream by applying `reduceByKey` over a sliding window. This is similar to `DStream.reduceByKey()` but applies it over a sliding window. Hash partitioning is used to generate the RDDs with `numPartitions` partitions.

reduceFunc

associative and commutative reduce function

windowDuration

width of the window; must be a multiple of this DStream's batching interval

slideDuration

sliding interval of the window (i.e., the interval after which the new DStream will generate RDDs); must be a multiple of this DStream's batching interval

numPartitions

Number of partitions of each RDD in the new DStream.
  74. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#reduceByKeyAndWindow\(reduceFunc:org.apache.spark.api.java.function.Function2\[V,V,V\],windowDuration:org.apache.spark.streaming.Duration,slideDuration:org.apache.spark.streaming.Duration\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,V\] "Permalink") def reduceByKeyAndWindow(reduceFunc: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[V, V, V], windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration")): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, V]
Return a new DStream by applying `reduceByKey` over a sliding window.
Return a new DStream by applying `reduceByKey` over a sliding window. This is similar to `DStream.reduceByKey()` but applies it over a sliding window. Hash partitioning is used to generate the RDDs with Spark's default number of partitions.

reduceFunc

associative and commutative reduce function

windowDuration

width of the window; must be a multiple of this DStream's batching interval

slideDuration

sliding interval of the window (i.e., the interval after which the new DStream will generate RDDs); must be a multiple of this DStream's batching interval
  75. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#reduceByKeyAndWindow\(reduceFunc:org.apache.spark.api.java.function.Function2\[V,V,V\],windowDuration:org.apache.spark.streaming.Duration\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,V\] "Permalink") def reduceByKeyAndWindow(reduceFunc: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[V, V, V], windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration")): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, V]
Create a new DStream by applying `reduceByKey` over a sliding window on `this` DStream.
Create a new DStream by applying `reduceByKey` over a sliding window on `this` DStream. Similar to `DStream.reduceByKey()`, but applies it over a sliding window. The new DStream generates RDDs with the same interval as this DStream. Hash partitioning is used to generate the RDDs with Spark's default number of partitions.

reduceFunc

associative and commutative reduce function

windowDuration

width of the window; must be a multiple of this DStream's batching interval
  76. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#reduceByWindow\(reduceFunc:org.apache.spark.api.java.function.Function2\[T,T,T\],invReduceFunc:org.apache.spark.api.java.function.Function2\[T,T,T\],windowDuration:org.apache.spark.streaming.Duration,slideDuration:org.apache.spark.streaming.Duration\):org.apache.spark.streaming.api.java.JavaDStream\[T\] "Permalink") def reduceByWindow(reduceFunc: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[(K, V), (K, V), (K, V)], invReduceFunc: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[(K, V), (K, V), (K, V)], windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration")): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[(K, V)]
Return a new DStream in which each RDD has a single element generated by reducing all elements in a sliding window over this DStream.
Return a new DStream in which each RDD has a single element generated by reducing all elements in a sliding window over this DStream. However, the reduction is done incrementally using the old window's reduced value :
    1. reduce the new values that entered the window (e.g., adding new counts) 2. "inverse reduce" the old values that left the window (e.g., subtracting old counts) This is more efficient than reduceByWindow without "inverse reduce" function. However, it is applicable to only "invertible reduce functions".

reduceFunc

associative and commutative reduce function

invReduceFunc

inverse reduce function; such that for all y, invertible x: `invReduceFunc(reduceFunc(x, y), x) = y`

windowDuration

width of the window; must be a multiple of this DStream's batching interval

slideDuration

sliding interval of the window (i.e., the interval after which the new DStream will generate RDDs); must be a multiple of this DStream's batching interval

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  77. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#reduceByWindow\(reduceFunc:org.apache.spark.api.java.function.Function2\[T,T,T\],windowDuration:org.apache.spark.streaming.Duration,slideDuration:org.apache.spark.streaming.Duration\):org.apache.spark.streaming.api.java.JavaDStream\[T\] "Permalink") def reduceByWindow(reduceFunc: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[(K, V), (K, V), (K, V)], windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration")): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[(K, V)]
Return a new DStream in which each RDD has a single element generated by reducing all elements in a sliding window over this DStream.
Return a new DStream in which each RDD has a single element generated by reducing all elements in a sliding window over this DStream.

reduceFunc

associative and commutative reduce function

windowDuration

width of the window; must be a multiple of this DStream's batching interval

slideDuration

sliding interval of the window (i.e., the interval after which the new DStream will generate RDDs); must be a multiple of this DStream's batching interval

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  78. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#repartition\(numPartitions:Int\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,V\] "Permalink") def repartition(numPartitions: Int): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, V]
Return a new DStream with an increased or decreased level of parallelism.
Return a new DStream with an increased or decreased level of parallelism. Each RDD in the returned DStream has exactly numPartitions partitions.
  79. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#rightOuterJoin\[W\]\(other:org.apache.spark.streaming.api.java.JavaPairDStream\[K,W\],partitioner:org.apache.spark.Partitioner\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,\(org.apache.spark.api.java.Optional\[V\],W\)\] "Permalink") def rightOuterJoin[W](other: [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, W], partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner")): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, ([Optional](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/Optional.html "org.apache.spark.api.java.Optional")[V], W)]
Return a new DStream by applying 'right outer join' between RDDs of `this` DStream and `other` DStream.
Return a new DStream by applying 'right outer join' between RDDs of `this` DStream and `other` DStream. The supplied org.apache.spark.Partitioner is used to control the partitioning of each RDD.
  80. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#rightOuterJoin\[W\]\(other:org.apache.spark.streaming.api.java.JavaPairDStream\[K,W\],numPartitions:Int\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,\(org.apache.spark.api.java.Optional\[V\],W\)\] "Permalink") def rightOuterJoin[W](other: [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, W], numPartitions: Int): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, ([Optional](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/Optional.html "org.apache.spark.api.java.Optional")[V], W)]
Return a new DStream by applying 'right outer join' between RDDs of `this` DStream and `other` DStream.
Return a new DStream by applying 'right outer join' between RDDs of `this` DStream and `other` DStream. Hash partitioning is used to generate the RDDs with `numPartitions` partitions.
  81. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#rightOuterJoin\[W\]\(other:org.apache.spark.streaming.api.java.JavaPairDStream\[K,W\]\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,\(org.apache.spark.api.java.Optional\[V\],W\)\] "Permalink") def rightOuterJoin[W](other: [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, W]): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, ([Optional](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/Optional.html "org.apache.spark.api.java.Optional")[V], W)]
Return a new DStream by applying 'right outer join' between RDDs of `this` DStream and `other` DStream.
Return a new DStream by applying 'right outer join' between RDDs of `this` DStream and `other` DStream. Hash partitioning is used to generate the RDDs with Spark's default number of partitions.
  82. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#saveAsHadoopFiles\[F<:org.apache.hadoop.mapred.OutputFormat\[_,_\]\]\(prefix:String,suffix:String,keyClass:Class\[_\],valueClass:Class\[_\],outputFormatClass:Class\[F\],conf:org.apache.hadoop.mapred.JobConf\):Unit "Permalink") def saveAsHadoopFiles[F <: OutputFormat[_, _]](prefix: String, suffix: String, keyClass: Class[_], valueClass: Class[_], outputFormatClass: Class[F], conf: JobConf): Unit
Save each RDD in `this` DStream as a Hadoop file.
Save each RDD in `this` DStream as a Hadoop file. The file name at each batch interval is generated based on `prefix` and `suffix`: "prefix-TIME_IN_MS.suffix".
  83. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#saveAsHadoopFiles\[F<:org.apache.hadoop.mapred.OutputFormat\[_,_\]\]\(prefix:String,suffix:String,keyClass:Class\[_\],valueClass:Class\[_\],outputFormatClass:Class\[F\]\):Unit "Permalink") def saveAsHadoopFiles[F <: OutputFormat[_, _]](prefix: String, suffix: String, keyClass: Class[_], valueClass: Class[_], outputFormatClass: Class[F]): Unit
Save each RDD in `this` DStream as a Hadoop file.
Save each RDD in `this` DStream as a Hadoop file. The file name at each batch interval is generated based on `prefix` and `suffix`: "prefix-TIME_IN_MS.suffix".
  84. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#saveAsHadoopFiles\(prefix:String,suffix:String\):Unit "Permalink") def saveAsHadoopFiles(prefix: String, suffix: String): Unit
Save each RDD in `this` DStream as a Hadoop file.
Save each RDD in `this` DStream as a Hadoop file. The file name at each batch interval is generated based on `prefix` and `suffix`: "prefix-TIME_IN_MS.suffix".
  85. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#saveAsNewAPIHadoopFiles\[F<:org.apache.hadoop.mapreduce.OutputFormat\[_,_\]\]\(prefix:String,suffix:String,keyClass:Class\[_\],valueClass:Class\[_\],outputFormatClass:Class\[F\],conf:org.apache.hadoop.conf.Configuration\):Unit "Permalink") def saveAsNewAPIHadoopFiles[F <: OutputFormat[_, _]](prefix: String, suffix: String, keyClass: Class[_], valueClass: Class[_], outputFormatClass: Class[F], conf: Configuration = [dstream.context.sparkContext.hadoopConfiguration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#dstream:org.apache.spark.streaming.dstream.DStream\[\(K,V\)\])): Unit
Save each RDD in `this` DStream as a Hadoop file.
Save each RDD in `this` DStream as a Hadoop file. The file name at each batch interval is generated based on `prefix` and `suffix`: "prefix-TIME_IN_MS.suffix".
  86. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#saveAsNewAPIHadoopFiles\[F<:org.apache.hadoop.mapreduce.OutputFormat\[_,_\]\]\(prefix:String,suffix:String,keyClass:Class\[_\],valueClass:Class\[_\],outputFormatClass:Class\[F\]\):Unit "Permalink") def saveAsNewAPIHadoopFiles[F <: OutputFormat[_, _]](prefix: String, suffix: String, keyClass: Class[_], valueClass: Class[_], outputFormatClass: Class[F]): Unit
Save each RDD in `this` DStream as a Hadoop file.
Save each RDD in `this` DStream as a Hadoop file. The file name at each batch interval is generated based on `prefix` and `suffix`: "prefix-TIME_IN_MS.suffix".
  87. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#saveAsNewAPIHadoopFiles\(prefix:String,suffix:String\):Unit "Permalink") def saveAsNewAPIHadoopFiles(prefix: String, suffix: String): Unit
Save each RDD in `this` DStream as a Hadoop file.
Save each RDD in `this` DStream as a Hadoop file. The file name at each batch interval is generated based on `prefix` and `suffix`: "prefix-TIME_IN_MS.suffix".
  88. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#scalaIntToJavaLong\(in:org.apache.spark.streaming.dstream.DStream\[Long\]\):org.apache.spark.streaming.api.java.JavaDStream\[Long\] "Permalink") implicit  def scalaIntToJavaLong(in: [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[Long]): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[[Long](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html#java.lang.Long "java.lang.Long")]

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  89. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#slice\(fromTime:org.apache.spark.streaming.Time,toTime:org.apache.spark.streaming.Time\):java.util.List\[R\] "Permalink") def slice(fromTime: [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time"), toTime: [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time")): [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#java.util.List "java.util.List")[[JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K, V]]
Return all the RDDs between 'fromDuration' to 'toDuration' (both included)
Return all the RDDs between 'fromDuration' to 'toDuration' (both included)

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  90. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0

Definition Classes
    AnyRef
  91. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#toJavaDStream\(\):org.apache.spark.streaming.api.java.JavaDStream\[\(K,V\)\] "Permalink") def toJavaDStream(): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[(K, V)]
Convert to a JavaDStream
  92. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#toString\(\):String "Permalink") def toString(): [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String")

Definition Classes
    AnyRef → Any
  93. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#transform\[U\]\(transformFunc:org.apache.spark.api.java.function.Function2\[R,org.apache.spark.streaming.Time,org.apache.spark.api.java.JavaRDD\[U\]\]\):org.apache.spark.streaming.api.java.JavaDStream\[U\] "Permalink") def transform[U](transformFunc: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[[JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K, V], [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time"), [JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[U]]): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[U]
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream.
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream.

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  94. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#transform\[U\]\(transformFunc:org.apache.spark.api.java.function.Function\[R,org.apache.spark.api.java.JavaRDD\[U\]\]\):org.apache.spark.streaming.api.java.JavaDStream\[U\] "Permalink") def transform[U](transformFunc: [Function](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function.html "org.apache.spark.api.java.function.Function")[[JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K, V], [JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[U]]): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[U]
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream.
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream.

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  95. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#transformToPair\[K2,V2\]\(transformFunc:org.apache.spark.api.java.function.Function2\[R,org.apache.spark.streaming.Time,org.apache.spark.api.java.JavaPairRDD\[K2,V2\]\]\):org.apache.spark.streaming.api.java.JavaPairDStream\[K2,V2\] "Permalink") def transformToPair[K2, V2](transformFunc: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[[JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K, V], [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time"), [JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K2, V2]]): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K2, V2]
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream.
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream.

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  96. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#transformToPair\[K2,V2\]\(transformFunc:org.apache.spark.api.java.function.Function\[R,org.apache.spark.api.java.JavaPairRDD\[K2,V2\]\]\):org.apache.spark.streaming.api.java.JavaPairDStream\[K2,V2\] "Permalink") def transformToPair[K2, V2](transformFunc: [Function](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function.html "org.apache.spark.api.java.function.Function")[[JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K, V], [JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K2, V2]]): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K2, V2]
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream.
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream.

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  97. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#transformWith\[K2,V2,W\]\(other:org.apache.spark.streaming.api.java.JavaPairDStream\[K2,V2\],transformFunc:org.apache.spark.api.java.function.Function3\[R,org.apache.spark.api.java.JavaPairRDD\[K2,V2\],org.apache.spark.streaming.Time,org.apache.spark.api.java.JavaRDD\[W\]\]\):org.apache.spark.streaming.api.java.JavaDStream\[W\] "Permalink") def transformWith[K2, V2, W](other: [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K2, V2], transformFunc: [Function3](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function3.html "org.apache.spark.api.java.function.Function3")[[JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K, V], [JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K2, V2], [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time"), [JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[W]]): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[W]
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream and 'other' DStream.
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream and 'other' DStream.

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  98. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#transformWith\[U,W\]\(other:org.apache.spark.streaming.api.java.JavaDStream\[U\],transformFunc:org.apache.spark.api.java.function.Function3\[R,org.apache.spark.api.java.JavaRDD\[U\],org.apache.spark.streaming.Time,org.apache.spark.api.java.JavaRDD\[W\]\]\):org.apache.spark.streaming.api.java.JavaDStream\[W\] "Permalink") def transformWith[U, W](other: [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[U], transformFunc: [Function3](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function3.html "org.apache.spark.api.java.function.Function3")[[JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K, V], [JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[U], [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time"), [JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[W]]): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[W]
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream and 'other' DStream.
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream and 'other' DStream.

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  99. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#transformWithToPair\[K2,V2,K3,V3\]\(other:org.apache.spark.streaming.api.java.JavaPairDStream\[K2,V2\],transformFunc:org.apache.spark.api.java.function.Function3\[R,org.apache.spark.api.java.JavaPairRDD\[K2,V2\],org.apache.spark.streaming.Time,org.apache.spark.api.java.JavaPairRDD\[K3,V3\]\]\):org.apache.spark.streaming.api.java.JavaPairDStream\[K3,V3\] "Permalink") def transformWithToPair[K2, V2, K3, V3](other: [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K2, V2], transformFunc: [Function3](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function3.html "org.apache.spark.api.java.function.Function3")[[JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K, V], [JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K2, V2], [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time"), [JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K3, V3]]): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K3, V3]
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream and 'other' DStream.
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream and 'other' DStream.

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  100. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#transformWithToPair\[U,K2,V2\]\(other:org.apache.spark.streaming.api.java.JavaDStream\[U\],transformFunc:org.apache.spark.api.java.function.Function3\[R,org.apache.spark.api.java.JavaRDD\[U\],org.apache.spark.streaming.Time,org.apache.spark.api.java.JavaPairRDD\[K2,V2\]\]\):org.apache.spark.streaming.api.java.JavaPairDStream\[K2,V2\] "Permalink") def transformWithToPair[U, K2, V2](other: [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[U], transformFunc: [Function3](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function3.html "org.apache.spark.api.java.function.Function3")[[JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K, V], [JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[U], [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time"), [JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K2, V2]]): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K2, V2]
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream and 'other' DStream.
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream and 'other' DStream.

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  101. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#union\(that:org.apache.spark.streaming.api.java.JavaPairDStream\[K,V\]\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,V\] "Permalink") def union(that: [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, V]): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, V]
Return a new DStream by unifying data of another DStream with this DStream.
Return a new DStream by unifying data of another DStream with this DStream.

that

Another DStream having the same interval (i.e., slideDuration) as this DStream.
  102. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#updateStateByKey\[S\]\(updateFunc:org.apache.spark.api.java.function.Function2\[java.util.List\[V\],org.apache.spark.api.java.Optional\[S\],org.apache.spark.api.java.Optional\[S\]\],partitioner:org.apache.spark.Partitioner,initialRDD:org.apache.spark.api.java.JavaPairRDD\[K,S\]\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,S\] "Permalink") def updateStateByKey[S](updateFunc: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#java.util.List "java.util.List")[V], [Optional](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/Optional.html "org.apache.spark.api.java.Optional")[S], [Optional](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/Optional.html "org.apache.spark.api.java.Optional")[S]], partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner"), initialRDD: [JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K, S]): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, S]
Return a new "state" DStream where the state for each key is updated by applying the given function on the previous state of the key and the new values of the key.
Return a new "state" DStream where the state for each key is updated by applying the given function on the previous state of the key and the new values of the key. org.apache.spark.Partitioner is used to control the partitioning of each RDD.

S

State type

updateFunc

State update function. If `this` function returns None, then corresponding state key-value pair will be eliminated.

partitioner

Partitioner for controlling the partitioning of each RDD in the new DStream.

initialRDD

initial state value of each key.
  103. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#updateStateByKey\[S\]\(updateFunc:org.apache.spark.api.java.function.Function2\[java.util.List\[V\],org.apache.spark.api.java.Optional\[S\],org.apache.spark.api.java.Optional\[S\]\],partitioner:org.apache.spark.Partitioner\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,S\] "Permalink") def updateStateByKey[S](updateFunc: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#java.util.List "java.util.List")[V], [Optional](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/Optional.html "org.apache.spark.api.java.Optional")[S], [Optional](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/Optional.html "org.apache.spark.api.java.Optional")[S]], partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner")): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, S]
Return a new "state" DStream where the state for each key is updated by applying the given function on the previous state of the key and the new values of the key.
Return a new "state" DStream where the state for each key is updated by applying the given function on the previous state of the key and the new values of the key. org.apache.spark.Partitioner is used to control the partitioning of each RDD.

S

State type

updateFunc

State update function. If `this` function returns None, then corresponding state key-value pair will be eliminated.

partitioner

Partitioner for controlling the partitioning of each RDD in the new DStream.
  104. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#updateStateByKey\[S\]\(updateFunc:org.apache.spark.api.java.function.Function2\[java.util.List\[V\],org.apache.spark.api.java.Optional\[S\],org.apache.spark.api.java.Optional\[S\]\],numPartitions:Int\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,S\] "Permalink") def updateStateByKey[S](updateFunc: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#java.util.List "java.util.List")[V], [Optional](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/Optional.html "org.apache.spark.api.java.Optional")[S], [Optional](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/Optional.html "org.apache.spark.api.java.Optional")[S]], numPartitions: Int): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, S]
Return a new "state" DStream where the state for each key is updated by applying the given function on the previous state of the key and the new values of each key.
Return a new "state" DStream where the state for each key is updated by applying the given function on the previous state of the key and the new values of each key. Hash partitioning is used to generate the RDDs with `numPartitions` partitions.

S

State type

updateFunc

State update function. If `this` function returns None, then corresponding state key-value pair will be eliminated.

numPartitions

Number of partitions of each RDD in the new DStream.
  105. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#updateStateByKey\[S\]\(updateFunc:org.apache.spark.api.java.function.Function2\[java.util.List\[V\],org.apache.spark.api.java.Optional\[S\],org.apache.spark.api.java.Optional\[S\]\]\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,S\] "Permalink") def updateStateByKey[S](updateFunc: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#java.util.List "java.util.List")[V], [Optional](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/Optional.html "org.apache.spark.api.java.Optional")[S], [Optional](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/Optional.html "org.apache.spark.api.java.Optional")[S]]): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, S]
Return a new "state" DStream where the state for each key is updated by applying the given function on the previous state of the key and the new values of each key.
Return a new "state" DStream where the state for each key is updated by applying the given function on the previous state of the key and the new values of each key. Hash partitioning is used to generate the RDDs with Spark's default number of partitions.

S

State type

updateFunc

State update function. If `this` function returns None, then corresponding state key-value pair will be eliminated.
  106. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#vManifest:scala.reflect.ClassTag\[V\] "Permalink") implicit  val vManifest: ClassTag[V]
  107. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])
  108. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  109. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#wait\(\):Unit "Permalink") final  def wait(): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])
  110. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#window\(windowDuration:org.apache.spark.streaming.Duration,slideDuration:org.apache.spark.streaming.Duration\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,V\] "Permalink") def window(windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration")): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, V]
Return a new DStream which is computed based on windowed batches of this DStream.
Return a new DStream which is computed based on windowed batches of this DStream.

windowDuration

duration (i.e., width) of the window; must be a multiple of this DStream's interval

slideDuration

sliding interval of the window (i.e., the interval after which the new DStream will generate RDDs); must be a multiple of this DStream's interval
  111. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#window\(windowDuration:org.apache.spark.streaming.Duration\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,V\] "Permalink") def window(windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration")): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, V]
Return a new DStream which is computed based on windowed batches of this DStream.
Return a new DStream which is computed based on windowed batches of this DStream. The new DStream generates RDDs with the same interval as this DStream.

windowDuration

width of the window; must be a multiple of this DStream's interval.
  112. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#wrapRDD\(rdd:org.apache.spark.rdd.RDD\[\(K,V\)\]\):org.apache.spark.api.java.JavaPairRDD\[K,V\] "Permalink") def wrapRDD(rdd: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, V)]): [JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K, V]

Definition Classes
     [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream") → [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")

### Deprecated Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#finalize\(\):Unit "Permalink") def finalize(): Unit

Attributes
    protected[lang]

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.Throwable]) @Deprecated

Deprecated

_(Since version 9)_

### Inherited from [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")[(K, V), [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, V], [JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K, V]]
### Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#checkpoint\(interval:org.apache.spark.streaming.Duration\):org.apache.spark.streaming.dstream.DStream\[T\] "Permalink") def checkpoint(interval: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration")): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, V)]
Enable periodic checkpointing of RDDs of this DStream.
Enable periodic checkpointing of RDDs of this DStream.

interval

Time interval after which generated RDD will be checkpointed

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#context\(\):org.apache.spark.streaming.StreamingContext "Permalink") def context(): [StreamingContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html "org.apache.spark.streaming.StreamingContext")
Return the [org.apache.spark.streaming.StreamingContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html "org.apache.spark.streaming.StreamingContext") associated with this DStream
Return the [org.apache.spark.streaming.StreamingContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html "org.apache.spark.streaming.StreamingContext") associated with this DStream

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#count\(\):org.apache.spark.streaming.api.java.JavaDStream\[Long\] "Permalink") def count(): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[[Long](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html#java.lang.Long "java.lang.Long")]
Return a new DStream in which each RDD has a single element generated by counting each RDD of this DStream.
Return a new DStream in which each RDD has a single element generated by counting each RDD of this DStream.

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#countByValue\(numPartitions:Int\):org.apache.spark.streaming.api.java.JavaPairDStream\[T,Long\] "Permalink") def countByValue(numPartitions: Int): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[(K, V), [Long](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html#java.lang.Long "java.lang.Long")]
Return a new DStream in which each RDD contains the counts of each distinct value in each RDD of this DStream.
Return a new DStream in which each RDD contains the counts of each distinct value in each RDD of this DStream. Hash partitioning is used to generate the RDDs with `numPartitions` partitions.

numPartitions

number of partitions of each RDD in the new DStream.

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#countByValue\(\):org.apache.spark.streaming.api.java.JavaPairDStream\[T,Long\] "Permalink") def countByValue(): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[(K, V), [Long](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html#java.lang.Long "java.lang.Long")]
Return a new DStream in which each RDD contains the counts of each distinct value in each RDD of this DStream.
Return a new DStream in which each RDD contains the counts of each distinct value in each RDD of this DStream. Hash partitioning is used to generate the RDDs with Spark's default number of partitions.

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#countByValueAndWindow\(windowDuration:org.apache.spark.streaming.Duration,slideDuration:org.apache.spark.streaming.Duration,numPartitions:Int\):org.apache.spark.streaming.api.java.JavaPairDStream\[T,Long\] "Permalink") def countByValueAndWindow(windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), numPartitions: Int): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[(K, V), [Long](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html#java.lang.Long "java.lang.Long")]
Return a new DStream in which each RDD contains the count of distinct elements in RDDs in a sliding window over this DStream.
Return a new DStream in which each RDD contains the count of distinct elements in RDDs in a sliding window over this DStream. Hash partitioning is used to generate the RDDs with `numPartitions` partitions.

windowDuration

width of the window; must be a multiple of this DStream's batching interval

slideDuration

sliding interval of the window (i.e., the interval after which the new DStream will generate RDDs); must be a multiple of this DStream's batching interval

numPartitions

number of partitions of each RDD in the new DStream.

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#countByValueAndWindow\(windowDuration:org.apache.spark.streaming.Duration,slideDuration:org.apache.spark.streaming.Duration\):org.apache.spark.streaming.api.java.JavaPairDStream\[T,Long\] "Permalink") def countByValueAndWindow(windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration")): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[(K, V), [Long](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html#java.lang.Long "java.lang.Long")]
Return a new DStream in which each RDD contains the count of distinct elements in RDDs in a sliding window over this DStream.
Return a new DStream in which each RDD contains the count of distinct elements in RDDs in a sliding window over this DStream. Hash partitioning is used to generate the RDDs with Spark's default number of partitions.

windowDuration

width of the window; must be a multiple of this DStream's batching interval

slideDuration

sliding interval of the window (i.e., the interval after which the new DStream will generate RDDs); must be a multiple of this DStream's batching interval

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#countByWindow\(windowDuration:org.apache.spark.streaming.Duration,slideDuration:org.apache.spark.streaming.Duration\):org.apache.spark.streaming.api.java.JavaDStream\[Long\] "Permalink") def countByWindow(windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration")): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[[Long](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html#java.lang.Long "java.lang.Long")]
Return a new DStream in which each RDD has a single element generated by counting the number of elements in a window over this DStream.
Return a new DStream in which each RDD has a single element generated by counting the number of elements in a window over this DStream. windowDuration and slideDuration are as defined in the window() operation. This is equivalent to window(windowDuration, slideDuration).count()

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#flatMap\[U\]\(f:org.apache.spark.api.java.function.FlatMapFunction\[T,U\]\):org.apache.spark.streaming.api.java.JavaDStream\[U\] "Permalink") def flatMap[U](f: [FlatMapFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction.html "org.apache.spark.api.java.function.FlatMapFunction")[(K, V), U]): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[U]
Return a new DStream by applying a function to all elements of this DStream, and then flattening the results
Return a new DStream by applying a function to all elements of this DStream, and then flattening the results

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#flatMapToPair\[K2,V2\]\(f:org.apache.spark.api.java.function.PairFlatMapFunction\[T,K2,V2\]\):org.apache.spark.streaming.api.java.JavaPairDStream\[K2,V2\] "Permalink") def flatMapToPair[K2, V2](f: [PairFlatMapFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/PairFlatMapFunction.html "org.apache.spark.api.java.function.PairFlatMapFunction")[(K, V), K2, V2]): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K2, V2]
Return a new DStream by applying a function to all elements of this DStream, and then flattening the results
Return a new DStream by applying a function to all elements of this DStream, and then flattening the results

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#foreachRDD\(foreachFunc:org.apache.spark.api.java.function.VoidFunction2\[R,org.apache.spark.streaming.Time\]\):Unit "Permalink") def foreachRDD(foreachFunc: [VoidFunction2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/VoidFunction2.html "org.apache.spark.api.java.function.VoidFunction2")[[JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K, V], [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time")]): Unit
Apply a function to each RDD in this DStream.
Apply a function to each RDD in this DStream. This is an output operator, so 'this' DStream will be registered as an output stream and therefore materialized.

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#foreachRDD\(foreachFunc:org.apache.spark.api.java.function.VoidFunction\[R\]\):Unit "Permalink") def foreachRDD(foreachFunc: [VoidFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/VoidFunction.html "org.apache.spark.api.java.function.VoidFunction")[[JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K, V]]): Unit
Apply a function to each RDD in this DStream.
Apply a function to each RDD in this DStream. This is an output operator, so 'this' DStream will be registered as an output stream and therefore materialized.

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#glom\(\):org.apache.spark.streaming.api.java.JavaDStream\[java.util.List\[T\]\] "Permalink") def glom(): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#java.util.List "java.util.List")[(K, V)]]
Return a new DStream in which each RDD is generated by applying glom() to each RDD of this DStream.
Return a new DStream in which each RDD is generated by applying glom() to each RDD of this DStream. Applying glom() to an RDD coalesces all elements within each partition into an array.

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#map\[U\]\(f:org.apache.spark.api.java.function.Function\[T,U\]\):org.apache.spark.streaming.api.java.JavaDStream\[U\] "Permalink") def map[U](f: [Function](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function.html "org.apache.spark.api.java.function.Function")[(K, V), U]): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[U]
Return a new DStream by applying a function to all elements of this DStream.
Return a new DStream by applying a function to all elements of this DStream.

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#mapPartitions\[U\]\(f:org.apache.spark.api.java.function.FlatMapFunction\[java.util.Iterator\[T\],U\]\):org.apache.spark.streaming.api.java.JavaDStream\[U\] "Permalink") def mapPartitions[U](f: [FlatMapFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction.html "org.apache.spark.api.java.function.FlatMapFunction")[[Iterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html#java.util.Iterator "java.util.Iterator")[(K, V)], U]): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[U]
Return a new DStream in which each RDD is generated by applying mapPartitions() to each RDDs of this DStream.
Return a new DStream in which each RDD is generated by applying mapPartitions() to each RDDs of this DStream. Applying mapPartitions() to an RDD applies a function to each partition of the RDD.

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#mapPartitionsToPair\[K2,V2\]\(f:org.apache.spark.api.java.function.PairFlatMapFunction\[java.util.Iterator\[T\],K2,V2\]\):org.apache.spark.streaming.api.java.JavaPairDStream\[K2,V2\] "Permalink") def mapPartitionsToPair[K2, V2](f: [PairFlatMapFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/PairFlatMapFunction.html "org.apache.spark.api.java.function.PairFlatMapFunction")[[Iterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html#java.util.Iterator "java.util.Iterator")[(K, V)], K2, V2]): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K2, V2]
Return a new DStream in which each RDD is generated by applying mapPartitions() to each RDDs of this DStream.
Return a new DStream in which each RDD is generated by applying mapPartitions() to each RDDs of this DStream. Applying mapPartitions() to an RDD applies a function to each partition of the RDD.

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#mapToPair\[K2,V2\]\(f:org.apache.spark.api.java.function.PairFunction\[T,K2,V2\]\):org.apache.spark.streaming.api.java.JavaPairDStream\[K2,V2\] "Permalink") def mapToPair[K2, V2](f: [PairFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/PairFunction.html "org.apache.spark.api.java.function.PairFunction")[(K, V), K2, V2]): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K2, V2]
Return a new DStream by applying a function to all elements of this DStream.
Return a new DStream by applying a function to all elements of this DStream.

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#print\(num:Int\):Unit "Permalink") def print(num: Int): Unit
Print the first num elements of each RDD generated in this DStream.
Print the first num elements of each RDD generated in this DStream. This is an output operator, so this DStream will be registered as an output stream and there materialized.

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#print\(\):Unit "Permalink") def print(): Unit
Print the first ten elements of each RDD generated in this DStream.
Print the first ten elements of each RDD generated in this DStream. This is an output operator, so this DStream will be registered as an output stream and there materialized.

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#reduce\(f:org.apache.spark.api.java.function.Function2\[T,T,T\]\):org.apache.spark.streaming.api.java.JavaDStream\[T\] "Permalink") def reduce(f: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[(K, V), (K, V), (K, V)]): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[(K, V)]
Return a new DStream in which each RDD has a single element generated by reducing each RDD of this DStream.
Return a new DStream in which each RDD has a single element generated by reducing each RDD of this DStream.

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#reduceByWindow\(reduceFunc:org.apache.spark.api.java.function.Function2\[T,T,T\],invReduceFunc:org.apache.spark.api.java.function.Function2\[T,T,T\],windowDuration:org.apache.spark.streaming.Duration,slideDuration:org.apache.spark.streaming.Duration\):org.apache.spark.streaming.api.java.JavaDStream\[T\] "Permalink") def reduceByWindow(reduceFunc: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[(K, V), (K, V), (K, V)], invReduceFunc: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[(K, V), (K, V), (K, V)], windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration")): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[(K, V)]
Return a new DStream in which each RDD has a single element generated by reducing all elements in a sliding window over this DStream.
Return a new DStream in which each RDD has a single element generated by reducing all elements in a sliding window over this DStream. However, the reduction is done incrementally using the old window's reduced value :
    1. reduce the new values that entered the window (e.g., adding new counts) 2. "inverse reduce" the old values that left the window (e.g., subtracting old counts) This is more efficient than reduceByWindow without "inverse reduce" function. However, it is applicable to only "invertible reduce functions".

reduceFunc

associative and commutative reduce function

invReduceFunc

inverse reduce function; such that for all y, invertible x: `invReduceFunc(reduceFunc(x, y), x) = y`

windowDuration

width of the window; must be a multiple of this DStream's batching interval

slideDuration

sliding interval of the window (i.e., the interval after which the new DStream will generate RDDs); must be a multiple of this DStream's batching interval

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#reduceByWindow\(reduceFunc:org.apache.spark.api.java.function.Function2\[T,T,T\],windowDuration:org.apache.spark.streaming.Duration,slideDuration:org.apache.spark.streaming.Duration\):org.apache.spark.streaming.api.java.JavaDStream\[T\] "Permalink") def reduceByWindow(reduceFunc: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[(K, V), (K, V), (K, V)], windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration")): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[(K, V)]
Return a new DStream in which each RDD has a single element generated by reducing all elements in a sliding window over this DStream.
Return a new DStream in which each RDD has a single element generated by reducing all elements in a sliding window over this DStream.

reduceFunc

associative and commutative reduce function

windowDuration

width of the window; must be a multiple of this DStream's batching interval

slideDuration

sliding interval of the window (i.e., the interval after which the new DStream will generate RDDs); must be a multiple of this DStream's batching interval

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  23. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#scalaIntToJavaLong\(in:org.apache.spark.streaming.dstream.DStream\[Long\]\):org.apache.spark.streaming.api.java.JavaDStream\[Long\] "Permalink") implicit  def scalaIntToJavaLong(in: [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[Long]): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[[Long](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html#java.lang.Long "java.lang.Long")]

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  24. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#slice\(fromTime:org.apache.spark.streaming.Time,toTime:org.apache.spark.streaming.Time\):java.util.List\[R\] "Permalink") def slice(fromTime: [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time"), toTime: [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time")): [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#java.util.List "java.util.List")[[JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K, V]]
Return all the RDDs between 'fromDuration' to 'toDuration' (both included)
Return all the RDDs between 'fromDuration' to 'toDuration' (both included)

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  25. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#transform\[U\]\(transformFunc:org.apache.spark.api.java.function.Function2\[R,org.apache.spark.streaming.Time,org.apache.spark.api.java.JavaRDD\[U\]\]\):org.apache.spark.streaming.api.java.JavaDStream\[U\] "Permalink") def transform[U](transformFunc: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[[JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K, V], [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time"), [JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[U]]): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[U]
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream.
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream.

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  26. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#transform\[U\]\(transformFunc:org.apache.spark.api.java.function.Function\[R,org.apache.spark.api.java.JavaRDD\[U\]\]\):org.apache.spark.streaming.api.java.JavaDStream\[U\] "Permalink") def transform[U](transformFunc: [Function](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function.html "org.apache.spark.api.java.function.Function")[[JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K, V], [JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[U]]): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[U]
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream.
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream.

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  27. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#transformToPair\[K2,V2\]\(transformFunc:org.apache.spark.api.java.function.Function2\[R,org.apache.spark.streaming.Time,org.apache.spark.api.java.JavaPairRDD\[K2,V2\]\]\):org.apache.spark.streaming.api.java.JavaPairDStream\[K2,V2\] "Permalink") def transformToPair[K2, V2](transformFunc: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[[JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K, V], [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time"), [JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K2, V2]]): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K2, V2]
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream.
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream.

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  28. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#transformToPair\[K2,V2\]\(transformFunc:org.apache.spark.api.java.function.Function\[R,org.apache.spark.api.java.JavaPairRDD\[K2,V2\]\]\):org.apache.spark.streaming.api.java.JavaPairDStream\[K2,V2\] "Permalink") def transformToPair[K2, V2](transformFunc: [Function](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function.html "org.apache.spark.api.java.function.Function")[[JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K, V], [JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K2, V2]]): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K2, V2]
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream.
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream.

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  29. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#transformWith\[K2,V2,W\]\(other:org.apache.spark.streaming.api.java.JavaPairDStream\[K2,V2\],transformFunc:org.apache.spark.api.java.function.Function3\[R,org.apache.spark.api.java.JavaPairRDD\[K2,V2\],org.apache.spark.streaming.Time,org.apache.spark.api.java.JavaRDD\[W\]\]\):org.apache.spark.streaming.api.java.JavaDStream\[W\] "Permalink") def transformWith[K2, V2, W](other: [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K2, V2], transformFunc: [Function3](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function3.html "org.apache.spark.api.java.function.Function3")[[JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K, V], [JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K2, V2], [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time"), [JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[W]]): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[W]
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream and 'other' DStream.
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream and 'other' DStream.

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  30. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#transformWith\[U,W\]\(other:org.apache.spark.streaming.api.java.JavaDStream\[U\],transformFunc:org.apache.spark.api.java.function.Function3\[R,org.apache.spark.api.java.JavaRDD\[U\],org.apache.spark.streaming.Time,org.apache.spark.api.java.JavaRDD\[W\]\]\):org.apache.spark.streaming.api.java.JavaDStream\[W\] "Permalink") def transformWith[U, W](other: [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[U], transformFunc: [Function3](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function3.html "org.apache.spark.api.java.function.Function3")[[JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K, V], [JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[U], [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time"), [JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[W]]): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[W]
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream and 'other' DStream.
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream and 'other' DStream.

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  31. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#transformWithToPair\[K2,V2,K3,V3\]\(other:org.apache.spark.streaming.api.java.JavaPairDStream\[K2,V2\],transformFunc:org.apache.spark.api.java.function.Function3\[R,org.apache.spark.api.java.JavaPairRDD\[K2,V2\],org.apache.spark.streaming.Time,org.apache.spark.api.java.JavaPairRDD\[K3,V3\]\]\):org.apache.spark.streaming.api.java.JavaPairDStream\[K3,V3\] "Permalink") def transformWithToPair[K2, V2, K3, V3](other: [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K2, V2], transformFunc: [Function3](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function3.html "org.apache.spark.api.java.function.Function3")[[JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K, V], [JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K2, V2], [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time"), [JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K3, V3]]): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K3, V3]
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream and 'other' DStream.
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream and 'other' DStream.

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  32. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#transformWithToPair\[U,K2,V2\]\(other:org.apache.spark.streaming.api.java.JavaDStream\[U\],transformFunc:org.apache.spark.api.java.function.Function3\[R,org.apache.spark.api.java.JavaRDD\[U\],org.apache.spark.streaming.Time,org.apache.spark.api.java.JavaPairRDD\[K2,V2\]\]\):org.apache.spark.streaming.api.java.JavaPairDStream\[K2,V2\] "Permalink") def transformWithToPair[U, K2, V2](other: [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[U], transformFunc: [Function3](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function3.html "org.apache.spark.api.java.function.Function3")[[JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K, V], [JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[U], [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time"), [JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K2, V2]]): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K2, V2]
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream and 'other' DStream.
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream and 'other' DStream.

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")

### Inherited from AnyRef
### Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html###:Int "Permalink") final  def ##: Int

Definition Classes
    AnyRef → Any
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#clone\(\):Object "Permalink") def clone(): AnyRef

Attributes
    protected[lang]

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#equals\(x$1:Object\):Boolean "Permalink") def equals(arg0: AnyRef): Boolean

Definition Classes
    AnyRef → Any
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef]

Definition Classes
    AnyRef → Any

Annotations
     @IntrinsicCandidate() @native()
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#hashCode\(\):Int "Permalink") def hashCode(): Int

Definition Classes
    AnyRef → Any

Annotations
     @IntrinsicCandidate() @native()
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#notify\(\):Unit "Permalink") final  def notify(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0

Definition Classes
    AnyRef
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#toString\(\):String "Permalink") def toString(): [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String")

Definition Classes
    AnyRef → Any
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#wait\(\):Unit "Permalink") final  def wait(): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#finalize\(\):Unit "Permalink") def finalize(): Unit

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
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0

Definition Classes
    Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean

Definition Classes
    Any

### Ungrouped
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html###:Int "Permalink") final  def ##: Int

Definition Classes
    AnyRef → Any
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0

Definition Classes
    Any
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#cache\(\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,V\] "Permalink") def cache(): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, V]
Persist RDDs of this DStream with the default storage level (MEMORY_ONLY_SER)
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#checkpoint\(interval:org.apache.spark.streaming.Duration\):org.apache.spark.streaming.dstream.DStream\[T\] "Permalink") def checkpoint(interval: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration")): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, V)]
Enable periodic checkpointing of RDDs of this DStream.
Enable periodic checkpointing of RDDs of this DStream.

interval

Time interval after which generated RDD will be checkpointed

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#classTag:scala.reflect.ClassTag\[\(K,V\)\] "Permalink") val classTag: ClassTag[(K, V)]

Definition Classes
     [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream") → [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#clone\(\):Object "Permalink") def clone(): AnyRef

Attributes
    protected[lang]

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#cogroup\[W\]\(other:org.apache.spark.streaming.api.java.JavaPairDStream\[K,W\],partitioner:org.apache.spark.Partitioner\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,\(Iterable\[V\],Iterable\[W\]\)\] "Permalink") def cogroup[W](other: [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, W], partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner")): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, ([Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html#java.lang.Iterable "java.lang.Iterable")[V], [Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html#java.lang.Iterable "java.lang.Iterable")[W])]
Return a new DStream by applying 'cogroup' between RDDs of `this` DStream and `other` DStream.
Return a new DStream by applying 'cogroup' between RDDs of `this` DStream and `other` DStream. Hash partitioning is used to generate the RDDs with `numPartitions` partitions.
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#cogroup\[W\]\(other:org.apache.spark.streaming.api.java.JavaPairDStream\[K,W\],numPartitions:Int\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,\(Iterable\[V\],Iterable\[W\]\)\] "Permalink") def cogroup[W](other: [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, W], numPartitions: Int): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, ([Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html#java.lang.Iterable "java.lang.Iterable")[V], [Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html#java.lang.Iterable "java.lang.Iterable")[W])]
Return a new DStream by applying 'cogroup' between RDDs of `this` DStream and `other` DStream.
Return a new DStream by applying 'cogroup' between RDDs of `this` DStream and `other` DStream. Hash partitioning is used to generate the RDDs with `numPartitions` partitions.
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#cogroup\[W\]\(other:org.apache.spark.streaming.api.java.JavaPairDStream\[K,W\]\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,\(Iterable\[V\],Iterable\[W\]\)\] "Permalink") def cogroup[W](other: [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, W]): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, ([Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html#java.lang.Iterable "java.lang.Iterable")[V], [Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html#java.lang.Iterable "java.lang.Iterable")[W])]
Return a new DStream by applying 'cogroup' between RDDs of `this` DStream and `other` DStream.
Return a new DStream by applying 'cogroup' between RDDs of `this` DStream and `other` DStream. Hash partitioning is used to generate the RDDs with Spark's default number of partitions.
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#combineByKey\[C\]\(createCombiner:org.apache.spark.api.java.function.Function\[V,C\],mergeValue:org.apache.spark.api.java.function.Function2\[C,V,C\],mergeCombiners:org.apache.spark.api.java.function.Function2\[C,C,C\],partitioner:org.apache.spark.Partitioner,mapSideCombine:Boolean\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,C\] "Permalink") def combineByKey[C](createCombiner: [Function](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function.html "org.apache.spark.api.java.function.Function")[V, C], mergeValue: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[C, V, C], mergeCombiners: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[C, C, C], partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner"), mapSideCombine: Boolean): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, C]
Combine elements of each key in DStream's RDDs using custom function.
Combine elements of each key in DStream's RDDs using custom function. This is similar to the combineByKey for RDDs. Please refer to combineByKey in org.apache.spark.rdd.PairRDDFunctions for more information.
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#combineByKey\[C\]\(createCombiner:org.apache.spark.api.java.function.Function\[V,C\],mergeValue:org.apache.spark.api.java.function.Function2\[C,V,C\],mergeCombiners:org.apache.spark.api.java.function.Function2\[C,C,C\],partitioner:org.apache.spark.Partitioner\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,C\] "Permalink") def combineByKey[C](createCombiner: [Function](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function.html "org.apache.spark.api.java.function.Function")[V, C], mergeValue: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[C, V, C], mergeCombiners: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[C, C, C], partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner")): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, C]
Combine elements of each key in DStream's RDDs using custom function.
Combine elements of each key in DStream's RDDs using custom function. This is similar to the combineByKey for RDDs. Please refer to combineByKey in org.apache.spark.rdd.PairRDDFunctions for more information.
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#compute\(validTime:org.apache.spark.streaming.Time\):org.apache.spark.api.java.JavaPairRDD\[K,V\] "Permalink") def compute(validTime: [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time")): [JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K, V]
Method that generates an RDD for the given Duration
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#context\(\):org.apache.spark.streaming.StreamingContext "Permalink") def context(): [StreamingContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html "org.apache.spark.streaming.StreamingContext")
Return the [org.apache.spark.streaming.StreamingContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html "org.apache.spark.streaming.StreamingContext") associated with this DStream
Return the [org.apache.spark.streaming.StreamingContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html "org.apache.spark.streaming.StreamingContext") associated with this DStream

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#count\(\):org.apache.spark.streaming.api.java.JavaDStream\[Long\] "Permalink") def count(): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[[Long](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html#java.lang.Long "java.lang.Long")]
Return a new DStream in which each RDD has a single element generated by counting each RDD of this DStream.
Return a new DStream in which each RDD has a single element generated by counting each RDD of this DStream.

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#countByValue\(numPartitions:Int\):org.apache.spark.streaming.api.java.JavaPairDStream\[T,Long\] "Permalink") def countByValue(numPartitions: Int): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[(K, V), [Long](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html#java.lang.Long "java.lang.Long")]
Return a new DStream in which each RDD contains the counts of each distinct value in each RDD of this DStream.
Return a new DStream in which each RDD contains the counts of each distinct value in each RDD of this DStream. Hash partitioning is used to generate the RDDs with `numPartitions` partitions.

numPartitions

number of partitions of each RDD in the new DStream.

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#countByValue\(\):org.apache.spark.streaming.api.java.JavaPairDStream\[T,Long\] "Permalink") def countByValue(): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[(K, V), [Long](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html#java.lang.Long "java.lang.Long")]
Return a new DStream in which each RDD contains the counts of each distinct value in each RDD of this DStream.
Return a new DStream in which each RDD contains the counts of each distinct value in each RDD of this DStream. Hash partitioning is used to generate the RDDs with Spark's default number of partitions.

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#countByValueAndWindow\(windowDuration:org.apache.spark.streaming.Duration,slideDuration:org.apache.spark.streaming.Duration,numPartitions:Int\):org.apache.spark.streaming.api.java.JavaPairDStream\[T,Long\] "Permalink") def countByValueAndWindow(windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), numPartitions: Int): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[(K, V), [Long](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html#java.lang.Long "java.lang.Long")]
Return a new DStream in which each RDD contains the count of distinct elements in RDDs in a sliding window over this DStream.
Return a new DStream in which each RDD contains the count of distinct elements in RDDs in a sliding window over this DStream. Hash partitioning is used to generate the RDDs with `numPartitions` partitions.

windowDuration

width of the window; must be a multiple of this DStream's batching interval

slideDuration

sliding interval of the window (i.e., the interval after which the new DStream will generate RDDs); must be a multiple of this DStream's batching interval

numPartitions

number of partitions of each RDD in the new DStream.

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#countByValueAndWindow\(windowDuration:org.apache.spark.streaming.Duration,slideDuration:org.apache.spark.streaming.Duration\):org.apache.spark.streaming.api.java.JavaPairDStream\[T,Long\] "Permalink") def countByValueAndWindow(windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration")): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[(K, V), [Long](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html#java.lang.Long "java.lang.Long")]
Return a new DStream in which each RDD contains the count of distinct elements in RDDs in a sliding window over this DStream.
Return a new DStream in which each RDD contains the count of distinct elements in RDDs in a sliding window over this DStream. Hash partitioning is used to generate the RDDs with Spark's default number of partitions.

windowDuration

width of the window; must be a multiple of this DStream's batching interval

slideDuration

sliding interval of the window (i.e., the interval after which the new DStream will generate RDDs); must be a multiple of this DStream's batching interval

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#countByWindow\(windowDuration:org.apache.spark.streaming.Duration,slideDuration:org.apache.spark.streaming.Duration\):org.apache.spark.streaming.api.java.JavaDStream\[Long\] "Permalink") def countByWindow(windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration")): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[[Long](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html#java.lang.Long "java.lang.Long")]
Return a new DStream in which each RDD has a single element generated by counting the number of elements in a window over this DStream.
Return a new DStream in which each RDD has a single element generated by counting the number of elements in a window over this DStream. windowDuration and slideDuration are as defined in the window() operation. This is equivalent to window(windowDuration, slideDuration).count()

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#dstream:org.apache.spark.streaming.dstream.DStream\[\(K,V\)\] "Permalink") val dstream: [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, V)]

Definition Classes
     [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream") → [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  23. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  24. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#equals\(x$1:Object\):Boolean "Permalink") def equals(arg0: AnyRef): Boolean

Definition Classes
    AnyRef → Any
  25. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#filter\(f:org.apache.spark.api.java.function.Function\[\(K,V\),Boolean\]\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,V\] "Permalink") def filter(f: [Function](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function.html "org.apache.spark.api.java.function.Function")[(K, V), [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html#java.lang.Boolean "java.lang.Boolean")]): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, V]
Return a new DStream containing only the elements that satisfy a predicate.
  26. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#flatMap\[U\]\(f:org.apache.spark.api.java.function.FlatMapFunction\[T,U\]\):org.apache.spark.streaming.api.java.JavaDStream\[U\] "Permalink") def flatMap[U](f: [FlatMapFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction.html "org.apache.spark.api.java.function.FlatMapFunction")[(K, V), U]): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[U]
Return a new DStream by applying a function to all elements of this DStream, and then flattening the results
Return a new DStream by applying a function to all elements of this DStream, and then flattening the results

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  27. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#flatMapToPair\[K2,V2\]\(f:org.apache.spark.api.java.function.PairFlatMapFunction\[T,K2,V2\]\):org.apache.spark.streaming.api.java.JavaPairDStream\[K2,V2\] "Permalink") def flatMapToPair[K2, V2](f: [PairFlatMapFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/PairFlatMapFunction.html "org.apache.spark.api.java.function.PairFlatMapFunction")[(K, V), K2, V2]): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K2, V2]
Return a new DStream by applying a function to all elements of this DStream, and then flattening the results
Return a new DStream by applying a function to all elements of this DStream, and then flattening the results

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  28. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#flatMapValues\[U\]\(f:org.apache.spark.api.java.function.FlatMapFunction\[V,U\]\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,U\] "Permalink") def flatMapValues[U](f: [FlatMapFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction.html "org.apache.spark.api.java.function.FlatMapFunction")[V, U]): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, U]
Return a new DStream by applying a flatmap function to the value of each key-value pairs in 'this' DStream without changing the key.
  29. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#foreachRDD\(foreachFunc:org.apache.spark.api.java.function.VoidFunction2\[R,org.apache.spark.streaming.Time\]\):Unit "Permalink") def foreachRDD(foreachFunc: [VoidFunction2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/VoidFunction2.html "org.apache.spark.api.java.function.VoidFunction2")[[JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K, V], [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time")]): Unit
Apply a function to each RDD in this DStream.
Apply a function to each RDD in this DStream. This is an output operator, so 'this' DStream will be registered as an output stream and therefore materialized.

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  30. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#foreachRDD\(foreachFunc:org.apache.spark.api.java.function.VoidFunction\[R\]\):Unit "Permalink") def foreachRDD(foreachFunc: [VoidFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/VoidFunction.html "org.apache.spark.api.java.function.VoidFunction")[[JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K, V]]): Unit
Apply a function to each RDD in this DStream.
Apply a function to each RDD in this DStream. This is an output operator, so 'this' DStream will be registered as an output stream and therefore materialized.

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  31. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#fullOuterJoin\[W\]\(other:org.apache.spark.streaming.api.java.JavaPairDStream\[K,W\],partitioner:org.apache.spark.Partitioner\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,\(org.apache.spark.api.java.Optional\[V\],org.apache.spark.api.java.Optional\[W\]\)\] "Permalink") def fullOuterJoin[W](other: [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, W], partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner")): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, ([Optional](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/Optional.html "org.apache.spark.api.java.Optional")[V], [Optional](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/Optional.html "org.apache.spark.api.java.Optional")[W])]
Return a new DStream by applying 'full outer join' between RDDs of `this` DStream and `other` DStream.
Return a new DStream by applying 'full outer join' between RDDs of `this` DStream and `other` DStream. The supplied org.apache.spark.Partitioner is used to control the partitioning of each RDD.
  32. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#fullOuterJoin\[W\]\(other:org.apache.spark.streaming.api.java.JavaPairDStream\[K,W\],numPartitions:Int\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,\(org.apache.spark.api.java.Optional\[V\],org.apache.spark.api.java.Optional\[W\]\)\] "Permalink") def fullOuterJoin[W](other: [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, W], numPartitions: Int): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, ([Optional](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/Optional.html "org.apache.spark.api.java.Optional")[V], [Optional](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/Optional.html "org.apache.spark.api.java.Optional")[W])]
Return a new DStream by applying 'full outer join' between RDDs of `this` DStream and `other` DStream.
Return a new DStream by applying 'full outer join' between RDDs of `this` DStream and `other` DStream. Hash partitioning is used to generate the RDDs with `numPartitions` partitions.
  33. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#fullOuterJoin\[W\]\(other:org.apache.spark.streaming.api.java.JavaPairDStream\[K,W\]\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,\(org.apache.spark.api.java.Optional\[V\],org.apache.spark.api.java.Optional\[W\]\)\] "Permalink") def fullOuterJoin[W](other: [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, W]): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, ([Optional](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/Optional.html "org.apache.spark.api.java.Optional")[V], [Optional](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/Optional.html "org.apache.spark.api.java.Optional")[W])]
Return a new DStream by applying 'full outer join' between RDDs of `this` DStream and `other` DStream.
Return a new DStream by applying 'full outer join' between RDDs of `this` DStream and `other` DStream. Hash partitioning is used to generate the RDDs with Spark's default number of partitions.
  34. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef]

Definition Classes
    AnyRef → Any

Annotations
     @IntrinsicCandidate() @native()
  35. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#glom\(\):org.apache.spark.streaming.api.java.JavaDStream\[java.util.List\[T\]\] "Permalink") def glom(): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#java.util.List "java.util.List")[(K, V)]]
Return a new DStream in which each RDD is generated by applying glom() to each RDD of this DStream.
Return a new DStream in which each RDD is generated by applying glom() to each RDD of this DStream. Applying glom() to an RDD coalesces all elements within each partition into an array.

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  36. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#groupByKey\(partitioner:org.apache.spark.Partitioner\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,Iterable\[V\]\] "Permalink") def groupByKey(partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner")): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, [Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html#java.lang.Iterable "java.lang.Iterable")[V]]
Return a new DStream by applying `groupByKey` on each RDD of `this` DStream.
Return a new DStream by applying `groupByKey` on each RDD of `this` DStream. Therefore, the values for each key in `this` DStream's RDDs are grouped into a single sequence to generate the RDDs of the new DStream. org.apache.spark.Partitioner is used to control the partitioning of each RDD.
  37. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#groupByKey\(numPartitions:Int\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,Iterable\[V\]\] "Permalink") def groupByKey(numPartitions: Int): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, [Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html#java.lang.Iterable "java.lang.Iterable")[V]]
Return a new DStream by applying `groupByKey` to each RDD.
Return a new DStream by applying `groupByKey` to each RDD. Hash partitioning is used to generate the RDDs with `numPartitions` partitions.
  38. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#groupByKey\(\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,Iterable\[V\]\] "Permalink") def groupByKey(): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, [Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html#java.lang.Iterable "java.lang.Iterable")[V]]
Return a new DStream by applying `groupByKey` to each RDD.
Return a new DStream by applying `groupByKey` to each RDD. Hash partitioning is used to generate the RDDs with Spark's default number of partitions.
  39. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#groupByKeyAndWindow\(windowDuration:org.apache.spark.streaming.Duration,slideDuration:org.apache.spark.streaming.Duration,partitioner:org.apache.spark.Partitioner\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,Iterable\[V\]\] "Permalink") def groupByKeyAndWindow(windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner")): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, [Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html#java.lang.Iterable "java.lang.Iterable")[V]]
Return a new DStream by applying `groupByKey` over a sliding window on `this` DStream.
Return a new DStream by applying `groupByKey` over a sliding window on `this` DStream. Similar to `DStream.groupByKey()`, but applies it over a sliding window.

windowDuration

width of the window; must be a multiple of this DStream's batching interval

slideDuration

sliding interval of the window (i.e., the interval after which the new DStream will generate RDDs); must be a multiple of this DStream's batching interval

partitioner

Partitioner for controlling the partitioning of each RDD in the new DStream.
  40. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#groupByKeyAndWindow\(windowDuration:org.apache.spark.streaming.Duration,slideDuration:org.apache.spark.streaming.Duration,numPartitions:Int\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,Iterable\[V\]\] "Permalink") def groupByKeyAndWindow(windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), numPartitions: Int): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, [Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html#java.lang.Iterable "java.lang.Iterable")[V]]
Return a new DStream by applying `groupByKey` over a sliding window on `this` DStream.
Return a new DStream by applying `groupByKey` over a sliding window on `this` DStream. Similar to `DStream.groupByKey()`, but applies it over a sliding window. Hash partitioning is used to generate the RDDs with `numPartitions` partitions.

windowDuration

width of the window; must be a multiple of this DStream's batching interval

slideDuration

sliding interval of the window (i.e., the interval after which the new DStream will generate RDDs); must be a multiple of this DStream's batching interval

numPartitions

Number of partitions of each RDD in the new DStream.
  41. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#groupByKeyAndWindow\(windowDuration:org.apache.spark.streaming.Duration,slideDuration:org.apache.spark.streaming.Duration\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,Iterable\[V\]\] "Permalink") def groupByKeyAndWindow(windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration")): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, [Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html#java.lang.Iterable "java.lang.Iterable")[V]]
Return a new DStream by applying `groupByKey` over a sliding window.
Return a new DStream by applying `groupByKey` over a sliding window. Similar to `DStream.groupByKey()`, but applies it over a sliding window. Hash partitioning is used to generate the RDDs with Spark's default number of partitions.

windowDuration

width of the window; must be a multiple of this DStream's batching interval

slideDuration

sliding interval of the window (i.e., the interval after which the new DStream will generate RDDs); must be a multiple of this DStream's batching interval
  42. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#groupByKeyAndWindow\(windowDuration:org.apache.spark.streaming.Duration\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,Iterable\[V\]\] "Permalink") def groupByKeyAndWindow(windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration")): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, [Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html#java.lang.Iterable "java.lang.Iterable")[V]]
Return a new DStream by applying `groupByKey` over a sliding window.
Return a new DStream by applying `groupByKey` over a sliding window. This is similar to `DStream.groupByKey()` but applies it over a sliding window. The new DStream generates RDDs with the same interval as this DStream. Hash partitioning is used to generate the RDDs with Spark's default number of partitions.

windowDuration

width of the window; must be a multiple of this DStream's batching interval
  43. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#hashCode\(\):Int "Permalink") def hashCode(): Int

Definition Classes
    AnyRef → Any

Annotations
     @IntrinsicCandidate() @native()
  44. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean

Definition Classes
    Any
  45. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#join\[W\]\(other:org.apache.spark.streaming.api.java.JavaPairDStream\[K,W\],partitioner:org.apache.spark.Partitioner\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,\(V,W\)\] "Permalink") def join[W](other: [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, W], partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner")): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, (V, W)]
Return a new DStream by applying 'join' between RDDs of `this` DStream and `other` DStream.
Return a new DStream by applying 'join' between RDDs of `this` DStream and `other` DStream. The supplied org.apache.spark.Partitioner is used to control the partitioning of each RDD.
  46. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#join\[W\]\(other:org.apache.spark.streaming.api.java.JavaPairDStream\[K,W\],numPartitions:Int\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,\(V,W\)\] "Permalink") def join[W](other: [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, W], numPartitions: Int): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, (V, W)]
Return a new DStream by applying 'join' between RDDs of `this` DStream and `other` DStream.
Return a new DStream by applying 'join' between RDDs of `this` DStream and `other` DStream. Hash partitioning is used to generate the RDDs with `numPartitions` partitions.
  47. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#join\[W\]\(other:org.apache.spark.streaming.api.java.JavaPairDStream\[K,W\]\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,\(V,W\)\] "Permalink") def join[W](other: [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, W]): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, (V, W)]
Return a new DStream by applying 'join' between RDDs of `this` DStream and `other` DStream.
Return a new DStream by applying 'join' between RDDs of `this` DStream and `other` DStream. Hash partitioning is used to generate the RDDs with Spark's default number of partitions.
  48. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#kManifest:scala.reflect.ClassTag\[K\] "Permalink") implicit  val kManifest: ClassTag[K]
  49. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#leftOuterJoin\[W\]\(other:org.apache.spark.streaming.api.java.JavaPairDStream\[K,W\],partitioner:org.apache.spark.Partitioner\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,\(V,org.apache.spark.api.java.Optional\[W\]\)\] "Permalink") def leftOuterJoin[W](other: [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, W], partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner")): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, (V, [Optional](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/Optional.html "org.apache.spark.api.java.Optional")[W])]
Return a new DStream by applying 'left outer join' between RDDs of `this` DStream and `other` DStream.
Return a new DStream by applying 'left outer join' between RDDs of `this` DStream and `other` DStream. The supplied org.apache.spark.Partitioner is used to control the partitioning of each RDD.
  50. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#leftOuterJoin\[W\]\(other:org.apache.spark.streaming.api.java.JavaPairDStream\[K,W\],numPartitions:Int\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,\(V,org.apache.spark.api.java.Optional\[W\]\)\] "Permalink") def leftOuterJoin[W](other: [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, W], numPartitions: Int): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, (V, [Optional](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/Optional.html "org.apache.spark.api.java.Optional")[W])]
Return a new DStream by applying 'left outer join' between RDDs of `this` DStream and `other` DStream.
Return a new DStream by applying 'left outer join' between RDDs of `this` DStream and `other` DStream. Hash partitioning is used to generate the RDDs with `numPartitions` partitions.
  51. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#leftOuterJoin\[W\]\(other:org.apache.spark.streaming.api.java.JavaPairDStream\[K,W\]\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,\(V,org.apache.spark.api.java.Optional\[W\]\)\] "Permalink") def leftOuterJoin[W](other: [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, W]): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, (V, [Optional](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/Optional.html "org.apache.spark.api.java.Optional")[W])]
Return a new DStream by applying 'left outer join' between RDDs of `this` DStream and `other` DStream.
Return a new DStream by applying 'left outer join' between RDDs of `this` DStream and `other` DStream. Hash partitioning is used to generate the RDDs with Spark's default number of partitions.
  52. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#map\[U\]\(f:org.apache.spark.api.java.function.Function\[T,U\]\):org.apache.spark.streaming.api.java.JavaDStream\[U\] "Permalink") def map[U](f: [Function](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function.html "org.apache.spark.api.java.function.Function")[(K, V), U]): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[U]
Return a new DStream by applying a function to all elements of this DStream.
Return a new DStream by applying a function to all elements of this DStream.

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  53. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#mapPartitions\[U\]\(f:org.apache.spark.api.java.function.FlatMapFunction\[java.util.Iterator\[T\],U\]\):org.apache.spark.streaming.api.java.JavaDStream\[U\] "Permalink") def mapPartitions[U](f: [FlatMapFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction.html "org.apache.spark.api.java.function.FlatMapFunction")[[Iterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html#java.util.Iterator "java.util.Iterator")[(K, V)], U]): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[U]
Return a new DStream in which each RDD is generated by applying mapPartitions() to each RDDs of this DStream.
Return a new DStream in which each RDD is generated by applying mapPartitions() to each RDDs of this DStream. Applying mapPartitions() to an RDD applies a function to each partition of the RDD.

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  54. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#mapPartitionsToPair\[K2,V2\]\(f:org.apache.spark.api.java.function.PairFlatMapFunction\[java.util.Iterator\[T\],K2,V2\]\):org.apache.spark.streaming.api.java.JavaPairDStream\[K2,V2\] "Permalink") def mapPartitionsToPair[K2, V2](f: [PairFlatMapFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/PairFlatMapFunction.html "org.apache.spark.api.java.function.PairFlatMapFunction")[[Iterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html#java.util.Iterator "java.util.Iterator")[(K, V)], K2, V2]): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K2, V2]
Return a new DStream in which each RDD is generated by applying mapPartitions() to each RDDs of this DStream.
Return a new DStream in which each RDD is generated by applying mapPartitions() to each RDDs of this DStream. Applying mapPartitions() to an RDD applies a function to each partition of the RDD.

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  55. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#mapToPair\[K2,V2\]\(f:org.apache.spark.api.java.function.PairFunction\[T,K2,V2\]\):org.apache.spark.streaming.api.java.JavaPairDStream\[K2,V2\] "Permalink") def mapToPair[K2, V2](f: [PairFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/PairFunction.html "org.apache.spark.api.java.function.PairFunction")[(K, V), K2, V2]): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K2, V2]
Return a new DStream by applying a function to all elements of this DStream.
Return a new DStream by applying a function to all elements of this DStream.

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  56. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#mapValues\[U\]\(f:org.apache.spark.api.java.function.Function\[V,U\]\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,U\] "Permalink") def mapValues[U](f: [Function](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function.html "org.apache.spark.api.java.function.Function")[V, U]): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, U]
Return a new DStream by applying a map function to the value of each key-value pairs in 'this' DStream without changing the key.
  57. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#mapWithState\[StateType,MappedType\]\(spec:org.apache.spark.streaming.StateSpec\[K,V,StateType,MappedType\]\):org.apache.spark.streaming.api.java.JavaMapWithStateDStream\[K,V,StateType,MappedType\] "Permalink") def mapWithState[StateType, MappedType](spec: [StateSpec](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StateSpec.html "org.apache.spark.streaming.StateSpec")[K, V, StateType, MappedType]): [JavaMapWithStateDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaMapWithStateDStream.html "org.apache.spark.streaming.api.java.JavaMapWithStateDStream")[K, V, StateType, MappedType]
Return a [JavaMapWithStateDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaMapWithStateDStream.html "org.apache.spark.streaming.api.java.JavaMapWithStateDStream") by applying a function to every key-value element of `this` stream, while maintaining some state data for each unique key.
Return a [JavaMapWithStateDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaMapWithStateDStream.html "org.apache.spark.streaming.api.java.JavaMapWithStateDStream") by applying a function to every key-value element of `this` stream, while maintaining some state data for each unique key. The mapping function and other specification (e.g. partitioners, timeouts, initial state data, etc.) of this transformation can be specified using `StateSpec` class. The state data is accessible in as a parameter of type `State` in the mapping function.
Example of using `mapWithState`:

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

StateType

Class type of the state data

MappedType

Class type of the mapped data

spec

Specification of this transformation
  58. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  59. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#notify\(\):Unit "Permalink") final  def notify(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  60. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  61. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#persist\(storageLevel:org.apache.spark.storage.StorageLevel\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,V\] "Permalink") def persist(storageLevel: [StorageLevel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StorageLevel.html "org.apache.spark.storage.StorageLevel")): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, V]
Persist the RDDs of this DStream with the given storage level
  62. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#persist\(\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,V\] "Permalink") def persist(): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, V]
Persist RDDs of this DStream with the default storage level (MEMORY_ONLY_SER)
  63. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#print\(num:Int\):Unit "Permalink") def print(num: Int): Unit
Print the first num elements of each RDD generated in this DStream.
Print the first num elements of each RDD generated in this DStream. This is an output operator, so this DStream will be registered as an output stream and there materialized.

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  64. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#print\(\):Unit "Permalink") def print(): Unit
Print the first ten elements of each RDD generated in this DStream.
Print the first ten elements of each RDD generated in this DStream. This is an output operator, so this DStream will be registered as an output stream and there materialized.

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  65. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#reduce\(f:org.apache.spark.api.java.function.Function2\[T,T,T\]\):org.apache.spark.streaming.api.java.JavaDStream\[T\] "Permalink") def reduce(f: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[(K, V), (K, V), (K, V)]): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[(K, V)]
Return a new DStream in which each RDD has a single element generated by reducing each RDD of this DStream.
Return a new DStream in which each RDD has a single element generated by reducing each RDD of this DStream.

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  66. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#reduceByKey\(func:org.apache.spark.api.java.function.Function2\[V,V,V\],partitioner:org.apache.spark.Partitioner\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,V\] "Permalink") def reduceByKey(func: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[V, V, V], partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner")): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, V]
Return a new DStream by applying `reduceByKey` to each RDD.
Return a new DStream by applying `reduceByKey` to each RDD. The values for each key are merged using the supplied reduce function. org.apache.spark.Partitioner is used to control the partitioning of each RDD.
  67. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#reduceByKey\(func:org.apache.spark.api.java.function.Function2\[V,V,V\],numPartitions:Int\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,V\] "Permalink") def reduceByKey(func: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[V, V, V], numPartitions: Int): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, V]
Return a new DStream by applying `reduceByKey` to each RDD.
Return a new DStream by applying `reduceByKey` to each RDD. The values for each key are merged using the supplied reduce function. Hash partitioning is used to generate the RDDs with `numPartitions` partitions.
  68. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#reduceByKey\(func:org.apache.spark.api.java.function.Function2\[V,V,V\]\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,V\] "Permalink") def reduceByKey(func: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[V, V, V]): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, V]
Return a new DStream by applying `reduceByKey` to each RDD.
Return a new DStream by applying `reduceByKey` to each RDD. The values for each key are merged using the associative and commutative reduce function. Hash partitioning is used to generate the RDDs with Spark's default number of partitions.
  69. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#reduceByKeyAndWindow\(reduceFunc:org.apache.spark.api.java.function.Function2\[V,V,V\],invReduceFunc:org.apache.spark.api.java.function.Function2\[V,V,V\],windowDuration:org.apache.spark.streaming.Duration,slideDuration:org.apache.spark.streaming.Duration,partitioner:org.apache.spark.Partitioner,filterFunc:org.apache.spark.api.java.function.Function\[\(K,V\),Boolean\]\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,V\] "Permalink") def reduceByKeyAndWindow(reduceFunc: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[V, V, V], invReduceFunc: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[V, V, V], windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner"), filterFunc: [Function](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function.html "org.apache.spark.api.java.function.Function")[(K, V), [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html#java.lang.Boolean "java.lang.Boolean")]): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, V]
Return a new DStream by applying incremental `reduceByKey` over a sliding window.
Return a new DStream by applying incremental `reduceByKey` over a sliding window. The reduced value of over a new window is calculated using the old window's reduce value :
    1. reduce the new values that entered the window (e.g., adding new counts) 2. "inverse reduce" the old values that left the window (e.g., subtracting old counts) This is more efficient that reduceByKeyAndWindow without "inverse reduce" function. However, it is applicable to only "invertible reduce functions".

reduceFunc

associative and commutative reduce function

invReduceFunc

inverse function

windowDuration

width of the window; must be a multiple of this DStream's batching interval

slideDuration

sliding interval of the window (i.e., the interval after which the new DStream will generate RDDs); must be a multiple of this DStream's batching interval

partitioner

Partitioner for controlling the partitioning of each RDD in the new DStream.

filterFunc

function to filter expired key-value pairs; only pairs that satisfy the function are retained set this to null if you do not want to filter
  70. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#reduceByKeyAndWindow\(reduceFunc:org.apache.spark.api.java.function.Function2\[V,V,V\],invReduceFunc:org.apache.spark.api.java.function.Function2\[V,V,V\],windowDuration:org.apache.spark.streaming.Duration,slideDuration:org.apache.spark.streaming.Duration,numPartitions:Int,filterFunc:org.apache.spark.api.java.function.Function\[\(K,V\),Boolean\]\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,V\] "Permalink") def reduceByKeyAndWindow(reduceFunc: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[V, V, V], invReduceFunc: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[V, V, V], windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), numPartitions: Int, filterFunc: [Function](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function.html "org.apache.spark.api.java.function.Function")[(K, V), [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html#java.lang.Boolean "java.lang.Boolean")]): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, V]
Return a new DStream by applying incremental `reduceByKey` over a sliding window.
Return a new DStream by applying incremental `reduceByKey` over a sliding window. The reduced value of over a new window is calculated using the old window's reduce value :
    1. reduce the new values that entered the window (e.g., adding new counts) 2. "inverse reduce" the old values that left the window (e.g., subtracting old counts) This is more efficient that reduceByKeyAndWindow without "inverse reduce" function. However, it is applicable to only "invertible reduce functions". Hash partitioning is used to generate the RDDs with `numPartitions` partitions.

reduceFunc

associative and commutative reduce function

invReduceFunc

inverse function

windowDuration

width of the window; must be a multiple of this DStream's batching interval

slideDuration

sliding interval of the window (i.e., the interval after which the new DStream will generate RDDs); must be a multiple of this DStream's batching interval

numPartitions

number of partitions of each RDD in the new DStream.

filterFunc

function to filter expired key-value pairs; only pairs that satisfy the function are retained set this to null if you do not want to filter
  71. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#reduceByKeyAndWindow\(reduceFunc:org.apache.spark.api.java.function.Function2\[V,V,V\],invReduceFunc:org.apache.spark.api.java.function.Function2\[V,V,V\],windowDuration:org.apache.spark.streaming.Duration,slideDuration:org.apache.spark.streaming.Duration\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,V\] "Permalink") def reduceByKeyAndWindow(reduceFunc: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[V, V, V], invReduceFunc: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[V, V, V], windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration")): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, V]
Return a new DStream by reducing over a using incremental computation.
Return a new DStream by reducing over a using incremental computation. The reduced value of over a new window is calculated using the old window's reduce value :
    1. reduce the new values that entered the window (e.g., adding new counts) 2. "inverse reduce" the old values that left the window (e.g., subtracting old counts) This is more efficient that reduceByKeyAndWindow without "inverse reduce" function. However, it is applicable to only "invertible reduce functions". Hash partitioning is used to generate the RDDs with Spark's default number of partitions.

reduceFunc

associative and commutative reduce function

invReduceFunc

inverse function; such that for all y, invertible x: `invReduceFunc(reduceFunc(x, y), x) = y`

windowDuration

width of the window; must be a multiple of this DStream's batching interval

slideDuration

sliding interval of the window (i.e., the interval after which the new DStream will generate RDDs); must be a multiple of this DStream's batching interval
  72. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#reduceByKeyAndWindow\(reduceFunc:org.apache.spark.api.java.function.Function2\[V,V,V\],windowDuration:org.apache.spark.streaming.Duration,slideDuration:org.apache.spark.streaming.Duration,partitioner:org.apache.spark.Partitioner\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,V\] "Permalink") def reduceByKeyAndWindow(reduceFunc: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[V, V, V], windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner")): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, V]
Return a new DStream by applying `reduceByKey` over a sliding window.
Return a new DStream by applying `reduceByKey` over a sliding window. Similar to `DStream.reduceByKey()`, but applies it over a sliding window.

reduceFunc

associative rand commutative educe function

windowDuration

width of the window; must be a multiple of this DStream's batching interval

slideDuration

sliding interval of the window (i.e., the interval after which the new DStream will generate RDDs); must be a multiple of this DStream's batching interval

partitioner

Partitioner for controlling the partitioning of each RDD in the new DStream.
  73. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#reduceByKeyAndWindow\(reduceFunc:org.apache.spark.api.java.function.Function2\[V,V,V\],windowDuration:org.apache.spark.streaming.Duration,slideDuration:org.apache.spark.streaming.Duration,numPartitions:Int\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,V\] "Permalink") def reduceByKeyAndWindow(reduceFunc: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[V, V, V], windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), numPartitions: Int): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, V]
Return a new DStream by applying `reduceByKey` over a sliding window.
Return a new DStream by applying `reduceByKey` over a sliding window. This is similar to `DStream.reduceByKey()` but applies it over a sliding window. Hash partitioning is used to generate the RDDs with `numPartitions` partitions.

reduceFunc

associative and commutative reduce function

windowDuration

width of the window; must be a multiple of this DStream's batching interval

slideDuration

sliding interval of the window (i.e., the interval after which the new DStream will generate RDDs); must be a multiple of this DStream's batching interval

numPartitions

Number of partitions of each RDD in the new DStream.
  74. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#reduceByKeyAndWindow\(reduceFunc:org.apache.spark.api.java.function.Function2\[V,V,V\],windowDuration:org.apache.spark.streaming.Duration,slideDuration:org.apache.spark.streaming.Duration\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,V\] "Permalink") def reduceByKeyAndWindow(reduceFunc: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[V, V, V], windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration")): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, V]
Return a new DStream by applying `reduceByKey` over a sliding window.
Return a new DStream by applying `reduceByKey` over a sliding window. This is similar to `DStream.reduceByKey()` but applies it over a sliding window. Hash partitioning is used to generate the RDDs with Spark's default number of partitions.

reduceFunc

associative and commutative reduce function

windowDuration

width of the window; must be a multiple of this DStream's batching interval

slideDuration

sliding interval of the window (i.e., the interval after which the new DStream will generate RDDs); must be a multiple of this DStream's batching interval
  75. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#reduceByKeyAndWindow\(reduceFunc:org.apache.spark.api.java.function.Function2\[V,V,V\],windowDuration:org.apache.spark.streaming.Duration\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,V\] "Permalink") def reduceByKeyAndWindow(reduceFunc: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[V, V, V], windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration")): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, V]
Create a new DStream by applying `reduceByKey` over a sliding window on `this` DStream.
Create a new DStream by applying `reduceByKey` over a sliding window on `this` DStream. Similar to `DStream.reduceByKey()`, but applies it over a sliding window. The new DStream generates RDDs with the same interval as this DStream. Hash partitioning is used to generate the RDDs with Spark's default number of partitions.

reduceFunc

associative and commutative reduce function

windowDuration

width of the window; must be a multiple of this DStream's batching interval
  76. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#reduceByWindow\(reduceFunc:org.apache.spark.api.java.function.Function2\[T,T,T\],invReduceFunc:org.apache.spark.api.java.function.Function2\[T,T,T\],windowDuration:org.apache.spark.streaming.Duration,slideDuration:org.apache.spark.streaming.Duration\):org.apache.spark.streaming.api.java.JavaDStream\[T\] "Permalink") def reduceByWindow(reduceFunc: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[(K, V), (K, V), (K, V)], invReduceFunc: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[(K, V), (K, V), (K, V)], windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration")): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[(K, V)]
Return a new DStream in which each RDD has a single element generated by reducing all elements in a sliding window over this DStream.
Return a new DStream in which each RDD has a single element generated by reducing all elements in a sliding window over this DStream. However, the reduction is done incrementally using the old window's reduced value :
    1. reduce the new values that entered the window (e.g., adding new counts) 2. "inverse reduce" the old values that left the window (e.g., subtracting old counts) This is more efficient than reduceByWindow without "inverse reduce" function. However, it is applicable to only "invertible reduce functions".

reduceFunc

associative and commutative reduce function

invReduceFunc

inverse reduce function; such that for all y, invertible x: `invReduceFunc(reduceFunc(x, y), x) = y`

windowDuration

width of the window; must be a multiple of this DStream's batching interval

slideDuration

sliding interval of the window (i.e., the interval after which the new DStream will generate RDDs); must be a multiple of this DStream's batching interval

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  77. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#reduceByWindow\(reduceFunc:org.apache.spark.api.java.function.Function2\[T,T,T\],windowDuration:org.apache.spark.streaming.Duration,slideDuration:org.apache.spark.streaming.Duration\):org.apache.spark.streaming.api.java.JavaDStream\[T\] "Permalink") def reduceByWindow(reduceFunc: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[(K, V), (K, V), (K, V)], windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration")): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[(K, V)]
Return a new DStream in which each RDD has a single element generated by reducing all elements in a sliding window over this DStream.
Return a new DStream in which each RDD has a single element generated by reducing all elements in a sliding window over this DStream.

reduceFunc

associative and commutative reduce function

windowDuration

width of the window; must be a multiple of this DStream's batching interval

slideDuration

sliding interval of the window (i.e., the interval after which the new DStream will generate RDDs); must be a multiple of this DStream's batching interval

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  78. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#repartition\(numPartitions:Int\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,V\] "Permalink") def repartition(numPartitions: Int): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, V]
Return a new DStream with an increased or decreased level of parallelism.
Return a new DStream with an increased or decreased level of parallelism. Each RDD in the returned DStream has exactly numPartitions partitions.
  79. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#rightOuterJoin\[W\]\(other:org.apache.spark.streaming.api.java.JavaPairDStream\[K,W\],partitioner:org.apache.spark.Partitioner\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,\(org.apache.spark.api.java.Optional\[V\],W\)\] "Permalink") def rightOuterJoin[W](other: [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, W], partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner")): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, ([Optional](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/Optional.html "org.apache.spark.api.java.Optional")[V], W)]
Return a new DStream by applying 'right outer join' between RDDs of `this` DStream and `other` DStream.
Return a new DStream by applying 'right outer join' between RDDs of `this` DStream and `other` DStream. The supplied org.apache.spark.Partitioner is used to control the partitioning of each RDD.
  80. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#rightOuterJoin\[W\]\(other:org.apache.spark.streaming.api.java.JavaPairDStream\[K,W\],numPartitions:Int\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,\(org.apache.spark.api.java.Optional\[V\],W\)\] "Permalink") def rightOuterJoin[W](other: [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, W], numPartitions: Int): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, ([Optional](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/Optional.html "org.apache.spark.api.java.Optional")[V], W)]
Return a new DStream by applying 'right outer join' between RDDs of `this` DStream and `other` DStream.
Return a new DStream by applying 'right outer join' between RDDs of `this` DStream and `other` DStream. Hash partitioning is used to generate the RDDs with `numPartitions` partitions.
  81. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#rightOuterJoin\[W\]\(other:org.apache.spark.streaming.api.java.JavaPairDStream\[K,W\]\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,\(org.apache.spark.api.java.Optional\[V\],W\)\] "Permalink") def rightOuterJoin[W](other: [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, W]): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, ([Optional](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/Optional.html "org.apache.spark.api.java.Optional")[V], W)]
Return a new DStream by applying 'right outer join' between RDDs of `this` DStream and `other` DStream.
Return a new DStream by applying 'right outer join' between RDDs of `this` DStream and `other` DStream. Hash partitioning is used to generate the RDDs with Spark's default number of partitions.
  82. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#saveAsHadoopFiles\[F<:org.apache.hadoop.mapred.OutputFormat\[_,_\]\]\(prefix:String,suffix:String,keyClass:Class\[_\],valueClass:Class\[_\],outputFormatClass:Class\[F\],conf:org.apache.hadoop.mapred.JobConf\):Unit "Permalink") def saveAsHadoopFiles[F <: OutputFormat[_, _]](prefix: String, suffix: String, keyClass: Class[_], valueClass: Class[_], outputFormatClass: Class[F], conf: JobConf): Unit
Save each RDD in `this` DStream as a Hadoop file.
Save each RDD in `this` DStream as a Hadoop file. The file name at each batch interval is generated based on `prefix` and `suffix`: "prefix-TIME_IN_MS.suffix".
  83. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#saveAsHadoopFiles\[F<:org.apache.hadoop.mapred.OutputFormat\[_,_\]\]\(prefix:String,suffix:String,keyClass:Class\[_\],valueClass:Class\[_\],outputFormatClass:Class\[F\]\):Unit "Permalink") def saveAsHadoopFiles[F <: OutputFormat[_, _]](prefix: String, suffix: String, keyClass: Class[_], valueClass: Class[_], outputFormatClass: Class[F]): Unit
Save each RDD in `this` DStream as a Hadoop file.
Save each RDD in `this` DStream as a Hadoop file. The file name at each batch interval is generated based on `prefix` and `suffix`: "prefix-TIME_IN_MS.suffix".
  84. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#saveAsHadoopFiles\(prefix:String,suffix:String\):Unit "Permalink") def saveAsHadoopFiles(prefix: String, suffix: String): Unit
Save each RDD in `this` DStream as a Hadoop file.
Save each RDD in `this` DStream as a Hadoop file. The file name at each batch interval is generated based on `prefix` and `suffix`: "prefix-TIME_IN_MS.suffix".
  85. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#saveAsNewAPIHadoopFiles\[F<:org.apache.hadoop.mapreduce.OutputFormat\[_,_\]\]\(prefix:String,suffix:String,keyClass:Class\[_\],valueClass:Class\[_\],outputFormatClass:Class\[F\],conf:org.apache.hadoop.conf.Configuration\):Unit "Permalink") def saveAsNewAPIHadoopFiles[F <: OutputFormat[_, _]](prefix: String, suffix: String, keyClass: Class[_], valueClass: Class[_], outputFormatClass: Class[F], conf: Configuration = [dstream.context.sparkContext.hadoopConfiguration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#dstream:org.apache.spark.streaming.dstream.DStream\[\(K,V\)\])): Unit
Save each RDD in `this` DStream as a Hadoop file.
Save each RDD in `this` DStream as a Hadoop file. The file name at each batch interval is generated based on `prefix` and `suffix`: "prefix-TIME_IN_MS.suffix".
  86. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#saveAsNewAPIHadoopFiles\[F<:org.apache.hadoop.mapreduce.OutputFormat\[_,_\]\]\(prefix:String,suffix:String,keyClass:Class\[_\],valueClass:Class\[_\],outputFormatClass:Class\[F\]\):Unit "Permalink") def saveAsNewAPIHadoopFiles[F <: OutputFormat[_, _]](prefix: String, suffix: String, keyClass: Class[_], valueClass: Class[_], outputFormatClass: Class[F]): Unit
Save each RDD in `this` DStream as a Hadoop file.
Save each RDD in `this` DStream as a Hadoop file. The file name at each batch interval is generated based on `prefix` and `suffix`: "prefix-TIME_IN_MS.suffix".
  87. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#saveAsNewAPIHadoopFiles\(prefix:String,suffix:String\):Unit "Permalink") def saveAsNewAPIHadoopFiles(prefix: String, suffix: String): Unit
Save each RDD in `this` DStream as a Hadoop file.
Save each RDD in `this` DStream as a Hadoop file. The file name at each batch interval is generated based on `prefix` and `suffix`: "prefix-TIME_IN_MS.suffix".
  88. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#scalaIntToJavaLong\(in:org.apache.spark.streaming.dstream.DStream\[Long\]\):org.apache.spark.streaming.api.java.JavaDStream\[Long\] "Permalink") implicit  def scalaIntToJavaLong(in: [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[Long]): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[[Long](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html#java.lang.Long "java.lang.Long")]

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  89. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#slice\(fromTime:org.apache.spark.streaming.Time,toTime:org.apache.spark.streaming.Time\):java.util.List\[R\] "Permalink") def slice(fromTime: [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time"), toTime: [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time")): [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#java.util.List "java.util.List")[[JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K, V]]
Return all the RDDs between 'fromDuration' to 'toDuration' (both included)
Return all the RDDs between 'fromDuration' to 'toDuration' (both included)

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  90. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0

Definition Classes
    AnyRef
  91. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#toJavaDStream\(\):org.apache.spark.streaming.api.java.JavaDStream\[\(K,V\)\] "Permalink") def toJavaDStream(): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[(K, V)]
Convert to a JavaDStream
  92. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#toString\(\):String "Permalink") def toString(): [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String")

Definition Classes
    AnyRef → Any
  93. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#transform\[U\]\(transformFunc:org.apache.spark.api.java.function.Function2\[R,org.apache.spark.streaming.Time,org.apache.spark.api.java.JavaRDD\[U\]\]\):org.apache.spark.streaming.api.java.JavaDStream\[U\] "Permalink") def transform[U](transformFunc: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[[JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K, V], [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time"), [JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[U]]): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[U]
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream.
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream.

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  94. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#transform\[U\]\(transformFunc:org.apache.spark.api.java.function.Function\[R,org.apache.spark.api.java.JavaRDD\[U\]\]\):org.apache.spark.streaming.api.java.JavaDStream\[U\] "Permalink") def transform[U](transformFunc: [Function](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function.html "org.apache.spark.api.java.function.Function")[[JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K, V], [JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[U]]): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[U]
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream.
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream.

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  95. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#transformToPair\[K2,V2\]\(transformFunc:org.apache.spark.api.java.function.Function2\[R,org.apache.spark.streaming.Time,org.apache.spark.api.java.JavaPairRDD\[K2,V2\]\]\):org.apache.spark.streaming.api.java.JavaPairDStream\[K2,V2\] "Permalink") def transformToPair[K2, V2](transformFunc: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[[JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K, V], [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time"), [JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K2, V2]]): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K2, V2]
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream.
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream.

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  96. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#transformToPair\[K2,V2\]\(transformFunc:org.apache.spark.api.java.function.Function\[R,org.apache.spark.api.java.JavaPairRDD\[K2,V2\]\]\):org.apache.spark.streaming.api.java.JavaPairDStream\[K2,V2\] "Permalink") def transformToPair[K2, V2](transformFunc: [Function](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function.html "org.apache.spark.api.java.function.Function")[[JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K, V], [JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K2, V2]]): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K2, V2]
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream.
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream.

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  97. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#transformWith\[K2,V2,W\]\(other:org.apache.spark.streaming.api.java.JavaPairDStream\[K2,V2\],transformFunc:org.apache.spark.api.java.function.Function3\[R,org.apache.spark.api.java.JavaPairRDD\[K2,V2\],org.apache.spark.streaming.Time,org.apache.spark.api.java.JavaRDD\[W\]\]\):org.apache.spark.streaming.api.java.JavaDStream\[W\] "Permalink") def transformWith[K2, V2, W](other: [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K2, V2], transformFunc: [Function3](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function3.html "org.apache.spark.api.java.function.Function3")[[JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K, V], [JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K2, V2], [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time"), [JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[W]]): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[W]
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream and 'other' DStream.
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream and 'other' DStream.

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  98. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#transformWith\[U,W\]\(other:org.apache.spark.streaming.api.java.JavaDStream\[U\],transformFunc:org.apache.spark.api.java.function.Function3\[R,org.apache.spark.api.java.JavaRDD\[U\],org.apache.spark.streaming.Time,org.apache.spark.api.java.JavaRDD\[W\]\]\):org.apache.spark.streaming.api.java.JavaDStream\[W\] "Permalink") def transformWith[U, W](other: [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[U], transformFunc: [Function3](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function3.html "org.apache.spark.api.java.function.Function3")[[JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K, V], [JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[U], [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time"), [JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[W]]): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[W]
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream and 'other' DStream.
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream and 'other' DStream.

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  99. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#transformWithToPair\[K2,V2,K3,V3\]\(other:org.apache.spark.streaming.api.java.JavaPairDStream\[K2,V2\],transformFunc:org.apache.spark.api.java.function.Function3\[R,org.apache.spark.api.java.JavaPairRDD\[K2,V2\],org.apache.spark.streaming.Time,org.apache.spark.api.java.JavaPairRDD\[K3,V3\]\]\):org.apache.spark.streaming.api.java.JavaPairDStream\[K3,V3\] "Permalink") def transformWithToPair[K2, V2, K3, V3](other: [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K2, V2], transformFunc: [Function3](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function3.html "org.apache.spark.api.java.function.Function3")[[JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K, V], [JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K2, V2], [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time"), [JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K3, V3]]): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K3, V3]
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream and 'other' DStream.
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream and 'other' DStream.

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  100. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#transformWithToPair\[U,K2,V2\]\(other:org.apache.spark.streaming.api.java.JavaDStream\[U\],transformFunc:org.apache.spark.api.java.function.Function3\[R,org.apache.spark.api.java.JavaRDD\[U\],org.apache.spark.streaming.Time,org.apache.spark.api.java.JavaPairRDD\[K2,V2\]\]\):org.apache.spark.streaming.api.java.JavaPairDStream\[K2,V2\] "Permalink") def transformWithToPair[U, K2, V2](other: [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[U], transformFunc: [Function3](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function3.html "org.apache.spark.api.java.function.Function3")[[JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K, V], [JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[U], [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time"), [JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K2, V2]]): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K2, V2]
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream and 'other' DStream.
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream and 'other' DStream.

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  101. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#union\(that:org.apache.spark.streaming.api.java.JavaPairDStream\[K,V\]\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,V\] "Permalink") def union(that: [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, V]): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, V]
Return a new DStream by unifying data of another DStream with this DStream.
Return a new DStream by unifying data of another DStream with this DStream.

that

Another DStream having the same interval (i.e., slideDuration) as this DStream.
  102. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#updateStateByKey\[S\]\(updateFunc:org.apache.spark.api.java.function.Function2\[java.util.List\[V\],org.apache.spark.api.java.Optional\[S\],org.apache.spark.api.java.Optional\[S\]\],partitioner:org.apache.spark.Partitioner,initialRDD:org.apache.spark.api.java.JavaPairRDD\[K,S\]\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,S\] "Permalink") def updateStateByKey[S](updateFunc: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#java.util.List "java.util.List")[V], [Optional](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/Optional.html "org.apache.spark.api.java.Optional")[S], [Optional](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/Optional.html "org.apache.spark.api.java.Optional")[S]], partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner"), initialRDD: [JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K, S]): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, S]
Return a new "state" DStream where the state for each key is updated by applying the given function on the previous state of the key and the new values of the key.
Return a new "state" DStream where the state for each key is updated by applying the given function on the previous state of the key and the new values of the key. org.apache.spark.Partitioner is used to control the partitioning of each RDD.

S

State type

updateFunc

State update function. If `this` function returns None, then corresponding state key-value pair will be eliminated.

partitioner

Partitioner for controlling the partitioning of each RDD in the new DStream.

initialRDD

initial state value of each key.
  103. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#updateStateByKey\[S\]\(updateFunc:org.apache.spark.api.java.function.Function2\[java.util.List\[V\],org.apache.spark.api.java.Optional\[S\],org.apache.spark.api.java.Optional\[S\]\],partitioner:org.apache.spark.Partitioner\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,S\] "Permalink") def updateStateByKey[S](updateFunc: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#java.util.List "java.util.List")[V], [Optional](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/Optional.html "org.apache.spark.api.java.Optional")[S], [Optional](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/Optional.html "org.apache.spark.api.java.Optional")[S]], partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner")): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, S]
Return a new "state" DStream where the state for each key is updated by applying the given function on the previous state of the key and the new values of the key.
Return a new "state" DStream where the state for each key is updated by applying the given function on the previous state of the key and the new values of the key. org.apache.spark.Partitioner is used to control the partitioning of each RDD.

S

State type

updateFunc

State update function. If `this` function returns None, then corresponding state key-value pair will be eliminated.

partitioner

Partitioner for controlling the partitioning of each RDD in the new DStream.
  104. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#updateStateByKey\[S\]\(updateFunc:org.apache.spark.api.java.function.Function2\[java.util.List\[V\],org.apache.spark.api.java.Optional\[S\],org.apache.spark.api.java.Optional\[S\]\],numPartitions:Int\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,S\] "Permalink") def updateStateByKey[S](updateFunc: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#java.util.List "java.util.List")[V], [Optional](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/Optional.html "org.apache.spark.api.java.Optional")[S], [Optional](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/Optional.html "org.apache.spark.api.java.Optional")[S]], numPartitions: Int): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, S]
Return a new "state" DStream where the state for each key is updated by applying the given function on the previous state of the key and the new values of each key.
Return a new "state" DStream where the state for each key is updated by applying the given function on the previous state of the key and the new values of each key. Hash partitioning is used to generate the RDDs with `numPartitions` partitions.

S

State type

updateFunc

State update function. If `this` function returns None, then corresponding state key-value pair will be eliminated.

numPartitions

Number of partitions of each RDD in the new DStream.
  105. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#updateStateByKey\[S\]\(updateFunc:org.apache.spark.api.java.function.Function2\[java.util.List\[V\],org.apache.spark.api.java.Optional\[S\],org.apache.spark.api.java.Optional\[S\]\]\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,S\] "Permalink") def updateStateByKey[S](updateFunc: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#java.util.List "java.util.List")[V], [Optional](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/Optional.html "org.apache.spark.api.java.Optional")[S], [Optional](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/Optional.html "org.apache.spark.api.java.Optional")[S]]): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, S]
Return a new "state" DStream where the state for each key is updated by applying the given function on the previous state of the key and the new values of each key.
Return a new "state" DStream where the state for each key is updated by applying the given function on the previous state of the key and the new values of each key. Hash partitioning is used to generate the RDDs with Spark's default number of partitions.

S

State type

updateFunc

State update function. If `this` function returns None, then corresponding state key-value pair will be eliminated.
  106. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#vManifest:scala.reflect.ClassTag\[V\] "Permalink") implicit  val vManifest: ClassTag[V]
  107. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])
  108. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  109. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#wait\(\):Unit "Permalink") final  def wait(): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])
  110. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#window\(windowDuration:org.apache.spark.streaming.Duration,slideDuration:org.apache.spark.streaming.Duration\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,V\] "Permalink") def window(windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration")): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, V]
Return a new DStream which is computed based on windowed batches of this DStream.
Return a new DStream which is computed based on windowed batches of this DStream.

windowDuration

duration (i.e., width) of the window; must be a multiple of this DStream's interval

slideDuration

sliding interval of the window (i.e., the interval after which the new DStream will generate RDDs); must be a multiple of this DStream's interval
  111. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#window\(windowDuration:org.apache.spark.streaming.Duration\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,V\] "Permalink") def window(windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration")): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, V]
Return a new DStream which is computed based on windowed batches of this DStream.
Return a new DStream which is computed based on windowed batches of this DStream. The new DStream generates RDDs with the same interval as this DStream.

windowDuration

width of the window; must be a multiple of this DStream's interval.
  112. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#wrapRDD\(rdd:org.apache.spark.rdd.RDD\[\(K,V\)\]\):org.apache.spark.api.java.JavaPairRDD\[K,V\] "Permalink") def wrapRDD(rdd: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, V)]): [JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K, V]

Definition Classes
     [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream") → [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  113. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html#finalize\(\):Unit "Permalink") def finalize(): Unit

Attributes
    protected[lang]

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.Throwable]) @Deprecated

Deprecated

_(Since version 9)_
