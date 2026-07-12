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
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/index.html "Permalink") package [api](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/index.html) 

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/broadcast/index.html "Permalink") package [broadcast](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/broadcast/index.html "Spark's broadcast variables, used to broadcast immutable datasets to all nodes.")
Spark's broadcast variables, used to broadcast immutable datasets to all nodes.
Spark's broadcast variables, used to broadcast immutable datasets to all nodes.  

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html "Permalink") package graphx
ALPHA COMPONENT GraphX is a graph processing framework built on top of Spark.
ALPHA COMPONENT GraphX is a graph processing framework built on top of Spark.  

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/impl/index.html "Permalink") package [impl](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/impl/index.html)
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/index.html "Permalink") package [lib](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/index.html "Various analytics functions for graphs.")
Various analytics functions for graphs.
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/util/index.html "Permalink") package [util](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/util/index.html "Collections of utilities used by graphx.")
Collections of utilities used by graphx.
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge$.html) [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html "A single directed edge consisting of a source id, target id, and the data associated with the edge.")[Edge](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html "A single directed edge consisting of a source id, target id, and the data associated with the edge.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/EdgeContext$.html) [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/EdgeContext.html "Represents an edge along with its neighboring vertices and allows sending messages along the edge.")[EdgeContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/EdgeContext.html "Represents an edge along with its neighboring vertices and allows sending messages along the edge.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/EdgeDirection$.html "A set of EdgeDirections.") [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/EdgeDirection.html "The direction of a directed edge relative to a vertex.")[EdgeDirection](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/EdgeDirection.html "The direction of a directed edge relative to a vertex.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/EdgeRDD$.html) [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/EdgeRDD.html "EdgeRDD\[ED, VD\] extends RDD\[Edge\[ED\]\] by storing the edges in columnar format on each partition for performance.")[EdgeRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/EdgeRDD.html "EdgeRDD\[ED, VD\] extends RDD\[Edge\[ED\]\] by storing the edges in columnar format on each partition for performance.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/EdgeTriplet.html "An edge triplet represents an edge along with the vertex attributes of its neighboring vertices.")[EdgeTriplet](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/EdgeTriplet.html "An edge triplet represents an edge along with the vertex attributes of its neighboring vertices.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph$.html "The Graph object contains a collection of routines used to construct graphs from RDDs.") [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "The Graph abstractly represents a graph with arbitrary objects associated with vertices and edges.")[Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "The Graph abstractly represents a graph with arbitrary objects associated with vertices and edges.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphLoader$.html "Provides utilities for loading Graphs from files.")[GraphLoader](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphLoader$.html "Provides utilities for loading Graphs from files.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html "Contains additional functionality for Graph.")[GraphOps](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html "Contains additional functionality for Graph.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphXUtils$.html)[GraphXUtils](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphXUtils$.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/PartitionStrategy$.html "Collection of built-in PartitionStrategy implementations.") [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/PartitionStrategy.html "Represents the way edges are assigned to edge partitions based on their source and destination vertex IDs.")[PartitionStrategy](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/PartitionStrategy.html "Represents the way edges are assigned to edge partitions based on their source and destination vertex IDs.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Pregel$.html "Implements a Pregel-like bulk-synchronous message-passing API.")[Pregel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Pregel$.html "Implements a Pregel-like bulk-synchronous message-passing API.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/TripletFields.html "Represents a subset of the fields of an EdgeTriplet or EdgeContext.")[TripletFields](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/TripletFields.html "Represents a subset of the fields of an EdgeTriplet or EdgeContext.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD$.html "The VertexRDD singleton is used to construct VertexRDDs.") [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "Extends RDD\[\(VertexId, VD\)\] by ensuring that there is only one entry for each vertex and by pre-indexing the entries for fast, efficient joins.")[VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "Extends RDD\[\(VertexId, VD\)\] by ensuring that there is only one entry for each vertex and by pre-indexing the entries for fast, efficient joins.")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/input/index.html "Permalink") package [input](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/input/index.html) 

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/index.html "Permalink") package [io](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/index.html "IO codecs used for compression.")
IO codecs used for compression.
IO codecs used for compression. See [org.apache.spark.io.CompressionCodec](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/CompressionCodec.html "org.apache.spark.io.CompressionCodec").  

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/launcher/index.html "Permalink") package [launcher](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/launcher/index.html) 

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/mapred/index.html "Permalink") package [mapred](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/mapred/index.html) 

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/metrics/index.html "Permalink") package [metrics](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/metrics/index.html) 

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/index.html "Permalink") package [ml](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/index.html "DataFrame-based machine learning APIs to let users quickly assemble and configure practical machine learning pipelines.")
DataFrame-based machine learning APIs to let users quickly assemble and configure practical machine learning pipelines.
DataFrame-based machine learning APIs to let users quickly assemble and configure practical machine learning pipelines.  

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/mllib/index.html "Permalink") package [mllib](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/mllib/index.html "RDD-based machine learning APIs \(in maintenance mode\).")
RDD-based machine learning APIs (in maintenance mode).
RDD-based machine learning APIs (in maintenance mode).
The `spark.mllib` package is in maintenance mode as of the Spark 2.0.0 release to encourage migration to the DataFrame-based APIs under the [org.apache.spark.ml](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/index.html "org.apache.spark.ml") package. While in maintenance mode,
    * no new features in the RDD-based `spark.mllib` package will be accepted, unless they block implementing new features in the DataFrame-based `spark.ml` package;
    * bug fixes in the RDD-based APIs will still be accepted.
