[Skip navigation links](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/kinesis/package-summary.html#skip-navbar-top "Skip navigation links")
  * [Overview](https://spark.apache.org/docs/latest/api/java/index.html)
  * Package
  * Class
  * [Deprecated](https://spark.apache.org/docs/latest/api/java/deprecated-list.html)
  * [Index](https://spark.apache.org/docs/latest/api/java/index-all.html)
  * [Help](https://spark.apache.org/docs/latest/api/java/help-doc.html#package)

  * Package:
  * Description |
  * [Related Packages](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/kinesis/package-summary.html#related-package-summary) |
  * [Classes and Interfaces](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/kinesis/package-summary.html#class-summary)

SEARCH:
# Package org.apache.spark.streaming.kinesis
* * *
package org.apache.spark.streaming.kinesis
  * Related Packages
Package
Description
[org.apache.spark.streaming](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/package-summary.html)
[org.apache.spark.streaming.dstream](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/dstream/package-summary.html)
Various implementations of DStreams.
[org.apache.spark.streaming.receiver](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/receiver/package-summary.html)
[org.apache.spark.streaming.scheduler](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/scheduler/package-summary.html)
[org.apache.spark.streaming.ui](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/ui/package-summary.html)
[org.apache.spark.streaming.util](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/util/package-summary.html)
  * All Classes and InterfacesInterfacesClasses
Class
Description
[DefaultCredentials](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/kinesis/DefaultCredentials.html "class in org.apache.spark.streaming.kinesis")
Returns DefaultAWSCredentialsProviderChain for authentication.
[KinesisInitialPositions](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/kinesis/KinesisInitialPositions.html "class in org.apache.spark.streaming.kinesis")
[KinesisInitialPositions.AtTimestamp](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/kinesis/KinesisInitialPositions.AtTimestamp.html "class in org.apache.spark.streaming.kinesis")
[KinesisInitialPositions.Latest](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/kinesis/KinesisInitialPositions.Latest.html "class in org.apache.spark.streaming.kinesis")
[KinesisInitialPositions.TrimHorizon](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/kinesis/KinesisInitialPositions.TrimHorizon.html "class in org.apache.spark.streaming.kinesis")
[KinesisUtilsPythonHelper](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/kinesis/KinesisUtilsPythonHelper.html "class in org.apache.spark.streaming.kinesis")
This is a helper class that wraps the methods in KinesisUtils into more Python-friendly class and function so that it can be easily instantiated and called from Python's KinesisUtils.
[SparkAWSCredentials](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/kinesis/SparkAWSCredentials.html "interface in org.apache.spark.streaming.kinesis")
Serializable interface providing a method executors can call to obtain an AWSCredentialsProvider instance for authenticating to AWS services.
[SparkAWSCredentials.Builder](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/kinesis/SparkAWSCredentials.Builder.html "class in org.apache.spark.streaming.kinesis")
Builder for [`SparkAWSCredentials`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/kinesis/SparkAWSCredentials.html "interface in org.apache.spark.streaming.kinesis") instances.
