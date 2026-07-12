[Skip navigation links](https://spark.apache.org/docs/latest/api/java/org/apache/spark/shuffle/api/package-summary.html#skip-navbar-top "Skip navigation links")
  * [Overview](https://spark.apache.org/docs/latest/api/java/index.html)
  * Package
  * Class
  * [Deprecated](https://spark.apache.org/docs/latest/api/java/deprecated-list.html)
  * [Index](https://spark.apache.org/docs/latest/api/java/index-all.html)
  * [Help](https://spark.apache.org/docs/latest/api/java/help-doc.html#package)

  * Package:
  * Description |
  * [Related Packages](https://spark.apache.org/docs/latest/api/java/org/apache/spark/shuffle/api/package-summary.html#related-package-summary) |
  * [Classes and Interfaces](https://spark.apache.org/docs/latest/api/java/org/apache/spark/shuffle/api/package-summary.html#class-summary)

SEARCH:
# Package org.apache.spark.shuffle.api
* * *
package org.apache.spark.shuffle.api
  * Related Packages
Package
Description
[org.apache.spark.shuffle.api.metadata](https://spark.apache.org/docs/latest/api/java/org/apache/spark/shuffle/api/metadata/package-summary.html)
  * Interfaces
Class
Description
[ShuffleDataIO](https://spark.apache.org/docs/latest/api/java/org/apache/spark/shuffle/api/ShuffleDataIO.html "interface in org.apache.spark.shuffle.api")
:: Private :: An interface for plugging in modules for storing and reading temporary shuffle data.
[ShuffleDriverComponents](https://spark.apache.org/docs/latest/api/java/org/apache/spark/shuffle/api/ShuffleDriverComponents.html "interface in org.apache.spark.shuffle.api")
:: Private :: An interface for building shuffle support modules for the Driver.
[ShuffleExecutorComponents](https://spark.apache.org/docs/latest/api/java/org/apache/spark/shuffle/api/ShuffleExecutorComponents.html "interface in org.apache.spark.shuffle.api")
:: Private :: An interface for building shuffle support for Executors.
[ShuffleMapOutputWriter](https://spark.apache.org/docs/latest/api/java/org/apache/spark/shuffle/api/ShuffleMapOutputWriter.html "interface in org.apache.spark.shuffle.api")
:: Private :: A top-level writer that returns child writers for persisting the output of a map task, and then commits all of the writes as one atomic operation.
[ShufflePartitionWriter](https://spark.apache.org/docs/latest/api/java/org/apache/spark/shuffle/api/ShufflePartitionWriter.html "interface in org.apache.spark.shuffle.api")
:: Private :: An interface for opening streams to persist partition bytes to a backing data store.
[SingleSpillShuffleMapOutputWriter](https://spark.apache.org/docs/latest/api/java/org/apache/spark/shuffle/api/SingleSpillShuffleMapOutputWriter.html "interface in org.apache.spark.shuffle.api")
Optional extension for partition writing that is optimized for transferring a single file to the backing store.
[WritableByteChannelWrapper](https://spark.apache.org/docs/latest/api/java/org/apache/spark/shuffle/api/WritableByteChannelWrapper.html "interface in org.apache.spark.shuffle.api")
:: Private :: A thin wrapper around a [`WritableByteChannel`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/nio/channels/WritableByteChannel.html "class or interface in java.nio.channels").