The developers will continue adding more features to the DataFrame-based APIs in the 2.x series to reach feature parity with the RDD-based APIs. And once we reach feature parity, this package will be deprecated.  

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark") 

See also
    
[SPARK-4591](https://issues.apache.org/jira/browse/SPARK-4591) to track the progress of feature parity
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/partial/index.html "Permalink") package [partial](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/partial/index.html "Support for approximate results.")
Support for approximate results.
Support for approximate results. This provides convenient api and also implementation for approximate calculation.  

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark") 

See also
    
[org.apache.spark.rdd.RDD.countApprox](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html#countApprox\(timeout:Long,confidence:Double\):org.apache.spark.partial.PartialResult\[org.apache.spark.partial.BoundedDouble\])
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/paths/index.html "Permalink") package [paths](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/paths/index.html) 

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/index.html "Permalink") package [rdd](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/index.html "Provides several RDD implementations.")
Provides several RDD implementations.
Provides several RDD implementations. See [org.apache.spark.rdd.RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD").  

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/resource/index.html "Permalink") package [resource](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/resource/index.html) 

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/index.html "Permalink") package [scheduler](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/index.html "Spark's scheduling components.")
Spark's scheduling components.
Spark's scheduling components. This includes the `org.apache.spark.scheduler.DAGScheduler` and lower level `org.apache.spark.scheduler.TaskScheduler`.  

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/security/index.html "Permalink") package [security](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/security/index.html) 

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/index.html "Permalink") package [serializer](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/index.html "Pluggable serializers for RDD and shuffle data.")
Pluggable serializers for RDD and shuffle data.
Pluggable serializers for RDD and shuffle data.  

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark") 

See also
    
[org.apache.spark.serializer.Serializer](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/Serializer.html "org.apache.spark.serializer.Serializer")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/shuffle/index.html "Permalink") package [shuffle](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/shuffle/index.html) 

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html "Permalink") package [sql](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html "Allows the execution of relational queries, including those expressed in SQL using Spark.")
Allows the execution of relational queries, including those expressed in SQL using Spark.
Allows the execution of relational queries, including those expressed in SQL using Spark.  

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/status/index.html "Permalink") package [status](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/status/index.html) 

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/index.html "Permalink") package [storage](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/index.html) 

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/index.html "Permalink") package [streaming](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/index.html "Spark Streaming functionality.")
Spark Streaming functionality.
Spark Streaming functionality. [org.apache.spark.streaming.StreamingContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html "org.apache.spark.streaming.StreamingContext") serves as the main entry point to Spark Streaming, while [org.apache.spark.streaming.dstream.DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream") is the data type representing a continuous sequence of RDDs, representing a continuous stream of data.
In addition, [org.apache.spark.streaming.dstream.PairDStreamFunctions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html "org.apache.spark.streaming.dstream.PairDStreamFunctions") contains operations available only on DStreams of key-value pairs, such as `groupByKey` and `reduceByKey`. These operations are automatically available on any DStream of the right type (e.g. DStream[(Int, Int)] through implicit conversions.
For the Java API of Spark Streaming, take a look at the [org.apache.spark.streaming.api.java.JavaStreamingContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html "org.apache.spark.streaming.api.java.JavaStreamingContext") which serves as the entry point, and the [org.apache.spark.streaming.api.java.JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream") and the [org.apache.spark.streaming.api.java.JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream") which have the DStream functionality.  

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ui/index.html "Permalink") package [ui](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ui/index.html) 

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/unsafe/index.html "Permalink") package [unsafe](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/unsafe/index.html) 

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/index.html "Permalink") package [util](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/index.html "Spark utilities.")
Spark utilities.
Spark utilities.  

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")


