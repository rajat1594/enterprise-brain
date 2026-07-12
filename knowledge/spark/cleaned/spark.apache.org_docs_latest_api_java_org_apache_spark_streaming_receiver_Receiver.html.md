[Skip navigation links](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/receiver/Receiver.html#skip-navbar-top "Skip navigation links")
  * [Overview](https://spark.apache.org/docs/latest/api/java/index.html)
  * [Package](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/receiver/package-summary.html)
  * Class
  * [Deprecated](https://spark.apache.org/docs/latest/api/java/deprecated-list.html)
  * [Index](https://spark.apache.org/docs/latest/api/java/index-all.html)
  * [Help](https://spark.apache.org/docs/latest/api/java/help-doc.html#class)

  * Summary:
  * Nested |
  * Field |
  * [Constr](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/receiver/Receiver.html#constructor-summary) |
  * [Method](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/receiver/Receiver.html#method-summary)

  * Detail:
  * Field |
  * [Constr](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/receiver/Receiver.html#constructor-detail) |
  * [Method](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/receiver/Receiver.html#method-detail)

SEARCH:
Package [org.apache.spark.streaming.receiver](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/receiver/package-summary.html)
# Class Receiver<T>
[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")
org.apache.spark.streaming.receiver.Receiver<T>

All Implemented Interfaces:
    `Serializable[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html "class or interface in java.io")`
* * *
public abstract class Receiver<T> extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") implements [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html "class or interface in java.io")
Developer API Abstract class of a receiver that can be run on worker nodes to receive external data. A custom receiver can be defined by defining the functions `onStart()` and `onStop()`. `onStart()` should define the setup steps necessary to start receiving data, and `onStop()` should define the cleanup steps necessary to stop receiving data. Exceptions while receiving can be handled either by restarting the receiver with `restart(...)` or stopped completely by `stop(...)`.
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

See Also:

  * [Serialized Form](https://spark.apache.org/docs/latest/api/java/serialized-form.html#org.apache.spark.streaming.receiver.Receiver)

  * ## Constructor Summary
Constructors
Constructor
Description
`Receiver[](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/receiver/Receiver.html#%3Cinit%3E\(org.apache.spark.storage.StorageLevel\))(StorageLevel[](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/StorageLevel.html "class in org.apache.spark.storage") storageLevel)`
  * ## Method Summary
All MethodsInstance MethodsAbstract MethodsConcrete Methods
Modifier and Type
Method
Description
`boolean`
`isStarted[](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/receiver/Receiver.html#isStarted\(\))()`
Check if the receiver has started or not.
`boolean`
`isStopped[](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/receiver/Receiver.html#isStopped\(\))()`
Check if receiver has been marked for stopping.
`abstract void`
`onStart[](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/receiver/Receiver.html#onStart\(\))()`
This method is called by the system when the receiver is started.
`abstract void`
`onStop[](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/receiver/Receiver.html#onStop\(\))()`
This method is called by the system when the receiver is stopped.
`scala.Option<String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")>`
`preferredLocation[](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/receiver/Receiver.html#preferredLocation\(\))()`
Override this to specify a preferred location (hostname).
`void`
`reportError[](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/receiver/Receiver.html#reportError\(java.lang.String,java.lang.Throwable\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") message,  Throwable[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class or interface in java.lang") throwable)`
Report exceptions in receiving data.
`void`
`restart[](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/receiver/Receiver.html#restart\(java.lang.String\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") message)`
Restart the receiver.
`void`
`restart[](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/receiver/Receiver.html#restart\(java.lang.String,java.lang.Throwable\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") message,  Throwable[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class or interface in java.lang") error)`
Restart the receiver.
`void`
`restart[](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/receiver/Receiver.html#restart\(java.lang.String,java.lang.Throwable,int\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") message,  Throwable[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class or interface in java.lang") error,  int millisecond)`
Restart the receiver.
`void`
`stop[](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/receiver/Receiver.html#stop\(java.lang.String\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") message)`
Stop the receiver completely.
`void`
`stop[](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/receiver/Receiver.html#stop\(java.lang.String,java.lang.Throwable\))(String[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") message,  Throwable[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class or interface in java.lang") error)`
Stop the receiver completely due to an exception
`StorageLevel[](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/StorageLevel.html "class in org.apache.spark.storage")`
`storageLevel[](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/receiver/Receiver.html#storageLevel\(\))()`
`void`
`store[](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/receiver/Receiver.html#store\(java.nio.ByteBuffer\))(ByteBuffer[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/nio/ByteBuffer.html "class or interface in java.nio") bytes)`
Store the bytes of received data as a data block into Spark's memory.
`void`
`store[](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/receiver/Receiver.html#store\(java.nio.ByteBuffer,java.lang.Object\))(ByteBuffer[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/nio/ByteBuffer.html "class or interface in java.nio") bytes,  Object[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") metadata)`
Store the bytes of received data as a data block into Spark's memory.
`void`
`store[](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/receiver/Receiver.html#store\(java.util.Iterator\))(Iterator[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html "class or interface in java.util")<T[](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/receiver/Receiver.html "type parameter in Receiver")> dataIterator)`
Store an iterator of received data as a data block into Spark's memory.
`void`
`store[](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/receiver/Receiver.html#store\(java.util.Iterator,java.lang.Object\))(Iterator[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html "class or interface in java.util")<T[](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/receiver/Receiver.html "type parameter in Receiver")> dataIterator,  Object[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") metadata)`
Store an iterator of received data as a data block into Spark's memory.
`void`
`store[](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/receiver/Receiver.html#store\(scala.collection.Iterator\))(scala.collection.Iterator<T[](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/receiver/Receiver.html "type parameter in Receiver")> dataIterator)`
Store an iterator of received data as a data block into Spark's memory.
`void`
`store[](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/receiver/Receiver.html#store\(scala.collection.Iterator,java.lang.Object\))(scala.collection.Iterator<T[](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/receiver/Receiver.html "type parameter in Receiver")> dataIterator,  Object[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") metadata)`
Store an iterator of received data as a data block into Spark's memory.
`void`
`store[](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/receiver/Receiver.html#store\(scala.collection.mutable.ArrayBuffer\))(scala.collection.mutable.ArrayBuffer<T[](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/receiver/Receiver.html "type parameter in Receiver")> dataBuffer)`
Store an ArrayBuffer of received data as a data block into Spark's memory.
`void`
`store[](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/receiver/Receiver.html#store\(scala.collection.mutable.ArrayBuffer,java.lang.Object\))(scala.collection.mutable.ArrayBuffer<T[](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/receiver/Receiver.html "type parameter in Receiver")> dataBuffer,  Object[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") metadata)`
Store an ArrayBuffer of received data as a data block into Spark's memory.
`void`
`store[](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/receiver/Receiver.html#store\(T\))(T[](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/receiver/Receiver.html "type parameter in Receiver") dataItem)`
Store a single item of received data to Spark's memory.
`int`
`streamId[](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/receiver/Receiver.html#streamId\(\))()`
Get the unique identifier the receiver input stream that this receiver is associated with.
### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")
`equals[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), getClass[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), hashCode[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), notify[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), notifyAll[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), toString[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), wait[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), wait[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), wait[](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`

  * ## Constructor Details
    * ### Receiver
public Receiver([StorageLevel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/StorageLevel.html "class in org.apache.spark.storage") storageLevel)
  * ## Method Details
    * ### isStarted
public boolean isStarted()
Check if the receiver has started or not.
    * ### isStopped
public boolean isStopped()
Check if receiver has been marked for stopping. Use this to identify when the receiving of data should be stopped.

Returns:
    (undocumented)
    * ### onStart
public abstract void onStart()
This method is called by the system when the receiver is started. This function must initialize all resources (threads, buffers, etc.) necessary for receiving data. This function must be non-blocking, so receiving the data must occur on a different thread. Received data can be stored with Spark by calling `store(data)`.
If there are errors in threads started here, then following options can be done (i) `reportError(...)` can be called to report the error to the driver. The receiving of data will continue uninterrupted. (ii) `stop(...)` can be called to stop receiving data. This will call `onStop()` to clear up all resources allocated (threads, buffers, etc.) during `onStart()`. (iii) `restart(...)` can be called to restart the receiver. This will call `onStop()` immediately, and then `onStart()` after a delay.
    * ### onStop
public abstract void onStop()
This method is called by the system when the receiver is stopped. All resources (threads, buffers, etc.) set up in `onStart()` must be cleaned up in this method.
    * ### preferredLocation
public scala.Option<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> preferredLocation()
Override this to specify a preferred location (hostname).
    * ### reportError
public void reportError([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") message, [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class or interface in java.lang") throwable)
Report exceptions in receiving data.
    * ### restart
public void restart([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") message)
Restart the receiver. This method schedules the restart and returns immediately. The stopping and subsequent starting of the receiver (by calling `onStop()` and `onStart()`) is performed asynchronously in a background thread. The delay between the stopping and the starting is defined by the Spark configuration `spark.streaming.receiverRestartDelay`. The `message` will be reported to the driver.

Parameters:
     `message` - (undocumented)
    * ### restart
public void restart([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") message, [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class or interface in java.lang") error)
Restart the receiver. This method schedules the restart and returns immediately. The stopping and subsequent starting of the receiver (by calling `onStop()` and `onStart()`) is performed asynchronously in a background thread. The delay between the stopping and the starting is defined by the Spark configuration `spark.streaming.receiverRestartDelay`. The `message` and `exception` will be reported to the driver.

Parameters:
     `message` - (undocumented)      `error` - (undocumented)
    * ### restart
public void restart([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") message, [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class or interface in java.lang") error, int millisecond)
Restart the receiver. This method schedules the restart and returns immediately. The stopping and subsequent starting of the receiver (by calling `onStop()` and `onStart()`) is performed asynchronously in a background thread.

Parameters:
     `message` - (undocumented)      `error` - (undocumented)      `millisecond` - (undocumented)
    * ### stop
public void stop([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") message)
Stop the receiver completely.
    * ### stop
public void stop([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") message, [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class or interface in java.lang") error)
Stop the receiver completely due to an exception
    * ### storageLevel
public [StorageLevel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/StorageLevel.html "class in org.apache.spark.storage") storageLevel()
    * ### store
public void store([T](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/receiver/Receiver.html "type parameter in Receiver") dataItem)
Store a single item of received data to Spark's memory. These single items will be aggregated together into data blocks before being pushed into Spark's memory.

Parameters:
     `dataItem` - (undocumented)
    * ### store
public void store(scala.collection.mutable.ArrayBuffer<[T](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/receiver/Receiver.html "type parameter in Receiver")> dataBuffer)
Store an ArrayBuffer of received data as a data block into Spark's memory.
    * ### store
public void store(scala.collection.mutable.ArrayBuffer<[T](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/receiver/Receiver.html "type parameter in Receiver")> dataBuffer, [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") metadata)
Store an ArrayBuffer of received data as a data block into Spark's memory. The metadata will be associated with this block of data for being used in the corresponding InputDStream.

Parameters:
     `dataBuffer` - (undocumented)      `metadata` - (undocumented)
    * ### store
public void store(scala.collection.Iterator<[T](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/receiver/Receiver.html "type parameter in Receiver")> dataIterator)
Store an iterator of received data as a data block into Spark's memory.
    * ### store
public void store([Iterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html "class or interface in java.util")<[T](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/receiver/Receiver.html "type parameter in Receiver")> dataIterator, [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") metadata)
Store an iterator of received data as a data block into Spark's memory. The metadata will be associated with this block of data for being used in the corresponding InputDStream.

Parameters:
     `dataIterator` - (undocumented)      `metadata` - (undocumented)
    * ### store
public void store([Iterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html "class or interface in java.util")<[T](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/receiver/Receiver.html "type parameter in Receiver")> dataIterator)
Store an iterator of received data as a data block into Spark's memory.
    * ### store
public void store(scala.collection.Iterator<[T](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/receiver/Receiver.html "type parameter in Receiver")> dataIterator, [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") metadata)
Store an iterator of received data as a data block into Spark's memory. The metadata will be associated with this block of data for being used in the corresponding InputDStream.

Parameters:
     `dataIterator` - (undocumented)      `metadata` - (undocumented)
    * ### store
public void store([ByteBuffer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/nio/ByteBuffer.html "class or interface in java.nio") bytes)
Store the bytes of received data as a data block into Spark's memory. Note that the data in the ByteBuffer must be serialized using the same serializer that Spark is configured to use.

Parameters:
     `bytes` - (undocumented)
    * ### store
public void store([ByteBuffer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/nio/ByteBuffer.html "class or interface in java.nio") bytes, [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") metadata)
Store the bytes of received data as a data block into Spark's memory. The metadata will be associated with this block of data for being used in the corresponding InputDStream.

Parameters:
     `bytes` - (undocumented)      `metadata` - (undocumented)
    * ### streamId
public int streamId()
Get the unique identifier the receiver input stream that this receiver is associated with.

Returns:
    (undocumented)
