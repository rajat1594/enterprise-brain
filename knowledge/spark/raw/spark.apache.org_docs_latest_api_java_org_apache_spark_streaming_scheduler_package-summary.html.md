[Skip navigation links](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/scheduler/package-summary.html#skip-navbar-top "Skip navigation links")
  * [Overview](https://spark.apache.org/docs/latest/api/java/index.html)
  * Package
  * Class
  * [Deprecated](https://spark.apache.org/docs/latest/api/java/deprecated-list.html)
  * [Index](https://spark.apache.org/docs/latest/api/java/index-all.html)
  * [Help](https://spark.apache.org/docs/latest/api/java/help-doc.html#package)


  * Package: 
  * Description | 
  * [Related Packages](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/scheduler/package-summary.html#related-package-summary) | 
  * [Classes and Interfaces](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/scheduler/package-summary.html#class-summary)


SEARCH:
# Package org.apache.spark.streaming.scheduler
* * *
package org.apache.spark.streaming.scheduler
  * Related Packages
Package
Description
[org.apache.spark.streaming](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/package-summary.html)
[org.apache.spark.streaming.scheduler.rate](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/scheduler/rate/package-summary.html)
[org.apache.spark.streaming.dstream](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/dstream/package-summary.html)
Various implementations of DStreams.
[org.apache.spark.streaming.kinesis](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/kinesis/package-summary.html)
[org.apache.spark.streaming.receiver](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/receiver/package-summary.html)
[org.apache.spark.streaming.ui](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/ui/package-summary.html)
[org.apache.spark.streaming.util](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/util/package-summary.html)
  * All Classes and InterfacesInterfacesClasses
Class
Description
[AllReceiverIds](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/scheduler/AllReceiverIds.html "class in org.apache.spark.streaming.scheduler")
A message used by ReceiverTracker to ask all receiver's ids still stored in ReceiverTrackerEndpoint.
[BatchInfo](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/scheduler/BatchInfo.html "class in org.apache.spark.streaming.scheduler")
Developer API Class having information on completed batches.
[GetAllReceiverInfo](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/scheduler/GetAllReceiverInfo.html "class in org.apache.spark.streaming.scheduler")
[JobGeneratorEvent](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/scheduler/JobGeneratorEvent.html "interface in org.apache.spark.streaming.scheduler")
Event classes for JobGenerator
[JobSchedulerEvent](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/scheduler/JobSchedulerEvent.html "interface in org.apache.spark.streaming.scheduler")
[OutputOperationInfo](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/scheduler/OutputOperationInfo.html "class in org.apache.spark.streaming.scheduler")
Developer API Class having information on output operations.
[ReceivedBlockTrackerLogEvent](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/scheduler/ReceivedBlockTrackerLogEvent.html "interface in org.apache.spark.streaming.scheduler")
Trait representing any event in the ReceivedBlockTracker that updates its state.
[ReceiverInfo](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/scheduler/ReceiverInfo.html "class in org.apache.spark.streaming.scheduler")
Developer API Class having information about a receiver
[ReceiverState](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/scheduler/ReceiverState.html "class in org.apache.spark.streaming.scheduler")
Enumeration to identify current state of a Receiver
[ReceiverTrackerLocalMessage](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/scheduler/ReceiverTrackerLocalMessage.html "interface in org.apache.spark.streaming.scheduler")
Messages used by the driver and ReceiverTrackerEndpoint to communicate locally.
[ReceiverTrackerMessage](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/scheduler/ReceiverTrackerMessage.html "interface in org.apache.spark.streaming.scheduler")
Messages used by the NetworkReceiver and the ReceiverTracker to communicate with each other.
[StatsReportListener](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/scheduler/StatsReportListener.html "class in org.apache.spark.streaming.scheduler")
Developer API A simple StreamingListener that logs summary statistics across Spark Streaming batches param: numBatchInfos Number of last batches to consider for generating statistics (default: 10)
[StopAllReceivers](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/scheduler/StopAllReceivers.html "class in org.apache.spark.streaming.scheduler")
This message will trigger ReceiverTrackerEndpoint to send stop signals to all registered receivers.
[StreamingListener](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/scheduler/StreamingListener.html "interface in org.apache.spark.streaming.scheduler")
Developer API A listener interface for receiving information about an ongoing streaming computation.
[StreamingListenerBatchCompleted](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/scheduler/StreamingListenerBatchCompleted.html "class in org.apache.spark.streaming.scheduler")
[StreamingListenerBatchStarted](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/scheduler/StreamingListenerBatchStarted.html "class in org.apache.spark.streaming.scheduler")
[StreamingListenerBatchSubmitted](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/scheduler/StreamingListenerBatchSubmitted.html "class in org.apache.spark.streaming.scheduler")
[StreamingListenerEvent](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/scheduler/StreamingListenerEvent.html "interface in org.apache.spark.streaming.scheduler")
Developer API Base trait for events related to StreamingListener
[StreamingListenerOutputOperationCompleted](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/scheduler/StreamingListenerOutputOperationCompleted.html "class in org.apache.spark.streaming.scheduler")
[StreamingListenerOutputOperationStarted](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/scheduler/StreamingListenerOutputOperationStarted.html "class in org.apache.spark.streaming.scheduler")
[StreamingListenerReceiverError](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/scheduler/StreamingListenerReceiverError.html "class in org.apache.spark.streaming.scheduler")
[StreamingListenerReceiverStarted](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/scheduler/StreamingListenerReceiverStarted.html "class in org.apache.spark.streaming.scheduler")
[StreamingListenerReceiverStopped](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/scheduler/StreamingListenerReceiverStopped.html "class in org.apache.spark.streaming.scheduler")
[StreamingListenerStreamingStarted](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/scheduler/StreamingListenerStreamingStarted.html "class in org.apache.spark.streaming.scheduler")
[StreamInputInfo](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/scheduler/StreamInputInfo.html "class in org.apache.spark.streaming.scheduler")
Developer API Track the information of input stream at specified batch time.