p
[org](https://spark.apache.org/docs/latest/api/scala/org/index.html "org").[apache](https://spark.apache.org/docs/latest/api/scala/org/apache/index.html "org.apache").[spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
# graphx[ __](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html "Permalink")
####  package graphx
ALPHA COMPONENT GraphX is a graph processing framework built on top of Spark.  

Source
    [package.scala](https://github.com/apache/spark/tree/v4.1.2/graphx/src/main/scala/org/apache/spark/graphx/package.scala)
Linear Supertypes
AnyRef, Any
__ __
Ordering
  1. Alphabetic
  2. By Inheritance


Inherited  

  1. graphx
  2. AnyRef
  3. Any


  1. Hide All
  2. Show All


Visibility
  1. Public
  2. Protected


### Package Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/impl/index.html "Permalink") package [impl](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/impl/index.html)
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/index.html "Permalink") package [lib](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/index.html "Various analytics functions for graphs.")
Various analytics functions for graphs.
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/util/index.html "Permalink") package [util](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/util/index.html "Collections of utilities used by graphx.")
Collections of utilities used by graphx.


### Type Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html "Permalink") case class [Edge](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html "A single directed edge consisting of a source id, target id, and the data associated with the edge.")[ED](srcId: [VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long) = 0, dstId: [VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long) = 0, attr: ED = null.asInstanceOf[ED]) extends Serializable with Product
A single directed edge consisting of a source id, target id, and the data associated with the edge.
A single directed edge consisting of a source id, target id, and the data associated with the edge.  

ED
    
type of the edge attribute 

srcId
    
The vertex id of the source vertex 

dstId
    
The vertex id of the target vertex 

attr
    
The attribute associated with the edge
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/EdgeContext.html "Permalink") abstract  class [EdgeContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/EdgeContext.html "Represents an edge along with its neighboring vertices and allows sending messages along the edge.")[VD, ED, A] extends AnyRef
Represents an edge along with its neighboring vertices and allows sending messages along the edge.
Represents an edge along with its neighboring vertices and allows sending messages along the edge. Used in [Graph#aggregateMessages](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html#aggregateMessages\[A\]\(sendMsg:org.apache.spark.graphx.EdgeContext\[VD,ED,A\]=>Unit,mergeMsg:\(A,A\)=>A,tripletFields:org.apache.spark.graphx.TripletFields\)\(implicitevidence$11:scala.reflect.ClassTag\[A\]\):org.apache.spark.graphx.VertexRDD\[A\]). 
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/EdgeDirection.html "Permalink") class [EdgeDirection](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/EdgeDirection.html "The direction of a directed edge relative to a vertex.") extends Serializable
The direction of a directed edge relative to a vertex.
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/EdgeRDD.html "Permalink") abstract  class [EdgeRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/EdgeRDD.html "EdgeRDD\[ED, VD\] extends RDD\[Edge\[ED\]\] by storing the edges in columnar format on each partition for performance.")[ED] extends [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[[Edge](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html "org.apache.spark.graphx.Edge")[ED]]
`EdgeRDD[ED, VD]` extends `RDD[Edge[ED]]` by storing the edges in columnar format on each partition for performance.
`EdgeRDD[ED, VD]` extends `RDD[Edge[ED]]` by storing the edges in columnar format on each partition for performance. It may additionally store the vertex attributes associated with each edge to provide the triplet view. Shipping of the vertex attributes is managed by `impl.ReplicatedVertexView`. 
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/EdgeTriplet.html "Permalink") class [EdgeTriplet](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/EdgeTriplet.html "An edge triplet represents an edge along with the vertex attributes of its neighboring vertices.")[VD, ED] extends [Edge](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html "org.apache.spark.graphx.Edge")[ED]
An edge triplet represents an edge along with the vertex attributes of its neighboring vertices.
An edge triplet represents an edge along with the vertex attributes of its neighboring vertices.  

VD
    
the type of the vertex attribute. 

ED
    
