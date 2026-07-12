[Skip navigation links](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/util/package-summary.html#skip-navbar-top "Skip navigation links")
  * [Overview](https://spark.apache.org/docs/latest/api/java/index.html)
  * Package
  * Class
  * [Deprecated](https://spark.apache.org/docs/latest/api/java/deprecated-list.html)
  * [Index](https://spark.apache.org/docs/latest/api/java/index-all.html)
  * [Help](https://spark.apache.org/docs/latest/api/java/help-doc.html#package)

  * Package:
  * Description |
  * [Related Packages](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/util/package-summary.html#related-package-summary) |
  * [Classes and Interfaces](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/util/package-summary.html#class-summary)

SEARCH:
# Package org.apache.spark.streaming.util
* * *
package org.apache.spark.streaming.util
  * Related Packages
Package
Description
[org.apache.spark.streaming](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/package-summary.html)
[org.apache.spark.streaming.dstream](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/dstream/package-summary.html)
Various implementations of DStreams.
[org.apache.spark.streaming.kinesis](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/kinesis/package-summary.html)
[org.apache.spark.streaming.receiver](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/receiver/package-summary.html)
[org.apache.spark.streaming.scheduler](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/scheduler/package-summary.html)
[org.apache.spark.streaming.ui](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/ui/package-summary.html)
  * Classes
Class
Description
[HdfsUtils](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/util/HdfsUtils.html "class in org.apache.spark.streaming.util")
[RawTextHelper](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/util/RawTextHelper.html "class in org.apache.spark.streaming.util")
[RawTextSender](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/util/RawTextSender.html "class in org.apache.spark.streaming.util")
A helper program that sends blocks of Kryo-serialized text strings out on a socket at a specified rate.
[WriteAheadLog](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/util/WriteAheadLog.html "class in org.apache.spark.streaming.util")
Developer API This abstract class represents a write ahead log (aka journal) that is used by Spark Streaming to save the received data (by receivers) and associated metadata to a reliable storage, so that they can be recovered after driver failures.
[WriteAheadLogRecordHandle](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/util/WriteAheadLogRecordHandle.html "class in org.apache.spark.streaming.util")
Developer API This abstract class represents a handle that refers to a record written in a [`WriteAheadLog`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/util/WriteAheadLog.html "class in org.apache.spark.streaming.util").
[WriteAheadLogUtils](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/util/WriteAheadLogUtils.html "class in org.apache.spark.streaming.util")
A helper class with utility functions related to the WriteAheadLog interface
