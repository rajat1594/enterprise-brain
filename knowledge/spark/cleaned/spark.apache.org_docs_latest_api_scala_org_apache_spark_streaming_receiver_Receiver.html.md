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
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/index.html "Permalink") package [receiver](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/index.html)

Definition Classes
    [streaming](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/index.html "org.apache.spark.streaming")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html ":: DeveloperApi :: Abstract class of a receiver that can be run on worker nodes to receive external data.")[Receiver](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html ":: DeveloperApi :: Abstract class of a receiver that can be run on worker nodes to receive external data.")

c
[org](https://spark.apache.org/docs/latest/api/scala/org/index.html "org").[apache](https://spark.apache.org/docs/latest/api/scala/org/apache/index.html "org.apache").[spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark").[streaming](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/index.html "org.apache.spark.streaming").[receiver](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/index.html "org.apache.spark.streaming.receiver")
# Receiver[ __](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html "Permalink")
####  abstract  class Receiver[T] extends Serializable
Developer API
Abstract class of a receiver that can be run on worker nodes to receive external data. A custom receiver can be defined by defining the functions `onStart()` and `onStop()`. `onStart()` should define the setup steps necessary to start receiving data, and `onStop()` should define the cleanup steps necessary to stop receiving data. Exceptions while receiving can be handled either by restarting the receiver with `restart(...)` or stopped completely by `stop(...)`.
A custom receiver in Scala would look like this.

```
class MyReceiver(storageLevel: StorageLevel) extends NetworkReceiver[String](storageLevel) {
    def onStart() {
        // Setup stuff (start threads, open sockets, etc.) to start receiving data.
        // Must start new thread to receive data, as onStart() must be non-blocking.

        // Call store(...) in those threads to store received data into Spark's memory.

        // Call stop(...), restart(...) or reportError(...) on any thread based on how
        // different errors need to be handled.

        // See corresponding method documentation for more details
    }

    def onStop() {
        // Cleanup stuff (stop threads, close sockets, etc.) to stop receiving data.
    }
}
```

A custom receiver in Java would look like this.

```
class MyReceiver extends Receiver<String> {
    public MyReceiver(StorageLevel storageLevel) {
        super(storageLevel);
    }

    public void onStart() {
         // Setup stuff (start threads, open sockets, etc.) to start receiving data.
         // Must start new thread to receive data, as onStart() must be non-blocking.

         // Call store(...) in those threads to store received data into Spark's memory.

         // Call stop(...), restart(...) or reportError(...) on any thread based on how
         // different errors need to be handled.

         // See corresponding method documentation for more details
    }

    public void onStop() {
         // Cleanup stuff (stop threads, close sockets, etc.) to stop receiving data.
    }
}
```

Annotations
     @DeveloperApi()

Source
    [Receiver.scala](https://github.com/apache/spark/tree/v4.1.2/streaming/src/main/scala/org/apache/spark/streaming/receiver/Receiver.scala)
Linear Supertypes
[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable"), AnyRef, Any
__ __
Ordering
  1. Alphabetic
  2. By Inheritance

Inherited

  1. Receiver
  2. Serializable
  3. AnyRef
  4. Any

  1. Hide All
  2. Show All

Visibility
  1. Public
  2. Protected

### Instance Constructors
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#<init>\(storageLevel:org.apache.spark.storage.StorageLevel\):org.apache.spark.streaming.receiver.Receiver\[T\] "Permalink") new Receiver(storageLevel: [StorageLevel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StorageLevel.html "org.apache.spark.storage.StorageLevel"))

### Abstract Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#onStart\(\):Unit "Permalink") abstract  def onStart(): Unit
This method is called by the system when the receiver is started.
This method is called by the system when the receiver is started. This function must initialize all resources (threads, buffers, etc.) necessary for receiving data. This function must be non-blocking, so receiving the data must occur on a different thread. Received data can be stored with Spark by calling `store(data)`.
If there are errors in threads started here, then following options can be done (i) `reportError(...)` can be called to report the error to the driver. The receiving of data will continue uninterrupted. (ii) `stop(...)` can be called to stop receiving data. This will call `onStop()` to clear up all resources allocated (threads, buffers, etc.) during `onStart()`. (iii) `restart(...)` can be called to restart the receiver. This will call `onStop()` immediately, and then `onStart()` after a delay.
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#onStop\(\):Unit "Permalink") abstract  def onStop(): Unit
This method is called by the system when the receiver is stopped.
This method is called by the system when the receiver is stopped. All resources (threads, buffers, etc.) set up in `onStart()` must be cleaned up in this method.

### Concrete Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html###:Int "Permalink") final  def ##: Int

Definition Classes
    AnyRef → Any
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0

Definition Classes
    Any
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#clone\(\):Object "Permalink") def clone(): AnyRef

Attributes
    protected[lang]

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#equals\(x$1:Object\):Boolean "Permalink") def equals(arg0: AnyRef): Boolean

Definition Classes
    AnyRef → Any
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef]

Definition Classes
    AnyRef → Any

Annotations
     @IntrinsicCandidate() @native()
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#hashCode\(\):Int "Permalink") def hashCode(): Int

Definition Classes
    AnyRef → Any

Annotations
     @IntrinsicCandidate() @native()
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean

Definition Classes
    Any
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#isStarted\(\):Boolean "Permalink") def isStarted(): Boolean
Check if the receiver has started or not.
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#isStopped\(\):Boolean "Permalink") def isStopped(): Boolean
Check if receiver has been marked for stopping.
Check if receiver has been marked for stopping. Use this to identify when the receiving of data should be stopped.
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#notify\(\):Unit "Permalink") final  def notify(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#preferredLocation:Option\[String\] "Permalink") def preferredLocation: Option[String]
Override this to specify a preferred location (hostname).
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#reportError\(message:String,throwable:Throwable\):Unit "Permalink") def reportError(message: String, throwable: Throwable): Unit
Report exceptions in receiving data.
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#restart\(message:String,error:Throwable,millisecond:Int\):Unit "Permalink") def restart(message: String, error: Throwable, millisecond: Int): Unit
Restart the receiver.
Restart the receiver. This method schedules the restart and returns immediately. The stopping and subsequent starting of the receiver (by calling `onStop()` and `onStart()`) is performed asynchronously in a background thread.
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#restart\(message:String,error:Throwable\):Unit "Permalink") def restart(message: String, error: Throwable): Unit
Restart the receiver.
Restart the receiver. This method schedules the restart and returns immediately. The stopping and subsequent starting of the receiver (by calling `onStop()` and `onStart()`) is performed asynchronously in a background thread. The delay between the stopping and the starting is defined by the Spark configuration `spark.streaming.receiverRestartDelay`. The `message` and `exception` will be reported to the driver.
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#restart\(message:String\):Unit "Permalink") def restart(message: String): Unit
Restart the receiver.
Restart the receiver. This method schedules the restart and returns immediately. The stopping and subsequent starting of the receiver (by calling `onStop()` and `onStart()`) is performed asynchronously in a background thread. The delay between the stopping and the starting is defined by the Spark configuration `spark.streaming.receiverRestartDelay`. The `message` will be reported to the driver.
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#stop\(message:String,error:Throwable\):Unit "Permalink") def stop(message: String, error: Throwable): Unit
Stop the receiver completely due to an exception
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#stop\(message:String\):Unit "Permalink") def stop(message: String): Unit
Stop the receiver completely.
  23. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#storageLevel:org.apache.spark.storage.StorageLevel "Permalink") val storageLevel: [StorageLevel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StorageLevel.html "org.apache.spark.storage.StorageLevel")
  24. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#store\(bytes:java.nio.ByteBuffer,metadata:Any\):Unit "Permalink") def store(bytes: [ByteBuffer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/nio/ByteBuffer.html#java.nio.ByteBuffer "java.nio.ByteBuffer"), metadata: Any): Unit
Store the bytes of received data as a data block into Spark's memory.
Store the bytes of received data as a data block into Spark's memory. The metadata will be associated with this block of data for being used in the corresponding InputDStream.
  25. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#store\(bytes:java.nio.ByteBuffer\):Unit "Permalink") def store(bytes: [ByteBuffer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/nio/ByteBuffer.html#java.nio.ByteBuffer "java.nio.ByteBuffer")): Unit
Store the bytes of received data as a data block into Spark's memory.
Store the bytes of received data as a data block into Spark's memory. Note that the data in the ByteBuffer must be serialized using the same serializer that Spark is configured to use.
  26. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#store\(dataIterator:Iterator\[T\],metadata:Any\):Unit "Permalink") def store(dataIterator: Iterator[T], metadata: Any): Unit
Store an iterator of received data as a data block into Spark's memory.
Store an iterator of received data as a data block into Spark's memory. The metadata will be associated with this block of data for being used in the corresponding InputDStream.
  27. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#store\(dataIterator:java.util.Iterator\[T\]\):Unit "Permalink") def store(dataIterator: [Iterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html#java.util.Iterator "java.util.Iterator")[T]): Unit
Store an iterator of received data as a data block into Spark's memory.
  28. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#store\(dataIterator:java.util.Iterator\[T\],metadata:Any\):Unit "Permalink") def store(dataIterator: [Iterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html#java.util.Iterator "java.util.Iterator")[T], metadata: Any): Unit
Store an iterator of received data as a data block into Spark's memory.
Store an iterator of received data as a data block into Spark's memory. The metadata will be associated with this block of data for being used in the corresponding InputDStream.
  29. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#store\(dataIterator:Iterator\[T\]\):Unit "Permalink") def store(dataIterator: Iterator[T]): Unit
Store an iterator of received data as a data block into Spark's memory.
  30. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#store\(dataBuffer:scala.collection.mutable.ArrayBuffer\[T\],metadata:Any\):Unit "Permalink") def store(dataBuffer: ArrayBuffer[T], metadata: Any): Unit
Store an ArrayBuffer of received data as a data block into Spark's memory.
Store an ArrayBuffer of received data as a data block into Spark's memory. The metadata will be associated with this block of data for being used in the corresponding InputDStream.
  31. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#store\(dataBuffer:scala.collection.mutable.ArrayBuffer\[T\]\):Unit "Permalink") def store(dataBuffer: ArrayBuffer[T]): Unit
Store an ArrayBuffer of received data as a data block into Spark's memory.
  32. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#store\(dataItem:T\):Unit "Permalink") def store(dataItem: T): Unit
Store a single item of received data to Spark's memory.
Store a single item of received data to Spark's memory. These single items will be aggregated together into data blocks before being pushed into Spark's memory.
  33. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#streamId:Int "Permalink") def streamId: Int
Get the unique identifier the receiver input stream that this receiver is associated with.
  34. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0

Definition Classes
    AnyRef
  35. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#toString\(\):String "Permalink") def toString(): [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String")

Definition Classes
    AnyRef → Any
  36. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])
  37. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  38. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#wait\(\):Unit "Permalink") final  def wait(): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])