the type of the edge attribute
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "Permalink") abstract  class [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "The Graph abstractly represents a graph with arbitrary objects associated with vertices and edges.")[VD, ED] extends Serializable
The Graph abstractly represents a graph with arbitrary objects associated with vertices and edges.
The Graph abstractly represents a graph with arbitrary objects associated with vertices and edges. The graph provides basic operations to access and manipulate the data associated with vertices and edges as well as the underlying structure. Like Spark RDDs, the graph is a functional data-structure in which mutating operations return new graphs.  

VD
    
the vertex attribute type 

ED
    
the edge attribute type 

Note
    
[GraphOps](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html "org.apache.spark.graphx.GraphOps") contains additional convenience operations and graph algorithms.
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html "Permalink") class [GraphOps](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html "Contains additional functionality for Graph.")[VD, ED] extends Serializable
Contains additional functionality for [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph").
Contains additional functionality for [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph"). All operations are expressed in terms of the efficient GraphX API. This class is implicitly constructed for each Graph object.  

VD
    
the vertex attribute type 

ED
    
the edge attribute type
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#PartitionID=Int "Permalink") type PartitionID = Int
Integer identifier of a graph partition.
Integer identifier of a graph partition. Must be less than 2^30.
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/PartitionStrategy.html "Permalink") trait [PartitionStrategy](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/PartitionStrategy.html "Represents the way edges are assigned to edge partitions based on their source and destination vertex IDs.") extends Serializable
Represents the way edges are assigned to edge partitions based on their source and destination vertex IDs.
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/TripletFields.html "Permalink") class [TripletFields](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/TripletFields.html "Represents a subset of the fields of an EdgeTriplet or EdgeContext.") extends [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable")
Represents a subset of the fields of an [EdgeTriplet](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/EdgeTriplet.html "org.apache.spark.graphx.EdgeTriplet") or [EdgeContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/EdgeContext.html "org.apache.spark.graphx.EdgeContext").
Represents a subset of the fields of an [EdgeTriplet](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/EdgeTriplet.html "org.apache.spark.graphx.EdgeTriplet") or [EdgeContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/EdgeContext.html "org.apache.spark.graphx.EdgeContext"). This allows the system to populate only those fields for efficiency. 
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long "Permalink") type VertexId = Long
A 64-bit vertex identifier that uniquely identifies a vertex within a graph.
A 64-bit vertex identifier that uniquely identifies a vertex within a graph. It does not need to follow any ordering or any constraints other than uniqueness. 
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "Permalink") abstract  class [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "Extends RDD\[\(VertexId, VD\)\] by ensuring that there is only one entry for each vertex and by pre-indexing the entries for fast, efficient joins.")[VD] extends [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]
Extends `RDD[(VertexId, VD)]` by ensuring that there is only one entry for each vertex and by pre-indexing the entries for fast, efficient joins.
Extends `RDD[(VertexId, VD)]` by ensuring that there is only one entry for each vertex and by pre-indexing the entries for fast, efficient joins. Two VertexRDDs with the same index can be joined efficiently. All operations except [reindex](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#reindex\(\):org.apache.spark.graphx.VertexRDD\[VD\]) preserve the index. To construct a `VertexRDD`, use the [VertexRDD object](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD$.html "org.apache.spark.graphx.VertexRDD").
Additionally, stores routing information to enable joining the vertex attributes with an [EdgeRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/EdgeRDD.html "org.apache.spark.graphx.EdgeRDD").  

VD
    
the vertex attribute associated with each vertex in the set.
Example:
    1. Construct a `VertexRDD` from a plain RDD:

```
// Construct an initial vertex set
val someData: RDD[(VertexId, SomeType)] = loadData(someFile)
val vset = VertexRDD(someData)
// If there were redundant values in someData we would use a reduceFunc
val vset2 = VertexRDD(someData, reduceFunc)
// Finally we can use the VertexRDD to index another dataset
val otherData: RDD[(VertexId, OtherType)] = loadData(otherFile)
val vset3 = vset2.innerJoin(otherData) { (vid, a, b) => b }
// Now we can construct very fast joins between the two sets
val vset4: VertexRDD[(SomeType, OtherType)] = vset.leftJoin(vset3)
```



### Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge$.html "Permalink") object [Edge](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge$.html) extends [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable")
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/EdgeContext$.html "Permalink") object [EdgeContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/EdgeContext$.html)
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/EdgeDirection$.html "Permalink") object [EdgeDirection](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/EdgeDirection$.html "A set of EdgeDirections.") extends [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable")
A set of [EdgeDirection](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/EdgeDirection.html "org.apache.spark.graphx.EdgeDirection")s.
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/EdgeRDD$.html "Permalink") object [EdgeRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/EdgeRDD$.html) extends [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable")
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph$.html "Permalink") object [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph$.html "The Graph object contains a collection of routines used to construct graphs from RDDs.") extends [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable")
The Graph object contains a collection of routines used to construct graphs from RDDs.
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphLoader$.html "Permalink") object [GraphLoader](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphLoader$.html "Provides utilities for loading Graphs from files.") extends Logging
Provides utilities for loading [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")s from files.
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphXUtils$.html "Permalink") object [GraphXUtils](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphXUtils$.html)
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/PartitionStrategy$.html "Permalink") object [PartitionStrategy](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/PartitionStrategy$.html "Collection of built-in PartitionStrategy implementations.") extends [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable")
Collection of built-in [PartitionStrategy](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/PartitionStrategy.html "org.apache.spark.graphx.PartitionStrategy") implementations.
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Pregel$.html "Permalink") object [Pregel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Pregel$.html "Implements a Pregel-like bulk-synchronous message-passing API.") extends Logging
Implements a Pregel-like bulk-synchronous message-passing API.
Implements a Pregel-like bulk-synchronous message-passing API.
Unlike the original Pregel API, the GraphX Pregel API factors the sendMessage computation over edges, enables the message sending computation to read both vertex attributes, and constrains messages to the graph structure. These changes allow for substantially more efficient distributed execution while also exposing greater flexibility for graph-based computation. 
Example:
    1. We can use the Pregel abstraction to implement PageRank:

