[Skip navigation links](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/streaming/package-summary.html#skip-navbar-top "Skip navigation links")
  * [Overview](https://spark.apache.org/docs/latest/api/java/index.html)
  * Package
  * Class
  * [Deprecated](https://spark.apache.org/docs/latest/api/java/deprecated-list.html)
  * [Index](https://spark.apache.org/docs/latest/api/java/index-all.html)
  * [Help](https://spark.apache.org/docs/latest/api/java/help-doc.html#package)


  * Package: 
  * Description | 
  * [Related Packages](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/streaming/package-summary.html#related-package-summary) | 
  * [Classes and Interfaces](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/streaming/package-summary.html#class-summary)


SEARCH:
# Package org.apache.spark.sql.streaming
* * *
package org.apache.spark.sql.streaming
  * Related Packages
Package
Description
[org.apache.spark.sql](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/package-summary.html)
[org.apache.spark.sql.streaming.ui](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/streaming/ui/package-summary.html)
  * All Classes and InterfacesInterfacesClassesExceptions
Class
Description
[DataStreamReader](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/streaming/DataStreamReader.html "class in org.apache.spark.sql.streaming")
Interface used to load a streaming `Dataset` from external storage systems (e.g.
[DataStreamWriter](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/streaming/DataStreamWriter.html "class in org.apache.spark.sql.streaming")<T>
Interface used to write a streaming `Dataset` to external storage systems (e.g.
[ExpiredTimerInfo](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/streaming/ExpiredTimerInfo.html "interface in org.apache.spark.sql.streaming")
Class used to provide access to expired timer's expiry time.
[GroupState](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/streaming/GroupState.html "interface in org.apache.spark.sql.streaming")<S>
Experimental
[GroupStateTimeout](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/streaming/GroupStateTimeout.html "class in org.apache.spark.sql.streaming")
Represents the type of timeouts possible for the Dataset operations `mapGroupsWithState` and `flatMapGroupsWithState`.
[ListState](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/streaming/ListState.html "interface in org.apache.spark.sql.streaming")<S>
Interface used for arbitrary stateful operations with the v2 API to capture list value state.
[MapState](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/streaming/MapState.html "interface in org.apache.spark.sql.streaming")<K,V>
Interface used for arbitrary stateful operations with the v2 API to capture map value state.
[OutputMode](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/streaming/OutputMode.html "class in org.apache.spark.sql.streaming")
OutputMode describes what data will be written to a streaming sink when there is new data available in a streaming DataFrame/Dataset.
[PythonStreamingQueryListener](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/streaming/PythonStreamingQueryListener.html "interface in org.apache.spark.sql.streaming")
Py4J allows a pure interface so this proxy is required.
[QueryInfo](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/streaming/QueryInfo.html "interface in org.apache.spark.sql.streaming")
Represents the query info provided to the stateful processor used in the arbitrary state API v2 to easily identify task retries on the same partition.
[SafeJsonSerializer](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/streaming/SafeJsonSerializer.html "class in org.apache.spark.sql.streaming")
[SinkProgress](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/streaming/SinkProgress.html "class in org.apache.spark.sql.streaming")
Information about progress made for a sink in the execution of a [`StreamingQuery`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/streaming/StreamingQuery.html "interface in org.apache.spark.sql.streaming") during a trigger.
[SourceProgress](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/streaming/SourceProgress.html "class in org.apache.spark.sql.streaming")
Information about progress made for a source in the execution of a [`StreamingQuery`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/streaming/StreamingQuery.html "interface in org.apache.spark.sql.streaming") during a trigger.
[StatefulProcessor](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/streaming/StatefulProcessor.html "class in org.apache.spark.sql.streaming")<K,I,O>
Represents the arbitrary stateful logic that needs to be provided by the user to perform stateful manipulations on keyed streams.
[StatefulProcessorHandle](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/streaming/StatefulProcessorHandle.html "interface in org.apache.spark.sql.streaming")
Represents the operation handle provided to the stateful processor used in the arbitrary state API v2.
[StatefulProcessorWithInitialState](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/streaming/StatefulProcessorWithInitialState.html "class in org.apache.spark.sql.streaming")<K,I,O,S>
Stateful processor with support for specifying initial state.
[StateOperatorProgress](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/streaming/StateOperatorProgress.html "class in org.apache.spark.sql.streaming")
Information about updates made to stateful operators in a [`StreamingQuery`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/streaming/StreamingQuery.html "interface in org.apache.spark.sql.streaming") during a trigger.
[StreamingQuery](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/streaming/StreamingQuery.html "interface in org.apache.spark.sql.streaming")
A handle to a query that is executing continuously in the background as new data arrives.
[StreamingQueryException](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/streaming/StreamingQueryException.html "class in org.apache.spark.sql.streaming")
Exception that stopped a [`StreamingQuery`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/streaming/StreamingQuery.html "interface in org.apache.spark.sql.streaming").
[StreamingQueryListener](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/streaming/StreamingQueryListener.html "class in org.apache.spark.sql.streaming")
Interface for listening to events related to [`StreamingQueries`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/streaming/StreamingQuery.html "interface in org.apache.spark.sql.streaming").
[StreamingQueryListener.Event](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/streaming/StreamingQueryListener.Event.html "interface in org.apache.spark.sql.streaming")
Base type of [`StreamingQueryListener`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/streaming/StreamingQueryListener.html "class in org.apache.spark.sql.streaming") events
[StreamingQueryListener.QueryIdleEvent](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/streaming/StreamingQueryListener.QueryIdleEvent.html "class in org.apache.spark.sql.streaming")
Event representing that query is idle and waiting for new data to process.
[StreamingQueryListener.QueryIdleEvent$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/streaming/StreamingQueryListener.QueryIdleEvent$.html "class in org.apache.spark.sql.streaming")
[StreamingQueryListener.QueryProgressEvent](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/streaming/StreamingQueryListener.QueryProgressEvent.html "class in org.apache.spark.sql.streaming")
Event representing any progress updates in a query.
[StreamingQueryListener.QueryProgressEvent$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/streaming/StreamingQueryListener.QueryProgressEvent$.html "class in org.apache.spark.sql.streaming")
[StreamingQueryListener.QueryStartedEvent](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/streaming/StreamingQueryListener.QueryStartedEvent.html "class in org.apache.spark.sql.streaming")
Event representing the start of a query param: id A unique query id that persists across restarts.
[StreamingQueryListener.QueryStartedEvent$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/streaming/StreamingQueryListener.QueryStartedEvent$.html "class in org.apache.spark.sql.streaming")
[StreamingQueryListener.QueryTerminatedEvent](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/streaming/StreamingQueryListener.QueryTerminatedEvent.html "class in org.apache.spark.sql.streaming")
Event representing that termination of a query.
[StreamingQueryListener.QueryTerminatedEvent$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/streaming/StreamingQueryListener.QueryTerminatedEvent$.html "class in org.apache.spark.sql.streaming")
[StreamingQueryManager](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/streaming/StreamingQueryManager.html "class in org.apache.spark.sql.streaming")
A class to manage all the [`StreamingQuery`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/streaming/StreamingQuery.html "interface in org.apache.spark.sql.streaming") active in a `SparkSession`.
[StreamingQueryProgress](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/streaming/StreamingQueryProgress.html "class in org.apache.spark.sql.streaming")
Information about progress made in the execution of a [`StreamingQuery`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/streaming/StreamingQuery.html "interface in org.apache.spark.sql.streaming") during a trigger.
[StreamingQueryStatus](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/streaming/StreamingQueryStatus.html "class in org.apache.spark.sql.streaming")
Reports information about the instantaneous status of a streaming query.
[TestGroupState](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/streaming/TestGroupState.html "interface in org.apache.spark.sql.streaming")<S>
Experimental
[TimeMode](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/streaming/TimeMode.html "class in org.apache.spark.sql.streaming")
Represents the time modes (used for specifying timers and ttl) possible for the Dataset operations `transformWithState`.
[TimerValues](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/streaming/TimerValues.html "interface in org.apache.spark.sql.streaming")
Class used to provide access to timer values for processing and event time populated before method invocations using the arbitrary state API v2.
[Trigger](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/streaming/Trigger.html "class in org.apache.spark.sql.streaming")
Policy used to indicate how often results should be produced by a [[StreamingQuery]].
[TTLConfig](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/streaming/TTLConfig.html "class in org.apache.spark.sql.streaming")
TTL Configuration for state variable.
[ValueState](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/streaming/ValueState.html "interface in org.apache.spark.sql.streaming")<S>
Interface used for arbitrary stateful operations with the v2 API to capture single value state.


