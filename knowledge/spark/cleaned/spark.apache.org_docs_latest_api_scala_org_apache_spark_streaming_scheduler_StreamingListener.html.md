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
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/index.html "Permalink") package [scheduler](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/index.html)

Definition Classes
    [streaming](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/index.html "org.apache.spark.streaming")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/rate/index.html "Permalink") package [rate](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/rate/index.html)

Definition Classes
    [scheduler](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/index.html "org.apache.spark.streaming.scheduler")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/BatchInfo.html ":: DeveloperApi :: Class having information on completed batches.")[BatchInfo](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/BatchInfo.html ":: DeveloperApi :: Class having information on completed batches.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/OutputOperationInfo.html ":: DeveloperApi :: Class having information on output operations.")[OutputOperationInfo](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/OutputOperationInfo.html ":: DeveloperApi :: Class having information on output operations.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/RateController$.html)[RateController](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/RateController$.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/ReceiverInfo.html ":: DeveloperApi :: Class having information about a receiver")[ReceiverInfo](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/ReceiverInfo.html ":: DeveloperApi :: Class having information about a receiver")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StatsReportListener.html ":: DeveloperApi :: A simple StreamingListener that logs summary statistics across Spark Streaming batches")[StatsReportListener](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StatsReportListener.html ":: DeveloperApi :: A simple StreamingListener that logs summary statistics across Spark Streaming batches")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamInputInfo$.html) [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamInputInfo.html ":: DeveloperApi :: Track the information of input stream at specified batch time.")[StreamInputInfo](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamInputInfo.html ":: DeveloperApi :: Track the information of input stream at specified batch time.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html ":: DeveloperApi :: A listener interface for receiving information about an ongoing streaming computation.")[StreamingListener](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html ":: DeveloperApi :: A listener interface for receiving information about an ongoing streaming computation.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListenerBatchCompleted.html)[StreamingListenerBatchCompleted](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListenerBatchCompleted.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListenerBatchStarted.html)[StreamingListenerBatchStarted](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListenerBatchStarted.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListenerBatchSubmitted.html)[StreamingListenerBatchSubmitted](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListenerBatchSubmitted.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListenerEvent.html ":: DeveloperApi :: Base trait for events related to StreamingListener")[StreamingListenerEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListenerEvent.html ":: DeveloperApi :: Base trait for events related to StreamingListener")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListenerOutputOperationCompleted.html)[StreamingListenerOutputOperationCompleted](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListenerOutputOperationCompleted.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListenerOutputOperationStarted.html)[StreamingListenerOutputOperationStarted](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListenerOutputOperationStarted.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListenerReceiverError.html)[StreamingListenerReceiverError](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListenerReceiverError.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListenerReceiverStarted.html)[StreamingListenerReceiverStarted](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListenerReceiverStarted.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListenerReceiverStopped.html)[StreamingListenerReceiverStopped](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListenerReceiverStopped.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListenerStreamingStarted.html)[StreamingListenerStreamingStarted](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListenerStreamingStarted.html)