```
val pagerankGraph: Graph[Double, Double] = graph
  // Associate the degree with each vertex
  .outerJoinVertices(graph.outDegrees) {
    (vid, vdata, deg) => deg.getOrElse(0)
  }
  // Set the weight on the edges based on the degree
  .mapTriplets(e => 1.0 / e.srcAttr)
  // Set the vertex attributes to the initial pagerank values
  .mapVertices((id, attr) => 1.0)

def vertexProgram(id: VertexId, attr: Double, msgSum: Double): Double =
  resetProb + (1.0 - resetProb) * msgSum
def sendMessage(id: VertexId, edge: EdgeTriplet[Double, Double]): Iterator[(VertexId, Double)] =
  Iterator((edge.dstId, edge.srcAttr * edge.attr))
def messageCombiner(a: Double, b: Double): Double = a + b
val initialMessage = 0.0
// Execute Pregel for a fixed number of iterations.
Pregel(pagerankGraph, initialMessage, numIter)(
  vertexProgram, sendMessage, messageCombiner)
```

  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD$.html "Permalink") object [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD$.html "The VertexRDD singleton is used to construct VertexRDDs.") extends [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable")
The VertexRDD singleton is used to construct VertexRDDs.


### Ungrouped
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html "Permalink") case class [Edge](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html "A single directed edge consisting of a source id, target id, and the data associated with the edge.")[ED](srcId: [VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long) = 0, dstId: [VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long) = 0, attr: ED = null.asInstanceOf[ED]) extends Serializable with Product
A single directed edge consisting of a source id, target id, and the data associated with the edge.
A single directed edge consisting of a source id, target id, and the data associated with the edge.  

ED
    
type of the edge attribute 

srcId
    
The vertex id of the source vertex 

dstId
    
The vertex id of the target vertex 

attr
    
