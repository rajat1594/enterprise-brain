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


c
[org](https://spark.apache.org/docs/latest/api/scala/org/index.html "org").[apache](https://spark.apache.org/docs/latest/api/scala/org/apache/index.html "org.apache").[spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark").[sql](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html "org.apache.spark.sql").[streaming](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/index.html "org.apache.spark.sql.streaming")
# DataStreamReader[ __](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html "Permalink")
####  abstract  class DataStreamReader extends AnyRef
Interface used to load a streaming `Dataset` from external storage systems (e.g. file systems, key-value stores, etc). Use `SparkSession.readStream` to access this.  

Annotations
     @Evolving() 

Source
    [DataStreamReader.scala](https://github.com/apache/spark/tree/v4.1.2/sql/api/src/main/scala/org/apache/spark/sql/streaming/DataStreamReader.scala) 

Since
    
2.0.0
Linear Supertypes
AnyRef, Any
__ __
Ordering
  1. Alphabetic
  2. By Inheritance


Inherited  

  1. DataStreamReader
  2. AnyRef
  3. Any


  1. Hide All
  2. Show All


Visibility
  1. Public
  2. Protected


### Instance Constructors
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#<init>\(\):org.apache.spark.sql.streaming.DataStreamReader "Permalink") new DataStreamReader()


### Abstract Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#assertNoSpecifiedSchema\(operation:String\):Unit "Permalink") abstract  def assertNoSpecifiedSchema(operation: String): Unit 

Attributes
    protected 
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#format\(source:String\):DataStreamReader.this.type "Permalink") abstract  def format(source: String): [DataStreamReader](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html "org.apache.spark.sql.streaming.DataStreamReader").this.type
Specifies the input data source format.
Specifies the input data source format.  

Since
    
2.0.0
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#load\(path:String\):org.apache.spark.sql.DataFrame "Permalink") abstract  def load(path: String): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Loads input in as a `DataFrame`, for data streams that read from some path.
Loads input in as a `DataFrame`, for data streams that read from some path.  

Since
    
2.0.0
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#load\(\):org.apache.spark.sql.DataFrame "Permalink") abstract  def load(): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Loads input data stream in as a `DataFrame`, for data streams that don't require a path (e.g.
Loads input data stream in as a `DataFrame`, for data streams that don't require a path (e.g. external key-value stores).  

Since
    
2.0.0
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#option\(key:String,value:String\):DataStreamReader.this.type "Permalink") abstract  def option(key: String, value: String): [DataStreamReader](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html "org.apache.spark.sql.streaming.DataStreamReader").this.type
Adds an input option for the underlying data source.
Adds an input option for the underlying data source.  

Since
    
2.0.0
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#options\(options:scala.collection.Map\[String,String\]\):DataStreamReader.this.type "Permalink") abstract  def options(options: Map[String, String]): [DataStreamReader](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html "org.apache.spark.sql.streaming.DataStreamReader").this.type
(Scala-specific) Adds input options for the underlying data source.
(Scala-specific) Adds input options for the underlying data source.  

Since
    
2.0.0
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#schema\(schema:org.apache.spark.sql.types.StructType\):DataStreamReader.this.type "Permalink") abstract  def schema(schema: [StructType](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/types/StructType.html "org.apache.spark.sql.types.StructType")): [DataStreamReader](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html "org.apache.spark.sql.streaming.DataStreamReader").this.type
Specifies the input schema.
Specifies the input schema. Some data sources (e.g. JSON) can infer the input schema automatically from data. By specifying the schema here, the underlying data source can skip the schema inference step, and thus speed up data loading.  

Since
    
2.0.0
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#table\(tableName:String\):org.apache.spark.sql.DataFrame "Permalink") abstract  def table(tableName: String): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Define a Streaming DataFrame on a Table.
Define a Streaming DataFrame on a Table. The DataSource corresponding to the table should support streaming mode. 

tableName
    
The name of the table 

Since
    
3.1.0


### Concrete Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html###:Int "Permalink") final  def ##: Int 

Definition Classes
    AnyRef → Any
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0 

Definition Classes
    Any
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#clone\(\):Object "Permalink") def clone(): AnyRef 

Attributes
    protected[lang]  

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#csv\(path:String\):org.apache.spark.sql.DataFrame "Permalink") def csv(path: String): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Loads a CSV file stream and returns the result as a `DataFrame`.
Loads a CSV file stream and returns the result as a `DataFrame`.
This function will go through the input once to determine the input schema if `inferSchema` is enabled. To avoid going through the entire data once, disable `inferSchema` option or specify the schema explicitly using `schema`.
You can set the following option(s):
     * `maxFilesPerTrigger` (default: no max limit): sets the maximum number of new files to be considered in every trigger.
     * `maxBytesPerTrigger` (default: no max limit): sets the maximum total size of new files to be considered in every trigger.
You can find the CSV-specific options for reading CSV file stream in <a href="https://spark.apache.org/docs/latest/sql-data-sources-csv.html#data-source-option"> Data Source Option in the version you use.  

Since
    
2.0.0
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#equals\(x$1:Object\):Boolean "Permalink") def equals(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef → Any
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef] 

Definition Classes
    AnyRef → Any 

Annotations
     @IntrinsicCandidate() @native()
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#hashCode\(\):Int "Permalink") def hashCode(): Int 

Definition Classes
    AnyRef → Any 

Annotations
     @IntrinsicCandidate() @native()
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean 

Definition Classes
    Any
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#json\(path:String\):org.apache.spark.sql.DataFrame "Permalink") def json(path: String): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Loads a JSON file stream and returns the results as a `DataFrame`.
Loads a JSON file stream and returns the results as a `DataFrame`.
[JSON Lines](http://jsonlines.org/) (newline-delimited JSON) is supported by default. For JSON (one record per file), set the `multiLine` option to true.
This function goes through the input once to determine the input schema. If you know the schema in advance, use the version that specifies the schema to avoid the extra scan.
You can set the following option(s):
     * `maxFilesPerTrigger` (default: no max limit): sets the maximum number of new files to be considered in every trigger.
     * `maxBytesPerTrigger` (default: no max limit): sets the maximum total size of new files to be considered in every trigger.
You can find the JSON-specific options for reading JSON file stream in <a href="https://spark.apache.org/docs/latest/sql-data-sources-json.html#data-source-option"> Data Source Option in the version you use.  

Since
    
2.0.0
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#notify\(\):Unit "Permalink") final  def notify(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#option\(key:String,value:Double\):DataStreamReader.this.type "Permalink") def option(key: String, value: Double): [DataStreamReader](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html "org.apache.spark.sql.streaming.DataStreamReader").this.type
Adds an input option for the underlying data source.
Adds an input option for the underlying data source.  

Since
    
2.0.0
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#option\(key:String,value:Long\):DataStreamReader.this.type "Permalink") def option(key: String, value: Long): [DataStreamReader](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html "org.apache.spark.sql.streaming.DataStreamReader").this.type
Adds an input option for the underlying data source.
Adds an input option for the underlying data source.  

Since
    
2.0.0
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#option\(key:String,value:Boolean\):DataStreamReader.this.type "Permalink") def option(key: String, value: Boolean): [DataStreamReader](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html "org.apache.spark.sql.streaming.DataStreamReader").this.type
Adds an input option for the underlying data source.
Adds an input option for the underlying data source.  

Since
    
2.0.0
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#options\(options:java.util.Map\[String,String\]\):DataStreamReader.this.type "Permalink") def options(options: [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#java.util.Map "java.util.Map")[String, String]): [DataStreamReader](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html "org.apache.spark.sql.streaming.DataStreamReader").this.type
(Java-specific) Adds input options for the underlying data source.
(Java-specific) Adds input options for the underlying data source.  

Since
    
2.0.0
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#orc\(path:String\):org.apache.spark.sql.DataFrame "Permalink") def orc(path: String): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Loads a ORC file stream, returning the result as a `DataFrame`.
Loads a ORC file stream, returning the result as a `DataFrame`.
You can set the following option(s):
     * `maxFilesPerTrigger` (default: no max limit): sets the maximum number of new files to be considered in every trigger.
     * `maxBytesPerTrigger` (default: no max limit): sets the maximum total size of new files to be considered in every trigger.
ORC-specific option(s) for reading ORC file stream can be found in [ Data Source Option](https://spark.apache.org/docs/latest/sql-data-sources-orc.html#data-source-option) in the version you use.  

Since
    
2.3.0
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#parquet\(path:String\):org.apache.spark.sql.DataFrame "Permalink") def parquet(path: String): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Loads a Parquet file stream, returning the result as a `DataFrame`.
Loads a Parquet file stream, returning the result as a `DataFrame`.
You can set the following option(s):
     * `maxFilesPerTrigger` (default: no max limit): sets the maximum number of new files to be considered in every trigger.
     * `maxBytesPerTrigger` (default: no max limit): sets the maximum total size of new files to be considered in every trigger.
Parquet-specific option(s) for reading Parquet file stream can be found in [ Data Source Option](https://spark.apache.org/docs/latest/sql-data-sources-parquet.html#data-source-option) in the version you use.  

Since
    
2.0.0
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#schema\(schemaString:String\):DataStreamReader.this.type "Permalink") def schema(schemaString: String): [DataStreamReader](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html "org.apache.spark.sql.streaming.DataStreamReader").this.type
Specifies the schema by using the input DDL-formatted string.
Specifies the schema by using the input DDL-formatted string. Some data sources (e.g. JSON) can infer the input schema automatically from data. By specifying the schema here, the underlying data source can skip the schema inference step, and thus speed up data loading.  

Since
    
2.3.0
  23. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0 

Definition Classes
    AnyRef
  24. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#text\(path:String\):org.apache.spark.sql.DataFrame "Permalink") def text(path: String): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Loads text files and returns a `DataFrame` whose schema starts with a string column named "value", and followed by partitioned columns if there are any.
Loads text files and returns a `DataFrame` whose schema starts with a string column named "value", and followed by partitioned columns if there are any. The text files must be encoded as UTF-8.
By default, each line in the text files is a new row in the resulting DataFrame. For example:

```
// Scala:
spark.readStream.text("/path/to/directory/")

// Java:
spark.readStream().text("/path/to/directory/")
```

You can set the following option(s):
     * `maxFilesPerTrigger` (default: no max limit): sets the maximum number of new files to be considered in every trigger.
     * `maxBytesPerTrigger` (default: no max limit): sets the maximum total size of new files to be considered in every trigger.
You can find the text-specific options for reading text files in <a href="https://spark.apache.org/docs/latest/sql-data-sources-text.html#data-source-option"> Data Source Option in the version you use.  

Since
    
2.0.0
  25. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#textFile\(path:String\):org.apache.spark.sql.Dataset\[String\] "Permalink") def textFile(path: String): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[String]
Loads text file(s) and returns a `Dataset` of String.
Loads text file(s) and returns a `Dataset` of String. The underlying schema of the Dataset contains a single string column named "value". The text files must be encoded as UTF-8.
If the directory structure of the text files contains partitioning information, those are ignored in the resulting Dataset. To include partitioning information as columns, use `text`.
By default, each line in the text file is a new element in the resulting Dataset. For example:

```
// Scala:
spark.readStream.textFile("/path/to/spark/README.md")

// Java:
spark.readStream().textFile("/path/to/spark/README.md")
```

You can set the text-specific options as specified in `DataStreamReader.text`.  

path
    
input path 

Since
    
2.1.0
  26. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#toString\(\):String "Permalink") def toString(): [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String") 

Definition Classes
    AnyRef → Any
  27. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#validateJsonSchema\(\):Unit "Permalink") def validateJsonSchema(): Unit 

Attributes
    protected 
  28. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#validateXmlSchema\(\):Unit "Permalink") def validateXmlSchema(): Unit 

Attributes
    protected 
  29. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  30. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  31. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#wait\(\):Unit "Permalink") final  def wait(): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  32. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#xml\(path:String\):org.apache.spark.sql.DataFrame "Permalink") def xml(path: String): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Loads a XML file stream and returns the result as a `DataFrame`.
Loads a XML file stream and returns the result as a `DataFrame`.
This function will go through the input once to determine the input schema if `inferSchema` is enabled. To avoid going through the entire data once, disable `inferSchema` option or specify the schema explicitly using `schema`.
You can set the following option(s):
     * `maxFilesPerTrigger` (default: no max limit): sets the maximum number of new files to be considered in every trigger.
     * `maxBytesPerTrigger` (default: no max limit): sets the maximum total size of new files to be considered in every trigger.
You can find the XML-specific options for reading XML file stream in <a href="https://spark.apache.org/docs/latest/sql-data-sources-xml.html#data-source-option"> Data Source Option in the version you use.  

Since
    
4.0.0


### Deprecated Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#finalize\(\):Unit "Permalink") def finalize(): Unit 

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
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html###:Int "Permalink") final  def ##: Int 

Definition Classes
    AnyRef → Any
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#clone\(\):Object "Permalink") def clone(): AnyRef 

Attributes
    protected[lang]  

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#equals\(x$1:Object\):Boolean "Permalink") def equals(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef → Any
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef] 

Definition Classes
    AnyRef → Any 

Annotations
     @IntrinsicCandidate() @native()
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#hashCode\(\):Int "Permalink") def hashCode(): Int 

Definition Classes
    AnyRef → Any 

Annotations
     @IntrinsicCandidate() @native()
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#notify\(\):Unit "Permalink") final  def notify(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0 

Definition Classes
    AnyRef
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#toString\(\):String "Permalink") def toString(): [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String") 

Definition Classes
    AnyRef → Any
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#wait\(\):Unit "Permalink") final  def wait(): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#finalize\(\):Unit "Permalink") def finalize(): Unit 

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
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0 

Definition Classes
    Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean 

Definition Classes
    Any


### Ungrouped
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#assertNoSpecifiedSchema\(operation:String\):Unit "Permalink") abstract  def assertNoSpecifiedSchema(operation: String): Unit 

Attributes
    protected 
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#format\(source:String\):DataStreamReader.this.type "Permalink") abstract  def format(source: String): [DataStreamReader](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html "org.apache.spark.sql.streaming.DataStreamReader").this.type
Specifies the input data source format.
Specifies the input data source format.  

Since
    
2.0.0
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#load\(path:String\):org.apache.spark.sql.DataFrame "Permalink") abstract  def load(path: String): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Loads input in as a `DataFrame`, for data streams that read from some path.
Loads input in as a `DataFrame`, for data streams that read from some path.  

Since
    
2.0.0
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#load\(\):org.apache.spark.sql.DataFrame "Permalink") abstract  def load(): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Loads input data stream in as a `DataFrame`, for data streams that don't require a path (e.g.
Loads input data stream in as a `DataFrame`, for data streams that don't require a path (e.g. external key-value stores).  

Since
    
2.0.0
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#option\(key:String,value:String\):DataStreamReader.this.type "Permalink") abstract  def option(key: String, value: String): [DataStreamReader](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html "org.apache.spark.sql.streaming.DataStreamReader").this.type
Adds an input option for the underlying data source.
Adds an input option for the underlying data source.  

Since
    
2.0.0
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#options\(options:scala.collection.Map\[String,String\]\):DataStreamReader.this.type "Permalink") abstract  def options(options: Map[String, String]): [DataStreamReader](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html "org.apache.spark.sql.streaming.DataStreamReader").this.type
(Scala-specific) Adds input options for the underlying data source.
(Scala-specific) Adds input options for the underlying data source.  

Since
    
2.0.0
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#schema\(schema:org.apache.spark.sql.types.StructType\):DataStreamReader.this.type "Permalink") abstract  def schema(schema: [StructType](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/types/StructType.html "org.apache.spark.sql.types.StructType")): [DataStreamReader](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html "org.apache.spark.sql.streaming.DataStreamReader").this.type
Specifies the input schema.
Specifies the input schema. Some data sources (e.g. JSON) can infer the input schema automatically from data. By specifying the schema here, the underlying data source can skip the schema inference step, and thus speed up data loading.  

Since
    
2.0.0
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#table\(tableName:String\):org.apache.spark.sql.DataFrame "Permalink") abstract  def table(tableName: String): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Define a Streaming DataFrame on a Table.
Define a Streaming DataFrame on a Table. The DataSource corresponding to the table should support streaming mode. 

tableName
    
The name of the table 

Since
    
3.1.0
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html###:Int "Permalink") final  def ##: Int 

Definition Classes
    AnyRef → Any
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0 

Definition Classes
    Any
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#clone\(\):Object "Permalink") def clone(): AnyRef 

Attributes
    protected[lang]  

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#csv\(path:String\):org.apache.spark.sql.DataFrame "Permalink") def csv(path: String): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Loads a CSV file stream and returns the result as a `DataFrame`.
Loads a CSV file stream and returns the result as a `DataFrame`.
This function will go through the input once to determine the input schema if `inferSchema` is enabled. To avoid going through the entire data once, disable `inferSchema` option or specify the schema explicitly using `schema`.
You can set the following option(s):
     * `maxFilesPerTrigger` (default: no max limit): sets the maximum number of new files to be considered in every trigger.
     * `maxBytesPerTrigger` (default: no max limit): sets the maximum total size of new files to be considered in every trigger.
You can find the CSV-specific options for reading CSV file stream in <a href="https://spark.apache.org/docs/latest/sql-data-sources-csv.html#data-source-option"> Data Source Option in the version you use.  

Since
    
2.0.0
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#equals\(x$1:Object\):Boolean "Permalink") def equals(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef → Any
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef] 

Definition Classes
    AnyRef → Any 

Annotations
     @IntrinsicCandidate() @native()
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#hashCode\(\):Int "Permalink") def hashCode(): Int 

Definition Classes
    AnyRef → Any 

Annotations
     @IntrinsicCandidate() @native()
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean 

Definition Classes
    Any
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#json\(path:String\):org.apache.spark.sql.DataFrame "Permalink") def json(path: String): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Loads a JSON file stream and returns the results as a `DataFrame`.
Loads a JSON file stream and returns the results as a `DataFrame`.
[JSON Lines](http://jsonlines.org/) (newline-delimited JSON) is supported by default. For JSON (one record per file), set the `multiLine` option to true.
This function goes through the input once to determine the input schema. If you know the schema in advance, use the version that specifies the schema to avoid the extra scan.
You can set the following option(s):
     * `maxFilesPerTrigger` (default: no max limit): sets the maximum number of new files to be considered in every trigger.
     * `maxBytesPerTrigger` (default: no max limit): sets the maximum total size of new files to be considered in every trigger.
You can find the JSON-specific options for reading JSON file stream in <a href="https://spark.apache.org/docs/latest/sql-data-sources-json.html#data-source-option"> Data Source Option in the version you use.  

Since
    
2.0.0
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#notify\(\):Unit "Permalink") final  def notify(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  23. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  24. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#option\(key:String,value:Double\):DataStreamReader.this.type "Permalink") def option(key: String, value: Double): [DataStreamReader](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html "org.apache.spark.sql.streaming.DataStreamReader").this.type
Adds an input option for the underlying data source.
Adds an input option for the underlying data source.  

Since
    
2.0.0
  25. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#option\(key:String,value:Long\):DataStreamReader.this.type "Permalink") def option(key: String, value: Long): [DataStreamReader](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html "org.apache.spark.sql.streaming.DataStreamReader").this.type
Adds an input option for the underlying data source.
Adds an input option for the underlying data source.  

Since
    
2.0.0
  26. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#option\(key:String,value:Boolean\):DataStreamReader.this.type "Permalink") def option(key: String, value: Boolean): [DataStreamReader](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html "org.apache.spark.sql.streaming.DataStreamReader").this.type
Adds an input option for the underlying data source.
Adds an input option for the underlying data source.  

Since
    
2.0.0
  27. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#options\(options:java.util.Map\[String,String\]\):DataStreamReader.this.type "Permalink") def options(options: [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#java.util.Map "java.util.Map")[String, String]): [DataStreamReader](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html "org.apache.spark.sql.streaming.DataStreamReader").this.type
(Java-specific) Adds input options for the underlying data source.
(Java-specific) Adds input options for the underlying data source.  

Since
    
2.0.0
  28. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#orc\(path:String\):org.apache.spark.sql.DataFrame "Permalink") def orc(path: String): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Loads a ORC file stream, returning the result as a `DataFrame`.
Loads a ORC file stream, returning the result as a `DataFrame`.
You can set the following option(s):
     * `maxFilesPerTrigger` (default: no max limit): sets the maximum number of new files to be considered in every trigger.
     * `maxBytesPerTrigger` (default: no max limit): sets the maximum total size of new files to be considered in every trigger.
ORC-specific option(s) for reading ORC file stream can be found in [ Data Source Option](https://spark.apache.org/docs/latest/sql-data-sources-orc.html#data-source-option) in the version you use.  

Since
    
2.3.0
  29. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#parquet\(path:String\):org.apache.spark.sql.DataFrame "Permalink") def parquet(path: String): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Loads a Parquet file stream, returning the result as a `DataFrame`.
Loads a Parquet file stream, returning the result as a `DataFrame`.
You can set the following option(s):
     * `maxFilesPerTrigger` (default: no max limit): sets the maximum number of new files to be considered in every trigger.
     * `maxBytesPerTrigger` (default: no max limit): sets the maximum total size of new files to be considered in every trigger.
Parquet-specific option(s) for reading Parquet file stream can be found in [ Data Source Option](https://spark.apache.org/docs/latest/sql-data-sources-parquet.html#data-source-option) in the version you use.  

Since
    
2.0.0
  30. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#schema\(schemaString:String\):DataStreamReader.this.type "Permalink") def schema(schemaString: String): [DataStreamReader](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html "org.apache.spark.sql.streaming.DataStreamReader").this.type
Specifies the schema by using the input DDL-formatted string.
Specifies the schema by using the input DDL-formatted string. Some data sources (e.g. JSON) can infer the input schema automatically from data. By specifying the schema here, the underlying data source can skip the schema inference step, and thus speed up data loading.  

Since
    
2.3.0
  31. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0 

Definition Classes
    AnyRef
  32. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#text\(path:String\):org.apache.spark.sql.DataFrame "Permalink") def text(path: String): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Loads text files and returns a `DataFrame` whose schema starts with a string column named "value", and followed by partitioned columns if there are any.
Loads text files and returns a `DataFrame` whose schema starts with a string column named "value", and followed by partitioned columns if there are any. The text files must be encoded as UTF-8.
By default, each line in the text files is a new row in the resulting DataFrame. For example:

```
// Scala:
spark.readStream.text("/path/to/directory/")

// Java:
spark.readStream().text("/path/to/directory/")
```

You can set the following option(s):
     * `maxFilesPerTrigger` (default: no max limit): sets the maximum number of new files to be considered in every trigger.
     * `maxBytesPerTrigger` (default: no max limit): sets the maximum total size of new files to be considered in every trigger.
You can find the text-specific options for reading text files in <a href="https://spark.apache.org/docs/latest/sql-data-sources-text.html#data-source-option"> Data Source Option in the version you use.  

Since
    
2.0.0
  33. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#textFile\(path:String\):org.apache.spark.sql.Dataset\[String\] "Permalink") def textFile(path: String): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[String]
Loads text file(s) and returns a `Dataset` of String.
Loads text file(s) and returns a `Dataset` of String. The underlying schema of the Dataset contains a single string column named "value". The text files must be encoded as UTF-8.
If the directory structure of the text files contains partitioning information, those are ignored in the resulting Dataset. To include partitioning information as columns, use `text`.
By default, each line in the text file is a new element in the resulting Dataset. For example:

```
// Scala:
spark.readStream.textFile("/path/to/spark/README.md")

// Java:
spark.readStream().textFile("/path/to/spark/README.md")
```

You can set the text-specific options as specified in `DataStreamReader.text`.  

path
    
input path 

Since
    
2.1.0
  34. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#toString\(\):String "Permalink") def toString(): [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String") 

Definition Classes
    AnyRef → Any
  35. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#validateJsonSchema\(\):Unit "Permalink") def validateJsonSchema(): Unit 

Attributes
    protected 
  36. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#validateXmlSchema\(\):Unit "Permalink") def validateXmlSchema(): Unit 

Attributes
    protected 
  37. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  38. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  39. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#wait\(\):Unit "Permalink") final  def wait(): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  40. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#xml\(path:String\):org.apache.spark.sql.DataFrame "Permalink") def xml(path: String): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Loads a XML file stream and returns the result as a `DataFrame`.
Loads a XML file stream and returns the result as a `DataFrame`.
This function will go through the input once to determine the input schema if `inferSchema` is enabled. To avoid going through the entire data once, disable `inferSchema` option or specify the schema explicitly using `schema`.
You can set the following option(s):
     * `maxFilesPerTrigger` (default: no max limit): sets the maximum number of new files to be considered in every trigger.
     * `maxBytesPerTrigger` (default: no max limit): sets the maximum total size of new files to be considered in every trigger.
You can find the XML-specific options for reading XML file stream in <a href="https://spark.apache.org/docs/latest/sql-data-sources-xml.html#data-source-option"> Data Source Option in the version you use.  

Since
    
4.0.0
  41. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamReader.html#finalize\(\):Unit "Permalink") def finalize(): Unit 

Attributes
    protected[lang]  

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.Throwable]) @Deprecated 

Deprecated
    
_(Since version 9)_