### Deprecated Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#finalize\(\):Unit "Permalink") def finalize(): Unit

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
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html###:Int "Permalink") final  def ##: Int

Definition Classes
    AnyRef → Any
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#clone\(\):Object "Permalink") def clone(): AnyRef

Attributes
    protected[lang]

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#equals\(x$1:Object\):Boolean "Permalink") def equals(arg0: AnyRef): Boolean

Definition Classes
    AnyRef → Any
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef]

Definition Classes
    AnyRef → Any

Annotations
     @IntrinsicCandidate() @native()
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#hashCode\(\):Int "Permalink") def hashCode(): Int

Definition Classes
    AnyRef → Any

Annotations
     @IntrinsicCandidate() @native()
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#notify\(\):Unit "Permalink") final  def notify(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0

Definition Classes
    AnyRef
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#toString\(\):String "Permalink") def toString(): [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String")

Definition Classes
    AnyRef → Any
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#wait\(\):Unit "Permalink") final  def wait(): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#finalize\(\):Unit "Permalink") def finalize(): Unit

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
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0

Definition Classes
    Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean

Definition Classes
    Any

### Ungrouped
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#onStart\(\):Unit "Permalink") abstract  def onStart(): Unit
This method is called by the system when the receiver is started.
This method is called by the system when the receiver is started. This function must initialize all resources (threads, buffers, etc.) necessary for receiving data. This function must be non-blocking, so receiving the data must occur on a different thread. Received data can be stored with Spark by calling `store(data)`.
If there are errors in threads started here, then following options can be done (i) `reportError(...)` can be called to report the error to the driver. The receiving of data will continue uninterrupted. (ii) `stop(...)` can be called to stop receiving data. This will call `onStop()` to clear up all resources allocated (threads, buffers, etc.) during `onStart()`. (iii) `restart(...)` can be called to restart the receiver. This will call `onStop()` immediately, and then `onStart()` after a delay.
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#onStop\(\):Unit "Permalink") abstract  def onStop(): Unit
This method is called by the system when the receiver is stopped.
This method is called by the system when the receiver is stopped. All resources (threads, buffers, etc.) set up in `onStart()` must be cleaned up in this method.
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html###:Int "Permalink") final  def ##: Int