t
[org](https://spark.apache.org/docs/latest/api/scala/org/index.html "org").[apache](https://spark.apache.org/docs/latest/api/scala/org/apache/index.html "org.apache").[spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark").[streaming](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/index.html "org.apache.spark.streaming").[scheduler](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/index.html "org.apache.spark.streaming.scheduler")
# StreamingListener[ __](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html "Permalink")
####  trait StreamingListener extends AnyRef
Developer API
A listener interface for receiving information about an ongoing streaming computation.

Annotations
     @DeveloperApi()

Source
    [StreamingListener.scala](https://github.com/apache/spark/tree/v4.1.2/streaming/src/main/scala/org/apache/spark/streaming/scheduler/StreamingListener.scala)
Linear Supertypes
AnyRef, Any
Known Subclasses
[StatsReportListener](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StatsReportListener.html "org.apache.spark.streaming.scheduler.StatsReportListener")
__ __
Ordering
  1. Alphabetic
  2. By Inheritance

Inherited

  1. StreamingListener
  2. AnyRef
  3. Any

  1. Hide All
  2. Show All

Visibility
  1. Public
  2. Protected

### Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html###:Int "Permalink") final  def ##: Int

Definition Classes
    AnyRef → Any
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0

Definition Classes
    Any
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html#clone\(\):Object "Permalink") def clone(): AnyRef

Attributes
    protected[lang]

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html#equals\(x$1:Object\):Boolean "Permalink") def equals(arg0: AnyRef): Boolean

Definition Classes
    AnyRef → Any
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef]

Definition Classes
    AnyRef → Any

Annotations
     @IntrinsicCandidate() @native()
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html#hashCode\(\):Int "Permalink") def hashCode(): Int

Definition Classes
    AnyRef → Any

Annotations
     @IntrinsicCandidate() @native()
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean

Definition Classes
    Any
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html#notify\(\):Unit "Permalink") final  def notify(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html#onBatchCompleted\(batchCompleted:org.apache.spark.streaming.scheduler.StreamingListenerBatchCompleted\):Unit "Permalink") def onBatchCompleted(batchCompleted: [StreamingListenerBatchCompleted](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListenerBatchCompleted.html "org.apache.spark.streaming.scheduler.StreamingListenerBatchCompleted")): Unit
Called when processing of a batch of jobs has completed.
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html#onBatchStarted\(batchStarted:org.apache.spark.streaming.scheduler.StreamingListenerBatchStarted\):Unit "Permalink") def onBatchStarted(batchStarted: [StreamingListenerBatchStarted](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListenerBatchStarted.html "org.apache.spark.streaming.scheduler.StreamingListenerBatchStarted")): Unit
Called when processing of a batch of jobs has started.
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html#onBatchSubmitted\(batchSubmitted:org.apache.spark.streaming.scheduler.StreamingListenerBatchSubmitted\):Unit "Permalink") def onBatchSubmitted(batchSubmitted: [StreamingListenerBatchSubmitted](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListenerBatchSubmitted.html "org.apache.spark.streaming.scheduler.StreamingListenerBatchSubmitted")): Unit
Called when a batch of jobs has been submitted for processing.
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html#onOutputOperationCompleted\(outputOperationCompleted:org.apache.spark.streaming.scheduler.StreamingListenerOutputOperationCompleted\):Unit "Permalink") def onOutputOperationCompleted(outputOperationCompleted: [StreamingListenerOutputOperationCompleted](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListenerOutputOperationCompleted.html "org.apache.spark.streaming.scheduler.StreamingListenerOutputOperationCompleted")): Unit
Called when processing of a job of a batch has completed.
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html#onOutputOperationStarted\(outputOperationStarted:org.apache.spark.streaming.scheduler.StreamingListenerOutputOperationStarted\):Unit "Permalink") def onOutputOperationStarted(outputOperationStarted: [StreamingListenerOutputOperationStarted](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListenerOutputOperationStarted.html "org.apache.spark.streaming.scheduler.StreamingListenerOutputOperationStarted")): Unit
Called when processing of a job of a batch has started.
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html#onReceiverError\(receiverError:org.apache.spark.streaming.scheduler.StreamingListenerReceiverError\):Unit "Permalink") def onReceiverError(receiverError: [StreamingListenerReceiverError](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListenerReceiverError.html "org.apache.spark.streaming.scheduler.StreamingListenerReceiverError")): Unit
Called when a receiver has reported an error
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html#onReceiverStarted\(receiverStarted:org.apache.spark.streaming.scheduler.StreamingListenerReceiverStarted\):Unit "Permalink") def onReceiverStarted(receiverStarted: [StreamingListenerReceiverStarted](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListenerReceiverStarted.html "org.apache.spark.streaming.scheduler.StreamingListenerReceiverStarted")): Unit
Called when a receiver has been started
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html#onReceiverStopped\(receiverStopped:org.apache.spark.streaming.scheduler.StreamingListenerReceiverStopped\):Unit "Permalink") def onReceiverStopped(receiverStopped: [StreamingListenerReceiverStopped](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListenerReceiverStopped.html "org.apache.spark.streaming.scheduler.StreamingListenerReceiverStopped")): Unit
Called when a receiver has been stopped
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html#onStreamingStarted\(streamingStarted:org.apache.spark.streaming.scheduler.StreamingListenerStreamingStarted\):Unit "Permalink") def onStreamingStarted(streamingStarted: [StreamingListenerStreamingStarted](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListenerStreamingStarted.html "org.apache.spark.streaming.scheduler.StreamingListenerStreamingStarted")): Unit
Called when the streaming has been started
  23. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0

Definition Classes
    AnyRef
  24. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html#toString\(\):String "Permalink") def toString(): [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String")

Definition Classes
    AnyRef → Any
  25. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])
  26. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  27. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html#wait\(\):Unit "Permalink") final  def wait(): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])

### Deprecated Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html#finalize\(\):Unit "Permalink") def finalize(): Unit

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
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html###:Int "Permalink") final  def ##: Int

Definition Classes
    AnyRef → Any
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html#clone\(\):Object "Permalink") def clone(): AnyRef

Attributes
    protected[lang]

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html#equals\(x$1:Object\):Boolean "Permalink") def equals(arg0: AnyRef): Boolean

Definition Classes
    AnyRef → Any
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef]

Definition Classes
    AnyRef → Any

Annotations
     @IntrinsicCandidate() @native()
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html#hashCode\(\):Int "Permalink") def hashCode(): Int

Definition Classes
    AnyRef → Any

Annotations
     @IntrinsicCandidate() @native()
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html#notify\(\):Unit "Permalink") final  def notify(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0

Definition Classes
    AnyRef
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html#toString\(\):String "Permalink") def toString(): [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String")

Definition Classes
    AnyRef → Any
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html#wait\(\):Unit "Permalink") final  def wait(): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html#finalize\(\):Unit "Permalink") def finalize(): Unit

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
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0

Definition Classes
    Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean

