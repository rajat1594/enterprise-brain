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
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/index.html "Permalink") package [dstream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/index.html "Various implementations of DStream's.")
Various implementations of DStream's.
Various implementations of DStream's.

Definition Classes
    [streaming](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/index.html "org.apache.spark.streaming")

See also

[org.apache.spark.streaming.dstream.DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/ConstantInputDStream.html "An input stream that always returns the same RDD on each time step.")[ConstantInputDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/ConstantInputDStream.html "An input stream that always returns the same RDD on each time step.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream$.html) [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "A Discretized Stream \(DStream\), the basic abstraction in Spark Streaming, is a continuous sequence of RDDs \(of the same type\) representing a continuous stream of data \(see org.apache.spark.rdd.RDD in the Spark core documentation for more details on RDDs\).")[DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "A Discretized Stream \(DStream\), the basic abstraction in Spark Streaming, is a continuous sequence of RDDs \(of the same type\) representing a continuous stream of data \(see org.apache.spark.rdd.RDD in the Spark core documentation for more details on RDDs\).")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/InputDStream.html "This is the abstract base class for all input streams.")[InputDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/InputDStream.html "This is the abstract base class for all input streams.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/MapWithStateDStream.html "DStream representing the stream of data generated by mapWithState operation on a pair DStream.")[MapWithStateDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/MapWithStateDStream.html "DStream representing the stream of data generated by mapWithState operation on a pair DStream.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html "Extra functions available on DStream of \(key, value\) pairs through an implicit conversion.")[PairDStreamFunctions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html "Extra functions available on DStream of \(key, value\) pairs through an implicit conversion.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/ReceiverInputDStream.html "Abstract class for defining any org.apache.spark.streaming.dstream.InputDStream that has to start a receiver on worker nodes to receive external data.")[ReceiverInputDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/ReceiverInputDStream.html "Abstract class for defining any org.apache.spark.streaming.dstream.InputDStream that has to start a receiver on worker nodes to receive external data.")