Definition Classes
    AnyRef → Any
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0

Definition Classes
    Any
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#clone\(\):Object "Permalink") def clone(): AnyRef

Attributes
    protected[lang]

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#equals\(x$1:Object\):Boolean "Permalink") def equals(arg0: AnyRef): Boolean

Definition Classes
    AnyRef → Any
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef]

Definition Classes
    AnyRef → Any

Annotations
     @IntrinsicCandidate() @native()
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#hashCode\(\):Int "Permalink") def hashCode(): Int

Definition Classes
    AnyRef → Any

Annotations
     @IntrinsicCandidate() @native()
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean

Definition Classes
    Any
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#isStarted\(\):Boolean "Permalink") def isStarted(): Boolean
Check if the receiver has started or not.
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#isStopped\(\):Boolean "Permalink") def isStopped(): Boolean
Check if receiver has been marked for stopping.
Check if receiver has been marked for stopping. Use this to identify when the receiving of data should be stopped.
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#notify\(\):Unit "Permalink") final  def notify(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#preferredLocation:Option\[String\] "Permalink") def preferredLocation: Option[String]
Override this to specify a preferred location (hostname).
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#reportError\(message:String,throwable:Throwable\):Unit "Permalink") def reportError(message: String, throwable: Throwable): Unit
Report exceptions in receiving data.
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#restart\(message:String,error:Throwable,millisecond:Int\):Unit "Permalink") def restart(message: String, error: Throwable, millisecond: Int): Unit
Restart the receiver.
Restart the receiver. This method schedules the restart and returns immediately. The stopping and subsequent starting of the receiver (by calling `onStop()` and `onStart()`) is performed asynchronously in a background thread.
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#restart\(message:String,error:Throwable\):Unit "Permalink") def restart(message: String, error: Throwable): Unit
Restart the receiver.
Restart the receiver. This method schedules the restart and returns immediately. The stopping and subsequent starting of the receiver (by calling `onStop()` and `onStart()`) is performed asynchronously in a background thread. The delay between the stopping and the starting is defined by the Spark configuration `spark.streaming.receiverRestartDelay`. The `message` and `exception` will be reported to the driver.
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#restart\(message:String\):Unit "Permalink") def restart(message: String): Unit
Restart the receiver.
Restart the receiver. This method schedules the restart and returns immediately. The stopping and subsequent starting of the receiver (by calling `onStop()` and `onStart()`) is performed asynchronously in a background thread. The delay between the stopping and the starting is defined by the Spark configuration `spark.streaming.receiverRestartDelay`. The `message` will be reported to the driver.
  23. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#stop\(message:String,error:Throwable\):Unit "Permalink") def stop(message: String, error: Throwable): Unit
