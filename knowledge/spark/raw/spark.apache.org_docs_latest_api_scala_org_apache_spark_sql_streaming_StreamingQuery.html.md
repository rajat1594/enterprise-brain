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
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html "Permalink") package [sql](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html "Allows the execution of relational queries, including those expressed in SQL using Spark.")
Allows the execution of relational queries, including those expressed in SQL using Spark.
Allows the execution of relational queries, including those expressed in SQL using Spark.  

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/index.html "Permalink") package [streaming](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/index.html) 

Definition Classes
    [sql](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html "org.apache.spark.sql")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html "Interface used to load a streaming Dataset from external storage systems \(e.g.")[DataStreamReader](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html "Interface used to load a streaming Dataset from external storage systems \(e.g.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamWriter.html "Interface used to write a streaming Dataset to external storage systems \(e.g.")[DataStreamWriter](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamWriter.html "Interface used to write a streaming Dataset to external storage systems \(e.g.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/ExpiredTimerInfo.html "Class used to provide access to expired timer's expiry time.")[ExpiredTimerInfo](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/ExpiredTimerInfo.html "Class used to provide access to expired timer's expiry time.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/GroupState.html ":: Experimental ::")[GroupState](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/GroupState.html ":: Experimental ::")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/GroupStateTimeout.html "Represents the type of timeouts possible for the Dataset operations mapGroupsWithState and flatMapGroupsWithState.")[GroupStateTimeout](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/GroupStateTimeout.html "Represents the type of timeouts possible for the Dataset operations mapGroupsWithState and flatMapGroupsWithState.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/ListState.html)[ListState](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/ListState.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/MapState.html)[MapState](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/MapState.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/OutputMode.html "OutputMode describes what data will be written to a streaming sink when there is new data available in a streaming DataFrame/Dataset.")[OutputMode](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/OutputMode.html "OutputMode describes what data will be written to a streaming sink when there is new data available in a streaming DataFrame/Dataset.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/QueryInfo.html "Represents the query info provided to the stateful processor used in the arbitrary state API v2 to easily identify task retries on the same partition.")[QueryInfo](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/QueryInfo.html "Represents the query info provided to the stateful processor used in the arbitrary state API v2 to easily identify task retries on the same partition.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/SinkProgress.html "Information about progress made for a sink in the execution of a StreamingQuery during a trigger.")[SinkProgress](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/SinkProgress.html "Information about progress made for a sink in the execution of a StreamingQuery during a trigger.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/SourceProgress.html "Information about progress made for a source in the execution of a StreamingQuery during a trigger.")[SourceProgress](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/SourceProgress.html "Information about progress made for a source in the execution of a StreamingQuery during a trigger.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StateOperatorProgress.html "Information about updates made to stateful operators in a StreamingQuery during a trigger.")[StateOperatorProgress](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StateOperatorProgress.html "Information about updates made to stateful operators in a StreamingQuery during a trigger.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StatefulProcessor.html "Represents the arbitrary stateful logic that needs to be provided by the user to perform stateful manipulations on keyed streams.")[StatefulProcessor](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StatefulProcessor.html "Represents the arbitrary stateful logic that needs to be provided by the user to perform stateful manipulations on keyed streams.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StatefulProcessorHandle.html "Represents the operation handle provided to the stateful processor used in the arbitrary state API v2.")[StatefulProcessorHandle](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StatefulProcessorHandle.html "Represents the operation handle provided to the stateful processor used in the arbitrary state API v2.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StatefulProcessorWithInitialState.html "Stateful processor with support for specifying initial state.")[StatefulProcessorWithInitialState](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StatefulProcessorWithInitialState.html "Stateful processor with support for specifying initial state.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html "A handle to a query that is executing continuously in the background as new data arrives.")[StreamingQuery](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html "A handle to a query that is executing continuously in the background as new data arrives.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQueryException.html "Exception that stopped a StreamingQuery.")[StreamingQueryException](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQueryException.html "Exception that stopped a StreamingQuery.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQueryListener$.html "Companion object of StreamingQueryListener that defines the listener events.") [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQueryListener.html "Interface for listening to events related to StreamingQueries.")[StreamingQueryListener](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQueryListener.html "Interface for listening to events related to StreamingQueries.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQueryManager.html "A class to manage all the StreamingQuery active in a SparkSession.")[StreamingQueryManager](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQueryManager.html "A class to manage all the StreamingQuery active in a SparkSession.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQueryProgress.html "Information about progress made in the execution of a StreamingQuery during a trigger.")[StreamingQueryProgress](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQueryProgress.html "Information about progress made in the execution of a StreamingQuery during a trigger.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQueryStatus.html "Reports information about the instantaneous status of a streaming query.")[StreamingQueryStatus](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQueryStatus.html "Reports information about the instantaneous status of a streaming query.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/TTLConfig$.html) [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/TTLConfig.html "TTL Configuration for state variable.")[TTLConfig](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/TTLConfig.html "TTL Configuration for state variable.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/TestGroupState$.html) [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/TestGroupState.html ":: Experimental ::")[TestGroupState](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/TestGroupState.html ":: Experimental ::")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/TimeMode.html "Represents the time modes \(used for specifying timers and ttl\) possible for the Dataset operations transformWithState.")[TimeMode](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/TimeMode.html "Represents the time modes \(used for specifying timers and ttl\) possible for the Dataset operations transformWithState.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/TimerValues.html "Class used to provide access to timer values for processing and event time populated before method invocations using the arbitrary state API v2.")[TimerValues](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/TimerValues.html "Class used to provide access to timer values for processing and event time populated before method invocations using the arbitrary state API v2.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/Trigger.html "Policy used to indicate how often results should be produced by a StreamingQuery.")[Trigger](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/Trigger.html "Policy used to indicate how often results should be produced by a StreamingQuery.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/ValueState.html)[ValueState](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/ValueState.html)


t
[org](https://spark.apache.org/docs/latest/api/scala/org/index.html "org").[apache](https://spark.apache.org/docs/latest/api/scala/org/apache/index.html "org.apache").[spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark").[sql](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html "org.apache.spark.sql").[streaming](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/index.html "org.apache.spark.sql.streaming")
# StreamingQuery[ __](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html "Permalink")
####  trait StreamingQuery extends AnyRef
A handle to a query that is executing continuously in the background as new data arrives. All these methods are thread-safe. 

Annotations
     @Evolving() 

Source
    [StreamingQuery.scala](https://github.com/apache/spark/tree/v4.1.2/sql/api/src/main/scala/org/apache/spark/sql/streaming/StreamingQuery.scala) 

Since
    
2.0.0
Linear Supertypes
AnyRef, Any
__ __
Ordering
  1. Alphabetic
  2. By Inheritance


Inherited  

  1. StreamingQuery
  2. AnyRef
  3. Any


  1. Hide All
  2. Show All


Visibility
  1. Public
  2. Protected


### Abstract Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#awaitTermination\(timeoutMs:Long\):Boolean "Permalink") abstract  def awaitTermination(timeoutMs: Long): Boolean
Waits for the termination of `this` query, either by `query.stop()` or by an exception.
Waits for the termination of `this` query, either by `query.stop()` or by an exception. If the query has terminated with an exception, then the exception will be thrown. Otherwise, it returns whether the query has terminated or not within the `timeoutMs` milliseconds.
If the query has terminated, then all subsequent calls to this method will either return `true` immediately (if the query was terminated by `stop()`), or throw the exception immediately (if the query has terminated with exception).  

Annotations
     @throws("") 

Since
    
2.0.0 

Exceptions thrown
    
[`StreamingQueryException`](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQueryException.html "org.apache.spark.sql.streaming.StreamingQueryException") if the query has terminated with an exception
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#awaitTermination\(\):Unit "Permalink") abstract  def awaitTermination(): Unit
Waits for the termination of `this` query, either by `query.stop()` or by an exception.
Waits for the termination of `this` query, either by `query.stop()` or by an exception. If the query has terminated with an exception, then the exception will be thrown.
If the query has terminated, then all subsequent calls to this method will either return immediately (if the query was terminated by `stop()`), or throw the exception immediately (if the query has terminated with exception).  

Annotations
     @throws("") 

Since
    
2.0.0 

Exceptions thrown
    
[`StreamingQueryException`](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQueryException.html "org.apache.spark.sql.streaming.StreamingQueryException") if the query has terminated with an exception.
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#exception:Option\[org.apache.spark.sql.streaming.StreamingQueryException\] "Permalink") abstract  def exception: Option[[StreamingQueryException](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQueryException.html "org.apache.spark.sql.streaming.StreamingQueryException")]
Returns the [StreamingQueryException](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQueryException.html "org.apache.spark.sql.streaming.StreamingQueryException") if the query was terminated by an exception.
Returns the [StreamingQueryException](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQueryException.html "org.apache.spark.sql.streaming.StreamingQueryException") if the query was terminated by an exception.  

Since
    
2.0.0
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#explain\(extended:Boolean\):Unit "Permalink") abstract  def explain(extended: Boolean): Unit
Prints the physical plan to the console for debugging purposes.
Prints the physical plan to the console for debugging purposes.  

extended
    
whether to do extended explain or not 

Since
    
2.0.0
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#explain\(\):Unit "Permalink") abstract  def explain(): Unit
Prints the physical plan to the console for debugging purposes.
Prints the physical plan to the console for debugging purposes. 

Since
    
2.0.0
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#id:java.util.UUID "Permalink") abstract  def id: [UUID](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/UUID.html#java.util.UUID "java.util.UUID")
Returns the unique id of this query that persists across restarts from checkpoint data.
Returns the unique id of this query that persists across restarts from checkpoint data. That is, this id is generated when a query is started for the first time, and will be the same every time it is restarted from checkpoint data. Also see [runId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#runId:java.util.UUID).  

Since
    
2.1.0
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#isActive:Boolean "Permalink") abstract  def isActive: Boolean
Returns `true` if this query is actively running.
Returns `true` if this query is actively running.  

Since
    
2.0.0
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#lastProgress:org.apache.spark.sql.streaming.StreamingQueryProgress "Permalink") abstract  def lastProgress: [StreamingQueryProgress](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQueryProgress.html "org.apache.spark.sql.streaming.StreamingQueryProgress")
Returns the most recent [StreamingQueryProgress](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQueryProgress.html "org.apache.spark.sql.streaming.StreamingQueryProgress") update of this streaming query.
Returns the most recent [StreamingQueryProgress](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQueryProgress.html "org.apache.spark.sql.streaming.StreamingQueryProgress") update of this streaming query.  

Since
    
2.1.0
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#name:String "Permalink") abstract  def name: String
Returns the user-specified name of the query, or null if not specified.
Returns the user-specified name of the query, or null if not specified. This name can be specified in the `org.apache.spark.sql.streaming.DataStreamWriter` as `dataframe.writeStream.queryName("query").start()`. This name, if set, must be unique across all active queries.  

Since
    
2.0.0
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#processAllAvailable\(\):Unit "Permalink") abstract  def processAllAvailable(): Unit
Blocks until all available data in the source has been processed and committed to the sink.
Blocks until all available data in the source has been processed and committed to the sink. This method is intended for testing. Note that in the case of continually arriving data, this method may block forever. Additionally, this method is only guaranteed to block until data that has been synchronously appended data to a `org.apache.spark.sql.execution.streaming.Source` prior to invocation. (i.e. `getOffset` must immediately reflect the addition). 

Since
    
2.0.0
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#recentProgress:Array\[org.apache.spark.sql.streaming.StreamingQueryProgress\] "Permalink") abstract  def recentProgress: Array[[StreamingQueryProgress](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQueryProgress.html "org.apache.spark.sql.streaming.StreamingQueryProgress")]
Returns an array of the most recent [StreamingQueryProgress](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQueryProgress.html "org.apache.spark.sql.streaming.StreamingQueryProgress") updates for this query.
Returns an array of the most recent [StreamingQueryProgress](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQueryProgress.html "org.apache.spark.sql.streaming.StreamingQueryProgress") updates for this query. The number of progress updates retained for each stream is configured by Spark session configuration `spark.sql.streaming.numRecentProgressUpdates`.  

Since
    
2.1.0
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#runId:java.util.UUID "Permalink") abstract  def runId: [UUID](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/UUID.html#java.util.UUID "java.util.UUID")
Returns the unique id of this run of the query.
Returns the unique id of this run of the query. That is, every start/restart of a query will generate a unique runId. Therefore, every time a query is restarted from checkpoint, it will have the same [id](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#id:java.util.UUID) but different [runId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#runId:java.util.UUID)s. 
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#sparkSession:org.apache.spark.sql.SparkSession "Permalink") abstract  def sparkSession: [SparkSession](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/SparkSession.html "org.apache.spark.sql.SparkSession")
Returns the `SparkSession` associated with `this`.
Returns the `SparkSession` associated with `this`.  

Since
    
2.0.0
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#status:org.apache.spark.sql.streaming.StreamingQueryStatus "Permalink") abstract  def status: [StreamingQueryStatus](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQueryStatus.html "org.apache.spark.sql.streaming.StreamingQueryStatus")
Returns the current status of the query.
Returns the current status of the query.  

Since
    
2.0.2
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#stop\(\):Unit "Permalink") abstract  def stop(): Unit
Stops the execution of this query if it is running.
Stops the execution of this query if it is running. This waits until the termination of the query execution threads or until a timeout is hit.
By default stop will block indefinitely. You can configure a timeout by the configuration `spark.sql.streaming.stopTimeout`. A timeout of 0 (or negative) milliseconds will block indefinitely. If a `TimeoutException` is thrown, users can retry stopping the stream. If the issue persists, it is advisable to kill the Spark application.  

Annotations
     @throws("") 

Since
    
2.0.0


### Concrete Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html###:Int "Permalink") final  def ##: Int 

Definition Classes
    AnyRef → Any
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0 

Definition Classes
    Any
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#clone\(\):Object "Permalink") def clone(): AnyRef 

Attributes
    protected[lang]  

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#equals\(x$1:Object\):Boolean "Permalink") def equals(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef → Any
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef] 

Definition Classes
    AnyRef → Any 

Annotations
     @IntrinsicCandidate() @native()
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#hashCode\(\):Int "Permalink") def hashCode(): Int 

Definition Classes
    AnyRef → Any 

Annotations
     @IntrinsicCandidate() @native()
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean 

Definition Classes
    Any
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#notify\(\):Unit "Permalink") final  def notify(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0 

Definition Classes
    AnyRef
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#toString\(\):String "Permalink") def toString(): [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String") 

Definition Classes
    AnyRef → Any
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#wait\(\):Unit "Permalink") final  def wait(): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])


### Deprecated Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#finalize\(\):Unit "Permalink") def finalize(): Unit 

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
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html###:Int "Permalink") final  def ##: Int 

Definition Classes
    AnyRef → Any
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#clone\(\):Object "Permalink") def clone(): AnyRef 

Attributes
    protected[lang]  

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#equals\(x$1:Object\):Boolean "Permalink") def equals(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef → Any
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef] 

Definition Classes
    AnyRef → Any 

Annotations
     @IntrinsicCandidate() @native()
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#hashCode\(\):Int "Permalink") def hashCode(): Int 

Definition Classes
    AnyRef → Any 

Annotations
     @IntrinsicCandidate() @native()
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#notify\(\):Unit "Permalink") final  def notify(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0 

Definition Classes
    AnyRef
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#toString\(\):String "Permalink") def toString(): [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String") 

Definition Classes
    AnyRef → Any
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#wait\(\):Unit "Permalink") final  def wait(): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#finalize\(\):Unit "Permalink") def finalize(): Unit 

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
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0 

Definition Classes
    Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean 

Definition Classes
    Any


### Ungrouped
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#awaitTermination\(timeoutMs:Long\):Boolean "Permalink") abstract  def awaitTermination(timeoutMs: Long): Boolean
Waits for the termination of `this` query, either by `query.stop()` or by an exception.
Waits for the termination of `this` query, either by `query.stop()` or by an exception. If the query has terminated with an exception, then the exception will be thrown. Otherwise, it returns whether the query has terminated or not within the `timeoutMs` milliseconds.
If the query has terminated, then all subsequent calls to this method will either return `true` immediately (if the query was terminated by `stop()`), or throw the exception immediately (if the query has terminated with exception).  

Annotations
     @throws("") 

Since
    
2.0.0 

Exceptions thrown
    
[`StreamingQueryException`](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQueryException.html "org.apache.spark.sql.streaming.StreamingQueryException") if the query has terminated with an exception
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#awaitTermination\(\):Unit "Permalink") abstract  def awaitTermination(): Unit
Waits for the termination of `this` query, either by `query.stop()` or by an exception.
Waits for the termination of `this` query, either by `query.stop()` or by an exception. If the query has terminated with an exception, then the exception will be thrown.
If the query has terminated, then all subsequent calls to this method will either return immediately (if the query was terminated by `stop()`), or throw the exception immediately (if the query has terminated with exception).  

Annotations
     @throws("") 

Since
    
2.0.0 

Exceptions thrown
    
[`StreamingQueryException`](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQueryException.html "org.apache.spark.sql.streaming.StreamingQueryException") if the query has terminated with an exception.
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#exception:Option\[org.apache.spark.sql.streaming.StreamingQueryException\] "Permalink") abstract  def exception: Option[[StreamingQueryException](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQueryException.html "org.apache.spark.sql.streaming.StreamingQueryException")]
Returns the [StreamingQueryException](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQueryException.html "org.apache.spark.sql.streaming.StreamingQueryException") if the query was terminated by an exception.
Returns the [StreamingQueryException](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQueryException.html "org.apache.spark.sql.streaming.StreamingQueryException") if the query was terminated by an exception.  

Since
    
2.0.0
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#explain\(extended:Boolean\):Unit "Permalink") abstract  def explain(extended: Boolean): Unit
Prints the physical plan to the console for debugging purposes.
Prints the physical plan to the console for debugging purposes.  

extended
    
whether to do extended explain or not 

Since
    
2.0.0
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#explain\(\):Unit "Permalink") abstract  def explain(): Unit
Prints the physical plan to the console for debugging purposes.
Prints the physical plan to the console for debugging purposes. 

Since
    
2.0.0
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#id:java.util.UUID "Permalink") abstract  def id: [UUID](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/UUID.html#java.util.UUID "java.util.UUID")
Returns the unique id of this query that persists across restarts from checkpoint data.
Returns the unique id of this query that persists across restarts from checkpoint data. That is, this id is generated when a query is started for the first time, and will be the same every time it is restarted from checkpoint data. Also see [runId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#runId:java.util.UUID).  

Since
    
2.1.0
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#isActive:Boolean "Permalink") abstract  def isActive: Boolean
Returns `true` if this query is actively running.
Returns `true` if this query is actively running.  

Since
    
2.0.0
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#lastProgress:org.apache.spark.sql.streaming.StreamingQueryProgress "Permalink") abstract  def lastProgress: [StreamingQueryProgress](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQueryProgress.html "org.apache.spark.sql.streaming.StreamingQueryProgress")
Returns the most recent [StreamingQueryProgress](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQueryProgress.html "org.apache.spark.sql.streaming.StreamingQueryProgress") update of this streaming query.
Returns the most recent [StreamingQueryProgress](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQueryProgress.html "org.apache.spark.sql.streaming.StreamingQueryProgress") update of this streaming query.  

Since
    
2.1.0
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#name:String "Permalink") abstract  def name: String
Returns the user-specified name of the query, or null if not specified.
Returns the user-specified name of the query, or null if not specified. This name can be specified in the `org.apache.spark.sql.streaming.DataStreamWriter` as `dataframe.writeStream.queryName("query").start()`. This name, if set, must be unique across all active queries.  

Since
    
2.0.0
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#processAllAvailable\(\):Unit "Permalink") abstract  def processAllAvailable(): Unit
Blocks until all available data in the source has been processed and committed to the sink.
Blocks until all available data in the source has been processed and committed to the sink. This method is intended for testing. Note that in the case of continually arriving data, this method may block forever. Additionally, this method is only guaranteed to block until data that has been synchronously appended data to a `org.apache.spark.sql.execution.streaming.Source` prior to invocation. (i.e. `getOffset` must immediately reflect the addition). 

Since
    
2.0.0
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#recentProgress:Array\[org.apache.spark.sql.streaming.StreamingQueryProgress\] "Permalink") abstract  def recentProgress: Array[[StreamingQueryProgress](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQueryProgress.html "org.apache.spark.sql.streaming.StreamingQueryProgress")]
Returns an array of the most recent [StreamingQueryProgress](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQueryProgress.html "org.apache.spark.sql.streaming.StreamingQueryProgress") updates for this query.
Returns an array of the most recent [StreamingQueryProgress](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQueryProgress.html "org.apache.spark.sql.streaming.StreamingQueryProgress") updates for this query. The number of progress updates retained for each stream is configured by Spark session configuration `spark.sql.streaming.numRecentProgressUpdates`.  

Since
    
2.1.0
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#runId:java.util.UUID "Permalink") abstract  def runId: [UUID](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/UUID.html#java.util.UUID "java.util.UUID")
Returns the unique id of this run of the query.
Returns the unique id of this run of the query. That is, every start/restart of a query will generate a unique runId. Therefore, every time a query is restarted from checkpoint, it will have the same [id](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#id:java.util.UUID) but different [runId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#runId:java.util.UUID)s. 
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#sparkSession:org.apache.spark.sql.SparkSession "Permalink") abstract  def sparkSession: [SparkSession](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/SparkSession.html "org.apache.spark.sql.SparkSession")
Returns the `SparkSession` associated with `this`.
Returns the `SparkSession` associated with `this`.  

Since
    
2.0.0
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#status:org.apache.spark.sql.streaming.StreamingQueryStatus "Permalink") abstract  def status: [StreamingQueryStatus](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQueryStatus.html "org.apache.spark.sql.streaming.StreamingQueryStatus")
Returns the current status of the query.
Returns the current status of the query.  

Since
    
2.0.2
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#stop\(\):Unit "Permalink") abstract  def stop(): Unit
Stops the execution of this query if it is running.
Stops the execution of this query if it is running. This waits until the termination of the query execution threads or until a timeout is hit.
By default stop will block indefinitely. You can configure a timeout by the configuration `spark.sql.streaming.stopTimeout`. A timeout of 0 (or negative) milliseconds will block indefinitely. If a `TimeoutException` is thrown, users can retry stopping the stream. If the issue persists, it is advisable to kill the Spark application.  

Annotations
     @throws("") 

Since
    
2.0.0
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html###:Int "Permalink") final  def ##: Int 

Definition Classes
    AnyRef → Any
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0 

Definition Classes
    Any
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#clone\(\):Object "Permalink") def clone(): AnyRef 

Attributes
    protected[lang]  

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#equals\(x$1:Object\):Boolean "Permalink") def equals(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef → Any
  23. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef] 

Definition Classes
    AnyRef → Any 

Annotations
     @IntrinsicCandidate() @native()
  24. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#hashCode\(\):Int "Permalink") def hashCode(): Int 

Definition Classes
    AnyRef → Any 

Annotations
     @IntrinsicCandidate() @native()
  25. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean 

Definition Classes
    Any
  26. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  27. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#notify\(\):Unit "Permalink") final  def notify(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  28. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  29. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0 

Definition Classes
    AnyRef
  30. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#toString\(\):String "Permalink") def toString(): [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String") 

Definition Classes
    AnyRef → Any
  31. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  32. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  33. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#wait\(\):Unit "Permalink") final  def wait(): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  34. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StreamingQuery.html#finalize\(\):Unit "Permalink") def finalize(): Unit 

Attributes
    protected[lang]  

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.Throwable]) @Deprecated 

Deprecated
    
_(Since version 9)_