c
[org](https://spark.apache.org/docs/latest/api/scala/org/index.html "org").[apache](https://spark.apache.org/docs/latest/api/scala/org/apache/index.html "org.apache").[spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark").[streaming](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/index.html "org.apache.spark.streaming").[dstream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/index.html "org.apache.spark.streaming.dstream")
# PairDStreamFunctions[ __](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html "Permalink")
####  class PairDStreamFunctions[K, V] extends Serializable
Extra functions available on DStream of (key, value) pairs through an implicit conversion.

Source
    [PairDStreamFunctions.scala](https://github.com/apache/spark/tree/v4.1.2/streaming/src/main/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.scala)
Linear Supertypes
[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable"), AnyRef, Any
__ __
Ordering
  1. Alphabetic
  2. By Inheritance

Inherited

  1. PairDStreamFunctions
  2. Serializable
  3. AnyRef
  4. Any

  1. Hide All
  2. Show All

Visibility
  1. Public
  2. Protected

### Instance Constructors
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#<init>\(self:org.apache.spark.streaming.dstream.DStream\[\(K,V\)\]\)\(implicitkt:scala.reflect.ClassTag\[K\],implicitvt:scala.reflect.ClassTag\[V\],implicitord:Ordering\[K\]\):org.apache.spark.streaming.dstream.PairDStreamFunctions\[K,V\] "Permalink") new PairDStreamFunctions(self: [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, V)])(implicit kt: ClassTag[K], vt: ClassTag[V], ord: Ordering[K])

### Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html###:Int "Permalink") final  def ##: Int

Definition Classes
    AnyRef → Any
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0

Definition Classes
    Any
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#clone\(\):Object "Permalink") def clone(): AnyRef

Attributes
    protected[lang]

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#cogroup\[W\]\(other:org.apache.spark.streaming.dstream.DStream\[\(K,W\)\],partitioner:org.apache.spark.Partitioner\)\(implicitevidence$15:scala.reflect.ClassTag\[W\]\):org.apache.spark.streaming.dstream.DStream\[\(K,\(Iterable\[V\],Iterable\[W\]\)\)\] "Permalink") def cogroup[W](other: [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, W)], partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner"))(implicit arg0: ClassTag[W]): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, (Iterable[V], Iterable[W]))]
Return a new DStream by applying 'cogroup' between RDDs of `this` DStream and `other` DStream.
Return a new DStream by applying 'cogroup' between RDDs of `this` DStream and `other` DStream. The supplied org.apache.spark.Partitioner is used to partition the generated RDDs.
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#cogroup\[W\]\(other:org.apache.spark.streaming.dstream.DStream\[\(K,W\)\],numPartitions:Int\)\(implicitevidence$14:scala.reflect.ClassTag\[W\]\):org.apache.spark.streaming.dstream.DStream\[\(K,\(Iterable\[V\],Iterable\[W\]\)\)\] "Permalink") def cogroup[W](other: [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, W)], numPartitions: Int)(implicit arg0: ClassTag[W]): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, (Iterable[V], Iterable[W]))]
Return a new DStream by applying 'cogroup' between RDDs of `this` DStream and `other` DStream.
Return a new DStream by applying 'cogroup' between RDDs of `this` DStream and `other` DStream. Hash partitioning is used to generate the RDDs with `numPartitions` partitions.
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#cogroup\[W\]\(other:org.apache.spark.streaming.dstream.DStream\[\(K,W\)\]\)\(implicitevidence$13:scala.reflect.ClassTag\[W\]\):org.apache.spark.streaming.dstream.DStream\[\(K,\(Iterable\[V\],Iterable\[W\]\)\)\] "Permalink") def cogroup[W](other: [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, W)])(implicit arg0: ClassTag[W]): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, (Iterable[V], Iterable[W]))]
Return a new DStream by applying 'cogroup' between RDDs of `this` DStream and `other` DStream.
Return a new DStream by applying 'cogroup' between RDDs of `this` DStream and `other` DStream. Hash partitioning is used to generate the RDDs with Spark's default number of partitions.
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#combineByKey\[C\]\(createCombiner:V=>C,mergeValue:\(C,V\)=>C,mergeCombiner:\(C,C\)=>C,partitioner:org.apache.spark.Partitioner,mapSideCombine:Boolean\)\(implicitevidence$1:scala.reflect.ClassTag\[C\]\):org.apache.spark.streaming.dstream.DStream\[\(K,C\)\] "Permalink") def combineByKey[C](createCombiner: (V) => C, mergeValue: (C, V) => C, mergeCombiner: (C, C) => C, partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner"), mapSideCombine: Boolean = true)(implicit arg0: ClassTag[C]): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, C)]
Combine elements of each key in DStream's RDDs using custom functions.
Combine elements of each key in DStream's RDDs using custom functions. This is similar to the combineByKey for RDDs. Please refer to combineByKey in org.apache.spark.rdd.PairRDDFunctions in the Spark core documentation for more information.
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#equals\(x$1:Object\):Boolean "Permalink") def equals(arg0: AnyRef): Boolean

Definition Classes
    AnyRef → Any
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#flatMapValues\[U\]\(flatMapValuesFunc:V=>IterableOnce\[U\]\)\(implicitevidence$12:scala.reflect.ClassTag\[U\]\):org.apache.spark.streaming.dstream.DStream\[\(K,U\)\] "Permalink") def flatMapValues[U](flatMapValuesFunc: (V) => IterableOnce[U])(implicit arg0: ClassTag[U]): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, U)]
Return a new DStream by applying a flatmap function to the value of each key-value pairs in 'this' DStream without changing the key.
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#fullOuterJoin\[W\]\(other:org.apache.spark.streaming.dstream.DStream\[\(K,W\)\],partitioner:org.apache.spark.Partitioner\)\(implicitevidence$27:scala.reflect.ClassTag\[W\]\):org.apache.spark.streaming.dstream.DStream\[\(K,\(Option\[V\],Option\[W\]\)\)\] "Permalink") def fullOuterJoin[W](other: [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, W)], partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner"))(implicit arg0: ClassTag[W]): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, (Option[V], Option[W]))]
Return a new DStream by applying 'full outer join' between RDDs of `this` DStream and `other` DStream.
Return a new DStream by applying 'full outer join' between RDDs of `this` DStream and `other` DStream. The supplied org.apache.spark.Partitioner is used to control the partitioning of each RDD.
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#fullOuterJoin\[W\]\(other:org.apache.spark.streaming.dstream.DStream\[\(K,W\)\],numPartitions:Int\)\(implicitevidence$26:scala.reflect.ClassTag\[W\]\):org.apache.spark.streaming.dstream.DStream\[\(K,\(Option\[V\],Option\[W\]\)\)\] "Permalink") def fullOuterJoin[W](other: [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, W)], numPartitions: Int)(implicit arg0: ClassTag[W]): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, (Option[V], Option[W]))]
Return a new DStream by applying 'full outer join' between RDDs of `this` DStream and `other` DStream.
Return a new DStream by applying 'full outer join' between RDDs of `this` DStream and `other` DStream. Hash partitioning is used to generate the RDDs with `numPartitions` partitions.
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#fullOuterJoin\[W\]\(other:org.apache.spark.streaming.dstream.DStream\[\(K,W\)\]\)\(implicitevidence$25:scala.reflect.ClassTag\[W\]\):org.apache.spark.streaming.dstream.DStream\[\(K,\(Option\[V\],Option\[W\]\)\)\] "Permalink") def fullOuterJoin[W](other: [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, W)])(implicit arg0: ClassTag[W]): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, (Option[V], Option[W]))]
Return a new DStream by applying 'full outer join' between RDDs of `this` DStream and `other` DStream.
Return a new DStream by applying 'full outer join' between RDDs of `this` DStream and `other` DStream. Hash partitioning is used to generate the RDDs with Spark's default number of partitions.
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef]

Definition Classes
    AnyRef → Any

Annotations
     @IntrinsicCandidate() @native()
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#groupByKey\(partitioner:org.apache.spark.Partitioner\):org.apache.spark.streaming.dstream.DStream\[\(K,Iterable\[V\]\)\] "Permalink") def groupByKey(partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner")): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, Iterable[V])]
Return a new DStream by applying `groupByKey` on each RDD.
Return a new DStream by applying `groupByKey` on each RDD. The supplied org.apache.spark.Partitioner is used to control the partitioning of each RDD.
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#groupByKey\(numPartitions:Int\):org.apache.spark.streaming.dstream.DStream\[\(K,Iterable\[V\]\)\] "Permalink") def groupByKey(numPartitions: Int): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, Iterable[V])]
Return a new DStream by applying `groupByKey` to each RDD.
Return a new DStream by applying `groupByKey` to each RDD. Hash partitioning is used to generate the RDDs with `numPartitions` partitions.
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#groupByKey\(\):org.apache.spark.streaming.dstream.DStream\[\(K,Iterable\[V\]\)\] "Permalink") def groupByKey(): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, Iterable[V])]
Return a new DStream by applying `groupByKey` to each RDD.
Return a new DStream by applying `groupByKey` to each RDD. Hash partitioning is used to generate the RDDs with Spark's default number of partitions.
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#groupByKeyAndWindow\(windowDuration:org.apache.spark.streaming.Duration,slideDuration:org.apache.spark.streaming.Duration,partitioner:org.apache.spark.Partitioner\):org.apache.spark.streaming.dstream.DStream\[\(K,Iterable\[V\]\)\] "Permalink") def groupByKeyAndWindow(windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner")): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, Iterable[V])]
Create a new DStream by applying `groupByKey` over a sliding window on `this` DStream.
Create a new DStream by applying `groupByKey` over a sliding window on `this` DStream. Similar to `DStream.groupByKey()`, but applies it over a sliding window.

windowDuration

width of the window; must be a multiple of this DStream's batching interval

slideDuration

sliding interval of the window (i.e., the interval after which the new DStream will generate RDDs); must be a multiple of this DStream's batching interval

partitioner

partitioner for controlling the partitioning of each RDD in the new DStream.
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#groupByKeyAndWindow\(windowDuration:org.apache.spark.streaming.Duration,slideDuration:org.apache.spark.streaming.Duration,numPartitions:Int\):org.apache.spark.streaming.dstream.DStream\[\(K,Iterable\[V\]\)\] "Permalink") def groupByKeyAndWindow(windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), numPartitions: Int): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, Iterable[V])]
Return a new DStream by applying `groupByKey` over a sliding window on `this` DStream.
Return a new DStream by applying `groupByKey` over a sliding window on `this` DStream. Similar to `DStream.groupByKey()`, but applies it over a sliding window. Hash partitioning is used to generate the RDDs with `numPartitions` partitions.

windowDuration

width of the window; must be a multiple of this DStream's batching interval

slideDuration

sliding interval of the window (i.e., the interval after which the new DStream will generate RDDs); must be a multiple of this DStream's batching interval

numPartitions

number of partitions of each RDD in the new DStream; if not specified then Spark's default number of partitions will be used
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#groupByKeyAndWindow\(windowDuration:org.apache.spark.streaming.Duration,slideDuration:org.apache.spark.streaming.Duration\):org.apache.spark.streaming.dstream.DStream\[\(K,Iterable\[V\]\)\] "Permalink") def groupByKeyAndWindow(windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration")): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, Iterable[V])]
Return a new DStream by applying `groupByKey` over a sliding window.
Return a new DStream by applying `groupByKey` over a sliding window. Similar to `DStream.groupByKey()`, but applies it over a sliding window. Hash partitioning is used to generate the RDDs with Spark's default number of partitions.

windowDuration

width of the window; must be a multiple of this DStream's batching interval

slideDuration

sliding interval of the window (i.e., the interval after which the new DStream will generate RDDs); must be a multiple of this DStream's batching interval
  23. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#groupByKeyAndWindow\(windowDuration:org.apache.spark.streaming.Duration\):org.apache.spark.streaming.dstream.DStream\[\(K,Iterable\[V\]\)\] "Permalink") def groupByKeyAndWindow(windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration")): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, Iterable[V])]
Return a new DStream by applying `groupByKey` over a sliding window.
Return a new DStream by applying `groupByKey` over a sliding window. This is similar to `DStream.groupByKey()` but applies it over a sliding window. The new DStream generates RDDs with the same interval as this DStream. Hash partitioning is used to generate the RDDs with Spark's default number of partitions.

windowDuration

width of the window; must be a multiple of this DStream's batching interval
  24. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#hashCode\(\):Int "Permalink") def hashCode(): Int

Definition Classes
    AnyRef → Any

Annotations
     @IntrinsicCandidate() @native()
  25. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean

Definition Classes
    Any
  26. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#join\[W\]\(other:org.apache.spark.streaming.dstream.DStream\[\(K,W\)\],partitioner:org.apache.spark.Partitioner\)\(implicitevidence$18:scala.reflect.ClassTag\[W\]\):org.apache.spark.streaming.dstream.DStream\[\(K,\(V,W\)\)\] "Permalink") def join[W](other: [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, W)], partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner"))(implicit arg0: ClassTag[W]): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, (V, W))]
Return a new DStream by applying 'join' between RDDs of `this` DStream and `other` DStream.
Return a new DStream by applying 'join' between RDDs of `this` DStream and `other` DStream. The supplied org.apache.spark.Partitioner is used to control the partitioning of each RDD.
  27. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#join\[W\]\(other:org.apache.spark.streaming.dstream.DStream\[\(K,W\)\],numPartitions:Int\)\(implicitevidence$17:scala.reflect.ClassTag\[W\]\):org.apache.spark.streaming.dstream.DStream\[\(K,\(V,W\)\)\] "Permalink") def join[W](other: [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, W)], numPartitions: Int)(implicit arg0: ClassTag[W]): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, (V, W))]
Return a new DStream by applying 'join' between RDDs of `this` DStream and `other` DStream.
Return a new DStream by applying 'join' between RDDs of `this` DStream and `other` DStream. Hash partitioning is used to generate the RDDs with `numPartitions` partitions.
  28. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#join\[W\]\(other:org.apache.spark.streaming.dstream.DStream\[\(K,W\)\]\)\(implicitevidence$16:scala.reflect.ClassTag\[W\]\):org.apache.spark.streaming.dstream.DStream\[\(K,\(V,W\)\)\] "Permalink") def join[W](other: [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, W)])(implicit arg0: ClassTag[W]): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, (V, W))]
Return a new DStream by applying 'join' between RDDs of `this` DStream and `other` DStream.
Return a new DStream by applying 'join' between RDDs of `this` DStream and `other` DStream. Hash partitioning is used to generate the RDDs with Spark's default number of partitions.
  29. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#leftOuterJoin\[W\]\(other:org.apache.spark.streaming.dstream.DStream\[\(K,W\)\],partitioner:org.apache.spark.Partitioner\)\(implicitevidence$21:scala.reflect.ClassTag\[W\]\):org.apache.spark.streaming.dstream.DStream\[\(K,\(V,Option\[W\]\)\)\] "Permalink") def leftOuterJoin[W](other: [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, W)], partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner"))(implicit arg0: ClassTag[W]): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, (V, Option[W]))]
Return a new DStream by applying 'left outer join' between RDDs of `this` DStream and `other` DStream.
Return a new DStream by applying 'left outer join' between RDDs of `this` DStream and `other` DStream. The supplied org.apache.spark.Partitioner is used to control the partitioning of each RDD.
  30. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#leftOuterJoin\[W\]\(other:org.apache.spark.streaming.dstream.DStream\[\(K,W\)\],numPartitions:Int\)\(implicitevidence$20:scala.reflect.ClassTag\[W\]\):org.apache.spark.streaming.dstream.DStream\[\(K,\(V,Option\[W\]\)\)\] "Permalink") def leftOuterJoin[W](other: [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, W)], numPartitions: Int)(implicit arg0: ClassTag[W]): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, (V, Option[W]))]
Return a new DStream by applying 'left outer join' between RDDs of `this` DStream and `other` DStream.
Return a new DStream by applying 'left outer join' between RDDs of `this` DStream and `other` DStream. Hash partitioning is used to generate the RDDs with `numPartitions` partitions.
  31. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#leftOuterJoin\[W\]\(other:org.apache.spark.streaming.dstream.DStream\[\(K,W\)\]\)\(implicitevidence$19:scala.reflect.ClassTag\[W\]\):org.apache.spark.streaming.dstream.DStream\[\(K,\(V,Option\[W\]\)\)\] "Permalink") def leftOuterJoin[W](other: [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, W)])(implicit arg0: ClassTag[W]): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, (V, Option[W]))]
Return a new DStream by applying 'left outer join' between RDDs of `this` DStream and `other` DStream.
Return a new DStream by applying 'left outer join' between RDDs of `this` DStream and `other` DStream. Hash partitioning is used to generate the RDDs with Spark's default number of partitions.
  32. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#mapValues\[U\]\(mapValuesFunc:V=>U\)\(implicitevidence$11:scala.reflect.ClassTag\[U\]\):org.apache.spark.streaming.dstream.DStream\[\(K,U\)\] "Permalink") def mapValues[U](mapValuesFunc: (V) => U)(implicit arg0: ClassTag[U]): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, U)]
Return a new DStream by applying a map function to the value of each key-value pairs in 'this' DStream without changing the key.
  33. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#mapWithState\[StateType,MappedType\]\(spec:org.apache.spark.streaming.StateSpec\[K,V,StateType,MappedType\]\)\(implicitevidence$2:scala.reflect.ClassTag\[StateType\],implicitevidence$3:scala.reflect.ClassTag\[MappedType\]\):org.apache.spark.streaming.dstream.MapWithStateDStream\[K,V,StateType,MappedType\] "Permalink") def mapWithState[StateType, MappedType](spec: [StateSpec](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StateSpec.html "org.apache.spark.streaming.StateSpec")[K, V, StateType, MappedType])(implicit arg0: ClassTag[StateType], arg1: ClassTag[MappedType]): [MapWithStateDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/MapWithStateDStream.html "org.apache.spark.streaming.dstream.MapWithStateDStream")[K, V, StateType, MappedType]
Return a [MapWithStateDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/MapWithStateDStream.html "org.apache.spark.streaming.dstream.MapWithStateDStream") by applying a function to every key-value element of `this` stream, while maintaining some state data for each unique key.
Return a [MapWithStateDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/MapWithStateDStream.html "org.apache.spark.streaming.dstream.MapWithStateDStream") by applying a function to every key-value element of `this` stream, while maintaining some state data for each unique key. The mapping function and other specification (e.g. partitioners, timeouts, initial state data, etc.) of this transformation can be specified using `StateSpec` class. The state data is accessible in as a parameter of type `State` in the mapping function.
Example of using `mapWithState`:

```
// A mapping function that maintains an integer state and return a String
def mappingFunction(key: String, value: Option[Int], state: State[Int]): Option[String] = {
  // Use state.exists(), state.get(), state.update() and state.remove()
  // to manage state, and return the necessary string
}

val spec = StateSpec.function(mappingFunction).numPartitions(10)

val mapWithStateDStream = keyValueDStream.mapWithState[StateType, MappedType](spec)
```

StateType

Class type of the state data

MappedType

Class type of the mapped data

spec

Specification of this transformation
  34. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  35. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#notify\(\):Unit "Permalink") final  def notify(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  36. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  37. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#reduceByKey\(reduceFunc:\(V,V\)=>V,partitioner:org.apache.spark.Partitioner\):org.apache.spark.streaming.dstream.DStream\[\(K,V\)\] "Permalink") def reduceByKey(reduceFunc: (V, V) => V, partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner")): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, V)]
Return a new DStream by applying `reduceByKey` to each RDD.
Return a new DStream by applying `reduceByKey` to each RDD. The values for each key are merged using the supplied reduce function. org.apache.spark.Partitioner is used to control the partitioning of each RDD.
  38. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#reduceByKey\(reduceFunc:\(V,V\)=>V,numPartitions:Int\):org.apache.spark.streaming.dstream.DStream\[\(K,V\)\] "Permalink") def reduceByKey(reduceFunc: (V, V) => V, numPartitions: Int): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, V)]
Return a new DStream by applying `reduceByKey` to each RDD.
Return a new DStream by applying `reduceByKey` to each RDD. The values for each key are merged using the supplied reduce function. Hash partitioning is used to generate the RDDs with `numPartitions` partitions.
  39. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#reduceByKey\(reduceFunc:\(V,V\)=>V\):org.apache.spark.streaming.dstream.DStream\[\(K,V\)\] "Permalink") def reduceByKey(reduceFunc: (V, V) => V): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, V)]
Return a new DStream by applying `reduceByKey` to each RDD.
Return a new DStream by applying `reduceByKey` to each RDD. The values for each key are merged using the associative and commutative reduce function. Hash partitioning is used to generate the RDDs with Spark's default number of partitions.
  40. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#reduceByKeyAndWindow\(reduceFunc:\(V,V\)=>V,invReduceFunc:\(V,V\)=>V,windowDuration:org.apache.spark.streaming.Duration,slideDuration:org.apache.spark.streaming.Duration,partitioner:org.apache.spark.Partitioner,filterFunc:\(\(K,V\)\)=>Boolean\):org.apache.spark.streaming.dstream.DStream\[\(K,V\)\] "Permalink") def reduceByKeyAndWindow(reduceFunc: (V, V) => V, invReduceFunc: (V, V) => V, windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner"), filterFunc: ((K, V)) => Boolean): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, V)]
Return a new DStream by applying incremental `reduceByKey` over a sliding window.
Return a new DStream by applying incremental `reduceByKey` over a sliding window. The reduced value of over a new window is calculated using the old window's reduced value :
    1. reduce the new values that entered the window (e.g., adding new counts) 2. "inverse reduce" the old values that left the window (e.g., subtracting old counts) This is more efficient than reduceByKeyAndWindow without "inverse reduce" function. However, it is applicable to only "invertible reduce functions".

reduceFunc

associative and commutative reduce function

invReduceFunc

inverse reduce function

windowDuration

width of the window; must be a multiple of this DStream's batching interval

slideDuration

sliding interval of the window (i.e., the interval after which the new DStream will generate RDDs); must be a multiple of this DStream's batching interval

partitioner

partitioner for controlling the partitioning of each RDD in the new DStream.

filterFunc

Optional function to filter expired key-value pairs; only pairs that satisfy the function are retained
  41. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#reduceByKeyAndWindow\(reduceFunc:\(V,V\)=>V,invReduceFunc:\(V,V\)=>V,windowDuration:org.apache.spark.streaming.Duration,slideDuration:org.apache.spark.streaming.Duration,numPartitions:Int,filterFunc:\(\(K,V\)\)=>Boolean\):org.apache.spark.streaming.dstream.DStream\[\(K,V\)\] "Permalink") def reduceByKeyAndWindow(reduceFunc: (V, V) => V, invReduceFunc: (V, V) => V, windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration") = [self.slideDuration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#slideDuration:org.apache.spark.streaming.Duration), numPartitions: Int = [ssc.sc.defaultParallelism](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#defaultParallelism:Int), filterFunc: ((K, V)) => Boolean = null): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, V)]
Return a new DStream by applying incremental `reduceByKey` over a sliding window.
Return a new DStream by applying incremental `reduceByKey` over a sliding window. The reduced value of over a new window is calculated using the old window's reduced value :
    1. reduce the new values that entered the window (e.g., adding new counts)
2. "inverse reduce" the old values that left the window (e.g., subtracting old counts)
This is more efficient than reduceByKeyAndWindow without "inverse reduce" function. However, it is applicable to only "invertible reduce functions". Hash partitioning is used to generate the RDDs with Spark's default number of partitions.

reduceFunc

associative and commutative reduce function

invReduceFunc

inverse reduce function; such that for all y, invertible x: `invReduceFunc(reduceFunc(x, y), x) = y`

windowDuration

width of the window; must be a multiple of this DStream's batching interval

slideDuration

sliding interval of the window (i.e., the interval after which the new DStream will generate RDDs); must be a multiple of this DStream's batching interval

filterFunc

Optional function to filter expired key-value pairs; only pairs that satisfy the function are retained
  42. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#reduceByKeyAndWindow\(reduceFunc:\(V,V\)=>V,windowDuration:org.apache.spark.streaming.Duration,slideDuration:org.apache.spark.streaming.Duration,partitioner:org.apache.spark.Partitioner\):org.apache.spark.streaming.dstream.DStream\[\(K,V\)\] "Permalink") def reduceByKeyAndWindow(reduceFunc: (V, V) => V, windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner")): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, V)]
Return a new DStream by applying `reduceByKey` over a sliding window.
Return a new DStream by applying `reduceByKey` over a sliding window. Similar to `DStream.reduceByKey()`, but applies it over a sliding window.

reduceFunc

associative and commutative reduce function

windowDuration

width of the window; must be a multiple of this DStream's batching interval

slideDuration

sliding interval of the window (i.e., the interval after which the new DStream will generate RDDs); must be a multiple of this DStream's batching interval

partitioner

partitioner for controlling the partitioning of each RDD in the new DStream.
  43. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#reduceByKeyAndWindow\(reduceFunc:\(V,V\)=>V,windowDuration:org.apache.spark.streaming.Duration,slideDuration:org.apache.spark.streaming.Duration,numPartitions:Int\):org.apache.spark.streaming.dstream.DStream\[\(K,V\)\] "Permalink") def reduceByKeyAndWindow(reduceFunc: (V, V) => V, windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), numPartitions: Int): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, V)]
Return a new DStream by applying `reduceByKey` over a sliding window.
Return a new DStream by applying `reduceByKey` over a sliding window. This is similar to `DStream.reduceByKey()` but applies it over a sliding window. Hash partitioning is used to generate the RDDs with `numPartitions` partitions.

reduceFunc

associative and commutative reduce function

windowDuration

width of the window; must be a multiple of this DStream's batching interval

slideDuration

sliding interval of the window (i.e., the interval after which the new DStream will generate RDDs); must be a multiple of this DStream's batching interval

numPartitions

number of partitions of each RDD in the new DStream.
  44. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#reduceByKeyAndWindow\(reduceFunc:\(V,V\)=>V,windowDuration:org.apache.spark.streaming.Duration,slideDuration:org.apache.spark.streaming.Duration\):org.apache.spark.streaming.dstream.DStream\[\(K,V\)\] "Permalink") def reduceByKeyAndWindow(reduceFunc: (V, V) => V, windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration")): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, V)]
Return a new DStream by applying `reduceByKey` over a sliding window.
Return a new DStream by applying `reduceByKey` over a sliding window. This is similar to `DStream.reduceByKey()` but applies it over a sliding window. Hash partitioning is used to generate the RDDs with Spark's default number of partitions.

reduceFunc

associative and commutative reduce function

windowDuration

width of the window; must be a multiple of this DStream's batching interval

slideDuration

sliding interval of the window (i.e., the interval after which the new DStream will generate RDDs); must be a multiple of this DStream's batching interval
  45. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#reduceByKeyAndWindow\(reduceFunc:\(V,V\)=>V,windowDuration:org.apache.spark.streaming.Duration\):org.apache.spark.streaming.dstream.DStream\[\(K,V\)\] "Permalink") def reduceByKeyAndWindow(reduceFunc: (V, V) => V, windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration")): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, V)]
Return a new DStream by applying `reduceByKey` over a sliding window on `this` DStream.
Return a new DStream by applying `reduceByKey` over a sliding window on `this` DStream. Similar to `DStream.reduceByKey()`, but applies it over a sliding window. The new DStream generates RDDs with the same interval as this DStream. Hash partitioning is used to generate the RDDs with Spark's default number of partitions.

reduceFunc

associative and commutative reduce function

windowDuration

width of the window; must be a multiple of this DStream's batching interval
  46. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#rightOuterJoin\[W\]\(other:org.apache.spark.streaming.dstream.DStream\[\(K,W\)\],partitioner:org.apache.spark.Partitioner\)\(implicitevidence$24:scala.reflect.ClassTag\[W\]\):org.apache.spark.streaming.dstream.DStream\[\(K,\(Option\[V\],W\)\)\] "Permalink") def rightOuterJoin[W](other: [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, W)], partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner"))(implicit arg0: ClassTag[W]): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, (Option[V], W))]
Return a new DStream by applying 'right outer join' between RDDs of `this` DStream and `other` DStream.
Return a new DStream by applying 'right outer join' between RDDs of `this` DStream and `other` DStream. The supplied org.apache.spark.Partitioner is used to control the partitioning of each RDD.
  47. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#rightOuterJoin\[W\]\(other:org.apache.spark.streaming.dstream.DStream\[\(K,W\)\],numPartitions:Int\)\(implicitevidence$23:scala.reflect.ClassTag\[W\]\):org.apache.spark.streaming.dstream.DStream\[\(K,\(Option\[V\],W\)\)\] "Permalink") def rightOuterJoin[W](other: [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, W)], numPartitions: Int)(implicit arg0: ClassTag[W]): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, (Option[V], W))]
Return a new DStream by applying 'right outer join' between RDDs of `this` DStream and `other` DStream.
Return a new DStream by applying 'right outer join' between RDDs of `this` DStream and `other` DStream. Hash partitioning is used to generate the RDDs with `numPartitions` partitions.
  48. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#rightOuterJoin\[W\]\(other:org.apache.spark.streaming.dstream.DStream\[\(K,W\)\]\)\(implicitevidence$22:scala.reflect.ClassTag\[W\]\):org.apache.spark.streaming.dstream.DStream\[\(K,\(Option\[V\],W\)\)\] "Permalink") def rightOuterJoin[W](other: [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, W)])(implicit arg0: ClassTag[W]): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, (Option[V], W))]
Return a new DStream by applying 'right outer join' between RDDs of `this` DStream and `other` DStream.
Return a new DStream by applying 'right outer join' between RDDs of `this` DStream and `other` DStream. Hash partitioning is used to generate the RDDs with Spark's default number of partitions.
  49. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#saveAsHadoopFiles\(prefix:String,suffix:String,keyClass:Class\[_\],valueClass:Class\[_\],outputFormatClass:Class\[_<:org.apache.hadoop.mapred.OutputFormat\[_,_\]\],conf:org.apache.hadoop.mapred.JobConf\):Unit "Permalink") def saveAsHadoopFiles(prefix: String, suffix: String, keyClass: Class[_], valueClass: Class[_], outputFormatClass: Class[_ <: OutputFormat[_, _]], conf: JobConf = [new JobConf(ssc.sparkContext.hadoopConfiguration)](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#sparkContext:org.apache.spark.SparkContext)): Unit
Save each RDD in `this` DStream as a Hadoop file.
Save each RDD in `this` DStream as a Hadoop file. The file name at each batch interval is generated based on `prefix` and `suffix`: "prefix-TIME_IN_MS.suffix"
  50. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#saveAsHadoopFiles\[F<:org.apache.hadoop.mapred.OutputFormat\[K,V\]\]\(prefix:String,suffix:String\)\(implicitfm:scala.reflect.ClassTag\[F\]\):Unit "Permalink") def saveAsHadoopFiles[F <: OutputFormat[K, V]](prefix: String, suffix: String)(implicit fm: ClassTag[F]): Unit
Save each RDD in `this` DStream as a Hadoop file.
Save each RDD in `this` DStream as a Hadoop file. The file name at each batch interval is generated based on `prefix` and `suffix`: "prefix-TIME_IN_MS.suffix"
  51. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#saveAsNewAPIHadoopFiles\(prefix:String,suffix:String,keyClass:Class\[_\],valueClass:Class\[_\],outputFormatClass:Class\[_<:org.apache.hadoop.mapreduce.OutputFormat\[_,_\]\],conf:org.apache.hadoop.conf.Configuration\):Unit "Permalink") def saveAsNewAPIHadoopFiles(prefix: String, suffix: String, keyClass: Class[_], valueClass: Class[_], outputFormatClass: Class[_ <: OutputFormat[_, _]], conf: Configuration = [ssc.sparkContext.hadoopConfiguration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#sparkContext:org.apache.spark.SparkContext)): Unit
Save each RDD in `this` DStream as a Hadoop file.
Save each RDD in `this` DStream as a Hadoop file. The file name at each batch interval is generated based on `prefix` and `suffix`: "prefix-TIME_IN_MS.suffix".
  52. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#saveAsNewAPIHadoopFiles\[F<:org.apache.hadoop.mapreduce.OutputFormat\[K,V\]\]\(prefix:String,suffix:String\)\(implicitfm:scala.reflect.ClassTag\[F\]\):Unit "Permalink") def saveAsNewAPIHadoopFiles[F <: OutputFormat[K, V]](prefix: String, suffix: String)(implicit fm: ClassTag[F]): Unit
Save each RDD in `this` DStream as a Hadoop file.
Save each RDD in `this` DStream as a Hadoop file. The file name at each batch interval is generated based on `prefix` and `suffix`: "prefix-TIME_IN_MS.suffix".
  53. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0

Definition Classes
    AnyRef
  54. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#toString\(\):String "Permalink") def toString(): [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String")

Definition Classes
    AnyRef → Any
  55. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#updateStateByKey\[S\]\(updateFunc:\(org.apache.spark.streaming.Time,K,Seq\[V\],Option\[S\]\)=>Option\[S\],partitioner:org.apache.spark.Partitioner,rememberPartitioner:Boolean,initialRDD:Option\[org.apache.spark.rdd.RDD\[\(K,S\)\]\]\)\(implicitevidence$10:scala.reflect.ClassTag\[S\]\):org.apache.spark.streaming.dstream.DStream\[\(K,S\)\] "Permalink") def updateStateByKey[S](updateFunc: ([Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time"), K, Seq[V], Option[S]) => Option[S], partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner"), rememberPartitioner: Boolean, initialRDD: Option[[RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, S)]] = None)(implicit arg0: ClassTag[S]): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, S)]
Return a new "state" DStream where the state for each key is updated by applying the given function on the previous state of the key and the new values of the key.
Return a new "state" DStream where the state for each key is updated by applying the given function on the previous state of the key and the new values of the key. In every batch the updateFunc will be called for each state even if there are no new values. org.apache.spark.Partitioner is used to control the partitioning of each RDD.

S

State type

updateFunc

State update function. If `this` function returns None, then corresponding state key-value pair will be eliminated.

partitioner

Partitioner for controlling the partitioning of each RDD in the new DStream.
  56. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#updateStateByKey\[S\]\(updateFunc:Iterator\[\(K,Seq\[V\],Option\[S\]\)\]=>Iterator\[\(K,S\)\],partitioner:org.apache.spark.Partitioner,rememberPartitioner:Boolean,initialRDD:org.apache.spark.rdd.RDD\[\(K,S\)\]\)\(implicitevidence$9:scala.reflect.ClassTag\[S\]\):org.apache.spark.streaming.dstream.DStream\[\(K,S\)\] "Permalink") def updateStateByKey[S](updateFunc: (Iterator[(K, Seq[V], Option[S])]) => Iterator[(K, S)], partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner"), rememberPartitioner: Boolean, initialRDD: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, S)])(implicit arg0: ClassTag[S]): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, S)]
Return a new "state" DStream where the state for each key is updated by applying the given function on the previous state of the key and the new values of each key.
Return a new "state" DStream where the state for each key is updated by applying the given function on the previous state of the key and the new values of each key. In every batch the updateFunc will be called for each state even if there are no new values. org.apache.spark.Partitioner is used to control the partitioning of each RDD.

S

State type

updateFunc

State update function. Note, that this function may generate a different tuple with a different key than the input key. Therefore keys may be removed or added in this way. It is up to the developer to decide whether to remember the partitioner despite the key being changed.

partitioner

Partitioner for controlling the partitioning of each RDD in the new DStream

rememberPartitioner

Whether to remember the partitioner object in the generated RDDs.

initialRDD

initial state value of each key.
  57. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#updateStateByKey\[S\]\(updateFunc:\(Seq\[V\],Option\[S\]\)=>Option\[S\],partitioner:org.apache.spark.Partitioner,initialRDD:org.apache.spark.rdd.RDD\[\(K,S\)\]\)\(implicitevidence$8:scala.reflect.ClassTag\[S\]\):org.apache.spark.streaming.dstream.DStream\[\(K,S\)\] "Permalink") def updateStateByKey[S](updateFunc: (Seq[V], Option[S]) => Option[S], partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner"), initialRDD: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, S)])(implicit arg0: ClassTag[S]): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, S)]
Return a new "state" DStream where the state for each key is updated by applying the given function on the previous state of the key and the new values of the key.
Return a new "state" DStream where the state for each key is updated by applying the given function on the previous state of the key and the new values of the key. In every batch the updateFunc will be called for each state even if there are no new values. org.apache.spark.Partitioner is used to control the partitioning of each RDD.

S

State type

updateFunc

State update function. If `this` function returns None, then corresponding state key-value pair will be eliminated.

partitioner

Partitioner for controlling the partitioning of each RDD in the new DStream.

initialRDD

initial state value of each key.
  58. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#updateStateByKey\[S\]\(updateFunc:Iterator\[\(K,Seq\[V\],Option\[S\]\)\]=>Iterator\[\(K,S\)\],partitioner:org.apache.spark.Partitioner,rememberPartitioner:Boolean\)\(implicitevidence$7:scala.reflect.ClassTag\[S\]\):org.apache.spark.streaming.dstream.DStream\[\(K,S\)\] "Permalink") def updateStateByKey[S](updateFunc: (Iterator[(K, Seq[V], Option[S])]) => Iterator[(K, S)], partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner"), rememberPartitioner: Boolean)(implicit arg0: ClassTag[S]): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, S)]
Return a new "state" DStream where the state for each key is updated by applying the given function on the previous state of the key and the new values of each key.
Return a new "state" DStream where the state for each key is updated by applying the given function on the previous state of the key and the new values of each key. In every batch the updateFunc will be called for each state even if there are no new values. [org.apache.spark.Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner") is used to control the partitioning of each RDD.

S

State type

updateFunc

State update function. Note, that this function may generate a different tuple with a different key than the input key. Therefore keys may be removed or added in this way. It is up to the developer to decide whether to remember the partitioner despite the key being changed.

partitioner

Partitioner for controlling the partitioning of each RDD in the new DStream

rememberPartitioner

Whether to remember the partitioner object in the generated RDDs.
  59. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#updateStateByKey\[S\]\(updateFunc:\(Seq\[V\],Option\[S\]\)=>Option\[S\],partitioner:org.apache.spark.Partitioner\)\(implicitevidence$6:scala.reflect.ClassTag\[S\]\):org.apache.spark.streaming.dstream.DStream\[\(K,S\)\] "Permalink") def updateStateByKey[S](updateFunc: (Seq[V], Option[S]) => Option[S], partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner"))(implicit arg0: ClassTag[S]): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, S)]
Return a new "state" DStream where the state for each key is updated by applying the given function on the previous state of the key and the new values of the key.
Return a new "state" DStream where the state for each key is updated by applying the given function on the previous state of the key and the new values of the key. In every batch the updateFunc will be called for each state even if there are no new values. [org.apache.spark.Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner") is used to control the partitioning of each RDD.

S

State type

updateFunc

State update function. If `this` function returns None, then corresponding state key-value pair will be eliminated.

partitioner

Partitioner for controlling the partitioning of each RDD in the new DStream.
  60. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#updateStateByKey\[S\]\(updateFunc:\(Seq\[V\],Option\[S\]\)=>Option\[S\],numPartitions:Int\)\(implicitevidence$5:scala.reflect.ClassTag\[S\]\):org.apache.spark.streaming.dstream.DStream\[\(K,S\)\] "Permalink") def updateStateByKey[S](updateFunc: (Seq[V], Option[S]) => Option[S], numPartitions: Int)(implicit arg0: ClassTag[S]): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, S)]
Return a new "state" DStream where the state for each key is updated by applying the given function on the previous state of the key and the new values of each key.
Return a new "state" DStream where the state for each key is updated by applying the given function on the previous state of the key and the new values of each key. In every batch the updateFunc will be called for each state even if there are no new values. Hash partitioning is used to generate the RDDs with `numPartitions` partitions.

S

State type

updateFunc

State update function. If `this` function returns None, then corresponding state key-value pair will be eliminated.

numPartitions

Number of partitions of each RDD in the new DStream.
  61. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#updateStateByKey\[S\]\(updateFunc:\(Seq\[V\],Option\[S\]\)=>Option\[S\]\)\(implicitevidence$4:scala.reflect.ClassTag\[S\]\):org.apache.spark.streaming.dstream.DStream\[\(K,S\)\] "Permalink") def updateStateByKey[S](updateFunc: (Seq[V], Option[S]) => Option[S])(implicit arg0: ClassTag[S]): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, S)]
Return a new "state" DStream where the state for each key is updated by applying the given function on the previous state of the key and the new values of each key.
Return a new "state" DStream where the state for each key is updated by applying the given function on the previous state of the key and the new values of each key. In every batch the updateFunc will be called for each state even if there are no new values. Hash partitioning is used to generate the RDDs with Spark's default number of partitions.

S

State type

updateFunc

State update function. If `this` function returns None, then corresponding state key-value pair will be eliminated.
  62. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])
  63. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  64. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#wait\(\):Unit "Permalink") final  def wait(): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])

### Deprecated Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#finalize\(\):Unit "Permalink") def finalize(): Unit

Attributes
    protected[lang]

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.Throwable]) @Deprecated

