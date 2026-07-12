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


[c](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream$.html "See companion object")
[org](https://spark.apache.org/docs/latest/api/scala/org/index.html "org").[apache](https://spark.apache.org/docs/latest/api/scala/org/apache/index.html "org.apache").[spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark").[streaming](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/index.html "org.apache.spark.streaming").[api](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/index.html "org.apache.spark.streaming.api").[java](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/index.html "org.apache.spark.streaming.api.java")
#  [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream$.html "See companion object")[ __](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "Permalink")
### 
Companion [object JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream$.html "See companion object")
####  class JavaDStream[T] extends AbstractJavaDStreamLike[T, [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[T], [JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[T]]
A Java-friendly interface to [org.apache.spark.streaming.dstream.DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream"), the basic abstraction in Spark Streaming that represents a continuous stream of data. DStreams can either be created from live data (such as, data from TCP sockets, Kafka, etc.) or it can be generated by transforming existing DStreams using operations such as `map`, `window`. For operations applicable to key-value pair DStreams, see [org.apache.spark.streaming.api.java.JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream").  

Source
    [JavaDStream.scala](https://github.com/apache/spark/tree/v4.1.2/streaming/src/main/scala/org/apache/spark/streaming/api/java/JavaDStream.scala)
Linear Supertypes
AbstractJavaDStreamLike[T, [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[T], [JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[T]], [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")[T, [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[T], [JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[T]], [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable"), AnyRef, Any
Known Subclasses
[JavaInputDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaInputDStream.html "org.apache.spark.streaming.api.java.JavaInputDStream"), [JavaMapWithStateDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaMapWithStateDStream.html "org.apache.spark.streaming.api.java.JavaMapWithStateDStream"), [JavaReceiverInputDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaReceiverInputDStream.html "org.apache.spark.streaming.api.java.JavaReceiverInputDStream")
__ __
Ordering
  1. Alphabetic
  2. By Inheritance


Inherited  

  1. JavaDStream
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
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#<init>\(dstream:org.apache.spark.streaming.dstream.DStream\[T\]\)\(implicitclassTag:scala.reflect.ClassTag\[T\]\):org.apache.spark.streaming.api.java.JavaDStream\[T\] "Permalink") new JavaDStream(dstream: [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[T])(implicit classTag: ClassTag[T])


### Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html###:Int "Permalink") final  def ##: Int 

Definition Classes
    AnyRef → Any
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0 

Definition Classes
    Any
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#cache\(\):org.apache.spark.streaming.api.java.JavaDStream\[T\] "Permalink") def cache(): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[T]
Persist RDDs of this DStream with the default storage level (MEMORY_ONLY_SER)
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#checkpoint\(interval:org.apache.spark.streaming.Duration\):org.apache.spark.streaming.dstream.DStream\[T\] "Permalink") def checkpoint(interval: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration")): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[T]
Enable periodic checkpointing of RDDs of this DStream.
Enable periodic checkpointing of RDDs of this DStream. 

interval
    
Time interval after which generated RDD will be checkpointed 

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#classTag:scala.reflect.ClassTag\[T\] "Permalink") implicit  val classTag: ClassTag[T] 

Definition Classes
     [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream") → [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#clone\(\):Object "Permalink") def clone(): AnyRef 

Attributes
    protected[lang]  

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#compute\(validTime:org.apache.spark.streaming.Time\):org.apache.spark.api.java.JavaRDD\[T\] "Permalink") def compute(validTime: [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time")): [JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[T]
Generate an RDD for the given duration
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#context\(\):org.apache.spark.streaming.StreamingContext "Permalink") def context(): [StreamingContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html "org.apache.spark.streaming.StreamingContext")
Return the [org.apache.spark.streaming.StreamingContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html "org.apache.spark.streaming.StreamingContext") associated with this DStream
Return the [org.apache.spark.streaming.StreamingContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html "org.apache.spark.streaming.StreamingContext") associated with this DStream 

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#count\(\):org.apache.spark.streaming.api.java.JavaDStream\[Long\] "Permalink") def count(): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[[Long](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html#java.lang.Long "java.lang.Long")]
Return a new DStream in which each RDD has a single element generated by counting each RDD of this DStream.
Return a new DStream in which each RDD has a single element generated by counting each RDD of this DStream.  

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#countByValue\(numPartitions:Int\):org.apache.spark.streaming.api.java.JavaPairDStream\[T,Long\] "Permalink") def countByValue(numPartitions: Int): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[T, [Long](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html#java.lang.Long "java.lang.Long")]
Return a new DStream in which each RDD contains the counts of each distinct value in each RDD of this DStream.
Return a new DStream in which each RDD contains the counts of each distinct value in each RDD of this DStream. Hash partitioning is used to generate the RDDs with `numPartitions` partitions. 

numPartitions
    
number of partitions of each RDD in the new DStream. 

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#countByValue\(\):org.apache.spark.streaming.api.java.JavaPairDStream\[T,Long\] "Permalink") def countByValue(): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[T, [Long](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html#java.lang.Long "java.lang.Long")]
Return a new DStream in which each RDD contains the counts of each distinct value in each RDD of this DStream.
Return a new DStream in which each RDD contains the counts of each distinct value in each RDD of this DStream. Hash partitioning is used to generate the RDDs with Spark's default number of partitions.  

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#countByValueAndWindow\(windowDuration:org.apache.spark.streaming.Duration,slideDuration:org.apache.spark.streaming.Duration,numPartitions:Int\):org.apache.spark.streaming.api.java.JavaPairDStream\[T,Long\] "Permalink") def countByValueAndWindow(windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), numPartitions: Int): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[T, [Long](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html#java.lang.Long "java.lang.Long")]
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
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#countByValueAndWindow\(windowDuration:org.apache.spark.streaming.Duration,slideDuration:org.apache.spark.streaming.Duration\):org.apache.spark.streaming.api.java.JavaPairDStream\[T,Long\] "Permalink") def countByValueAndWindow(windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration")): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[T, [Long](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html#java.lang.Long "java.lang.Long")]
Return a new DStream in which each RDD contains the count of distinct elements in RDDs in a sliding window over this DStream.
Return a new DStream in which each RDD contains the count of distinct elements in RDDs in a sliding window over this DStream. Hash partitioning is used to generate the RDDs with Spark's default number of partitions. 

windowDuration
    
width of the window; must be a multiple of this DStream's batching interval 

slideDuration
    
sliding interval of the window (i.e., the interval after which the new DStream will generate RDDs); must be a multiple of this DStream's batching interval 

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#countByWindow\(windowDuration:org.apache.spark.streaming.Duration,slideDuration:org.apache.spark.streaming.Duration\):org.apache.spark.streaming.api.java.JavaDStream\[Long\] "Permalink") def countByWindow(windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration")): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[[Long](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html#java.lang.Long "java.lang.Long")]
Return a new DStream in which each RDD has a single element generated by counting the number of elements in a window over this DStream.
Return a new DStream in which each RDD has a single element generated by counting the number of elements in a window over this DStream. windowDuration and slideDuration are as defined in the window() operation. This is equivalent to window(windowDuration, slideDuration).count()  

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#dstream:org.apache.spark.streaming.dstream.DStream\[T\] "Permalink") val dstream: [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[T] 

Definition Classes
     [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream") → [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#equals\(x$1:Object\):Boolean "Permalink") def equals(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef → Any
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#filter\(f:org.apache.spark.api.java.function.Function\[T,Boolean\]\):org.apache.spark.streaming.api.java.JavaDStream\[T\] "Permalink") def filter(f: [Function](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function.html "org.apache.spark.api.java.function.Function")[T, [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html#java.lang.Boolean "java.lang.Boolean")]): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[T]
Return a new DStream containing only the elements that satisfy a predicate.
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#flatMap\[U\]\(f:org.apache.spark.api.java.function.FlatMapFunction\[T,U\]\):org.apache.spark.streaming.api.java.JavaDStream\[U\] "Permalink") def flatMap[U](f: [FlatMapFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction.html "org.apache.spark.api.java.function.FlatMapFunction")[T, U]): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[U]
Return a new DStream by applying a function to all elements of this DStream, and then flattening the results 
Return a new DStream by applying a function to all elements of this DStream, and then flattening the results  

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#flatMapToPair\[K2,V2\]\(f:org.apache.spark.api.java.function.PairFlatMapFunction\[T,K2,V2\]\):org.apache.spark.streaming.api.java.JavaPairDStream\[K2,V2\] "Permalink") def flatMapToPair[K2, V2](f: [PairFlatMapFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/PairFlatMapFunction.html "org.apache.spark.api.java.function.PairFlatMapFunction")[T, K2, V2]): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K2, V2]
Return a new DStream by applying a function to all elements of this DStream, and then flattening the results 
Return a new DStream by applying a function to all elements of this DStream, and then flattening the results  

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  23. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#foreachRDD\(foreachFunc:org.apache.spark.api.java.function.VoidFunction2\[R,org.apache.spark.streaming.Time\]\):Unit "Permalink") def foreachRDD(foreachFunc: [VoidFunction2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/VoidFunction2.html "org.apache.spark.api.java.function.VoidFunction2")[[JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[T], [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time")]): Unit
Apply a function to each RDD in this DStream.
Apply a function to each RDD in this DStream. This is an output operator, so 'this' DStream will be registered as an output stream and therefore materialized.  

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  24. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#foreachRDD\(foreachFunc:org.apache.spark.api.java.function.VoidFunction\[R\]\):Unit "Permalink") def foreachRDD(foreachFunc: [VoidFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/VoidFunction.html "org.apache.spark.api.java.function.VoidFunction")[[JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[T]]): Unit
Apply a function to each RDD in this DStream.
Apply a function to each RDD in this DStream. This is an output operator, so 'this' DStream will be registered as an output stream and therefore materialized.  

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  25. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef] 

Definition Classes
    AnyRef → Any 

Annotations
     @IntrinsicCandidate() @native()
  26. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#glom\(\):org.apache.spark.streaming.api.java.JavaDStream\[java.util.List\[T\]\] "Permalink") def glom(): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#java.util.List "java.util.List")[T]]
Return a new DStream in which each RDD is generated by applying glom() to each RDD of this DStream.
Return a new DStream in which each RDD is generated by applying glom() to each RDD of this DStream. Applying glom() to an RDD coalesces all elements within each partition into an array.  

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  27. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#hashCode\(\):Int "Permalink") def hashCode(): Int 

Definition Classes
    AnyRef → Any 

Annotations
     @IntrinsicCandidate() @native()
  28. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean 

Definition Classes
    Any
  29. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#map\[U\]\(f:org.apache.spark.api.java.function.Function\[T,U\]\):org.apache.spark.streaming.api.java.JavaDStream\[U\] "Permalink") def map[U](f: [Function](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function.html "org.apache.spark.api.java.function.Function")[T, U]): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[U]
Return a new DStream by applying a function to all elements of this DStream.
Return a new DStream by applying a function to all elements of this DStream. 

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  30. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#mapPartitions\[U\]\(f:org.apache.spark.api.java.function.FlatMapFunction\[java.util.Iterator\[T\],U\]\):org.apache.spark.streaming.api.java.JavaDStream\[U\] "Permalink") def mapPartitions[U](f: [FlatMapFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction.html "org.apache.spark.api.java.function.FlatMapFunction")[[Iterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html#java.util.Iterator "java.util.Iterator")[T], U]): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[U]
Return a new DStream in which each RDD is generated by applying mapPartitions() to each RDDs of this DStream.
Return a new DStream in which each RDD is generated by applying mapPartitions() to each RDDs of this DStream. Applying mapPartitions() to an RDD applies a function to each partition of the RDD.  

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  31. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#mapPartitionsToPair\[K2,V2\]\(f:org.apache.spark.api.java.function.PairFlatMapFunction\[java.util.Iterator\[T\],K2,V2\]\):org.apache.spark.streaming.api.java.JavaPairDStream\[K2,V2\] "Permalink") def mapPartitionsToPair[K2, V2](f: [PairFlatMapFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/PairFlatMapFunction.html "org.apache.spark.api.java.function.PairFlatMapFunction")[[Iterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html#java.util.Iterator "java.util.Iterator")[T], K2, V2]): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K2, V2]
Return a new DStream in which each RDD is generated by applying mapPartitions() to each RDDs of this DStream.
Return a new DStream in which each RDD is generated by applying mapPartitions() to each RDDs of this DStream. Applying mapPartitions() to an RDD applies a function to each partition of the RDD.  

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  32. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#mapToPair\[K2,V2\]\(f:org.apache.spark.api.java.function.PairFunction\[T,K2,V2\]\):org.apache.spark.streaming.api.java.JavaPairDStream\[K2,V2\] "Permalink") def mapToPair[K2, V2](f: [PairFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/PairFunction.html "org.apache.spark.api.java.function.PairFunction")[T, K2, V2]): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K2, V2]
Return a new DStream by applying a function to all elements of this DStream.
Return a new DStream by applying a function to all elements of this DStream. 

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  33. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  34. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#notify\(\):Unit "Permalink") final  def notify(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  35. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  36. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#persist\(storageLevel:org.apache.spark.storage.StorageLevel\):org.apache.spark.streaming.api.java.JavaDStream\[T\] "Permalink") def persist(storageLevel: [StorageLevel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StorageLevel.html "org.apache.spark.storage.StorageLevel")): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[T]
Persist the RDDs of this DStream with the given storage level
  37. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#persist\(\):org.apache.spark.streaming.api.java.JavaDStream\[T\] "Permalink") def persist(): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[T]
Persist RDDs of this DStream with the default storage level (MEMORY_ONLY_SER)
  38. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#print\(num:Int\):Unit "Permalink") def print(num: Int): Unit
Print the first num elements of each RDD generated in this DStream.
Print the first num elements of each RDD generated in this DStream. This is an output operator, so this DStream will be registered as an output stream and there materialized.  

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  39. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#print\(\):Unit "Permalink") def print(): Unit
Print the first ten elements of each RDD generated in this DStream.
Print the first ten elements of each RDD generated in this DStream. This is an output operator, so this DStream will be registered as an output stream and there materialized.  

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  40. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#reduce\(f:org.apache.spark.api.java.function.Function2\[T,T,T\]\):org.apache.spark.streaming.api.java.JavaDStream\[T\] "Permalink") def reduce(f: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[T, T, T]): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[T]
Return a new DStream in which each RDD has a single element generated by reducing each RDD of this DStream.
Return a new DStream in which each RDD has a single element generated by reducing each RDD of this DStream.  

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  41. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#reduceByWindow\(reduceFunc:org.apache.spark.api.java.function.Function2\[T,T,T\],invReduceFunc:org.apache.spark.api.java.function.Function2\[T,T,T\],windowDuration:org.apache.spark.streaming.Duration,slideDuration:org.apache.spark.streaming.Duration\):org.apache.spark.streaming.api.java.JavaDStream\[T\] "Permalink") def reduceByWindow(reduceFunc: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[T, T, T], invReduceFunc: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[T, T, T], windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration")): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[T]
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
  42. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#reduceByWindow\(reduceFunc:org.apache.spark.api.java.function.Function2\[T,T,T\],windowDuration:org.apache.spark.streaming.Duration,slideDuration:org.apache.spark.streaming.Duration\):org.apache.spark.streaming.api.java.JavaDStream\[T\] "Permalink") def reduceByWindow(reduceFunc: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[T, T, T], windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration")): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[T]
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
  43. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#repartition\(numPartitions:Int\):org.apache.spark.streaming.api.java.JavaDStream\[T\] "Permalink") def repartition(numPartitions: Int): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[T]
Return a new DStream with an increased or decreased level of parallelism.
Return a new DStream with an increased or decreased level of parallelism. Each RDD in the returned DStream has exactly numPartitions partitions. 
  44. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#scalaIntToJavaLong\(in:org.apache.spark.streaming.dstream.DStream\[Long\]\):org.apache.spark.streaming.api.java.JavaDStream\[Long\] "Permalink") implicit  def scalaIntToJavaLong(in: [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[Long]): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[[Long](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html#java.lang.Long "java.lang.Long")] 

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  45. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#slice\(fromTime:org.apache.spark.streaming.Time,toTime:org.apache.spark.streaming.Time\):java.util.List\[R\] "Permalink") def slice(fromTime: [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time"), toTime: [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time")): [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#java.util.List "java.util.List")[[JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[T]]
Return all the RDDs between 'fromDuration' to 'toDuration' (both included) 
Return all the RDDs between 'fromDuration' to 'toDuration' (both included)  

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  46. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0 

Definition Classes
    AnyRef
  47. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#toString\(\):String "Permalink") def toString(): [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String") 

Definition Classes
    AnyRef → Any
  48. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#transform\[U\]\(transformFunc:org.apache.spark.api.java.function.Function2\[R,org.apache.spark.streaming.Time,org.apache.spark.api.java.JavaRDD\[U\]\]\):org.apache.spark.streaming.api.java.JavaDStream\[U\] "Permalink") def transform[U](transformFunc: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[[JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[T], [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time"), [JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[U]]): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[U]
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream.
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream.  

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  49. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#transform\[U\]\(transformFunc:org.apache.spark.api.java.function.Function\[R,org.apache.spark.api.java.JavaRDD\[U\]\]\):org.apache.spark.streaming.api.java.JavaDStream\[U\] "Permalink") def transform[U](transformFunc: [Function](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function.html "org.apache.spark.api.java.function.Function")[[JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[T], [JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[U]]): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[U]
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream.
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream.  

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  50. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#transformToPair\[K2,V2\]\(transformFunc:org.apache.spark.api.java.function.Function2\[R,org.apache.spark.streaming.Time,org.apache.spark.api.java.JavaPairRDD\[K2,V2\]\]\):org.apache.spark.streaming.api.java.JavaPairDStream\[K2,V2\] "Permalink") def transformToPair[K2, V2](transformFunc: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[[JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[T], [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time"), [JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K2, V2]]): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K2, V2]
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream.
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream.  

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  51. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#transformToPair\[K2,V2\]\(transformFunc:org.apache.spark.api.java.function.Function\[R,org.apache.spark.api.java.JavaPairRDD\[K2,V2\]\]\):org.apache.spark.streaming.api.java.JavaPairDStream\[K2,V2\] "Permalink") def transformToPair[K2, V2](transformFunc: [Function](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function.html "org.apache.spark.api.java.function.Function")[[JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[T], [JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K2, V2]]): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K2, V2]
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream.
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream.  

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  52. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#transformWith\[K2,V2,W\]\(other:org.apache.spark.streaming.api.java.JavaPairDStream\[K2,V2\],transformFunc:org.apache.spark.api.java.function.Function3\[R,org.apache.spark.api.java.JavaPairRDD\[K2,V2\],org.apache.spark.streaming.Time,org.apache.spark.api.java.JavaRDD\[W\]\]\):org.apache.spark.streaming.api.java.JavaDStream\[W\] "Permalink") def transformWith[K2, V2, W](other: [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K2, V2], transformFunc: [Function3](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function3.html "org.apache.spark.api.java.function.Function3")[[JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[T], [JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K2, V2], [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time"), [JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[W]]): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[W]
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream and 'other' DStream.
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream and 'other' DStream.  

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  53. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#transformWith\[U,W\]\(other:org.apache.spark.streaming.api.java.JavaDStream\[U\],transformFunc:org.apache.spark.api.java.function.Function3\[R,org.apache.spark.api.java.JavaRDD\[U\],org.apache.spark.streaming.Time,org.apache.spark.api.java.JavaRDD\[W\]\]\):org.apache.spark.streaming.api.java.JavaDStream\[W\] "Permalink") def transformWith[U, W](other: [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[U], transformFunc: [Function3](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function3.html "org.apache.spark.api.java.function.Function3")[[JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[T], [JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[U], [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time"), [JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[W]]): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[W]
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream and 'other' DStream.
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream and 'other' DStream.  

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  54. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#transformWithToPair\[K2,V2,K3,V3\]\(other:org.apache.spark.streaming.api.java.JavaPairDStream\[K2,V2\],transformFunc:org.apache.spark.api.java.function.Function3\[R,org.apache.spark.api.java.JavaPairRDD\[K2,V2\],org.apache.spark.streaming.Time,org.apache.spark.api.java.JavaPairRDD\[K3,V3\]\]\):org.apache.spark.streaming.api.java.JavaPairDStream\[K3,V3\] "Permalink") def transformWithToPair[K2, V2, K3, V3](other: [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K2, V2], transformFunc: [Function3](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function3.html "org.apache.spark.api.java.function.Function3")[[JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[T], [JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K2, V2], [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time"), [JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K3, V3]]): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K3, V3]
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream and 'other' DStream.
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream and 'other' DStream.  

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  55. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#transformWithToPair\[U,K2,V2\]\(other:org.apache.spark.streaming.api.java.JavaDStream\[U\],transformFunc:org.apache.spark.api.java.function.Function3\[R,org.apache.spark.api.java.JavaRDD\[U\],org.apache.spark.streaming.Time,org.apache.spark.api.java.JavaPairRDD\[K2,V2\]\]\):org.apache.spark.streaming.api.java.JavaPairDStream\[K2,V2\] "Permalink") def transformWithToPair[U, K2, V2](other: [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[U], transformFunc: [Function3](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function3.html "org.apache.spark.api.java.function.Function3")[[JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[T], [JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[U], [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time"), [JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K2, V2]]): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K2, V2]
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream and 'other' DStream.
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream and 'other' DStream.  

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  56. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#union\(that:org.apache.spark.streaming.api.java.JavaDStream\[T\]\):org.apache.spark.streaming.api.java.JavaDStream\[T\] "Permalink") def union(that: [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[T]): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[T]
Return a new DStream by unifying data of another DStream with this DStream.
Return a new DStream by unifying data of another DStream with this DStream. 

that
    
Another DStream having the same interval (i.e., slideDuration) as this DStream.
  57. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  58. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  59. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#wait\(\):Unit "Permalink") final  def wait(): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  60. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#window\(windowDuration:org.apache.spark.streaming.Duration,slideDuration:org.apache.spark.streaming.Duration\):org.apache.spark.streaming.api.java.JavaDStream\[T\] "Permalink") def window(windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration")): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[T]
Return a new DStream in which each RDD contains all the elements in seen in a sliding window of time over this DStream.
Return a new DStream in which each RDD contains all the elements in seen in a sliding window of time over this DStream. 

windowDuration
    
width of the window; must be a multiple of this DStream's batching interval 

slideDuration
    
sliding interval of the window (i.e., the interval after which the new DStream will generate RDDs); must be a multiple of this DStream's batching interval
  61. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#window\(windowDuration:org.apache.spark.streaming.Duration\):org.apache.spark.streaming.api.java.JavaDStream\[T\] "Permalink") def window(windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration")): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[T]
Return a new DStream in which each RDD contains all the elements in seen in a sliding window of time over this DStream.
Return a new DStream in which each RDD contains all the elements in seen in a sliding window of time over this DStream. The new DStream generates RDDs with the same interval as this DStream. 

windowDuration
    
width of the window; must be a multiple of this DStream's interval.
  62. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#wrapRDD\(rdd:org.apache.spark.rdd.RDD\[T\]\):org.apache.spark.api.java.JavaRDD\[T\] "Permalink") def wrapRDD(rdd: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[T]): [JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[T] 

Definition Classes
     [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream") → [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")


### Deprecated Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#finalize\(\):Unit "Permalink") def finalize(): Unit 

Attributes
    protected[lang]  

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.Throwable]) @Deprecated 

Deprecated
    
_(Since version 9)_


### Inherited from [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")[T, [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[T], [JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[T]]
### Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#checkpoint\(interval:org.apache.spark.streaming.Duration\):org.apache.spark.streaming.dstream.DStream\[T\] "Permalink") def checkpoint(interval: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration")): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[T]
Enable periodic checkpointing of RDDs of this DStream.
Enable periodic checkpointing of RDDs of this DStream. 

interval
    
Time interval after which generated RDD will be checkpointed 

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#context\(\):org.apache.spark.streaming.StreamingContext "Permalink") def context(): [StreamingContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html "org.apache.spark.streaming.StreamingContext")
Return the [org.apache.spark.streaming.StreamingContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html "org.apache.spark.streaming.StreamingContext") associated with this DStream
Return the [org.apache.spark.streaming.StreamingContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html "org.apache.spark.streaming.StreamingContext") associated with this DStream 

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#count\(\):org.apache.spark.streaming.api.java.JavaDStream\[Long\] "Permalink") def count(): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[[Long](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html#java.lang.Long "java.lang.Long")]
Return a new DStream in which each RDD has a single element generated by counting each RDD of this DStream.
Return a new DStream in which each RDD has a single element generated by counting each RDD of this DStream.  

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#countByValue\(numPartitions:Int\):org.apache.spark.streaming.api.java.JavaPairDStream\[T,Long\] "Permalink") def countByValue(numPartitions: Int): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[T, [Long](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html#java.lang.Long "java.lang.Long")]
Return a new DStream in which each RDD contains the counts of each distinct value in each RDD of this DStream.
Return a new DStream in which each RDD contains the counts of each distinct value in each RDD of this DStream. Hash partitioning is used to generate the RDDs with `numPartitions` partitions. 

numPartitions
    
number of partitions of each RDD in the new DStream. 

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#countByValue\(\):org.apache.spark.streaming.api.java.JavaPairDStream\[T,Long\] "Permalink") def countByValue(): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[T, [Long](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html#java.lang.Long "java.lang.Long")]
Return a new DStream in which each RDD contains the counts of each distinct value in each RDD of this DStream.
Return a new DStream in which each RDD contains the counts of each distinct value in each RDD of this DStream. Hash partitioning is used to generate the RDDs with Spark's default number of partitions.  

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#countByValueAndWindow\(windowDuration:org.apache.spark.streaming.Duration,slideDuration:org.apache.spark.streaming.Duration,numPartitions:Int\):org.apache.spark.streaming.api.java.JavaPairDStream\[T,Long\] "Permalink") def countByValueAndWindow(windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), numPartitions: Int): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[T, [Long](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html#java.lang.Long "java.lang.Long")]
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
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#countByValueAndWindow\(windowDuration:org.apache.spark.streaming.Duration,slideDuration:org.apache.spark.streaming.Duration\):org.apache.spark.streaming.api.java.JavaPairDStream\[T,Long\] "Permalink") def countByValueAndWindow(windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration")): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[T, [Long](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html#java.lang.Long "java.lang.Long")]
Return a new DStream in which each RDD contains the count of distinct elements in RDDs in a sliding window over this DStream.
Return a new DStream in which each RDD contains the count of distinct elements in RDDs in a sliding window over this DStream. Hash partitioning is used to generate the RDDs with Spark's default number of partitions. 

windowDuration
    
width of the window; must be a multiple of this DStream's batching interval 

slideDuration
    
sliding interval of the window (i.e., the interval after which the new DStream will generate RDDs); must be a multiple of this DStream's batching interval 

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#countByWindow\(windowDuration:org.apache.spark.streaming.Duration,slideDuration:org.apache.spark.streaming.Duration\):org.apache.spark.streaming.api.java.JavaDStream\[Long\] "Permalink") def countByWindow(windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration")): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[[Long](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html#java.lang.Long "java.lang.Long")]
Return a new DStream in which each RDD has a single element generated by counting the number of elements in a window over this DStream.
Return a new DStream in which each RDD has a single element generated by counting the number of elements in a window over this DStream. windowDuration and slideDuration are as defined in the window() operation. This is equivalent to window(windowDuration, slideDuration).count()  

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#flatMap\[U\]\(f:org.apache.spark.api.java.function.FlatMapFunction\[T,U\]\):org.apache.spark.streaming.api.java.JavaDStream\[U\] "Permalink") def flatMap[U](f: [FlatMapFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction.html "org.apache.spark.api.java.function.FlatMapFunction")[T, U]): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[U]
Return a new DStream by applying a function to all elements of this DStream, and then flattening the results 
Return a new DStream by applying a function to all elements of this DStream, and then flattening the results  

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#flatMapToPair\[K2,V2\]\(f:org.apache.spark.api.java.function.PairFlatMapFunction\[T,K2,V2\]\):org.apache.spark.streaming.api.java.JavaPairDStream\[K2,V2\] "Permalink") def flatMapToPair[K2, V2](f: [PairFlatMapFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/PairFlatMapFunction.html "org.apache.spark.api.java.function.PairFlatMapFunction")[T, K2, V2]): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K2, V2]
Return a new DStream by applying a function to all elements of this DStream, and then flattening the results 
Return a new DStream by applying a function to all elements of this DStream, and then flattening the results  

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#foreachRDD\(foreachFunc:org.apache.spark.api.java.function.VoidFunction2\[R,org.apache.spark.streaming.Time\]\):Unit "Permalink") def foreachRDD(foreachFunc: [VoidFunction2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/VoidFunction2.html "org.apache.spark.api.java.function.VoidFunction2")[[JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[T], [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time")]): Unit
Apply a function to each RDD in this DStream.
Apply a function to each RDD in this DStream. This is an output operator, so 'this' DStream will be registered as an output stream and therefore materialized.  

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#foreachRDD\(foreachFunc:org.apache.spark.api.java.function.VoidFunction\[R\]\):Unit "Permalink") def foreachRDD(foreachFunc: [VoidFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/VoidFunction.html "org.apache.spark.api.java.function.VoidFunction")[[JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[T]]): Unit
Apply a function to each RDD in this DStream.
Apply a function to each RDD in this DStream. This is an output operator, so 'this' DStream will be registered as an output stream and therefore materialized.  

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#glom\(\):org.apache.spark.streaming.api.java.JavaDStream\[java.util.List\[T\]\] "Permalink") def glom(): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#java.util.List "java.util.List")[T]]
Return a new DStream in which each RDD is generated by applying glom() to each RDD of this DStream.
Return a new DStream in which each RDD is generated by applying glom() to each RDD of this DStream. Applying glom() to an RDD coalesces all elements within each partition into an array.  

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#map\[U\]\(f:org.apache.spark.api.java.function.Function\[T,U\]\):org.apache.spark.streaming.api.java.JavaDStream\[U\] "Permalink") def map[U](f: [Function](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function.html "org.apache.spark.api.java.function.Function")[T, U]): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[U]
Return a new DStream by applying a function to all elements of this DStream.
Return a new DStream by applying a function to all elements of this DStream. 

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#mapPartitions\[U\]\(f:org.apache.spark.api.java.function.FlatMapFunction\[java.util.Iterator\[T\],U\]\):org.apache.spark.streaming.api.java.JavaDStream\[U\] "Permalink") def mapPartitions[U](f: [FlatMapFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction.html "org.apache.spark.api.java.function.FlatMapFunction")[[Iterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html#java.util.Iterator "java.util.Iterator")[T], U]): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[U]
Return a new DStream in which each RDD is generated by applying mapPartitions() to each RDDs of this DStream.
Return a new DStream in which each RDD is generated by applying mapPartitions() to each RDDs of this DStream. Applying mapPartitions() to an RDD applies a function to each partition of the RDD.  

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#mapPartitionsToPair\[K2,V2\]\(f:org.apache.spark.api.java.function.PairFlatMapFunction\[java.util.Iterator\[T\],K2,V2\]\):org.apache.spark.streaming.api.java.JavaPairDStream\[K2,V2\] "Permalink") def mapPartitionsToPair[K2, V2](f: [PairFlatMapFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/PairFlatMapFunction.html "org.apache.spark.api.java.function.PairFlatMapFunction")[[Iterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html#java.util.Iterator "java.util.Iterator")[T], K2, V2]): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K2, V2]
Return a new DStream in which each RDD is generated by applying mapPartitions() to each RDDs of this DStream.
Return a new DStream in which each RDD is generated by applying mapPartitions() to each RDDs of this DStream. Applying mapPartitions() to an RDD applies a function to each partition of the RDD.  

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#mapToPair\[K2,V2\]\(f:org.apache.spark.api.java.function.PairFunction\[T,K2,V2\]\):org.apache.spark.streaming.api.java.JavaPairDStream\[K2,V2\] "Permalink") def mapToPair[K2, V2](f: [PairFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/PairFunction.html "org.apache.spark.api.java.function.PairFunction")[T, K2, V2]): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K2, V2]
Return a new DStream by applying a function to all elements of this DStream.
Return a new DStream by applying a function to all elements of this DStream. 

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#print\(num:Int\):Unit "Permalink") def print(num: Int): Unit
Print the first num elements of each RDD generated in this DStream.
Print the first num elements of each RDD generated in this DStream. This is an output operator, so this DStream will be registered as an output stream and there materialized.  

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#print\(\):Unit "Permalink") def print(): Unit
Print the first ten elements of each RDD generated in this DStream.
Print the first ten elements of each RDD generated in this DStream. This is an output operator, so this DStream will be registered as an output stream and there materialized.  

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#reduce\(f:org.apache.spark.api.java.function.Function2\[T,T,T\]\):org.apache.spark.streaming.api.java.JavaDStream\[T\] "Permalink") def reduce(f: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[T, T, T]): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[T]
Return a new DStream in which each RDD has a single element generated by reducing each RDD of this DStream.
Return a new DStream in which each RDD has a single element generated by reducing each RDD of this DStream.  

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#reduceByWindow\(reduceFunc:org.apache.spark.api.java.function.Function2\[T,T,T\],invReduceFunc:org.apache.spark.api.java.function.Function2\[T,T,T\],windowDuration:org.apache.spark.streaming.Duration,slideDuration:org.apache.spark.streaming.Duration\):org.apache.spark.streaming.api.java.JavaDStream\[T\] "Permalink") def reduceByWindow(reduceFunc: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[T, T, T], invReduceFunc: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[T, T, T], windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration")): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[T]
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
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#reduceByWindow\(reduceFunc:org.apache.spark.api.java.function.Function2\[T,T,T\],windowDuration:org.apache.spark.streaming.Duration,slideDuration:org.apache.spark.streaming.Duration\):org.apache.spark.streaming.api.java.JavaDStream\[T\] "Permalink") def reduceByWindow(reduceFunc: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[T, T, T], windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration")): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[T]
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
  23. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#scalaIntToJavaLong\(in:org.apache.spark.streaming.dstream.DStream\[Long\]\):org.apache.spark.streaming.api.java.JavaDStream\[Long\] "Permalink") implicit  def scalaIntToJavaLong(in: [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[Long]): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[[Long](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html#java.lang.Long "java.lang.Long")] 

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  24. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#slice\(fromTime:org.apache.spark.streaming.Time,toTime:org.apache.spark.streaming.Time\):java.util.List\[R\] "Permalink") def slice(fromTime: [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time"), toTime: [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time")): [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#java.util.List "java.util.List")[[JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[T]]
Return all the RDDs between 'fromDuration' to 'toDuration' (both included) 
Return all the RDDs between 'fromDuration' to 'toDuration' (both included)  

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  25. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#transform\[U\]\(transformFunc:org.apache.spark.api.java.function.Function2\[R,org.apache.spark.streaming.Time,org.apache.spark.api.java.JavaRDD\[U\]\]\):org.apache.spark.streaming.api.java.JavaDStream\[U\] "Permalink") def transform[U](transformFunc: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[[JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[T], [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time"), [JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[U]]): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[U]
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream.
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream.  

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  26. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#transform\[U\]\(transformFunc:org.apache.spark.api.java.function.Function\[R,org.apache.spark.api.java.JavaRDD\[U\]\]\):org.apache.spark.streaming.api.java.JavaDStream\[U\] "Permalink") def transform[U](transformFunc: [Function](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function.html "org.apache.spark.api.java.function.Function")[[JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[T], [JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[U]]): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[U]
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream.
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream.  

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  27. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#transformToPair\[K2,V2\]\(transformFunc:org.apache.spark.api.java.function.Function2\[R,org.apache.spark.streaming.Time,org.apache.spark.api.java.JavaPairRDD\[K2,V2\]\]\):org.apache.spark.streaming.api.java.JavaPairDStream\[K2,V2\] "Permalink") def transformToPair[K2, V2](transformFunc: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[[JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[T], [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time"), [JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K2, V2]]): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K2, V2]
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream.
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream.  

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  28. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#transformToPair\[K2,V2\]\(transformFunc:org.apache.spark.api.java.function.Function\[R,org.apache.spark.api.java.JavaPairRDD\[K2,V2\]\]\):org.apache.spark.streaming.api.java.JavaPairDStream\[K2,V2\] "Permalink") def transformToPair[K2, V2](transformFunc: [Function](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function.html "org.apache.spark.api.java.function.Function")[[JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[T], [JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K2, V2]]): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K2, V2]
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream.
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream.  

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  29. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#transformWith\[K2,V2,W\]\(other:org.apache.spark.streaming.api.java.JavaPairDStream\[K2,V2\],transformFunc:org.apache.spark.api.java.function.Function3\[R,org.apache.spark.api.java.JavaPairRDD\[K2,V2\],org.apache.spark.streaming.Time,org.apache.spark.api.java.JavaRDD\[W\]\]\):org.apache.spark.streaming.api.java.JavaDStream\[W\] "Permalink") def transformWith[K2, V2, W](other: [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K2, V2], transformFunc: [Function3](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function3.html "org.apache.spark.api.java.function.Function3")[[JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[T], [JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K2, V2], [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time"), [JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[W]]): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[W]
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream and 'other' DStream.
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream and 'other' DStream.  

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  30. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#transformWith\[U,W\]\(other:org.apache.spark.streaming.api.java.JavaDStream\[U\],transformFunc:org.apache.spark.api.java.function.Function3\[R,org.apache.spark.api.java.JavaRDD\[U\],org.apache.spark.streaming.Time,org.apache.spark.api.java.JavaRDD\[W\]\]\):org.apache.spark.streaming.api.java.JavaDStream\[W\] "Permalink") def transformWith[U, W](other: [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[U], transformFunc: [Function3](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function3.html "org.apache.spark.api.java.function.Function3")[[JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[T], [JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[U], [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time"), [JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[W]]): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[W]
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream and 'other' DStream.
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream and 'other' DStream.  

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  31. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#transformWithToPair\[K2,V2,K3,V3\]\(other:org.apache.spark.streaming.api.java.JavaPairDStream\[K2,V2\],transformFunc:org.apache.spark.api.java.function.Function3\[R,org.apache.spark.api.java.JavaPairRDD\[K2,V2\],org.apache.spark.streaming.Time,org.apache.spark.api.java.JavaPairRDD\[K3,V3\]\]\):org.apache.spark.streaming.api.java.JavaPairDStream\[K3,V3\] "Permalink") def transformWithToPair[K2, V2, K3, V3](other: [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K2, V2], transformFunc: [Function3](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function3.html "org.apache.spark.api.java.function.Function3")[[JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[T], [JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K2, V2], [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time"), [JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K3, V3]]): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K3, V3]
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream and 'other' DStream.
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream and 'other' DStream.  

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  32. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#transformWithToPair\[U,K2,V2\]\(other:org.apache.spark.streaming.api.java.JavaDStream\[U\],transformFunc:org.apache.spark.api.java.function.Function3\[R,org.apache.spark.api.java.JavaRDD\[U\],org.apache.spark.streaming.Time,org.apache.spark.api.java.JavaPairRDD\[K2,V2\]\]\):org.apache.spark.streaming.api.java.JavaPairDStream\[K2,V2\] "Permalink") def transformWithToPair[U, K2, V2](other: [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[U], transformFunc: [Function3](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function3.html "org.apache.spark.api.java.function.Function3")[[JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[T], [JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[U], [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time"), [JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K2, V2]]): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K2, V2]
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream and 'other' DStream.
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream and 'other' DStream.  

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")


### Inherited from AnyRef
### Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html###:Int "Permalink") final  def ##: Int 

Definition Classes
    AnyRef → Any
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#clone\(\):Object "Permalink") def clone(): AnyRef 

Attributes
    protected[lang]  

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#equals\(x$1:Object\):Boolean "Permalink") def equals(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef → Any
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef] 

Definition Classes
    AnyRef → Any 

Annotations
     @IntrinsicCandidate() @native()
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#hashCode\(\):Int "Permalink") def hashCode(): Int 

Definition Classes
    AnyRef → Any 

Annotations
     @IntrinsicCandidate() @native()
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#notify\(\):Unit "Permalink") final  def notify(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0 

Definition Classes
    AnyRef
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#toString\(\):String "Permalink") def toString(): [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String") 

Definition Classes
    AnyRef → Any
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#wait\(\):Unit "Permalink") final  def wait(): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#finalize\(\):Unit "Permalink") def finalize(): Unit 

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
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0 

Definition Classes
    Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean 

Definition Classes
    Any


### Ungrouped
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html###:Int "Permalink") final  def ##: Int 

Definition Classes
    AnyRef → Any
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0 

Definition Classes
    Any
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#cache\(\):org.apache.spark.streaming.api.java.JavaDStream\[T\] "Permalink") def cache(): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[T]
Persist RDDs of this DStream with the default storage level (MEMORY_ONLY_SER)
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#checkpoint\(interval:org.apache.spark.streaming.Duration\):org.apache.spark.streaming.dstream.DStream\[T\] "Permalink") def checkpoint(interval: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration")): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[T]
Enable periodic checkpointing of RDDs of this DStream.
Enable periodic checkpointing of RDDs of this DStream. 

interval
    
Time interval after which generated RDD will be checkpointed 

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#classTag:scala.reflect.ClassTag\[T\] "Permalink") implicit  val classTag: ClassTag[T] 

Definition Classes
     [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream") → [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#clone\(\):Object "Permalink") def clone(): AnyRef 

Attributes
    protected[lang]  

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#compute\(validTime:org.apache.spark.streaming.Time\):org.apache.spark.api.java.JavaRDD\[T\] "Permalink") def compute(validTime: [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time")): [JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[T]
Generate an RDD for the given duration
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#context\(\):org.apache.spark.streaming.StreamingContext "Permalink") def context(): [StreamingContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html "org.apache.spark.streaming.StreamingContext")
Return the [org.apache.spark.streaming.StreamingContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html "org.apache.spark.streaming.StreamingContext") associated with this DStream
Return the [org.apache.spark.streaming.StreamingContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html "org.apache.spark.streaming.StreamingContext") associated with this DStream 

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#count\(\):org.apache.spark.streaming.api.java.JavaDStream\[Long\] "Permalink") def count(): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[[Long](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html#java.lang.Long "java.lang.Long")]
Return a new DStream in which each RDD has a single element generated by counting each RDD of this DStream.
Return a new DStream in which each RDD has a single element generated by counting each RDD of this DStream.  

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#countByValue\(numPartitions:Int\):org.apache.spark.streaming.api.java.JavaPairDStream\[T,Long\] "Permalink") def countByValue(numPartitions: Int): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[T, [Long](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html#java.lang.Long "java.lang.Long")]
Return a new DStream in which each RDD contains the counts of each distinct value in each RDD of this DStream.
Return a new DStream in which each RDD contains the counts of each distinct value in each RDD of this DStream. Hash partitioning is used to generate the RDDs with `numPartitions` partitions. 

numPartitions
    
number of partitions of each RDD in the new DStream. 

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#countByValue\(\):org.apache.spark.streaming.api.java.JavaPairDStream\[T,Long\] "Permalink") def countByValue(): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[T, [Long](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html#java.lang.Long "java.lang.Long")]
Return a new DStream in which each RDD contains the counts of each distinct value in each RDD of this DStream.
Return a new DStream in which each RDD contains the counts of each distinct value in each RDD of this DStream. Hash partitioning is used to generate the RDDs with Spark's default number of partitions.  

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#countByValueAndWindow\(windowDuration:org.apache.spark.streaming.Duration,slideDuration:org.apache.spark.streaming.Duration,numPartitions:Int\):org.apache.spark.streaming.api.java.JavaPairDStream\[T,Long\] "Permalink") def countByValueAndWindow(windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), numPartitions: Int): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[T, [Long](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html#java.lang.Long "java.lang.Long")]
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
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#countByValueAndWindow\(windowDuration:org.apache.spark.streaming.Duration,slideDuration:org.apache.spark.streaming.Duration\):org.apache.spark.streaming.api.java.JavaPairDStream\[T,Long\] "Permalink") def countByValueAndWindow(windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration")): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[T, [Long](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html#java.lang.Long "java.lang.Long")]
Return a new DStream in which each RDD contains the count of distinct elements in RDDs in a sliding window over this DStream.
Return a new DStream in which each RDD contains the count of distinct elements in RDDs in a sliding window over this DStream. Hash partitioning is used to generate the RDDs with Spark's default number of partitions. 

windowDuration
    
width of the window; must be a multiple of this DStream's batching interval 

slideDuration
    
sliding interval of the window (i.e., the interval after which the new DStream will generate RDDs); must be a multiple of this DStream's batching interval 

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#countByWindow\(windowDuration:org.apache.spark.streaming.Duration,slideDuration:org.apache.spark.streaming.Duration\):org.apache.spark.streaming.api.java.JavaDStream\[Long\] "Permalink") def countByWindow(windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration")): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[[Long](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html#java.lang.Long "java.lang.Long")]
Return a new DStream in which each RDD has a single element generated by counting the number of elements in a window over this DStream.
Return a new DStream in which each RDD has a single element generated by counting the number of elements in a window over this DStream. windowDuration and slideDuration are as defined in the window() operation. This is equivalent to window(windowDuration, slideDuration).count()  

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#dstream:org.apache.spark.streaming.dstream.DStream\[T\] "Permalink") val dstream: [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[T] 

Definition Classes
     [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream") → [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#equals\(x$1:Object\):Boolean "Permalink") def equals(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef → Any
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#filter\(f:org.apache.spark.api.java.function.Function\[T,Boolean\]\):org.apache.spark.streaming.api.java.JavaDStream\[T\] "Permalink") def filter(f: [Function](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function.html "org.apache.spark.api.java.function.Function")[T, [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html#java.lang.Boolean "java.lang.Boolean")]): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[T]
Return a new DStream containing only the elements that satisfy a predicate.
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#flatMap\[U\]\(f:org.apache.spark.api.java.function.FlatMapFunction\[T,U\]\):org.apache.spark.streaming.api.java.JavaDStream\[U\] "Permalink") def flatMap[U](f: [FlatMapFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction.html "org.apache.spark.api.java.function.FlatMapFunction")[T, U]): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[U]
Return a new DStream by applying a function to all elements of this DStream, and then flattening the results 
Return a new DStream by applying a function to all elements of this DStream, and then flattening the results  

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#flatMapToPair\[K2,V2\]\(f:org.apache.spark.api.java.function.PairFlatMapFunction\[T,K2,V2\]\):org.apache.spark.streaming.api.java.JavaPairDStream\[K2,V2\] "Permalink") def flatMapToPair[K2, V2](f: [PairFlatMapFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/PairFlatMapFunction.html "org.apache.spark.api.java.function.PairFlatMapFunction")[T, K2, V2]): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K2, V2]
Return a new DStream by applying a function to all elements of this DStream, and then flattening the results 
Return a new DStream by applying a function to all elements of this DStream, and then flattening the results  

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  23. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#foreachRDD\(foreachFunc:org.apache.spark.api.java.function.VoidFunction2\[R,org.apache.spark.streaming.Time\]\):Unit "Permalink") def foreachRDD(foreachFunc: [VoidFunction2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/VoidFunction2.html "org.apache.spark.api.java.function.VoidFunction2")[[JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[T], [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time")]): Unit
Apply a function to each RDD in this DStream.
Apply a function to each RDD in this DStream. This is an output operator, so 'this' DStream will be registered as an output stream and therefore materialized.  

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  24. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#foreachRDD\(foreachFunc:org.apache.spark.api.java.function.VoidFunction\[R\]\):Unit "Permalink") def foreachRDD(foreachFunc: [VoidFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/VoidFunction.html "org.apache.spark.api.java.function.VoidFunction")[[JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[T]]): Unit
Apply a function to each RDD in this DStream.
Apply a function to each RDD in this DStream. This is an output operator, so 'this' DStream will be registered as an output stream and therefore materialized.  

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  25. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef] 

Definition Classes
    AnyRef → Any 

Annotations
     @IntrinsicCandidate() @native()
  26. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#glom\(\):org.apache.spark.streaming.api.java.JavaDStream\[java.util.List\[T\]\] "Permalink") def glom(): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#java.util.List "java.util.List")[T]]
Return a new DStream in which each RDD is generated by applying glom() to each RDD of this DStream.
Return a new DStream in which each RDD is generated by applying glom() to each RDD of this DStream. Applying glom() to an RDD coalesces all elements within each partition into an array.  

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  27. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#hashCode\(\):Int "Permalink") def hashCode(): Int 

Definition Classes
    AnyRef → Any 

Annotations
     @IntrinsicCandidate() @native()
  28. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean 

Definition Classes
    Any
  29. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#map\[U\]\(f:org.apache.spark.api.java.function.Function\[T,U\]\):org.apache.spark.streaming.api.java.JavaDStream\[U\] "Permalink") def map[U](f: [Function](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function.html "org.apache.spark.api.java.function.Function")[T, U]): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[U]
Return a new DStream by applying a function to all elements of this DStream.
Return a new DStream by applying a function to all elements of this DStream. 

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  30. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#mapPartitions\[U\]\(f:org.apache.spark.api.java.function.FlatMapFunction\[java.util.Iterator\[T\],U\]\):org.apache.spark.streaming.api.java.JavaDStream\[U\] "Permalink") def mapPartitions[U](f: [FlatMapFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction.html "org.apache.spark.api.java.function.FlatMapFunction")[[Iterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html#java.util.Iterator "java.util.Iterator")[T], U]): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[U]
Return a new DStream in which each RDD is generated by applying mapPartitions() to each RDDs of this DStream.
Return a new DStream in which each RDD is generated by applying mapPartitions() to each RDDs of this DStream. Applying mapPartitions() to an RDD applies a function to each partition of the RDD.  

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  31. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#mapPartitionsToPair\[K2,V2\]\(f:org.apache.spark.api.java.function.PairFlatMapFunction\[java.util.Iterator\[T\],K2,V2\]\):org.apache.spark.streaming.api.java.JavaPairDStream\[K2,V2\] "Permalink") def mapPartitionsToPair[K2, V2](f: [PairFlatMapFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/PairFlatMapFunction.html "org.apache.spark.api.java.function.PairFlatMapFunction")[[Iterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html#java.util.Iterator "java.util.Iterator")[T], K2, V2]): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K2, V2]
Return a new DStream in which each RDD is generated by applying mapPartitions() to each RDDs of this DStream.
Return a new DStream in which each RDD is generated by applying mapPartitions() to each RDDs of this DStream. Applying mapPartitions() to an RDD applies a function to each partition of the RDD.  

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  32. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#mapToPair\[K2,V2\]\(f:org.apache.spark.api.java.function.PairFunction\[T,K2,V2\]\):org.apache.spark.streaming.api.java.JavaPairDStream\[K2,V2\] "Permalink") def mapToPair[K2, V2](f: [PairFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/PairFunction.html "org.apache.spark.api.java.function.PairFunction")[T, K2, V2]): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K2, V2]
Return a new DStream by applying a function to all elements of this DStream.
Return a new DStream by applying a function to all elements of this DStream. 

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  33. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  34. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#notify\(\):Unit "Permalink") final  def notify(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  35. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  36. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#persist\(storageLevel:org.apache.spark.storage.StorageLevel\):org.apache.spark.streaming.api.java.JavaDStream\[T\] "Permalink") def persist(storageLevel: [StorageLevel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StorageLevel.html "org.apache.spark.storage.StorageLevel")): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[T]
Persist the RDDs of this DStream with the given storage level
  37. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#persist\(\):org.apache.spark.streaming.api.java.JavaDStream\[T\] "Permalink") def persist(): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[T]
Persist RDDs of this DStream with the default storage level (MEMORY_ONLY_SER)
  38. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#print\(num:Int\):Unit "Permalink") def print(num: Int): Unit
Print the first num elements of each RDD generated in this DStream.
Print the first num elements of each RDD generated in this DStream. This is an output operator, so this DStream will be registered as an output stream and there materialized.  

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  39. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#print\(\):Unit "Permalink") def print(): Unit
Print the first ten elements of each RDD generated in this DStream.
Print the first ten elements of each RDD generated in this DStream. This is an output operator, so this DStream will be registered as an output stream and there materialized.  

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  40. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#reduce\(f:org.apache.spark.api.java.function.Function2\[T,T,T\]\):org.apache.spark.streaming.api.java.JavaDStream\[T\] "Permalink") def reduce(f: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[T, T, T]): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[T]
Return a new DStream in which each RDD has a single element generated by reducing each RDD of this DStream.
Return a new DStream in which each RDD has a single element generated by reducing each RDD of this DStream.  

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  41. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#reduceByWindow\(reduceFunc:org.apache.spark.api.java.function.Function2\[T,T,T\],invReduceFunc:org.apache.spark.api.java.function.Function2\[T,T,T\],windowDuration:org.apache.spark.streaming.Duration,slideDuration:org.apache.spark.streaming.Duration\):org.apache.spark.streaming.api.java.JavaDStream\[T\] "Permalink") def reduceByWindow(reduceFunc: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[T, T, T], invReduceFunc: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[T, T, T], windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration")): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[T]
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
  42. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#reduceByWindow\(reduceFunc:org.apache.spark.api.java.function.Function2\[T,T,T\],windowDuration:org.apache.spark.streaming.Duration,slideDuration:org.apache.spark.streaming.Duration\):org.apache.spark.streaming.api.java.JavaDStream\[T\] "Permalink") def reduceByWindow(reduceFunc: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[T, T, T], windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration")): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[T]
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
  43. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#repartition\(numPartitions:Int\):org.apache.spark.streaming.api.java.JavaDStream\[T\] "Permalink") def repartition(numPartitions: Int): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[T]
Return a new DStream with an increased or decreased level of parallelism.
Return a new DStream with an increased or decreased level of parallelism. Each RDD in the returned DStream has exactly numPartitions partitions. 
  44. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#scalaIntToJavaLong\(in:org.apache.spark.streaming.dstream.DStream\[Long\]\):org.apache.spark.streaming.api.java.JavaDStream\[Long\] "Permalink") implicit  def scalaIntToJavaLong(in: [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[Long]): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[[Long](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html#java.lang.Long "java.lang.Long")] 

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  45. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#slice\(fromTime:org.apache.spark.streaming.Time,toTime:org.apache.spark.streaming.Time\):java.util.List\[R\] "Permalink") def slice(fromTime: [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time"), toTime: [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time")): [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#java.util.List "java.util.List")[[JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[T]]
Return all the RDDs between 'fromDuration' to 'toDuration' (both included) 
Return all the RDDs between 'fromDuration' to 'toDuration' (both included)  

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  46. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0 

Definition Classes
    AnyRef
  47. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#toString\(\):String "Permalink") def toString(): [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String") 

Definition Classes
    AnyRef → Any
  48. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#transform\[U\]\(transformFunc:org.apache.spark.api.java.function.Function2\[R,org.apache.spark.streaming.Time,org.apache.spark.api.java.JavaRDD\[U\]\]\):org.apache.spark.streaming.api.java.JavaDStream\[U\] "Permalink") def transform[U](transformFunc: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[[JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[T], [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time"), [JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[U]]): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[U]
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream.
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream.  

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  49. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#transform\[U\]\(transformFunc:org.apache.spark.api.java.function.Function\[R,org.apache.spark.api.java.JavaRDD\[U\]\]\):org.apache.spark.streaming.api.java.JavaDStream\[U\] "Permalink") def transform[U](transformFunc: [Function](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function.html "org.apache.spark.api.java.function.Function")[[JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[T], [JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[U]]): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[U]
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream.
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream.  

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  50. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#transformToPair\[K2,V2\]\(transformFunc:org.apache.spark.api.java.function.Function2\[R,org.apache.spark.streaming.Time,org.apache.spark.api.java.JavaPairRDD\[K2,V2\]\]\):org.apache.spark.streaming.api.java.JavaPairDStream\[K2,V2\] "Permalink") def transformToPair[K2, V2](transformFunc: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[[JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[T], [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time"), [JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K2, V2]]): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K2, V2]
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream.
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream.  

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  51. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#transformToPair\[K2,V2\]\(transformFunc:org.apache.spark.api.java.function.Function\[R,org.apache.spark.api.java.JavaPairRDD\[K2,V2\]\]\):org.apache.spark.streaming.api.java.JavaPairDStream\[K2,V2\] "Permalink") def transformToPair[K2, V2](transformFunc: [Function](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function.html "org.apache.spark.api.java.function.Function")[[JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[T], [JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K2, V2]]): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K2, V2]
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream.
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream.  

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  52. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#transformWith\[K2,V2,W\]\(other:org.apache.spark.streaming.api.java.JavaPairDStream\[K2,V2\],transformFunc:org.apache.spark.api.java.function.Function3\[R,org.apache.spark.api.java.JavaPairRDD\[K2,V2\],org.apache.spark.streaming.Time,org.apache.spark.api.java.JavaRDD\[W\]\]\):org.apache.spark.streaming.api.java.JavaDStream\[W\] "Permalink") def transformWith[K2, V2, W](other: [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K2, V2], transformFunc: [Function3](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function3.html "org.apache.spark.api.java.function.Function3")[[JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[T], [JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K2, V2], [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time"), [JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[W]]): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[W]
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream and 'other' DStream.
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream and 'other' DStream.  

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  53. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#transformWith\[U,W\]\(other:org.apache.spark.streaming.api.java.JavaDStream\[U\],transformFunc:org.apache.spark.api.java.function.Function3\[R,org.apache.spark.api.java.JavaRDD\[U\],org.apache.spark.streaming.Time,org.apache.spark.api.java.JavaRDD\[W\]\]\):org.apache.spark.streaming.api.java.JavaDStream\[W\] "Permalink") def transformWith[U, W](other: [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[U], transformFunc: [Function3](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function3.html "org.apache.spark.api.java.function.Function3")[[JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[T], [JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[U], [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time"), [JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[W]]): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[W]
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream and 'other' DStream.
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream and 'other' DStream.  

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  54. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#transformWithToPair\[K2,V2,K3,V3\]\(other:org.apache.spark.streaming.api.java.JavaPairDStream\[K2,V2\],transformFunc:org.apache.spark.api.java.function.Function3\[R,org.apache.spark.api.java.JavaPairRDD\[K2,V2\],org.apache.spark.streaming.Time,org.apache.spark.api.java.JavaPairRDD\[K3,V3\]\]\):org.apache.spark.streaming.api.java.JavaPairDStream\[K3,V3\] "Permalink") def transformWithToPair[K2, V2, K3, V3](other: [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K2, V2], transformFunc: [Function3](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function3.html "org.apache.spark.api.java.function.Function3")[[JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[T], [JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K2, V2], [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time"), [JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K3, V3]]): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K3, V3]
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream and 'other' DStream.
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream and 'other' DStream.  

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  55. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#transformWithToPair\[U,K2,V2\]\(other:org.apache.spark.streaming.api.java.JavaDStream\[U\],transformFunc:org.apache.spark.api.java.function.Function3\[R,org.apache.spark.api.java.JavaRDD\[U\],org.apache.spark.streaming.Time,org.apache.spark.api.java.JavaPairRDD\[K2,V2\]\]\):org.apache.spark.streaming.api.java.JavaPairDStream\[K2,V2\] "Permalink") def transformWithToPair[U, K2, V2](other: [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[U], transformFunc: [Function3](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function3.html "org.apache.spark.api.java.function.Function3")[[JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[T], [JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[U], [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time"), [JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K2, V2]]): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K2, V2]
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream and 'other' DStream.
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream and 'other' DStream.  

Definition Classes
    [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  56. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#union\(that:org.apache.spark.streaming.api.java.JavaDStream\[T\]\):org.apache.spark.streaming.api.java.JavaDStream\[T\] "Permalink") def union(that: [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[T]): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[T]
Return a new DStream by unifying data of another DStream with this DStream.
Return a new DStream by unifying data of another DStream with this DStream. 

that
    
Another DStream having the same interval (i.e., slideDuration) as this DStream.
  57. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  58. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  59. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#wait\(\):Unit "Permalink") final  def wait(): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  60. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#window\(windowDuration:org.apache.spark.streaming.Duration,slideDuration:org.apache.spark.streaming.Duration\):org.apache.spark.streaming.api.java.JavaDStream\[T\] "Permalink") def window(windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration")): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[T]
Return a new DStream in which each RDD contains all the elements in seen in a sliding window of time over this DStream.
Return a new DStream in which each RDD contains all the elements in seen in a sliding window of time over this DStream. 

windowDuration
    
width of the window; must be a multiple of this DStream's batching interval 

slideDuration
    
sliding interval of the window (i.e., the interval after which the new DStream will generate RDDs); must be a multiple of this DStream's batching interval
  61. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#window\(windowDuration:org.apache.spark.streaming.Duration\):org.apache.spark.streaming.api.java.JavaDStream\[T\] "Permalink") def window(windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration")): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[T]
Return a new DStream in which each RDD contains all the elements in seen in a sliding window of time over this DStream.
Return a new DStream in which each RDD contains all the elements in seen in a sliding window of time over this DStream. The new DStream generates RDDs with the same interval as this DStream. 

windowDuration
    
width of the window; must be a multiple of this DStream's interval.
  62. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#wrapRDD\(rdd:org.apache.spark.rdd.RDD\[T\]\):org.apache.spark.api.java.JavaRDD\[T\] "Permalink") def wrapRDD(rdd: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[T]): [JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[T] 

Definition Classes
     [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream") → [JavaDStreamLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStreamLike.html "org.apache.spark.streaming.api.java.JavaDStreamLike")
  63. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html#finalize\(\):Unit "Permalink") def finalize(): Unit 

Attributes
    protected[lang]  

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.Throwable]) @Deprecated 

Deprecated
    
_(Since version 9)_