Stop the receiver completely due to an exception
  24. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#stop\(message:String\):Unit "Permalink") def stop(message: String): Unit
Stop the receiver completely.
  25. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#storageLevel:org.apache.spark.storage.StorageLevel "Permalink") val storageLevel: [StorageLevel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StorageLevel.html "org.apache.spark.storage.StorageLevel")
  26. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#store\(bytes:java.nio.ByteBuffer,metadata:Any\):Unit "Permalink") def store(bytes: [ByteBuffer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/nio/ByteBuffer.html#java.nio.ByteBuffer "java.nio.ByteBuffer"), metadata: Any): Unit
Store the bytes of received data as a data block into Spark's memory.
Store the bytes of received data as a data block into Spark's memory. The metadata will be associated with this block of data for being used in the corresponding InputDStream.
  27. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#store\(bytes:java.nio.ByteBuffer\):Unit "Permalink") def store(bytes: [ByteBuffer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/nio/ByteBuffer.html#java.nio.ByteBuffer "java.nio.ByteBuffer")): Unit
Store the bytes of received data as a data block into Spark's memory.
Store the bytes of received data as a data block into Spark's memory. Note that the data in the ByteBuffer must be serialized using the same serializer that Spark is configured to use.
  28. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#store\(dataIterator:Iterator\[T\],metadata:Any\):Unit "Permalink") def store(dataIterator: Iterator[T], metadata: Any): Unit