Deprecated

_(Since version 9)_

### Inherited from AnyRef
### Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html###:Int "Permalink") final  def ##: Int

Definition Classes
    AnyRef → Any
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#clone\(\):Object "Permalink") def clone(): AnyRef

Attributes
    protected[lang]

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#equals\(x$1:Object\):Boolean "Permalink") def equals(arg0: AnyRef): Boolean

Definition Classes
    AnyRef → Any
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef]

Definition Classes
    AnyRef → Any

Annotations
     @IntrinsicCandidate() @native()
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#hashCode\(\):Int "Permalink") def hashCode(): Int

Definition Classes
    AnyRef → Any

Annotations
     @IntrinsicCandidate() @native()
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#notify\(\):Unit "Permalink") final  def notify(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0

Definition Classes
    AnyRef
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#toString\(\):String "Permalink") def toString(): [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String")

Definition Classes
    AnyRef → Any
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#wait\(\):Unit "Permalink") final  def wait(): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#finalize\(\):Unit "Permalink") def finalize(): Unit

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
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0

Definition Classes
    Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean

Definition Classes
    Any

### Ungrouped
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html###:Int "Permalink") final  def ##: Int

Definition Classes
    AnyRef → Any
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0

Definition Classes
    Any
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#clone\(\):Object "Permalink") def clone(): AnyRef

