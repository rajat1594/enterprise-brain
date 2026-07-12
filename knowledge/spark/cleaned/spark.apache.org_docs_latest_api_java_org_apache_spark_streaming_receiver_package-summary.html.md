[Skip navigation links](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/receiver/package-summary.html#skip-navbar-top "Skip navigation links")
  * [Overview](https://spark.apache.org/docs/latest/api/java/index.html)
  * Package
  * Class
  * [Deprecated](https://spark.apache.org/docs/latest/api/java/deprecated-list.html)
  * [Index](https://spark.apache.org/docs/latest/api/java/index-all.html)
  * [Help](https://spark.apache.org/docs/latest/api/java/help-doc.html#package)

  * Package:
  * Description |
  * [Related Packages](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/receiver/package-summary.html#related-package-summary) |
  * [Classes and Interfaces](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/receiver/package-summary.html#class-summary)

SEARCH:
# Package org.apache.spark.streaming.receiver
* * *
package org.apache.spark.streaming.receiver
  * Related Packages
Package
Description
[org.apache.spark.streaming](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/package-summary.html)
[org.apache.spark.streaming.dstream](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/dstream/package-summary.html)
Various implementations of DStreams.
[org.apache.spark.streaming.kinesis](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/kinesis/package-summary.html)
[org.apache.spark.streaming.scheduler](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/scheduler/package-summary.html)
[org.apache.spark.streaming.ui](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/ui/package-summary.html)
[org.apache.spark.streaming.util](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/util/package-summary.html)
  * All Classes and InterfacesInterfacesClasses
Class
Description
[BlockGeneratorListener](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/receiver/BlockGeneratorListener.html "interface in org.apache.spark.streaming.receiver")
Listener object for BlockGenerator events
[ReceivedBlock](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/receiver/ReceivedBlock.html "interface in org.apache.spark.streaming.receiver")
Trait representing a received block
[ReceivedBlockHandler](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/receiver/ReceivedBlockHandler.html "interface in org.apache.spark.streaming.receiver")
Trait that represents a class that handles the storage of blocks received by receiver
[ReceivedBlockStoreResult](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/receiver/ReceivedBlockStoreResult.html "interface in org.apache.spark.streaming.receiver")
Trait that represents the metadata related to storage of blocks
[Receiver](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/receiver/Receiver.html "class in org.apache.spark.streaming.receiver")<T>
Developer API Abstract class of a receiver that can be run on worker nodes to receive external data.
[ReceiverMessage](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/receiver/ReceiverMessage.html "interface in org.apache.spark.streaming.receiver")
Messages sent to the Receiver.
[StopReceiver](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/receiver/StopReceiver.html "class in org.apache.spark.streaming.receiver")