Store an iterator of received data as a data block into Spark's memory.
Store an iterator of received data as a data block into Spark's memory. The metadata will be associated with this block of data for being used in the corresponding InputDStream.
  29. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#store\(dataIterator:java.util.Iterator\[T\]\):Unit "Permalink") def store(dataIterator: [Iterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html#java.util.Iterator "java.util.Iterator")[T]): Unit
Store an iterator of received data as a data block into Spark's memory.
  30. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#store\(dataIterator:java.util.Iterator\[T\],metadata:Any\):Unit "Permalink") def store(dataIterator: [Iterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html#java.util.Iterator "java.util.Iterator")[T], metadata: Any): Unit
Store an iterator of received data as a data block into Spark's memory.
Store an iterator of received data as a data block into Spark's memory. The metadata will be associated with this block of data for being used in the corresponding InputDStream.
  31. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#store\(dataIterator:Iterator\[T\]\):Unit "Permalink") def store(dataIterator: Iterator[T]): Unit
Store an iterator of received data as a data block into Spark's memory.
  32. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#store\(dataBuffer:scala.collection.mutable.ArrayBuffer\[T\],metadata:Any\):Unit "Permalink") def store(dataBuffer: ArrayBuffer[T], metadata: Any): Unit
Store an ArrayBuffer of received data as a data block into Spark's memory.
Store an ArrayBuffer of received data as a data block into Spark's memory. The metadata will be associated with this block of data for being used in the corresponding InputDStream.
  33. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#store\(dataBuffer:scala.collection.mutable.ArrayBuffer\[T\]\):Unit "Permalink") def store(dataBuffer: ArrayBuffer[T]): Unit
Store an ArrayBuffer of received data as a data block into Spark's memory.
  34. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#store\(dataItem:T\):Unit "Permalink") def store(dataItem: T): Unit
Store a single item of received data to Spark's memory.
Store a single item of received data to Spark's memory. These single items will be aggregated together into data blocks before being pushed into Spark's memory.
  35. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#streamId:Int "Permalink") def streamId: Int
Get the unique identifier the receiver input stream that this receiver is associated with.
  36. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0

Definition Classes
    AnyRef
  37. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#toString\(\):String "Permalink") def toString(): [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String")

Definition Classes
    AnyRef → Any
  38. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])
  39. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  40. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#wait\(\):Unit "Permalink") final  def wait(): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])
  41. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html#finalize\(\):Unit "Permalink") def finalize(): Unit

Attributes
    protected[lang]

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.Throwable]) @Deprecated

Deprecated

_(Since version 9)_