Attributes
    protected[lang]

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#cogroup\[W\]\(other:org.apache.spark.streaming.dstream.DStream\[\(K,W\)\],partitioner:org.apache.spark.Partitioner\)\(implicitevidence$15:scala.reflect.ClassTag\[W\]\):org.apache.spark.streaming.dstream.DStream\[\(K,\(Iterable\[V\],Iterable\[W\]\)\)\] "Permalink") def cogroup[W](other: [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, W)], partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner"))(implicit arg0: ClassTag[W]): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, (Iterable[V], Iterable[W]))]
Return a new DStream by applying 'cogroup' between RDDs of `this` DStream and `other` DStream.
Return a new DStream by applying 'cogroup' between RDDs of `this` DStream and `other` DStream. The supplied org.apache.spark.Partitioner is used to partition the generated RDDs.
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#cogroup\[W\]\(other:org.apache.spark.streaming.dstream.DStream\[\(K,W\)\],numPartitions:Int\)\(implicitevidence$14:scala.reflect.ClassTag\[W\]\):org.apache.spark.streaming.dstream.DStream\[\(K,\(Iterable\[V\],Iterable\[W\]\)\)\] "Permalink") def cogroup[W](other: [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, W)], numPartitions: Int)(implicit arg0: ClassTag[W]): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, (Iterable[V], Iterable[W]))]
Return a new DStream by applying 'cogroup' between RDDs of `this` DStream and `other` DStream.
Return a new DStream by applying 'cogroup' between RDDs of `this` DStream and `other` DStream. Hash partitioning is used to generate the RDDs with `numPartitions` partitions.
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#cogroup\[W\]\(other:org.apache.spark.streaming.dstream.DStream\[\(K,W\)\]\)\(implicitevidence$13:scala.reflect.ClassTag\[W\]\):org.apache.spark.streaming.dstream.DStream\[\(K,\(Iterable\[V\],Iterable\[W\]\)\)\] "Permalink") def cogroup[W](other: [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, W)])(implicit arg0: ClassTag[W]): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, (Iterable[V], Iterable[W]))]
Return a new DStream by applying 'cogroup' between RDDs of `this` DStream and `other` DStream.
Return a new DStream by applying 'cogroup' between RDDs of `this` DStream and `other` DStream. Hash partitioning is used to generate the RDDs with Spark's default number of partitions.
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#combineByKey\[C\]\(createCombiner:V=>C,mergeValue:\(C,V\)=>C,mergeCombiner:\(C,C\)=>C,partitioner:org.apache.spark.Partitioner,mapSideCombine:Boolean\)\(implicitevidence$1:scala.reflect.ClassTag\[C\]\):org.apache.spark.streaming.dstream.DStream\[\(K,C\)\] "Permalink") def combineByKey[C](createCombiner: (V) => C, mergeValue: (C, V) => C, mergeCombiner: (C, C) => C, partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner"), mapSideCombine: Boolean = true)(implicit arg0: ClassTag[C]): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, C)]
Combine elements of each key in DStream's RDDs using custom functions.
Combine elements of each key in DStream's RDDs using custom functions. This is similar to the combineByKey for RDDs. Please refer to combineByKey in org.apache.spark.rdd.PairRDDFunctions in the Spark core documentation for more information.
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#equals\(x$1:Object\):Boolean "Permalink") def equals(arg0: AnyRef): Boolean

