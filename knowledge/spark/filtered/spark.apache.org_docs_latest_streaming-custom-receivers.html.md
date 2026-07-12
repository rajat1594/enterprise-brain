[ ![](https://spark.apache.org/images/spark-logo-rev.svg)](https://spark.apache.org/docs/latest/index.html)4.1.2
  * [Overview](https://spark.apache.org/docs/latest/index.html)
  * [Programming Guides](https://spark.apache.org/docs/latest/streaming-custom-receivers.html)
[Quick Start](https://spark.apache.org/docs/latest/quick-start.html) [RDDs, Accumulators, Broadcasts Vars](https://spark.apache.org/docs/latest/rdd-programming-guide.html) [SQL, DataFrames, and Datasets](https://spark.apache.org/docs/latest/sql-programming-guide.html) [Structured Streaming](https://spark.apache.org/docs/latest/streaming/index.html) [Spark Streaming (DStreams)](https://spark.apache.org/docs/latest/streaming-programming-guide.html) [MLlib (Machine Learning)](https://spark.apache.org/docs/latest/ml-guide.html) [GraphX (Graph Processing)](https://spark.apache.org/docs/latest/graphx-programming-guide.html) [SparkR (R on Spark)](https://spark.apache.org/docs/latest/sparkr.html) [PySpark (Python on Spark)](https://spark.apache.org/docs/latest/api/python/getting_started/index.html) [Declarative Pipelines](https://spark.apache.org/docs/latest/declarative-pipelines-programming-guide.html)
  * [API Docs](https://spark.apache.org/docs/latest/streaming-custom-receivers.html)
[Python](https://spark.apache.org/docs/latest/api/python/index.html) [Scala](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html) [Java](https://spark.apache.org/docs/latest/api/java/index.html) [R](https://spark.apache.org/docs/latest/api/R/index.html) [SQL, Built-in Functions](https://spark.apache.org/docs/latest/api/sql/index.html)
  * [Deploying](https://spark.apache.org/docs/latest/streaming-custom-receivers.html)
[Overview](https://spark.apache.org/docs/latest/cluster-overview.html) [Submitting Applications](https://spark.apache.org/docs/latest/submitting-applications.html) [Spark Standalone](https://spark.apache.org/docs/latest/spark-standalone.html) [YARN](https://spark.apache.org/docs/latest/running-on-yarn.html) [Kubernetes](https://spark.apache.org/docs/latest/running-on-kubernetes.html)
  * [More](https://spark.apache.org/docs/latest/streaming-custom-receivers.html)
[Configuration](https://spark.apache.org/docs/latest/configuration.html) [Monitoring](https://spark.apache.org/docs/latest/monitoring.html) [Tuning Guide](https://spark.apache.org/docs/latest/tuning.html) [Job Scheduling](https://spark.apache.org/docs/latest/job-scheduling.html) [Security](https://spark.apache.org/docs/latest/security.html) [Hardware Provisioning](https://spark.apache.org/docs/latest/hardware-provisioning.html) [Migration Guide](https://spark.apache.org/docs/latest/migration-guide.html) [Building Spark](https://spark.apache.org/docs/latest/building-spark.html) [Contributing to Spark](https://spark.apache.org/contributing.html) [Third Party Projects](https://spark.apache.org/third-party-projects.html)
  * 

# Spark Streaming Custom Receivers[](https://spark.apache.org/docs/latest/streaming-custom-receivers.html#spark-streaming-custom-receivers)
Spark Streaming can receive streaming data from any arbitrary data source beyond the ones for which it has built-in support (that is, beyond Kafka, Kinesis, files, sockets, etc.). This requires the developer to implement a _receiver_ that is customized for receiving data from the concerned data source. This guide walks through the process of implementing a custom receiver and using it in a Spark Streaming application. Note that custom receivers can be implemented in Scala or Java.
## Implementing a Custom Receiver[](https://spark.apache.org/docs/latest/streaming-custom-receivers.html#implementing-a-custom-receiver)
This starts with implementing a **Receiver** ([Scala doc](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/receiver/Receiver.html), [Java doc](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/receiver/Receiver.html)). A custom receiver must extend this abstract class by implementing two methods
  * `onStart()`: Things to do to start receiving data.
  * `onStop()`: Things to do to stop receiving data.


Both `onStart()` and `onStop()` must not block indefinitely. Typically, `onStart()` would start the threads that are responsible for receiving the data, and `onStop()` would ensure that these threads receiving the data are stopped. The receiving threads can also use `isStopped()`, a `Receiver` method, to check whether they should stop receiving data.
Once the data is received, that data can be stored inside Spark by calling `store(data)`, which is a method provided by the Receiver class. There are a number of flavors of `store()` which allow one to store the received data record-at-a-time or as whole collection of objects / serialized bytes. Note that the flavor of `store()` used to implement a receiver affects its reliability and fault-tolerance semantics. This is discussed [later](https://spark.apache.org/docs/latest/streaming-custom-receivers.html#receiver-reliability) in more detail.
Any exception in the receiving threads should be caught and handled properly to avoid silent failures of the receiver. `restart(<exception>)` will restart the receiver by asynchronously calling `onStop()` and then calling `onStart()` after a delay. `stop(<exception>)` will call `onStop()` and terminate the receiver. Also, `reportError(<error>)` reports an error message to the driver (visible in the logs and UI) without stopping / restarting the receiver.
The following is a custom receiver that receives a stream of text over a socket. It treats ‘\n’ delimited lines in the text stream as records and stores them with Spark. If the receiving thread has any error connecting or receiving, the receiver is restarted to make another attempt to connect.
  * **Scala**
  * **Java**



```
class CustomReceiver(host: String, port: Int)
  extends Receiver[String](StorageLevel.MEMORY_AND_DISK_2) with Logging {

  def onStart() {
    // Start the thread that receives data over a connection
    new Thread("Socket Receiver") {
      override def run() { receive() }
    }.start()
  }

  def onStop() {
    // There is nothing much to do as the thread calling receive()
    // is designed to stop by itself if isStopped() returns false
  }

  /** Create a socket connection and receive data until receiver is stopped */
  private def receive() {
    var socket: Socket = null
    var userInput: String = null
    try {
      // Connect to host:port
      socket = new Socket(host, port)

      // Until stopped or connection broken continue reading
      val reader = new BufferedReader(
        new InputStreamReader(socket.getInputStream(), StandardCharsets.UTF_8))
      userInput = reader.readLine()
      while(!isStopped && userInput != null) {
        store(userInput)
        userInput = reader.readLine()
      }
      reader.close()
      socket.close()

      // Restart in an attempt to connect again when server is active again
      restart("Trying to connect again")
    } catch {
      case e: java.net.ConnectException =>
        // restart if could not connect to server
        restart("Error connecting to " + host + ":" + port, e)
      case t: Throwable =>
        // restart if there is any other error
        restart("Error receiving data", t)
    }
  }
}
```


```
public class JavaCustomReceiver extends Receiver<String> {

  String host = null;
  int port = -1;

  public JavaCustomReceiver(String host_ , int port_) {
    super(StorageLevel.MEMORY_AND_DISK_2());
    host = host_;
    port = port_;
  }

  @Override
  public void onStart() {
    // Start the thread that receives data over a connection
    new Thread(this::receive).start();
  }

  @Override
  public void onStop() {
    // There is nothing much to do as the thread calling receive()
    // is designed to stop by itself if isStopped() returns false
  }

  /** Create a socket connection and receive data until receiver is stopped */
  private void receive() {
    Socket socket = null;
    String userInput = null;

    try {
      // connect to the server
      socket = new Socket(host, port);

      BufferedReader reader = new BufferedReader(
        new InputStreamReader(socket.getInputStream(), StandardCharsets.UTF_8));

      // Until stopped or connection broken continue reading
      while (!isStopped() && (userInput = reader.readLine()) != null) {
        System.out.println("Received data '" + userInput + "'");
        store(userInput);
      }
      reader.close();
      socket.close();

      // Restart in an attempt to connect again when server is active again
      restart("Trying to connect again");
    } catch(ConnectException ce) {
      // restart if could not connect to server
      restart("Could not connect", ce);
    } catch(Throwable t) {
      // restart if there is any other error
      restart("Error receiving data", t);
    }
  }
}
```

## Using the custom receiver in a Spark Streaming application[](https://spark.apache.org/docs/latest/streaming-custom-receivers.html#using-the-custom-receiver-in-a-spark-streaming-application)
The custom receiver can be used in a Spark Streaming application by using `streamingContext.receiverStream(<instance of custom receiver>)`. This will create an input DStream using data received by the instance of custom receiver, as shown below:
  * **Scala**
  * **Java**



```
// Assuming ssc is the StreamingContext
val customReceiverStream = ssc.receiverStream(new CustomReceiver(host, port))
val words = customReceiverStream.flatMap(_.split(" "))
...
```

The full source code is in the example [CustomReceiver.scala](https://github.com/apache/spark/blob/v4.1.2/examples/src/main/scala/org/apache/spark/examples/streaming/CustomReceiver.scala).

```
// Assuming ssc is the JavaStreamingContext
JavaDStream<String> customReceiverStream = ssc.receiverStream(new JavaCustomReceiver(host, port));
JavaDStream<String> words = customReceiverStream.flatMap(s -> ...);
...
```

The full source code is in the example [JavaCustomReceiver.java](https://github.com/apache/spark/blob/v4.1.2/examples/src/main/java/org/apache/spark/examples/streaming/JavaCustomReceiver.java).
## Receiver Reliability[](https://spark.apache.org/docs/latest/streaming-custom-receivers.html#receiver-reliability)
As discussed in brief in the [Spark Streaming Programming Guide](https://spark.apache.org/docs/latest/streaming-programming-guide.html#receiver-reliability), there are two kinds of receivers based on their reliability and fault-tolerance semantics.
  1. _Reliable Receiver_ - For _reliable sources_ that allow sent data to be acknowledged, a _reliable receiver_ correctly acknowledges to the source that the data has been received and stored in Spark reliably (that is, replicated successfully). Usually, implementing this receiver involves careful consideration of the semantics of source acknowledgements.
  2. _Unreliable Receiver_ - An _unreliable receiver_ does _not_ send acknowledgement to a source. This can be used for sources that do not support acknowledgement, or even for reliable sources when one does not want or need to go into the complexity of acknowledgement.


To implement a _reliable receiver_ , you have to use `store(multiple-records)` to store data. This flavor of `store` is a blocking call which returns only after all the given records have been stored inside Spark. If the receiver’s configured storage level uses replication (enabled by default), then this call returns after replication has completed. Thus it ensures that the data is reliably stored, and the receiver can now acknowledge the source appropriately. This ensures that no data is lost when the receiver fails in the middle of replicating data – the buffered data will not be acknowledged and hence will be later resent by the source.
An _unreliable receiver_ does not have to implement any of this logic. It can simply receive records from the source and insert them one-at-a-time using `store(single-record)`. While it does not get the reliability guarantees of `store(multiple-records)`, it has the following advantages:
  * The system takes care of chunking that data into appropriate sized blocks (look for block interval in the [Spark Streaming Programming Guide](https://spark.apache.org/docs/latest/streaming-programming-guide.html)).
  * The system takes care of controlling the receiving rates if the rate limits have been specified.
  * Because of these two, unreliable receivers are simpler to implement than reliable receivers.


The following table summarizes the characteristics of both types of receivers  
| Receiver Type  | Characteristics  |  
| --- | --- |  
| **Unreliable Receivers**  |  Simple to implement.  
System takes care of block generation and rate control. No fault-tolerance guarantees, can lose data on receiver failure.   |  
| **Reliable Receivers**  |  Strong fault-tolerance guarantees, can ensure zero data loss.  
Block generation and rate control to be handled by the receiver implementation.  
Implementation complexity depends on the acknowledgement mechanisms of the source.   |  
|   |   |
