[Skip navigation links](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/package-summary.html#skip-navbar-top "Skip navigation links")
  * [Overview](https://spark.apache.org/docs/latest/api/java/index.html)
  * Package
  * Class
  * [Deprecated](https://spark.apache.org/docs/latest/api/java/deprecated-list.html)
  * [Index](https://spark.apache.org/docs/latest/api/java/index-all.html)
  * [Help](https://spark.apache.org/docs/latest/api/java/help-doc.html#package)

  * Package:
  * Description |
  * [Related Packages](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/package-summary.html#related-package-summary) |
  * [Classes and Interfaces](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/package-summary.html#class-summary)

SEARCH:
# Package org.apache.spark.streaming
* * *
package org.apache.spark.streaming
  * Related Packages
Package
Description
[org.apache.spark](https://spark.apache.org/docs/latest/api/java/org/apache/spark/package-summary.html)
Core Spark classes in Scala.
[org.apache.spark.streaming.dstream](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/dstream/package-summary.html)
Various implementations of DStreams.
[org.apache.spark.streaming.kinesis](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/kinesis/package-summary.html)
[org.apache.spark.streaming.receiver](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/receiver/package-summary.html)
[org.apache.spark.streaming.scheduler](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/scheduler/package-summary.html)
[org.apache.spark.streaming.ui](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/ui/package-summary.html)
[org.apache.spark.streaming.util](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/util/package-summary.html)
  * All Classes and InterfacesClassesEnum Classes
Class
Description
[CheckpointReader](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/CheckpointReader.html "class in org.apache.spark.streaming")
[Duration](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/Duration.html "class in org.apache.spark.streaming")
[Durations](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/Durations.html "class in org.apache.spark.streaming")
[Milliseconds](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/Milliseconds.html "class in org.apache.spark.streaming")
Helper object that creates instance of [`Duration`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/Duration.html "class in org.apache.spark.streaming") representing a given number of milliseconds.
[Minutes](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/Minutes.html "class in org.apache.spark.streaming")
Helper object that creates instance of [`Duration`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/Duration.html "class in org.apache.spark.streaming") representing a given number of minutes.
[Seconds](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/Seconds.html "class in org.apache.spark.streaming")
Helper object that creates instance of [`Duration`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/Duration.html "class in org.apache.spark.streaming") representing a given number of seconds.
[State](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/State.html "class in org.apache.spark.streaming")<S>
Experimental Abstract class for getting and updating the state in mapping function used in the `mapWithState` operation of a [`pair DStream`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/dstream/PairDStreamFunctions.html "class in org.apache.spark.streaming.dstream") (Scala) or a [`JavaPairDStream`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/api/java/JavaPairDStream.html "class in org.apache.spark.streaming.api.java") (Java).
[StateSpec](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/StateSpec.html "class in org.apache.spark.streaming")<KeyType,ValueType,StateType,MappedType>
Experimental Abstract class representing all the specifications of the DStream transformation `mapWithState` operation of a [`pair DStream`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/dstream/PairDStreamFunctions.html "class in org.apache.spark.streaming.dstream") (Scala) or a [`JavaPairDStream`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/api/java/JavaPairDStream.html "class in org.apache.spark.streaming.api.java") (Java).
[StreamingConf](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/StreamingConf.html "class in org.apache.spark.streaming")
[StreamingContext](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/StreamingContext.html "class in org.apache.spark.streaming")
Deprecated.
This is deprecated as of Spark 3.4.0.
[StreamingContextPythonHelper](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/StreamingContextPythonHelper.html "class in org.apache.spark.streaming")
[StreamingContextState](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/StreamingContextState.html "enum class in org.apache.spark.streaming")
Developer API Represents the state of a StreamingContext.
[Time](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/Time.html "class in org.apache.spark.streaming")
This is a simple class that represents an absolute instant of time.