Definition Classes
    AnyRef → Any
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#flatMapValues\[U\]\(flatMapValuesFunc:V=>IterableOnce\[U\]\)\(implicitevidence$12:scala.reflect.ClassTag\[U\]\):org.apache.spark.streaming.dstream.DStream\[\(K,U\)\] "Permalink") def flatMapValues[U](flatMapValuesFunc: (V) => IterableOnce[U])(implicit arg0: ClassTag[U]): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, U)]
Return a new DStream by applying a flatmap function to the value of each key-value pairs in 'this' DStream without changing the key.
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#fullOuterJoin\[W\]\(other:org.apache.spark.streaming.dstream.DStream\[\(K,W\)\],partitioner:org.apache.spark.Partitioner\)\(implicitevidence$27:scala.reflect.ClassTag\[W\]\):org.apache.spark.streaming.dstream.DStream\[\(K,\(Option\[V\],Option\[W\]\)\)\] "Permalink") def fullOuterJoin[W](other: [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, W)], partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner"))(implicit arg0: ClassTag[W]): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, (Option[V], Option[W]))]
Return a new DStream by applying 'full outer join' between RDDs of `this` DStream and `other` DStream.
Return a new DStream by applying 'full outer join' between RDDs of `this` DStream and `other` DStream. The supplied org.apache.spark.Partitioner is used to control the partitioning of each RDD.
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#fullOuterJoin\[W\]\(other:org.apache.spark.streaming.dstream.DStream\[\(K,W\)\],numPartitions:Int\)\(implicitevidence$26:scala.reflect.ClassTag\[W\]\):org.apache.spark.streaming.dstream.DStream\[\(K,\(Option\[V\],Option\[W\]\)\)\] "Permalink") def fullOuterJoin[W](other: [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, W)], numPartitions: Int)(implicit arg0: ClassTag[W]): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, (Option[V], Option[W]))]
Return a new DStream by applying 'full outer join' between RDDs of `this` DStream and `other` DStream.
Return a new DStream by applying 'full outer join' between RDDs of `this` DStream and `other` DStream. Hash partitioning is used to generate the RDDs with `numPartitions` partitions.
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#fullOuterJoin\[W\]\(other:org.apache.spark.streaming.dstream.DStream\[\(K,W\)\]\)\(implicitevidence$25:scala.reflect.ClassTag\[W\]\):org.apache.spark.streaming.dstream.DStream\[\(K,\(Option\[V\],Option\[W\]\)\)\] "Permalink") def fullOuterJoin[W](other: [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, W)])(implicit arg0: ClassTag[W]): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, (Option[V], Option[W]))]
Return a new DStream by applying 'full outer join' between RDDs of `this` DStream and `other` DStream.
Return a new DStream by applying 'full outer join' between RDDs of `this` DStream and `other` DStream. Hash partitioning is used to generate the RDDs with Spark's default number of partitions.
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef]

Definition Classes
    AnyRef → Any

Annotations
     @IntrinsicCandidate() @native()
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#groupByKey\(partitioner:org.apache.spark.Partitioner\):org.apache.spark.streaming.dstream.DStream\[\(K,Iterable\[V\]\)\] "Permalink") def groupByKey(partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner")): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, Iterable[V])]
Return a new DStream by applying `groupByKey` on each RDD.
Return a new DStream by applying `groupByKey` on each RDD. The supplied org.apache.spark.Partitioner is used to control the partitioning of each RDD.
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#groupByKey\(numPartitions:Int\):org.apache.spark.streaming.dstream.DStream\[\(K,Iterable\[V\]\)\] "Permalink") def groupByKey(numPartitions: Int): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, Iterable[V])]
Return a new DStream by applying `groupByKey` to each RDD.
Return a new DStream by applying `groupByKey` to each RDD. Hash partitioning is used to generate the RDDs with `numPartitions` partitions.
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#groupByKey\(\):org.apache.spark.streaming.dstream.DStream\[\(K,Iterable\[V\]\)\] "Permalink") def groupByKey(): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, Iterable[V])]
Return a new DStream by applying `groupByKey` to each RDD.
Return a new DStream by applying `groupByKey` to each RDD. Hash partitioning is used to generate the RDDs with Spark's default number of partitions.
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#groupByKeyAndWindow\(windowDuration:org.apache.spark.streaming.Duration,slideDuration:org.apache.spark.streaming.Duration,partitioner:org.apache.spark.Partitioner\):org.apache.spark.streaming.dstream.DStream\[\(K,Iterable\[V\]\)\] "Permalink") def groupByKeyAndWindow(windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner")): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, Iterable[V])]
Create a new DStream by applying `groupByKey` over a sliding window on `this` DStream.
Create a new DStream by applying `groupByKey` over a sliding window on `this` DStream. Similar to `DStream.groupByKey()`, but applies it over a sliding window.

windowDuration

width of the window; must be a multiple of this DStream's batching interval

slideDuration

sliding interval of the window (i.e., the interval after which the new DStream will generate RDDs); must be a multiple of this DStream's batching interval