The attribute associated with the edge
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/EdgeContext.html "Permalink") abstract  class [EdgeContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/EdgeContext.html "Represents an edge along with its neighboring vertices and allows sending messages along the edge.")[VD, ED, A] extends AnyRef
Represents an edge along with its neighboring vertices and allows sending messages along the edge.
Represents an edge along with its neighboring vertices and allows sending messages along the edge. Used in [Graph#aggregateMessages](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html#aggregateMessages\[A\]\(sendMsg:org.apache.spark.graphx.EdgeContext\[VD,ED,A\]=>Unit,mergeMsg:\(A,A\)=>A,tripletFields:org.apache.spark.graphx.TripletFields\)\(implicitevidence$11:scala.reflect.ClassTag\[A\]\):org.apache.spark.graphx.VertexRDD\[A\]). 
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/EdgeDirection.html "Permalink") class [EdgeDirection](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/EdgeDirection.html "The direction of a directed edge relative to a vertex.") extends Serializable
The direction of a directed edge relative to a vertex.
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/EdgeRDD.html "Permalink") abstract  class [EdgeRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/EdgeRDD.html "EdgeRDD\[ED, VD\] extends RDD\[Edge\[ED\]\] by storing the edges in columnar format on each partition for performance.")[ED] extends [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[[Edge](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html "org.apache.spark.graphx.Edge")[ED]]
`EdgeRDD[ED, VD]` extends `RDD[Edge[ED]]` by storing the edges in columnar format on each partition for performance.
`EdgeRDD[ED, VD]` extends `RDD[Edge[ED]]` by storing the edges in columnar format on each partition for performance. It may additionally store the vertex attributes associated with each edge to provide the triplet view. Shipping of the vertex attributes is managed by `impl.ReplicatedVertexView`. 
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/EdgeTriplet.html "Permalink") class [EdgeTriplet](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/EdgeTriplet.html "An edge triplet represents an edge along with the vertex attributes of its neighboring vertices.")[VD, ED] extends [Edge](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html "org.apache.spark.graphx.Edge")[ED]
An edge triplet represents an edge along with the vertex attributes of its neighboring vertices.
An edge triplet represents an edge along with the vertex attributes of its neighboring vertices.  

VD
    
the type of the vertex attribute. 

ED
    
the type of the edge attribute
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "Permalink") abstract  class [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "The Graph abstractly represents a graph with arbitrary objects associated with vertices and edges.")[VD, ED] extends Serializable
The Graph abstractly represents a graph with arbitrary objects associated with vertices and edges.
The Graph abstractly represents a graph with arbitrary objects associated with vertices and edges. The graph provides basic operations to access and manipulate the data associated with vertices and edges as well as the underlying structure. Like Spark RDDs, the graph is a functional data-structure in which mutating operations return new graphs.  

VD
    
the vertex attribute type 

ED
    
the edge attribute type 

Note
    
