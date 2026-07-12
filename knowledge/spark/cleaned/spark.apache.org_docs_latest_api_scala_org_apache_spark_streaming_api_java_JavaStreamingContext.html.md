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

[c](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext$.html "See companion object")
[org](https://spark.apache.org/docs/latest/api/scala/org/index.html "org").[apache](https://spark.apache.org/docs/latest/api/scala/org/apache/index.html "org.apache").[spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark").[streaming](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/index.html "org.apache.spark.streaming").[api](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/index.html "org.apache.spark.streaming.api").[java](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/index.html "org.apache.spark.streaming.api.java")
#  [JavaStreamingContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext$.html "See companion object")[ __](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html "Permalink")
###
Companion [object JavaStreamingContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext$.html "See companion object")
####  class JavaStreamingContext extends [Closeable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Closeable.html#java.io.Closeable "java.io.Closeable")
A Java-friendly version of [org.apache.spark.streaming.StreamingContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html "org.apache.spark.streaming.StreamingContext") which is the main entry point for Spark Streaming functionality. It provides methods to create [org.apache.spark.streaming.api.java.JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream") and [org.apache.spark.streaming.api.java.JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream") from input sources. The internal org.apache.spark.api.java.JavaSparkContext (see core Spark documentation) can be accessed using `context.sparkContext`. After creating and transforming DStreams, the streaming computation can be started and stopped using `context.start()` and `context.stop()`, respectively. `context.awaitTermination()` allows the current thread to wait for the termination of a context by `stop()` or by an exception.

Annotations
     @deprecated

Deprecated

_(Since version Spark 3.4.0)_ DStream is deprecated. Migrate to Structured Streaming.

Source
    [JavaStreamingContext.scala](https://github.com/apache/spark/tree/v4.1.2/streaming/src/main/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.scala)
Linear Supertypes
[Closeable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Closeable.html#java.io.Closeable "java.io.Closeable"), [AutoCloseable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/AutoCloseable.html#java.lang.AutoCloseable "java.lang.AutoCloseable"), AnyRef, Any
__ __
Ordering
  1. Alphabetic
  2. By Inheritance

Inherited

  1. JavaStreamingContext
  2. Closeable
  3. AutoCloseable
  4. AnyRef
  5. Any

  1. Hide All
  2. Show All

Visibility
  1. Public
  2. Protected

### Instance Constructors
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#<init>\(path:String,hadoopConf:org.apache.hadoop.conf.Configuration\):org.apache.spark.streaming.api.java.JavaStreamingContext "Permalink") new JavaStreamingContext(path: String, hadoopConf: Configuration)
Re-creates a JavaStreamingContext from a checkpoint file.
Re-creates a JavaStreamingContext from a checkpoint file.

path

Path to the directory that was specified as the checkpoint directory
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#<init>\(path:String\):org.apache.spark.streaming.api.java.JavaStreamingContext "Permalink") new JavaStreamingContext(path: String)
Recreate a JavaStreamingContext from a checkpoint file.
Recreate a JavaStreamingContext from a checkpoint file.

path

Path to the directory that was specified as the checkpoint directory
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#<init>\(conf:org.apache.spark.SparkConf,batchDuration:org.apache.spark.streaming.Duration\):org.apache.spark.streaming.api.java.JavaStreamingContext "Permalink") new JavaStreamingContext(conf: [SparkConf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkConf.html "org.apache.spark.SparkConf"), batchDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"))
Create a JavaStreamingContext using a SparkConf configuration.
Create a JavaStreamingContext using a SparkConf configuration.

conf

A Spark application configuration

batchDuration

The time interval at which streaming data will be divided into batches
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#<init>\(sparkContext:org.apache.spark.api.java.JavaSparkContext,batchDuration:org.apache.spark.streaming.Duration\):org.apache.spark.streaming.api.java.JavaStreamingContext "Permalink") new JavaStreamingContext(sparkContext: [JavaSparkContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaSparkContext.html "org.apache.spark.api.java.JavaSparkContext"), batchDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"))
Create a JavaStreamingContext using an existing JavaSparkContext.
Create a JavaStreamingContext using an existing JavaSparkContext.

sparkContext

The underlying JavaSparkContext to use

batchDuration

The time interval at which streaming data will be divided into batches
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#<init>\(master:String,appName:String,batchDuration:org.apache.spark.streaming.Duration,sparkHome:String,jars:Array\[String\],environment:java.util.Map\[String,String\]\):org.apache.spark.streaming.api.java.JavaStreamingContext "Permalink") new JavaStreamingContext(master: String, appName: String, batchDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), sparkHome: String, jars: Array[String], environment: [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#java.util.Map "java.util.Map")[String, String])
Create a StreamingContext.
Create a StreamingContext.

master

Name of the Spark Master

appName

Name to be used when registering with the scheduler

batchDuration

The time interval at which streaming data will be divided into batches

sparkHome

The SPARK_HOME directory on the worker nodes

jars

Collection of JARs to send to the cluster. These can be paths on the local file system or HDFS, HTTP, HTTPS, or FTP URLs.

environment

Environment variables to set on worker nodes
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#<init>\(master:String,appName:String,batchDuration:org.apache.spark.streaming.Duration,sparkHome:String,jars:Array\[String\]\):org.apache.spark.streaming.api.java.JavaStreamingContext "Permalink") new JavaStreamingContext(master: String, appName: String, batchDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), sparkHome: String, jars: Array[String])
Create a StreamingContext.
Create a StreamingContext.

master

Name of the Spark Master

appName

Name to be used when registering with the scheduler

batchDuration

The time interval at which streaming data will be divided into batches

sparkHome

The SPARK_HOME directory on the worker nodes

jars

Collection of JARs to send to the cluster. These can be paths on the local file system or HDFS, HTTP, HTTPS, or FTP URLs.
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#<init>\(master:String,appName:String,batchDuration:org.apache.spark.streaming.Duration,sparkHome:String,jarFile:String\):org.apache.spark.streaming.api.java.JavaStreamingContext "Permalink") new JavaStreamingContext(master: String, appName: String, batchDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"), sparkHome: String, jarFile: String)
Create a StreamingContext.
Create a StreamingContext.

master

Name of the Spark Master

appName

Name to be used when registering with the scheduler

batchDuration

The time interval at which streaming data will be divided into batches

sparkHome

The SPARK_HOME directory on the worker nodes

jarFile

JAR file containing job code, to ship to cluster. This can be a path on the local file system or an HDFS, HTTP, HTTPS, or FTP URL.
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#<init>\(master:String,appName:String,batchDuration:org.apache.spark.streaming.Duration\):org.apache.spark.streaming.api.java.JavaStreamingContext "Permalink") new JavaStreamingContext(master: String, appName: String, batchDuration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration"))
Create a StreamingContext.
Create a StreamingContext.

master

Name of the Spark Master

appName

Name to be used when registering with the scheduler

batchDuration

The time interval at which streaming data will be divided into batches
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#<init>\(ssc:org.apache.spark.streaming.StreamingContext\):org.apache.spark.streaming.api.java.JavaStreamingContext "Permalink") new JavaStreamingContext(ssc: [StreamingContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html "org.apache.spark.streaming.StreamingContext"))

Deprecated

This is deprecated as of Spark 3.4.0. There are no longer updates to DStream and it's a legacy project. There is a newer and easier to use streaming engine in Spark called Structured Streaming. You should use Spark Structured Streaming for your streaming applications.

### Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html###:Int "Permalink") final  def ##: Int

Definition Classes
    AnyRef → Any
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#addStreamingListener\(streamingListener:org.apache.spark.streaming.scheduler.StreamingListener\):Unit "Permalink") def addStreamingListener(streamingListener: [StreamingListener](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html "org.apache.spark.streaming.scheduler.StreamingListener")): Unit
Add a [org.apache.spark.streaming.scheduler.StreamingListener](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html "org.apache.spark.streaming.scheduler.StreamingListener") object for receiving system events related to streaming.
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0

Definition Classes
    Any
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#awaitTermination\(\):Unit "Permalink") def awaitTermination(): Unit
Wait for the execution to stop.
Wait for the execution to stop. Any exceptions that occurs during the execution will be thrown in this thread.

Annotations
     @throws("")
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#awaitTerminationOrTimeout\(timeout:Long\):Boolean "Permalink") def awaitTerminationOrTimeout(timeout: Long): Boolean
Wait for the execution to stop.
Wait for the execution to stop. Any exceptions that occurs during the execution will be thrown in this thread.

timeout

time to wait in milliseconds

returns

`true` if it's stopped; or throw the reported error during the execution; or `false` if the waiting time elapsed before returning from the method.

Annotations
     @throws("")
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#binaryRecordsStream\(directory:String,recordLength:Int\):org.apache.spark.streaming.api.java.JavaDStream\[Array\[Byte\]\] "Permalink") def binaryRecordsStream(directory: String, recordLength: Int): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[Array[Byte]]
Create an input stream that monitors a Hadoop-compatible filesystem for new files and reads them as flat binary files with fixed record lengths, yielding byte arrays
Create an input stream that monitors a Hadoop-compatible filesystem for new files and reads them as flat binary files with fixed record lengths, yielding byte arrays

directory

HDFS directory to monitor for new files

recordLength

The length at which to split the records

Note

We ensure that the byte array for each record in the resulting RDDs of the DStream has the provided record length.
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#checkpoint\(directory:String\):Unit "Permalink") def checkpoint(directory: String): Unit
Sets the context to periodically checkpoint the DStream operations for master fault-tolerance.
Sets the context to periodically checkpoint the DStream operations for master fault-tolerance. The graph will be checkpointed every batch interval.

directory

HDFS-compatible directory where the checkpoint data will be reliably stored
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#clone\(\):Object "Permalink") def clone(): AnyRef

Attributes
    protected[lang]

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#close\(\):Unit "Permalink") def close(): Unit

Definition Classes
     [JavaStreamingContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html "org.apache.spark.streaming.api.java.JavaStreamingContext") → Closeable → AutoCloseable
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#equals\(x$1:Object\):Boolean "Permalink") def equals(arg0: AnyRef): Boolean

Definition Classes
    AnyRef → Any
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#fileStream\[K,V,F<:org.apache.hadoop.mapreduce.InputFormat\[K,V\]\]\(directory:String,kClass:Class\[K\],vClass:Class\[V\],fClass:Class\[F\],filter:org.apache.spark.api.java.function.Function\[org.apache.hadoop.fs.Path,Boolean\],newFilesOnly:Boolean,conf:org.apache.hadoop.conf.Configuration\):org.apache.spark.streaming.api.java.JavaPairInputDStream\[K,V\] "Permalink") def fileStream[K, V, F <: InputFormat[K, V]](directory: String, kClass: Class[K], vClass: Class[V], fClass: Class[F], filter: [Function](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function.html "org.apache.spark.api.java.function.Function")[Path, [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html#java.lang.Boolean "java.lang.Boolean")], newFilesOnly: Boolean, conf: Configuration): [JavaPairInputDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairInputDStream.html "org.apache.spark.streaming.api.java.JavaPairInputDStream")[K, V]
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

kClass

class of key for reading HDFS file

vClass

class of value for reading HDFS file

fClass

class of input format for reading HDFS file

filter

Function to filter paths to process

newFilesOnly

Should process only new files and ignore existing files in the directory

conf

Hadoop configuration
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#fileStream\[K,V,F<:org.apache.hadoop.mapreduce.InputFormat\[K,V\]\]\(directory:String,kClass:Class\[K\],vClass:Class\[V\],fClass:Class\[F\],filter:org.apache.spark.api.java.function.Function\[org.apache.hadoop.fs.Path,Boolean\],newFilesOnly:Boolean\):org.apache.spark.streaming.api.java.JavaPairInputDStream\[K,V\] "Permalink") def fileStream[K, V, F <: InputFormat[K, V]](directory: String, kClass: Class[K], vClass: Class[V], fClass: Class[F], filter: [Function](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function.html "org.apache.spark.api.java.function.Function")[Path, [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html#java.lang.Boolean "java.lang.Boolean")], newFilesOnly: Boolean): [JavaPairInputDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairInputDStream.html "org.apache.spark.streaming.api.java.JavaPairInputDStream")[K, V]
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

kClass

class of key for reading HDFS file

vClass

class of value for reading HDFS file

fClass

class of input format for reading HDFS file

filter

Function to filter paths to process

newFilesOnly

Should process only new files and ignore existing files in the directory
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#fileStream\[K,V,F<:org.apache.hadoop.mapreduce.InputFormat\[K,V\]\]\(directory:String,kClass:Class\[K\],vClass:Class\[V\],fClass:Class\[F\]\):org.apache.spark.streaming.api.java.JavaPairInputDStream\[K,V\] "Permalink") def fileStream[K, V, F <: InputFormat[K, V]](directory: String, kClass: Class[K], vClass: Class[V], fClass: Class[F]): [JavaPairInputDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairInputDStream.html "org.apache.spark.streaming.api.java.JavaPairInputDStream")[K, V]
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

kClass

class of key for reading HDFS file

vClass

class of value for reading HDFS file

fClass

class of input format for reading HDFS file
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef]

Definition Classes
    AnyRef → Any

Annotations
     @IntrinsicCandidate() @native()
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#getState\(\):org.apache.spark.streaming.StreamingContextState "Permalink") def getState(): [StreamingContextState](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContextState.html "org.apache.spark.streaming.StreamingContextState")
Return the current state of the context. The context can be in three possible states -
- StreamingContextState.INITIALIZED - The context has been created, but not been started yet. Input DStreams, transformations and output operations can be created on the context.
- StreamingContextState.ACTIVE - The context has been started, and been not stopped. Input DStreams, transformations and output operations cannot be created on the context.
- StreamingContextState.STOPPED - The context has been stopped and cannot be used any more.
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#hashCode\(\):Int "Permalink") def hashCode(): Int

Definition Classes
    AnyRef → Any

Annotations
     @IntrinsicCandidate() @native()
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean

Definition Classes
    Any
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#notify\(\):Unit "Permalink") final  def notify(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  23. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  24. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#queueStream\[T\]\(queue:java.util.Queue\[org.apache.spark.api.java.JavaRDD\[T\]\],oneAtATime:Boolean,defaultRDD:org.apache.spark.api.java.JavaRDD\[T\]\):org.apache.spark.streaming.api.java.JavaInputDStream\[T\] "Permalink") def queueStream[T](queue: [Queue](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Queue.html#java.util.Queue "java.util.Queue")[[JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[T]], oneAtATime: Boolean, defaultRDD: [JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[T]): [JavaInputDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaInputDStream.html "org.apache.spark.streaming.api.java.JavaInputDStream")[T]
Create an input stream from a queue of RDDs.
Create an input stream from a queue of RDDs. In each batch, it will process either one or all of the RDDs returned by the queue.

T

Type of objects in the RDD

queue

Queue of RDDs

oneAtATime

Whether only one RDD should be consumed from the queue in every interval

defaultRDD

Default RDD is returned by the DStream when the queue is empty

Note

1. Changes to the queue after the stream is created will not be recognized. 2. Arbitrary RDDs can be added to `queueStream`, there is no way to recover data of those RDDs, so `queueStream` doesn't support checkpointing.
  25. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#queueStream\[T\]\(queue:java.util.Queue\[org.apache.spark.api.java.JavaRDD\[T\]\],oneAtATime:Boolean\):org.apache.spark.streaming.api.java.JavaInputDStream\[T\] "Permalink") def queueStream[T](queue: [Queue](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Queue.html#java.util.Queue "java.util.Queue")[[JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[T]], oneAtATime: Boolean): [JavaInputDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaInputDStream.html "org.apache.spark.streaming.api.java.JavaInputDStream")[T]
Create an input stream from a queue of RDDs.
Create an input stream from a queue of RDDs. In each batch, it will process either one or all of the RDDs returned by the queue.

T

Type of objects in the RDD

queue

Queue of RDDs

oneAtATime

Whether only one RDD should be consumed from the queue in every interval

Note

1. Changes to the queue after the stream is created will not be recognized. 2. Arbitrary RDDs can be added to `queueStream`, there is no way to recover data of those RDDs, so `queueStream` doesn't support checkpointing.
  26. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#queueStream\[T\]\(queue:java.util.Queue\[org.apache.spark.api.java.JavaRDD\[T\]\]\):org.apache.spark.streaming.api.java.JavaDStream\[T\] "Permalink") def queueStream[T](queue: [Queue](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Queue.html#java.util.Queue "java.util.Queue")[[JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[T]]): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[T]
Create an input stream from a queue of RDDs.
Create an input stream from a queue of RDDs. In each batch, it will process either one or all of the RDDs returned by the queue.

T

Type of objects in the RDD

queue

Queue of RDDs

Note

1. Changes to the queue after the stream is created will not be recognized. 2. Arbitrary RDDs can be added to `queueStream`, there is no way to recover data of those RDDs, so `queueStream` doesn't support checkpointing.
  27. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#rawSocketStream\[T\]\(hostname:String,port:Int\):org.apache.spark.streaming.api.java.JavaReceiverInputDStream\[T\] "Permalink") def rawSocketStream[T](hostname: String, port: Int): [JavaReceiverInputDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaReceiverInputDStream.html "org.apache.spark.streaming.api.java.JavaReceiverInputDStream")[T]
Create an input stream from network source hostname:port, where data is received as serialized blocks (serialized using the Spark's serializer) that can be directly pushed into the block manager without deserializing them.
Create an input stream from network source hostname:port, where data is received as serialized blocks (serialized using the Spark's serializer) that can be directly pushed into the block manager without deserializing them. This is the most efficient way to receive data.

T

Type of the objects in the received blocks

hostname

Hostname to connect to for receiving data

port

Port to connect to for receiving data
  28. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#rawSocketStream\[T\]\(hostname:String,port:Int,storageLevel:org.apache.spark.storage.StorageLevel\):org.apache.spark.streaming.api.java.JavaReceiverInputDStream\[T\] "Permalink") def rawSocketStream[T](hostname: String, port: Int, storageLevel: [StorageLevel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StorageLevel.html "org.apache.spark.storage.StorageLevel")): [JavaReceiverInputDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaReceiverInputDStream.html "org.apache.spark.streaming.api.java.JavaReceiverInputDStream")[T]
Create an input stream from network source hostname:port, where data is received as serialized blocks (serialized using the Spark's serializer) that can be directly pushed into the block manager without deserializing them.
Create an input stream from network source hostname:port, where data is received as serialized blocks (serialized using the Spark's serializer) that can be directly pushed into the block manager without deserializing them. This is the most efficient way to receive data.

T

Type of the objects in the received blocks

hostname

Hostname to connect to for receiving data

port

Port to connect to for receiving data

storageLevel

Storage level to use for storing the received objects
  29. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#receiverStream\[T\]\(receiver:org.apache.spark.streaming.receiver.Receiver\[T\]\):org.apache.spark.streaming.api.java.JavaReceiverInputDStream\[T\] "Permalink") def receiverStream[T](receiver: [Receiver](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html "org.apache.spark.streaming.receiver.Receiver")[T]): [JavaReceiverInputDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaReceiverInputDStream.html "org.apache.spark.streaming.api.java.JavaReceiverInputDStream")[T]
Create an input stream with any arbitrary user implemented receiver.
Create an input stream with any arbitrary user implemented receiver. Find more details at: https://spark.apache.org/docs/latest/streaming-custom-receivers.html

receiver

Custom implementation of Receiver
  30. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#remember\(duration:org.apache.spark.streaming.Duration\):Unit "Permalink") def remember(duration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration")): Unit
Sets each DStreams in this context to remember RDDs it generated in the last given duration.
Sets each DStreams in this context to remember RDDs it generated in the last given duration. DStreams remember RDDs only for a limited duration of duration and releases them for garbage collection. This method allows the developer to specify how long to remember the RDDs ( if the developer wishes to query old data outside the DStream computation).

duration

Minimum duration that each DStream should remember its RDDs
  31. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#socketStream\[T\]\(hostname:String,port:Int,converter:org.apache.spark.api.java.function.Function\[java.io.InputStream,Iterable\[T\]\],storageLevel:org.apache.spark.storage.StorageLevel\):org.apache.spark.streaming.api.java.JavaReceiverInputDStream\[T\] "Permalink") def socketStream[T](hostname: String, port: Int, converter: [Function](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function.html "org.apache.spark.api.java.function.Function")[[InputStream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html#java.io.InputStream "java.io.InputStream"), [Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html#java.lang.Iterable "java.lang.Iterable")[T]], storageLevel: [StorageLevel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StorageLevel.html "org.apache.spark.storage.StorageLevel")): [JavaReceiverInputDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaReceiverInputDStream.html "org.apache.spark.streaming.api.java.JavaReceiverInputDStream")[T]
Create an input stream from network source hostname:port.
Create an input stream from network source hostname:port. Data is received using a TCP socket and the receive bytes it interpreted as object using the given converter.

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
  32. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#socketTextStream\(hostname:String,port:Int\):org.apache.spark.streaming.api.java.JavaReceiverInputDStream\[String\] "Permalink") def socketTextStream(hostname: String, port: Int): [JavaReceiverInputDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaReceiverInputDStream.html "org.apache.spark.streaming.api.java.JavaReceiverInputDStream")[String]
Create an input stream from network source hostname:port.
Create an input stream from network source hostname:port. Data is received using a TCP socket and the receive bytes is interpreted as UTF8 encoded \n delimited lines. Storage level of the data will be the default StorageLevel.MEMORY_AND_DISK_SER_2.

hostname

Hostname to connect to for receiving data

port

Port to connect to for receiving data
  33. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#socketTextStream\(hostname:String,port:Int,storageLevel:org.apache.spark.storage.StorageLevel\):org.apache.spark.streaming.api.java.JavaReceiverInputDStream\[String\] "Permalink") def socketTextStream(hostname: String, port: Int, storageLevel: [StorageLevel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StorageLevel.html "org.apache.spark.storage.StorageLevel")): [JavaReceiverInputDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaReceiverInputDStream.html "org.apache.spark.streaming.api.java.JavaReceiverInputDStream")[String]
Create an input stream from network source hostname:port.
Create an input stream from network source hostname:port. Data is received using a TCP socket and the receive bytes is interpreted as UTF8 encoded \n delimited lines.

hostname

Hostname to connect to for receiving data

port

Port to connect to for receiving data

storageLevel

Storage level to use for storing the received objects
  34. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#sparkContext:org.apache.spark.api.java.JavaSparkContext "Permalink") val sparkContext: [JavaSparkContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaSparkContext.html "org.apache.spark.api.java.JavaSparkContext")
The underlying SparkContext
  35. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#ssc:org.apache.spark.streaming.StreamingContext "Permalink") val ssc: [StreamingContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html "org.apache.spark.streaming.StreamingContext")
  36. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#start\(\):Unit "Permalink") def start(): Unit
Start the execution of the streams.
  37. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#stop\(stopSparkContext:Boolean,stopGracefully:Boolean\):Unit "Permalink") def stop(stopSparkContext: Boolean, stopGracefully: Boolean): Unit
Stop the execution of the streams.
Stop the execution of the streams.

stopSparkContext

Stop the associated SparkContext or not

stopGracefully

Stop gracefully by waiting for the processing of all received data to be completed
  38. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#stop\(stopSparkContext:Boolean\):Unit "Permalink") def stop(stopSparkContext: Boolean): Unit
Stop the execution of the streams.
Stop the execution of the streams.

stopSparkContext

Stop the associated SparkContext or not
  39. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#stop\(\):Unit "Permalink") def stop(): Unit
Stop the execution of the streams.
Stop the execution of the streams. Will stop the associated JavaSparkContext as well.
  40. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0

Definition Classes
    AnyRef
  41. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#textFileStream\(directory:String\):org.apache.spark.streaming.api.java.JavaDStream\[String\] "Permalink") def textFileStream(directory: String): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[String]
Create an input stream that monitors a Hadoop-compatible filesystem for new files and reads them as text files (using key as LongWritable, value as Text and input format as TextInputFormat).
Create an input stream that monitors a Hadoop-compatible filesystem for new files and reads them as text files (using key as LongWritable, value as Text and input format as TextInputFormat). Files must be written to the monitored directory by "moving" them from another location within the same file system. File names starting with . are ignored. The text files must be encoded as UTF-8.

directory

HDFS directory to monitor for new file
  42. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#toString\(\):String "Permalink") def toString(): [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String")

Definition Classes
    AnyRef → Any
  43. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#transform\[T\]\(dstreams:java.util.List\[org.apache.spark.streaming.api.java.JavaDStream\[_\]\],transformFunc:org.apache.spark.api.java.function.Function2\[java.util.List\[org.apache.spark.api.java.JavaRDD\[_\]\],org.apache.spark.streaming.Time,org.apache.spark.api.java.JavaRDD\[T\]\]\):org.apache.spark.streaming.api.java.JavaDStream\[T\] "Permalink") def transform[T](dstreams: [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#java.util.List "java.util.List")[[JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[_]], transformFunc: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#java.util.List "java.util.List")[[JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[_]], [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time"), [JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[T]]): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[T]
Create a new DStream in which each RDD is generated by applying a function on RDDs of the DStreams.
Create a new DStream in which each RDD is generated by applying a function on RDDs of the DStreams. The order of the JavaRDDs in the transform function parameter will be the same as the order of corresponding DStreams in the list.

Note

For adding a JavaPairDStream in the list of JavaDStreams, convert it to a JavaDStream using [org.apache.spark.streaming.api.java.JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream").toJavaDStream(). In the transform function, convert the JavaRDD corresponding to that JavaDStream to a JavaPairRDD using org.apache.spark.api.java.JavaPairRDD.fromJavaRDD().
  44. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#transformToPair\[K,V\]\(dstreams:java.util.List\[org.apache.spark.streaming.api.java.JavaDStream\[_\]\],transformFunc:org.apache.spark.api.java.function.Function2\[java.util.List\[org.apache.spark.api.java.JavaRDD\[_\]\],org.apache.spark.streaming.Time,org.apache.spark.api.java.JavaPairRDD\[K,V\]\]\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,V\] "Permalink") def transformToPair[K, V](dstreams: [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#java.util.List "java.util.List")[[JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[_]], transformFunc: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#java.util.List "java.util.List")[[JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[_]], [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time"), [JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K, V]]): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, V]
Create a new DStream in which each RDD is generated by applying a function on RDDs of the DStreams.
Create a new DStream in which each RDD is generated by applying a function on RDDs of the DStreams. The order of the JavaRDDs in the transform function parameter will be the same as the order of corresponding DStreams in the list.

Note

For adding a JavaPairDStream in the list of JavaDStreams, convert it to a JavaDStream using [org.apache.spark.streaming.api.java.JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream").toJavaDStream(). In the transform function, convert the JavaRDD corresponding to that JavaDStream to a JavaPairRDD using org.apache.spark.api.java.JavaPairRDD.fromJavaRDD().
  45. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#union\[K,V\]\(jdstreams:org.apache.spark.streaming.api.java.JavaPairDStream\[K,V\]*\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,V\] "Permalink") def union[K, V](jdstreams: [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, V]*): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, V]
Create a unified DStream from multiple DStreams of the same type and same slide duration.
Create a unified DStream from multiple DStreams of the same type and same slide duration.

Annotations
     @varargs()
  46. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#union\[T\]\(jdstreams:org.apache.spark.streaming.api.java.JavaDStream\[T\]*\):org.apache.spark.streaming.api.java.JavaDStream\[T\] "Permalink") def union[T](jdstreams: [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[T]*): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[T]
Create a unified DStream from multiple DStreams of the same type and same slide duration.
Create a unified DStream from multiple DStreams of the same type and same slide duration.

Annotations
     @varargs()
  47. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])
  48. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  49. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#wait\(\):Unit "Permalink") final  def wait(): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])

### Deprecated Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#finalize\(\):Unit "Permalink") def finalize(): Unit

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
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html###:Int "Permalink") final  def ##: Int

Definition Classes
    AnyRef → Any
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#clone\(\):Object "Permalink") def clone(): AnyRef

Attributes
    protected[lang]

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#equals\(x$1:Object\):Boolean "Permalink") def equals(arg0: AnyRef): Boolean

Definition Classes
    AnyRef → Any
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef]

Definition Classes
    AnyRef → Any

Annotations
     @IntrinsicCandidate() @native()
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#hashCode\(\):Int "Permalink") def hashCode(): Int

Definition Classes
    AnyRef → Any

Annotations
     @IntrinsicCandidate() @native()
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#notify\(\):Unit "Permalink") final  def notify(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0

Definition Classes
    AnyRef
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#toString\(\):String "Permalink") def toString(): [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String")

Definition Classes
    AnyRef → Any
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#wait\(\):Unit "Permalink") final  def wait(): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#finalize\(\):Unit "Permalink") def finalize(): Unit

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
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0

Definition Classes
    Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean

Definition Classes
    Any

### Ungrouped
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html###:Int "Permalink") final  def ##: Int

Definition Classes
    AnyRef → Any
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#addStreamingListener\(streamingListener:org.apache.spark.streaming.scheduler.StreamingListener\):Unit "Permalink") def addStreamingListener(streamingListener: [StreamingListener](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html "org.apache.spark.streaming.scheduler.StreamingListener")): Unit
Add a [org.apache.spark.streaming.scheduler.StreamingListener](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html "org.apache.spark.streaming.scheduler.StreamingListener") object for receiving system events related to streaming.
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0

Definition Classes
    Any
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#awaitTermination\(\):Unit "Permalink") def awaitTermination(): Unit
Wait for the execution to stop.
Wait for the execution to stop. Any exceptions that occurs during the execution will be thrown in this thread.

Annotations
     @throws("")
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#awaitTerminationOrTimeout\(timeout:Long\):Boolean "Permalink") def awaitTerminationOrTimeout(timeout: Long): Boolean
Wait for the execution to stop.
Wait for the execution to stop. Any exceptions that occurs during the execution will be thrown in this thread.

timeout

time to wait in milliseconds

returns

`true` if it's stopped; or throw the reported error during the execution; or `false` if the waiting time elapsed before returning from the method.

Annotations
     @throws("")
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#binaryRecordsStream\(directory:String,recordLength:Int\):org.apache.spark.streaming.api.java.JavaDStream\[Array\[Byte\]\] "Permalink") def binaryRecordsStream(directory: String, recordLength: Int): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[Array[Byte]]
Create an input stream that monitors a Hadoop-compatible filesystem for new files and reads them as flat binary files with fixed record lengths, yielding byte arrays
Create an input stream that monitors a Hadoop-compatible filesystem for new files and reads them as flat binary files with fixed record lengths, yielding byte arrays

directory

HDFS directory to monitor for new files

recordLength

The length at which to split the records

Note

We ensure that the byte array for each record in the resulting RDDs of the DStream has the provided record length.
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#checkpoint\(directory:String\):Unit "Permalink") def checkpoint(directory: String): Unit
Sets the context to periodically checkpoint the DStream operations for master fault-tolerance.
Sets the context to periodically checkpoint the DStream operations for master fault-tolerance. The graph will be checkpointed every batch interval.

directory

HDFS-compatible directory where the checkpoint data will be reliably stored
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#clone\(\):Object "Permalink") def clone(): AnyRef

Attributes
    protected[lang]

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#close\(\):Unit "Permalink") def close(): Unit

Definition Classes
     [JavaStreamingContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html "org.apache.spark.streaming.api.java.JavaStreamingContext") → Closeable → AutoCloseable
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#equals\(x$1:Object\):Boolean "Permalink") def equals(arg0: AnyRef): Boolean

Definition Classes
    AnyRef → Any
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#fileStream\[K,V,F<:org.apache.hadoop.mapreduce.InputFormat\[K,V\]\]\(directory:String,kClass:Class\[K\],vClass:Class\[V\],fClass:Class\[F\],filter:org.apache.spark.api.java.function.Function\[org.apache.hadoop.fs.Path,Boolean\],newFilesOnly:Boolean,conf:org.apache.hadoop.conf.Configuration\):org.apache.spark.streaming.api.java.JavaPairInputDStream\[K,V\] "Permalink") def fileStream[K, V, F <: InputFormat[K, V]](directory: String, kClass: Class[K], vClass: Class[V], fClass: Class[F], filter: [Function](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function.html "org.apache.spark.api.java.function.Function")[Path, [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html#java.lang.Boolean "java.lang.Boolean")], newFilesOnly: Boolean, conf: Configuration): [JavaPairInputDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairInputDStream.html "org.apache.spark.streaming.api.java.JavaPairInputDStream")[K, V]
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

kClass

class of key for reading HDFS file

vClass

class of value for reading HDFS file

fClass

class of input format for reading HDFS file

filter

Function to filter paths to process

newFilesOnly

Should process only new files and ignore existing files in the directory

conf

Hadoop configuration
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#fileStream\[K,V,F<:org.apache.hadoop.mapreduce.InputFormat\[K,V\]\]\(directory:String,kClass:Class\[K\],vClass:Class\[V\],fClass:Class\[F\],filter:org.apache.spark.api.java.function.Function\[org.apache.hadoop.fs.Path,Boolean\],newFilesOnly:Boolean\):org.apache.spark.streaming.api.java.JavaPairInputDStream\[K,V\] "Permalink") def fileStream[K, V, F <: InputFormat[K, V]](directory: String, kClass: Class[K], vClass: Class[V], fClass: Class[F], filter: [Function](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function.html "org.apache.spark.api.java.function.Function")[Path, [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html#java.lang.Boolean "java.lang.Boolean")], newFilesOnly: Boolean): [JavaPairInputDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairInputDStream.html "org.apache.spark.streaming.api.java.JavaPairInputDStream")[K, V]
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

kClass

class of key for reading HDFS file

vClass

class of value for reading HDFS file

fClass

class of input format for reading HDFS file

filter

Function to filter paths to process

newFilesOnly

Should process only new files and ignore existing files in the directory
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#fileStream\[K,V,F<:org.apache.hadoop.mapreduce.InputFormat\[K,V\]\]\(directory:String,kClass:Class\[K\],vClass:Class\[V\],fClass:Class\[F\]\):org.apache.spark.streaming.api.java.JavaPairInputDStream\[K,V\] "Permalink") def fileStream[K, V, F <: InputFormat[K, V]](directory: String, kClass: Class[K], vClass: Class[V], fClass: Class[F]): [JavaPairInputDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairInputDStream.html "org.apache.spark.streaming.api.java.JavaPairInputDStream")[K, V]
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

kClass

class of key for reading HDFS file

vClass

class of value for reading HDFS file

fClass

class of input format for reading HDFS file
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef]

Definition Classes
    AnyRef → Any

Annotations
     @IntrinsicCandidate() @native()
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#getState\(\):org.apache.spark.streaming.StreamingContextState "Permalink") def getState(): [StreamingContextState](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContextState.html "org.apache.spark.streaming.StreamingContextState")
Return the current state of the context. The context can be in three possible states -
- StreamingContextState.INITIALIZED - The context has been created, but not been started yet. Input DStreams, transformations and output operations can be created on the context.
- StreamingContextState.ACTIVE - The context has been started, and been not stopped. Input DStreams, transformations and output operations cannot be created on the context.
- StreamingContextState.STOPPED - The context has been stopped and cannot be used any more.
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#hashCode\(\):Int "Permalink") def hashCode(): Int

Definition Classes
    AnyRef → Any

Annotations
     @IntrinsicCandidate() @native()
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean

Definition Classes
    Any
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#notify\(\):Unit "Permalink") final  def notify(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  23. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  24. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#queueStream\[T\]\(queue:java.util.Queue\[org.apache.spark.api.java.JavaRDD\[T\]\],oneAtATime:Boolean,defaultRDD:org.apache.spark.api.java.JavaRDD\[T\]\):org.apache.spark.streaming.api.java.JavaInputDStream\[T\] "Permalink") def queueStream[T](queue: [Queue](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Queue.html#java.util.Queue "java.util.Queue")[[JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[T]], oneAtATime: Boolean, defaultRDD: [JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[T]): [JavaInputDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaInputDStream.html "org.apache.spark.streaming.api.java.JavaInputDStream")[T]
Create an input stream from a queue of RDDs.
Create an input stream from a queue of RDDs. In each batch, it will process either one or all of the RDDs returned by the queue.

T

Type of objects in the RDD

queue

Queue of RDDs

oneAtATime

Whether only one RDD should be consumed from the queue in every interval

defaultRDD

Default RDD is returned by the DStream when the queue is empty

Note

1. Changes to the queue after the stream is created will not be recognized. 2. Arbitrary RDDs can be added to `queueStream`, there is no way to recover data of those RDDs, so `queueStream` doesn't support checkpointing.
  25. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#queueStream\[T\]\(queue:java.util.Queue\[org.apache.spark.api.java.JavaRDD\[T\]\],oneAtATime:Boolean\):org.apache.spark.streaming.api.java.JavaInputDStream\[T\] "Permalink") def queueStream[T](queue: [Queue](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Queue.html#java.util.Queue "java.util.Queue")[[JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[T]], oneAtATime: Boolean): [JavaInputDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaInputDStream.html "org.apache.spark.streaming.api.java.JavaInputDStream")[T]
Create an input stream from a queue of RDDs.
Create an input stream from a queue of RDDs. In each batch, it will process either one or all of the RDDs returned by the queue.

T

Type of objects in the RDD

queue

Queue of RDDs

oneAtATime

Whether only one RDD should be consumed from the queue in every interval

Note

1. Changes to the queue after the stream is created will not be recognized. 2. Arbitrary RDDs can be added to `queueStream`, there is no way to recover data of those RDDs, so `queueStream` doesn't support checkpointing.
  26. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#queueStream\[T\]\(queue:java.util.Queue\[org.apache.spark.api.java.JavaRDD\[T\]\]\):org.apache.spark.streaming.api.java.JavaDStream\[T\] "Permalink") def queueStream[T](queue: [Queue](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Queue.html#java.util.Queue "java.util.Queue")[[JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[T]]): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[T]
Create an input stream from a queue of RDDs.
Create an input stream from a queue of RDDs. In each batch, it will process either one or all of the RDDs returned by the queue.

T

Type of objects in the RDD

queue

Queue of RDDs

Note

1. Changes to the queue after the stream is created will not be recognized. 2. Arbitrary RDDs can be added to `queueStream`, there is no way to recover data of those RDDs, so `queueStream` doesn't support checkpointing.
  27. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#rawSocketStream\[T\]\(hostname:String,port:Int\):org.apache.spark.streaming.api.java.JavaReceiverInputDStream\[T\] "Permalink") def rawSocketStream[T](hostname: String, port: Int): [JavaReceiverInputDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaReceiverInputDStream.html "org.apache.spark.streaming.api.java.JavaReceiverInputDStream")[T]
Create an input stream from network source hostname:port, where data is received as serialized blocks (serialized using the Spark's serializer) that can be directly pushed into the block manager without deserializing them.
Create an input stream from network source hostname:port, where data is received as serialized blocks (serialized using the Spark's serializer) that can be directly pushed into the block manager without deserializing them. This is the most efficient way to receive data.

T

Type of the objects in the received blocks

hostname

Hostname to connect to for receiving data

port

Port to connect to for receiving data
  28. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#rawSocketStream\[T\]\(hostname:String,port:Int,storageLevel:org.apache.spark.storage.StorageLevel\):org.apache.spark.streaming.api.java.JavaReceiverInputDStream\[T\] "Permalink") def rawSocketStream[T](hostname: String, port: Int, storageLevel: [StorageLevel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StorageLevel.html "org.apache.spark.storage.StorageLevel")): [JavaReceiverInputDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaReceiverInputDStream.html "org.apache.spark.streaming.api.java.JavaReceiverInputDStream")[T]
Create an input stream from network source hostname:port, where data is received as serialized blocks (serialized using the Spark's serializer) that can be directly pushed into the block manager without deserializing them.
Create an input stream from network source hostname:port, where data is received as serialized blocks (serialized using the Spark's serializer) that can be directly pushed into the block manager without deserializing them. This is the most efficient way to receive data.

T

Type of the objects in the received blocks

hostname

Hostname to connect to for receiving data

port

Port to connect to for receiving data

storageLevel

Storage level to use for storing the received objects
  29. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#receiverStream\[T\]\(receiver:org.apache.spark.streaming.receiver.Receiver\[T\]\):org.apache.spark.streaming.api.java.JavaReceiverInputDStream\[T\] "Permalink") def receiverStream[T](receiver: [Receiver](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html "org.apache.spark.streaming.receiver.Receiver")[T]): [JavaReceiverInputDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaReceiverInputDStream.html "org.apache.spark.streaming.api.java.JavaReceiverInputDStream")[T]
Create an input stream with any arbitrary user implemented receiver.
Create an input stream with any arbitrary user implemented receiver. Find more details at: https://spark.apache.org/docs/latest/streaming-custom-receivers.html

receiver

Custom implementation of Receiver
  30. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#remember\(duration:org.apache.spark.streaming.Duration\):Unit "Permalink") def remember(duration: [Duration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Duration.html "org.apache.spark.streaming.Duration")): Unit
Sets each DStreams in this context to remember RDDs it generated in the last given duration.
Sets each DStreams in this context to remember RDDs it generated in the last given duration. DStreams remember RDDs only for a limited duration of duration and releases them for garbage collection. This method allows the developer to specify how long to remember the RDDs ( if the developer wishes to query old data outside the DStream computation).

duration

Minimum duration that each DStream should remember its RDDs
  31. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#socketStream\[T\]\(hostname:String,port:Int,converter:org.apache.spark.api.java.function.Function\[java.io.InputStream,Iterable\[T\]\],storageLevel:org.apache.spark.storage.StorageLevel\):org.apache.spark.streaming.api.java.JavaReceiverInputDStream\[T\] "Permalink") def socketStream[T](hostname: String, port: Int, converter: [Function](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function.html "org.apache.spark.api.java.function.Function")[[InputStream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html#java.io.InputStream "java.io.InputStream"), [Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html#java.lang.Iterable "java.lang.Iterable")[T]], storageLevel: [StorageLevel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StorageLevel.html "org.apache.spark.storage.StorageLevel")): [JavaReceiverInputDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaReceiverInputDStream.html "org.apache.spark.streaming.api.java.JavaReceiverInputDStream")[T]
Create an input stream from network source hostname:port.
Create an input stream from network source hostname:port. Data is received using a TCP socket and the receive bytes it interpreted as object using the given converter.

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
  32. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#socketTextStream\(hostname:String,port:Int\):org.apache.spark.streaming.api.java.JavaReceiverInputDStream\[String\] "Permalink") def socketTextStream(hostname: String, port: Int): [JavaReceiverInputDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaReceiverInputDStream.html "org.apache.spark.streaming.api.java.JavaReceiverInputDStream")[String]
Create an input stream from network source hostname:port.
Create an input stream from network source hostname:port. Data is received using a TCP socket and the receive bytes is interpreted as UTF8 encoded \n delimited lines. Storage level of the data will be the default StorageLevel.MEMORY_AND_DISK_SER_2.

hostname

Hostname to connect to for receiving data

port

Port to connect to for receiving data
  33. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#socketTextStream\(hostname:String,port:Int,storageLevel:org.apache.spark.storage.StorageLevel\):org.apache.spark.streaming.api.java.JavaReceiverInputDStream\[String\] "Permalink") def socketTextStream(hostname: String, port: Int, storageLevel: [StorageLevel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StorageLevel.html "org.apache.spark.storage.StorageLevel")): [JavaReceiverInputDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaReceiverInputDStream.html "org.apache.spark.streaming.api.java.JavaReceiverInputDStream")[String]
Create an input stream from network source hostname:port.
Create an input stream from network source hostname:port. Data is received using a TCP socket and the receive bytes is interpreted as UTF8 encoded \n delimited lines.

hostname

Hostname to connect to for receiving data

port

Port to connect to for receiving data

storageLevel

Storage level to use for storing the received objects
  34. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#sparkContext:org.apache.spark.api.java.JavaSparkContext "Permalink") val sparkContext: [JavaSparkContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaSparkContext.html "org.apache.spark.api.java.JavaSparkContext")
The underlying SparkContext
  35. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#ssc:org.apache.spark.streaming.StreamingContext "Permalink") val ssc: [StreamingContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html "org.apache.spark.streaming.StreamingContext")
  36. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#start\(\):Unit "Permalink") def start(): Unit
Start the execution of the streams.
  37. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#stop\(stopSparkContext:Boolean,stopGracefully:Boolean\):Unit "Permalink") def stop(stopSparkContext: Boolean, stopGracefully: Boolean): Unit
Stop the execution of the streams.
Stop the execution of the streams.

stopSparkContext

Stop the associated SparkContext or not

stopGracefully

Stop gracefully by waiting for the processing of all received data to be completed
  38. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#stop\(stopSparkContext:Boolean\):Unit "Permalink") def stop(stopSparkContext: Boolean): Unit
Stop the execution of the streams.
Stop the execution of the streams.

stopSparkContext

Stop the associated SparkContext or not
  39. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#stop\(\):Unit "Permalink") def stop(): Unit
Stop the execution of the streams.
Stop the execution of the streams. Will stop the associated JavaSparkContext as well.
  40. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0

Definition Classes
    AnyRef
  41. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#textFileStream\(directory:String\):org.apache.spark.streaming.api.java.JavaDStream\[String\] "Permalink") def textFileStream(directory: String): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[String]
Create an input stream that monitors a Hadoop-compatible filesystem for new files and reads them as text files (using key as LongWritable, value as Text and input format as TextInputFormat).
Create an input stream that monitors a Hadoop-compatible filesystem for new files and reads them as text files (using key as LongWritable, value as Text and input format as TextInputFormat). Files must be written to the monitored directory by "moving" them from another location within the same file system. File names starting with . are ignored. The text files must be encoded as UTF-8.

directory

HDFS directory to monitor for new file
  42. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#toString\(\):String "Permalink") def toString(): [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String")

Definition Classes
    AnyRef → Any
  43. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#transform\[T\]\(dstreams:java.util.List\[org.apache.spark.streaming.api.java.JavaDStream\[_\]\],transformFunc:org.apache.spark.api.java.function.Function2\[java.util.List\[org.apache.spark.api.java.JavaRDD\[_\]\],org.apache.spark.streaming.Time,org.apache.spark.api.java.JavaRDD\[T\]\]\):org.apache.spark.streaming.api.java.JavaDStream\[T\] "Permalink") def transform[T](dstreams: [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#java.util.List "java.util.List")[[JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[_]], transformFunc: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#java.util.List "java.util.List")[[JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[_]], [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time"), [JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[T]]): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[T]
Create a new DStream in which each RDD is generated by applying a function on RDDs of the DStreams.
Create a new DStream in which each RDD is generated by applying a function on RDDs of the DStreams. The order of the JavaRDDs in the transform function parameter will be the same as the order of corresponding DStreams in the list.

Note

For adding a JavaPairDStream in the list of JavaDStreams, convert it to a JavaDStream using [org.apache.spark.streaming.api.java.JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream").toJavaDStream(). In the transform function, convert the JavaRDD corresponding to that JavaDStream to a JavaPairRDD using org.apache.spark.api.java.JavaPairRDD.fromJavaRDD().
  44. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#transformToPair\[K,V\]\(dstreams:java.util.List\[org.apache.spark.streaming.api.java.JavaDStream\[_\]\],transformFunc:org.apache.spark.api.java.function.Function2\[java.util.List\[org.apache.spark.api.java.JavaRDD\[_\]\],org.apache.spark.streaming.Time,org.apache.spark.api.java.JavaPairRDD\[K,V\]\]\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,V\] "Permalink") def transformToPair[K, V](dstreams: [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#java.util.List "java.util.List")[[JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[_]], transformFunc: [Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "org.apache.spark.api.java.function.Function2")[[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#java.util.List "java.util.List")[[JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[_]], [Time](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/Time.html "org.apache.spark.streaming.Time"), [JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K, V]]): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, V]
Create a new DStream in which each RDD is generated by applying a function on RDDs of the DStreams.
Create a new DStream in which each RDD is generated by applying a function on RDDs of the DStreams. The order of the JavaRDDs in the transform function parameter will be the same as the order of corresponding DStreams in the list.

Note

For adding a JavaPairDStream in the list of JavaDStreams, convert it to a JavaDStream using [org.apache.spark.streaming.api.java.JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream").toJavaDStream(). In the transform function, convert the JavaRDD corresponding to that JavaDStream to a JavaPairRDD using org.apache.spark.api.java.JavaPairRDD.fromJavaRDD().
  45. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#union\[K,V\]\(jdstreams:org.apache.spark.streaming.api.java.JavaPairDStream\[K,V\]*\):org.apache.spark.streaming.api.java.JavaPairDStream\[K,V\] "Permalink") def union[K, V](jdstreams: [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, V]*): [JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream")[K, V]
Create a unified DStream from multiple DStreams of the same type and same slide duration.
Create a unified DStream from multiple DStreams of the same type and same slide duration.

Annotations
     @varargs()
  46. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#union\[T\]\(jdstreams:org.apache.spark.streaming.api.java.JavaDStream\[T\]*\):org.apache.spark.streaming.api.java.JavaDStream\[T\] "Permalink") def union[T](jdstreams: [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[T]*): [JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream")[T]
Create a unified DStream from multiple DStreams of the same type and same slide duration.
Create a unified DStream from multiple DStreams of the same type and same slide duration.

Annotations
     @varargs()
  47. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])
  48. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  49. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#wait\(\):Unit "Permalink") final  def wait(): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])
  50. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html#finalize\(\):Unit "Permalink") def finalize(): Unit

Attributes
    protected[lang]

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.Throwable]) @Deprecated

Deprecated

_(Since version 9)_