partitioner

partitioner for controlling the partitioning of each RDD in the new DStream.
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#groupByKeyAndWindow\(windowDuration:org.apache.spark.streaming.Duration,slideDuration:org.apache.spark.streaming.Duration,numPartitions:Int\):org.apache.spark.streaming.dstream.DStream\[\(K,Iterable\[V\]\)\] "Permalink") def groupByKeyAndWindow(windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), numPartitions: Int): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, Iterable[V])]
Return a new DStream by applying `groupByKey` over a sliding window on `this` DStream.
Return a new DStream by applying `groupByKey` over a sliding window on `this` DStream. Similar to `DStream.groupByKey()`, but applies it over a sliding window. Hash partitioning is used to generate the RDDs with `numPartitions` partitions.

windowDuration

width of the window; must be a multiple of this DStream's batching interval

slideDuration

sliding interval of the window (i.e., the interval after which the new DStream will generate RDDs); must be a multiple of this DStream's batching interval

numPartitions

number of partitions of each RDD in the new DStream; if not specified then Spark's default number of partitions will be used
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#groupByKeyAndWindow\(windowDuration:org.apache.spark.streaming.Duration,slideDuration:org.apache.spark.streaming.Duration\):org.apache.spark.streaming.dstream.DStream\[\(K,Iterable\[V\]\)\] "Permalink") def groupByKeyAndWindow(windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration")): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, Iterable[V])]
Return a new DStream by applying `groupByKey` over a sliding window.
Return a new DStream by applying `groupByKey` over a sliding window. Similar to `DStream.groupByKey()`, but applies it over a sliding window. Hash partitioning is used to generate the RDDs with Spark's default number of partitions.

windowDuration

width of the window; must be a multiple of this DStream's batching interval

slideDuration

sliding interval of the window (i.e., the interval after which the new DStream will generate RDDs); must be a multiple of this DStream's batching interval
  23. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#groupByKeyAndWindow\(windowDuration:org.apache.spark.streaming.Duration\):org.apache.spark.streaming.dstream.DStream\[\(K,Iterable\[V\]\)\] "Permalink") def groupByKeyAndWindow(windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration")): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, Iterable[V])]
Return a new DStream by applying `groupByKey` over a sliding window.
Return a new DStream by applying `groupByKey` over a sliding window. This is similar to `DStream.groupByKey()` but applies it over a sliding window. The new DStream generates RDDs with the same interval as this DStream. Hash partitioning is used to generate the RDDs with Spark's default number of partitions.

windowDuration

width of the window; must be a multiple of this DStream's batching interval
  24. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#hashCode\(\):Int "Permalink") def hashCode(): Int

Definition Classes
    AnyRef → Any

Annotations
     @IntrinsicCandidate() @native()
  25. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean

Definition Classes
    Any
  26. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#join\[W\]\(other:org.apache.spark.streaming.dstream.DStream\[\(K,W\)\],partitioner:org.apache.spark.Partitioner\)\(implicitevidence$18:scala.reflect.ClassTag\[W\]\):org.apache.spark.streaming.dstream.DStream\[\(K,\(V,W\)\)\] "Permalink") def join[W](other: [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, W)], partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner"))(implicit arg0: ClassTag[W]): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, (V, W))]
Return a new DStream by applying 'join' between RDDs of `this` DStream and `other` DStream.
Return a new DStream by applying 'join' between RDDs of `this` DStream and `other` DStream. The supplied org.apache.spark.Partitioner is used to control the partitioning of each RDD.
  27. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#join\[W\]\(other:org.apache.spark.streaming.dstream.DStream\[\(K,W\)\],numPartitions:Int\)\(implicitevidence$17:scala.reflect.ClassTag\[W\]\):org.apache.spark.streaming.dstream.DStream\[\(K,\(V,W\)\)\] "Permalink") def join[W](other: [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, W)], numPartitions: Int)(implicit arg0: ClassTag[W]): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, (V, W))]
Return a new DStream by applying 'join' between RDDs of `this` DStream and `other` DStream.
Return a new DStream by applying 'join' between RDDs of `this` DStream and `other` DStream. Hash partitioning is used to generate the RDDs with `numPartitions` partitions.
  28. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#join\[W\]\(other:org.apache.spark.streaming.dstream.DStream\[\(K,W\)\]\)\(implicitevidence$16:scala.reflect.ClassTag\[W\]\):org.apache.spark.streaming.dstream.DStream\[\(K,\(V,W\)\)\] "Permalink") def join[W](other: [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, W)])(implicit arg0: ClassTag[W]): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, (V, W))]
Return a new DStream by applying 'join' between RDDs of `this` DStream and `other` DStream.
Return a new DStream by applying 'join' between RDDs of `this` DStream and `other` DStream. Hash partitioning is used to generate the RDDs with Spark's default number of partitions.
  29. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#leftOuterJoin\[W\]\(other:org.apache.spark.streaming.dstream.DStream\[\(K,W\)\],partitioner:org.apache.spark.Partitioner\)\(implicitevidence$21:scala.reflect.ClassTag\[W\]\):org.apache.spark.streaming.dstream.DStream\[\(K,\(V,Option\[W\]\)\)\] "Permalink") def leftOuterJoin[W](other: [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, W)], partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner"))(implicit arg0: ClassTag[W]): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, (V, Option[W]))]
Return a new DStream by applying 'left outer join' between RDDs of `this` DStream and `other` DStream.
Return a new DStream by applying 'left outer join' between RDDs of `this` DStream and `other` DStream. The supplied org.apache.spark.Partitioner is used to control the partitioning of each RDD.
  30. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#leftOuterJoin\[W\]\(other:org.apache.spark.streaming.dstream.DStream\[\(K,W\)\],numPartitions:Int\)\(implicitevidence$20:scala.reflect.ClassTag\[W\]\):org.apache.spark.streaming.dstream.DStream\[\(K,\(V,Option\[W\]\)\)\] "Permalink") def leftOuterJoin[W](other: [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, W)], numPartitions: Int)(implicit arg0: ClassTag[W]): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, (V, Option[W]))]
Return a new DStream by applying 'left outer join' between RDDs of `this` DStream and `other` DStream.
Return a new DStream by applying 'left outer join' between RDDs of `this` DStream and `other` DStream. Hash partitioning is used to generate the RDDs with `numPartitions` partitions.
  31. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#leftOuterJoin\[W\]\(other:org.apache.spark.streaming.dstream.DStream\[\(K,W\)\]\)\(implicitevidence$19:scala.reflect.ClassTag\[W\]\):org.apache.spark.streaming.dstream.DStream\[\(K,\(V,Option\[W\]\)\)\] "Permalink") def leftOuterJoin[W](other: [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, W)])(implicit arg0: ClassTag[W]): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, (V, Option[W]))]
Return a new DStream by applying 'left outer join' between RDDs of `this` DStream and `other` DStream.
Return a new DStream by applying 'left outer join' between RDDs of `this` DStream and `other` DStream. Hash partitioning is used to generate the RDDs with Spark's default number of partitions.
  32. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#mapValues\[U\]\(mapValuesFunc:V=>U\)\(implicitevidence$11:scala.reflect.ClassTag\[U\]\):org.apache.spark.streaming.dstream.DStream\[\(K,U\)\] "Permalink") def mapValues[U](mapValuesFunc: (V) => U)(implicit arg0: ClassTag[U]): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, U)]
Return a new DStream by applying a map function to the value of each key-value pairs in 'this' DStream without changing the key.
  33. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#mapWithState\[StateType,MappedType\]\(spec:org.apache.spark.streaming.StateSpec\[K,V,StateType,MappedType\]\)\(implicitevidence$2:scala.reflect.ClassTag\[StateType\],implicitevidence$3:scala.reflect.ClassTag\[MappedType\]\):org.apache.spark.streaming.dstream.MapWithStateDStream\[K,V,StateType,MappedType\] "Permalink") def mapWithState[StateType, MappedType](spec: [StateSpec](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StateSpec.html "org.apache.spark.streaming.StateSpec")[K, V, StateType, MappedType])(implicit arg0: ClassTag[StateType], arg1: ClassTag[MappedType]): [MapWithStateDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/MapWithStateDStream.html "org.apache.spark.streaming.dstream.MapWithStateDStream")[K, V, StateType, MappedType]
Return a [MapWithStateDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/MapWithStateDStream.html "org.apache.spark.streaming.dstream.MapWithStateDStream") by applying a function to every key-value element of `this` stream, while maintaining some state data for each unique key.
Return a [MapWithStateDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/MapWithStateDStream.html "org.apache.spark.streaming.dstream.MapWithStateDStream") by applying a function to every key-value element of `this` stream, while maintaining some state data for each unique key. The mapping function and other specification (e.g. partitioners, timeouts, initial state data, etc.) of this transformation can be specified using `StateSpec` class. The state data is accessible in as a parameter of type `State` in the mapping function.
Example of using `mapWithState`:

```
// A mapping function that maintains an integer state and return a String
def mappingFunction(key: String, value: Option[Int], state: State[Int]): Option[String] = {
  // Use state.exists(), state.get(), state.update() and state.remove()
  // to manage state, and return the necessary string
}

val spec = StateSpec.function(mappingFunction).numPartitions(10)

val mapWithStateDStream = keyValueDStream.mapWithState[StateType, MappedType](spec)
```

StateType

Class type of the state data

MappedType

Class type of the mapped data

spec

Specification of this transformation
  34. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  35. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#notify\(\):Unit "Permalink") final  def notify(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  36. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  37. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#reduceByKey\(reduceFunc:\(V,V\)=>V,partitioner:org.apache.spark.Partitioner\):org.apache.spark.streaming.dstream.DStream\[\(K,V\)\] "Permalink") def reduceByKey(reduceFunc: (V, V) => V, partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner")): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, V)]
Return a new DStream by applying `reduceByKey` to each RDD.
Return a new DStream by applying `reduceByKey` to each RDD. The values for each key are merged using the supplied reduce function. org.apache.spark.Partitioner is used to control the partitioning of each RDD.
  38. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#reduceByKey\(reduceFunc:\(V,V\)=>V,numPartitions:Int\):org.apache.spark.streaming.dstream.DStream\[\(K,V\)\] "Permalink") def reduceByKey(reduceFunc: (V, V) => V, numPartitions: Int): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, V)]
Return a new DStream by applying `reduceByKey` to each RDD.
Return a new DStream by applying `reduceByKey` to each RDD. The values for each key are merged using the supplied reduce function. Hash partitioning is used to generate the RDDs with `numPartitions` partitions.
  39. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#reduceByKey\(reduceFunc:\(V,V\)=>V\):org.apache.spark.streaming.dstream.DStream\[\(K,V\)\] "Permalink") def reduceByKey(reduceFunc: (V, V) => V): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, V)]
