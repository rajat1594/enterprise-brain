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


[c](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream$.html "See companion object")
[org](https://spark.apache.org/docs/latest/api/scala/org/index.html "org").[apache](https://spark.apache.org/docs/latest/api/scala/org/apache/index.html "org.apache").[spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark").[streaming](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/index.html "org.apache.spark.streaming").[dstream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/index.html "org.apache.spark.streaming.dstream")
#  [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream$.html "See companion object")[ __](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "Permalink")
### 
Companion [object DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream$.html "See companion object")
####  abstract  class DStream[T] extends Serializable with Logging
A Discretized Stream (DStream), the basic abstraction in Spark Streaming, is a continuous sequence of RDDs (of the same type) representing a continuous stream of data (see org.apache.spark.rdd.RDD in the Spark core documentation for more details on RDDs). DStreams can either be created from live data (such as, data from TCP sockets, Kafka, etc.) using a [org.apache.spark.streaming.StreamingContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html "org.apache.spark.streaming.StreamingContext") or it can be generated by transforming existing DStreams using operations such as `map`, `window` and `reduceByKeyAndWindow`. While a Spark Streaming program is running, each DStream periodically generates a RDD, either from live data or by transforming the RDD generated by a parent DStream.
This class contains the basic operations available on all DStreams, such as `map`, `filter` and `window`. In addition, [org.apache.spark.streaming.dstream.PairDStreamFunctions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html "org.apache.spark.streaming.dstream.PairDStreamFunctions") contains operations available only on DStreams of key-value pairs, such as `groupByKeyAndWindow` and `join`. These operations are automatically available on any DStream of pairs (e.g., DStream[(Int, Int)] through implicit conversions.
A DStream internally is characterized by a few basic properties:
  * A list of other DStreams that the DStream depends on
  * A time interval at which the DStream generates an RDD
  * A function that is used to generate an RDD after each time interval 



Source
    [DStream.scala](https://github.com/apache/spark/tree/v4.1.2/streaming/src/main/scala/org/apache/spark/streaming/dstream/DStream.scala)
Linear Supertypes
Logging, [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable"), AnyRef, Any
Known Subclasses
[ConstantInputDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/ConstantInputDStream.html "org.apache.spark.streaming.dstream.ConstantInputDStream"), [InputDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/InputDStream.html "org.apache.spark.streaming.dstream.InputDStream"), [MapWithStateDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/MapWithStateDStream.html "org.apache.spark.streaming.dstream.MapWithStateDStream"), [ReceiverInputDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/ReceiverInputDStream.html "org.apache.spark.streaming.dstream.ReceiverInputDStream")
__ __
Ordering
  1. Alphabetic
  2. By Inheritance


Inherited  

  1. DStream
  2. Logging
  3. Serializable
  4. AnyRef
  5. Any


  1. Hide All
  2. Show All


Visibility
  1. Public
  2. Protected


### Instance Constructors
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#<init>\(ssc:org.apache.spark.streaming.StreamingContext\)\(implicitevidence$1:scala.reflect.ClassTag\[T\]\):org.apache.spark.streaming.dstream.DStream\[T\] "Permalink") new DStream(ssc: [StreamingContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html "org.apache.spark.streaming.StreamingContext"))(implicit arg0: ClassTag[T])


### Type Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#LogStringContextextendsAnyRef "Permalink") implicit  class LogStringContext extends AnyRef 

Definition Classes
    Logging


### Abstract Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#compute\(validTime:org.apache.spark.streaming.Time\):Option\[org.apache.spark.rdd.RDD\[T\]\] "Permalink") abstract  def compute(validTime: [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time")): Option[[RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[T]]
Method that generates an RDD for the given time
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#dependencies:List\[org.apache.spark.streaming.dstream.DStream\[_\]\] "Permalink") abstract  def dependencies: List[[DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[_]]
List of parent DStreams on which this DStream depends on
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#slideDuration:org.apache.spark.streaming.Duration "Permalink") abstract  def slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration")
Time interval after which the DStream generates an RDD


### Concrete Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html###:Int "Permalink") final  def ##: Int 

Definition Classes
    AnyRef → Any
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#MDC\(key:org.apache.spark.internal.LogKey,value:Any\):org.apache.spark.internal.MDC "Permalink") def MDC(key: LogKey, value: Any): MDC 

Attributes
    protected  

Definition Classes
    Logging
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0 

Definition Classes
    Any
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#baseScope:Option\[String\] "Permalink") val baseScope: Option[String]
The base scope associated with the operation that created this DStream.
The base scope associated with the operation that created this DStream.
This is the medium through which we pass the DStream operation name (e.g. updatedStateByKey) to the RDDs created by this DStream. Note that we never use this scope directly in RDDs. Instead, we instantiate a new scope during each call to `compute` based on this one.
This is not defined if the DStream is created outside of one of the public DStream operations.  

Attributes
    protected[[streaming](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/index.html "org.apache.spark.streaming")] 
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#cache\(\):org.apache.spark.streaming.dstream.DStream\[T\] "Permalink") def cache(): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[T]
Persist RDDs of this DStream with the default storage level (MEMORY_ONLY_SER)
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#checkpoint\(interval:org.apache.spark.streaming.Duration\):org.apache.spark.streaming.dstream.DStream\[T\] "Permalink") def checkpoint(interval: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration")): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[T]
Enable periodic checkpointing of RDDs of this DStream
Enable periodic checkpointing of RDDs of this DStream 

interval
    
Time interval after which generated RDD will be checkpointed
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#clone\(\):Object "Permalink") def clone(): AnyRef 

Attributes
    protected[lang]  

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#context:org.apache.spark.streaming.StreamingContext "Permalink") def context: [StreamingContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html "org.apache.spark.streaming.StreamingContext")
Return the StreamingContext associated with this DStream
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#count\(\):org.apache.spark.streaming.dstream.DStream\[Long\] "Permalink") def count(): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[Long]
Return a new DStream in which each RDD has a single element generated by counting each RDD of this DStream.
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#countByValue\(numPartitions:Int\)\(implicitord:Ordering\[T\]\):org.apache.spark.streaming.dstream.DStream\[\(T,Long\)\] "Permalink") def countByValue(numPartitions: Int = [ssc.sc.defaultParallelism](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#defaultParallelism:Int))(implicit ord: Ordering[T] = null): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(T, Long)]
Return a new DStream in which each RDD contains the counts of each distinct value in each RDD of this DStream.
Return a new DStream in which each RDD contains the counts of each distinct value in each RDD of this DStream. Hash partitioning is used to generate the RDDs with `numPartitions` partitions (Spark's default number of partitions if `numPartitions` not specified). 
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#countByValueAndWindow\(windowDuration:org.apache.spark.streaming.Duration,slideDuration:org.apache.spark.streaming.Duration,numPartitions:Int\)\(implicitord:Ordering\[T\]\):org.apache.spark.streaming.dstream.DStream\[\(T,Long\)\] "Permalink") def countByValueAndWindow(windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), numPartitions: Int = [ssc.sc.defaultParallelism](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#defaultParallelism:Int))(implicit ord: Ordering[T] = null): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(T, Long)]
Return a new DStream in which each RDD contains the count of distinct elements in RDDs in a sliding window over this DStream.
Return a new DStream in which each RDD contains the count of distinct elements in RDDs in a sliding window over this DStream. Hash partitioning is used to generate the RDDs with `numPartitions` partitions (Spark's default number of partitions if `numPartitions` not specified). 

windowDuration
    
width of the window; must be a multiple of this DStream's batching interval 

slideDuration
    
sliding interval of the window (i.e., the interval after which the new DStream will generate RDDs); must be a multiple of this DStream's batching interval 

numPartitions
    
number of partitions of each RDD in the new DStream.
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#countByWindow\(windowDuration:org.apache.spark.streaming.Duration,slideDuration:org.apache.spark.streaming.Duration\):org.apache.spark.streaming.dstream.DStream\[Long\] "Permalink") def countByWindow(windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration")): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[Long]
Return a new DStream in which each RDD has a single element generated by counting the number of elements in a sliding window over this DStream.
Return a new DStream in which each RDD has a single element generated by counting the number of elements in a sliding window over this DStream. Hash partitioning is used to generate the RDDs with Spark's default number of partitions. 

windowDuration
    
width of the window; must be a multiple of this DStream's batching interval 

slideDuration
    
sliding interval of the window (i.e., the interval after which the new DStream will generate RDDs); must be a multiple of this DStream's batching interval
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#createRDDWithLocalProperties\[U\]\(time:org.apache.spark.streaming.Time,displayInnerRDDOps:Boolean\)\(body:=>U\):U "Permalink") def createRDDWithLocalProperties[U](time: [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time"), displayInnerRDDOps: Boolean)(body: => U): U
Wrap a body of code such that the call site and operation scope information are passed to the RDDs created in this body properly.
Wrap a body of code such that the call site and operation scope information are passed to the RDDs created in this body properly. 

time
    
Current batch time that should be embedded in the scope names 

displayInnerRDDOps
    
Whether the detailed callsites and scopes of the inner RDDs generated by `body` will be displayed in the UI; only the scope and callsite of the DStream operation that generated `this` will be displayed. 

body
    
RDD creation code to execute with certain local properties. 

Attributes
    protected[[streaming](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/index.html "org.apache.spark.streaming")] 
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#equals\(x$1:Object\):Boolean "Permalink") def equals(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef → Any
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#filter\(filterFunc:T=>Boolean\):org.apache.spark.streaming.dstream.DStream\[T\] "Permalink") def filter(filterFunc: (T) => Boolean): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[T]
Return a new DStream containing only the elements that satisfy a predicate.
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#flatMap\[U\]\(flatMapFunc:T=>IterableOnce\[U\]\)\(implicitevidence$3:scala.reflect.ClassTag\[U\]\):org.apache.spark.streaming.dstream.DStream\[U\] "Permalink") def flatMap[U](flatMapFunc: (T) => IterableOnce[U])(implicit arg0: ClassTag[U]): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[U]
Return a new DStream by applying a function to all elements of this DStream, and then flattening the results 
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#foreachRDD\(foreachFunc:\(org.apache.spark.rdd.RDD\[T\],org.apache.spark.streaming.Time\)=>Unit\):Unit "Permalink") def foreachRDD(foreachFunc: ([RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[T], [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time")) => Unit): Unit
Apply a function to each RDD in this DStream.
Apply a function to each RDD in this DStream. This is an output operator, so 'this' DStream will be registered as an output stream and therefore materialized. 
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#foreachRDD\(foreachFunc:org.apache.spark.rdd.RDD\[T\]=>Unit\):Unit "Permalink") def foreachRDD(foreachFunc: ([RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[T]) => Unit): Unit
Apply a function to each RDD in this DStream.
Apply a function to each RDD in this DStream. This is an output operator, so 'this' DStream will be registered as an output stream and therefore materialized. 
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef] 

Definition Classes
    AnyRef → Any 

Annotations
     @IntrinsicCandidate() @native()
  23. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#glom\(\):org.apache.spark.streaming.dstream.DStream\[Array\[T\]\] "Permalink") def glom(): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[Array[T]]
Return a new DStream in which each RDD is generated by applying glom() to each RDD of this DStream.
Return a new DStream in which each RDD is generated by applying glom() to each RDD of this DStream. Applying glom() to an RDD coalesces all elements within each partition into an array. 
  24. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#hashCode\(\):Int "Permalink") def hashCode(): Int 

Definition Classes
    AnyRef → Any 

Annotations
     @IntrinsicCandidate() @native()
  25. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#initializeLogIfNecessary\(isInterpreter:Boolean,silent:Boolean\):Boolean "Permalink") def initializeLogIfNecessary(isInterpreter: Boolean, silent: Boolean): Boolean 

Attributes
    protected  

Definition Classes
    Logging
  26. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#initializeLogIfNecessary\(isInterpreter:Boolean\):Unit "Permalink") def initializeLogIfNecessary(isInterpreter: Boolean): Unit 

Attributes
    protected  

Definition Classes
    Logging
  27. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean 

Definition Classes
    Any
  28. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#isTraceEnabled\(\):Boolean "Permalink") def isTraceEnabled(): Boolean 

Attributes
    protected  

Definition Classes
    Logging
  29. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#log:org.slf4j.Logger "Permalink") def log: Logger 

Attributes
    protected  

Definition Classes
    Logging
  30. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#logBasedOnLevel\(level:org.slf4j.event.Level\)\(f:=>org.apache.spark.internal.MessageWithContext\):Unit "Permalink") def logBasedOnLevel(level: Level)(f: => MessageWithContext): Unit 

Attributes
    protected  

Definition Classes
    Logging
  31. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#logDebug\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logDebug(msg: => String, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  32. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#logDebug\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logDebug(entry: LogEntry, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  33. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#logDebug\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logDebug(entry: LogEntry): Unit 

Attributes
    protected  

Definition Classes
    Logging
  34. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#logDebug\(msg:=>String\):Unit "Permalink") def logDebug(msg: => String): Unit 

Attributes
    protected  

Definition Classes
    Logging
  35. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#logError\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logError(msg: => String, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  36. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#logError\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logError(entry: LogEntry, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  37. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#logError\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logError(entry: LogEntry): Unit 

Attributes
    protected  

Definition Classes
    Logging
  38. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#logError\(msg:=>String\):Unit "Permalink") def logError(msg: => String): Unit 

Attributes
    protected  

Definition Classes
    Logging
  39. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#logInfo\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logInfo(msg: => String, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  40. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#logInfo\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logInfo(entry: LogEntry, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  41. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#logInfo\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logInfo(entry: LogEntry): Unit 

Attributes
    protected  

Definition Classes
    Logging
  42. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#logInfo\(msg:=>String\):Unit "Permalink") def logInfo(msg: => String): Unit 

Attributes
    protected  

Definition Classes
    Logging
  43. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#logName:String "Permalink") def logName: [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String") 

Attributes
    protected  

Definition Classes
    Logging
  44. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#logTrace\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logTrace(msg: => String, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  45. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#logTrace\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logTrace(entry: LogEntry, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  46. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#logTrace\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logTrace(entry: LogEntry): Unit 

Attributes
    protected  

Definition Classes
    Logging
  47. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#logTrace\(msg:=>String\):Unit "Permalink") def logTrace(msg: => String): Unit 

Attributes
    protected  

Definition Classes
    Logging
  48. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#logWarning\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logWarning(msg: => String, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  49. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#logWarning\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logWarning(entry: LogEntry, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  50. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#logWarning\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logWarning(entry: LogEntry): Unit 

Attributes
    protected  

Definition Classes
    Logging
  51. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#logWarning\(msg:=>String\):Unit "Permalink") def logWarning(msg: => String): Unit 

Attributes
    protected  

Definition Classes
    Logging
  52. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#map\[U\]\(mapFunc:T=>U\)\(implicitevidence$2:scala.reflect.ClassTag\[U\]\):org.apache.spark.streaming.dstream.DStream\[U\] "Permalink") def map[U](mapFunc: (T) => U)(implicit arg0: ClassTag[U]): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[U]
Return a new DStream by applying a function to all elements of this DStream.
  53. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#mapPartitions\[U\]\(mapPartFunc:Iterator\[T\]=>Iterator\[U\],preservePartitioning:Boolean\)\(implicitevidence$4:scala.reflect.ClassTag\[U\]\):org.apache.spark.streaming.dstream.DStream\[U\] "Permalink") def mapPartitions[U](mapPartFunc: (Iterator[T]) => Iterator[U], preservePartitioning: Boolean = false)(implicit arg0: ClassTag[U]): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[U]
Return a new DStream in which each RDD is generated by applying mapPartitions() to each RDDs of this DStream.
Return a new DStream in which each RDD is generated by applying mapPartitions() to each RDDs of this DStream. Applying mapPartitions() to an RDD applies a function to each partition of the RDD. 
  54. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  55. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#notify\(\):Unit "Permalink") final  def notify(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  56. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  57. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#persist\(\):org.apache.spark.streaming.dstream.DStream\[T\] "Permalink") def persist(): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[T]
Persist RDDs of this DStream with the default storage level (MEMORY_ONLY_SER)
  58. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#persist\(level:org.apache.spark.storage.StorageLevel\):org.apache.spark.streaming.dstream.DStream\[T\] "Permalink") def persist(level: [StorageLevel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StorageLevel.html "org.apache.spark.storage.StorageLevel")): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[T]
Persist the RDDs of this DStream with the given storage level
  59. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#print\(num:Int\):Unit "Permalink") def print(num: Int): Unit
Print the first num elements of each RDD generated in this DStream.
Print the first num elements of each RDD generated in this DStream. This is an output operator, so this DStream will be registered as an output stream and there materialized. 
  60. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#print\(\):Unit "Permalink") def print(): Unit
Print the first ten elements of each RDD generated in this DStream.
Print the first ten elements of each RDD generated in this DStream. This is an output operator, so this DStream will be registered as an output stream and there materialized. 
  61. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#reduce\(reduceFunc:\(T,T\)=>T\):org.apache.spark.streaming.dstream.DStream\[T\] "Permalink") def reduce(reduceFunc: (T, T) => T): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[T]
Return a new DStream in which each RDD has a single element generated by reducing each RDD of this DStream.
  62. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#reduceByWindow\(reduceFunc:\(T,T\)=>T,invReduceFunc:\(T,T\)=>T,windowDuration:org.apache.spark.streaming.Duration,slideDuration:org.apache.spark.streaming.Duration\):org.apache.spark.streaming.dstream.DStream\[T\] "Permalink") def reduceByWindow(reduceFunc: (T, T) => T, invReduceFunc: (T, T) => T, windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration")): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[T]
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
  63. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#reduceByWindow\(reduceFunc:\(T,T\)=>T,windowDuration:org.apache.spark.streaming.Duration,slideDuration:org.apache.spark.streaming.Duration\):org.apache.spark.streaming.dstream.DStream\[T\] "Permalink") def reduceByWindow(reduceFunc: (T, T) => T, windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration")): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[T]
Return a new DStream in which each RDD has a single element generated by reducing all elements in a sliding window over this DStream.
Return a new DStream in which each RDD has a single element generated by reducing all elements in a sliding window over this DStream. 

reduceFunc
    
associative and commutative reduce function 

windowDuration
    
width of the window; must be a multiple of this DStream's batching interval 

slideDuration
    
sliding interval of the window (i.e., the interval after which the new DStream will generate RDDs); must be a multiple of this DStream's batching interval
  64. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#repartition\(numPartitions:Int\):org.apache.spark.streaming.dstream.DStream\[T\] "Permalink") def repartition(numPartitions: Int): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[T]
Return a new DStream with an increased or decreased level of parallelism.
Return a new DStream with an increased or decreased level of parallelism. Each RDD in the returned DStream has exactly numPartitions partitions. 
  65. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#saveAsObjectFiles\(prefix:String,suffix:String\):Unit "Permalink") def saveAsObjectFiles(prefix: String, suffix: String = ""): Unit
Save each RDD in this DStream as a Sequence file of serialized objects.
Save each RDD in this DStream as a Sequence file of serialized objects. The file name at each batch interval is generated based on `prefix` and `suffix`: "prefix-TIME_IN_MS.suffix". 
  66. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#saveAsTextFiles\(prefix:String,suffix:String\):Unit "Permalink") def saveAsTextFiles(prefix: String, suffix: String = ""): Unit
Save each RDD in this DStream as at text file, using string representation of elements.
Save each RDD in this DStream as at text file, using string representation of elements. The file name at each batch interval is generated based on `prefix` and `suffix`: "prefix-TIME_IN_MS.suffix". 
  67. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#slice\(fromTime:org.apache.spark.streaming.Time,toTime:org.apache.spark.streaming.Time\):Seq\[org.apache.spark.rdd.RDD\[T\]\] "Permalink") def slice(fromTime: [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time"), toTime: [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time")): Seq[[RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[T]]
Return all the RDDs between 'fromTime' to 'toTime' (both included) 
  68. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#slice\(interval:org.apache.spark.streaming.Interval\):Seq\[org.apache.spark.rdd.RDD\[T\]\] "Permalink") def slice(interval: Interval): Seq[[RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[T]]
Return all the RDDs defined by the Interval object (both end times included) 
  69. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0 

Definition Classes
    AnyRef
  70. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#toString\(\):String "Permalink") def toString(): [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String") 

Definition Classes
    AnyRef → Any
  71. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#transform\[U\]\(transformFunc:\(org.apache.spark.rdd.RDD\[T\],org.apache.spark.streaming.Time\)=>org.apache.spark.rdd.RDD\[U\]\)\(implicitevidence$6:scala.reflect.ClassTag\[U\]\):org.apache.spark.streaming.dstream.DStream\[U\] "Permalink") def transform[U](transformFunc: ([RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[T], [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time")) => [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[U])(implicit arg0: ClassTag[U]): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[U]
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream.
  72. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#transform\[U\]\(transformFunc:org.apache.spark.rdd.RDD\[T\]=>org.apache.spark.rdd.RDD\[U\]\)\(implicitevidence$5:scala.reflect.ClassTag\[U\]\):org.apache.spark.streaming.dstream.DStream\[U\] "Permalink") def transform[U](transformFunc: ([RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[T]) => [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[U])(implicit arg0: ClassTag[U]): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[U]
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream.
  73. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#transformWith\[U,V\]\(other:org.apache.spark.streaming.dstream.DStream\[U\],transformFunc:\(org.apache.spark.rdd.RDD\[T\],org.apache.spark.rdd.RDD\[U\],org.apache.spark.streaming.Time\)=>org.apache.spark.rdd.RDD\[V\]\)\(implicitevidence$9:scala.reflect.ClassTag\[U\],implicitevidence$10:scala.reflect.ClassTag\[V\]\):org.apache.spark.streaming.dstream.DStream\[V\] "Permalink") def transformWith[U, V](other: [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[U], transformFunc: ([RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[T], [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[U], [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time")) => [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[V])(implicit arg0: ClassTag[U], arg1: ClassTag[V]): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[V]
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream and 'other' DStream.
  74. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#transformWith\[U,V\]\(other:org.apache.spark.streaming.dstream.DStream\[U\],transformFunc:\(org.apache.spark.rdd.RDD\[T\],org.apache.spark.rdd.RDD\[U\]\)=>org.apache.spark.rdd.RDD\[V\]\)\(implicitevidence$7:scala.reflect.ClassTag\[U\],implicitevidence$8:scala.reflect.ClassTag\[V\]\):org.apache.spark.streaming.dstream.DStream\[V\] "Permalink") def transformWith[U, V](other: [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[U], transformFunc: ([RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[T], [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[U]) => [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[V])(implicit arg0: ClassTag[U], arg1: ClassTag[V]): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[V]
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream and 'other' DStream.
  75. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#union\(that:org.apache.spark.streaming.dstream.DStream\[T\]\):org.apache.spark.streaming.dstream.DStream\[T\] "Permalink") def union(that: [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[T]): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[T]
Return a new DStream by unifying data of another DStream with this DStream.
Return a new DStream by unifying data of another DStream with this DStream. 

that
    
Another DStream having the same slideDuration as this DStream.
  76. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  77. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  78. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#wait\(\):Unit "Permalink") final  def wait(): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  79. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#window\(windowDuration:org.apache.spark.streaming.Duration,slideDuration:org.apache.spark.streaming.Duration\):org.apache.spark.streaming.dstream.DStream\[T\] "Permalink") def window(windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration")): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[T]
Return a new DStream in which each RDD contains all the elements in seen in a sliding window of time over this DStream.
Return a new DStream in which each RDD contains all the elements in seen in a sliding window of time over this DStream. 

windowDuration
    
width of the window; must be a multiple of this DStream's batching interval 

slideDuration
    
sliding interval of the window (i.e., the interval after which the new DStream will generate RDDs); must be a multiple of this DStream's batching interval
  80. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#window\(windowDuration:org.apache.spark.streaming.Duration\):org.apache.spark.streaming.dstream.DStream\[T\] "Permalink") def window(windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration")): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[T]
Return a new DStream in which each RDD contains all the elements in seen in a sliding window of time over this DStream.
Return a new DStream in which each RDD contains all the elements in seen in a sliding window of time over this DStream. The new DStream generates RDDs with the same interval as this DStream. 

windowDuration
    
width of the window; must be a multiple of this DStream's interval.
  81. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#withLogContext\(context:java.util.Map\[String,String\]\)\(body:=>Unit\):Unit "Permalink") def withLogContext(context: [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#java.util.Map "java.util.Map")[String, String])(body: => Unit): Unit 

Attributes
    protected  

Definition Classes
    Logging


### Deprecated Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#finalize\(\):Unit "Permalink") def finalize(): Unit 

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
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#MDC\(key:org.apache.spark.internal.LogKey,value:Any\):org.apache.spark.internal.MDC "Permalink") def MDC(key: LogKey, value: Any): MDC 

Attributes
    protected  

Definition Classes
    Logging
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#initializeLogIfNecessary\(isInterpreter:Boolean,silent:Boolean\):Boolean "Permalink") def initializeLogIfNecessary(isInterpreter: Boolean, silent: Boolean): Boolean 

Attributes
    protected  

Definition Classes
    Logging
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#initializeLogIfNecessary\(isInterpreter:Boolean\):Unit "Permalink") def initializeLogIfNecessary(isInterpreter: Boolean): Unit 

Attributes
    protected  

Definition Classes
    Logging
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#isTraceEnabled\(\):Boolean "Permalink") def isTraceEnabled(): Boolean 

Attributes
    protected  

Definition Classes
    Logging
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#log:org.slf4j.Logger "Permalink") def log: Logger 

Attributes
    protected  

Definition Classes
    Logging
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#logBasedOnLevel\(level:org.slf4j.event.Level\)\(f:=>org.apache.spark.internal.MessageWithContext\):Unit "Permalink") def logBasedOnLevel(level: Level)(f: => MessageWithContext): Unit 

Attributes
    protected  

Definition Classes
    Logging
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#logDebug\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logDebug(msg: => String, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#logDebug\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logDebug(entry: LogEntry, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#logDebug\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logDebug(entry: LogEntry): Unit 

Attributes
    protected  

Definition Classes
    Logging
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#logDebug\(msg:=>String\):Unit "Permalink") def logDebug(msg: => String): Unit 

Attributes
    protected  

Definition Classes
    Logging
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#logError\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logError(msg: => String, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#logError\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logError(entry: LogEntry, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#logError\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logError(entry: LogEntry): Unit 

Attributes
    protected  

Definition Classes
    Logging
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#logError\(msg:=>String\):Unit "Permalink") def logError(msg: => String): Unit 

Attributes
    protected  

Definition Classes
    Logging
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#logInfo\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logInfo(msg: => String, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#logInfo\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logInfo(entry: LogEntry, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#logInfo\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logInfo(entry: LogEntry): Unit 

Attributes
    protected  

Definition Classes
    Logging
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#logInfo\(msg:=>String\):Unit "Permalink") def logInfo(msg: => String): Unit 

Attributes
    protected  

Definition Classes
    Logging
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#logName:String "Permalink") def logName: [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String") 

Attributes
    protected  

Definition Classes
    Logging
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#logTrace\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logTrace(msg: => String, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#logTrace\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logTrace(entry: LogEntry, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#logTrace\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logTrace(entry: LogEntry): Unit 

Attributes
    protected  

Definition Classes
    Logging
  23. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#logTrace\(msg:=>String\):Unit "Permalink") def logTrace(msg: => String): Unit 

Attributes
    protected  

Definition Classes
    Logging
  24. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#logWarning\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logWarning(msg: => String, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  25. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#logWarning\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logWarning(entry: LogEntry, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  26. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#logWarning\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logWarning(entry: LogEntry): Unit 

Attributes
    protected  

Definition Classes
    Logging
  27. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#logWarning\(msg:=>String\):Unit "Permalink") def logWarning(msg: => String): Unit 

Attributes
    protected  

Definition Classes
    Logging
  28. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#withLogContext\(context:java.util.Map\[String,String\]\)\(body:=>Unit\):Unit "Permalink") def withLogContext(context: [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#java.util.Map "java.util.Map")[String, String])(body: => Unit): Unit 

Attributes
    protected  

Definition Classes
    Logging


### Inherited from AnyRef
### Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html###:Int "Permalink") final  def ##: Int 

Definition Classes
    AnyRef → Any
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#clone\(\):Object "Permalink") def clone(): AnyRef 

Attributes
    protected[lang]  

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#equals\(x$1:Object\):Boolean "Permalink") def equals(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef → Any
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef] 

Definition Classes
    AnyRef → Any 

Annotations
     @IntrinsicCandidate() @native()
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#hashCode\(\):Int "Permalink") def hashCode(): Int 

Definition Classes
    AnyRef → Any 

Annotations
     @IntrinsicCandidate() @native()
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#notify\(\):Unit "Permalink") final  def notify(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0 

Definition Classes
    AnyRef
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#toString\(\):String "Permalink") def toString(): [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String") 

Definition Classes
    AnyRef → Any
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#wait\(\):Unit "Permalink") final  def wait(): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#finalize\(\):Unit "Permalink") def finalize(): Unit 

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
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0 

Definition Classes
    Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean 

Definition Classes
    Any


### Ungrouped
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#LogStringContextextendsAnyRef "Permalink") implicit  class LogStringContext extends AnyRef 

Definition Classes
    Logging


  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#compute\(validTime:org.apache.spark.streaming.Time\):Option\[org.apache.spark.rdd.RDD\[T\]\] "Permalink") abstract  def compute(validTime: [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time")): Option[[RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[T]]
Method that generates an RDD for the given time
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#dependencies:List\[org.apache.spark.streaming.dstream.DStream\[_\]\] "Permalink") abstract  def dependencies: List[[DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[_]]
List of parent DStreams on which this DStream depends on
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#slideDuration:org.apache.spark.streaming.Duration "Permalink") abstract  def slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration")
Time interval after which the DStream generates an RDD
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html###:Int "Permalink") final  def ##: Int 

Definition Classes
    AnyRef → Any
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#MDC\(key:org.apache.spark.internal.LogKey,value:Any\):org.apache.spark.internal.MDC "Permalink") def MDC(key: LogKey, value: Any): MDC 

Attributes
    protected  

Definition Classes
    Logging
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0 

Definition Classes
    Any
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#baseScope:Option\[String\] "Permalink") val baseScope: Option[String]
The base scope associated with the operation that created this DStream.
The base scope associated with the operation that created this DStream.
This is the medium through which we pass the DStream operation name (e.g. updatedStateByKey) to the RDDs created by this DStream. Note that we never use this scope directly in RDDs. Instead, we instantiate a new scope during each call to `compute` based on this one.
This is not defined if the DStream is created outside of one of the public DStream operations.  

Attributes
    protected[[streaming](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/index.html "org.apache.spark.streaming")] 
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#cache\(\):org.apache.spark.streaming.dstream.DStream\[T\] "Permalink") def cache(): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[T]
Persist RDDs of this DStream with the default storage level (MEMORY_ONLY_SER)
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#checkpoint\(interval:org.apache.spark.streaming.Duration\):org.apache.spark.streaming.dstream.DStream\[T\] "Permalink") def checkpoint(interval: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration")): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[T]
Enable periodic checkpointing of RDDs of this DStream
Enable periodic checkpointing of RDDs of this DStream 

interval
    
Time interval after which generated RDD will be checkpointed
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#clone\(\):Object "Permalink") def clone(): AnyRef 

Attributes
    protected[lang]  

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#context:org.apache.spark.streaming.StreamingContext "Permalink") def context: [StreamingContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html "org.apache.spark.streaming.StreamingContext")
Return the StreamingContext associated with this DStream
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#count\(\):org.apache.spark.streaming.dstream.DStream\[Long\] "Permalink") def count(): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[Long]
Return a new DStream in which each RDD has a single element generated by counting each RDD of this DStream.
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#countByValue\(numPartitions:Int\)\(implicitord:Ordering\[T\]\):org.apache.spark.streaming.dstream.DStream\[\(T,Long\)\] "Permalink") def countByValue(numPartitions: Int = [ssc.sc.defaultParallelism](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#defaultParallelism:Int))(implicit ord: Ordering[T] = null): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(T, Long)]
Return a new DStream in which each RDD contains the counts of each distinct value in each RDD of this DStream.
Return a new DStream in which each RDD contains the counts of each distinct value in each RDD of this DStream. Hash partitioning is used to generate the RDDs with `numPartitions` partitions (Spark's default number of partitions if `numPartitions` not specified). 
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#countByValueAndWindow\(windowDuration:org.apache.spark.streaming.Duration,slideDuration:org.apache.spark.streaming.Duration,numPartitions:Int\)\(implicitord:Ordering\[T\]\):org.apache.spark.streaming.dstream.DStream\[\(T,Long\)\] "Permalink") def countByValueAndWindow(windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), numPartitions: Int = [ssc.sc.defaultParallelism](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html#defaultParallelism:Int))(implicit ord: Ordering[T] = null): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[(T, Long)]
Return a new DStream in which each RDD contains the count of distinct elements in RDDs in a sliding window over this DStream.
Return a new DStream in which each RDD contains the count of distinct elements in RDDs in a sliding window over this DStream. Hash partitioning is used to generate the RDDs with `numPartitions` partitions (Spark's default number of partitions if `numPartitions` not specified). 

windowDuration
    
width of the window; must be a multiple of this DStream's batching interval 

slideDuration
    
sliding interval of the window (i.e., the interval after which the new DStream will generate RDDs); must be a multiple of this DStream's batching interval 

numPartitions
    
number of partitions of each RDD in the new DStream.
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#countByWindow\(windowDuration:org.apache.spark.streaming.Duration,slideDuration:org.apache.spark.streaming.Duration\):org.apache.spark.streaming.dstream.DStream\[Long\] "Permalink") def countByWindow(windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration")): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[Long]
Return a new DStream in which each RDD has a single element generated by counting the number of elements in a sliding window over this DStream.
Return a new DStream in which each RDD has a single element generated by counting the number of elements in a sliding window over this DStream. Hash partitioning is used to generate the RDDs with Spark's default number of partitions. 

windowDuration
    
width of the window; must be a multiple of this DStream's batching interval 

slideDuration
    
sliding interval of the window (i.e., the interval after which the new DStream will generate RDDs); must be a multiple of this DStream's batching interval
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#createRDDWithLocalProperties\[U\]\(time:org.apache.spark.streaming.Time,displayInnerRDDOps:Boolean\)\(body:=>U\):U "Permalink") def createRDDWithLocalProperties[U](time: [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time"), displayInnerRDDOps: Boolean)(body: => U): U
Wrap a body of code such that the call site and operation scope information are passed to the RDDs created in this body properly.
Wrap a body of code such that the call site and operation scope information are passed to the RDDs created in this body properly. 

time
    
Current batch time that should be embedded in the scope names 

displayInnerRDDOps
    
Whether the detailed callsites and scopes of the inner RDDs generated by `body` will be displayed in the UI; only the scope and callsite of the DStream operation that generated `this` will be displayed. 

body
    
RDD creation code to execute with certain local properties. 

Attributes
    protected[[streaming](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/index.html "org.apache.spark.streaming")] 
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#equals\(x$1:Object\):Boolean "Permalink") def equals(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef → Any
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#filter\(filterFunc:T=>Boolean\):org.apache.spark.streaming.dstream.DStream\[T\] "Permalink") def filter(filterFunc: (T) => Boolean): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[T]
Return a new DStream containing only the elements that satisfy a predicate.
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#flatMap\[U\]\(flatMapFunc:T=>IterableOnce\[U\]\)\(implicitevidence$3:scala.reflect.ClassTag\[U\]\):org.apache.spark.streaming.dstream.DStream\[U\] "Permalink") def flatMap[U](flatMapFunc: (T) => IterableOnce[U])(implicit arg0: ClassTag[U]): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[U]
Return a new DStream by applying a function to all elements of this DStream, and then flattening the results 
  23. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#foreachRDD\(foreachFunc:\(org.apache.spark.rdd.RDD\[T\],org.apache.spark.streaming.Time\)=>Unit\):Unit "Permalink") def foreachRDD(foreachFunc: ([RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[T], [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time")) => Unit): Unit
Apply a function to each RDD in this DStream.
Apply a function to each RDD in this DStream. This is an output operator, so 'this' DStream will be registered as an output stream and therefore materialized. 
  24. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#foreachRDD\(foreachFunc:org.apache.spark.rdd.RDD\[T\]=>Unit\):Unit "Permalink") def foreachRDD(foreachFunc: ([RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[T]) => Unit): Unit
Apply a function to each RDD in this DStream.
Apply a function to each RDD in this DStream. This is an output operator, so 'this' DStream will be registered as an output stream and therefore materialized. 
  25. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef] 

Definition Classes
    AnyRef → Any 

Annotations
     @IntrinsicCandidate() @native()
  26. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#glom\(\):org.apache.spark.streaming.dstream.DStream\[Array\[T\]\] "Permalink") def glom(): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[Array[T]]
Return a new DStream in which each RDD is generated by applying glom() to each RDD of this DStream.
Return a new DStream in which each RDD is generated by applying glom() to each RDD of this DStream. Applying glom() to an RDD coalesces all elements within each partition into an array. 
  27. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#hashCode\(\):Int "Permalink") def hashCode(): Int 

Definition Classes
    AnyRef → Any 

Annotations
     @IntrinsicCandidate() @native()
  28. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#initializeLogIfNecessary\(isInterpreter:Boolean,silent:Boolean\):Boolean "Permalink") def initializeLogIfNecessary(isInterpreter: Boolean, silent: Boolean): Boolean 

Attributes
    protected  

Definition Classes
    Logging
  29. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#initializeLogIfNecessary\(isInterpreter:Boolean\):Unit "Permalink") def initializeLogIfNecessary(isInterpreter: Boolean): Unit 

Attributes
    protected  

Definition Classes
    Logging
  30. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean 

Definition Classes
    Any
  31. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#isTraceEnabled\(\):Boolean "Permalink") def isTraceEnabled(): Boolean 

Attributes
    protected  

Definition Classes
    Logging
  32. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#log:org.slf4j.Logger "Permalink") def log: Logger 

Attributes
    protected  

Definition Classes
    Logging
  33. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#logBasedOnLevel\(level:org.slf4j.event.Level\)\(f:=>org.apache.spark.internal.MessageWithContext\):Unit "Permalink") def logBasedOnLevel(level: Level)(f: => MessageWithContext): Unit 

Attributes
    protected  

Definition Classes
    Logging
  34. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#logDebug\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logDebug(msg: => String, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  35. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#logDebug\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logDebug(entry: LogEntry, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  36. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#logDebug\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logDebug(entry: LogEntry): Unit 

Attributes
    protected  

Definition Classes
    Logging
  37. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#logDebug\(msg:=>String\):Unit "Permalink") def logDebug(msg: => String): Unit 

Attributes
    protected  

Definition Classes
    Logging
  38. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#logError\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logError(msg: => String, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  39. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#logError\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logError(entry: LogEntry, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  40. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#logError\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logError(entry: LogEntry): Unit 

Attributes
    protected  

Definition Classes
    Logging
  41. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#logError\(msg:=>String\):Unit "Permalink") def logError(msg: => String): Unit 

Attributes
    protected  

Definition Classes
    Logging
  42. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#logInfo\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logInfo(msg: => String, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  43. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#logInfo\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logInfo(entry: LogEntry, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  44. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#logInfo\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logInfo(entry: LogEntry): Unit 

Attributes
    protected  

Definition Classes
    Logging
  45. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#logInfo\(msg:=>String\):Unit "Permalink") def logInfo(msg: => String): Unit 

Attributes
    protected  

Definition Classes
    Logging
  46. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#logName:String "Permalink") def logName: [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String") 

Attributes
    protected  

Definition Classes
    Logging
  47. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#logTrace\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logTrace(msg: => String, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  48. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#logTrace\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logTrace(entry: LogEntry, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  49. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#logTrace\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logTrace(entry: LogEntry): Unit 

Attributes
    protected  

Definition Classes
    Logging
  50. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#logTrace\(msg:=>String\):Unit "Permalink") def logTrace(msg: => String): Unit 

Attributes
    protected  

Definition Classes
    Logging
  51. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#logWarning\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logWarning(msg: => String, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  52. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#logWarning\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logWarning(entry: LogEntry, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  53. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#logWarning\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logWarning(entry: LogEntry): Unit 

Attributes
    protected  

Definition Classes
    Logging
  54. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#logWarning\(msg:=>String\):Unit "Permalink") def logWarning(msg: => String): Unit 

Attributes
    protected  

Definition Classes
    Logging
  55. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#map\[U\]\(mapFunc:T=>U\)\(implicitevidence$2:scala.reflect.ClassTag\[U\]\):org.apache.spark.streaming.dstream.DStream\[U\] "Permalink") def map[U](mapFunc: (T) => U)(implicit arg0: ClassTag[U]): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[U]
Return a new DStream by applying a function to all elements of this DStream.
  56. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#mapPartitions\[U\]\(mapPartFunc:Iterator\[T\]=>Iterator\[U\],preservePartitioning:Boolean\)\(implicitevidence$4:scala.reflect.ClassTag\[U\]\):org.apache.spark.streaming.dstream.DStream\[U\] "Permalink") def mapPartitions[U](mapPartFunc: (Iterator[T]) => Iterator[U], preservePartitioning: Boolean = false)(implicit arg0: ClassTag[U]): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[U]
Return a new DStream in which each RDD is generated by applying mapPartitions() to each RDDs of this DStream.
Return a new DStream in which each RDD is generated by applying mapPartitions() to each RDDs of this DStream. Applying mapPartitions() to an RDD applies a function to each partition of the RDD. 
  57. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  58. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#notify\(\):Unit "Permalink") final  def notify(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  59. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  60. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#persist\(\):org.apache.spark.streaming.dstream.DStream\[T\] "Permalink") def persist(): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[T]
Persist RDDs of this DStream with the default storage level (MEMORY_ONLY_SER)
  61. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#persist\(level:org.apache.spark.storage.StorageLevel\):org.apache.spark.streaming.dstream.DStream\[T\] "Permalink") def persist(level: [StorageLevel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StorageLevel.html "org.apache.spark.storage.StorageLevel")): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[T]
Persist the RDDs of this DStream with the given storage level
  62. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#print\(num:Int\):Unit "Permalink") def print(num: Int): Unit
Print the first num elements of each RDD generated in this DStream.
Print the first num elements of each RDD generated in this DStream. This is an output operator, so this DStream will be registered as an output stream and there materialized. 
  63. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#print\(\):Unit "Permalink") def print(): Unit
Print the first ten elements of each RDD generated in this DStream.
Print the first ten elements of each RDD generated in this DStream. This is an output operator, so this DStream will be registered as an output stream and there materialized. 
  64. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#reduce\(reduceFunc:\(T,T\)=>T\):org.apache.spark.streaming.dstream.DStream\[T\] "Permalink") def reduce(reduceFunc: (T, T) => T): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[T]
Return a new DStream in which each RDD has a single element generated by reducing each RDD of this DStream.
  65. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#reduceByWindow\(reduceFunc:\(T,T\)=>T,invReduceFunc:\(T,T\)=>T,windowDuration:org.apache.spark.streaming.Duration,slideDuration:org.apache.spark.streaming.Duration\):org.apache.spark.streaming.dstream.DStream\[T\] "Permalink") def reduceByWindow(reduceFunc: (T, T) => T, invReduceFunc: (T, T) => T, windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration")): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[T]
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
  66. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#reduceByWindow\(reduceFunc:\(T,T\)=>T,windowDuration:org.apache.spark.streaming.Duration,slideDuration:org.apache.spark.streaming.Duration\):org.apache.spark.streaming.dstream.DStream\[T\] "Permalink") def reduceByWindow(reduceFunc: (T, T) => T, windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration")): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[T]
Return a new DStream in which each RDD has a single element generated by reducing all elements in a sliding window over this DStream.
Return a new DStream in which each RDD has a single element generated by reducing all elements in a sliding window over this DStream. 

reduceFunc
    
associative and commutative reduce function 

windowDuration
    
width of the window; must be a multiple of this DStream's batching interval 

slideDuration
    
sliding interval of the window (i.e., the interval after which the new DStream will generate RDDs); must be a multiple of this DStream's batching interval
  67. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#repartition\(numPartitions:Int\):org.apache.spark.streaming.dstream.DStream\[T\] "Permalink") def repartition(numPartitions: Int): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[T]
Return a new DStream with an increased or decreased level of parallelism.
Return a new DStream with an increased or decreased level of parallelism. Each RDD in the returned DStream has exactly numPartitions partitions. 
  68. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#saveAsObjectFiles\(prefix:String,suffix:String\):Unit "Permalink") def saveAsObjectFiles(prefix: String, suffix: String = ""): Unit
Save each RDD in this DStream as a Sequence file of serialized objects.
Save each RDD in this DStream as a Sequence file of serialized objects. The file name at each batch interval is generated based on `prefix` and `suffix`: "prefix-TIME_IN_MS.suffix". 
  69. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#saveAsTextFiles\(prefix:String,suffix:String\):Unit "Permalink") def saveAsTextFiles(prefix: String, suffix: String = ""): Unit
Save each RDD in this DStream as at text file, using string representation of elements.
Save each RDD in this DStream as at text file, using string representation of elements. The file name at each batch interval is generated based on `prefix` and `suffix`: "prefix-TIME_IN_MS.suffix". 
  70. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#slice\(fromTime:org.apache.spark.streaming.Time,toTime:org.apache.spark.streaming.Time\):Seq\[org.apache.spark.rdd.RDD\[T\]\] "Permalink") def slice(fromTime: [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time"), toTime: [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time")): Seq[[RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[T]]
Return all the RDDs between 'fromTime' to 'toTime' (both included) 
  71. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#slice\(interval:org.apache.spark.streaming.Interval\):Seq\[org.apache.spark.rdd.RDD\[T\]\] "Permalink") def slice(interval: Interval): Seq[[RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[T]]
Return all the RDDs defined by the Interval object (both end times included) 
  72. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0 

Definition Classes
    AnyRef
  73. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#toString\(\):String "Permalink") def toString(): [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String") 

Definition Classes
    AnyRef → Any
  74. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#transform\[U\]\(transformFunc:\(org.apache.spark.rdd.RDD\[T\],org.apache.spark.streaming.Time\)=>org.apache.spark.rdd.RDD\[U\]\)\(implicitevidence$6:scala.reflect.ClassTag\[U\]\):org.apache.spark.streaming.dstream.DStream\[U\] "Permalink") def transform[U](transformFunc: ([RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[T], [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time")) => [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[U])(implicit arg0: ClassTag[U]): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[U]
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream.
  75. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#transform\[U\]\(transformFunc:org.apache.spark.rdd.RDD\[T\]=>org.apache.spark.rdd.RDD\[U\]\)\(implicitevidence$5:scala.reflect.ClassTag\[U\]\):org.apache.spark.streaming.dstream.DStream\[U\] "Permalink") def transform[U](transformFunc: ([RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[T]) => [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[U])(implicit arg0: ClassTag[U]): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[U]
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream.
  76. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#transformWith\[U,V\]\(other:org.apache.spark.streaming.dstream.DStream\[U\],transformFunc:\(org.apache.spark.rdd.RDD\[T\],org.apache.spark.rdd.RDD\[U\],org.apache.spark.streaming.Time\)=>org.apache.spark.rdd.RDD\[V\]\)\(implicitevidence$9:scala.reflect.ClassTag\[U\],implicitevidence$10:scala.reflect.ClassTag\[V\]\):org.apache.spark.streaming.dstream.DStream\[V\] "Permalink") def transformWith[U, V](other: [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[U], transformFunc: ([RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[T], [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[U], [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time")) => [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[V])(implicit arg0: ClassTag[U], arg1: ClassTag[V]): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[V]
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream and 'other' DStream.
  77. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#transformWith\[U,V\]\(other:org.apache.spark.streaming.dstream.DStream\[U\],transformFunc:\(org.apache.spark.rdd.RDD\[T\],org.apache.spark.rdd.RDD\[U\]\)=>org.apache.spark.rdd.RDD\[V\]\)\(implicitevidence$7:scala.reflect.ClassTag\[U\],implicitevidence$8:scala.reflect.ClassTag\[V\]\):org.apache.spark.streaming.dstream.DStream\[V\] "Permalink") def transformWith[U, V](other: [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[U], transformFunc: ([RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[T], [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[U]) => [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[V])(implicit arg0: ClassTag[U], arg1: ClassTag[V]): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[V]
Return a new DStream in which each RDD is generated by applying a function on each RDD of 'this' DStream and 'other' DStream.
  78. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#union\(that:org.apache.spark.streaming.dstream.DStream\[T\]\):org.apache.spark.streaming.dstream.DStream\[T\] "Permalink") def union(that: [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[T]): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[T]
Return a new DStream by unifying data of another DStream with this DStream.
Return a new DStream by unifying data of another DStream with this DStream. 

that
    
Another DStream having the same slideDuration as this DStream.
  79. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  80. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  81. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#wait\(\):Unit "Permalink") final  def wait(): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  82. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#window\(windowDuration:org.apache.spark.streaming.Duration,slideDuration:org.apache.spark.streaming.Duration\):org.apache.spark.streaming.dstream.DStream\[T\] "Permalink") def window(windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), slideDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration")): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[T]
Return a new DStream in which each RDD contains all the elements in seen in a sliding window of time over this DStream.
Return a new DStream in which each RDD contains all the elements in seen in a sliding window of time over this DStream. 

windowDuration
    
width of the window; must be a multiple of this DStream's batching interval 

slideDuration
    
sliding interval of the window (i.e., the interval after which the new DStream will generate RDDs); must be a multiple of this DStream's batching interval
  83. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#window\(windowDuration:org.apache.spark.streaming.Duration\):org.apache.spark.streaming.dstream.DStream\[T\] "Permalink") def window(windowDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration")): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[T]
Return a new DStream in which each RDD contains all the elements in seen in a sliding window of time over this DStream.
Return a new DStream in which each RDD contains all the elements in seen in a sliding window of time over this DStream. The new DStream generates RDDs with the same interval as this DStream. 

windowDuration
    
width of the window; must be a multiple of this DStream's interval.
  84. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#withLogContext\(context:java.util.Map\[String,String\]\)\(body:=>Unit\):Unit "Permalink") def withLogContext(context: [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#java.util.Map "java.util.Map")[String, String])(body: => Unit): Unit 

Attributes
    protected  

Definition Classes
    Logging
  85. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html#finalize\(\):Unit "Permalink") def finalize(): Unit 

Attributes
    protected[lang]  

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.Throwable]) @Deprecated 

Deprecated
    
_(Since version 9)_


