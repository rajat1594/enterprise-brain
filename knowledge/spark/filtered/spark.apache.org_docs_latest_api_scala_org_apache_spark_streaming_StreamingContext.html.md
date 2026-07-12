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
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/index.html "Permalink") package [dstream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/index.html "Various implementations of DStream's.")
Various implementations of DStream's.
Various implementations of DStream's. 

Definition Classes
    [streaming](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/index.html "org.apache.spark.streaming") 

See also
    
[org.apache.spark.streaming.dstream.DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/kinesis/index.html "Permalink") package [kinesis](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/kinesis/index.html) 

Definition Classes
    [streaming](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/index.html "org.apache.spark.streaming")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/index.html "Permalink") package [receiver](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/index.html) 

Definition Classes
    [streaming](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/index.html "org.apache.spark.streaming")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/index.html "Permalink") package [scheduler](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/index.html) 

Definition Classes
    [streaming](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/index.html "org.apache.spark.streaming")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/util/index.html "Permalink") package [util](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/util/index.html) 

Definition Classes
    [streaming](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/index.html "org.apache.spark.streaming")
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


[c](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext$.html "See companion object")
[org](https://spark.apache.org/docs/latest/api/scala/org/index.html "org").[apache](https://spark.apache.org/docs/latest/api/scala/org/apache/index.html "org.apache").[spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark").[streaming](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/index.html "org.apache.spark.streaming")
#  [StreamingContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext$.html "See companion object")[ __](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html "Permalink")
### 
Companion [object StreamingContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext$.html "See companion object")
####  class StreamingContext extends Logging
Main entry point for Spark Streaming functionality. It provides methods used to create [org.apache.spark.streaming.dstream.DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")s from various input sources. It can be either created by providing a Spark master URL and an appName, or from a org.apache.spark.SparkConf configuration (see core Spark documentation), or from an existing org.apache.spark.SparkContext. The associated SparkContext can be accessed using `context.sparkContext`. After creating and transforming DStreams, the streaming computation can be started and stopped using `context.start()` and `context.stop()`, respectively. `context.awaitTermination()` allows the current thread to wait for the termination of the context by `stop()` or by an exception. 

Annotations
     @deprecated 

Deprecated
    
_(Since version Spark 3.4.0)_ DStream is deprecated. Migrate to Structured Streaming. 

Source
    [StreamingContext.scala](https://github.com/apache/spark/tree/v4.1.2/streaming/src/main/scala/org/apache/spark/streaming/StreamingContext.scala)
Linear Supertypes
Logging, AnyRef, Any
__ __
Ordering
  1. Alphabetic
  2. By Inheritance


Inherited  

  1. StreamingContext
  2. Logging
  3. AnyRef
  4. Any


  1. Hide All
  2. Show All


Visibility
  1. Public
  2. Protected


### Instance Constructors
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#<init>\(path:String,sparkContext:org.apache.spark.SparkContext\):org.apache.spark.streaming.StreamingContext "Permalink") new StreamingContext(path: String, sparkContext: [SparkContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html "org.apache.spark.SparkContext"))
Recreate a StreamingContext from a checkpoint file using an existing SparkContext.
Recreate a StreamingContext from a checkpoint file using an existing SparkContext. 

path
    
Path to the directory that was specified as the checkpoint directory 

sparkContext
    
Existing SparkContext
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#<init>\(path:String\):org.apache.spark.streaming.StreamingContext "Permalink") new StreamingContext(path: String)
Recreate a StreamingContext from a checkpoint file.
Recreate a StreamingContext from a checkpoint file. 

path
    
Path to the directory that was specified as the checkpoint directory
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#<init>\(path:String,hadoopConf:org.apache.hadoop.conf.Configuration\):org.apache.spark.streaming.StreamingContext "Permalink") new StreamingContext(path: String, hadoopConf: Configuration)
Recreate a StreamingContext from a checkpoint file.
Recreate a StreamingContext from a checkpoint file. 

path
    
Path to the directory that was specified as the checkpoint directory 

hadoopConf
    
Optional, configuration object if necessary for reading from HDFS compatible filesystems
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#<init>\(master:String,appName:String,batchDuration:org.apache.spark.streaming.Duration,sparkHome:String,jars:Seq\[String\],environment:scala.collection.Map\[String,String\]\):org.apache.spark.streaming.StreamingContext "Permalink") new StreamingContext(master: String, appName: String, batchDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), sparkHome: String = null, jars: Seq[String] = Nil, environment: Map[String, String] = Map())
Create a StreamingContext by providing the details necessary for creating a new SparkContext.
Create a StreamingContext by providing the details necessary for creating a new SparkContext. 

master
    
cluster URL to connect to (e.g. spark://host:port, local[4]). 

appName
    
a name for your job, to display on the cluster web UI 

batchDuration
    
the time interval at which streaming data will be divided into batches
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#<init>\(conf:org.apache.spark.SparkConf,batchDuration:org.apache.spark.streaming.Duration\):org.apache.spark.streaming.StreamingContext "Permalink") new StreamingContext(conf: [SparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html "org.apache.spark.SparkConf"), batchDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"))
Create a StreamingContext by providing the configuration necessary for a new SparkContext.
Create a StreamingContext by providing the configuration necessary for a new SparkContext. 

conf
    
a org.apache.spark.SparkConf object specifying Spark parameters 

batchDuration
    
the time interval at which streaming data will be divided into batches
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#<init>\(sparkContext:org.apache.spark.SparkContext,batchDuration:org.apache.spark.streaming.Duration\):org.apache.spark.streaming.StreamingContext "Permalink") new StreamingContext(sparkContext: [SparkContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html "org.apache.spark.SparkContext"), batchDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"))
Create a StreamingContext using an existing SparkContext.
Create a StreamingContext using an existing SparkContext. 

sparkContext
    
existing SparkContext 

batchDuration
    
the time interval at which streaming data will be divided into batches


### Type Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#LogStringContextextendsAnyRef "Permalink") implicit  class LogStringContext extends AnyRef 

Definition Classes
    Logging


### Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html###:Int "Permalink") final  def ##: Int 

Definition Classes
    AnyRef → Any
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#MDC\(key:org.apache.spark.internal.LogKey,value:Any\):org.apache.spark.internal.MDC "Permalink") def MDC(key: LogKey, value: Any): MDC 

Attributes
    protected  

Definition Classes
    Logging
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#addStreamingListener\(streamingListener:org.apache.spark.streaming.scheduler.StreamingListener\):Unit "Permalink") def addStreamingListener(streamingListener: [StreamingListener](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html "org.apache.spark.streaming.scheduler.StreamingListener")): Unit
Add a [org.apache.spark.streaming.scheduler.StreamingListener](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html "org.apache.spark.streaming.scheduler.StreamingListener") object for receiving system events related to streaming.
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0 

Definition Classes
    Any
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#awaitTermination\(\):Unit "Permalink") def awaitTermination(): Unit
Wait for the execution to stop.
Wait for the execution to stop. Any exceptions that occurs during the execution will be thrown in this thread. 
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#awaitTerminationOrTimeout\(timeout:Long\):Boolean "Permalink") def awaitTerminationOrTimeout(timeout: Long): Boolean
Wait for the execution to stop.
Wait for the execution to stop. Any exceptions that occurs during the execution will be thrown in this thread.  

timeout
    
time to wait in milliseconds 

returns
    
`true` if it's stopped; or throw the reported error during the execution; or `false` if the waiting time elapsed before returning from the method.
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#binaryRecordsStream\(directory:String,recordLength:Int\):org.apache.spark.streaming.dstream.DStream\[Array\[Byte\]\] "Permalink") def binaryRecordsStream(directory: String, recordLength: Int): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[Array[Byte]]
Create an input stream that monitors a Hadoop-compatible filesystem for new files and reads them as flat binary files, assuming a fixed length per record, generating one byte array per record.
Create an input stream that monitors a Hadoop-compatible filesystem for new files and reads them as flat binary files, assuming a fixed length per record, generating one byte array per record. Files must be written to the monitored directory by "moving" them from another location within the same file system. File names starting with . are ignored.  

directory
    
HDFS directory to monitor for new file 

recordLength
    
length of each record in bytes 

Note
    
We ensure that the byte array for each record in the resulting RDDs of the DStream has the provided record length.
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#checkpoint\(directory:String\):Unit "Permalink") def checkpoint(directory: String): Unit
Set the context to periodically checkpoint the DStream operations for driver fault-tolerance.
Set the context to periodically checkpoint the DStream operations for driver fault-tolerance. 

directory
    
HDFS-compatible directory where the checkpoint data will be reliably stored. Note that this must be a fault-tolerant file system like HDFS.
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#clone\(\):Object "Permalink") def clone(): AnyRef 

Attributes
    protected[lang]  

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#equals\(x$1:Object\):Boolean "Permalink") def equals(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef → Any
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#fileStream\[K,V,F<:org.apache.hadoop.mapreduce.InputFormat\[K,V\]\]\(directory:String,filter:org.apache.hadoop.fs.Path=>Boolean,newFilesOnly:Boolean,conf:org.apache.hadoop.conf.Configuration\)\(implicitevidence$10:scala.reflect.ClassTag\[K\],implicitevidence$11:scala.reflect.ClassTag\[V\],implicitevidence$12:scala.reflect.ClassTag\[F\]\):org.apache.spark.streaming.dstream.InputDStream\[\(K,V\)\] "Permalink") def fileStream[K, V, F <: InputFormat[K, V]](directory: String, filter: (Path) => Boolean, newFilesOnly: Boolean, conf: Configuration)(implicit arg0: ClassTag[K], arg1: ClassTag[V], arg2: ClassTag[F]): [InputDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/InputDStream.html "org.apache.spark.streaming.dstream.InputDStream")[(K, V)]
Create an input stream that monitors a Hadoop-compatible filesystem for new files and reads them using the given key-value types and input format.
Create an input stream that monitors a Hadoop-compatible filesystem for new files and reads them using the given key-value types and input format. Files must be written to the monitored directory by "moving" them from another location within the same file system. File names starting with . are ignored. 

K
    
Key type for reading HDFS file 

V
    
Value type for reading HDFS file 

F
    
Input format for reading HDFS file 

directory
    
HDFS directory to monitor for new file 

filter
    
Function to filter paths to process 

newFilesOnly
    
Should process only new files and ignore existing files in the directory 

conf
    
Hadoop configuration
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#fileStream\[K,V,F<:org.apache.hadoop.mapreduce.InputFormat\[K,V\]\]\(directory:String,filter:org.apache.hadoop.fs.Path=>Boolean,newFilesOnly:Boolean\)\(implicitevidence$7:scala.reflect.ClassTag\[K\],implicitevidence$8:scala.reflect.ClassTag\[V\],implicitevidence$9:scala.reflect.ClassTag\[F\]\):org.apache.spark.streaming.dstream.InputDStream\[\(K,V\)\] "Permalink") def fileStream[K, V, F <: InputFormat[K, V]](directory: String, filter: (Path) => Boolean, newFilesOnly: Boolean)(implicit arg0: ClassTag[K], arg1: ClassTag[V], arg2: ClassTag[F]): [InputDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/InputDStream.html "org.apache.spark.streaming.dstream.InputDStream")[(K, V)]
Create an input stream that monitors a Hadoop-compatible filesystem for new files and reads them using the given key-value types and input format.
Create an input stream that monitors a Hadoop-compatible filesystem for new files and reads them using the given key-value types and input format. Files must be written to the monitored directory by "moving" them from another location within the same file system. 

K
    
Key type for reading HDFS file 

V
    
Value type for reading HDFS file 

F
    
Input format for reading HDFS file 

directory
    
HDFS directory to monitor for new file 

filter
    
Function to filter paths to process 

newFilesOnly
    
Should process only new files and ignore existing files in the directory
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#fileStream\[K,V,F<:org.apache.hadoop.mapreduce.InputFormat\[K,V\]\]\(directory:String\)\(implicitevidence$4:scala.reflect.ClassTag\[K\],implicitevidence$5:scala.reflect.ClassTag\[V\],implicitevidence$6:scala.reflect.ClassTag\[F\]\):org.apache.spark.streaming.dstream.InputDStream\[\(K,V\)\] "Permalink") def fileStream[K, V, F <: InputFormat[K, V]](directory: String)(implicit arg0: ClassTag[K], arg1: ClassTag[V], arg2: ClassTag[F]): [InputDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/InputDStream.html "org.apache.spark.streaming.dstream.InputDStream")[(K, V)]
Create an input stream that monitors a Hadoop-compatible filesystem for new files and reads them using the given key-value types and input format.
Create an input stream that monitors a Hadoop-compatible filesystem for new files and reads them using the given key-value types and input format. Files must be written to the monitored directory by "moving" them from another location within the same file system. File names starting with . are ignored. 

K
    
Key type for reading HDFS file 

V
    
Value type for reading HDFS file 

F
    
Input format for reading HDFS file 

directory
    
HDFS directory to monitor for new file
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef] 

Definition Classes
    AnyRef → Any 

Annotations
     @IntrinsicCandidate() @native()
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#getState\(\):org.apache.spark.streaming.StreamingContextState "Permalink") def getState(): [StreamingContextState](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContextState.html "org.apache.spark.streaming.StreamingContextState")
Return the current state of the context. The context can be in three possible states -
     * StreamingContextState.INITIALIZED - The context has been created, but not started yet. Input DStreams, transformations and output operations can be created on the context.
     * StreamingContextState.ACTIVE - The context has been started, and not stopped. Input DStreams, transformations and output operations cannot be created on the context.
     * StreamingContextState.STOPPED - The context has been stopped and cannot be used any more.  

Annotations
     @DeveloperApi()
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#hashCode\(\):Int "Permalink") def hashCode(): Int 

Definition Classes
    AnyRef → Any 

Annotations
     @IntrinsicCandidate() @native()
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#initializeLogIfNecessary\(isInterpreter:Boolean,silent:Boolean\):Boolean "Permalink") def initializeLogIfNecessary(isInterpreter: Boolean, silent: Boolean): Boolean 

Attributes
    protected  

Definition Classes
    Logging
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#initializeLogIfNecessary\(isInterpreter:Boolean\):Unit "Permalink") def initializeLogIfNecessary(isInterpreter: Boolean): Unit 

Attributes
    protected  

Definition Classes
    Logging
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean 

Definition Classes
    Any
  23. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#isTraceEnabled\(\):Boolean "Permalink") def isTraceEnabled(): Boolean 

Attributes
    protected  

Definition Classes
    Logging
  24. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#log:org.slf4j.Logger "Permalink") def log: Logger 

Attributes
    protected  

Definition Classes
    Logging
  25. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#logBasedOnLevel\(level:org.slf4j.event.Level\)\(f:=>org.apache.spark.internal.MessageWithContext\):Unit "Permalink") def logBasedOnLevel(level: Level)(f: => MessageWithContext): Unit 

Attributes
    protected  

Definition Classes
    Logging
  26. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#logDebug\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logDebug(msg: => String, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  27. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#logDebug\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logDebug(entry: LogEntry, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  28. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#logDebug\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logDebug(entry: LogEntry): Unit 

Attributes
    protected  

Definition Classes
    Logging
  29. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#logDebug\(msg:=>String\):Unit "Permalink") def logDebug(msg: => String): Unit 

Attributes
    protected  

Definition Classes
    Logging
  30. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#logError\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logError(msg: => String, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  31. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#logError\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logError(entry: LogEntry, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  32. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#logError\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logError(entry: LogEntry): Unit 

Attributes
    protected  

Definition Classes
    Logging
  33. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#logError\(msg:=>String\):Unit "Permalink") def logError(msg: => String): Unit 

Attributes
    protected  

Definition Classes
    Logging
  34. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#logInfo\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logInfo(msg: => String, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  35. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#logInfo\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logInfo(entry: LogEntry, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  36. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#logInfo\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logInfo(entry: LogEntry): Unit 

Attributes
    protected  

Definition Classes
    Logging
  37. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#logInfo\(msg:=>String\):Unit "Permalink") def logInfo(msg: => String): Unit 

Attributes
    protected  

Definition Classes
    Logging
  38. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#logName:String "Permalink") def logName: [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String") 

Attributes
    protected  

Definition Classes
    Logging
  39. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#logTrace\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logTrace(msg: => String, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  40. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#logTrace\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logTrace(entry: LogEntry, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  41. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#logTrace\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logTrace(entry: LogEntry): Unit 

Attributes
    protected  

Definition Classes
    Logging
  42. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#logTrace\(msg:=>String\):Unit "Permalink") def logTrace(msg: => String): Unit 

Attributes
    protected  

Definition Classes
    Logging
  43. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#logWarning\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logWarning(msg: => String, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  44. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#logWarning\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logWarning(entry: LogEntry, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  45. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#logWarning\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logWarning(entry: LogEntry): Unit 

Attributes
    protected  

Definition Classes
    Logging
  46. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#logWarning\(msg:=>String\):Unit "Permalink") def logWarning(msg: => String): Unit 

Attributes
    protected  

Definition Classes
    Logging
  47. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  48. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#notify\(\):Unit "Permalink") final  def notify(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  49. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  50. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#queueStream\[T\]\(queue:scala.collection.mutable.Queue\[org.apache.spark.rdd.RDD\[T\]\],oneAtATime:Boolean,defaultRDD:org.apache.spark.rdd.RDD\[T\]\)\(implicitevidence$14:scala.reflect.ClassTag\[T\]\):org.apache.spark.streaming.dstream.InputDStream\[T\] "Permalink") def queueStream[T](queue: Queue[[RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[T]], oneAtATime: Boolean, defaultRDD: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[T])(implicit arg0: ClassTag[T]): [InputDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/InputDStream.html "org.apache.spark.streaming.dstream.InputDStream")[T]
Create an input stream from a queue of RDDs.
Create an input stream from a queue of RDDs. In each batch, it will process either one or all of the RDDs returned by the queue.  

T
    
Type of objects in the RDD 

queue
    
Queue of RDDs. Modifications to this data structure must be synchronized. 

oneAtATime
    
Whether only one RDD should be consumed from the queue in every interval 

defaultRDD
    
Default RDD is returned by the DStream when the queue is empty. Set as null if no RDD should be returned when empty 

Note
    
Arbitrary RDDs can be added to `queueStream`, there is no way to recover data of those RDDs, so `queueStream` doesn't support checkpointing.
  51. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#queueStream\[T\]\(queue:scala.collection.mutable.Queue\[org.apache.spark.rdd.RDD\[T\]\],oneAtATime:Boolean\)\(implicitevidence$13:scala.reflect.ClassTag\[T\]\):org.apache.spark.streaming.dstream.InputDStream\[T\] "Permalink") def queueStream[T](queue: Queue[[RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[T]], oneAtATime: Boolean = true)(implicit arg0: ClassTag[T]): [InputDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/InputDStream.html "org.apache.spark.streaming.dstream.InputDStream")[T]
Create an input stream from a queue of RDDs.
Create an input stream from a queue of RDDs. In each batch, it will process either one or all of the RDDs returned by the queue.  

T
    
Type of objects in the RDD 

queue
    
Queue of RDDs. Modifications to this data structure must be synchronized. 

oneAtATime
    
Whether only one RDD should be consumed from the queue in every interval 

Note
    
Arbitrary RDDs can be added to `queueStream`, there is no way to recover data of those RDDs, so `queueStream` doesn't support checkpointing.
  52. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#rawSocketStream\[T\]\(hostname:String,port:Int,storageLevel:org.apache.spark.storage.StorageLevel\)\(implicitevidence$3:scala.reflect.ClassTag\[T\]\):org.apache.spark.streaming.dstream.ReceiverInputDStream\[T\] "Permalink") def rawSocketStream[T](hostname: String, port: Int, storageLevel: [StorageLevel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StorageLevel.html "org.apache.spark.storage.StorageLevel") = [StorageLevel.MEMORY_AND_DISK_SER_2](https://spark.apache.org/docs/latest/api/scala/org/index.html))(implicit arg0: ClassTag[T]): [ReceiverInputDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/ReceiverInputDStream.html "org.apache.spark.streaming.dstream.ReceiverInputDStream")[T]
Create an input stream from network source hostname:port, where data is received as serialized blocks (serialized using the Spark's serializer) that can be directly pushed into the block manager without deserializing them.
Create an input stream from network source hostname:port, where data is received as serialized blocks (serialized using the Spark's serializer) that can be directly pushed into the block manager without deserializing them. This is the most efficient way to receive data. 

T
    
Type of the objects in the received blocks 

hostname
    
Hostname to connect to for receiving data 

port
    
Port to connect to for receiving data 

storageLevel
    
Storage level to use for storing the received objects (default: StorageLevel.MEMORY_AND_DISK_SER_2)
  53. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#receiverStream\[T\]\(receiver:org.apache.spark.streaming.receiver.Receiver\[T\]\)\(implicitevidence$1:scala.reflect.ClassTag\[T\]\):org.apache.spark.streaming.dstream.ReceiverInputDStream\[T\] "Permalink") def receiverStream[T](receiver: [Receiver](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html "org.apache.spark.streaming.receiver.Receiver")[T])(implicit arg0: ClassTag[T]): [ReceiverInputDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/ReceiverInputDStream.html "org.apache.spark.streaming.dstream.ReceiverInputDStream")[T]
Create an input stream with any arbitrary user implemented receiver.
Create an input stream with any arbitrary user implemented receiver. Find more details at https://spark.apache.org/docs/latest/streaming-custom-receivers.html 

receiver
    
Custom implementation of Receiver
  54. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#remember\(duration:org.apache.spark.streaming.Duration\):Unit "Permalink") def remember(duration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration")): Unit
Set each DStream in this context to remember RDDs it generated in the last given duration.
Set each DStream in this context to remember RDDs it generated in the last given duration. DStreams remember RDDs only for a limited duration of time and release them for garbage collection. This method allows the developer to specify how long to remember the RDDs ( if the developer wishes to query old data outside the DStream computation). 

duration
    
Minimum duration that each DStream should remember its RDDs
  55. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#removeStreamingListener\(streamingListener:org.apache.spark.streaming.scheduler.StreamingListener\):Unit "Permalink") def removeStreamingListener(streamingListener: [StreamingListener](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html "org.apache.spark.streaming.scheduler.StreamingListener")): Unit
  56. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#socketStream\[T\]\(hostname:String,port:Int,converter:java.io.InputStream=>Iterator\[T\],storageLevel:org.apache.spark.storage.StorageLevel\)\(implicitevidence$2:scala.reflect.ClassTag\[T\]\):org.apache.spark.streaming.dstream.ReceiverInputDStream\[T\] "Permalink") def socketStream[T](hostname: String, port: Int, converter: ([InputStream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html#java.io.InputStream "java.io.InputStream")) => Iterator[T], storageLevel: [StorageLevel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StorageLevel.html "org.apache.spark.storage.StorageLevel"))(implicit arg0: ClassTag[T]): [ReceiverInputDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/ReceiverInputDStream.html "org.apache.spark.streaming.dstream.ReceiverInputDStream")[T]
Creates an input stream from TCP source hostname:port.
Creates an input stream from TCP source hostname:port. Data is received using a TCP socket and the receive bytes it interpreted as object using the given converter. 

T
    
Type of the objects received (after converting bytes to objects) 

hostname
    
Hostname to connect to for receiving data 

port
    
Port to connect to for receiving data 

converter
    
Function to convert the byte stream to objects 

storageLevel
    
Storage level to use for storing the received objects
  57. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#socketTextStream\(hostname:String,port:Int,storageLevel:org.apache.spark.storage.StorageLevel\):org.apache.spark.streaming.dstream.ReceiverInputDStream\[String\] "Permalink") def socketTextStream(hostname: String, port: Int, storageLevel: [StorageLevel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StorageLevel.html "org.apache.spark.storage.StorageLevel") = [StorageLevel.MEMORY_AND_DISK_SER_2](https://spark.apache.org/docs/latest/api/scala/org/index.html)): [ReceiverInputDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/ReceiverInputDStream.html "org.apache.spark.streaming.dstream.ReceiverInputDStream")[String]
Creates an input stream from TCP source hostname:port.
Creates an input stream from TCP source hostname:port. Data is received using a TCP socket and the receive bytes is interpreted as UTF8 encoded `\n` delimited lines. 

hostname
    
Hostname to connect to for receiving data 

port
    
Port to connect to for receiving data 

storageLevel
    
Storage level to use for storing the received objects (default: StorageLevel.MEMORY_AND_DISK_SER_2) 

See also
    
[socketStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#socketStream\[T\]\(hostname:String,port:Int,converter:java.io.InputStream=>Iterator\[T\],storageLevel:org.apache.spark.storage.StorageLevel\)\(implicitevidence$2:scala.reflect.ClassTag\[T\]\):org.apache.spark.streaming.dstream.ReceiverInputDStream\[T\])
  58. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#sparkContext:org.apache.spark.SparkContext "Permalink") def sparkContext: [SparkContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html "org.apache.spark.SparkContext")
Return the associated Spark context 
  59. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#start\(\):Unit "Permalink") def start(): Unit
Start the execution of the streams.
Start the execution of the streams.  

Exceptions thrown
    
`IllegalStateException` if the StreamingContext is already stopped.
  60. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#stop\(stopSparkContext:Boolean,stopGracefully:Boolean\):Unit "Permalink") def stop(stopSparkContext: Boolean, stopGracefully: Boolean): Unit
Stop the execution of the streams, with option of ensuring all received data has been processed.
Stop the execution of the streams, with option of ensuring all received data has been processed.  

stopSparkContext
    
if true, stops the associated SparkContext. The underlying SparkContext will be stopped regardless of whether this StreamingContext has been started. 

stopGracefully
    
if true, stops gracefully by waiting for the processing of all received data to be completed
  61. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#stop\(stopSparkContext:Boolean\):Unit "Permalink") def stop(stopSparkContext: Boolean = [conf.getBoolean("spark.streaming.stopSparkContextByDefault", true)](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html#getBoolean\(key:String,defaultValue:Boolean\):Boolean)): Unit
Stop the execution of the streams immediately (does not wait for all received data to be processed).
Stop the execution of the streams immediately (does not wait for all received data to be processed). By default, if `stopSparkContext` is not specified, the underlying SparkContext will also be stopped. This implicit behavior can be configured using the SparkConf configuration spark.streaming.stopSparkContextByDefault.  

stopSparkContext
    
If true, stops the associated SparkContext. The underlying SparkContext will be stopped regardless of whether this StreamingContext has been started.
  62. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0 

Definition Classes
    AnyRef
  63. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#textFileStream\(directory:String\):org.apache.spark.streaming.dstream.DStream\[String\] "Permalink") def textFileStream(directory: String): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[String]
Create an input stream that monitors a Hadoop-compatible filesystem for new files and reads them as text files (using key as LongWritable, value as Text and input format as TextInputFormat).
Create an input stream that monitors a Hadoop-compatible filesystem for new files and reads them as text files (using key as LongWritable, value as Text and input format as TextInputFormat). Files must be written to the monitored directory by "moving" them from another location within the same file system. File names starting with . are ignored. The text files must be encoded as UTF-8.  

directory
    
HDFS directory to monitor for new file
  64. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#toString\(\):String "Permalink") def toString(): [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String") 

Definition Classes
    AnyRef → Any
  65. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#transform\[T\]\(dstreams:Seq\[org.apache.spark.streaming.dstream.DStream\[_\]\],transformFunc:\(Seq\[org.apache.spark.rdd.RDD\[_\]\],org.apache.spark.streaming.Time\)=>org.apache.spark.rdd.RDD\[T\]\)\(implicitevidence$16:scala.reflect.ClassTag\[T\]\):org.apache.spark.streaming.dstream.DStream\[T\] "Permalink") def transform[T](dstreams: Seq[[DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[_]], transformFunc: (Seq[[RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[_]], [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time")) => [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[T])(implicit arg0: ClassTag[T]): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[T]
Create a new DStream in which each RDD is generated by applying a function on RDDs of the DStreams.
  66. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#union\[T\]\(streams:Seq\[org.apache.spark.streaming.dstream.DStream\[T\]\]\)\(implicitevidence$15:scala.reflect.ClassTag\[T\]\):org.apache.spark.streaming.dstream.DStream\[T\] "Permalink") def union[T](streams: Seq[[DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[T]])(implicit arg0: ClassTag[T]): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[T]
Create a unified DStream from multiple DStreams of the same type and same slide duration.
  67. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  68. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  69. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#wait\(\):Unit "Permalink") final  def wait(): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  70. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#withLogContext\(context:java.util.Map\[String,String\]\)\(body:=>Unit\):Unit "Permalink") def withLogContext(context: [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#java.util.Map "java.util.Map")[String, String])(body: => Unit): Unit 

Attributes
    protected  

Definition Classes
    Logging


### Deprecated Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#finalize\(\):Unit "Permalink") def finalize(): Unit 

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
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#MDC\(key:org.apache.spark.internal.LogKey,value:Any\):org.apache.spark.internal.MDC "Permalink") def MDC(key: LogKey, value: Any): MDC 

Attributes
    protected  

Definition Classes
    Logging
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#initializeLogIfNecessary\(isInterpreter:Boolean,silent:Boolean\):Boolean "Permalink") def initializeLogIfNecessary(isInterpreter: Boolean, silent: Boolean): Boolean 

Attributes
    protected  

Definition Classes
    Logging
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#initializeLogIfNecessary\(isInterpreter:Boolean\):Unit "Permalink") def initializeLogIfNecessary(isInterpreter: Boolean): Unit 

Attributes
    protected  

Definition Classes
    Logging
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#isTraceEnabled\(\):Boolean "Permalink") def isTraceEnabled(): Boolean 

Attributes
    protected  

Definition Classes
    Logging
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#log:org.slf4j.Logger "Permalink") def log: Logger 

Attributes
    protected  

Definition Classes
    Logging
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#logBasedOnLevel\(level:org.slf4j.event.Level\)\(f:=>org.apache.spark.internal.MessageWithContext\):Unit "Permalink") def logBasedOnLevel(level: Level)(f: => MessageWithContext): Unit 

Attributes
    protected  

Definition Classes
    Logging
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#logDebug\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logDebug(msg: => String, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#logDebug\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logDebug(entry: LogEntry, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#logDebug\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logDebug(entry: LogEntry): Unit 

Attributes
    protected  

Definition Classes
    Logging
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#logDebug\(msg:=>String\):Unit "Permalink") def logDebug(msg: => String): Unit 

Attributes
    protected  

Definition Classes
    Logging
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#logError\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logError(msg: => String, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#logError\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logError(entry: LogEntry, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#logError\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logError(entry: LogEntry): Unit 

Attributes
    protected  

Definition Classes
    Logging
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#logError\(msg:=>String\):Unit "Permalink") def logError(msg: => String): Unit 

Attributes
    protected  

Definition Classes
    Logging
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#logInfo\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logInfo(msg: => String, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#logInfo\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logInfo(entry: LogEntry, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#logInfo\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logInfo(entry: LogEntry): Unit 

Attributes
    protected  

Definition Classes
    Logging
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#logInfo\(msg:=>String\):Unit "Permalink") def logInfo(msg: => String): Unit 

Attributes
    protected  

Definition Classes
    Logging
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#logName:String "Permalink") def logName: [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String") 

Attributes
    protected  

Definition Classes
    Logging
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#logTrace\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logTrace(msg: => String, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#logTrace\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logTrace(entry: LogEntry, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#logTrace\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logTrace(entry: LogEntry): Unit 

Attributes
    protected  

Definition Classes
    Logging
  23. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#logTrace\(msg:=>String\):Unit "Permalink") def logTrace(msg: => String): Unit 

Attributes
    protected  

Definition Classes
    Logging
  24. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#logWarning\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logWarning(msg: => String, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  25. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#logWarning\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logWarning(entry: LogEntry, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  26. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#logWarning\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logWarning(entry: LogEntry): Unit 

Attributes
    protected  

Definition Classes
    Logging
  27. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#logWarning\(msg:=>String\):Unit "Permalink") def logWarning(msg: => String): Unit 

Attributes
    protected  

Definition Classes
    Logging
  28. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#withLogContext\(context:java.util.Map\[String,String\]\)\(body:=>Unit\):Unit "Permalink") def withLogContext(context: [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#java.util.Map "java.util.Map")[String, String])(body: => Unit): Unit 

Attributes
    protected  

Definition Classes
    Logging


### Inherited from AnyRef
### Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html###:Int "Permalink") final  def ##: Int 

Definition Classes
    AnyRef → Any
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#clone\(\):Object "Permalink") def clone(): AnyRef 

Attributes
    protected[lang]  

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#equals\(x$1:Object\):Boolean "Permalink") def equals(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef → Any
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef] 

Definition Classes
    AnyRef → Any 

Annotations
     @IntrinsicCandidate() @native()
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#hashCode\(\):Int "Permalink") def hashCode(): Int 

Definition Classes
    AnyRef → Any 

Annotations
     @IntrinsicCandidate() @native()
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#notify\(\):Unit "Permalink") final  def notify(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0 

Definition Classes
    AnyRef
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#toString\(\):String "Permalink") def toString(): [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String") 

Definition Classes
    AnyRef → Any
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#wait\(\):Unit "Permalink") final  def wait(): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#finalize\(\):Unit "Permalink") def finalize(): Unit 

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
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0 

Definition Classes
    Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean 

Definition Classes
    Any


### Ungrouped
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#LogStringContextextendsAnyRef "Permalink") implicit  class LogStringContext extends AnyRef 

Definition Classes
    Logging


  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html###:Int "Permalink") final  def ##: Int 

Definition Classes
    AnyRef → Any
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#MDC\(key:org.apache.spark.internal.LogKey,value:Any\):org.apache.spark.internal.MDC "Permalink") def MDC(key: LogKey, value: Any): MDC 

Attributes
    protected  

Definition Classes
    Logging
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#addStreamingListener\(streamingListener:org.apache.spark.streaming.scheduler.StreamingListener\):Unit "Permalink") def addStreamingListener(streamingListener: [StreamingListener](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html "org.apache.spark.streaming.scheduler.StreamingListener")): Unit
Add a [org.apache.spark.streaming.scheduler.StreamingListener](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html "org.apache.spark.streaming.scheduler.StreamingListener") object for receiving system events related to streaming.
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0 

Definition Classes
    Any
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#awaitTermination\(\):Unit "Permalink") def awaitTermination(): Unit
Wait for the execution to stop.
Wait for the execution to stop. Any exceptions that occurs during the execution will be thrown in this thread. 
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#awaitTerminationOrTimeout\(timeout:Long\):Boolean "Permalink") def awaitTerminationOrTimeout(timeout: Long): Boolean
Wait for the execution to stop.
Wait for the execution to stop. Any exceptions that occurs during the execution will be thrown in this thread.  

timeout
    
time to wait in milliseconds 

returns
    
`true` if it's stopped; or throw the reported error during the execution; or `false` if the waiting time elapsed before returning from the method.
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#binaryRecordsStream\(directory:String,recordLength:Int\):org.apache.spark.streaming.dstream.DStream\[Array\[Byte\]\] "Permalink") def binaryRecordsStream(directory: String, recordLength: Int): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[Array[Byte]]
Create an input stream that monitors a Hadoop-compatible filesystem for new files and reads them as flat binary files, assuming a fixed length per record, generating one byte array per record.
Create an input stream that monitors a Hadoop-compatible filesystem for new files and reads them as flat binary files, assuming a fixed length per record, generating one byte array per record. Files must be written to the monitored directory by "moving" them from another location within the same file system. File names starting with . are ignored.  

directory
    
HDFS directory to monitor for new file 

recordLength
    
length of each record in bytes 

Note
    
We ensure that the byte array for each record in the resulting RDDs of the DStream has the provided record length.
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#checkpoint\(directory:String\):Unit "Permalink") def checkpoint(directory: String): Unit
Set the context to periodically checkpoint the DStream operations for driver fault-tolerance.
Set the context to periodically checkpoint the DStream operations for driver fault-tolerance. 

directory
    
HDFS-compatible directory where the checkpoint data will be reliably stored. Note that this must be a fault-tolerant file system like HDFS.
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#clone\(\):Object "Permalink") def clone(): AnyRef 

Attributes
    protected[lang]  

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#equals\(x$1:Object\):Boolean "Permalink") def equals(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef → Any
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#fileStream\[K,V,F<:org.apache.hadoop.mapreduce.InputFormat\[K,V\]\]\(directory:String,filter:org.apache.hadoop.fs.Path=>Boolean,newFilesOnly:Boolean,conf:org.apache.hadoop.conf.Configuration\)\(implicitevidence$10:scala.reflect.ClassTag\[K\],implicitevidence$11:scala.reflect.ClassTag\[V\],implicitevidence$12:scala.reflect.ClassTag\[F\]\):org.apache.spark.streaming.dstream.InputDStream\[\(K,V\)\] "Permalink") def fileStream[K, V, F <: InputFormat[K, V]](directory: String, filter: (Path) => Boolean, newFilesOnly: Boolean, conf: Configuration)(implicit arg0: ClassTag[K], arg1: ClassTag[V], arg2: ClassTag[F]): [InputDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/InputDStream.html "org.apache.spark.streaming.dstream.InputDStream")[(K, V)]
Create an input stream that monitors a Hadoop-compatible filesystem for new files and reads them using the given key-value types and input format.
Create an input stream that monitors a Hadoop-compatible filesystem for new files and reads them using the given key-value types and input format. Files must be written to the monitored directory by "moving" them from another location within the same file system. File names starting with . are ignored. 

K
    
Key type for reading HDFS file 

V
    
Value type for reading HDFS file 

F
    
Input format for reading HDFS file 

directory
    
HDFS directory to monitor for new file 

filter
    
Function to filter paths to process 

newFilesOnly
    
Should process only new files and ignore existing files in the directory 

conf
    
Hadoop configuration
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#fileStream\[K,V,F<:org.apache.hadoop.mapreduce.InputFormat\[K,V\]\]\(directory:String,filter:org.apache.hadoop.fs.Path=>Boolean,newFilesOnly:Boolean\)\(implicitevidence$7:scala.reflect.ClassTag\[K\],implicitevidence$8:scala.reflect.ClassTag\[V\],implicitevidence$9:scala.reflect.ClassTag\[F\]\):org.apache.spark.streaming.dstream.InputDStream\[\(K,V\)\] "Permalink") def fileStream[K, V, F <: InputFormat[K, V]](directory: String, filter: (Path) => Boolean, newFilesOnly: Boolean)(implicit arg0: ClassTag[K], arg1: ClassTag[V], arg2: ClassTag[F]): [InputDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/InputDStream.html "org.apache.spark.streaming.dstream.InputDStream")[(K, V)]
Create an input stream that monitors a Hadoop-compatible filesystem for new files and reads them using the given key-value types and input format.
Create an input stream that monitors a Hadoop-compatible filesystem for new files and reads them using the given key-value types and input format. Files must be written to the monitored directory by "moving" them from another location within the same file system. 

K
    
Key type for reading HDFS file 

V
    
Value type for reading HDFS file 

F
    
Input format for reading HDFS file 

directory
    
HDFS directory to monitor for new file 

filter
    
Function to filter paths to process 

newFilesOnly
    
Should process only new files and ignore existing files in the directory
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#fileStream\[K,V,F<:org.apache.hadoop.mapreduce.InputFormat\[K,V\]\]\(directory:String\)\(implicitevidence$4:scala.reflect.ClassTag\[K\],implicitevidence$5:scala.reflect.ClassTag\[V\],implicitevidence$6:scala.reflect.ClassTag\[F\]\):org.apache.spark.streaming.dstream.InputDStream\[\(K,V\)\] "Permalink") def fileStream[K, V, F <: InputFormat[K, V]](directory: String)(implicit arg0: ClassTag[K], arg1: ClassTag[V], arg2: ClassTag[F]): [InputDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/InputDStream.html "org.apache.spark.streaming.dstream.InputDStream")[(K, V)]
Create an input stream that monitors a Hadoop-compatible filesystem for new files and reads them using the given key-value types and input format.
Create an input stream that monitors a Hadoop-compatible filesystem for new files and reads them using the given key-value types and input format. Files must be written to the monitored directory by "moving" them from another location within the same file system. File names starting with . are ignored. 

K
    
Key type for reading HDFS file 

V
    
Value type for reading HDFS file 

F
    
Input format for reading HDFS file 

directory
    
HDFS directory to monitor for new file
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef] 

Definition Classes
    AnyRef → Any 

Annotations
     @IntrinsicCandidate() @native()
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#getState\(\):org.apache.spark.streaming.StreamingContextState "Permalink") def getState(): [StreamingContextState](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContextState.html "org.apache.spark.streaming.StreamingContextState")
Return the current state of the context. The context can be in three possible states -
     * StreamingContextState.INITIALIZED - The context has been created, but not started yet. Input DStreams, transformations and output operations can be created on the context.
     * StreamingContextState.ACTIVE - The context has been started, and not stopped. Input DStreams, transformations and output operations cannot be created on the context.
     * StreamingContextState.STOPPED - The context has been stopped and cannot be used any more.  

Annotations
     @DeveloperApi()
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#hashCode\(\):Int "Permalink") def hashCode(): Int 

Definition Classes
    AnyRef → Any 

Annotations
     @IntrinsicCandidate() @native()
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#initializeLogIfNecessary\(isInterpreter:Boolean,silent:Boolean\):Boolean "Permalink") def initializeLogIfNecessary(isInterpreter: Boolean, silent: Boolean): Boolean 

Attributes
    protected  

Definition Classes
    Logging
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#initializeLogIfNecessary\(isInterpreter:Boolean\):Unit "Permalink") def initializeLogIfNecessary(isInterpreter: Boolean): Unit 

Attributes
    protected  

Definition Classes
    Logging
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean 

Definition Classes
    Any
  23. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#isTraceEnabled\(\):Boolean "Permalink") def isTraceEnabled(): Boolean 

Attributes
    protected  

Definition Classes
    Logging
  24. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#log:org.slf4j.Logger "Permalink") def log: Logger 

Attributes
    protected  

Definition Classes
    Logging
  25. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#logBasedOnLevel\(level:org.slf4j.event.Level\)\(f:=>org.apache.spark.internal.MessageWithContext\):Unit "Permalink") def logBasedOnLevel(level: Level)(f: => MessageWithContext): Unit 

Attributes
    protected  

Definition Classes
    Logging
  26. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#logDebug\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logDebug(msg: => String, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  27. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#logDebug\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logDebug(entry: LogEntry, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  28. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#logDebug\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logDebug(entry: LogEntry): Unit 

Attributes
    protected  

Definition Classes
    Logging
  29. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#logDebug\(msg:=>String\):Unit "Permalink") def logDebug(msg: => String): Unit 

Attributes
    protected  

Definition Classes
    Logging
  30. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#logError\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logError(msg: => String, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  31. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#logError\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logError(entry: LogEntry, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  32. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#logError\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logError(entry: LogEntry): Unit 

Attributes
    protected  

Definition Classes
    Logging
  33. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#logError\(msg:=>String\):Unit "Permalink") def logError(msg: => String): Unit 

Attributes
    protected  

Definition Classes
    Logging
  34. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#logInfo\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logInfo(msg: => String, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  35. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#logInfo\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logInfo(entry: LogEntry, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  36. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#logInfo\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logInfo(entry: LogEntry): Unit 

Attributes
    protected  

Definition Classes
    Logging
  37. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#logInfo\(msg:=>String\):Unit "Permalink") def logInfo(msg: => String): Unit 

Attributes
    protected  

Definition Classes
    Logging
  38. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#logName:String "Permalink") def logName: [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String") 

Attributes
    protected  

Definition Classes
    Logging
  39. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#logTrace\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logTrace(msg: => String, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  40. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#logTrace\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logTrace(entry: LogEntry, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  41. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#logTrace\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logTrace(entry: LogEntry): Unit 

Attributes
    protected  

Definition Classes
    Logging
  42. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#logTrace\(msg:=>String\):Unit "Permalink") def logTrace(msg: => String): Unit 

Attributes
    protected  

Definition Classes
    Logging
  43. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#logWarning\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logWarning(msg: => String, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  44. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#logWarning\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logWarning(entry: LogEntry, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  45. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#logWarning\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logWarning(entry: LogEntry): Unit 

Attributes
    protected  

Definition Classes
    Logging
  46. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#logWarning\(msg:=>String\):Unit "Permalink") def logWarning(msg: => String): Unit 

Attributes
    protected  

Definition Classes
    Logging
  47. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  48. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#notify\(\):Unit "Permalink") final  def notify(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  49. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  50. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#queueStream\[T\]\(queue:scala.collection.mutable.Queue\[org.apache.spark.rdd.RDD\[T\]\],oneAtATime:Boolean,defaultRDD:org.apache.spark.rdd.RDD\[T\]\)\(implicitevidence$14:scala.reflect.ClassTag\[T\]\):org.apache.spark.streaming.dstream.InputDStream\[T\] "Permalink") def queueStream[T](queue: Queue[[RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[T]], oneAtATime: Boolean, defaultRDD: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[T])(implicit arg0: ClassTag[T]): [InputDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/InputDStream.html "org.apache.spark.streaming.dstream.InputDStream")[T]
Create an input stream from a queue of RDDs.
Create an input stream from a queue of RDDs. In each batch, it will process either one or all of the RDDs returned by the queue.  

T
    
Type of objects in the RDD 

queue
    
Queue of RDDs. Modifications to this data structure must be synchronized. 

oneAtATime
    
Whether only one RDD should be consumed from the queue in every interval 

defaultRDD
    
Default RDD is returned by the DStream when the queue is empty. Set as null if no RDD should be returned when empty 

Note
    
Arbitrary RDDs can be added to `queueStream`, there is no way to recover data of those RDDs, so `queueStream` doesn't support checkpointing.
  51. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#queueStream\[T\]\(queue:scala.collection.mutable.Queue\[org.apache.spark.rdd.RDD\[T\]\],oneAtATime:Boolean\)\(implicitevidence$13:scala.reflect.ClassTag\[T\]\):org.apache.spark.streaming.dstream.InputDStream\[T\] "Permalink") def queueStream[T](queue: Queue[[RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[T]], oneAtATime: Boolean = true)(implicit arg0: ClassTag[T]): [InputDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/InputDStream.html "org.apache.spark.streaming.dstream.InputDStream")[T]
Create an input stream from a queue of RDDs.
Create an input stream from a queue of RDDs. In each batch, it will process either one or all of the RDDs returned by the queue.  

T
    
Type of objects in the RDD 

queue
    
Queue of RDDs. Modifications to this data structure must be synchronized. 

oneAtATime
    
Whether only one RDD should be consumed from the queue in every interval 

Note
    
Arbitrary RDDs can be added to `queueStream`, there is no way to recover data of those RDDs, so `queueStream` doesn't support checkpointing.
  52. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#rawSocketStream\[T\]\(hostname:String,port:Int,storageLevel:org.apache.spark.storage.StorageLevel\)\(implicitevidence$3:scala.reflect.ClassTag\[T\]\):org.apache.spark.streaming.dstream.ReceiverInputDStream\[T\] "Permalink") def rawSocketStream[T](hostname: String, port: Int, storageLevel: [StorageLevel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StorageLevel.html "org.apache.spark.storage.StorageLevel") = [StorageLevel.MEMORY_AND_DISK_SER_2](https://spark.apache.org/docs/latest/api/scala/org/index.html))(implicit arg0: ClassTag[T]): [ReceiverInputDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/ReceiverInputDStream.html "org.apache.spark.streaming.dstream.ReceiverInputDStream")[T]
Create an input stream from network source hostname:port, where data is received as serialized blocks (serialized using the Spark's serializer) that can be directly pushed into the block manager without deserializing them.
Create an input stream from network source hostname:port, where data is received as serialized blocks (serialized using the Spark's serializer) that can be directly pushed into the block manager without deserializing them. This is the most efficient way to receive data. 

T
    
Type of the objects in the received blocks 

hostname
    
Hostname to connect to for receiving data 

port
    
Port to connect to for receiving data 

storageLevel
    
Storage level to use for storing the received objects (default: StorageLevel.MEMORY_AND_DISK_SER_2)
  53. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#receiverStream\[T\]\(receiver:org.apache.spark.streaming.receiver.Receiver\[T\]\)\(implicitevidence$1:scala.reflect.ClassTag\[T\]\):org.apache.spark.streaming.dstream.ReceiverInputDStream\[T\] "Permalink") def receiverStream[T](receiver: [Receiver](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html "org.apache.spark.streaming.receiver.Receiver")[T])(implicit arg0: ClassTag[T]): [ReceiverInputDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/ReceiverInputDStream.html "org.apache.spark.streaming.dstream.ReceiverInputDStream")[T]
Create an input stream with any arbitrary user implemented receiver.
Create an input stream with any arbitrary user implemented receiver. Find more details at https://spark.apache.org/docs/latest/streaming-custom-receivers.html 

receiver
    
Custom implementation of Receiver
  54. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#remember\(duration:org.apache.spark.streaming.Duration\):Unit "Permalink") def remember(duration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration")): Unit
Set each DStream in this context to remember RDDs it generated in the last given duration.
Set each DStream in this context to remember RDDs it generated in the last given duration. DStreams remember RDDs only for a limited duration of time and release them for garbage collection. This method allows the developer to specify how long to remember the RDDs ( if the developer wishes to query old data outside the DStream computation). 

duration
    
Minimum duration that each DStream should remember its RDDs
  55. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#removeStreamingListener\(streamingListener:org.apache.spark.streaming.scheduler.StreamingListener\):Unit "Permalink") def removeStreamingListener(streamingListener: [StreamingListener](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html "org.apache.spark.streaming.scheduler.StreamingListener")): Unit
  56. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#socketStream\[T\]\(hostname:String,port:Int,converter:java.io.InputStream=>Iterator\[T\],storageLevel:org.apache.spark.storage.StorageLevel\)\(implicitevidence$2:scala.reflect.ClassTag\[T\]\):org.apache.spark.streaming.dstream.ReceiverInputDStream\[T\] "Permalink") def socketStream[T](hostname: String, port: Int, converter: ([InputStream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html#java.io.InputStream "java.io.InputStream")) => Iterator[T], storageLevel: [StorageLevel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StorageLevel.html "org.apache.spark.storage.StorageLevel"))(implicit arg0: ClassTag[T]): [ReceiverInputDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/ReceiverInputDStream.html "org.apache.spark.streaming.dstream.ReceiverInputDStream")[T]
Creates an input stream from TCP source hostname:port.
Creates an input stream from TCP source hostname:port. Data is received using a TCP socket and the receive bytes it interpreted as object using the given converter. 

T
    
Type of the objects received (after converting bytes to objects) 

hostname
    
Hostname to connect to for receiving data 

port
    
Port to connect to for receiving data 

converter
    
Function to convert the byte stream to objects 

storageLevel
    
Storage level to use for storing the received objects
  57. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#socketTextStream\(hostname:String,port:Int,storageLevel:org.apache.spark.storage.StorageLevel\):org.apache.spark.streaming.dstream.ReceiverInputDStream\[String\] "Permalink") def socketTextStream(hostname: String, port: Int, storageLevel: [StorageLevel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StorageLevel.html "org.apache.spark.storage.StorageLevel") = [StorageLevel.MEMORY_AND_DISK_SER_2](https://spark.apache.org/docs/latest/api/scala/org/index.html)): [ReceiverInputDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/ReceiverInputDStream.html "org.apache.spark.streaming.dstream.ReceiverInputDStream")[String]
Creates an input stream from TCP source hostname:port.
Creates an input stream from TCP source hostname:port. Data is received using a TCP socket and the receive bytes is interpreted as UTF8 encoded `\n` delimited lines. 

hostname
    
Hostname to connect to for receiving data 

port
    
Port to connect to for receiving data 

storageLevel
    
Storage level to use for storing the received objects (default: StorageLevel.MEMORY_AND_DISK_SER_2) 

See also
    
[socketStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#socketStream\[T\]\(hostname:String,port:Int,converter:java.io.InputStream=>Iterator\[T\],storageLevel:org.apache.spark.storage.StorageLevel\)\(implicitevidence$2:scala.reflect.ClassTag\[T\]\):org.apache.spark.streaming.dstream.ReceiverInputDStream\[T\])
  58. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#sparkContext:org.apache.spark.SparkContext "Permalink") def sparkContext: [SparkContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html "org.apache.spark.SparkContext")
Return the associated Spark context 
  59. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#start\(\):Unit "Permalink") def start(): Unit
Start the execution of the streams.
Start the execution of the streams.  

Exceptions thrown
    
`IllegalStateException` if the StreamingContext is already stopped.
  60. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#stop\(stopSparkContext:Boolean,stopGracefully:Boolean\):Unit "Permalink") def stop(stopSparkContext: Boolean, stopGracefully: Boolean): Unit
Stop the execution of the streams, with option of ensuring all received data has been processed.
Stop the execution of the streams, with option of ensuring all received data has been processed.  

stopSparkContext
    
if true, stops the associated SparkContext. The underlying SparkContext will be stopped regardless of whether this StreamingContext has been started. 

stopGracefully
    
if true, stops gracefully by waiting for the processing of all received data to be completed
  61. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#stop\(stopSparkContext:Boolean\):Unit "Permalink") def stop(stopSparkContext: Boolean = [conf.getBoolean("spark.streaming.stopSparkContextByDefault", true)](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ReadOnlySparkConf.html#getBoolean\(key:String,defaultValue:Boolean\):Boolean)): Unit
Stop the execution of the streams immediately (does not wait for all received data to be processed).
Stop the execution of the streams immediately (does not wait for all received data to be processed). By default, if `stopSparkContext` is not specified, the underlying SparkContext will also be stopped. This implicit behavior can be configured using the SparkConf configuration spark.streaming.stopSparkContextByDefault.  

stopSparkContext
    
If true, stops the associated SparkContext. The underlying SparkContext will be stopped regardless of whether this StreamingContext has been started.
  62. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0 

Definition Classes
    AnyRef
  63. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#textFileStream\(directory:String\):org.apache.spark.streaming.dstream.DStream\[String\] "Permalink") def textFileStream(directory: String): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[String]
Create an input stream that monitors a Hadoop-compatible filesystem for new files and reads them as text files (using key as LongWritable, value as Text and input format as TextInputFormat).
Create an input stream that monitors a Hadoop-compatible filesystem for new files and reads them as text files (using key as LongWritable, value as Text and input format as TextInputFormat). Files must be written to the monitored directory by "moving" them from another location within the same file system. File names starting with . are ignored. The text files must be encoded as UTF-8.  

directory
    
HDFS directory to monitor for new file
  64. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#toString\(\):String "Permalink") def toString(): [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String") 

Definition Classes
    AnyRef → Any
  65. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#transform\[T\]\(dstreams:Seq\[org.apache.spark.streaming.dstream.DStream\[_\]\],transformFunc:\(Seq\[org.apache.spark.rdd.RDD\[_\]\],org.apache.spark.streaming.Time\)=>org.apache.spark.rdd.RDD\[T\]\)\(implicitevidence$16:scala.reflect.ClassTag\[T\]\):org.apache.spark.streaming.dstream.DStream\[T\] "Permalink") def transform[T](dstreams: Seq[[DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[_]], transformFunc: (Seq[[RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[_]], [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time")) => [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[T])(implicit arg0: ClassTag[T]): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[T]
Create a new DStream in which each RDD is generated by applying a function on RDDs of the DStreams.
  66. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#union\[T\]\(streams:Seq\[org.apache.spark.streaming.dstream.DStream\[T\]\]\)\(implicitevidence$15:scala.reflect.ClassTag\[T\]\):org.apache.spark.streaming.dstream.DStream\[T\] "Permalink") def union[T](streams: Seq[[DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[T]])(implicit arg0: ClassTag[T]): [DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream")[T]
Create a unified DStream from multiple DStreams of the same type and same slide duration.
  67. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  68. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  69. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#wait\(\):Unit "Permalink") final  def wait(): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  70. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#withLogContext\(context:java.util.Map\[String,String\]\)\(body:=>Unit\):Unit "Permalink") def withLogContext(context: [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#java.util.Map "java.util.Map")[String, String])(body: => Unit): Unit 

Attributes
    protected  

Definition Classes
    Logging
  71. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html#finalize\(\):Unit "Permalink") def finalize(): Unit 

Attributes
    protected[lang]  

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.Throwable]) @Deprecated 

Deprecated
    
_(Since version 9)_