Return a new DStream by applying `reduceByKey` to each RDD.
Return a new DStream by applying `reduceByKey` to each RDD. The values for each key are merged using the associative and commutative reduce function. Hash partitioning is used to generate the RDDs with Spark's default number of partitions.
  40. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#reduceByKeyAndWindow\(reduceFunc:\(V,V\)=>V,invReduceFunc:\(V,V\)=>V,windowDuration:org.apache.spark.streaming.Duration,slideDuration:org.apache.spark.streaming.Duration,partitioner:org.apache.spark.Partitioner,filterFunc:\(\(K,V\)\)=>Boolean\):org.apache.spark.streaming.dstream.DStream\[\(K,V\)\] "Permalink") def reduceByKeyAndWindow(reduceFunc: (V, V) => V, invReduceFunc: (V, V) => V, windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner"), filterFunc: ((K, V)) => Boolean): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, V)]
Return a new DStream by applying incremental `reduceByKey` over a sliding window.
Return a new DStream by applying incremental `reduceByKey` over a sliding window. The reduced value of over a new window is calculated using the old window's reduced value :
    1. reduce the new values that entered the window (e.g., adding new counts) 2. "inverse reduce" the old values that left the window (e.g., subtracting old counts) This is more efficient than reduceByKeyAndWindow without "inverse reduce" function. However, it is applicable to only "invertible reduce functions".

reduceFunc

associative and commutative reduce function

invReduceFunc

inverse reduce function

windowDuration

width of the window; must be a multiple of this DStream's batching interval

slideDuration

sliding interval of the window (i.e., the interval after which the new DStream will generate RDDs); must be a multiple of this DStream's batching interval

partitioner

partitioner for controlling the partitioning of each RDD in the new DStream.

filterFunc

Optional function to filter expired key-value pairs; only pairs that satisfy the function are retained
  41. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#reduceByKeyAndWindow\(reduceFunc:\(V,V\)=>V,invReduceFunc:\(V,V\)=>V,windowDuration:org.apache.spark.streaming.Duration,slideDuration:org.apache.spark.streaming.Duration,numPartitions:Int,filterFunc:\(\(K,V\)\)=>Boolean\):org.apache.spark.streaming.dstream.DStream\[\(K,V\)\] "Permalink") def reduceByKeyAndWindow(reduceFunc: (V, V) => V, invReduceFunc: (V, V) => V, windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration") = [self.slideDuration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#slideDuration:org.apache.spark.streaming.Duration), numPartitions: Int = [ssc.sc.defaultParallelism](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#defaultParallelism:Int), filterFunc: ((K, V)) => Boolean = null): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, V)]
Return a new DStream by applying incremental `reduceByKey` over a sliding window.
Return a new DStream by applying incremental `reduceByKey` over a sliding window. The reduced value of over a new window is calculated using the old window's reduced value :
    1. reduce the new values that entered the window (e.g., adding new counts)
2. "inverse reduce" the old values that left the window (e.g., subtracting old counts)
This is more efficient than reduceByKeyAndWindow without "inverse reduce" function. However, it is applicable to only "invertible reduce functions". Hash partitioning is used to generate the RDDs with Spark's default number of partitions.

reduceFunc

associative and commutative reduce function

invReduceFunc

inverse reduce function; such that for all y, invertible x: `invReduceFunc(reduceFunc(x, y), x) = y`

windowDuration

width of the window; must be a multiple of this DStream's batching interval

slideDuration

sliding interval of the window (i.e., the interval after which the new DStream will generate RDDs); must be a multiple of this DStream's batching interval

filterFunc

Optional function to filter expired key-value pairs; only pairs that satisfy the function are retained
  42. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#reduceByKeyAndWindow\(reduceFunc:\(V,V\)=>V,windowDuration:org.apache.spark.streaming.Duration,slideDuration:org.apache.spark.streaming.Duration,partitioner:org.apache.spark.Partitioner\):org.apache.spark.streaming.dstream.DStream\[\(K,V\)\] "Permalink") def reduceByKeyAndWindow(reduceFunc: (V, V) => V, windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner")): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, V)]
Return a new DStream by applying `reduceByKey` over a sliding window.
Return a new DStream by applying `reduceByKey` over a sliding window. Similar to `DStream.reduceByKey()`, but applies it over a sliding window.

reduceFunc

associative and commutative reduce function

windowDuration

width of the window; must be a multiple of this DStream's batching interval

slideDuration

sliding interval of the window (i.e., the interval after which the new DStream will generate RDDs); must be a multiple of this DStream's batching interval

partitioner

partitioner for controlling the partitioning of each RDD in the new DStream.
  43. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#reduceByKeyAndWindow\(reduceFunc:\(V,V\)=>V,windowDuration:org.apache.spark.streaming.Duration,slideDuration:org.apache.spark.streaming.Duration,numPartitions:Int\):org.apache.spark.streaming.dstream.DStream\[\(K,V\)\] "Permalink") def reduceByKeyAndWindow(reduceFunc: (V, V) => V, windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), numPartitions: Int): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, V)]
Return a new DStream by applying `reduceByKey` over a sliding window.
Return a new DStream by applying `reduceByKey` over a sliding window. This is similar to `DStream.reduceByKey()` but applies it over a sliding window. Hash partitioning is used to generate the RDDs with `numPartitions` partitions.

reduceFunc

associative and commutative reduce function

windowDuration

width of the window; must be a multiple of this DStream's batching interval

slideDuration

sliding interval of the window (i.e., the interval after which the new DStream will generate RDDs); must be a multiple of this DStream's batching interval

numPartitions

number of partitions of each RDD in the new DStream.
  44. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#reduceByKeyAndWindow\(reduceFunc:\(V,V\)=>V,windowDuration:org.apache.spark.streaming.Duration,slideDuration:org.apache.spark.streaming.Duration\):org.apache.spark.streaming.dstream.DStream\[\(K,V\)\] "Permalink") def reduceByKeyAndWindow(reduceFunc: (V, V) => V, windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration")): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, V)]
Return a new DStream by applying `reduceByKey` over a sliding window.
Return a new DStream by applying `reduceByKey` over a sliding window. This is similar to `DStream.reduceByKey()` but applies it over a sliding window. Hash partitioning is used to generate the RDDs with Spark's default number of partitions.

reduceFunc

associative and commutative reduce function

windowDuration

width of the window; must be a multiple of this DStream's batching interval

slideDuration

sliding interval of the window (i.e., the interval after which the new DStream will generate RDDs); must be a multiple of this DStream's batching interval
  45. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#reduceByKeyAndWindow\(reduceFunc:\(V,V\)=>V,windowDuration:org.apache.spark.streaming.Duration\):org.apache.spark.streaming.dstream.DStream\[\(K,V\)\] "Permalink") def reduceByKeyAndWindow(reduceFunc: (V, V) => V, windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration")): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, V)]
Return a new DStream by applying `reduceByKey` over a sliding window on `this` DStream.
Return a new DStream by applying `reduceByKey` over a sliding window on `this` DStream. Similar to `DStream.reduceByKey()`, but applies it over a sliding window. The new DStream generates RDDs with the same interval as this DStream. Hash partitioning is used to generate the RDDs with Spark's default number of partitions.

reduceFunc

associative and commutative reduce function

windowDuration

width of the window; must be a multiple of this DStream's batching interval
  46. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#rightOuterJoin\[W\]\(other:org.apache.spark.streaming.dstream.DStream\[\(K,W\)\],partitioner:org.apache.spark.Partitioner\)\(implicitevidence$24:scala.reflect.ClassTag\[W\]\):org.apache.spark.streaming.dstream.DStream\[\(K,\(Option\[V\],W\)\)\] "Permalink") def rightOuterJoin[W](other: [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, W)], partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner"))(implicit arg0: ClassTag[W]): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, (Option[V], W))]
Return a new DStream by applying 'right outer join' between RDDs of `this` DStream and `other` DStream.
Return a new DStream by applying 'right outer join' between RDDs of `this` DStream and `other` DStream. The supplied org.apache.spark.Partitioner is used to control the partitioning of each RDD.
  47. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#rightOuterJoin\[W\]\(other:org.apache.spark.streaming.dstream.DStream\[\(K,W\)\],numPartitions:Int\)\(implicitevidence$23:scala.reflect.ClassTag\[W\]\):org.apache.spark.streaming.dstream.DStream\[\(K,\(Option\[V\],W\)\)\] "Permalink") def rightOuterJoin[W](other: [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, W)], numPartitions: Int)(implicit arg0: ClassTag[W]): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, (Option[V], W))]
Return a new DStream by applying 'right outer join' between RDDs of `this` DStream and `other` DStream.
Return a new DStream by applying 'right outer join' between RDDs of `this` DStream and `other` DStream. Hash partitioning is used to generate the RDDs with `numPartitions` partitions.
  48. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#rightOuterJoin\[W\]\(other:org.apache.spark.streaming.dstream.DStream\[\(K,W\)\]\)\(implicitevidence$22:scala.reflect.ClassTag\[W\]\):org.apache.spark.streaming.dstream.DStream\[\(K,\(Option\[V\],W\)\)\] "Permalink") def rightOuterJoin[W](other: [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, W)])(implicit arg0: ClassTag[W]): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, (Option[V], W))]
Return a new DStream by applying 'right outer join' between RDDs of `this` DStream and `other` DStream.
Return a new DStream by applying 'right outer join' between RDDs of `this` DStream and `other` DStream. Hash partitioning is used to generate the RDDs with Spark's default number of partitions.
  49. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#saveAsHadoopFiles\(prefix:String,suffix:String,keyClass:Class\[_\],valueClass:Class\[_\],outputFormatClass:Class\[_<:org.apache.hadoop.mapred.OutputFormat\[_,_\]\],conf:org.apache.hadoop.mapred.JobConf\):Unit "Permalink") def saveAsHadoopFiles(prefix: String, suffix: String, keyClass: Class[_], valueClass: Class[_], outputFormatClass: Class[_ <: OutputFormat[_, _]], conf: JobConf = [new JobConf(ssc.sparkContext.hadoopConfiguration)](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#sparkContext:org.apache.spark.SparkContext)): Unit
Save each RDD in `this` DStream as a Hadoop file.
Save each RDD in `this` DStream as a Hadoop file. The file name at each batch interval is generated based on `prefix` and `suffix`: "prefix-TIME_IN_MS.suffix"
  50. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#saveAsHadoopFiles\[F<:org.apache.hadoop.mapred.OutputFormat\[K,V\]\]\(prefix:String,suffix:String\)\(implicitfm:scala.reflect.ClassTag\[F\]\):Unit "Permalink") def saveAsHadoopFiles[F <: OutputFormat[K, V]](prefix: String, suffix: String)(implicit fm: ClassTag[F]): Unit