[GraphOps](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html "org.apache.spark.graphx.GraphOps") contains additional convenience operations and graph algorithms.
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html "Permalink") class [GraphOps](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html "Contains additional functionality for Graph.")[VD, ED] extends Serializable
Contains additional functionality for [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph").
Contains additional functionality for [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph"). All operations are expressed in terms of the efficient GraphX API. This class is implicitly constructed for each Graph object.  

VD
    
the vertex attribute type 

ED
    
the edge attribute type
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#PartitionID=Int "Permalink") type PartitionID = Int
Integer identifier of a graph partition.
Integer identifier of a graph partition. Must be less than 2^30.
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/PartitionStrategy.html "Permalink") trait [PartitionStrategy](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/PartitionStrategy.html "Represents the way edges are assigned to edge partitions based on their source and destination vertex IDs.") extends Serializable
Represents the way edges are assigned to edge partitions based on their source and destination vertex IDs.
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/TripletFields.html "Permalink") class [TripletFields](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/TripletFields.html "Represents a subset of the fields of an EdgeTriplet or EdgeContext.") extends [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable")
Represents a subset of the fields of an [EdgeTriplet](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/EdgeTriplet.html "org.apache.spark.graphx.EdgeTriplet") or [EdgeContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/EdgeContext.html "org.apache.spark.graphx.EdgeContext").
Represents a subset of the fields of an [EdgeTriplet](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/EdgeTriplet.html "org.apache.spark.graphx.EdgeTriplet") or [EdgeContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/EdgeContext.html "org.apache.spark.graphx.EdgeContext"). This allows the system to populate only those fields for efficiency. 
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long "Permalink") type VertexId = Long
A 64-bit vertex identifier that uniquely identifies a vertex within a graph.
A 64-bit vertex identifier that uniquely identifies a vertex within a graph. It does not need to follow any ordering or any constraints other than uniqueness. 
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "Permalink") abstract  class [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "Extends RDD\[\(VertexId, VD\)\] by ensuring that there is only one entry for each vertex and by pre-indexing the entries for fast, efficient joins.")[VD] extends [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]
Extends `RDD[(VertexId, VD)]` by ensuring that there is only one entry for each vertex and by pre-indexing the entries for fast, efficient joins.
Extends `RDD[(VertexId, VD)]` by ensuring that there is only one entry for each vertex and by pre-indexing the entries for fast, efficient joins. Two VertexRDDs with the same index can be joined efficiently. All operations except [reindex](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#reindex\(\):org.apache.spark.graphx.VertexRDD\[VD\]) preserve the index. To construct a `VertexRDD`, use the [VertexRDD object](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD$.html "org.apache.spark.graphx.VertexRDD").
Additionally, stores routing information to enable joining the vertex attributes with an [EdgeRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/EdgeRDD.html "org.apache.spark.graphx.EdgeRDD").  

VD
    
the vertex attribute associated with each vertex in the set.
Example:
    1. Construct a `VertexRDD` from a plain RDD:

```
// Construct an initial vertex set
val someData: RDD[(VertexId, SomeType)] = loadData(someFile)
val vset = VertexRDD(someData)
// If there were redundant values in someData we would use a reduceFunc
val vset2 = VertexRDD(someData, reduceFunc)
// Finally we can use the VertexRDD to index another dataset
val otherData: RDD[(VertexId, OtherType)] = loadData(otherFile)
val vset3 = vset2.innerJoin(otherData) { (vid, a, b) => b }
// Now we can construct very fast joins between the two sets
val vset4: VertexRDD[(SomeType, OtherType)] = vset.leftJoin(vset3)
```



  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge$.html "Permalink") object [Edge](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge$.html) extends [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable")
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/EdgeContext$.html "Permalink") object [EdgeContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/EdgeContext$.html)
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/EdgeDirection$.html "Permalink") object [EdgeDirection](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/EdgeDirection$.html "A set of EdgeDirections.") extends [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable")
A set of [EdgeDirection](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/EdgeDirection.html "org.apache.spark.graphx.EdgeDirection")s.
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/EdgeRDD$.html "Permalink") object [EdgeRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/EdgeRDD$.html) extends [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable")
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph$.html "Permalink") object [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph$.html "The Graph object contains a collection of routines used to construct graphs from RDDs.") extends [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable")
The Graph object contains a collection of routines used to construct graphs from RDDs.
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphLoader$.html "Permalink") object [GraphLoader](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphLoader$.html "Provides utilities for loading Graphs from files.") extends Logging
Provides utilities for loading [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")s from files.
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphXUtils$.html "Permalink") object [GraphXUtils](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphXUtils$.html)
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/PartitionStrategy$.html "Permalink") object [PartitionStrategy](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/PartitionStrategy$.html "Collection of built-in PartitionStrategy implementations.") extends [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable")
Collection of built-in [PartitionStrategy](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/PartitionStrategy.html "org.apache.spark.graphx.PartitionStrategy") implementations.
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Pregel$.html "Permalink") object [Pregel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Pregel$.html "Implements a Pregel-like bulk-synchronous message-passing API.") extends Logging
Implements a Pregel-like bulk-synchronous message-passing API.
Implements a Pregel-like bulk-synchronous message-passing API.
Unlike the original Pregel API, the GraphX Pregel API factors the sendMessage computation over edges, enables the message sending computation to read both vertex attributes, and constrains messages to the graph structure. These changes allow for substantially more efficient distributed execution while also exposing greater flexibility for graph-based computation. 
Example:
    1. We can use the Pregel abstraction to implement PageRank:

```
val pagerankGraph: Graph[Double, Double] = graph
  // Associate the degree with each vertex
  .outerJoinVertices(graph.outDegrees) {
    (vid, vdata, deg) => deg.getOrElse(0)
  }
  // Set the weight on the edges based on the degree
  .mapTriplets(e => 1.0 / e.srcAttr)
  // Set the vertex attributes to the initial pagerank values
  .mapVertices((id, attr) => 1.0)

def vertexProgram(id: VertexId, attr: Double, msgSum: Double): Double =
  resetProb + (1.0 - resetProb) * msgSum
def sendMessage(id: VertexId, edge: EdgeTriplet[Double, Double]): Iterator[(VertexId, Double)] =
  Iterator((edge.dstId, edge.srcAttr * edge.attr))
def messageCombiner(a: Double, b: Double): Double = a + b
val initialMessage = 0.0
// Execute Pregel for a fixed number of iterations.
Pregel(pagerankGraph, initialMessage, numIter)(
  vertexProgram, sendMessage, messageCombiner)
```

  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD$.html "Permalink") object [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD$.html "The VertexRDD singleton is used to construct VertexRDDs.") extends [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable")
The VertexRDD singleton is used to construct VertexRDDs.