Definition Classes
    Any

### Ungrouped
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html###:Int "Permalink") final  def ##: Int

Definition Classes
    AnyRef → Any
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0

Definition Classes
    Any
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html#clone\(\):Object "Permalink") def clone(): AnyRef

Attributes
    protected[lang]

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html#equals\(x$1:Object\):Boolean "Permalink") def equals(arg0: AnyRef): Boolean

Definition Classes
    AnyRef → Any
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef]

Definition Classes
    AnyRef → Any

Annotations
     @IntrinsicCandidate() @native()
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html#hashCode\(\):Int "Permalink") def hashCode(): Int

Definition Classes
    AnyRef → Any

Annotations
     @IntrinsicCandidate() @native()
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean

Definition Classes
    Any
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html#notify\(\):Unit "Permalink") final  def notify(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html#onBatchCompleted\(batchCompleted:org.apache.spark.streaming.scheduler.StreamingListenerBatchCompleted\):Unit "Permalink") def onBatchCompleted(batchCompleted: [StreamingListenerBatchCompleted](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListenerBatchCompleted.html "org.apache.spark.streaming.scheduler.StreamingListenerBatchCompleted")): Unit
Called when processing of a batch of jobs has completed.
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html#onBatchStarted\(batchStarted:org.apache.spark.streaming.scheduler.StreamingListenerBatchStarted\):Unit "Permalink") def onBatchStarted(batchStarted: [StreamingListenerBatchStarted](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListenerBatchStarted.html "org.apache.spark.streaming.scheduler.StreamingListenerBatchStarted")): Unit
Called when processing of a batch of jobs has started.
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html#onBatchSubmitted\(batchSubmitted:org.apache.spark.streaming.scheduler.StreamingListenerBatchSubmitted\):Unit "Permalink") def onBatchSubmitted(batchSubmitted: [StreamingListenerBatchSubmitted](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListenerBatchSubmitted.html "org.apache.spark.streaming.scheduler.StreamingListenerBatchSubmitted")): Unit
Called when a batch of jobs has been submitted for processing.
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html#onOutputOperationCompleted\(outputOperationCompleted:org.apache.spark.streaming.scheduler.StreamingListenerOutputOperationCompleted\):Unit "Permalink") def onOutputOperationCompleted(outputOperationCompleted: [StreamingListenerOutputOperationCompleted](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListenerOutputOperationCompleted.html "org.apache.spark.streaming.scheduler.StreamingListenerOutputOperationCompleted")): Unit
Called when processing of a job of a batch has completed.
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html#onOutputOperationStarted\(outputOperationStarted:org.apache.spark.streaming.scheduler.StreamingListenerOutputOperationStarted\):Unit "Permalink") def onOutputOperationStarted(outputOperationStarted: [StreamingListenerOutputOperationStarted](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListenerOutputOperationStarted.html "org.apache.spark.streaming.scheduler.StreamingListenerOutputOperationStarted")): Unit
Called when processing of a job of a batch has started.
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html#onReceiverError\(receiverError:org.apache.spark.streaming.scheduler.StreamingListenerReceiverError\):Unit "Permalink") def onReceiverError(receiverError: [StreamingListenerReceiverError](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListenerReceiverError.html "org.apache.spark.streaming.scheduler.StreamingListenerReceiverError")): Unit
Called when a receiver has reported an error
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html#onReceiverStarted\(receiverStarted:org.apache.spark.streaming.scheduler.StreamingListenerReceiverStarted\):Unit "Permalink") def onReceiverStarted(receiverStarted: [StreamingListenerReceiverStarted](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListenerReceiverStarted.html "org.apache.spark.streaming.scheduler.StreamingListenerReceiverStarted")): Unit
Called when a receiver has been started
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html#onReceiverStopped\(receiverStopped:org.apache.spark.streaming.scheduler.StreamingListenerReceiverStopped\):Unit "Permalink") def onReceiverStopped(receiverStopped: [StreamingListenerReceiverStopped](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListenerReceiverStopped.html "org.apache.spark.streaming.scheduler.StreamingListenerReceiverStopped")): Unit
Called when a receiver has been stopped
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html#onStreamingStarted\(streamingStarted:org.apache.spark.streaming.scheduler.StreamingListenerStreamingStarted\):Unit "Permalink") def onStreamingStarted(streamingStarted: [StreamingListenerStreamingStarted](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListenerStreamingStarted.html "org.apache.spark.streaming.scheduler.StreamingListenerStreamingStarted")): Unit
Called when the streaming has been started
  23. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0

Definition Classes
    AnyRef
  24. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html#toString\(\):String "Permalink") def toString(): [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String")

Definition Classes
    AnyRef → Any
  25. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])
  26. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  27. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html#wait\(\):Unit "Permalink") final  def wait(): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])
  28. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/scheduler/StreamingListener.html#finalize\(\):Unit "Permalink") def finalize(): Unit

Attributes
    protected[lang]

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.Throwable]) @Deprecated

Deprecated

_(Since version 9)_