Save each RDD in `this` DStream as a Hadoop file.
Save each RDD in `this` DStream as a Hadoop file. The file name at each batch interval is generated based on `prefix` and `suffix`: "prefix-TIME_IN_MS.suffix"
  51. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#saveAsNewAPIHadoopFiles\(prefix:String,suffix:String,keyClass:Class\[_\],valueClass:Class\[_\],outputFormatClass:Class\[_<:org.apache.hadoop.mapreduce.OutputFormat\[_,_\]\],conf:org.apache.hadoop.conf.Configuration\):Unit "Permalink") def saveAsNewAPIHadoopFiles(prefix: String, suffix: String, keyClass: Class[_], valueClass: Class[_], outputFormatClass: Class[_ <: OutputFormat[_, _]], conf: Configuration = [ssc.sparkContext.hadoopConfiguration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#sparkContext:org.apache.spark.SparkContext)): Unit
Save each RDD in `this` DStream as a Hadoop file.
Save each RDD in `this` DStream as a Hadoop file. The file name at each batch interval is generated based on `prefix` and `suffix`: "prefix-TIME_IN_MS.suffix".
  52. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#saveAsNewAPIHadoopFiles\[F<:org.apache.hadoop.mapreduce.OutputFormat\[K,V\]\]\(prefix:String,suffix:String\)\(implicitfm:scala.reflect.ClassTag\[F\]\):Unit "Permalink") def saveAsNewAPIHadoopFiles[F <: OutputFormat[K, V]](prefix: String, suffix: String)(implicit fm: ClassTag[F]): Unit
Save each RDD in `this` DStream as a Hadoop file.
Save each RDD in `this` DStream as a Hadoop file. The file name at each batch interval is generated based on `prefix` and `suffix`: "prefix-TIME_IN_MS.suffix".
  53. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0

Definition Classes
    AnyRef
  54. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#toString\(\):String "Permalink") def toString(): [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String")

Definition Classes
    AnyRef → Any
  55. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#updateStateByKey\[S\]\(updateFunc:\(org.apache.spark.streaming.Time,K,Seq\[V\],Option\[S\]\)=>Option\[S\],partitioner:org.apache.spark.Partitioner,rememberPartitioner:Boolean,initialRDD:Option\[org.apache.spark.rdd.RDD\[\(K,S\)\]\]\)\(implicitevidence$10:scala.reflect.ClassTag\[S\]\):org.apache.spark.streaming.dstream.DStream\[\(K,S\)\] "Permalink") def updateStateByKey[S](updateFunc: ([Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time"), K, Seq[V], Option[S]) => Option[S], partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner"), rememberPartitioner: Boolean, initialRDD: Option[[RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, S)]] = None)(implicit arg0: ClassTag[S]): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, S)]
Return a new "state" DStream where the state for each key is updated by applying the given function on the previous state of the key and the new values of the key.
Return a new "state" DStream where the state for each key is updated by applying the given function on the previous state of the key and the new values of the key. In every batch the updateFunc will be called for each state even if there are no new values. org.apache.spark.Partitioner is used to control the partitioning of each RDD.

S

State type

updateFunc

State update function. If `this` function returns None, then corresponding state key-value pair will be eliminated.

partitioner

Partitioner for controlling the partitioning of each RDD in the new DStream.
  56. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#updateStateByKey\[S\]\(updateFunc:Iterator\[\(K,Seq\[V\],Option\[S\]\)\]=>Iterator\[\(K,S\)\],partitioner:org.apache.spark.Partitioner,rememberPartitioner:Boolean,initialRDD:org.apache.spark.rdd.RDD\[\(K,S\)\]\)\(implicitevidence$9:scala.reflect.ClassTag\[S\]\):org.apache.spark.streaming.dstream.DStream\[\(K,S\)\] "Permalink") def updateStateByKey[S](updateFunc: (Iterator[(K, Seq[V], Option[S])]) => Iterator[(K, S)], partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner"), rememberPartitioner: Boolean, initialRDD: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, S)])(implicit arg0: ClassTag[S]): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, S)]
Return a new "state" DStream where the state for each key is updated by applying the given function on the previous state of the key and the new values of each key.
Return a new "state" DStream where the state for each key is updated by applying the given function on the previous state of the key and the new values of each key. In every batch the updateFunc will be called for each state even if there are no new values. org.apache.spark.Partitioner is used to control the partitioning of each RDD.

S

State type

updateFunc

State update function. Note, that this function may generate a different tuple with a different key than the input key. Therefore keys may be removed or added in this way. It is up to the developer to decide whether to remember the partitioner despite the key being changed.

partitioner

Partitioner for controlling the partitioning of each RDD in the new DStream

rememberPartitioner

Whether to remember the partitioner object in the generated RDDs.

initialRDD

initial state value of each key.
  57. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#updateStateByKey\[S\]\(updateFunc:\(Seq\[V\],Option\[S\]\)=>Option\[S\],partitioner:org.apache.spark.Partitioner,initialRDD:org.apache.spark.rdd.RDD\[\(K,S\)\]\)\(implicitevidence$8:scala.reflect.ClassTag\[S\]\):org.apache.spark.streaming.dstream.DStream\[\(K,S\)\] "Permalink") def updateStateByKey[S](updateFunc: (Seq[V], Option[S]) => Option[S], partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner"), initialRDD: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, S)])(implicit arg0: ClassTag[S]): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, S)]
Return a new "state" DStream where the state for each key is updated by applying the given function on the previous state of the key and the new values of the key.
Return a new "state" DStream where the state for each key is updated by applying the given function on the previous state of the key and the new values of the key. In every batch the updateFunc will be called for each state even if there are no new values. org.apache.spark.Partitioner is used to control the partitioning of each RDD.

S

State type

updateFunc

State update function. If `this` function returns None, then corresponding state key-value pair will be eliminated.

partitioner

Partitioner for controlling the partitioning of each RDD in the new DStream.

initialRDD

initial state value of each key.
  58. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#updateStateByKey\[S\]\(updateFunc:Iterator\[\(K,Seq\[V\],Option\[S\]\)\]=>Iterator\[\(K,S\)\],partitioner:org.apache.spark.Partitioner,rememberPartitioner:Boolean\)\(implicitevidence$7:scala.reflect.ClassTag\[S\]\):org.apache.spark.streaming.dstream.DStream\[\(K,S\)\] "Permalink") def updateStateByKey[S](updateFunc: (Iterator[(K, Seq[V], Option[S])]) => Iterator[(K, S)], partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner"), rememberPartitioner: Boolean)(implicit arg0: ClassTag[S]): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, S)]
Return a new "state" DStream where the state for each key is updated by applying the given function on the previous state of the key and the new values of each key.
Return a new "state" DStream where the state for each key is updated by applying the given function on the previous state of the key and the new values of each key. In every batch the updateFunc will be called for each state even if there are no new values. [org.apache.spark.Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner") is used to control the partitioning of each RDD.

S

State type

updateFunc

State update function. Note, that this function may generate a different tuple with a different key than the input key. Therefore keys may be removed or added in this way. It is up to the developer to decide whether to remember the partitioner despite the key being changed.

partitioner

Partitioner for controlling the partitioning of each RDD in the new DStream

rememberPartitioner

Whether to remember the partitioner object in the generated RDDs.
  59. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#updateStateByKey\[S\]\(updateFunc:\(Seq\[V\],Option\[S\]\)=>Option\[S\],partitioner:org.apache.spark.Partitioner\)\(implicitevidence$6:scala.reflect.ClassTag\[S\]\):org.apache.spark.streaming.dstream.DStream\[\(K,S\)\] "Permalink") def updateStateByKey[S](updateFunc: (Seq[V], Option[S]) => Option[S], partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner"))(implicit arg0: ClassTag[S]): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, S)]
Return a new "state" DStream where the state for each key is updated by applying the given function on the previous state of the key and the new values of the key.
Return a new "state" DStream where the state for each key is updated by applying the given function on the previous state of the key and the new values of the key. In every batch the updateFunc will be called for each state even if there are no new values. [org.apache.spark.Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner") is used to control the partitioning of each RDD.

S

State type

updateFunc

State update function. If `this` function returns None, then corresponding state key-value pair will be eliminated.

partitioner

Partitioner for controlling the partitioning of each RDD in the new DStream.
  60. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#updateStateByKey\[S\]\(updateFunc:\(Seq\[V\],Option\[S\]\)=>Option\[S\],numPartitions:Int\)\(implicitevidence$5:scala.reflect.ClassTag\[S\]\):org.apache.spark.streaming.dstream.DStream\[\(K,S\)\] "Permalink") def updateStateByKey[S](updateFunc: (Seq[V], Option[S]) => Option[S], numPartitions: Int)(implicit arg0: ClassTag[S]): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, S)]
Return a new "state" DStream where the state for each key is updated by applying the given function on the previous state of the key and the new values of each key.
Return a new "state" DStream where the state for each key is updated by applying the given function on the previous state of the key and the new values of each key. In every batch the updateFunc will be called for each state even if there are no new values. Hash partitioning is used to generate the RDDs with `numPartitions` partitions.

S

State type

updateFunc

State update function. If `this` function returns None, then corresponding state key-value pair will be eliminated.

numPartitions

Number of partitions of each RDD in the new DStream.
  61. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#updateStateByKey\[S\]\(updateFunc:\(Seq\[V\],Option\[S\]\)=>Option\[S\]\)\(implicitevidence$4:scala.reflect.ClassTag\[S\]\):org.apache.spark.streaming.dstream.DStream\[\(K,S\)\] "Permalink") def updateStateByKey[S](updateFunc: (Seq[V], Option[S]) => Option[S])(implicit arg0: ClassTag[S]): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(K, S)]
Return a new "state" DStream where the state for each key is updated by applying the given function on the previous state of the key and the new values of each key.
Return a new "state" DStream where the state for each key is updated by applying the given function on the previous state of the key and the new values of each key. In every batch the updateFunc will be called for each state even if there are no new values. Hash partitioning is used to generate the RDDs with Spark's default number of partitions.

S

State type

updateFunc

State update function. If `this` function returns None, then corresponding state key-value pair will be eliminated.
  62. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])
  63. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  64. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#wait\(\):Unit "Permalink") final  def wait(): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])
  65. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html#finalize\(\):Unit "Permalink") def finalize(): Unit

Attributes
    protected[lang]

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.Throwable]) @Deprecated

Deprecated

_(Since version 9)_
