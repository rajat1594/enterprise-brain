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
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html "Permalink") package [graphx](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html "ALPHA COMPONENT GraphX is a graph processing framework built on top of Spark.")
ALPHA COMPONENT GraphX is a graph processing framework built on top of Spark.
ALPHA COMPONENT GraphX is a graph processing framework built on top of Spark.  

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/impl/index.html "Permalink") package [impl](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/impl/index.html) 

Definition Classes
    [graphx](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html "org.apache.spark.graphx")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/index.html "Permalink") package [lib](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/index.html "Various analytics functions for graphs.")
Various analytics functions for graphs.
Various analytics functions for graphs.  

Definition Classes
    [graphx](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html "org.apache.spark.graphx")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/util/index.html "Permalink") package [util](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/util/index.html "Collections of utilities used by graphx.")
Collections of utilities used by graphx.
Collections of utilities used by graphx.  

Definition Classes
    [graphx](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html "org.apache.spark.graphx")
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


[c](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD$.html "See companion object")
[org](https://spark.apache.org/docs/latest/api/scala/org/index.html "org").[apache](https://spark.apache.org/docs/latest/api/scala/org/apache/index.html "org.apache").[spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark").[graphx](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html "org.apache.spark.graphx")
#  [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD$.html "See companion object")[ __](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "Permalink")
### 
Companion [object VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD$.html "See companion object")
####  abstract  class VertexRDD[VD] extends [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]
Extends `RDD[(VertexId, VD)]` by ensuring that there is only one entry for each vertex and by pre-indexing the entries for fast, efficient joins. Two VertexRDDs with the same index can be joined efficiently. All operations except [reindex](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#reindex\(\):org.apache.spark.graphx.VertexRDD\[VD\]) preserve the index. To construct a `VertexRDD`, use the [VertexRDD object](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD$.html "org.apache.spark.graphx.VertexRDD").
Additionally, stores routing information to enable joining the vertex attributes with an [EdgeRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/EdgeRDD.html "org.apache.spark.graphx.EdgeRDD").  

VD
    
the vertex attribute associated with each vertex in the set. 

Source
    [VertexRDD.scala](https://github.com/apache/spark/tree/v4.1.2/graphx/src/main/scala/org/apache/spark/graphx/VertexRDD.scala)
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



Linear Supertypes
[RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)], Logging, [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable"), AnyRef, Any
Known Subclasses
[VertexRDDImpl](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/impl/VertexRDDImpl.html "org.apache.spark.graphx.impl.VertexRDDImpl")
__ __
Ordering
  1. Alphabetic
  2. By Inheritance


Inherited  

  1. VertexRDD
  2. RDD
  3. Logging
  4. Serializable
  5. AnyRef
  6. Any


  1. Hide All
  2. Show All


Visibility
  1. Public
  2. Protected


### Instance Constructors
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#<init>\(sc:org.apache.spark.SparkContext,deps:Seq\[org.apache.spark.Dependency\[_\]\]\):org.apache.spark.graphx.VertexRDD\[VD\] "Permalink") new VertexRDD(sc: [SparkContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html "org.apache.spark.SparkContext"), deps: Seq[[Dependency](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Dependency.html "org.apache.spark.Dependency")[_]])


### Type Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#LogStringContextextendsAnyRef "Permalink") implicit  class LogStringContext extends AnyRef 

Definition Classes
    Logging


### Abstract Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#aggregateUsingIndex\[VD2\]\(messages:org.apache.spark.rdd.RDD\[\(org.apache.spark.graphx.VertexId,VD2\)\],reduceFunc:\(VD2,VD2\)=>VD2\)\(implicitevidence$12:scala.reflect.ClassTag\[VD2\]\):org.apache.spark.graphx.VertexRDD\[VD2\] "Permalink") abstract  def aggregateUsingIndex[VD2](messages: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD2)], reduceFunc: (VD2, VD2) => VD2)(implicit arg0: ClassTag[VD2]): [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "org.apache.spark.graphx.VertexRDD")[VD2]
Aggregates vertices in `messages` that have the same ids using `reduceFunc`, returning a VertexRDD co-indexed with `this`.
Aggregates vertices in `messages` that have the same ids using `reduceFunc`, returning a VertexRDD co-indexed with `this`.  

messages
    
an RDD containing messages to aggregate, where each message is a pair of its target vertex ID and the message data 

reduceFunc
    
the associative aggregation function for merging messages to the same vertex 

returns
    
a VertexRDD co-indexed with `this`, containing only vertices that received messages. For those vertices, their values are the result of applying `reduceFunc` to all received messages.
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#diff\(other:org.apache.spark.graphx.VertexRDD\[VD\]\):org.apache.spark.graphx.VertexRDD\[VD\] "Permalink") abstract  def diff(other: [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "org.apache.spark.graphx.VertexRDD")[VD]): [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "org.apache.spark.graphx.VertexRDD")[VD]
For each vertex present in both `this` and `other`, `diff` returns only those vertices with differing values; for values that are different, keeps the values from `other`.
For each vertex present in both `this` and `other`, `diff` returns only those vertices with differing values; for values that are different, keeps the values from `other`. This is only guaranteed to work if the VertexRDDs share a common ancestor.  

other
    
the other VertexRDD with which to diff against.
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#diff\(other:org.apache.spark.rdd.RDD\[\(org.apache.spark.graphx.VertexId,VD\)\]\):org.apache.spark.graphx.VertexRDD\[VD\] "Permalink") abstract  def diff(other: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]): [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "org.apache.spark.graphx.VertexRDD")[VD]
For each vertex present in both `this` and `other`, `diff` returns only those vertices with differing values; for values that are different, keeps the values from `other`.
For each vertex present in both `this` and `other`, `diff` returns only those vertices with differing values; for values that are different, keeps the values from `other`. This is only guaranteed to work if the VertexRDDs share a common ancestor.  

other
    
the other RDD[(VertexId, VD)] with which to diff against.
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#innerJoin\[U,VD2\]\(other:org.apache.spark.rdd.RDD\[\(org.apache.spark.graphx.VertexId,U\)\]\)\(f:\(org.apache.spark.graphx.VertexId,VD,U\)=>VD2\)\(implicitevidence$10:scala.reflect.ClassTag\[U\],implicitevidence$11:scala.reflect.ClassTag\[VD2\]\):org.apache.spark.graphx.VertexRDD\[VD2\] "Permalink") abstract  def innerJoin[U, VD2](other: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), U)])(f: ([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD, U) => VD2)(implicit arg0: ClassTag[U], arg1: ClassTag[VD2]): [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "org.apache.spark.graphx.VertexRDD")[VD2]
Inner joins this VertexRDD with an RDD containing vertex attribute pairs.
Inner joins this VertexRDD with an RDD containing vertex attribute pairs. If the other RDD is backed by a VertexRDD with the same index then the efficient [innerZipJoin](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#innerZipJoin\[U,VD2\]\(other:org.apache.spark.graphx.VertexRDD\[U\]\)\(f:\(org.apache.spark.graphx.VertexId,VD,U\)=>VD2\)\(implicitevidence$8:scala.reflect.ClassTag\[U\],implicitevidence$9:scala.reflect.ClassTag\[VD2\]\):org.apache.spark.graphx.VertexRDD\[VD2\]) implementation is used.  

other
    
an RDD containing vertices to join. If there are multiple entries for the same vertex, one is picked arbitrarily. Use [aggregateUsingIndex](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#aggregateUsingIndex\[VD2\]\(messages:org.apache.spark.rdd.RDD\[\(org.apache.spark.graphx.VertexId,VD2\)\],reduceFunc:\(VD2,VD2\)=>VD2\)\(implicitevidence$12:scala.reflect.ClassTag\[VD2\]\):org.apache.spark.graphx.VertexRDD\[VD2\]) to merge multiple entries. 

f
    
the join function applied to corresponding values of `this` and `other` 

returns
    
a VertexRDD co-indexed with `this`, containing only vertices that appear in both `this` and `other`, with values supplied by `f`
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#innerZipJoin\[U,VD2\]\(other:org.apache.spark.graphx.VertexRDD\[U\]\)\(f:\(org.apache.spark.graphx.VertexId,VD,U\)=>VD2\)\(implicitevidence$8:scala.reflect.ClassTag\[U\],implicitevidence$9:scala.reflect.ClassTag\[VD2\]\):org.apache.spark.graphx.VertexRDD\[VD2\] "Permalink") abstract  def innerZipJoin[U, VD2](other: [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "org.apache.spark.graphx.VertexRDD")[U])(f: ([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD, U) => VD2)(implicit arg0: ClassTag[U], arg1: ClassTag[VD2]): [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "org.apache.spark.graphx.VertexRDD")[VD2]
Efficiently inner joins this VertexRDD with another VertexRDD sharing the same index.
Efficiently inner joins this VertexRDD with another VertexRDD sharing the same index. See [innerJoin](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#innerJoin\[U,VD2\]\(other:org.apache.spark.rdd.RDD\[\(org.apache.spark.graphx.VertexId,U\)\]\)\(f:\(org.apache.spark.graphx.VertexId,VD,U\)=>VD2\)\(implicitevidence$10:scala.reflect.ClassTag\[U\],implicitevidence$11:scala.reflect.ClassTag\[VD2\]\):org.apache.spark.graphx.VertexRDD\[VD2\]) for the behavior of the join. 
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#leftJoin\[VD2,VD3\]\(other:org.apache.spark.rdd.RDD\[\(org.apache.spark.graphx.VertexId,VD2\)\]\)\(f:\(org.apache.spark.graphx.VertexId,VD,Option\[VD2\]\)=>VD3\)\(implicitevidence$6:scala.reflect.ClassTag\[VD2\],implicitevidence$7:scala.reflect.ClassTag\[VD3\]\):org.apache.spark.graphx.VertexRDD\[VD3\] "Permalink") abstract  def leftJoin[VD2, VD3](other: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD2)])(f: ([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD, Option[VD2]) => VD3)(implicit arg0: ClassTag[VD2], arg1: ClassTag[VD3]): [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "org.apache.spark.graphx.VertexRDD")[VD3]
Left joins this VertexRDD with an RDD containing vertex attribute pairs.
Left joins this VertexRDD with an RDD containing vertex attribute pairs. If the other RDD is backed by a VertexRDD with the same index then the efficient [leftZipJoin](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#leftZipJoin\[VD2,VD3\]\(other:org.apache.spark.graphx.VertexRDD\[VD2\]\)\(f:\(org.apache.spark.graphx.VertexId,VD,Option\[VD2\]\)=>VD3\)\(implicitevidence$4:scala.reflect.ClassTag\[VD2\],implicitevidence$5:scala.reflect.ClassTag\[VD3\]\):org.apache.spark.graphx.VertexRDD\[VD3\]) implementation is used. The resulting VertexRDD contains an entry for each vertex in `this`. If `other` is missing any vertex in this VertexRDD, `f` is passed `None`. If there are duplicates, the vertex is picked arbitrarily.  

VD2
    
the attribute type of the other VertexRDD 

VD3
    
the attribute type of the resulting VertexRDD 

other
    
the other VertexRDD with which to join 

f
    
the function mapping a vertex id and its attributes in this and the other vertex set to a new vertex attribute. 

returns
    
a VertexRDD containing all the vertices in this VertexRDD with the attributes emitted by `f`.
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#leftZipJoin\[VD2,VD3\]\(other:org.apache.spark.graphx.VertexRDD\[VD2\]\)\(f:\(org.apache.spark.graphx.VertexId,VD,Option\[VD2\]\)=>VD3\)\(implicitevidence$4:scala.reflect.ClassTag\[VD2\],implicitevidence$5:scala.reflect.ClassTag\[VD3\]\):org.apache.spark.graphx.VertexRDD\[VD3\] "Permalink") abstract  def leftZipJoin[VD2, VD3](other: [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "org.apache.spark.graphx.VertexRDD")[VD2])(f: ([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD, Option[VD2]) => VD3)(implicit arg0: ClassTag[VD2], arg1: ClassTag[VD3]): [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "org.apache.spark.graphx.VertexRDD")[VD3]
Left joins this RDD with another VertexRDD with the same index.
Left joins this RDD with another VertexRDD with the same index. This function will fail if both VertexRDDs do not share the same index. The resulting vertex set contains an entry for each vertex in `this`. If `other` is missing any vertex in this VertexRDD, `f` is passed `None`.  

VD2
    
the attribute type of the other VertexRDD 

VD3
    
the attribute type of the resulting VertexRDD 

other
    
the other VertexRDD with which to join. 

f
    
the function mapping a vertex id and its attributes in this and the other vertex set to a new vertex attribute. 

returns
    
a VertexRDD containing the results of `f`
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#mapValues\[VD2\]\(f:\(org.apache.spark.graphx.VertexId,VD\)=>VD2\)\(implicitevidence$3:scala.reflect.ClassTag\[VD2\]\):org.apache.spark.graphx.VertexRDD\[VD2\] "Permalink") abstract  def mapValues[VD2](f: ([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD) => VD2)(implicit arg0: ClassTag[VD2]): [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "org.apache.spark.graphx.VertexRDD")[VD2]
Maps each vertex attribute, additionally supplying the vertex ID.
Maps each vertex attribute, additionally supplying the vertex ID.  

VD2
    
the type returned by the map function 

f
    
the function applied to each ID-value pair in the RDD 

returns
    
a new VertexRDD with values obtained by applying `f` to each of the entries in the original VertexRDD. The resulting VertexRDD retains the same index.
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#mapValues\[VD2\]\(f:VD=>VD2\)\(implicitevidence$2:scala.reflect.ClassTag\[VD2\]\):org.apache.spark.graphx.VertexRDD\[VD2\] "Permalink") abstract  def mapValues[VD2](f: (VD) => VD2)(implicit arg0: ClassTag[VD2]): [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "org.apache.spark.graphx.VertexRDD")[VD2]
Maps each vertex attribute, preserving the index.
Maps each vertex attribute, preserving the index.  

VD2
    
the type returned by the map function 

f
    
the function applied to each value in the RDD 

returns
    
a new VertexRDD with values obtained by applying `f` to each of the entries in the original VertexRDD
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#minus\(other:org.apache.spark.graphx.VertexRDD\[VD\]\):org.apache.spark.graphx.VertexRDD\[VD\] "Permalink") abstract  def minus(other: [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "org.apache.spark.graphx.VertexRDD")[VD]): [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "org.apache.spark.graphx.VertexRDD")[VD]
For each VertexId present in both `this` and `other`, minus will act as a set difference operation returning only those unique VertexId's present in `this`.
For each VertexId present in both `this` and `other`, minus will act as a set difference operation returning only those unique VertexId's present in `this`.  

other
    
a VertexRDD to run the set operation against
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#minus\(other:org.apache.spark.rdd.RDD\[\(org.apache.spark.graphx.VertexId,VD\)\]\):org.apache.spark.graphx.VertexRDD\[VD\] "Permalink") abstract  def minus(other: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]): [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "org.apache.spark.graphx.VertexRDD")[VD]
For each VertexId present in both `this` and `other`, minus will act as a set difference operation returning only those unique VertexId's present in `this`.
For each VertexId present in both `this` and `other`, minus will act as a set difference operation returning only those unique VertexId's present in `this`.  

other
    
an RDD to run the set operation against
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#reindex\(\):org.apache.spark.graphx.VertexRDD\[VD\] "Permalink") abstract  def reindex(): [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "org.apache.spark.graphx.VertexRDD")[VD]
Construct a new VertexRDD that is indexed by only the visible vertices.
Construct a new VertexRDD that is indexed by only the visible vertices. The resulting VertexRDD will be based on a different index and can no longer be quickly joined with this RDD. 
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#reverseRoutingTables\(\):org.apache.spark.graphx.VertexRDD\[VD\] "Permalink") abstract  def reverseRoutingTables(): [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "org.apache.spark.graphx.VertexRDD")[VD]
Returns a new `VertexRDD` reflecting a reversal of all edge directions in the corresponding [EdgeRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/EdgeRDD.html "org.apache.spark.graphx.EdgeRDD").
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#vdTag:scala.reflect.ClassTag\[VD\] "Permalink") implicit abstract  def vdTag: ClassTag[VD] 

Attributes
    protected 
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#withEdges\(edges:org.apache.spark.graphx.EdgeRDD\[_\]\):org.apache.spark.graphx.VertexRDD\[VD\] "Permalink") abstract  def withEdges(edges: [EdgeRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/EdgeRDD.html "org.apache.spark.graphx.EdgeRDD")[_]): [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "org.apache.spark.graphx.VertexRDD")[VD]
Prepares this VertexRDD for efficient joins with the given EdgeRDD.


### Concrete Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html###:Int "Permalink") final  def ##: Int 

Definition Classes
    AnyRef → Any
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#++\(other:org.apache.spark.rdd.RDD\[T\]\):org.apache.spark.rdd.RDD\[T\] "Permalink") def ++(other: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]
Return the union of this RDD and another one.
Return the union of this RDD and another one. Any identical elements will appear multiple times (use `.distinct()` to eliminate them).  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#MDC\(key:org.apache.spark.internal.LogKey,value:Any\):org.apache.spark.internal.MDC "Permalink") def MDC(key: LogKey, value: Any): MDC 

Attributes
    protected  

Definition Classes
    Logging
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#aggregate\[U\]\(zeroValue:U\)\(seqOp:\(U,T\)=>U,combOp:\(U,U\)=>U\)\(implicitevidence$33:scala.reflect.ClassTag\[U\]\):U "Permalink") def aggregate[U](zeroValue: U)(seqOp: (U, ([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)) => U, combOp: (U, U) => U)(implicit arg0: ClassTag[U]): U
Aggregate the elements of each partition, and then the results for all the partitions, using given combine functions and a neutral "zero value".
Aggregate the elements of each partition, and then the results for all the partitions, using given combine functions and a neutral "zero value". This function can return a different result type, U, than the type of this RDD, T. Thus, we need one operation for merging a T into an U and one operation for merging two U's, as in scala.IterableOnce. Both of these functions are allowed to modify and return their first argument instead of creating a new U to avoid memory allocation.  

zeroValue
    
the initial value for the accumulated result of each partition for the `seqOp` operator, and also the initial value for the combine results from different partitions for the `combOp` operator - this will typically be the neutral element (e.g. `Nil` for list concatenation or `0` for summation) 

seqOp
    
an operator used to accumulate results within a partition 

combOp
    
an associative operator used to combine results from different partitions 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0 

Definition Classes
    Any
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#barrier\(\):org.apache.spark.rdd.RDDBarrier\[T\] "Permalink") def barrier(): [RDDBarrier](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDDBarrier.html "org.apache.spark.rdd.RDDBarrier")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]
Marks the current stage as a barrier stage, where Spark must launch all tasks together.
Marks the current stage as a barrier stage, where Spark must launch all tasks together. In case of a task failure, instead of only restarting the failed task, Spark will abort the entire stage and re-launch all tasks for this stage. The barrier execution mode feature is experimental and it only handles limited scenarios. Please read the linked SPIP and design docs to understand the limitations and future plans. 

returns
    
an RDDBarrier instance that provides actions within a barrier stage 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Annotations
     @Experimental() @Since("2.4.0") 

See also
    
[org.apache.spark.BarrierTaskContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/BarrierTaskContext.html "org.apache.spark.BarrierTaskContext")
[ SPIP: Barrier Execution Mode](https://issues.apache.org/jira/browse/SPARK-24374)
[Design Doc](https://issues.apache.org/jira/browse/SPARK-24582)
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#cache\(\):RDD.this.type "Permalink") def cache(): [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "org.apache.spark.graphx.VertexRDD").this.type
Persist this RDD with the default storage level (`MEMORY_ONLY`).
Persist this RDD with the default storage level (`MEMORY_ONLY`).  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#cartesian\[U\]\(other:org.apache.spark.rdd.RDD\[U\]\)\(implicitevidence$5:scala.reflect.ClassTag\[U\]\):org.apache.spark.rdd.RDD\[\(T,U\)\] "Permalink") def cartesian[U](other: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[U])(implicit arg0: ClassTag[U]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD), U)]
Return the Cartesian product of this RDD and another one, that is, the RDD of all pairs of elements (a, b) where a is in `this` and b is in `other`.
Return the Cartesian product of this RDD and another one, that is, the RDD of all pairs of elements (a, b) where a is in `this` and b is in `other`.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#checkpoint\(\):Unit "Permalink") def checkpoint(): Unit
Mark this RDD for checkpointing.
Mark this RDD for checkpointing. It will be saved to a file inside the checkpoint directory set with `SparkContext#setCheckpointDir` and all references to its parent RDDs will be removed. This function must be called before any job has been executed on this RDD. It is strongly recommended that this RDD is persisted in memory, otherwise saving it on a file will require recomputation.
The data is only checkpointed when `doCheckpoint()` is called, and this only happens at the end of the first action execution on this RDD. The final data that is checkpointed after the first action may be different from the data that was used during the action, due to non-determinism of the underlying operation and retries. If the purpose of the checkpoint is to achieve saving a deterministic snapshot of the data, an eager action may need to be called first on the RDD to trigger the checkpoint.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#cleanShuffleDependencies\(blocking:Boolean\):Unit "Permalink") def cleanShuffleDependencies(blocking: Boolean = false): Unit
Removes an RDD's shuffles and it's non-persisted ancestors.
Removes an RDD's shuffles and it's non-persisted ancestors. When running without a shuffle service, cleaning up shuffle files enables downscaling. If you use the RDD after this call, you should checkpoint and materialize it first. If you are uncertain of what you are doing, please do not use this feature. Additional techniques for mitigating orphaned shuffle files: * Tuning the driver GC to be more aggressive, so the regular context cleaner is triggered * Setting an appropriate TTL for shuffle files to be auto cleaned  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Annotations
     @DeveloperApi() @Since("3.1.0")
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#clearDependencies\(\):Unit "Permalink") def clearDependencies(): Unit
Clears the dependencies of this RDD.
Clears the dependencies of this RDD. This method must ensure that all references to the original parent RDDs are removed to enable the parent RDDs to be garbage collected. Subclasses of RDD may override this method for implementing their own cleaning logic. See [org.apache.spark.rdd.UnionRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/UnionRDD.html "org.apache.spark.rdd.UnionRDD") for an example.  

Attributes
    protected  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#clone\(\):Object "Permalink") def clone(): AnyRef 

Attributes
    protected[lang]  

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#coalesce\(numPartitions:Int,shuffle:Boolean,partitionCoalescer:Option\[org.apache.spark.rdd.PartitionCoalescer\]\)\(implicitord:Ordering\[T\]\):org.apache.spark.rdd.RDD\[T\] "Permalink") def coalesce(numPartitions: Int, shuffle: Boolean = false, partitionCoalescer: Option[[PartitionCoalescer](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PartitionCoalescer.html "org.apache.spark.rdd.PartitionCoalescer")] = Option.empty)(implicit ord: Ordering[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)] = null): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]
Return a new RDD that is reduced into `numPartitions` partitions.
Return a new RDD that is reduced into `numPartitions` partitions.
This results in a narrow dependency, e.g. if you go from 1000 partitions to 100 partitions, there will not be a shuffle, instead each of the 100 new partitions will claim 10 of the current partitions. If a larger number of partitions is requested, it will stay at the current number of partitions.
However, if you're doing a drastic coalesce, e.g. to numPartitions = 1, this may result in your computation taking place on fewer nodes than you like (e.g. one node in the case of numPartitions = 1). To avoid this, you can pass shuffle = true. This will add a shuffle step, but means the current upstream partitions will be executed in parallel (per whatever the current partitioning is).  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Note
    
With shuffle = true, you can actually coalesce to a larger number of partitions. This is useful if you have a small number of partitions, say 100, potentially with a few partitions being abnormally large. Calling coalesce(1000, shuffle = true) will result in 1000 partitions with the data distributed using a hash partitioner. The optional partition coalescer passed in must be serializable.
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#collect\[U\]\(f:PartialFunction\[T,U\]\)\(implicitevidence$32:scala.reflect.ClassTag\[U\]\):org.apache.spark.rdd.RDD\[U\] "Permalink") def collect[U](f: PartialFunction[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD), U])(implicit arg0: ClassTag[U]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[U]
Return an RDD that contains all matching values by applying `f`.
Return an RDD that contains all matching values by applying `f`.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#collect\(\):Array\[T\] "Permalink") def collect(): Array[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]
Return an array that contains all of the elements in this RDD.
Return an array that contains all of the elements in this RDD.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Note
    
This method should only be used if the resulting array is expected to be small, as all the data is loaded into the driver's memory.
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#compute\(part:org.apache.spark.Partition,context:org.apache.spark.TaskContext\):Iterator\[\(org.apache.spark.graphx.VertexId,VD\)\] "Permalink") def compute(part: [Partition](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partition.html "org.apache.spark.Partition"), context: [TaskContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskContext.html "org.apache.spark.TaskContext")): Iterator[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]
Provides the `RDD[(VertexId, VD)]` equivalent output.
Provides the `RDD[(VertexId, VD)]` equivalent output.  

Definition Classes
     [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "org.apache.spark.graphx.VertexRDD") → [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#context:org.apache.spark.SparkContext "Permalink") def context: [SparkContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html "org.apache.spark.SparkContext")
The [org.apache.spark.SparkContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html "org.apache.spark.SparkContext") that this RDD was created on.
The [org.apache.spark.SparkContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html "org.apache.spark.SparkContext") that this RDD was created on. 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#count\(\):Long "Permalink") def count(): Long
Return the number of elements in the RDD.
Return the number of elements in the RDD.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#countApprox\(timeout:Long,confidence:Double\):org.apache.spark.partial.PartialResult\[org.apache.spark.partial.BoundedDouble\] "Permalink") def countApprox(timeout: Long, confidence: Double = 0.95): [PartialResult](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/partial/PartialResult.html "org.apache.spark.partial.PartialResult")[[BoundedDouble](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/partial/BoundedDouble.html "org.apache.spark.partial.BoundedDouble")]
Approximate version of count() that returns a potentially incomplete result within a timeout, even if not all tasks have finished.
Approximate version of count() that returns a potentially incomplete result within a timeout, even if not all tasks have finished.
The confidence is the probability that the error bounds of the result will contain the true value. That is, if countApprox were called repeatedly with confidence 0.9, we would expect 90% of the results to contain the true count. The confidence must be in the range [0,1] or an exception will be thrown.  

timeout
    
maximum time to wait for the job, in milliseconds 

confidence
    
the desired statistical confidence in the result 

returns
    
a potentially incomplete result, with error bounds 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#countApproxDistinct\(relativeSD:Double\):Long "Permalink") def countApproxDistinct(relativeSD: Double = 0.05): Long
Return approximate number of distinct elements in the RDD.
Return approximate number of distinct elements in the RDD.
The algorithm used is based on streamlib's implementation of "HyperLogLog in Practice: Algorithmic Engineering of a State of The Art Cardinality Estimation Algorithm", available [here](https://doi.org/10.1145/2452376.2452456).  

relativeSD
    
Relative accuracy. Smaller values create counters that require more space. It must be greater than 0.000017. 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  23. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#countApproxDistinct\(p:Int,sp:Int\):Long "Permalink") def countApproxDistinct(p: Int, sp: Int): Long
Return approximate number of distinct elements in the RDD.
Return approximate number of distinct elements in the RDD.
The algorithm used is based on streamlib's implementation of "HyperLogLog in Practice: Algorithmic Engineering of a State of The Art Cardinality Estimation Algorithm", available [here](https://doi.org/10.1145/2452376.2452456).
The relative accuracy is approximately `1.054 / sqrt(2^p)`. Setting a nonzero (`sp` is greater than `p`) would trigger sparse representation of registers, which may reduce the memory consumption and increase accuracy when the cardinality is small. `` 

p
    
The precision value for the normal set. `p` must be a value between 4 and `sp` if `sp` is not zero (32 max). 

sp
    
The precision value for the sparse set, between 0 and 32. If `sp` equals 0, the sparse representation is skipped. 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  24. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#countByValue\(\)\(implicitord:Ordering\[T\]\):scala.collection.Map\[T,Long\] "Permalink") def countByValue()(implicit ord: Ordering[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)] = null): Map[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD), Long]
Return the count of each unique value in this RDD as a local map of (value, count) pairs.
Return the count of each unique value in this RDD as a local map of (value, count) pairs.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Note
    
This method should only be used if the resulting map is expected to be small, as the whole thing is loaded into the driver's memory. To handle very large results, consider using

```
rdd.map(x => (x, 1L)).reduceByKey(_ + _)
```

, which returns an RDD[T, Long] instead of a map.
  25. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#countByValueApprox\(timeout:Long,confidence:Double\)\(implicitord:Ordering\[T\]\):org.apache.spark.partial.PartialResult\[scala.collection.Map\[T,org.apache.spark.partial.BoundedDouble\]\] "Permalink") def countByValueApprox(timeout: Long, confidence: Double = 0.95)(implicit ord: Ordering[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)] = null): [PartialResult](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/partial/PartialResult.html "org.apache.spark.partial.PartialResult")[Map[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD), [BoundedDouble](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/partial/BoundedDouble.html "org.apache.spark.partial.BoundedDouble")]]
Approximate version of countByValue().
Approximate version of countByValue().  

timeout
    
maximum time to wait for the job, in milliseconds 

confidence
    
the desired statistical confidence in the result 

returns
    
a potentially incomplete result, with error bounds 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  26. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#dependencies:Seq\[org.apache.spark.Dependency\[_\]\] "Permalink") final  def dependencies: Seq[[Dependency](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Dependency.html "org.apache.spark.Dependency")[_]]
Get the list of dependencies of this RDD, taking into account whether the RDD is checkpointed or not.
Get the list of dependencies of this RDD, taking into account whether the RDD is checkpointed or not.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  27. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#distinct\(\):org.apache.spark.rdd.RDD\[T\] "Permalink") def distinct(): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]
Return a new RDD containing the distinct elements in this RDD.
Return a new RDD containing the distinct elements in this RDD.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  28. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#distinct\(numPartitions:Int\)\(implicitord:Ordering\[T\]\):org.apache.spark.rdd.RDD\[T\] "Permalink") def distinct(numPartitions: Int)(implicit ord: Ordering[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)] = null): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]
Return a new RDD containing the distinct elements in this RDD.
Return a new RDD containing the distinct elements in this RDD.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  29. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  30. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#equals\(x$1:Object\):Boolean "Permalink") def equals(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef → Any
  31. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#filter\(pred:\(\(org.apache.spark.graphx.VertexId,VD\)\)=>Boolean\):org.apache.spark.graphx.VertexRDD\[VD\] "Permalink") def filter(pred: (([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)) => Boolean): [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "org.apache.spark.graphx.VertexRDD")[VD]
Restricts the vertex set to the set of vertices satisfying the given predicate.
Restricts the vertex set to the set of vertices satisfying the given predicate. This operation preserves the index for efficient joins with the original RDD, and it sets bits in the bitmask rather than allocating new memory.
It is declared and defined here to allow refining the return type from `RDD[(VertexId, VD)]` to `VertexRDD[VD]`.  

pred
    
the user defined predicate, which takes a tuple to conform to the `RDD[(VertexId, VD)]` interface 

Definition Classes
     [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "org.apache.spark.graphx.VertexRDD") → [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  32. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#first\(\):T "Permalink") def first(): ([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)
Return the first element in this RDD.
Return the first element in this RDD.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  33. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#firstParent\[U\]\(implicitevidence$36:scala.reflect.ClassTag\[U\]\):org.apache.spark.rdd.RDD\[U\] "Permalink") def firstParent[U](implicit arg0: ClassTag[U]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[U]
Returns the first parent RDD
Returns the first parent RDD 

Attributes
    protected[[spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")]  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  34. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#flatMap\[U\]\(f:T=>IterableOnce\[U\]\)\(implicitevidence$4:scala.reflect.ClassTag\[U\]\):org.apache.spark.rdd.RDD\[U\] "Permalink") def flatMap[U](f: (([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)) => IterableOnce[U])(implicit arg0: ClassTag[U]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[U]
Return a new RDD by first applying a function to all elements of this RDD, and then flattening the results.
Return a new RDD by first applying a function to all elements of this RDD, and then flattening the results.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  35. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#fold\(zeroValue:T\)\(op:\(T,T\)=>T\):T "Permalink") def fold(zeroValue: ([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD))(op: (([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD), ([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)) => ([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)): ([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)
Aggregate the elements of each partition, and then the results for all the partitions, using a given associative function and a neutral "zero value".
Aggregate the elements of each partition, and then the results for all the partitions, using a given associative function and a neutral "zero value". The function op(t1, t2) is allowed to modify t1 and return it as its result value to avoid object allocation; however, it should not modify t2.
This behaves somewhat differently from fold operations implemented for non-distributed collections in functional languages like Scala. This fold operation may be applied to partitions individually, and then fold those results into the final result, rather than apply the fold to each element sequentially in some defined ordering. For functions that are not commutative, the result may differ from that of a fold applied to a non-distributed collection.  

zeroValue
    
the initial value for the accumulated result of each partition for the `op` operator, and also the initial value for the combine results from different partitions for the `op` operator - this will typically be the neutral element (e.g. `Nil` for list concatenation or `0` for summation) 

op
    
an operator used to both accumulate results within a partition and combine results from different partitions 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  36. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#foreach\(f:T=>Unit\):Unit "Permalink") def foreach(f: (([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)) => Unit): Unit
Applies a function f to all elements of this RDD.
Applies a function f to all elements of this RDD.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  37. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#foreachPartition\(f:Iterator\[T\]=>Unit\):Unit "Permalink") def foreachPartition(f: (Iterator[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]) => Unit): Unit
Applies a function f to each partition of this RDD.
Applies a function f to each partition of this RDD.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  38. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#getCheckpointFile:Option\[String\] "Permalink") def getCheckpointFile: Option[String]
Gets the name of the directory to which this RDD was checkpointed.
Gets the name of the directory to which this RDD was checkpointed. This is not defined if the RDD is checkpointed locally.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  39. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef] 

Definition Classes
    AnyRef → Any 

Annotations
     @IntrinsicCandidate() @native()
  40. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#getDependencies:Seq\[org.apache.spark.Dependency\[_\]\] "Permalink") def getDependencies: Seq[[Dependency](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Dependency.html "org.apache.spark.Dependency")[_]]
Implemented by subclasses to return how this RDD depends on parent RDDs.
Implemented by subclasses to return how this RDD depends on parent RDDs. This method will only be called once, so it is safe to implement a time-consuming computation in it.  

Attributes
    protected  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  41. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#getNumPartitions:Int "Permalink") final  def getNumPartitions: Int
Returns the number of partitions of this RDD.
Returns the number of partitions of this RDD.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Annotations
     @Since("1.6.0")
  42. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#getOutputDeterministicLevel:org.apache.spark.rdd.DeterministicLevel.Value "Permalink") def getOutputDeterministicLevel: [rdd.DeterministicLevel.Value](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/DeterministicLevel$.html#ValueextendsOrdered\[Enumeration.this.Value\]withSerializable) 

Attributes
    protected  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Annotations
     @DeveloperApi()
  43. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#getPartitions:Array\[org.apache.spark.Partition\] "Permalink") def getPartitions: Array[[Partition](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partition.html "org.apache.spark.Partition")]
Implemented by subclasses to return the set of partitions in this RDD.
Implemented by subclasses to return the set of partitions in this RDD. This method will only be called once, so it is safe to implement a time-consuming computation in it.
The partitions in this array must satisfy the following property: `rdd.partitions.zipWithIndex.forall { case (partition, index) => partition.index == index }` 

Attributes
    protected  

Definition Classes
     [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "org.apache.spark.graphx.VertexRDD") → [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  44. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#getPreferredLocations\(split:org.apache.spark.Partition\):Seq\[String\] "Permalink") def getPreferredLocations(split: [Partition](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partition.html "org.apache.spark.Partition")): Seq[String]
Optionally overridden by subclasses to specify placement preferences.
Optionally overridden by subclasses to specify placement preferences.  

Attributes
    protected  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  45. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#getResourceProfile\(\):org.apache.spark.resource.ResourceProfile "Permalink") def getResourceProfile(): [ResourceProfile](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/resource/ResourceProfile.html "org.apache.spark.resource.ResourceProfile")
Get the ResourceProfile specified with this RDD or null if it wasn't specified.
Get the ResourceProfile specified with this RDD or null if it wasn't specified. 

returns
    
the user specified ResourceProfile or null (for Java compatibility) if none was specified 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Annotations
     @Experimental() @Since("3.1.0")
  46. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#getStorageLevel:org.apache.spark.storage.StorageLevel "Permalink") def getStorageLevel: [StorageLevel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StorageLevel.html "org.apache.spark.storage.StorageLevel")
Get the RDD's current storage level, or StorageLevel.NONE if none is set.
Get the RDD's current storage level, or StorageLevel.NONE if none is set. 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  47. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#glom\(\):org.apache.spark.rdd.RDD\[Array\[T\]\] "Permalink") def glom(): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[Array[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]]
Return an RDD created by coalescing all elements within each partition into an array.
Return an RDD created by coalescing all elements within each partition into an array.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  48. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#groupBy\[K\]\(f:T=>K,p:org.apache.spark.Partitioner\)\(implicitkt:scala.reflect.ClassTag\[K\],implicitord:Ordering\[K\]\):org.apache.spark.rdd.RDD\[\(K,Iterable\[T\]\)\] "Permalink") def groupBy[K](f: (([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)) => K, p: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner"))(implicit kt: ClassTag[K], ord: Ordering[K] = null): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, Iterable[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)])]
Return an RDD of grouped items.
Return an RDD of grouped items. Each group consists of a key and a sequence of elements mapping to that key. The ordering of elements within each group is not guaranteed, and may even differ each time the resulting RDD is evaluated.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Note
    
This operation may be very expensive. If you are grouping in order to perform an aggregation (such as a sum or average) over each key, using `PairRDDFunctions.aggregateByKey` or `PairRDDFunctions.reduceByKey` will provide much better performance.
  49. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#groupBy\[K\]\(f:T=>K,numPartitions:Int\)\(implicitkt:scala.reflect.ClassTag\[K\]\):org.apache.spark.rdd.RDD\[\(K,Iterable\[T\]\)\] "Permalink") def groupBy[K](f: (([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)) => K, numPartitions: Int)(implicit kt: ClassTag[K]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, Iterable[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)])]
Return an RDD of grouped elements.
Return an RDD of grouped elements. Each group consists of a key and a sequence of elements mapping to that key. The ordering of elements within each group is not guaranteed, and may even differ each time the resulting RDD is evaluated.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Note
    
This operation may be very expensive. If you are grouping in order to perform an aggregation (such as a sum or average) over each key, using `PairRDDFunctions.aggregateByKey` or `PairRDDFunctions.reduceByKey` will provide much better performance.
  50. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#groupBy\[K\]\(f:T=>K\)\(implicitkt:scala.reflect.ClassTag\[K\]\):org.apache.spark.rdd.RDD\[\(K,Iterable\[T\]\)\] "Permalink") def groupBy[K](f: (([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)) => K)(implicit kt: ClassTag[K]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, Iterable[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)])]
Return an RDD of grouped items.
Return an RDD of grouped items. Each group consists of a key and a sequence of elements mapping to that key. The ordering of elements within each group is not guaranteed, and may even differ each time the resulting RDD is evaluated.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Note
    
This operation may be very expensive. If you are grouping in order to perform an aggregation (such as a sum or average) over each key, using `PairRDDFunctions.aggregateByKey` or `PairRDDFunctions.reduceByKey` will provide much better performance.
  51. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#hashCode\(\):Int "Permalink") def hashCode(): Int 

Definition Classes
    AnyRef → Any 

Annotations
     @IntrinsicCandidate() @native()
  52. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#id:Int "Permalink") val id: Int
A unique ID for this RDD (within its SparkContext).
A unique ID for this RDD (within its SparkContext). 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  53. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#initializeLogIfNecessary\(isInterpreter:Boolean,silent:Boolean\):Boolean "Permalink") def initializeLogIfNecessary(isInterpreter: Boolean, silent: Boolean): Boolean 

Attributes
    protected  

Definition Classes
    Logging
  54. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#initializeLogIfNecessary\(isInterpreter:Boolean\):Unit "Permalink") def initializeLogIfNecessary(isInterpreter: Boolean): Unit 

Attributes
    protected  

Definition Classes
    Logging
  55. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#intersection\(other:org.apache.spark.rdd.RDD\[T\],numPartitions:Int\):org.apache.spark.rdd.RDD\[T\] "Permalink") def intersection(other: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)], numPartitions: Int): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]
Return the intersection of this RDD and another one.
Return the intersection of this RDD and another one. The output will not contain any duplicate elements, even if the input RDDs did. Performs a hash partition across the cluster  

numPartitions
    
How many partitions to use in the resulting RDD 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Note
    
This method performs a shuffle internally.
  56. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#intersection\(other:org.apache.spark.rdd.RDD\[T\],partitioner:org.apache.spark.Partitioner\)\(implicitord:Ordering\[T\]\):org.apache.spark.rdd.RDD\[T\] "Permalink") def intersection(other: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)], partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner"))(implicit ord: Ordering[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)] = null): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]
Return the intersection of this RDD and another one.
Return the intersection of this RDD and another one. The output will not contain any duplicate elements, even if the input RDDs did.  

partitioner
    
Partitioner to use for the resulting RDD 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Note
    
This method performs a shuffle internally.
  57. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#intersection\(other:org.apache.spark.rdd.RDD\[T\]\):org.apache.spark.rdd.RDD\[T\] "Permalink") def intersection(other: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]
Return the intersection of this RDD and another one.
Return the intersection of this RDD and another one. The output will not contain any duplicate elements, even if the input RDDs did.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Note
    
This method performs a shuffle internally.
  58. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#isBarrier_:Boolean "Permalink") lazy val isBarrier_: Boolean 

Attributes
    protected  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Annotations
     @transient()
  59. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#isCheckpointed:Boolean "Permalink") def isCheckpointed: Boolean
Return whether this RDD is checkpointed and materialized, either reliably or locally.
Return whether this RDD is checkpointed and materialized, either reliably or locally.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  60. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#isEmpty\(\):Boolean "Permalink") def isEmpty(): Boolean 

returns
    
true if and only if the RDD contains no elements at all. Note that an RDD may be empty even when it has at least 1 partition. 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Note
    
Due to complications in the internal implementation, this method will raise an exception if called on an RDD of `Nothing` or `Null`. This may be come up in practice because, for example, the type of `parallelize(Seq())` is `RDD[Nothing]`. (`parallelize(Seq())` should be avoided anyway in favor of `parallelize(Seq[T]())`.)
  61. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean 

Definition Classes
    Any
  62. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#isTraceEnabled\(\):Boolean "Permalink") def isTraceEnabled(): Boolean 

Attributes
    protected  

Definition Classes
    Logging
  63. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#iterator\(split:org.apache.spark.Partition,context:org.apache.spark.TaskContext\):Iterator\[T\] "Permalink") final  def iterator(split: [Partition](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partition.html "org.apache.spark.Partition"), context: [TaskContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskContext.html "org.apache.spark.TaskContext")): Iterator[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]
Internal method to this RDD; will read from cache if applicable, or otherwise compute it.
Internal method to this RDD; will read from cache if applicable, or otherwise compute it. This should _not_ be called by users directly, but is available for implementers of custom subclasses of RDD.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  64. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#keyBy\[K\]\(f:T=>K\):org.apache.spark.rdd.RDD\[\(K,T\)\] "Permalink") def keyBy[K](f: (([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)) => K): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, ([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD))]
Creates tuples of the elements in this RDD by applying `f`.
Creates tuples of the elements in this RDD by applying `f`.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  65. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#localCheckpoint\(\):RDD.this.type "Permalink") def localCheckpoint(): [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "org.apache.spark.graphx.VertexRDD").this.type
Mark this RDD for local checkpointing using Spark's existing caching layer.
Mark this RDD for local checkpointing using Spark's existing caching layer.
This method is for users who wish to truncate RDD lineages while skipping the expensive step of replicating the materialized data in a reliable distributed file system. This is useful for RDDs with long lineages that need to be truncated periodically (e.g. GraphX).
Local checkpointing sacrifices fault-tolerance for performance. In particular, checkpointed data is written to ephemeral local storage in the executors instead of to a reliable, fault-tolerant storage. The effect is that if an executor fails during the computation, the checkpointed data may no longer be accessible, causing an irrecoverable job failure.
This is NOT safe to use with dynamic allocation, which removes executors along with their cached blocks. If you must use both features, you are advised to set `spark.dynamicAllocation.cachedExecutorIdleTimeout` to a high value.
The checkpoint directory set through `SparkContext#setCheckpointDir` is not used.
The data is only checkpointed when `doCheckpoint()` is called, and this only happens at the end of the first action execution on this RDD. The final data that is checkpointed after the first action may be different from the data that was used during the action, due to non-determinism of the underlying operation and retries. If the purpose of the checkpoint is to achieve saving a deterministic snapshot of the data, an eager action may need to be called first on the RDD to trigger the checkpoint.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  66. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#log:org.slf4j.Logger "Permalink") def log: Logger 

Attributes
    protected  

Definition Classes
    Logging
  67. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#logBasedOnLevel\(level:org.slf4j.event.Level\)\(f:=>org.apache.spark.internal.MessageWithContext\):Unit "Permalink") def logBasedOnLevel(level: Level)(f: => MessageWithContext): Unit 

Attributes
    protected  

Definition Classes
    Logging
  68. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#logDebug\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logDebug(msg: => String, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  69. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#logDebug\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logDebug(entry: LogEntry, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  70. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#logDebug\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logDebug(entry: LogEntry): Unit 

Attributes
    protected  

Definition Classes
    Logging
  71. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#logDebug\(msg:=>String\):Unit "Permalink") def logDebug(msg: => String): Unit 

Attributes
    protected  

Definition Classes
    Logging
  72. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#logError\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logError(msg: => String, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  73. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#logError\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logError(entry: LogEntry, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  74. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#logError\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logError(entry: LogEntry): Unit 

Attributes
    protected  

Definition Classes
    Logging
  75. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#logError\(msg:=>String\):Unit "Permalink") def logError(msg: => String): Unit 

Attributes
    protected  

Definition Classes
    Logging
  76. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#logInfo\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logInfo(msg: => String, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  77. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#logInfo\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logInfo(entry: LogEntry, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  78. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#logInfo\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logInfo(entry: LogEntry): Unit 

Attributes
    protected  

Definition Classes
    Logging
  79. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#logInfo\(msg:=>String\):Unit "Permalink") def logInfo(msg: => String): Unit 

Attributes
    protected  

Definition Classes
    Logging
  80. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#logName:String "Permalink") def logName: [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String") 

Attributes
    protected  

Definition Classes
    Logging
  81. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#logTrace\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logTrace(msg: => String, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  82. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#logTrace\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logTrace(entry: LogEntry, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  83. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#logTrace\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logTrace(entry: LogEntry): Unit 

Attributes
    protected  

Definition Classes
    Logging
  84. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#logTrace\(msg:=>String\):Unit "Permalink") def logTrace(msg: => String): Unit 

Attributes
    protected  

Definition Classes
    Logging
  85. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#logWarning\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logWarning(msg: => String, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  86. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#logWarning\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logWarning(entry: LogEntry, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  87. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#logWarning\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logWarning(entry: LogEntry): Unit 

Attributes
    protected  

Definition Classes
    Logging
  88. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#logWarning\(msg:=>String\):Unit "Permalink") def logWarning(msg: => String): Unit 

Attributes
    protected  

Definition Classes
    Logging
  89. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#map\[U\]\(f:T=>U\)\(implicitevidence$3:scala.reflect.ClassTag\[U\]\):org.apache.spark.rdd.RDD\[U\] "Permalink") def map[U](f: (([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)) => U)(implicit arg0: ClassTag[U]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[U]
Return a new RDD by applying a function to all elements of this RDD.
Return a new RDD by applying a function to all elements of this RDD.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  90. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#mapPartitions\[U\]\(f:Iterator\[T\]=>Iterator\[U\],preservesPartitioning:Boolean\)\(implicitevidence$6:scala.reflect.ClassTag\[U\]\):org.apache.spark.rdd.RDD\[U\] "Permalink") def mapPartitions[U](f: (Iterator[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]) => Iterator[U], preservesPartitioning: Boolean = false)(implicit arg0: ClassTag[U]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[U]
Return a new RDD by applying a function to each partition of this RDD.
Return a new RDD by applying a function to each partition of this RDD.
`preservesPartitioning` indicates whether the input function preserves the partitioner, which should be `false` unless this is a pair RDD and the input function doesn't modify the keys.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  91. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#mapPartitionsWithEvaluator\[U\]\(evaluatorFactory:org.apache.spark.PartitionEvaluatorFactory\[T,U\]\)\(implicitevidence$10:scala.reflect.ClassTag\[U\]\):org.apache.spark.rdd.RDD\[U\] "Permalink") def mapPartitionsWithEvaluator[U](evaluatorFactory: [PartitionEvaluatorFactory](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/PartitionEvaluatorFactory.html "org.apache.spark.PartitionEvaluatorFactory")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD), U])(implicit arg0: ClassTag[U]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[U]
Return a new RDD by applying an evaluator to each partition of this RDD.
Return a new RDD by applying an evaluator to each partition of this RDD. The given evaluator factory will be serialized and sent to executors, and each task will create an evaluator with the factory, and use the evaluator to transform the data of the input partition.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Annotations
     @DeveloperApi() @Since("3.5.0")
  92. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#mapPartitionsWithIndex\[U\]\(f:\(Int,Iterator\[T\]\)=>Iterator\[U\],preservesPartitioning:Boolean\)\(implicitevidence$9:scala.reflect.ClassTag\[U\]\):org.apache.spark.rdd.RDD\[U\] "Permalink") def mapPartitionsWithIndex[U](f: (Int, Iterator[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]) => Iterator[U], preservesPartitioning: Boolean = false)(implicit arg0: ClassTag[U]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[U]
Return a new RDD by applying a function to each partition of this RDD, while tracking the index of the original partition.
Return a new RDD by applying a function to each partition of this RDD, while tracking the index of the original partition.
`preservesPartitioning` indicates whether the input function preserves the partitioner, which should be `false` unless this is a pair RDD and the input function doesn't modify the keys.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  93. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#max\(\)\(implicitord:Ordering\[T\]\):T "Permalink") def max()(implicit ord: Ordering[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]): ([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)
Returns the max of this RDD as defined by the implicit Ordering[T].
Returns the max of this RDD as defined by the implicit Ordering[T]. 

returns
    
the maximum element of the RDD 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  94. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#min\(\)\(implicitord:Ordering\[T\]\):T "Permalink") def min()(implicit ord: Ordering[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]): ([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)
Returns the min of this RDD as defined by the implicit Ordering[T].
Returns the min of this RDD as defined by the implicit Ordering[T]. 

returns
    
the minimum element of the RDD 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  95. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#name:String "Permalink") var name: String
A friendly name for this RDD
A friendly name for this RDD 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  96. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  97. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#notify\(\):Unit "Permalink") final  def notify(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  98. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  99. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#parent\[U\]\(j:Int\)\(implicitevidence$37:scala.reflect.ClassTag\[U\]\):org.apache.spark.rdd.RDD\[U\] "Permalink") def parent[U](j: Int)(implicit arg0: ClassTag[U]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[U]
Returns the jth parent RDD: e.g.
Returns the jth parent RDD: e.g. rdd.parent[T](0) is equivalent to rdd.firstParent[T] 

Attributes
    protected[[spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")]  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  100. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#partitioner:Option\[org.apache.spark.Partitioner\] "Permalink") val partitioner: Option[[Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner")]
Optionally overridden by subclasses to specify how they are partitioned.
Optionally overridden by subclasses to specify how they are partitioned. 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  101. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#partitions:Array\[org.apache.spark.Partition\] "Permalink") final  def partitions: Array[[Partition](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partition.html "org.apache.spark.Partition")]
Get the array of partitions of this RDD, taking into account whether the RDD is checkpointed or not.
Get the array of partitions of this RDD, taking into account whether the RDD is checkpointed or not.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  102. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#persist\(\):RDD.this.type "Permalink") def persist(): [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "org.apache.spark.graphx.VertexRDD").this.type
Persist this RDD with the default storage level (`MEMORY_ONLY`).
Persist this RDD with the default storage level (`MEMORY_ONLY`).  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  103. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#persist\(newLevel:org.apache.spark.storage.StorageLevel\):RDD.this.type "Permalink") def persist(newLevel: [StorageLevel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StorageLevel.html "org.apache.spark.storage.StorageLevel")): [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "org.apache.spark.graphx.VertexRDD").this.type
Set this RDD's storage level to persist its values across operations after the first time it is computed.
Set this RDD's storage level to persist its values across operations after the first time it is computed. This can only be used to assign a new storage level if the RDD does not have a storage level set yet. Local checkpointing is an exception.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  104. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#pipe\(command:Seq\[String\],env:scala.collection.Map\[String,String\],printPipeContext:\(String=>Unit\)=>Unit,printRDDElement:\(T,String=>Unit\)=>Unit,separateWorkingDir:Boolean,bufferSize:Int,encoding:String\):org.apache.spark.rdd.RDD\[String\] "Permalink") def pipe(command: Seq[String], env: Map[String, String] = Map(), printPipeContext: ((String) => Unit) => Unit = null, printRDDElement: (([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD), (String) => Unit) => Unit = null, separateWorkingDir: Boolean = false, bufferSize: Int = 8192, encoding: String = Codec.defaultCharsetCodec.name): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[String]
Return an RDD created by piping elements to a forked external process.
Return an RDD created by piping elements to a forked external process. The resulting RDD is computed by executing the given process once per partition. All elements of each input partition are written to a process's stdin as lines of input separated by a newline. The resulting partition consists of the process's stdout output, with each line of stdout resulting in one element of the output partition. A process is invoked even for empty partitions.
The print behavior can be customized by providing two functions.  

command
    
command to run in forked process. 

env
    
environment variables to set. 

printPipeContext
    
Before piping elements, this function is called as an opportunity to pipe context data. Print line function (like out.println) will be passed as printPipeContext's parameter. 

printRDDElement
    
Use this function to customize how to pipe elements. This function will be called with each RDD element as the 1st parameter, and the print line function (like out.println()) as the 2nd parameter. An example of pipe the RDD data of groupBy() in a streaming way, instead of constructing a huge String to concat all the elements:

```
def printRDDElement(record:(String, Seq[String]), f:String=>Unit) =
  for (e <- record._2) {f(e)}
```


separateWorkingDir
    
Use separate working directories for each task. 

bufferSize
    
Buffer size for the stdin writer for the piped process. 

encoding
    
Char encoding used for interacting (via stdin, stdout and stderr) with the piped process 

returns
    
the result RDD 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  105. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#pipe\(command:String,env:scala.collection.Map\[String,String\]\):org.apache.spark.rdd.RDD\[String\] "Permalink") def pipe(command: String, env: Map[String, String]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[String]
Return an RDD created by piping elements to a forked external process.
Return an RDD created by piping elements to a forked external process.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  106. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#pipe\(command:String\):org.apache.spark.rdd.RDD\[String\] "Permalink") def pipe(command: String): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[String]
Return an RDD created by piping elements to a forked external process.
Return an RDD created by piping elements to a forked external process.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  107. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#preferredLocations\(split:org.apache.spark.Partition\):Seq\[String\] "Permalink") final  def preferredLocations(split: [Partition](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partition.html "org.apache.spark.Partition")): Seq[String]
Get the preferred locations of a partition, taking into account whether the RDD is checkpointed.
Get the preferred locations of a partition, taking into account whether the RDD is checkpointed.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  108. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#randomSplit\(weights:Array\[Double\],seed:Long\):Array\[org.apache.spark.rdd.RDD\[T\]\] "Permalink") def randomSplit(weights: Array[Double], seed: Long = [Utils.random.nextLong](https://spark.apache.org/docs/latest/api/scala/org/index.html)): Array[[RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]]
Randomly splits this RDD with the provided weights.
Randomly splits this RDD with the provided weights.  

weights
    
weights for splits, will be normalized if they don't sum to 1 

seed
    
random seed 

returns
    
split RDDs in an array 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  109. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#reduce\(f:\(T,T\)=>T\):T "Permalink") def reduce(f: (([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD), ([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)) => ([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)): ([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)
Reduces the elements of this RDD using the specified commutative and associative binary operator.
Reduces the elements of this RDD using the specified commutative and associative binary operator.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  110. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#repartition\(numPartitions:Int\)\(implicitord:Ordering\[T\]\):org.apache.spark.rdd.RDD\[T\] "Permalink") def repartition(numPartitions: Int)(implicit ord: Ordering[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)] = null): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]
Return a new RDD that has exactly numPartitions partitions.
Return a new RDD that has exactly numPartitions partitions.
Can increase or decrease the level of parallelism in this RDD. Internally, this uses a shuffle to redistribute data.
If you are decreasing the number of partitions in this RDD, consider using `coalesce`, which can avoid performing a shuffle.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  111. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#sample\(withReplacement:Boolean,fraction:Double,seed:Long\):org.apache.spark.rdd.RDD\[T\] "Permalink") def sample(withReplacement: Boolean, fraction: Double, seed: Long = [Utils.random.nextLong](https://spark.apache.org/docs/latest/api/scala/org/index.html)): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]
Return a sampled subset of this RDD.
Return a sampled subset of this RDD.  

withReplacement
    
can elements be sampled multiple times (replaced when sampled out) 

fraction
    
expected size of the sample as a fraction of this RDD's size without replacement: probability that each element is chosen; fraction must be [0, 1] with replacement: expected number of times each element is chosen; fraction must be greater than or equal to 0 

seed
    
seed for the random number generator 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Note
    
This is NOT guaranteed to provide exactly the fraction of the count of the given RDD.
  112. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#saveAsObjectFile\(path:String\):Unit "Permalink") def saveAsObjectFile(path: String): Unit
Save this RDD as a SequenceFile of serialized objects.
Save this RDD as a SequenceFile of serialized objects.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  113. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#saveAsTextFile\(path:String,codec:Class\[_<:org.apache.hadoop.io.compress.CompressionCodec\]\):Unit "Permalink") def saveAsTextFile(path: String, codec: Class[_ <: CompressionCodec]): Unit
Save this RDD as a compressed text file, using string representations of elements.
Save this RDD as a compressed text file, using string representations of elements.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  114. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#saveAsTextFile\(path:String\):Unit "Permalink") def saveAsTextFile(path: String): Unit
Save this RDD as a text file, using string representations of elements.
Save this RDD as a text file, using string representations of elements.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  115. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#setName\(_name:String\):RDD.this.type "Permalink") def setName(_name: String): [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "org.apache.spark.graphx.VertexRDD").this.type
Assign a name to this RDD
Assign a name to this RDD 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  116. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#sortBy\[K\]\(f:T=>K,ascending:Boolean,numPartitions:Int\)\(implicitord:Ordering\[K\],implicitctag:scala.reflect.ClassTag\[K\]\):org.apache.spark.rdd.RDD\[T\] "Permalink") def sortBy[K](f: (([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)) => K, ascending: Boolean = true, numPartitions: Int = [this.partitions.length](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html#partitions:Array\[org.apache.spark.Partition\]))(implicit ord: Ordering[K], ctag: ClassTag[K]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]
Return this RDD sorted by the given key function.
Return this RDD sorted by the given key function.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  117. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#sparkContext:org.apache.spark.SparkContext "Permalink") def sparkContext: [SparkContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html "org.apache.spark.SparkContext")
The SparkContext that created this RDD.
The SparkContext that created this RDD. 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  118. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#subtract\(other:org.apache.spark.rdd.RDD\[T\],p:org.apache.spark.Partitioner\)\(implicitord:Ordering\[T\]\):org.apache.spark.rdd.RDD\[T\] "Permalink") def subtract(other: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)], p: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner"))(implicit ord: Ordering[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)] = null): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]
Return an RDD with the elements from `this` that are not in `other`.
Return an RDD with the elements from `this` that are not in `other`.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  119. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#subtract\(other:org.apache.spark.rdd.RDD\[T\],numPartitions:Int\):org.apache.spark.rdd.RDD\[T\] "Permalink") def subtract(other: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)], numPartitions: Int): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]
Return an RDD with the elements from `this` that are not in `other`.
Return an RDD with the elements from `this` that are not in `other`.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  120. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#subtract\(other:org.apache.spark.rdd.RDD\[T\]\):org.apache.spark.rdd.RDD\[T\] "Permalink") def subtract(other: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]
Return an RDD with the elements from `this` that are not in `other`.
Return an RDD with the elements from `this` that are not in `other`.
Uses `this` partitioner/partition size, because even if `other` is huge, the resulting RDD will be <= us.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  121. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0 

Definition Classes
    AnyRef
  122. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#take\(num:Int\):Array\[T\] "Permalink") def take(num: Int): Array[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]
Take the first num elements of the RDD.
Take the first num elements of the RDD. It works by first scanning one partition, and use the results from that partition to estimate the number of additional partitions needed to satisfy the limit.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Note
    
This method should only be used if the resulting array is expected to be small, as all the data is loaded into the driver's memory.
, 
Due to complications in the internal implementation, this method will raise an exception if called on an RDD of `Nothing` or `Null`.
  123. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#takeOrdered\(num:Int\)\(implicitord:Ordering\[T\]\):Array\[T\] "Permalink") def takeOrdered(num: Int)(implicit ord: Ordering[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]): Array[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]
Returns the first k (smallest) elements from this RDD as defined by the specified implicit Ordering[T] and maintains the ordering.
Returns the first k (smallest) elements from this RDD as defined by the specified implicit Ordering[T] and maintains the ordering. This does the opposite of [top](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#top\(num:Int\)\(implicitord:Ordering\[T\]\):Array\[T\]). For example:

```
sc.parallelize(Seq(10, 4, 2, 12, 3)).takeOrdered(1)
// returns Array(2)

sc.parallelize(Seq(2, 3, 4, 5, 6)).takeOrdered(2)
// returns Array(2, 3)
```


num
    
k, the number of elements to return 

ord
    
the implicit ordering for T 

returns
    
an array of top elements 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Note
    
This method should only be used if the resulting array is expected to be small, as all the data is loaded into the driver's memory.
  124. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#takeSample\(withReplacement:Boolean,num:Int,seed:Long\):Array\[T\] "Permalink") def takeSample(withReplacement: Boolean, num: Int, seed: Long = [Utils.random.nextLong](https://spark.apache.org/docs/latest/api/scala/org/index.html)): Array[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]
Return a fixed-size sampled subset of this RDD in an array 
Return a fixed-size sampled subset of this RDD in an array  

withReplacement
    
whether sampling is done with replacement 

num
    
size of the returned sample 

seed
    
seed for the random number generator 

returns
    
sample of specified size in an array 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Note
    
this method should only be used if the resulting array is expected to be small, as all the data is loaded into the driver's memory.
  125. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#toDebugString:String "Permalink") def toDebugString: String
A description of this RDD and its recursive dependencies for debugging.
A description of this RDD and its recursive dependencies for debugging. 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  126. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#toJavaRDD\(\):org.apache.spark.api.java.JavaRDD\[T\] "Permalink") def toJavaRDD(): [JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)] 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  127. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#toLocalIterator:Iterator\[T\] "Permalink") def toLocalIterator: Iterator[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]
Return an iterator that contains all of the elements in this RDD.
Return an iterator that contains all of the elements in this RDD.
The iterator will consume as much memory as the largest partition in this RDD.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Note
    
This results in multiple Spark jobs, and if the input RDD is the result of a wide transformation (e.g. join with different partitioners), to avoid recomputing the input RDD should be cached first.
  128. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#toString\(\):String "Permalink") def toString(): String 

Definition Classes
     [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") → AnyRef → Any
  129. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#top\(num:Int\)\(implicitord:Ordering\[T\]\):Array\[T\] "Permalink") def top(num: Int)(implicit ord: Ordering[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]): Array[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]
Returns the top k (largest) elements from this RDD as defined by the specified implicit Ordering[T] and maintains the ordering.
Returns the top k (largest) elements from this RDD as defined by the specified implicit Ordering[T] and maintains the ordering. This does the opposite of [takeOrdered](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#takeOrdered\(num:Int\)\(implicitord:Ordering\[T\]\):Array\[T\]). For example:

```
sc.parallelize(Seq(10, 4, 2, 12, 3)).top(1)
// returns Array(12)

sc.parallelize(Seq(2, 3, 4, 5, 6)).top(2)
// returns Array(6, 5)
```


num
    
k, the number of top elements to return 

ord
    
the implicit ordering for T 

returns
    
an array of top elements 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Note
    
This method should only be used if the resulting array is expected to be small, as all the data is loaded into the driver's memory.
  130. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#treeAggregate\[U\]\(zeroValue:U,seqOp:\(U,T\)=>U,combOp:\(U,U\)=>U,depth:Int,finalAggregateOnExecutor:Boolean\)\(implicitevidence$35:scala.reflect.ClassTag\[U\]\):U "Permalink") def treeAggregate[U](zeroValue: U, seqOp: (U, ([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)) => U, combOp: (U, U) => U, depth: Int, finalAggregateOnExecutor: Boolean)(implicit arg0: ClassTag[U]): U
[org.apache.spark.rdd.RDD#treeAggregate](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html#treeAggregate\[U\]\(zeroValue:U,seqOp:\(U,T\)=>U,combOp:\(U,U\)=>U,depth:Int,finalAggregateOnExecutor:Boolean\)\(implicitevidence$35:scala.reflect.ClassTag\[U\]\):U) with a parameter to do the final aggregation on the executor 
[org.apache.spark.rdd.RDD#treeAggregate](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html#treeAggregate\[U\]\(zeroValue:U,seqOp:\(U,T\)=>U,combOp:\(U,U\)=>U,depth:Int,finalAggregateOnExecutor:Boolean\)\(implicitevidence$35:scala.reflect.ClassTag\[U\]\):U) with a parameter to do the final aggregation on the executor  

finalAggregateOnExecutor
    
do final aggregation on executor 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  131. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#treeAggregate\[U\]\(zeroValue:U\)\(seqOp:\(U,T\)=>U,combOp:\(U,U\)=>U,depth:Int\)\(implicitevidence$34:scala.reflect.ClassTag\[U\]\):U "Permalink") def treeAggregate[U](zeroValue: U)(seqOp: (U, ([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)) => U, combOp: (U, U) => U, depth: Int = 2)(implicit arg0: ClassTag[U]): U
Aggregates the elements of this RDD in a multi-level tree pattern.
Aggregates the elements of this RDD in a multi-level tree pattern. This method is semantically identical to [org.apache.spark.rdd.RDD#aggregate](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html#aggregate\[U\]\(zeroValue:U\)\(seqOp:\(U,T\)=>U,combOp:\(U,U\)=>U\)\(implicitevidence$33:scala.reflect.ClassTag\[U\]\):U).  

depth
    
suggested depth of the tree (default: 2) 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  132. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#treeReduce\(f:\(T,T\)=>T,depth:Int\):T "Permalink") def treeReduce(f: (([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD), ([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)) => ([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD), depth: Int = 2): ([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)
Reduces the elements of this RDD in a multi-level tree pattern.
Reduces the elements of this RDD in a multi-level tree pattern.  

depth
    
suggested depth of the tree (default: 2) 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

See also
    
[org.apache.spark.rdd.RDD#reduce](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html#reduce\(f:\(T,T\)=>T\):T)
  133. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#union\(other:org.apache.spark.rdd.RDD\[T\]\):org.apache.spark.rdd.RDD\[T\] "Permalink") def union(other: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]
Return the union of this RDD and another one.
Return the union of this RDD and another one. Any identical elements will appear multiple times (use `.distinct()` to eliminate them).  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  134. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#unpersist\(blocking:Boolean\):RDD.this.type "Permalink") def unpersist(blocking: Boolean = false): [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "org.apache.spark.graphx.VertexRDD").this.type
Mark the RDD as non-persistent, and remove all blocks for it from memory and disk.
Mark the RDD as non-persistent, and remove all blocks for it from memory and disk.  

blocking
    
Whether to block until all blocks are deleted (default: false) 

returns
    
This RDD. 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  135. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  136. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  137. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#wait\(\):Unit "Permalink") final  def wait(): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  138. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#withLogContext\(context:java.util.Map\[String,String\]\)\(body:=>Unit\):Unit "Permalink") def withLogContext(context: [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#java.util.Map "java.util.Map")[String, String])(body: => Unit): Unit 

Attributes
    protected  

Definition Classes
    Logging
  139. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#withResources\(rp:org.apache.spark.resource.ResourceProfile\):RDD.this.type "Permalink") def withResources(rp: [ResourceProfile](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/resource/ResourceProfile.html "org.apache.spark.resource.ResourceProfile")): [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "org.apache.spark.graphx.VertexRDD").this.type
Specify a ResourceProfile to use when calculating this RDD.
Specify a ResourceProfile to use when calculating this RDD. This is only supported on certain cluster managers and currently requires dynamic allocation to be enabled. It will result in new executors with the resources specified being acquired to calculate the RDD.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Annotations
     @Experimental() @Since("3.1.0")
  140. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#zip\[U\]\(other:org.apache.spark.rdd.RDD\[U\]\)\(implicitevidence$13:scala.reflect.ClassTag\[U\]\):org.apache.spark.rdd.RDD\[\(T,U\)\] "Permalink") def zip[U](other: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[U])(implicit arg0: ClassTag[U]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD), U)]
Zips this RDD with another one, returning key-value pairs with the first element in each RDD, second element in each RDD, etc.
Zips this RDD with another one, returning key-value pairs with the first element in each RDD, second element in each RDD, etc. Assumes that the two RDDs have the *same number of partitions* and the *same number of elements in each partition* (e.g. one was made through a map on the other).  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  141. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#zipPartitions\[B,C,D,V\]\(rdd2:org.apache.spark.rdd.RDD\[B\],rdd3:org.apache.spark.rdd.RDD\[C\],rdd4:org.apache.spark.rdd.RDD\[D\]\)\(f:\(Iterator\[T\],Iterator\[B\],Iterator\[C\],Iterator\[D\]\)=>Iterator\[V\]\)\(implicitevidence$28:scala.reflect.ClassTag\[B\],implicitevidence$29:scala.reflect.ClassTag\[C\],implicitevidence$30:scala.reflect.ClassTag\[D\],implicitevidence$31:scala.reflect.ClassTag\[V\]\):org.apache.spark.rdd.RDD\[V\] "Permalink") def zipPartitions[B, C, D, V](rdd2: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[B], rdd3: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[C], rdd4: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[D])(f: (Iterator[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)], Iterator[B], Iterator[C], Iterator[D]) => Iterator[V])(implicit arg0: ClassTag[B], arg1: ClassTag[C], arg2: ClassTag[D], arg3: ClassTag[V]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[V] 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  142. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#zipPartitions\[B,C,D,V\]\(rdd2:org.apache.spark.rdd.RDD\[B\],rdd3:org.apache.spark.rdd.RDD\[C\],rdd4:org.apache.spark.rdd.RDD\[D\],preservesPartitioning:Boolean\)\(f:\(Iterator\[T\],Iterator\[B\],Iterator\[C\],Iterator\[D\]\)=>Iterator\[V\]\)\(implicitevidence$24:scala.reflect.ClassTag\[B\],implicitevidence$25:scala.reflect.ClassTag\[C\],implicitevidence$26:scala.reflect.ClassTag\[D\],implicitevidence$27:scala.reflect.ClassTag\[V\]\):org.apache.spark.rdd.RDD\[V\] "Permalink") def zipPartitions[B, C, D, V](rdd2: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[B], rdd3: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[C], rdd4: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[D], preservesPartitioning: Boolean)(f: (Iterator[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)], Iterator[B], Iterator[C], Iterator[D]) => Iterator[V])(implicit arg0: ClassTag[B], arg1: ClassTag[C], arg2: ClassTag[D], arg3: ClassTag[V]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[V] 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  143. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#zipPartitions\[B,C,V\]\(rdd2:org.apache.spark.rdd.RDD\[B\],rdd3:org.apache.spark.rdd.RDD\[C\]\)\(f:\(Iterator\[T\],Iterator\[B\],Iterator\[C\]\)=>Iterator\[V\]\)\(implicitevidence$21:scala.reflect.ClassTag\[B\],implicitevidence$22:scala.reflect.ClassTag\[C\],implicitevidence$23:scala.reflect.ClassTag\[V\]\):org.apache.spark.rdd.RDD\[V\] "Permalink") def zipPartitions[B, C, V](rdd2: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[B], rdd3: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[C])(f: (Iterator[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)], Iterator[B], Iterator[C]) => Iterator[V])(implicit arg0: ClassTag[B], arg1: ClassTag[C], arg2: ClassTag[V]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[V] 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  144. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#zipPartitions\[B,C,V\]\(rdd2:org.apache.spark.rdd.RDD\[B\],rdd3:org.apache.spark.rdd.RDD\[C\],preservesPartitioning:Boolean\)\(f:\(Iterator\[T\],Iterator\[B\],Iterator\[C\]\)=>Iterator\[V\]\)\(implicitevidence$18:scala.reflect.ClassTag\[B\],implicitevidence$19:scala.reflect.ClassTag\[C\],implicitevidence$20:scala.reflect.ClassTag\[V\]\):org.apache.spark.rdd.RDD\[V\] "Permalink") def zipPartitions[B, C, V](rdd2: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[B], rdd3: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[C], preservesPartitioning: Boolean)(f: (Iterator[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)], Iterator[B], Iterator[C]) => Iterator[V])(implicit arg0: ClassTag[B], arg1: ClassTag[C], arg2: ClassTag[V]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[V] 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  145. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#zipPartitions\[B,V\]\(rdd2:org.apache.spark.rdd.RDD\[B\]\)\(f:\(Iterator\[T\],Iterator\[B\]\)=>Iterator\[V\]\)\(implicitevidence$16:scala.reflect.ClassTag\[B\],implicitevidence$17:scala.reflect.ClassTag\[V\]\):org.apache.spark.rdd.RDD\[V\] "Permalink") def zipPartitions[B, V](rdd2: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[B])(f: (Iterator[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)], Iterator[B]) => Iterator[V])(implicit arg0: ClassTag[B], arg1: ClassTag[V]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[V] 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  146. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#zipPartitions\[B,V\]\(rdd2:org.apache.spark.rdd.RDD\[B\],preservesPartitioning:Boolean\)\(f:\(Iterator\[T\],Iterator\[B\]\)=>Iterator\[V\]\)\(implicitevidence$14:scala.reflect.ClassTag\[B\],implicitevidence$15:scala.reflect.ClassTag\[V\]\):org.apache.spark.rdd.RDD\[V\] "Permalink") def zipPartitions[B, V](rdd2: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[B], preservesPartitioning: Boolean)(f: (Iterator[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)], Iterator[B]) => Iterator[V])(implicit arg0: ClassTag[B], arg1: ClassTag[V]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[V]
Zip this RDD's partitions with one (or more) RDD(s) and return a new RDD by applying a function to the zipped partitions.
Zip this RDD's partitions with one (or more) RDD(s) and return a new RDD by applying a function to the zipped partitions. Assumes that all the RDDs have the *same number of partitions*, but does *not* require them to have the same number of elements in each partition.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  147. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#zipPartitionsWithEvaluator\[U\]\(rdd2:org.apache.spark.rdd.RDD\[T\],evaluatorFactory:org.apache.spark.PartitionEvaluatorFactory\[T,U\]\)\(implicitevidence$11:scala.reflect.ClassTag\[U\]\):org.apache.spark.rdd.RDD\[U\] "Permalink") def zipPartitionsWithEvaluator[U](rdd2: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)], evaluatorFactory: [PartitionEvaluatorFactory](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/PartitionEvaluatorFactory.html "org.apache.spark.PartitionEvaluatorFactory")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD), U])(implicit arg0: ClassTag[U]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[U]
Zip this RDD's partitions with another RDD and return a new RDD by applying an evaluator to the zipped partitions.
Zip this RDD's partitions with another RDD and return a new RDD by applying an evaluator to the zipped partitions. Assumes that the two RDDs have the *same number of partitions*, but does *not* require them to have the same number of elements in each partition.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Annotations
     @DeveloperApi() @Since("3.5.0")
  148. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#zipWithIndex\(\):org.apache.spark.rdd.RDD\[\(T,Long\)\] "Permalink") def zipWithIndex(): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD), Long)]
Zips this RDD with its element indices.
Zips this RDD with its element indices. The ordering is first based on the partition index and then the ordering of items within each partition. So the first item in the first partition gets index 0, and the last item in the last partition receives the largest index.
This is similar to Scala's zipWithIndex but it uses Long instead of Int as the index type. This method needs to trigger a spark job when this RDD contains more than one partitions.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Note
    
Some RDDs, such as those returned by groupBy(), do not guarantee order of elements in a partition. The index assigned to each element is therefore not guaranteed, and may even change if the RDD is reevaluated. If a fixed ordering is required to guarantee the same index assignments, you should sort the RDD with sortByKey() or save it to a file.
  149. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#zipWithUniqueId\(\):org.apache.spark.rdd.RDD\[\(T,Long\)\] "Permalink") def zipWithUniqueId(): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD), Long)]
Zips this RDD with generated unique Long ids.
Zips this RDD with generated unique Long ids. Items in the kth partition will get ids k, n+k, 2*n+k, ..., where n is the number of partitions. So there may exist gaps, but this method won't trigger a spark job, which is different from [org.apache.spark.rdd.RDD#zipWithIndex](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html#zipWithIndex\(\):org.apache.spark.rdd.RDD\[\(T,Long\)\]).  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Note
    
Some RDDs, such as those returned by groupBy(), do not guarantee order of elements in a partition. The unique ID assigned to each element is therefore not guaranteed, and may even change if the RDD is reevaluated. If a fixed ordering is required to guarantee the same index assignments, you should sort the RDD with sortByKey() or save it to a file.


### Deprecated Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#finalize\(\):Unit "Permalink") def finalize(): Unit 

Attributes
    protected[lang]  

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.Throwable]) @Deprecated 

Deprecated
    
_(Since version 9)_


### Inherited from [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]
### Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#++\(other:org.apache.spark.rdd.RDD\[T\]\):org.apache.spark.rdd.RDD\[T\] "Permalink") def ++(other: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]
Return the union of this RDD and another one.
Return the union of this RDD and another one. Any identical elements will appear multiple times (use `.distinct()` to eliminate them).  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#aggregate\[U\]\(zeroValue:U\)\(seqOp:\(U,T\)=>U,combOp:\(U,U\)=>U\)\(implicitevidence$33:scala.reflect.ClassTag\[U\]\):U "Permalink") def aggregate[U](zeroValue: U)(seqOp: (U, ([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)) => U, combOp: (U, U) => U)(implicit arg0: ClassTag[U]): U
Aggregate the elements of each partition, and then the results for all the partitions, using given combine functions and a neutral "zero value".
Aggregate the elements of each partition, and then the results for all the partitions, using given combine functions and a neutral "zero value". This function can return a different result type, U, than the type of this RDD, T. Thus, we need one operation for merging a T into an U and one operation for merging two U's, as in scala.IterableOnce. Both of these functions are allowed to modify and return their first argument instead of creating a new U to avoid memory allocation.  

zeroValue
    
the initial value for the accumulated result of each partition for the `seqOp` operator, and also the initial value for the combine results from different partitions for the `combOp` operator - this will typically be the neutral element (e.g. `Nil` for list concatenation or `0` for summation) 

seqOp
    
an operator used to accumulate results within a partition 

combOp
    
an associative operator used to combine results from different partitions 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#barrier\(\):org.apache.spark.rdd.RDDBarrier\[T\] "Permalink") def barrier(): [RDDBarrier](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDDBarrier.html "org.apache.spark.rdd.RDDBarrier")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]
Marks the current stage as a barrier stage, where Spark must launch all tasks together.
Marks the current stage as a barrier stage, where Spark must launch all tasks together. In case of a task failure, instead of only restarting the failed task, Spark will abort the entire stage and re-launch all tasks for this stage. The barrier execution mode feature is experimental and it only handles limited scenarios. Please read the linked SPIP and design docs to understand the limitations and future plans. 

returns
    
an RDDBarrier instance that provides actions within a barrier stage 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Annotations
     @Experimental() @Since("2.4.0") 

See also
    
[org.apache.spark.BarrierTaskContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/BarrierTaskContext.html "org.apache.spark.BarrierTaskContext")
[ SPIP: Barrier Execution Mode](https://issues.apache.org/jira/browse/SPARK-24374)
[Design Doc](https://issues.apache.org/jira/browse/SPARK-24582)
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#cache\(\):RDD.this.type "Permalink") def cache(): [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "org.apache.spark.graphx.VertexRDD").this.type
Persist this RDD with the default storage level (`MEMORY_ONLY`).
Persist this RDD with the default storage level (`MEMORY_ONLY`).  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#cartesian\[U\]\(other:org.apache.spark.rdd.RDD\[U\]\)\(implicitevidence$5:scala.reflect.ClassTag\[U\]\):org.apache.spark.rdd.RDD\[\(T,U\)\] "Permalink") def cartesian[U](other: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[U])(implicit arg0: ClassTag[U]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD), U)]
Return the Cartesian product of this RDD and another one, that is, the RDD of all pairs of elements (a, b) where a is in `this` and b is in `other`.
Return the Cartesian product of this RDD and another one, that is, the RDD of all pairs of elements (a, b) where a is in `this` and b is in `other`.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#checkpoint\(\):Unit "Permalink") def checkpoint(): Unit
Mark this RDD for checkpointing.
Mark this RDD for checkpointing. It will be saved to a file inside the checkpoint directory set with `SparkContext#setCheckpointDir` and all references to its parent RDDs will be removed. This function must be called before any job has been executed on this RDD. It is strongly recommended that this RDD is persisted in memory, otherwise saving it on a file will require recomputation.
The data is only checkpointed when `doCheckpoint()` is called, and this only happens at the end of the first action execution on this RDD. The final data that is checkpointed after the first action may be different from the data that was used during the action, due to non-determinism of the underlying operation and retries. If the purpose of the checkpoint is to achieve saving a deterministic snapshot of the data, an eager action may need to be called first on the RDD to trigger the checkpoint.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#cleanShuffleDependencies\(blocking:Boolean\):Unit "Permalink") def cleanShuffleDependencies(blocking: Boolean = false): Unit
Removes an RDD's shuffles and it's non-persisted ancestors.
Removes an RDD's shuffles and it's non-persisted ancestors. When running without a shuffle service, cleaning up shuffle files enables downscaling. If you use the RDD after this call, you should checkpoint and materialize it first. If you are uncertain of what you are doing, please do not use this feature. Additional techniques for mitigating orphaned shuffle files: * Tuning the driver GC to be more aggressive, so the regular context cleaner is triggered * Setting an appropriate TTL for shuffle files to be auto cleaned  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Annotations
     @DeveloperApi() @Since("3.1.0")
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#clearDependencies\(\):Unit "Permalink") def clearDependencies(): Unit
Clears the dependencies of this RDD.
Clears the dependencies of this RDD. This method must ensure that all references to the original parent RDDs are removed to enable the parent RDDs to be garbage collected. Subclasses of RDD may override this method for implementing their own cleaning logic. See [org.apache.spark.rdd.UnionRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/UnionRDD.html "org.apache.spark.rdd.UnionRDD") for an example.  

Attributes
    protected  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#coalesce\(numPartitions:Int,shuffle:Boolean,partitionCoalescer:Option\[org.apache.spark.rdd.PartitionCoalescer\]\)\(implicitord:Ordering\[T\]\):org.apache.spark.rdd.RDD\[T\] "Permalink") def coalesce(numPartitions: Int, shuffle: Boolean = false, partitionCoalescer: Option[[PartitionCoalescer](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PartitionCoalescer.html "org.apache.spark.rdd.PartitionCoalescer")] = Option.empty)(implicit ord: Ordering[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)] = null): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]
Return a new RDD that is reduced into `numPartitions` partitions.
Return a new RDD that is reduced into `numPartitions` partitions.
This results in a narrow dependency, e.g. if you go from 1000 partitions to 100 partitions, there will not be a shuffle, instead each of the 100 new partitions will claim 10 of the current partitions. If a larger number of partitions is requested, it will stay at the current number of partitions.
However, if you're doing a drastic coalesce, e.g. to numPartitions = 1, this may result in your computation taking place on fewer nodes than you like (e.g. one node in the case of numPartitions = 1). To avoid this, you can pass shuffle = true. This will add a shuffle step, but means the current upstream partitions will be executed in parallel (per whatever the current partitioning is).  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Note
    
With shuffle = true, you can actually coalesce to a larger number of partitions. This is useful if you have a small number of partitions, say 100, potentially with a few partitions being abnormally large. Calling coalesce(1000, shuffle = true) will result in 1000 partitions with the data distributed using a hash partitioner. The optional partition coalescer passed in must be serializable.
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#collect\[U\]\(f:PartialFunction\[T,U\]\)\(implicitevidence$32:scala.reflect.ClassTag\[U\]\):org.apache.spark.rdd.RDD\[U\] "Permalink") def collect[U](f: PartialFunction[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD), U])(implicit arg0: ClassTag[U]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[U]
Return an RDD that contains all matching values by applying `f`.
Return an RDD that contains all matching values by applying `f`.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#collect\(\):Array\[T\] "Permalink") def collect(): Array[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]
Return an array that contains all of the elements in this RDD.
Return an array that contains all of the elements in this RDD.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Note
    
This method should only be used if the resulting array is expected to be small, as all the data is loaded into the driver's memory.
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#context:org.apache.spark.SparkContext "Permalink") def context: [SparkContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html "org.apache.spark.SparkContext")
The [org.apache.spark.SparkContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html "org.apache.spark.SparkContext") that this RDD was created on.
The [org.apache.spark.SparkContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html "org.apache.spark.SparkContext") that this RDD was created on. 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#count\(\):Long "Permalink") def count(): Long
Return the number of elements in the RDD.
Return the number of elements in the RDD.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#countApprox\(timeout:Long,confidence:Double\):org.apache.spark.partial.PartialResult\[org.apache.spark.partial.BoundedDouble\] "Permalink") def countApprox(timeout: Long, confidence: Double = 0.95): [PartialResult](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/partial/PartialResult.html "org.apache.spark.partial.PartialResult")[[BoundedDouble](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/partial/BoundedDouble.html "org.apache.spark.partial.BoundedDouble")]
Approximate version of count() that returns a potentially incomplete result within a timeout, even if not all tasks have finished.
Approximate version of count() that returns a potentially incomplete result within a timeout, even if not all tasks have finished.
The confidence is the probability that the error bounds of the result will contain the true value. That is, if countApprox were called repeatedly with confidence 0.9, we would expect 90% of the results to contain the true count. The confidence must be in the range [0,1] or an exception will be thrown.  

timeout
    
maximum time to wait for the job, in milliseconds 

confidence
    
the desired statistical confidence in the result 

returns
    
a potentially incomplete result, with error bounds 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#countApproxDistinct\(relativeSD:Double\):Long "Permalink") def countApproxDistinct(relativeSD: Double = 0.05): Long
Return approximate number of distinct elements in the RDD.
Return approximate number of distinct elements in the RDD.
The algorithm used is based on streamlib's implementation of "HyperLogLog in Practice: Algorithmic Engineering of a State of The Art Cardinality Estimation Algorithm", available [here](https://doi.org/10.1145/2452376.2452456).  

relativeSD
    
Relative accuracy. Smaller values create counters that require more space. It must be greater than 0.000017. 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#countApproxDistinct\(p:Int,sp:Int\):Long "Permalink") def countApproxDistinct(p: Int, sp: Int): Long
Return approximate number of distinct elements in the RDD.
Return approximate number of distinct elements in the RDD.
The algorithm used is based on streamlib's implementation of "HyperLogLog in Practice: Algorithmic Engineering of a State of The Art Cardinality Estimation Algorithm", available [here](https://doi.org/10.1145/2452376.2452456).
The relative accuracy is approximately `1.054 / sqrt(2^p)`. Setting a nonzero (`sp` is greater than `p`) would trigger sparse representation of registers, which may reduce the memory consumption and increase accuracy when the cardinality is small. `` 

p
    
The precision value for the normal set. `p` must be a value between 4 and `sp` if `sp` is not zero (32 max). 

sp
    
The precision value for the sparse set, between 0 and 32. If `sp` equals 0, the sparse representation is skipped. 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#countByValue\(\)\(implicitord:Ordering\[T\]\):scala.collection.Map\[T,Long\] "Permalink") def countByValue()(implicit ord: Ordering[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)] = null): Map[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD), Long]
Return the count of each unique value in this RDD as a local map of (value, count) pairs.
Return the count of each unique value in this RDD as a local map of (value, count) pairs.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Note
    
This method should only be used if the resulting map is expected to be small, as the whole thing is loaded into the driver's memory. To handle very large results, consider using

```
rdd.map(x => (x, 1L)).reduceByKey(_ + _)
```

, which returns an RDD[T, Long] instead of a map.
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#countByValueApprox\(timeout:Long,confidence:Double\)\(implicitord:Ordering\[T\]\):org.apache.spark.partial.PartialResult\[scala.collection.Map\[T,org.apache.spark.partial.BoundedDouble\]\] "Permalink") def countByValueApprox(timeout: Long, confidence: Double = 0.95)(implicit ord: Ordering[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)] = null): [PartialResult](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/partial/PartialResult.html "org.apache.spark.partial.PartialResult")[Map[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD), [BoundedDouble](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/partial/BoundedDouble.html "org.apache.spark.partial.BoundedDouble")]]
Approximate version of countByValue().
Approximate version of countByValue().  

timeout
    
maximum time to wait for the job, in milliseconds 

confidence
    
the desired statistical confidence in the result 

returns
    
a potentially incomplete result, with error bounds 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#dependencies:Seq\[org.apache.spark.Dependency\[_\]\] "Permalink") final  def dependencies: Seq[[Dependency](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Dependency.html "org.apache.spark.Dependency")[_]]
Get the list of dependencies of this RDD, taking into account whether the RDD is checkpointed or not.
Get the list of dependencies of this RDD, taking into account whether the RDD is checkpointed or not.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#distinct\(\):org.apache.spark.rdd.RDD\[T\] "Permalink") def distinct(): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]
Return a new RDD containing the distinct elements in this RDD.
Return a new RDD containing the distinct elements in this RDD.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#distinct\(numPartitions:Int\)\(implicitord:Ordering\[T\]\):org.apache.spark.rdd.RDD\[T\] "Permalink") def distinct(numPartitions: Int)(implicit ord: Ordering[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)] = null): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]
Return a new RDD containing the distinct elements in this RDD.
Return a new RDD containing the distinct elements in this RDD.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#first\(\):T "Permalink") def first(): ([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)
Return the first element in this RDD.
Return the first element in this RDD.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  23. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#firstParent\[U\]\(implicitevidence$36:scala.reflect.ClassTag\[U\]\):org.apache.spark.rdd.RDD\[U\] "Permalink") def firstParent[U](implicit arg0: ClassTag[U]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[U]
Returns the first parent RDD
Returns the first parent RDD 

Attributes
    protected[[spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")]  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  24. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#flatMap\[U\]\(f:T=>IterableOnce\[U\]\)\(implicitevidence$4:scala.reflect.ClassTag\[U\]\):org.apache.spark.rdd.RDD\[U\] "Permalink") def flatMap[U](f: (([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)) => IterableOnce[U])(implicit arg0: ClassTag[U]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[U]
Return a new RDD by first applying a function to all elements of this RDD, and then flattening the results.
Return a new RDD by first applying a function to all elements of this RDD, and then flattening the results.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  25. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#fold\(zeroValue:T\)\(op:\(T,T\)=>T\):T "Permalink") def fold(zeroValue: ([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD))(op: (([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD), ([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)) => ([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)): ([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)
Aggregate the elements of each partition, and then the results for all the partitions, using a given associative function and a neutral "zero value".
Aggregate the elements of each partition, and then the results for all the partitions, using a given associative function and a neutral "zero value". The function op(t1, t2) is allowed to modify t1 and return it as its result value to avoid object allocation; however, it should not modify t2.
This behaves somewhat differently from fold operations implemented for non-distributed collections in functional languages like Scala. This fold operation may be applied to partitions individually, and then fold those results into the final result, rather than apply the fold to each element sequentially in some defined ordering. For functions that are not commutative, the result may differ from that of a fold applied to a non-distributed collection.  

zeroValue
    
the initial value for the accumulated result of each partition for the `op` operator, and also the initial value for the combine results from different partitions for the `op` operator - this will typically be the neutral element (e.g. `Nil` for list concatenation or `0` for summation) 

op
    
an operator used to both accumulate results within a partition and combine results from different partitions 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  26. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#foreach\(f:T=>Unit\):Unit "Permalink") def foreach(f: (([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)) => Unit): Unit
Applies a function f to all elements of this RDD.
Applies a function f to all elements of this RDD.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  27. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#foreachPartition\(f:Iterator\[T\]=>Unit\):Unit "Permalink") def foreachPartition(f: (Iterator[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]) => Unit): Unit
Applies a function f to each partition of this RDD.
Applies a function f to each partition of this RDD.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  28. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#getCheckpointFile:Option\[String\] "Permalink") def getCheckpointFile: Option[String]
Gets the name of the directory to which this RDD was checkpointed.
Gets the name of the directory to which this RDD was checkpointed. This is not defined if the RDD is checkpointed locally.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  29. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#getDependencies:Seq\[org.apache.spark.Dependency\[_\]\] "Permalink") def getDependencies: Seq[[Dependency](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Dependency.html "org.apache.spark.Dependency")[_]]
Implemented by subclasses to return how this RDD depends on parent RDDs.
Implemented by subclasses to return how this RDD depends on parent RDDs. This method will only be called once, so it is safe to implement a time-consuming computation in it.  

Attributes
    protected  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  30. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#getNumPartitions:Int "Permalink") final  def getNumPartitions: Int
Returns the number of partitions of this RDD.
Returns the number of partitions of this RDD.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Annotations
     @Since("1.6.0")
  31. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#getOutputDeterministicLevel:org.apache.spark.rdd.DeterministicLevel.Value "Permalink") def getOutputDeterministicLevel: [rdd.DeterministicLevel.Value](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/DeterministicLevel$.html#ValueextendsOrdered\[Enumeration.this.Value\]withSerializable) 

Attributes
    protected  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Annotations
     @DeveloperApi()
  32. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#getPreferredLocations\(split:org.apache.spark.Partition\):Seq\[String\] "Permalink") def getPreferredLocations(split: [Partition](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partition.html "org.apache.spark.Partition")): Seq[String]
Optionally overridden by subclasses to specify placement preferences.
Optionally overridden by subclasses to specify placement preferences.  

Attributes
    protected  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  33. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#getResourceProfile\(\):org.apache.spark.resource.ResourceProfile "Permalink") def getResourceProfile(): [ResourceProfile](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/resource/ResourceProfile.html "org.apache.spark.resource.ResourceProfile")
Get the ResourceProfile specified with this RDD or null if it wasn't specified.
Get the ResourceProfile specified with this RDD or null if it wasn't specified. 

returns
    
the user specified ResourceProfile or null (for Java compatibility) if none was specified 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Annotations
     @Experimental() @Since("3.1.0")
  34. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#getStorageLevel:org.apache.spark.storage.StorageLevel "Permalink") def getStorageLevel: [StorageLevel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StorageLevel.html "org.apache.spark.storage.StorageLevel")
Get the RDD's current storage level, or StorageLevel.NONE if none is set.
Get the RDD's current storage level, or StorageLevel.NONE if none is set. 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  35. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#glom\(\):org.apache.spark.rdd.RDD\[Array\[T\]\] "Permalink") def glom(): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[Array[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]]
Return an RDD created by coalescing all elements within each partition into an array.
Return an RDD created by coalescing all elements within each partition into an array.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  36. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#groupBy\[K\]\(f:T=>K,p:org.apache.spark.Partitioner\)\(implicitkt:scala.reflect.ClassTag\[K\],implicitord:Ordering\[K\]\):org.apache.spark.rdd.RDD\[\(K,Iterable\[T\]\)\] "Permalink") def groupBy[K](f: (([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)) => K, p: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner"))(implicit kt: ClassTag[K], ord: Ordering[K] = null): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, Iterable[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)])]
Return an RDD of grouped items.
Return an RDD of grouped items. Each group consists of a key and a sequence of elements mapping to that key. The ordering of elements within each group is not guaranteed, and may even differ each time the resulting RDD is evaluated.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Note
    
This operation may be very expensive. If you are grouping in order to perform an aggregation (such as a sum or average) over each key, using `PairRDDFunctions.aggregateByKey` or `PairRDDFunctions.reduceByKey` will provide much better performance.
  37. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#groupBy\[K\]\(f:T=>K,numPartitions:Int\)\(implicitkt:scala.reflect.ClassTag\[K\]\):org.apache.spark.rdd.RDD\[\(K,Iterable\[T\]\)\] "Permalink") def groupBy[K](f: (([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)) => K, numPartitions: Int)(implicit kt: ClassTag[K]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, Iterable[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)])]
Return an RDD of grouped elements.
Return an RDD of grouped elements. Each group consists of a key and a sequence of elements mapping to that key. The ordering of elements within each group is not guaranteed, and may even differ each time the resulting RDD is evaluated.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Note
    
This operation may be very expensive. If you are grouping in order to perform an aggregation (such as a sum or average) over each key, using `PairRDDFunctions.aggregateByKey` or `PairRDDFunctions.reduceByKey` will provide much better performance.
  38. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#groupBy\[K\]\(f:T=>K\)\(implicitkt:scala.reflect.ClassTag\[K\]\):org.apache.spark.rdd.RDD\[\(K,Iterable\[T\]\)\] "Permalink") def groupBy[K](f: (([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)) => K)(implicit kt: ClassTag[K]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, Iterable[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)])]
Return an RDD of grouped items.
Return an RDD of grouped items. Each group consists of a key and a sequence of elements mapping to that key. The ordering of elements within each group is not guaranteed, and may even differ each time the resulting RDD is evaluated.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Note
    
This operation may be very expensive. If you are grouping in order to perform an aggregation (such as a sum or average) over each key, using `PairRDDFunctions.aggregateByKey` or `PairRDDFunctions.reduceByKey` will provide much better performance.
  39. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#id:Int "Permalink") val id: Int
A unique ID for this RDD (within its SparkContext).
A unique ID for this RDD (within its SparkContext). 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  40. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#intersection\(other:org.apache.spark.rdd.RDD\[T\],numPartitions:Int\):org.apache.spark.rdd.RDD\[T\] "Permalink") def intersection(other: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)], numPartitions: Int): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]
Return the intersection of this RDD and another one.
Return the intersection of this RDD and another one. The output will not contain any duplicate elements, even if the input RDDs did. Performs a hash partition across the cluster  

numPartitions
    
How many partitions to use in the resulting RDD 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Note
    
This method performs a shuffle internally.
  41. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#intersection\(other:org.apache.spark.rdd.RDD\[T\],partitioner:org.apache.spark.Partitioner\)\(implicitord:Ordering\[T\]\):org.apache.spark.rdd.RDD\[T\] "Permalink") def intersection(other: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)], partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner"))(implicit ord: Ordering[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)] = null): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]
Return the intersection of this RDD and another one.
Return the intersection of this RDD and another one. The output will not contain any duplicate elements, even if the input RDDs did.  

partitioner
    
Partitioner to use for the resulting RDD 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Note
    
This method performs a shuffle internally.
  42. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#intersection\(other:org.apache.spark.rdd.RDD\[T\]\):org.apache.spark.rdd.RDD\[T\] "Permalink") def intersection(other: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]
Return the intersection of this RDD and another one.
Return the intersection of this RDD and another one. The output will not contain any duplicate elements, even if the input RDDs did.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Note
    
This method performs a shuffle internally.
  43. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#isBarrier_:Boolean "Permalink") lazy val isBarrier_: Boolean 

Attributes
    protected  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Annotations
     @transient()
  44. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#isCheckpointed:Boolean "Permalink") def isCheckpointed: Boolean
Return whether this RDD is checkpointed and materialized, either reliably or locally.
Return whether this RDD is checkpointed and materialized, either reliably or locally.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  45. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#isEmpty\(\):Boolean "Permalink") def isEmpty(): Boolean 

returns
    
true if and only if the RDD contains no elements at all. Note that an RDD may be empty even when it has at least 1 partition. 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Note
    
Due to complications in the internal implementation, this method will raise an exception if called on an RDD of `Nothing` or `Null`. This may be come up in practice because, for example, the type of `parallelize(Seq())` is `RDD[Nothing]`. (`parallelize(Seq())` should be avoided anyway in favor of `parallelize(Seq[T]())`.)
  46. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#iterator\(split:org.apache.spark.Partition,context:org.apache.spark.TaskContext\):Iterator\[T\] "Permalink") final  def iterator(split: [Partition](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partition.html "org.apache.spark.Partition"), context: [TaskContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskContext.html "org.apache.spark.TaskContext")): Iterator[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]
Internal method to this RDD; will read from cache if applicable, or otherwise compute it.
Internal method to this RDD; will read from cache if applicable, or otherwise compute it. This should _not_ be called by users directly, but is available for implementers of custom subclasses of RDD.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  47. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#keyBy\[K\]\(f:T=>K\):org.apache.spark.rdd.RDD\[\(K,T\)\] "Permalink") def keyBy[K](f: (([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)) => K): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, ([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD))]
Creates tuples of the elements in this RDD by applying `f`.
Creates tuples of the elements in this RDD by applying `f`.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  48. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#localCheckpoint\(\):RDD.this.type "Permalink") def localCheckpoint(): [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "org.apache.spark.graphx.VertexRDD").this.type
Mark this RDD for local checkpointing using Spark's existing caching layer.
Mark this RDD for local checkpointing using Spark's existing caching layer.
This method is for users who wish to truncate RDD lineages while skipping the expensive step of replicating the materialized data in a reliable distributed file system. This is useful for RDDs with long lineages that need to be truncated periodically (e.g. GraphX).
Local checkpointing sacrifices fault-tolerance for performance. In particular, checkpointed data is written to ephemeral local storage in the executors instead of to a reliable, fault-tolerant storage. The effect is that if an executor fails during the computation, the checkpointed data may no longer be accessible, causing an irrecoverable job failure.
This is NOT safe to use with dynamic allocation, which removes executors along with their cached blocks. If you must use both features, you are advised to set `spark.dynamicAllocation.cachedExecutorIdleTimeout` to a high value.
The checkpoint directory set through `SparkContext#setCheckpointDir` is not used.
The data is only checkpointed when `doCheckpoint()` is called, and this only happens at the end of the first action execution on this RDD. The final data that is checkpointed after the first action may be different from the data that was used during the action, due to non-determinism of the underlying operation and retries. If the purpose of the checkpoint is to achieve saving a deterministic snapshot of the data, an eager action may need to be called first on the RDD to trigger the checkpoint.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  49. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#map\[U\]\(f:T=>U\)\(implicitevidence$3:scala.reflect.ClassTag\[U\]\):org.apache.spark.rdd.RDD\[U\] "Permalink") def map[U](f: (([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)) => U)(implicit arg0: ClassTag[U]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[U]
Return a new RDD by applying a function to all elements of this RDD.
Return a new RDD by applying a function to all elements of this RDD.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  50. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#mapPartitions\[U\]\(f:Iterator\[T\]=>Iterator\[U\],preservesPartitioning:Boolean\)\(implicitevidence$6:scala.reflect.ClassTag\[U\]\):org.apache.spark.rdd.RDD\[U\] "Permalink") def mapPartitions[U](f: (Iterator[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]) => Iterator[U], preservesPartitioning: Boolean = false)(implicit arg0: ClassTag[U]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[U]
Return a new RDD by applying a function to each partition of this RDD.
Return a new RDD by applying a function to each partition of this RDD.
`preservesPartitioning` indicates whether the input function preserves the partitioner, which should be `false` unless this is a pair RDD and the input function doesn't modify the keys.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  51. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#mapPartitionsWithEvaluator\[U\]\(evaluatorFactory:org.apache.spark.PartitionEvaluatorFactory\[T,U\]\)\(implicitevidence$10:scala.reflect.ClassTag\[U\]\):org.apache.spark.rdd.RDD\[U\] "Permalink") def mapPartitionsWithEvaluator[U](evaluatorFactory: [PartitionEvaluatorFactory](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/PartitionEvaluatorFactory.html "org.apache.spark.PartitionEvaluatorFactory")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD), U])(implicit arg0: ClassTag[U]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[U]
Return a new RDD by applying an evaluator to each partition of this RDD.
Return a new RDD by applying an evaluator to each partition of this RDD. The given evaluator factory will be serialized and sent to executors, and each task will create an evaluator with the factory, and use the evaluator to transform the data of the input partition.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Annotations
     @DeveloperApi() @Since("3.5.0")
  52. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#mapPartitionsWithIndex\[U\]\(f:\(Int,Iterator\[T\]\)=>Iterator\[U\],preservesPartitioning:Boolean\)\(implicitevidence$9:scala.reflect.ClassTag\[U\]\):org.apache.spark.rdd.RDD\[U\] "Permalink") def mapPartitionsWithIndex[U](f: (Int, Iterator[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]) => Iterator[U], preservesPartitioning: Boolean = false)(implicit arg0: ClassTag[U]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[U]
Return a new RDD by applying a function to each partition of this RDD, while tracking the index of the original partition.
Return a new RDD by applying a function to each partition of this RDD, while tracking the index of the original partition.
`preservesPartitioning` indicates whether the input function preserves the partitioner, which should be `false` unless this is a pair RDD and the input function doesn't modify the keys.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  53. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#max\(\)\(implicitord:Ordering\[T\]\):T "Permalink") def max()(implicit ord: Ordering[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]): ([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)
Returns the max of this RDD as defined by the implicit Ordering[T].
Returns the max of this RDD as defined by the implicit Ordering[T]. 

returns
    
the maximum element of the RDD 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  54. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#min\(\)\(implicitord:Ordering\[T\]\):T "Permalink") def min()(implicit ord: Ordering[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]): ([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)
Returns the min of this RDD as defined by the implicit Ordering[T].
Returns the min of this RDD as defined by the implicit Ordering[T]. 

returns
    
the minimum element of the RDD 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  55. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#name:String "Permalink") var name: String
A friendly name for this RDD
A friendly name for this RDD 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  56. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#parent\[U\]\(j:Int\)\(implicitevidence$37:scala.reflect.ClassTag\[U\]\):org.apache.spark.rdd.RDD\[U\] "Permalink") def parent[U](j: Int)(implicit arg0: ClassTag[U]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[U]
Returns the jth parent RDD: e.g.
Returns the jth parent RDD: e.g. rdd.parent[T](0) is equivalent to rdd.firstParent[T] 

Attributes
    protected[[spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")]  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  57. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#partitioner:Option\[org.apache.spark.Partitioner\] "Permalink") val partitioner: Option[[Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner")]
Optionally overridden by subclasses to specify how they are partitioned.
Optionally overridden by subclasses to specify how they are partitioned. 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  58. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#partitions:Array\[org.apache.spark.Partition\] "Permalink") final  def partitions: Array[[Partition](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partition.html "org.apache.spark.Partition")]
Get the array of partitions of this RDD, taking into account whether the RDD is checkpointed or not.
Get the array of partitions of this RDD, taking into account whether the RDD is checkpointed or not.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  59. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#persist\(\):RDD.this.type "Permalink") def persist(): [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "org.apache.spark.graphx.VertexRDD").this.type
Persist this RDD with the default storage level (`MEMORY_ONLY`).
Persist this RDD with the default storage level (`MEMORY_ONLY`).  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  60. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#persist\(newLevel:org.apache.spark.storage.StorageLevel\):RDD.this.type "Permalink") def persist(newLevel: [StorageLevel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StorageLevel.html "org.apache.spark.storage.StorageLevel")): [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "org.apache.spark.graphx.VertexRDD").this.type
Set this RDD's storage level to persist its values across operations after the first time it is computed.
Set this RDD's storage level to persist its values across operations after the first time it is computed. This can only be used to assign a new storage level if the RDD does not have a storage level set yet. Local checkpointing is an exception.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  61. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#pipe\(command:Seq\[String\],env:scala.collection.Map\[String,String\],printPipeContext:\(String=>Unit\)=>Unit,printRDDElement:\(T,String=>Unit\)=>Unit,separateWorkingDir:Boolean,bufferSize:Int,encoding:String\):org.apache.spark.rdd.RDD\[String\] "Permalink") def pipe(command: Seq[String], env: Map[String, String] = Map(), printPipeContext: ((String) => Unit) => Unit = null, printRDDElement: (([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD), (String) => Unit) => Unit = null, separateWorkingDir: Boolean = false, bufferSize: Int = 8192, encoding: String = Codec.defaultCharsetCodec.name): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[String]
Return an RDD created by piping elements to a forked external process.
Return an RDD created by piping elements to a forked external process. The resulting RDD is computed by executing the given process once per partition. All elements of each input partition are written to a process's stdin as lines of input separated by a newline. The resulting partition consists of the process's stdout output, with each line of stdout resulting in one element of the output partition. A process is invoked even for empty partitions.
The print behavior can be customized by providing two functions.  

command
    
command to run in forked process. 

env
    
environment variables to set. 

printPipeContext
    
Before piping elements, this function is called as an opportunity to pipe context data. Print line function (like out.println) will be passed as printPipeContext's parameter. 

printRDDElement
    
Use this function to customize how to pipe elements. This function will be called with each RDD element as the 1st parameter, and the print line function (like out.println()) as the 2nd parameter. An example of pipe the RDD data of groupBy() in a streaming way, instead of constructing a huge String to concat all the elements:

```
def printRDDElement(record:(String, Seq[String]), f:String=>Unit) =
  for (e <- record._2) {f(e)}
```


separateWorkingDir
    
Use separate working directories for each task. 

bufferSize
    
Buffer size for the stdin writer for the piped process. 

encoding
    
Char encoding used for interacting (via stdin, stdout and stderr) with the piped process 

returns
    
the result RDD 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  62. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#pipe\(command:String,env:scala.collection.Map\[String,String\]\):org.apache.spark.rdd.RDD\[String\] "Permalink") def pipe(command: String, env: Map[String, String]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[String]
Return an RDD created by piping elements to a forked external process.
Return an RDD created by piping elements to a forked external process.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  63. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#pipe\(command:String\):org.apache.spark.rdd.RDD\[String\] "Permalink") def pipe(command: String): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[String]
Return an RDD created by piping elements to a forked external process.
Return an RDD created by piping elements to a forked external process.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  64. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#preferredLocations\(split:org.apache.spark.Partition\):Seq\[String\] "Permalink") final  def preferredLocations(split: [Partition](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partition.html "org.apache.spark.Partition")): Seq[String]
Get the preferred locations of a partition, taking into account whether the RDD is checkpointed.
Get the preferred locations of a partition, taking into account whether the RDD is checkpointed.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  65. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#randomSplit\(weights:Array\[Double\],seed:Long\):Array\[org.apache.spark.rdd.RDD\[T\]\] "Permalink") def randomSplit(weights: Array[Double], seed: Long = [Utils.random.nextLong](https://spark.apache.org/docs/latest/api/scala/org/index.html)): Array[[RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]]
Randomly splits this RDD with the provided weights.
Randomly splits this RDD with the provided weights.  

weights
    
weights for splits, will be normalized if they don't sum to 1 

seed
    
random seed 

returns
    
split RDDs in an array 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  66. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#reduce\(f:\(T,T\)=>T\):T "Permalink") def reduce(f: (([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD), ([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)) => ([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)): ([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)
Reduces the elements of this RDD using the specified commutative and associative binary operator.
Reduces the elements of this RDD using the specified commutative and associative binary operator.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  67. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#repartition\(numPartitions:Int\)\(implicitord:Ordering\[T\]\):org.apache.spark.rdd.RDD\[T\] "Permalink") def repartition(numPartitions: Int)(implicit ord: Ordering[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)] = null): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]
Return a new RDD that has exactly numPartitions partitions.
Return a new RDD that has exactly numPartitions partitions.
Can increase or decrease the level of parallelism in this RDD. Internally, this uses a shuffle to redistribute data.
If you are decreasing the number of partitions in this RDD, consider using `coalesce`, which can avoid performing a shuffle.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  68. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#sample\(withReplacement:Boolean,fraction:Double,seed:Long\):org.apache.spark.rdd.RDD\[T\] "Permalink") def sample(withReplacement: Boolean, fraction: Double, seed: Long = [Utils.random.nextLong](https://spark.apache.org/docs/latest/api/scala/org/index.html)): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]
Return a sampled subset of this RDD.
Return a sampled subset of this RDD.  

withReplacement
    
can elements be sampled multiple times (replaced when sampled out) 

fraction
    
expected size of the sample as a fraction of this RDD's size without replacement: probability that each element is chosen; fraction must be [0, 1] with replacement: expected number of times each element is chosen; fraction must be greater than or equal to 0 

seed
    
seed for the random number generator 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Note
    
This is NOT guaranteed to provide exactly the fraction of the count of the given RDD.
  69. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#saveAsObjectFile\(path:String\):Unit "Permalink") def saveAsObjectFile(path: String): Unit
Save this RDD as a SequenceFile of serialized objects.
Save this RDD as a SequenceFile of serialized objects.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  70. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#saveAsTextFile\(path:String,codec:Class\[_<:org.apache.hadoop.io.compress.CompressionCodec\]\):Unit "Permalink") def saveAsTextFile(path: String, codec: Class[_ <: CompressionCodec]): Unit
Save this RDD as a compressed text file, using string representations of elements.
Save this RDD as a compressed text file, using string representations of elements.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  71. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#saveAsTextFile\(path:String\):Unit "Permalink") def saveAsTextFile(path: String): Unit
Save this RDD as a text file, using string representations of elements.
Save this RDD as a text file, using string representations of elements.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  72. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#setName\(_name:String\):RDD.this.type "Permalink") def setName(_name: String): [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "org.apache.spark.graphx.VertexRDD").this.type
Assign a name to this RDD
Assign a name to this RDD 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  73. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#sortBy\[K\]\(f:T=>K,ascending:Boolean,numPartitions:Int\)\(implicitord:Ordering\[K\],implicitctag:scala.reflect.ClassTag\[K\]\):org.apache.spark.rdd.RDD\[T\] "Permalink") def sortBy[K](f: (([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)) => K, ascending: Boolean = true, numPartitions: Int = [this.partitions.length](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html#partitions:Array\[org.apache.spark.Partition\]))(implicit ord: Ordering[K], ctag: ClassTag[K]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]
Return this RDD sorted by the given key function.
Return this RDD sorted by the given key function.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  74. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#sparkContext:org.apache.spark.SparkContext "Permalink") def sparkContext: [SparkContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html "org.apache.spark.SparkContext")
The SparkContext that created this RDD.
The SparkContext that created this RDD. 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  75. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#subtract\(other:org.apache.spark.rdd.RDD\[T\],p:org.apache.spark.Partitioner\)\(implicitord:Ordering\[T\]\):org.apache.spark.rdd.RDD\[T\] "Permalink") def subtract(other: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)], p: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner"))(implicit ord: Ordering[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)] = null): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]
Return an RDD with the elements from `this` that are not in `other`.
Return an RDD with the elements from `this` that are not in `other`.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  76. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#subtract\(other:org.apache.spark.rdd.RDD\[T\],numPartitions:Int\):org.apache.spark.rdd.RDD\[T\] "Permalink") def subtract(other: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)], numPartitions: Int): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]
Return an RDD with the elements from `this` that are not in `other`.
Return an RDD with the elements from `this` that are not in `other`.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  77. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#subtract\(other:org.apache.spark.rdd.RDD\[T\]\):org.apache.spark.rdd.RDD\[T\] "Permalink") def subtract(other: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]
Return an RDD with the elements from `this` that are not in `other`.
Return an RDD with the elements from `this` that are not in `other`.
Uses `this` partitioner/partition size, because even if `other` is huge, the resulting RDD will be <= us.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  78. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#take\(num:Int\):Array\[T\] "Permalink") def take(num: Int): Array[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]
Take the first num elements of the RDD.
Take the first num elements of the RDD. It works by first scanning one partition, and use the results from that partition to estimate the number of additional partitions needed to satisfy the limit.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Note
    
This method should only be used if the resulting array is expected to be small, as all the data is loaded into the driver's memory.
, 
Due to complications in the internal implementation, this method will raise an exception if called on an RDD of `Nothing` or `Null`.
  79. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#takeOrdered\(num:Int\)\(implicitord:Ordering\[T\]\):Array\[T\] "Permalink") def takeOrdered(num: Int)(implicit ord: Ordering[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]): Array[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]
Returns the first k (smallest) elements from this RDD as defined by the specified implicit Ordering[T] and maintains the ordering.
Returns the first k (smallest) elements from this RDD as defined by the specified implicit Ordering[T] and maintains the ordering. This does the opposite of [top](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#top\(num:Int\)\(implicitord:Ordering\[T\]\):Array\[T\]). For example:

```
sc.parallelize(Seq(10, 4, 2, 12, 3)).takeOrdered(1)
// returns Array(2)

sc.parallelize(Seq(2, 3, 4, 5, 6)).takeOrdered(2)
// returns Array(2, 3)
```


num
    
k, the number of elements to return 

ord
    
the implicit ordering for T 

returns
    
an array of top elements 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Note
    
This method should only be used if the resulting array is expected to be small, as all the data is loaded into the driver's memory.
  80. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#takeSample\(withReplacement:Boolean,num:Int,seed:Long\):Array\[T\] "Permalink") def takeSample(withReplacement: Boolean, num: Int, seed: Long = [Utils.random.nextLong](https://spark.apache.org/docs/latest/api/scala/org/index.html)): Array[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]
Return a fixed-size sampled subset of this RDD in an array 
Return a fixed-size sampled subset of this RDD in an array  

withReplacement
    
whether sampling is done with replacement 

num
    
size of the returned sample 

seed
    
seed for the random number generator 

returns
    
sample of specified size in an array 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Note
    
this method should only be used if the resulting array is expected to be small, as all the data is loaded into the driver's memory.
  81. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#toDebugString:String "Permalink") def toDebugString: String
A description of this RDD and its recursive dependencies for debugging.
A description of this RDD and its recursive dependencies for debugging. 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  82. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#toJavaRDD\(\):org.apache.spark.api.java.JavaRDD\[T\] "Permalink") def toJavaRDD(): [JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)] 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  83. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#toLocalIterator:Iterator\[T\] "Permalink") def toLocalIterator: Iterator[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]
Return an iterator that contains all of the elements in this RDD.
Return an iterator that contains all of the elements in this RDD.
The iterator will consume as much memory as the largest partition in this RDD.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Note
    
This results in multiple Spark jobs, and if the input RDD is the result of a wide transformation (e.g. join with different partitioners), to avoid recomputing the input RDD should be cached first.
  84. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#toString\(\):String "Permalink") def toString(): String 

Definition Classes
     [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") → AnyRef → Any
  85. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#top\(num:Int\)\(implicitord:Ordering\[T\]\):Array\[T\] "Permalink") def top(num: Int)(implicit ord: Ordering[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]): Array[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]
Returns the top k (largest) elements from this RDD as defined by the specified implicit Ordering[T] and maintains the ordering.
Returns the top k (largest) elements from this RDD as defined by the specified implicit Ordering[T] and maintains the ordering. This does the opposite of [takeOrdered](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#takeOrdered\(num:Int\)\(implicitord:Ordering\[T\]\):Array\[T\]). For example:

```
sc.parallelize(Seq(10, 4, 2, 12, 3)).top(1)
// returns Array(12)

sc.parallelize(Seq(2, 3, 4, 5, 6)).top(2)
// returns Array(6, 5)
```


num
    
k, the number of top elements to return 

ord
    
the implicit ordering for T 

returns
    
an array of top elements 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Note
    
This method should only be used if the resulting array is expected to be small, as all the data is loaded into the driver's memory.
  86. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#treeAggregate\[U\]\(zeroValue:U,seqOp:\(U,T\)=>U,combOp:\(U,U\)=>U,depth:Int,finalAggregateOnExecutor:Boolean\)\(implicitevidence$35:scala.reflect.ClassTag\[U\]\):U "Permalink") def treeAggregate[U](zeroValue: U, seqOp: (U, ([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)) => U, combOp: (U, U) => U, depth: Int, finalAggregateOnExecutor: Boolean)(implicit arg0: ClassTag[U]): U
[org.apache.spark.rdd.RDD#treeAggregate](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html#treeAggregate\[U\]\(zeroValue:U,seqOp:\(U,T\)=>U,combOp:\(U,U\)=>U,depth:Int,finalAggregateOnExecutor:Boolean\)\(implicitevidence$35:scala.reflect.ClassTag\[U\]\):U) with a parameter to do the final aggregation on the executor 
[org.apache.spark.rdd.RDD#treeAggregate](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html#treeAggregate\[U\]\(zeroValue:U,seqOp:\(U,T\)=>U,combOp:\(U,U\)=>U,depth:Int,finalAggregateOnExecutor:Boolean\)\(implicitevidence$35:scala.reflect.ClassTag\[U\]\):U) with a parameter to do the final aggregation on the executor  

finalAggregateOnExecutor
    
do final aggregation on executor 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  87. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#treeAggregate\[U\]\(zeroValue:U\)\(seqOp:\(U,T\)=>U,combOp:\(U,U\)=>U,depth:Int\)\(implicitevidence$34:scala.reflect.ClassTag\[U\]\):U "Permalink") def treeAggregate[U](zeroValue: U)(seqOp: (U, ([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)) => U, combOp: (U, U) => U, depth: Int = 2)(implicit arg0: ClassTag[U]): U
Aggregates the elements of this RDD in a multi-level tree pattern.
Aggregates the elements of this RDD in a multi-level tree pattern. This method is semantically identical to [org.apache.spark.rdd.RDD#aggregate](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html#aggregate\[U\]\(zeroValue:U\)\(seqOp:\(U,T\)=>U,combOp:\(U,U\)=>U\)\(implicitevidence$33:scala.reflect.ClassTag\[U\]\):U).  

depth
    
suggested depth of the tree (default: 2) 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  88. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#treeReduce\(f:\(T,T\)=>T,depth:Int\):T "Permalink") def treeReduce(f: (([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD), ([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)) => ([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD), depth: Int = 2): ([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)
Reduces the elements of this RDD in a multi-level tree pattern.
Reduces the elements of this RDD in a multi-level tree pattern.  

depth
    
suggested depth of the tree (default: 2) 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

See also
    
[org.apache.spark.rdd.RDD#reduce](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html#reduce\(f:\(T,T\)=>T\):T)
  89. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#union\(other:org.apache.spark.rdd.RDD\[T\]\):org.apache.spark.rdd.RDD\[T\] "Permalink") def union(other: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]
Return the union of this RDD and another one.
Return the union of this RDD and another one. Any identical elements will appear multiple times (use `.distinct()` to eliminate them).  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  90. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#unpersist\(blocking:Boolean\):RDD.this.type "Permalink") def unpersist(blocking: Boolean = false): [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "org.apache.spark.graphx.VertexRDD").this.type
Mark the RDD as non-persistent, and remove all blocks for it from memory and disk.
Mark the RDD as non-persistent, and remove all blocks for it from memory and disk.  

blocking
    
Whether to block until all blocks are deleted (default: false) 

returns
    
This RDD. 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  91. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#withResources\(rp:org.apache.spark.resource.ResourceProfile\):RDD.this.type "Permalink") def withResources(rp: [ResourceProfile](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/resource/ResourceProfile.html "org.apache.spark.resource.ResourceProfile")): [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "org.apache.spark.graphx.VertexRDD").this.type
Specify a ResourceProfile to use when calculating this RDD.
Specify a ResourceProfile to use when calculating this RDD. This is only supported on certain cluster managers and currently requires dynamic allocation to be enabled. It will result in new executors with the resources specified being acquired to calculate the RDD.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Annotations
     @Experimental() @Since("3.1.0")
  92. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#zip\[U\]\(other:org.apache.spark.rdd.RDD\[U\]\)\(implicitevidence$13:scala.reflect.ClassTag\[U\]\):org.apache.spark.rdd.RDD\[\(T,U\)\] "Permalink") def zip[U](other: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[U])(implicit arg0: ClassTag[U]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD), U)]
Zips this RDD with another one, returning key-value pairs with the first element in each RDD, second element in each RDD, etc.
Zips this RDD with another one, returning key-value pairs with the first element in each RDD, second element in each RDD, etc. Assumes that the two RDDs have the *same number of partitions* and the *same number of elements in each partition* (e.g. one was made through a map on the other).  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  93. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#zipPartitions\[B,C,D,V\]\(rdd2:org.apache.spark.rdd.RDD\[B\],rdd3:org.apache.spark.rdd.RDD\[C\],rdd4:org.apache.spark.rdd.RDD\[D\]\)\(f:\(Iterator\[T\],Iterator\[B\],Iterator\[C\],Iterator\[D\]\)=>Iterator\[V\]\)\(implicitevidence$28:scala.reflect.ClassTag\[B\],implicitevidence$29:scala.reflect.ClassTag\[C\],implicitevidence$30:scala.reflect.ClassTag\[D\],implicitevidence$31:scala.reflect.ClassTag\[V\]\):org.apache.spark.rdd.RDD\[V\] "Permalink") def zipPartitions[B, C, D, V](rdd2: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[B], rdd3: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[C], rdd4: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[D])(f: (Iterator[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)], Iterator[B], Iterator[C], Iterator[D]) => Iterator[V])(implicit arg0: ClassTag[B], arg1: ClassTag[C], arg2: ClassTag[D], arg3: ClassTag[V]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[V] 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  94. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#zipPartitions\[B,C,D,V\]\(rdd2:org.apache.spark.rdd.RDD\[B\],rdd3:org.apache.spark.rdd.RDD\[C\],rdd4:org.apache.spark.rdd.RDD\[D\],preservesPartitioning:Boolean\)\(f:\(Iterator\[T\],Iterator\[B\],Iterator\[C\],Iterator\[D\]\)=>Iterator\[V\]\)\(implicitevidence$24:scala.reflect.ClassTag\[B\],implicitevidence$25:scala.reflect.ClassTag\[C\],implicitevidence$26:scala.reflect.ClassTag\[D\],implicitevidence$27:scala.reflect.ClassTag\[V\]\):org.apache.spark.rdd.RDD\[V\] "Permalink") def zipPartitions[B, C, D, V](rdd2: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[B], rdd3: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[C], rdd4: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[D], preservesPartitioning: Boolean)(f: (Iterator[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)], Iterator[B], Iterator[C], Iterator[D]) => Iterator[V])(implicit arg0: ClassTag[B], arg1: ClassTag[C], arg2: ClassTag[D], arg3: ClassTag[V]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[V] 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  95. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#zipPartitions\[B,C,V\]\(rdd2:org.apache.spark.rdd.RDD\[B\],rdd3:org.apache.spark.rdd.RDD\[C\]\)\(f:\(Iterator\[T\],Iterator\[B\],Iterator\[C\]\)=>Iterator\[V\]\)\(implicitevidence$21:scala.reflect.ClassTag\[B\],implicitevidence$22:scala.reflect.ClassTag\[C\],implicitevidence$23:scala.reflect.ClassTag\[V\]\):org.apache.spark.rdd.RDD\[V\] "Permalink") def zipPartitions[B, C, V](rdd2: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[B], rdd3: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[C])(f: (Iterator[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)], Iterator[B], Iterator[C]) => Iterator[V])(implicit arg0: ClassTag[B], arg1: ClassTag[C], arg2: ClassTag[V]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[V] 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  96. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#zipPartitions\[B,C,V\]\(rdd2:org.apache.spark.rdd.RDD\[B\],rdd3:org.apache.spark.rdd.RDD\[C\],preservesPartitioning:Boolean\)\(f:\(Iterator\[T\],Iterator\[B\],Iterator\[C\]\)=>Iterator\[V\]\)\(implicitevidence$18:scala.reflect.ClassTag\[B\],implicitevidence$19:scala.reflect.ClassTag\[C\],implicitevidence$20:scala.reflect.ClassTag\[V\]\):org.apache.spark.rdd.RDD\[V\] "Permalink") def zipPartitions[B, C, V](rdd2: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[B], rdd3: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[C], preservesPartitioning: Boolean)(f: (Iterator[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)], Iterator[B], Iterator[C]) => Iterator[V])(implicit arg0: ClassTag[B], arg1: ClassTag[C], arg2: ClassTag[V]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[V] 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  97. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#zipPartitions\[B,V\]\(rdd2:org.apache.spark.rdd.RDD\[B\]\)\(f:\(Iterator\[T\],Iterator\[B\]\)=>Iterator\[V\]\)\(implicitevidence$16:scala.reflect.ClassTag\[B\],implicitevidence$17:scala.reflect.ClassTag\[V\]\):org.apache.spark.rdd.RDD\[V\] "Permalink") def zipPartitions[B, V](rdd2: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[B])(f: (Iterator[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)], Iterator[B]) => Iterator[V])(implicit arg0: ClassTag[B], arg1: ClassTag[V]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[V] 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  98. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#zipPartitions\[B,V\]\(rdd2:org.apache.spark.rdd.RDD\[B\],preservesPartitioning:Boolean\)\(f:\(Iterator\[T\],Iterator\[B\]\)=>Iterator\[V\]\)\(implicitevidence$14:scala.reflect.ClassTag\[B\],implicitevidence$15:scala.reflect.ClassTag\[V\]\):org.apache.spark.rdd.RDD\[V\] "Permalink") def zipPartitions[B, V](rdd2: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[B], preservesPartitioning: Boolean)(f: (Iterator[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)], Iterator[B]) => Iterator[V])(implicit arg0: ClassTag[B], arg1: ClassTag[V]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[V]
Zip this RDD's partitions with one (or more) RDD(s) and return a new RDD by applying a function to the zipped partitions.
Zip this RDD's partitions with one (or more) RDD(s) and return a new RDD by applying a function to the zipped partitions. Assumes that all the RDDs have the *same number of partitions*, but does *not* require them to have the same number of elements in each partition.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  99. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#zipPartitionsWithEvaluator\[U\]\(rdd2:org.apache.spark.rdd.RDD\[T\],evaluatorFactory:org.apache.spark.PartitionEvaluatorFactory\[T,U\]\)\(implicitevidence$11:scala.reflect.ClassTag\[U\]\):org.apache.spark.rdd.RDD\[U\] "Permalink") def zipPartitionsWithEvaluator[U](rdd2: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)], evaluatorFactory: [PartitionEvaluatorFactory](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/PartitionEvaluatorFactory.html "org.apache.spark.PartitionEvaluatorFactory")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD), U])(implicit arg0: ClassTag[U]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[U]
Zip this RDD's partitions with another RDD and return a new RDD by applying an evaluator to the zipped partitions.
Zip this RDD's partitions with another RDD and return a new RDD by applying an evaluator to the zipped partitions. Assumes that the two RDDs have the *same number of partitions*, but does *not* require them to have the same number of elements in each partition.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Annotations
     @DeveloperApi() @Since("3.5.0")
  100. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#zipWithIndex\(\):org.apache.spark.rdd.RDD\[\(T,Long\)\] "Permalink") def zipWithIndex(): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD), Long)]
Zips this RDD with its element indices.
Zips this RDD with its element indices. The ordering is first based on the partition index and then the ordering of items within each partition. So the first item in the first partition gets index 0, and the last item in the last partition receives the largest index.
This is similar to Scala's zipWithIndex but it uses Long instead of Int as the index type. This method needs to trigger a spark job when this RDD contains more than one partitions.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Note
    
Some RDDs, such as those returned by groupBy(), do not guarantee order of elements in a partition. The index assigned to each element is therefore not guaranteed, and may even change if the RDD is reevaluated. If a fixed ordering is required to guarantee the same index assignments, you should sort the RDD with sortByKey() or save it to a file.
  101. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#zipWithUniqueId\(\):org.apache.spark.rdd.RDD\[\(T,Long\)\] "Permalink") def zipWithUniqueId(): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD), Long)]
Zips this RDD with generated unique Long ids.
Zips this RDD with generated unique Long ids. Items in the kth partition will get ids k, n+k, 2*n+k, ..., where n is the number of partitions. So there may exist gaps, but this method won't trigger a spark job, which is different from [org.apache.spark.rdd.RDD#zipWithIndex](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html#zipWithIndex\(\):org.apache.spark.rdd.RDD\[\(T,Long\)\]).  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Note
    
Some RDDs, such as those returned by groupBy(), do not guarantee order of elements in a partition. The unique ID assigned to each element is therefore not guaranteed, and may even change if the RDD is reevaluated. If a fixed ordering is required to guarantee the same index assignments, you should sort the RDD with sortByKey() or save it to a file.


### Inherited from Logging
### Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#MDC\(key:org.apache.spark.internal.LogKey,value:Any\):org.apache.spark.internal.MDC "Permalink") def MDC(key: LogKey, value: Any): MDC 

Attributes
    protected  

Definition Classes
    Logging
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#initializeLogIfNecessary\(isInterpreter:Boolean,silent:Boolean\):Boolean "Permalink") def initializeLogIfNecessary(isInterpreter: Boolean, silent: Boolean): Boolean 

Attributes
    protected  

Definition Classes
    Logging
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#initializeLogIfNecessary\(isInterpreter:Boolean\):Unit "Permalink") def initializeLogIfNecessary(isInterpreter: Boolean): Unit 

Attributes
    protected  

Definition Classes
    Logging
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#isTraceEnabled\(\):Boolean "Permalink") def isTraceEnabled(): Boolean 

Attributes
    protected  

Definition Classes
    Logging
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#log:org.slf4j.Logger "Permalink") def log: Logger 

Attributes
    protected  

Definition Classes
    Logging
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#logBasedOnLevel\(level:org.slf4j.event.Level\)\(f:=>org.apache.spark.internal.MessageWithContext\):Unit "Permalink") def logBasedOnLevel(level: Level)(f: => MessageWithContext): Unit 

Attributes
    protected  

Definition Classes
    Logging
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#logDebug\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logDebug(msg: => String, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#logDebug\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logDebug(entry: LogEntry, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#logDebug\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logDebug(entry: LogEntry): Unit 

Attributes
    protected  

Definition Classes
    Logging
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#logDebug\(msg:=>String\):Unit "Permalink") def logDebug(msg: => String): Unit 

Attributes
    protected  

Definition Classes
    Logging
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#logError\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logError(msg: => String, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#logError\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logError(entry: LogEntry, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#logError\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logError(entry: LogEntry): Unit 

Attributes
    protected  

Definition Classes
    Logging
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#logError\(msg:=>String\):Unit "Permalink") def logError(msg: => String): Unit 

Attributes
    protected  

Definition Classes
    Logging
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#logInfo\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logInfo(msg: => String, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#logInfo\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logInfo(entry: LogEntry, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#logInfo\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logInfo(entry: LogEntry): Unit 

Attributes
    protected  

Definition Classes
    Logging
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#logInfo\(msg:=>String\):Unit "Permalink") def logInfo(msg: => String): Unit 

Attributes
    protected  

Definition Classes
    Logging
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#logName:String "Permalink") def logName: [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String") 

Attributes
    protected  

Definition Classes
    Logging
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#logTrace\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logTrace(msg: => String, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#logTrace\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logTrace(entry: LogEntry, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#logTrace\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logTrace(entry: LogEntry): Unit 

Attributes
    protected  

Definition Classes
    Logging
  23. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#logTrace\(msg:=>String\):Unit "Permalink") def logTrace(msg: => String): Unit 

Attributes
    protected  

Definition Classes
    Logging
  24. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#logWarning\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logWarning(msg: => String, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  25. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#logWarning\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logWarning(entry: LogEntry, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  26. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#logWarning\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logWarning(entry: LogEntry): Unit 

Attributes
    protected  

Definition Classes
    Logging
  27. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#logWarning\(msg:=>String\):Unit "Permalink") def logWarning(msg: => String): Unit 

Attributes
    protected  

Definition Classes
    Logging
  28. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#withLogContext\(context:java.util.Map\[String,String\]\)\(body:=>Unit\):Unit "Permalink") def withLogContext(context: [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#java.util.Map "java.util.Map")[String, String])(body: => Unit): Unit 

Attributes
    protected  

Definition Classes
    Logging


### Inherited from AnyRef
### Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html###:Int "Permalink") final  def ##: Int 

Definition Classes
    AnyRef → Any
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#clone\(\):Object "Permalink") def clone(): AnyRef 

Attributes
    protected[lang]  

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#equals\(x$1:Object\):Boolean "Permalink") def equals(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef → Any
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef] 

Definition Classes
    AnyRef → Any 

Annotations
     @IntrinsicCandidate() @native()
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#hashCode\(\):Int "Permalink") def hashCode(): Int 

Definition Classes
    AnyRef → Any 

Annotations
     @IntrinsicCandidate() @native()
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#notify\(\):Unit "Permalink") final  def notify(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0 

Definition Classes
    AnyRef
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#wait\(\):Unit "Permalink") final  def wait(): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#finalize\(\):Unit "Permalink") def finalize(): Unit 

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
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0 

Definition Classes
    Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean 

Definition Classes
    Any


### Ungrouped
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#LogStringContextextendsAnyRef "Permalink") implicit  class LogStringContext extends AnyRef 

Definition Classes
    Logging


  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#aggregateUsingIndex\[VD2\]\(messages:org.apache.spark.rdd.RDD\[\(org.apache.spark.graphx.VertexId,VD2\)\],reduceFunc:\(VD2,VD2\)=>VD2\)\(implicitevidence$12:scala.reflect.ClassTag\[VD2\]\):org.apache.spark.graphx.VertexRDD\[VD2\] "Permalink") abstract  def aggregateUsingIndex[VD2](messages: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD2)], reduceFunc: (VD2, VD2) => VD2)(implicit arg0: ClassTag[VD2]): [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "org.apache.spark.graphx.VertexRDD")[VD2]
Aggregates vertices in `messages` that have the same ids using `reduceFunc`, returning a VertexRDD co-indexed with `this`.
Aggregates vertices in `messages` that have the same ids using `reduceFunc`, returning a VertexRDD co-indexed with `this`.  

messages
    
an RDD containing messages to aggregate, where each message is a pair of its target vertex ID and the message data 

reduceFunc
    
the associative aggregation function for merging messages to the same vertex 

returns
    
a VertexRDD co-indexed with `this`, containing only vertices that received messages. For those vertices, their values are the result of applying `reduceFunc` to all received messages.
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#diff\(other:org.apache.spark.graphx.VertexRDD\[VD\]\):org.apache.spark.graphx.VertexRDD\[VD\] "Permalink") abstract  def diff(other: [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "org.apache.spark.graphx.VertexRDD")[VD]): [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "org.apache.spark.graphx.VertexRDD")[VD]
For each vertex present in both `this` and `other`, `diff` returns only those vertices with differing values; for values that are different, keeps the values from `other`.
For each vertex present in both `this` and `other`, `diff` returns only those vertices with differing values; for values that are different, keeps the values from `other`. This is only guaranteed to work if the VertexRDDs share a common ancestor.  

other
    
the other VertexRDD with which to diff against.
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#diff\(other:org.apache.spark.rdd.RDD\[\(org.apache.spark.graphx.VertexId,VD\)\]\):org.apache.spark.graphx.VertexRDD\[VD\] "Permalink") abstract  def diff(other: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]): [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "org.apache.spark.graphx.VertexRDD")[VD]
For each vertex present in both `this` and `other`, `diff` returns only those vertices with differing values; for values that are different, keeps the values from `other`.
For each vertex present in both `this` and `other`, `diff` returns only those vertices with differing values; for values that are different, keeps the values from `other`. This is only guaranteed to work if the VertexRDDs share a common ancestor.  

other
    
the other RDD[(VertexId, VD)] with which to diff against.
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#innerJoin\[U,VD2\]\(other:org.apache.spark.rdd.RDD\[\(org.apache.spark.graphx.VertexId,U\)\]\)\(f:\(org.apache.spark.graphx.VertexId,VD,U\)=>VD2\)\(implicitevidence$10:scala.reflect.ClassTag\[U\],implicitevidence$11:scala.reflect.ClassTag\[VD2\]\):org.apache.spark.graphx.VertexRDD\[VD2\] "Permalink") abstract  def innerJoin[U, VD2](other: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), U)])(f: ([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD, U) => VD2)(implicit arg0: ClassTag[U], arg1: ClassTag[VD2]): [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "org.apache.spark.graphx.VertexRDD")[VD2]
Inner joins this VertexRDD with an RDD containing vertex attribute pairs.
Inner joins this VertexRDD with an RDD containing vertex attribute pairs. If the other RDD is backed by a VertexRDD with the same index then the efficient [innerZipJoin](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#innerZipJoin\[U,VD2\]\(other:org.apache.spark.graphx.VertexRDD\[U\]\)\(f:\(org.apache.spark.graphx.VertexId,VD,U\)=>VD2\)\(implicitevidence$8:scala.reflect.ClassTag\[U\],implicitevidence$9:scala.reflect.ClassTag\[VD2\]\):org.apache.spark.graphx.VertexRDD\[VD2\]) implementation is used.  

other
    
an RDD containing vertices to join. If there are multiple entries for the same vertex, one is picked arbitrarily. Use [aggregateUsingIndex](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#aggregateUsingIndex\[VD2\]\(messages:org.apache.spark.rdd.RDD\[\(org.apache.spark.graphx.VertexId,VD2\)\],reduceFunc:\(VD2,VD2\)=>VD2\)\(implicitevidence$12:scala.reflect.ClassTag\[VD2\]\):org.apache.spark.graphx.VertexRDD\[VD2\]) to merge multiple entries. 

f
    
the join function applied to corresponding values of `this` and `other` 

returns
    
a VertexRDD co-indexed with `this`, containing only vertices that appear in both `this` and `other`, with values supplied by `f`
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#innerZipJoin\[U,VD2\]\(other:org.apache.spark.graphx.VertexRDD\[U\]\)\(f:\(org.apache.spark.graphx.VertexId,VD,U\)=>VD2\)\(implicitevidence$8:scala.reflect.ClassTag\[U\],implicitevidence$9:scala.reflect.ClassTag\[VD2\]\):org.apache.spark.graphx.VertexRDD\[VD2\] "Permalink") abstract  def innerZipJoin[U, VD2](other: [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "org.apache.spark.graphx.VertexRDD")[U])(f: ([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD, U) => VD2)(implicit arg0: ClassTag[U], arg1: ClassTag[VD2]): [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "org.apache.spark.graphx.VertexRDD")[VD2]
Efficiently inner joins this VertexRDD with another VertexRDD sharing the same index.
Efficiently inner joins this VertexRDD with another VertexRDD sharing the same index. See [innerJoin](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#innerJoin\[U,VD2\]\(other:org.apache.spark.rdd.RDD\[\(org.apache.spark.graphx.VertexId,U\)\]\)\(f:\(org.apache.spark.graphx.VertexId,VD,U\)=>VD2\)\(implicitevidence$10:scala.reflect.ClassTag\[U\],implicitevidence$11:scala.reflect.ClassTag\[VD2\]\):org.apache.spark.graphx.VertexRDD\[VD2\]) for the behavior of the join. 
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#leftJoin\[VD2,VD3\]\(other:org.apache.spark.rdd.RDD\[\(org.apache.spark.graphx.VertexId,VD2\)\]\)\(f:\(org.apache.spark.graphx.VertexId,VD,Option\[VD2\]\)=>VD3\)\(implicitevidence$6:scala.reflect.ClassTag\[VD2\],implicitevidence$7:scala.reflect.ClassTag\[VD3\]\):org.apache.spark.graphx.VertexRDD\[VD3\] "Permalink") abstract  def leftJoin[VD2, VD3](other: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD2)])(f: ([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD, Option[VD2]) => VD3)(implicit arg0: ClassTag[VD2], arg1: ClassTag[VD3]): [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "org.apache.spark.graphx.VertexRDD")[VD3]
Left joins this VertexRDD with an RDD containing vertex attribute pairs.
Left joins this VertexRDD with an RDD containing vertex attribute pairs. If the other RDD is backed by a VertexRDD with the same index then the efficient [leftZipJoin](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#leftZipJoin\[VD2,VD3\]\(other:org.apache.spark.graphx.VertexRDD\[VD2\]\)\(f:\(org.apache.spark.graphx.VertexId,VD,Option\[VD2\]\)=>VD3\)\(implicitevidence$4:scala.reflect.ClassTag\[VD2\],implicitevidence$5:scala.reflect.ClassTag\[VD3\]\):org.apache.spark.graphx.VertexRDD\[VD3\]) implementation is used. The resulting VertexRDD contains an entry for each vertex in `this`. If `other` is missing any vertex in this VertexRDD, `f` is passed `None`. If there are duplicates, the vertex is picked arbitrarily.  

VD2
    
the attribute type of the other VertexRDD 

VD3
    
the attribute type of the resulting VertexRDD 

other
    
the other VertexRDD with which to join 

f
    
the function mapping a vertex id and its attributes in this and the other vertex set to a new vertex attribute. 

returns
    
a VertexRDD containing all the vertices in this VertexRDD with the attributes emitted by `f`.
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#leftZipJoin\[VD2,VD3\]\(other:org.apache.spark.graphx.VertexRDD\[VD2\]\)\(f:\(org.apache.spark.graphx.VertexId,VD,Option\[VD2\]\)=>VD3\)\(implicitevidence$4:scala.reflect.ClassTag\[VD2\],implicitevidence$5:scala.reflect.ClassTag\[VD3\]\):org.apache.spark.graphx.VertexRDD\[VD3\] "Permalink") abstract  def leftZipJoin[VD2, VD3](other: [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "org.apache.spark.graphx.VertexRDD")[VD2])(f: ([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD, Option[VD2]) => VD3)(implicit arg0: ClassTag[VD2], arg1: ClassTag[VD3]): [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "org.apache.spark.graphx.VertexRDD")[VD3]
Left joins this RDD with another VertexRDD with the same index.
Left joins this RDD with another VertexRDD with the same index. This function will fail if both VertexRDDs do not share the same index. The resulting vertex set contains an entry for each vertex in `this`. If `other` is missing any vertex in this VertexRDD, `f` is passed `None`.  

VD2
    
the attribute type of the other VertexRDD 

VD3
    
the attribute type of the resulting VertexRDD 

other
    
the other VertexRDD with which to join. 

f
    
the function mapping a vertex id and its attributes in this and the other vertex set to a new vertex attribute. 

returns
    
a VertexRDD containing the results of `f`
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#mapValues\[VD2\]\(f:\(org.apache.spark.graphx.VertexId,VD\)=>VD2\)\(implicitevidence$3:scala.reflect.ClassTag\[VD2\]\):org.apache.spark.graphx.VertexRDD\[VD2\] "Permalink") abstract  def mapValues[VD2](f: ([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD) => VD2)(implicit arg0: ClassTag[VD2]): [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "org.apache.spark.graphx.VertexRDD")[VD2]
Maps each vertex attribute, additionally supplying the vertex ID.
Maps each vertex attribute, additionally supplying the vertex ID.  

VD2
    
the type returned by the map function 

f
    
the function applied to each ID-value pair in the RDD 

returns
    
a new VertexRDD with values obtained by applying `f` to each of the entries in the original VertexRDD. The resulting VertexRDD retains the same index.
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#mapValues\[VD2\]\(f:VD=>VD2\)\(implicitevidence$2:scala.reflect.ClassTag\[VD2\]\):org.apache.spark.graphx.VertexRDD\[VD2\] "Permalink") abstract  def mapValues[VD2](f: (VD) => VD2)(implicit arg0: ClassTag[VD2]): [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "org.apache.spark.graphx.VertexRDD")[VD2]
Maps each vertex attribute, preserving the index.
Maps each vertex attribute, preserving the index.  

VD2
    
the type returned by the map function 

f
    
the function applied to each value in the RDD 

returns
    
a new VertexRDD with values obtained by applying `f` to each of the entries in the original VertexRDD
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#minus\(other:org.apache.spark.graphx.VertexRDD\[VD\]\):org.apache.spark.graphx.VertexRDD\[VD\] "Permalink") abstract  def minus(other: [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "org.apache.spark.graphx.VertexRDD")[VD]): [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "org.apache.spark.graphx.VertexRDD")[VD]
For each VertexId present in both `this` and `other`, minus will act as a set difference operation returning only those unique VertexId's present in `this`.
For each VertexId present in both `this` and `other`, minus will act as a set difference operation returning only those unique VertexId's present in `this`.  

other
    
a VertexRDD to run the set operation against
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#minus\(other:org.apache.spark.rdd.RDD\[\(org.apache.spark.graphx.VertexId,VD\)\]\):org.apache.spark.graphx.VertexRDD\[VD\] "Permalink") abstract  def minus(other: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]): [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "org.apache.spark.graphx.VertexRDD")[VD]
For each VertexId present in both `this` and `other`, minus will act as a set difference operation returning only those unique VertexId's present in `this`.
For each VertexId present in both `this` and `other`, minus will act as a set difference operation returning only those unique VertexId's present in `this`.  

other
    
an RDD to run the set operation against
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#reindex\(\):org.apache.spark.graphx.VertexRDD\[VD\] "Permalink") abstract  def reindex(): [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "org.apache.spark.graphx.VertexRDD")[VD]
Construct a new VertexRDD that is indexed by only the visible vertices.
Construct a new VertexRDD that is indexed by only the visible vertices. The resulting VertexRDD will be based on a different index and can no longer be quickly joined with this RDD. 
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#reverseRoutingTables\(\):org.apache.spark.graphx.VertexRDD\[VD\] "Permalink") abstract  def reverseRoutingTables(): [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "org.apache.spark.graphx.VertexRDD")[VD]
Returns a new `VertexRDD` reflecting a reversal of all edge directions in the corresponding [EdgeRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/EdgeRDD.html "org.apache.spark.graphx.EdgeRDD").
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#vdTag:scala.reflect.ClassTag\[VD\] "Permalink") implicit abstract  def vdTag: ClassTag[VD] 

Attributes
    protected 
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#withEdges\(edges:org.apache.spark.graphx.EdgeRDD\[_\]\):org.apache.spark.graphx.VertexRDD\[VD\] "Permalink") abstract  def withEdges(edges: [EdgeRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/EdgeRDD.html "org.apache.spark.graphx.EdgeRDD")[_]): [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "org.apache.spark.graphx.VertexRDD")[VD]
Prepares this VertexRDD for efficient joins with the given EdgeRDD.
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html###:Int "Permalink") final  def ##: Int 

Definition Classes
    AnyRef → Any
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#++\(other:org.apache.spark.rdd.RDD\[T\]\):org.apache.spark.rdd.RDD\[T\] "Permalink") def ++(other: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]
Return the union of this RDD and another one.
Return the union of this RDD and another one. Any identical elements will appear multiple times (use `.distinct()` to eliminate them).  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#MDC\(key:org.apache.spark.internal.LogKey,value:Any\):org.apache.spark.internal.MDC "Permalink") def MDC(key: LogKey, value: Any): MDC 

Attributes
    protected  

Definition Classes
    Logging
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#aggregate\[U\]\(zeroValue:U\)\(seqOp:\(U,T\)=>U,combOp:\(U,U\)=>U\)\(implicitevidence$33:scala.reflect.ClassTag\[U\]\):U "Permalink") def aggregate[U](zeroValue: U)(seqOp: (U, ([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)) => U, combOp: (U, U) => U)(implicit arg0: ClassTag[U]): U
Aggregate the elements of each partition, and then the results for all the partitions, using given combine functions and a neutral "zero value".
Aggregate the elements of each partition, and then the results for all the partitions, using given combine functions and a neutral "zero value". This function can return a different result type, U, than the type of this RDD, T. Thus, we need one operation for merging a T into an U and one operation for merging two U's, as in scala.IterableOnce. Both of these functions are allowed to modify and return their first argument instead of creating a new U to avoid memory allocation.  

zeroValue
    
the initial value for the accumulated result of each partition for the `seqOp` operator, and also the initial value for the combine results from different partitions for the `combOp` operator - this will typically be the neutral element (e.g. `Nil` for list concatenation or `0` for summation) 

seqOp
    
an operator used to accumulate results within a partition 

combOp
    
an associative operator used to combine results from different partitions 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0 

Definition Classes
    Any
  23. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#barrier\(\):org.apache.spark.rdd.RDDBarrier\[T\] "Permalink") def barrier(): [RDDBarrier](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDDBarrier.html "org.apache.spark.rdd.RDDBarrier")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]
Marks the current stage as a barrier stage, where Spark must launch all tasks together.
Marks the current stage as a barrier stage, where Spark must launch all tasks together. In case of a task failure, instead of only restarting the failed task, Spark will abort the entire stage and re-launch all tasks for this stage. The barrier execution mode feature is experimental and it only handles limited scenarios. Please read the linked SPIP and design docs to understand the limitations and future plans. 

returns
    
an RDDBarrier instance that provides actions within a barrier stage 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Annotations
     @Experimental() @Since("2.4.0") 

See also
    
[org.apache.spark.BarrierTaskContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/BarrierTaskContext.html "org.apache.spark.BarrierTaskContext")
[ SPIP: Barrier Execution Mode](https://issues.apache.org/jira/browse/SPARK-24374)
[Design Doc](https://issues.apache.org/jira/browse/SPARK-24582)
  24. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#cache\(\):RDD.this.type "Permalink") def cache(): [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "org.apache.spark.graphx.VertexRDD").this.type
Persist this RDD with the default storage level (`MEMORY_ONLY`).
Persist this RDD with the default storage level (`MEMORY_ONLY`).  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  25. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#cartesian\[U\]\(other:org.apache.spark.rdd.RDD\[U\]\)\(implicitevidence$5:scala.reflect.ClassTag\[U\]\):org.apache.spark.rdd.RDD\[\(T,U\)\] "Permalink") def cartesian[U](other: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[U])(implicit arg0: ClassTag[U]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD), U)]
Return the Cartesian product of this RDD and another one, that is, the RDD of all pairs of elements (a, b) where a is in `this` and b is in `other`.
Return the Cartesian product of this RDD and another one, that is, the RDD of all pairs of elements (a, b) where a is in `this` and b is in `other`.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  26. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#checkpoint\(\):Unit "Permalink") def checkpoint(): Unit
Mark this RDD for checkpointing.
Mark this RDD for checkpointing. It will be saved to a file inside the checkpoint directory set with `SparkContext#setCheckpointDir` and all references to its parent RDDs will be removed. This function must be called before any job has been executed on this RDD. It is strongly recommended that this RDD is persisted in memory, otherwise saving it on a file will require recomputation.
The data is only checkpointed when `doCheckpoint()` is called, and this only happens at the end of the first action execution on this RDD. The final data that is checkpointed after the first action may be different from the data that was used during the action, due to non-determinism of the underlying operation and retries. If the purpose of the checkpoint is to achieve saving a deterministic snapshot of the data, an eager action may need to be called first on the RDD to trigger the checkpoint.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  27. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#cleanShuffleDependencies\(blocking:Boolean\):Unit "Permalink") def cleanShuffleDependencies(blocking: Boolean = false): Unit
Removes an RDD's shuffles and it's non-persisted ancestors.
Removes an RDD's shuffles and it's non-persisted ancestors. When running without a shuffle service, cleaning up shuffle files enables downscaling. If you use the RDD after this call, you should checkpoint and materialize it first. If you are uncertain of what you are doing, please do not use this feature. Additional techniques for mitigating orphaned shuffle files: * Tuning the driver GC to be more aggressive, so the regular context cleaner is triggered * Setting an appropriate TTL for shuffle files to be auto cleaned  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Annotations
     @DeveloperApi() @Since("3.1.0")
  28. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#clearDependencies\(\):Unit "Permalink") def clearDependencies(): Unit
Clears the dependencies of this RDD.
Clears the dependencies of this RDD. This method must ensure that all references to the original parent RDDs are removed to enable the parent RDDs to be garbage collected. Subclasses of RDD may override this method for implementing their own cleaning logic. See [org.apache.spark.rdd.UnionRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/UnionRDD.html "org.apache.spark.rdd.UnionRDD") for an example.  

Attributes
    protected  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  29. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#clone\(\):Object "Permalink") def clone(): AnyRef 

Attributes
    protected[lang]  

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  30. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#coalesce\(numPartitions:Int,shuffle:Boolean,partitionCoalescer:Option\[org.apache.spark.rdd.PartitionCoalescer\]\)\(implicitord:Ordering\[T\]\):org.apache.spark.rdd.RDD\[T\] "Permalink") def coalesce(numPartitions: Int, shuffle: Boolean = false, partitionCoalescer: Option[[PartitionCoalescer](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PartitionCoalescer.html "org.apache.spark.rdd.PartitionCoalescer")] = Option.empty)(implicit ord: Ordering[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)] = null): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]
Return a new RDD that is reduced into `numPartitions` partitions.
Return a new RDD that is reduced into `numPartitions` partitions.
This results in a narrow dependency, e.g. if you go from 1000 partitions to 100 partitions, there will not be a shuffle, instead each of the 100 new partitions will claim 10 of the current partitions. If a larger number of partitions is requested, it will stay at the current number of partitions.
However, if you're doing a drastic coalesce, e.g. to numPartitions = 1, this may result in your computation taking place on fewer nodes than you like (e.g. one node in the case of numPartitions = 1). To avoid this, you can pass shuffle = true. This will add a shuffle step, but means the current upstream partitions will be executed in parallel (per whatever the current partitioning is).  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Note
    
With shuffle = true, you can actually coalesce to a larger number of partitions. This is useful if you have a small number of partitions, say 100, potentially with a few partitions being abnormally large. Calling coalesce(1000, shuffle = true) will result in 1000 partitions with the data distributed using a hash partitioner. The optional partition coalescer passed in must be serializable.
  31. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#collect\[U\]\(f:PartialFunction\[T,U\]\)\(implicitevidence$32:scala.reflect.ClassTag\[U\]\):org.apache.spark.rdd.RDD\[U\] "Permalink") def collect[U](f: PartialFunction[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD), U])(implicit arg0: ClassTag[U]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[U]
Return an RDD that contains all matching values by applying `f`.
Return an RDD that contains all matching values by applying `f`.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  32. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#collect\(\):Array\[T\] "Permalink") def collect(): Array[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]
Return an array that contains all of the elements in this RDD.
Return an array that contains all of the elements in this RDD.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Note
    
This method should only be used if the resulting array is expected to be small, as all the data is loaded into the driver's memory.
  33. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#compute\(part:org.apache.spark.Partition,context:org.apache.spark.TaskContext\):Iterator\[\(org.apache.spark.graphx.VertexId,VD\)\] "Permalink") def compute(part: [Partition](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partition.html "org.apache.spark.Partition"), context: [TaskContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskContext.html "org.apache.spark.TaskContext")): Iterator[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]
Provides the `RDD[(VertexId, VD)]` equivalent output.
Provides the `RDD[(VertexId, VD)]` equivalent output.  

Definition Classes
     [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "org.apache.spark.graphx.VertexRDD") → [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  34. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#context:org.apache.spark.SparkContext "Permalink") def context: [SparkContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html "org.apache.spark.SparkContext")
The [org.apache.spark.SparkContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html "org.apache.spark.SparkContext") that this RDD was created on.
The [org.apache.spark.SparkContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html "org.apache.spark.SparkContext") that this RDD was created on. 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  35. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#count\(\):Long "Permalink") def count(): Long
Return the number of elements in the RDD.
Return the number of elements in the RDD.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  36. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#countApprox\(timeout:Long,confidence:Double\):org.apache.spark.partial.PartialResult\[org.apache.spark.partial.BoundedDouble\] "Permalink") def countApprox(timeout: Long, confidence: Double = 0.95): [PartialResult](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/partial/PartialResult.html "org.apache.spark.partial.PartialResult")[[BoundedDouble](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/partial/BoundedDouble.html "org.apache.spark.partial.BoundedDouble")]
Approximate version of count() that returns a potentially incomplete result within a timeout, even if not all tasks have finished.
Approximate version of count() that returns a potentially incomplete result within a timeout, even if not all tasks have finished.
The confidence is the probability that the error bounds of the result will contain the true value. That is, if countApprox were called repeatedly with confidence 0.9, we would expect 90% of the results to contain the true count. The confidence must be in the range [0,1] or an exception will be thrown.  

timeout
    
maximum time to wait for the job, in milliseconds 

confidence
    
the desired statistical confidence in the result 

returns
    
a potentially incomplete result, with error bounds 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  37. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#countApproxDistinct\(relativeSD:Double\):Long "Permalink") def countApproxDistinct(relativeSD: Double = 0.05): Long
Return approximate number of distinct elements in the RDD.
Return approximate number of distinct elements in the RDD.
The algorithm used is based on streamlib's implementation of "HyperLogLog in Practice: Algorithmic Engineering of a State of The Art Cardinality Estimation Algorithm", available [here](https://doi.org/10.1145/2452376.2452456).  

relativeSD
    
Relative accuracy. Smaller values create counters that require more space. It must be greater than 0.000017. 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  38. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#countApproxDistinct\(p:Int,sp:Int\):Long "Permalink") def countApproxDistinct(p: Int, sp: Int): Long
Return approximate number of distinct elements in the RDD.
Return approximate number of distinct elements in the RDD.
The algorithm used is based on streamlib's implementation of "HyperLogLog in Practice: Algorithmic Engineering of a State of The Art Cardinality Estimation Algorithm", available [here](https://doi.org/10.1145/2452376.2452456).
The relative accuracy is approximately `1.054 / sqrt(2^p)`. Setting a nonzero (`sp` is greater than `p`) would trigger sparse representation of registers, which may reduce the memory consumption and increase accuracy when the cardinality is small. `` 

p
    
The precision value for the normal set. `p` must be a value between 4 and `sp` if `sp` is not zero (32 max). 

sp
    
The precision value for the sparse set, between 0 and 32. If `sp` equals 0, the sparse representation is skipped. 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  39. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#countByValue\(\)\(implicitord:Ordering\[T\]\):scala.collection.Map\[T,Long\] "Permalink") def countByValue()(implicit ord: Ordering[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)] = null): Map[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD), Long]
Return the count of each unique value in this RDD as a local map of (value, count) pairs.
Return the count of each unique value in this RDD as a local map of (value, count) pairs.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Note
    
This method should only be used if the resulting map is expected to be small, as the whole thing is loaded into the driver's memory. To handle very large results, consider using

```
rdd.map(x => (x, 1L)).reduceByKey(_ + _)
```

, which returns an RDD[T, Long] instead of a map.
  40. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#countByValueApprox\(timeout:Long,confidence:Double\)\(implicitord:Ordering\[T\]\):org.apache.spark.partial.PartialResult\[scala.collection.Map\[T,org.apache.spark.partial.BoundedDouble\]\] "Permalink") def countByValueApprox(timeout: Long, confidence: Double = 0.95)(implicit ord: Ordering[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)] = null): [PartialResult](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/partial/PartialResult.html "org.apache.spark.partial.PartialResult")[Map[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD), [BoundedDouble](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/partial/BoundedDouble.html "org.apache.spark.partial.BoundedDouble")]]
Approximate version of countByValue().
Approximate version of countByValue().  

timeout
    
maximum time to wait for the job, in milliseconds 

confidence
    
the desired statistical confidence in the result 

returns
    
a potentially incomplete result, with error bounds 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  41. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#dependencies:Seq\[org.apache.spark.Dependency\[_\]\] "Permalink") final  def dependencies: Seq[[Dependency](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Dependency.html "org.apache.spark.Dependency")[_]]
Get the list of dependencies of this RDD, taking into account whether the RDD is checkpointed or not.
Get the list of dependencies of this RDD, taking into account whether the RDD is checkpointed or not.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  42. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#distinct\(\):org.apache.spark.rdd.RDD\[T\] "Permalink") def distinct(): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]
Return a new RDD containing the distinct elements in this RDD.
Return a new RDD containing the distinct elements in this RDD.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  43. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#distinct\(numPartitions:Int\)\(implicitord:Ordering\[T\]\):org.apache.spark.rdd.RDD\[T\] "Permalink") def distinct(numPartitions: Int)(implicit ord: Ordering[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)] = null): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]
Return a new RDD containing the distinct elements in this RDD.
Return a new RDD containing the distinct elements in this RDD.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  44. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  45. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#equals\(x$1:Object\):Boolean "Permalink") def equals(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef → Any
  46. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#filter\(pred:\(\(org.apache.spark.graphx.VertexId,VD\)\)=>Boolean\):org.apache.spark.graphx.VertexRDD\[VD\] "Permalink") def filter(pred: (([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)) => Boolean): [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "org.apache.spark.graphx.VertexRDD")[VD]
Restricts the vertex set to the set of vertices satisfying the given predicate.
Restricts the vertex set to the set of vertices satisfying the given predicate. This operation preserves the index for efficient joins with the original RDD, and it sets bits in the bitmask rather than allocating new memory.
It is declared and defined here to allow refining the return type from `RDD[(VertexId, VD)]` to `VertexRDD[VD]`.  

pred
    
the user defined predicate, which takes a tuple to conform to the `RDD[(VertexId, VD)]` interface 

Definition Classes
     [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "org.apache.spark.graphx.VertexRDD") → [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  47. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#first\(\):T "Permalink") def first(): ([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)
Return the first element in this RDD.
Return the first element in this RDD.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  48. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#firstParent\[U\]\(implicitevidence$36:scala.reflect.ClassTag\[U\]\):org.apache.spark.rdd.RDD\[U\] "Permalink") def firstParent[U](implicit arg0: ClassTag[U]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[U]
Returns the first parent RDD
Returns the first parent RDD 

Attributes
    protected[[spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")]  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  49. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#flatMap\[U\]\(f:T=>IterableOnce\[U\]\)\(implicitevidence$4:scala.reflect.ClassTag\[U\]\):org.apache.spark.rdd.RDD\[U\] "Permalink") def flatMap[U](f: (([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)) => IterableOnce[U])(implicit arg0: ClassTag[U]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[U]
Return a new RDD by first applying a function to all elements of this RDD, and then flattening the results.
Return a new RDD by first applying a function to all elements of this RDD, and then flattening the results.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  50. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#fold\(zeroValue:T\)\(op:\(T,T\)=>T\):T "Permalink") def fold(zeroValue: ([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD))(op: (([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD), ([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)) => ([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)): ([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)
Aggregate the elements of each partition, and then the results for all the partitions, using a given associative function and a neutral "zero value".
Aggregate the elements of each partition, and then the results for all the partitions, using a given associative function and a neutral "zero value". The function op(t1, t2) is allowed to modify t1 and return it as its result value to avoid object allocation; however, it should not modify t2.
This behaves somewhat differently from fold operations implemented for non-distributed collections in functional languages like Scala. This fold operation may be applied to partitions individually, and then fold those results into the final result, rather than apply the fold to each element sequentially in some defined ordering. For functions that are not commutative, the result may differ from that of a fold applied to a non-distributed collection.  

zeroValue
    
the initial value for the accumulated result of each partition for the `op` operator, and also the initial value for the combine results from different partitions for the `op` operator - this will typically be the neutral element (e.g. `Nil` for list concatenation or `0` for summation) 

op
    
an operator used to both accumulate results within a partition and combine results from different partitions 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  51. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#foreach\(f:T=>Unit\):Unit "Permalink") def foreach(f: (([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)) => Unit): Unit
Applies a function f to all elements of this RDD.
Applies a function f to all elements of this RDD.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  52. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#foreachPartition\(f:Iterator\[T\]=>Unit\):Unit "Permalink") def foreachPartition(f: (Iterator[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]) => Unit): Unit
Applies a function f to each partition of this RDD.
Applies a function f to each partition of this RDD.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  53. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#getCheckpointFile:Option\[String\] "Permalink") def getCheckpointFile: Option[String]
Gets the name of the directory to which this RDD was checkpointed.
Gets the name of the directory to which this RDD was checkpointed. This is not defined if the RDD is checkpointed locally.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  54. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef] 

Definition Classes
    AnyRef → Any 

Annotations
     @IntrinsicCandidate() @native()
  55. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#getDependencies:Seq\[org.apache.spark.Dependency\[_\]\] "Permalink") def getDependencies: Seq[[Dependency](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Dependency.html "org.apache.spark.Dependency")[_]]
Implemented by subclasses to return how this RDD depends on parent RDDs.
Implemented by subclasses to return how this RDD depends on parent RDDs. This method will only be called once, so it is safe to implement a time-consuming computation in it.  

Attributes
    protected  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  56. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#getNumPartitions:Int "Permalink") final  def getNumPartitions: Int
Returns the number of partitions of this RDD.
Returns the number of partitions of this RDD.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Annotations
     @Since("1.6.0")
  57. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#getOutputDeterministicLevel:org.apache.spark.rdd.DeterministicLevel.Value "Permalink") def getOutputDeterministicLevel: [rdd.DeterministicLevel.Value](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/DeterministicLevel$.html#ValueextendsOrdered\[Enumeration.this.Value\]withSerializable) 

Attributes
    protected  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Annotations
     @DeveloperApi()
  58. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#getPartitions:Array\[org.apache.spark.Partition\] "Permalink") def getPartitions: Array[[Partition](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partition.html "org.apache.spark.Partition")]
Implemented by subclasses to return the set of partitions in this RDD.
Implemented by subclasses to return the set of partitions in this RDD. This method will only be called once, so it is safe to implement a time-consuming computation in it.
The partitions in this array must satisfy the following property: `rdd.partitions.zipWithIndex.forall { case (partition, index) => partition.index == index }` 

Attributes
    protected  

Definition Classes
     [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "org.apache.spark.graphx.VertexRDD") → [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  59. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#getPreferredLocations\(split:org.apache.spark.Partition\):Seq\[String\] "Permalink") def getPreferredLocations(split: [Partition](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partition.html "org.apache.spark.Partition")): Seq[String]
Optionally overridden by subclasses to specify placement preferences.
Optionally overridden by subclasses to specify placement preferences.  

Attributes
    protected  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  60. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#getResourceProfile\(\):org.apache.spark.resource.ResourceProfile "Permalink") def getResourceProfile(): [ResourceProfile](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/resource/ResourceProfile.html "org.apache.spark.resource.ResourceProfile")
Get the ResourceProfile specified with this RDD or null if it wasn't specified.
Get the ResourceProfile specified with this RDD or null if it wasn't specified. 

returns
    
the user specified ResourceProfile or null (for Java compatibility) if none was specified 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Annotations
     @Experimental() @Since("3.1.0")
  61. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#getStorageLevel:org.apache.spark.storage.StorageLevel "Permalink") def getStorageLevel: [StorageLevel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StorageLevel.html "org.apache.spark.storage.StorageLevel")
Get the RDD's current storage level, or StorageLevel.NONE if none is set.
Get the RDD's current storage level, or StorageLevel.NONE if none is set. 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  62. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#glom\(\):org.apache.spark.rdd.RDD\[Array\[T\]\] "Permalink") def glom(): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[Array[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]]
Return an RDD created by coalescing all elements within each partition into an array.
Return an RDD created by coalescing all elements within each partition into an array.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  63. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#groupBy\[K\]\(f:T=>K,p:org.apache.spark.Partitioner\)\(implicitkt:scala.reflect.ClassTag\[K\],implicitord:Ordering\[K\]\):org.apache.spark.rdd.RDD\[\(K,Iterable\[T\]\)\] "Permalink") def groupBy[K](f: (([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)) => K, p: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner"))(implicit kt: ClassTag[K], ord: Ordering[K] = null): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, Iterable[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)])]
Return an RDD of grouped items.
Return an RDD of grouped items. Each group consists of a key and a sequence of elements mapping to that key. The ordering of elements within each group is not guaranteed, and may even differ each time the resulting RDD is evaluated.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Note
    
This operation may be very expensive. If you are grouping in order to perform an aggregation (such as a sum or average) over each key, using `PairRDDFunctions.aggregateByKey` or `PairRDDFunctions.reduceByKey` will provide much better performance.
  64. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#groupBy\[K\]\(f:T=>K,numPartitions:Int\)\(implicitkt:scala.reflect.ClassTag\[K\]\):org.apache.spark.rdd.RDD\[\(K,Iterable\[T\]\)\] "Permalink") def groupBy[K](f: (([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)) => K, numPartitions: Int)(implicit kt: ClassTag[K]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, Iterable[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)])]
Return an RDD of grouped elements.
Return an RDD of grouped elements. Each group consists of a key and a sequence of elements mapping to that key. The ordering of elements within each group is not guaranteed, and may even differ each time the resulting RDD is evaluated.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Note
    
This operation may be very expensive. If you are grouping in order to perform an aggregation (such as a sum or average) over each key, using `PairRDDFunctions.aggregateByKey` or `PairRDDFunctions.reduceByKey` will provide much better performance.
  65. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#groupBy\[K\]\(f:T=>K\)\(implicitkt:scala.reflect.ClassTag\[K\]\):org.apache.spark.rdd.RDD\[\(K,Iterable\[T\]\)\] "Permalink") def groupBy[K](f: (([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)) => K)(implicit kt: ClassTag[K]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, Iterable[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)])]
Return an RDD of grouped items.
Return an RDD of grouped items. Each group consists of a key and a sequence of elements mapping to that key. The ordering of elements within each group is not guaranteed, and may even differ each time the resulting RDD is evaluated.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Note
    
This operation may be very expensive. If you are grouping in order to perform an aggregation (such as a sum or average) over each key, using `PairRDDFunctions.aggregateByKey` or `PairRDDFunctions.reduceByKey` will provide much better performance.
  66. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#hashCode\(\):Int "Permalink") def hashCode(): Int 

Definition Classes
    AnyRef → Any 

Annotations
     @IntrinsicCandidate() @native()
  67. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#id:Int "Permalink") val id: Int
A unique ID for this RDD (within its SparkContext).
A unique ID for this RDD (within its SparkContext). 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  68. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#initializeLogIfNecessary\(isInterpreter:Boolean,silent:Boolean\):Boolean "Permalink") def initializeLogIfNecessary(isInterpreter: Boolean, silent: Boolean): Boolean 

Attributes
    protected  

Definition Classes
    Logging
  69. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#initializeLogIfNecessary\(isInterpreter:Boolean\):Unit "Permalink") def initializeLogIfNecessary(isInterpreter: Boolean): Unit 

Attributes
    protected  

Definition Classes
    Logging
  70. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#intersection\(other:org.apache.spark.rdd.RDD\[T\],numPartitions:Int\):org.apache.spark.rdd.RDD\[T\] "Permalink") def intersection(other: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)], numPartitions: Int): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]
Return the intersection of this RDD and another one.
Return the intersection of this RDD and another one. The output will not contain any duplicate elements, even if the input RDDs did. Performs a hash partition across the cluster  

numPartitions
    
How many partitions to use in the resulting RDD 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Note
    
This method performs a shuffle internally.
  71. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#intersection\(other:org.apache.spark.rdd.RDD\[T\],partitioner:org.apache.spark.Partitioner\)\(implicitord:Ordering\[T\]\):org.apache.spark.rdd.RDD\[T\] "Permalink") def intersection(other: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)], partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner"))(implicit ord: Ordering[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)] = null): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]
Return the intersection of this RDD and another one.
Return the intersection of this RDD and another one. The output will not contain any duplicate elements, even if the input RDDs did.  

partitioner
    
Partitioner to use for the resulting RDD 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Note
    
This method performs a shuffle internally.
  72. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#intersection\(other:org.apache.spark.rdd.RDD\[T\]\):org.apache.spark.rdd.RDD\[T\] "Permalink") def intersection(other: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]
Return the intersection of this RDD and another one.
Return the intersection of this RDD and another one. The output will not contain any duplicate elements, even if the input RDDs did.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Note
    
This method performs a shuffle internally.
  73. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#isBarrier_:Boolean "Permalink") lazy val isBarrier_: Boolean 

Attributes
    protected  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Annotations
     @transient()
  74. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#isCheckpointed:Boolean "Permalink") def isCheckpointed: Boolean
Return whether this RDD is checkpointed and materialized, either reliably or locally.
Return whether this RDD is checkpointed and materialized, either reliably or locally.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  75. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#isEmpty\(\):Boolean "Permalink") def isEmpty(): Boolean 

returns
    
true if and only if the RDD contains no elements at all. Note that an RDD may be empty even when it has at least 1 partition. 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Note
    
Due to complications in the internal implementation, this method will raise an exception if called on an RDD of `Nothing` or `Null`. This may be come up in practice because, for example, the type of `parallelize(Seq())` is `RDD[Nothing]`. (`parallelize(Seq())` should be avoided anyway in favor of `parallelize(Seq[T]())`.)
  76. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean 

Definition Classes
    Any
  77. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#isTraceEnabled\(\):Boolean "Permalink") def isTraceEnabled(): Boolean 

Attributes
    protected  

Definition Classes
    Logging
  78. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#iterator\(split:org.apache.spark.Partition,context:org.apache.spark.TaskContext\):Iterator\[T\] "Permalink") final  def iterator(split: [Partition](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partition.html "org.apache.spark.Partition"), context: [TaskContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskContext.html "org.apache.spark.TaskContext")): Iterator[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]
Internal method to this RDD; will read from cache if applicable, or otherwise compute it.
Internal method to this RDD; will read from cache if applicable, or otherwise compute it. This should _not_ be called by users directly, but is available for implementers of custom subclasses of RDD.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  79. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#keyBy\[K\]\(f:T=>K\):org.apache.spark.rdd.RDD\[\(K,T\)\] "Permalink") def keyBy[K](f: (([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)) => K): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, ([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD))]
Creates tuples of the elements in this RDD by applying `f`.
Creates tuples of the elements in this RDD by applying `f`.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  80. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#localCheckpoint\(\):RDD.this.type "Permalink") def localCheckpoint(): [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "org.apache.spark.graphx.VertexRDD").this.type
Mark this RDD for local checkpointing using Spark's existing caching layer.
Mark this RDD for local checkpointing using Spark's existing caching layer.
This method is for users who wish to truncate RDD lineages while skipping the expensive step of replicating the materialized data in a reliable distributed file system. This is useful for RDDs with long lineages that need to be truncated periodically (e.g. GraphX).
Local checkpointing sacrifices fault-tolerance for performance. In particular, checkpointed data is written to ephemeral local storage in the executors instead of to a reliable, fault-tolerant storage. The effect is that if an executor fails during the computation, the checkpointed data may no longer be accessible, causing an irrecoverable job failure.
This is NOT safe to use with dynamic allocation, which removes executors along with their cached blocks. If you must use both features, you are advised to set `spark.dynamicAllocation.cachedExecutorIdleTimeout` to a high value.
The checkpoint directory set through `SparkContext#setCheckpointDir` is not used.
The data is only checkpointed when `doCheckpoint()` is called, and this only happens at the end of the first action execution on this RDD. The final data that is checkpointed after the first action may be different from the data that was used during the action, due to non-determinism of the underlying operation and retries. If the purpose of the checkpoint is to achieve saving a deterministic snapshot of the data, an eager action may need to be called first on the RDD to trigger the checkpoint.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  81. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#log:org.slf4j.Logger "Permalink") def log: Logger 

Attributes
    protected  

Definition Classes
    Logging
  82. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#logBasedOnLevel\(level:org.slf4j.event.Level\)\(f:=>org.apache.spark.internal.MessageWithContext\):Unit "Permalink") def logBasedOnLevel(level: Level)(f: => MessageWithContext): Unit 

Attributes
    protected  

Definition Classes
    Logging
  83. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#logDebug\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logDebug(msg: => String, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  84. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#logDebug\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logDebug(entry: LogEntry, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  85. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#logDebug\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logDebug(entry: LogEntry): Unit 

Attributes
    protected  

Definition Classes
    Logging
  86. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#logDebug\(msg:=>String\):Unit "Permalink") def logDebug(msg: => String): Unit 

Attributes
    protected  

Definition Classes
    Logging
  87. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#logError\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logError(msg: => String, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  88. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#logError\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logError(entry: LogEntry, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  89. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#logError\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logError(entry: LogEntry): Unit 

Attributes
    protected  

Definition Classes
    Logging
  90. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#logError\(msg:=>String\):Unit "Permalink") def logError(msg: => String): Unit 

Attributes
    protected  

Definition Classes
    Logging
  91. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#logInfo\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logInfo(msg: => String, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  92. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#logInfo\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logInfo(entry: LogEntry, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  93. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#logInfo\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logInfo(entry: LogEntry): Unit 

Attributes
    protected  

Definition Classes
    Logging
  94. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#logInfo\(msg:=>String\):Unit "Permalink") def logInfo(msg: => String): Unit 

Attributes
    protected  

Definition Classes
    Logging
  95. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#logName:String "Permalink") def logName: [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String") 

Attributes
    protected  

Definition Classes
    Logging
  96. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#logTrace\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logTrace(msg: => String, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  97. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#logTrace\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logTrace(entry: LogEntry, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  98. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#logTrace\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logTrace(entry: LogEntry): Unit 

Attributes
    protected  

Definition Classes
    Logging
  99. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#logTrace\(msg:=>String\):Unit "Permalink") def logTrace(msg: => String): Unit 

Attributes
    protected  

Definition Classes
    Logging
  100. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#logWarning\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logWarning(msg: => String, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  101. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#logWarning\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logWarning(entry: LogEntry, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  102. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#logWarning\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logWarning(entry: LogEntry): Unit 

Attributes
    protected  

Definition Classes
    Logging
  103. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#logWarning\(msg:=>String\):Unit "Permalink") def logWarning(msg: => String): Unit 

Attributes
    protected  

Definition Classes
    Logging
  104. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#map\[U\]\(f:T=>U\)\(implicitevidence$3:scala.reflect.ClassTag\[U\]\):org.apache.spark.rdd.RDD\[U\] "Permalink") def map[U](f: (([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)) => U)(implicit arg0: ClassTag[U]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[U]
Return a new RDD by applying a function to all elements of this RDD.
Return a new RDD by applying a function to all elements of this RDD.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  105. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#mapPartitions\[U\]\(f:Iterator\[T\]=>Iterator\[U\],preservesPartitioning:Boolean\)\(implicitevidence$6:scala.reflect.ClassTag\[U\]\):org.apache.spark.rdd.RDD\[U\] "Permalink") def mapPartitions[U](f: (Iterator[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]) => Iterator[U], preservesPartitioning: Boolean = false)(implicit arg0: ClassTag[U]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[U]
Return a new RDD by applying a function to each partition of this RDD.
Return a new RDD by applying a function to each partition of this RDD.
`preservesPartitioning` indicates whether the input function preserves the partitioner, which should be `false` unless this is a pair RDD and the input function doesn't modify the keys.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  106. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#mapPartitionsWithEvaluator\[U\]\(evaluatorFactory:org.apache.spark.PartitionEvaluatorFactory\[T,U\]\)\(implicitevidence$10:scala.reflect.ClassTag\[U\]\):org.apache.spark.rdd.RDD\[U\] "Permalink") def mapPartitionsWithEvaluator[U](evaluatorFactory: [PartitionEvaluatorFactory](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/PartitionEvaluatorFactory.html "org.apache.spark.PartitionEvaluatorFactory")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD), U])(implicit arg0: ClassTag[U]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[U]
Return a new RDD by applying an evaluator to each partition of this RDD.
Return a new RDD by applying an evaluator to each partition of this RDD. The given evaluator factory will be serialized and sent to executors, and each task will create an evaluator with the factory, and use the evaluator to transform the data of the input partition.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Annotations
     @DeveloperApi() @Since("3.5.0")
  107. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#mapPartitionsWithIndex\[U\]\(f:\(Int,Iterator\[T\]\)=>Iterator\[U\],preservesPartitioning:Boolean\)\(implicitevidence$9:scala.reflect.ClassTag\[U\]\):org.apache.spark.rdd.RDD\[U\] "Permalink") def mapPartitionsWithIndex[U](f: (Int, Iterator[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]) => Iterator[U], preservesPartitioning: Boolean = false)(implicit arg0: ClassTag[U]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[U]
Return a new RDD by applying a function to each partition of this RDD, while tracking the index of the original partition.
Return a new RDD by applying a function to each partition of this RDD, while tracking the index of the original partition.
`preservesPartitioning` indicates whether the input function preserves the partitioner, which should be `false` unless this is a pair RDD and the input function doesn't modify the keys.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  108. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#max\(\)\(implicitord:Ordering\[T\]\):T "Permalink") def max()(implicit ord: Ordering[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]): ([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)
Returns the max of this RDD as defined by the implicit Ordering[T].
Returns the max of this RDD as defined by the implicit Ordering[T]. 

returns
    
the maximum element of the RDD 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  109. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#min\(\)\(implicitord:Ordering\[T\]\):T "Permalink") def min()(implicit ord: Ordering[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]): ([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)
Returns the min of this RDD as defined by the implicit Ordering[T].
Returns the min of this RDD as defined by the implicit Ordering[T]. 

returns
    
the minimum element of the RDD 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  110. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#name:String "Permalink") var name: String
A friendly name for this RDD
A friendly name for this RDD 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  111. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  112. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#notify\(\):Unit "Permalink") final  def notify(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  113. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  114. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#parent\[U\]\(j:Int\)\(implicitevidence$37:scala.reflect.ClassTag\[U\]\):org.apache.spark.rdd.RDD\[U\] "Permalink") def parent[U](j: Int)(implicit arg0: ClassTag[U]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[U]
Returns the jth parent RDD: e.g.
Returns the jth parent RDD: e.g. rdd.parent[T](0) is equivalent to rdd.firstParent[T] 

Attributes
    protected[[spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")]  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  115. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#partitioner:Option\[org.apache.spark.Partitioner\] "Permalink") val partitioner: Option[[Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner")]
Optionally overridden by subclasses to specify how they are partitioned.
Optionally overridden by subclasses to specify how they are partitioned. 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  116. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#partitions:Array\[org.apache.spark.Partition\] "Permalink") final  def partitions: Array[[Partition](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partition.html "org.apache.spark.Partition")]
Get the array of partitions of this RDD, taking into account whether the RDD is checkpointed or not.
Get the array of partitions of this RDD, taking into account whether the RDD is checkpointed or not.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  117. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#persist\(\):RDD.this.type "Permalink") def persist(): [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "org.apache.spark.graphx.VertexRDD").this.type
Persist this RDD with the default storage level (`MEMORY_ONLY`).
Persist this RDD with the default storage level (`MEMORY_ONLY`).  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  118. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#persist\(newLevel:org.apache.spark.storage.StorageLevel\):RDD.this.type "Permalink") def persist(newLevel: [StorageLevel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StorageLevel.html "org.apache.spark.storage.StorageLevel")): [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "org.apache.spark.graphx.VertexRDD").this.type
Set this RDD's storage level to persist its values across operations after the first time it is computed.
Set this RDD's storage level to persist its values across operations after the first time it is computed. This can only be used to assign a new storage level if the RDD does not have a storage level set yet. Local checkpointing is an exception.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  119. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#pipe\(command:Seq\[String\],env:scala.collection.Map\[String,String\],printPipeContext:\(String=>Unit\)=>Unit,printRDDElement:\(T,String=>Unit\)=>Unit,separateWorkingDir:Boolean,bufferSize:Int,encoding:String\):org.apache.spark.rdd.RDD\[String\] "Permalink") def pipe(command: Seq[String], env: Map[String, String] = Map(), printPipeContext: ((String) => Unit) => Unit = null, printRDDElement: (([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD), (String) => Unit) => Unit = null, separateWorkingDir: Boolean = false, bufferSize: Int = 8192, encoding: String = Codec.defaultCharsetCodec.name): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[String]
Return an RDD created by piping elements to a forked external process.
Return an RDD created by piping elements to a forked external process. The resulting RDD is computed by executing the given process once per partition. All elements of each input partition are written to a process's stdin as lines of input separated by a newline. The resulting partition consists of the process's stdout output, with each line of stdout resulting in one element of the output partition. A process is invoked even for empty partitions.
The print behavior can be customized by providing two functions.  

command
    
command to run in forked process. 

env
    
environment variables to set. 

printPipeContext
    
Before piping elements, this function is called as an opportunity to pipe context data. Print line function (like out.println) will be passed as printPipeContext's parameter. 

printRDDElement
    
Use this function to customize how to pipe elements. This function will be called with each RDD element as the 1st parameter, and the print line function (like out.println()) as the 2nd parameter. An example of pipe the RDD data of groupBy() in a streaming way, instead of constructing a huge String to concat all the elements:

```
def printRDDElement(record:(String, Seq[String]), f:String=>Unit) =
  for (e <- record._2) {f(e)}
```


separateWorkingDir
    
Use separate working directories for each task. 

bufferSize
    
Buffer size for the stdin writer for the piped process. 

encoding
    
Char encoding used for interacting (via stdin, stdout and stderr) with the piped process 

returns
    
the result RDD 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  120. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#pipe\(command:String,env:scala.collection.Map\[String,String\]\):org.apache.spark.rdd.RDD\[String\] "Permalink") def pipe(command: String, env: Map[String, String]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[String]
Return an RDD created by piping elements to a forked external process.
Return an RDD created by piping elements to a forked external process.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  121. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#pipe\(command:String\):org.apache.spark.rdd.RDD\[String\] "Permalink") def pipe(command: String): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[String]
Return an RDD created by piping elements to a forked external process.
Return an RDD created by piping elements to a forked external process.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  122. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#preferredLocations\(split:org.apache.spark.Partition\):Seq\[String\] "Permalink") final  def preferredLocations(split: [Partition](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partition.html "org.apache.spark.Partition")): Seq[String]
Get the preferred locations of a partition, taking into account whether the RDD is checkpointed.
Get the preferred locations of a partition, taking into account whether the RDD is checkpointed.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  123. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#randomSplit\(weights:Array\[Double\],seed:Long\):Array\[org.apache.spark.rdd.RDD\[T\]\] "Permalink") def randomSplit(weights: Array[Double], seed: Long = [Utils.random.nextLong](https://spark.apache.org/docs/latest/api/scala/org/index.html)): Array[[RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]]
Randomly splits this RDD with the provided weights.
Randomly splits this RDD with the provided weights.  

weights
    
weights for splits, will be normalized if they don't sum to 1 

seed
    
random seed 

returns
    
split RDDs in an array 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  124. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#reduce\(f:\(T,T\)=>T\):T "Permalink") def reduce(f: (([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD), ([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)) => ([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)): ([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)
Reduces the elements of this RDD using the specified commutative and associative binary operator.
Reduces the elements of this RDD using the specified commutative and associative binary operator.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  125. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#repartition\(numPartitions:Int\)\(implicitord:Ordering\[T\]\):org.apache.spark.rdd.RDD\[T\] "Permalink") def repartition(numPartitions: Int)(implicit ord: Ordering[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)] = null): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]
Return a new RDD that has exactly numPartitions partitions.
Return a new RDD that has exactly numPartitions partitions.
Can increase or decrease the level of parallelism in this RDD. Internally, this uses a shuffle to redistribute data.
If you are decreasing the number of partitions in this RDD, consider using `coalesce`, which can avoid performing a shuffle.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  126. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#sample\(withReplacement:Boolean,fraction:Double,seed:Long\):org.apache.spark.rdd.RDD\[T\] "Permalink") def sample(withReplacement: Boolean, fraction: Double, seed: Long = [Utils.random.nextLong](https://spark.apache.org/docs/latest/api/scala/org/index.html)): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]
Return a sampled subset of this RDD.
Return a sampled subset of this RDD.  

withReplacement
    
can elements be sampled multiple times (replaced when sampled out) 

fraction
    
expected size of the sample as a fraction of this RDD's size without replacement: probability that each element is chosen; fraction must be [0, 1] with replacement: expected number of times each element is chosen; fraction must be greater than or equal to 0 

seed
    
seed for the random number generator 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Note
    
This is NOT guaranteed to provide exactly the fraction of the count of the given RDD.
  127. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#saveAsObjectFile\(path:String\):Unit "Permalink") def saveAsObjectFile(path: String): Unit
Save this RDD as a SequenceFile of serialized objects.
Save this RDD as a SequenceFile of serialized objects.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  128. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#saveAsTextFile\(path:String,codec:Class\[_<:org.apache.hadoop.io.compress.CompressionCodec\]\):Unit "Permalink") def saveAsTextFile(path: String, codec: Class[_ <: CompressionCodec]): Unit
Save this RDD as a compressed text file, using string representations of elements.
Save this RDD as a compressed text file, using string representations of elements.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  129. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#saveAsTextFile\(path:String\):Unit "Permalink") def saveAsTextFile(path: String): Unit
Save this RDD as a text file, using string representations of elements.
Save this RDD as a text file, using string representations of elements.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  130. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#setName\(_name:String\):RDD.this.type "Permalink") def setName(_name: String): [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "org.apache.spark.graphx.VertexRDD").this.type
Assign a name to this RDD
Assign a name to this RDD 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  131. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#sortBy\[K\]\(f:T=>K,ascending:Boolean,numPartitions:Int\)\(implicitord:Ordering\[K\],implicitctag:scala.reflect.ClassTag\[K\]\):org.apache.spark.rdd.RDD\[T\] "Permalink") def sortBy[K](f: (([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)) => K, ascending: Boolean = true, numPartitions: Int = [this.partitions.length](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html#partitions:Array\[org.apache.spark.Partition\]))(implicit ord: Ordering[K], ctag: ClassTag[K]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]
Return this RDD sorted by the given key function.
Return this RDD sorted by the given key function.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  132. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#sparkContext:org.apache.spark.SparkContext "Permalink") def sparkContext: [SparkContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html "org.apache.spark.SparkContext")
The SparkContext that created this RDD.
The SparkContext that created this RDD. 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  133. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#subtract\(other:org.apache.spark.rdd.RDD\[T\],p:org.apache.spark.Partitioner\)\(implicitord:Ordering\[T\]\):org.apache.spark.rdd.RDD\[T\] "Permalink") def subtract(other: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)], p: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner"))(implicit ord: Ordering[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)] = null): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]
Return an RDD with the elements from `this` that are not in `other`.
Return an RDD with the elements from `this` that are not in `other`.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  134. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#subtract\(other:org.apache.spark.rdd.RDD\[T\],numPartitions:Int\):org.apache.spark.rdd.RDD\[T\] "Permalink") def subtract(other: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)], numPartitions: Int): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]
Return an RDD with the elements from `this` that are not in `other`.
Return an RDD with the elements from `this` that are not in `other`.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  135. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#subtract\(other:org.apache.spark.rdd.RDD\[T\]\):org.apache.spark.rdd.RDD\[T\] "Permalink") def subtract(other: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]
Return an RDD with the elements from `this` that are not in `other`.
Return an RDD with the elements from `this` that are not in `other`.
Uses `this` partitioner/partition size, because even if `other` is huge, the resulting RDD will be <= us.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  136. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0 

Definition Classes
    AnyRef
  137. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#take\(num:Int\):Array\[T\] "Permalink") def take(num: Int): Array[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]
Take the first num elements of the RDD.
Take the first num elements of the RDD. It works by first scanning one partition, and use the results from that partition to estimate the number of additional partitions needed to satisfy the limit.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Note
    
This method should only be used if the resulting array is expected to be small, as all the data is loaded into the driver's memory.
, 
Due to complications in the internal implementation, this method will raise an exception if called on an RDD of `Nothing` or `Null`.
  138. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#takeOrdered\(num:Int\)\(implicitord:Ordering\[T\]\):Array\[T\] "Permalink") def takeOrdered(num: Int)(implicit ord: Ordering[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]): Array[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]
Returns the first k (smallest) elements from this RDD as defined by the specified implicit Ordering[T] and maintains the ordering.
Returns the first k (smallest) elements from this RDD as defined by the specified implicit Ordering[T] and maintains the ordering. This does the opposite of [top](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#top\(num:Int\)\(implicitord:Ordering\[T\]\):Array\[T\]). For example:

```
sc.parallelize(Seq(10, 4, 2, 12, 3)).takeOrdered(1)
// returns Array(2)

sc.parallelize(Seq(2, 3, 4, 5, 6)).takeOrdered(2)
// returns Array(2, 3)
```


num
    
k, the number of elements to return 

ord
    
the implicit ordering for T 

returns
    
an array of top elements 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Note
    
This method should only be used if the resulting array is expected to be small, as all the data is loaded into the driver's memory.
  139. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#takeSample\(withReplacement:Boolean,num:Int,seed:Long\):Array\[T\] "Permalink") def takeSample(withReplacement: Boolean, num: Int, seed: Long = [Utils.random.nextLong](https://spark.apache.org/docs/latest/api/scala/org/index.html)): Array[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]
Return a fixed-size sampled subset of this RDD in an array 
Return a fixed-size sampled subset of this RDD in an array  

withReplacement
    
whether sampling is done with replacement 

num
    
size of the returned sample 

seed
    
seed for the random number generator 

returns
    
sample of specified size in an array 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Note
    
this method should only be used if the resulting array is expected to be small, as all the data is loaded into the driver's memory.
  140. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#toDebugString:String "Permalink") def toDebugString: String
A description of this RDD and its recursive dependencies for debugging.
A description of this RDD and its recursive dependencies for debugging. 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  141. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#toJavaRDD\(\):org.apache.spark.api.java.JavaRDD\[T\] "Permalink") def toJavaRDD(): [JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)] 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  142. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#toLocalIterator:Iterator\[T\] "Permalink") def toLocalIterator: Iterator[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]
Return an iterator that contains all of the elements in this RDD.
Return an iterator that contains all of the elements in this RDD.
The iterator will consume as much memory as the largest partition in this RDD.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Note
    
This results in multiple Spark jobs, and if the input RDD is the result of a wide transformation (e.g. join with different partitioners), to avoid recomputing the input RDD should be cached first.
  143. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#toString\(\):String "Permalink") def toString(): String 

Definition Classes
     [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") → AnyRef → Any
  144. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#top\(num:Int\)\(implicitord:Ordering\[T\]\):Array\[T\] "Permalink") def top(num: Int)(implicit ord: Ordering[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]): Array[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]
Returns the top k (largest) elements from this RDD as defined by the specified implicit Ordering[T] and maintains the ordering.
Returns the top k (largest) elements from this RDD as defined by the specified implicit Ordering[T] and maintains the ordering. This does the opposite of [takeOrdered](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#takeOrdered\(num:Int\)\(implicitord:Ordering\[T\]\):Array\[T\]). For example:

```
sc.parallelize(Seq(10, 4, 2, 12, 3)).top(1)
// returns Array(12)

sc.parallelize(Seq(2, 3, 4, 5, 6)).top(2)
// returns Array(6, 5)
```


num
    
k, the number of top elements to return 

ord
    
the implicit ordering for T 

returns
    
an array of top elements 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Note
    
This method should only be used if the resulting array is expected to be small, as all the data is loaded into the driver's memory.
  145. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#treeAggregate\[U\]\(zeroValue:U,seqOp:\(U,T\)=>U,combOp:\(U,U\)=>U,depth:Int,finalAggregateOnExecutor:Boolean\)\(implicitevidence$35:scala.reflect.ClassTag\[U\]\):U "Permalink") def treeAggregate[U](zeroValue: U, seqOp: (U, ([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)) => U, combOp: (U, U) => U, depth: Int, finalAggregateOnExecutor: Boolean)(implicit arg0: ClassTag[U]): U
[org.apache.spark.rdd.RDD#treeAggregate](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html#treeAggregate\[U\]\(zeroValue:U,seqOp:\(U,T\)=>U,combOp:\(U,U\)=>U,depth:Int,finalAggregateOnExecutor:Boolean\)\(implicitevidence$35:scala.reflect.ClassTag\[U\]\):U) with a parameter to do the final aggregation on the executor 
[org.apache.spark.rdd.RDD#treeAggregate](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html#treeAggregate\[U\]\(zeroValue:U,seqOp:\(U,T\)=>U,combOp:\(U,U\)=>U,depth:Int,finalAggregateOnExecutor:Boolean\)\(implicitevidence$35:scala.reflect.ClassTag\[U\]\):U) with a parameter to do the final aggregation on the executor  

finalAggregateOnExecutor
    
do final aggregation on executor 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  146. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#treeAggregate\[U\]\(zeroValue:U\)\(seqOp:\(U,T\)=>U,combOp:\(U,U\)=>U,depth:Int\)\(implicitevidence$34:scala.reflect.ClassTag\[U\]\):U "Permalink") def treeAggregate[U](zeroValue: U)(seqOp: (U, ([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)) => U, combOp: (U, U) => U, depth: Int = 2)(implicit arg0: ClassTag[U]): U
Aggregates the elements of this RDD in a multi-level tree pattern.
Aggregates the elements of this RDD in a multi-level tree pattern. This method is semantically identical to [org.apache.spark.rdd.RDD#aggregate](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html#aggregate\[U\]\(zeroValue:U\)\(seqOp:\(U,T\)=>U,combOp:\(U,U\)=>U\)\(implicitevidence$33:scala.reflect.ClassTag\[U\]\):U).  

depth
    
suggested depth of the tree (default: 2) 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  147. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#treeReduce\(f:\(T,T\)=>T,depth:Int\):T "Permalink") def treeReduce(f: (([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD), ([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)) => ([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD), depth: Int = 2): ([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)
Reduces the elements of this RDD in a multi-level tree pattern.
Reduces the elements of this RDD in a multi-level tree pattern.  

depth
    
suggested depth of the tree (default: 2) 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

See also
    
[org.apache.spark.rdd.RDD#reduce](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html#reduce\(f:\(T,T\)=>T\):T)
  148. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#union\(other:org.apache.spark.rdd.RDD\[T\]\):org.apache.spark.rdd.RDD\[T\] "Permalink") def union(other: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]
Return the union of this RDD and another one.
Return the union of this RDD and another one. Any identical elements will appear multiple times (use `.distinct()` to eliminate them).  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  149. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#unpersist\(blocking:Boolean\):RDD.this.type "Permalink") def unpersist(blocking: Boolean = false): [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "org.apache.spark.graphx.VertexRDD").this.type
Mark the RDD as non-persistent, and remove all blocks for it from memory and disk.
Mark the RDD as non-persistent, and remove all blocks for it from memory and disk.  

blocking
    
Whether to block until all blocks are deleted (default: false) 

returns
    
This RDD. 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  150. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  151. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  152. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#wait\(\):Unit "Permalink") final  def wait(): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  153. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#withLogContext\(context:java.util.Map\[String,String\]\)\(body:=>Unit\):Unit "Permalink") def withLogContext(context: [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#java.util.Map "java.util.Map")[String, String])(body: => Unit): Unit 

Attributes
    protected  

Definition Classes
    Logging
  154. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#withResources\(rp:org.apache.spark.resource.ResourceProfile\):RDD.this.type "Permalink") def withResources(rp: [ResourceProfile](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/resource/ResourceProfile.html "org.apache.spark.resource.ResourceProfile")): [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "org.apache.spark.graphx.VertexRDD").this.type
Specify a ResourceProfile to use when calculating this RDD.
Specify a ResourceProfile to use when calculating this RDD. This is only supported on certain cluster managers and currently requires dynamic allocation to be enabled. It will result in new executors with the resources specified being acquired to calculate the RDD.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Annotations
     @Experimental() @Since("3.1.0")
  155. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#zip\[U\]\(other:org.apache.spark.rdd.RDD\[U\]\)\(implicitevidence$13:scala.reflect.ClassTag\[U\]\):org.apache.spark.rdd.RDD\[\(T,U\)\] "Permalink") def zip[U](other: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[U])(implicit arg0: ClassTag[U]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD), U)]
Zips this RDD with another one, returning key-value pairs with the first element in each RDD, second element in each RDD, etc.
Zips this RDD with another one, returning key-value pairs with the first element in each RDD, second element in each RDD, etc. Assumes that the two RDDs have the *same number of partitions* and the *same number of elements in each partition* (e.g. one was made through a map on the other).  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  156. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#zipPartitions\[B,C,D,V\]\(rdd2:org.apache.spark.rdd.RDD\[B\],rdd3:org.apache.spark.rdd.RDD\[C\],rdd4:org.apache.spark.rdd.RDD\[D\]\)\(f:\(Iterator\[T\],Iterator\[B\],Iterator\[C\],Iterator\[D\]\)=>Iterator\[V\]\)\(implicitevidence$28:scala.reflect.ClassTag\[B\],implicitevidence$29:scala.reflect.ClassTag\[C\],implicitevidence$30:scala.reflect.ClassTag\[D\],implicitevidence$31:scala.reflect.ClassTag\[V\]\):org.apache.spark.rdd.RDD\[V\] "Permalink") def zipPartitions[B, C, D, V](rdd2: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[B], rdd3: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[C], rdd4: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[D])(f: (Iterator[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)], Iterator[B], Iterator[C], Iterator[D]) => Iterator[V])(implicit arg0: ClassTag[B], arg1: ClassTag[C], arg2: ClassTag[D], arg3: ClassTag[V]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[V] 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  157. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#zipPartitions\[B,C,D,V\]\(rdd2:org.apache.spark.rdd.RDD\[B\],rdd3:org.apache.spark.rdd.RDD\[C\],rdd4:org.apache.spark.rdd.RDD\[D\],preservesPartitioning:Boolean\)\(f:\(Iterator\[T\],Iterator\[B\],Iterator\[C\],Iterator\[D\]\)=>Iterator\[V\]\)\(implicitevidence$24:scala.reflect.ClassTag\[B\],implicitevidence$25:scala.reflect.ClassTag\[C\],implicitevidence$26:scala.reflect.ClassTag\[D\],implicitevidence$27:scala.reflect.ClassTag\[V\]\):org.apache.spark.rdd.RDD\[V\] "Permalink") def zipPartitions[B, C, D, V](rdd2: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[B], rdd3: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[C], rdd4: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[D], preservesPartitioning: Boolean)(f: (Iterator[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)], Iterator[B], Iterator[C], Iterator[D]) => Iterator[V])(implicit arg0: ClassTag[B], arg1: ClassTag[C], arg2: ClassTag[D], arg3: ClassTag[V]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[V] 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  158. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#zipPartitions\[B,C,V\]\(rdd2:org.apache.spark.rdd.RDD\[B\],rdd3:org.apache.spark.rdd.RDD\[C\]\)\(f:\(Iterator\[T\],Iterator\[B\],Iterator\[C\]\)=>Iterator\[V\]\)\(implicitevidence$21:scala.reflect.ClassTag\[B\],implicitevidence$22:scala.reflect.ClassTag\[C\],implicitevidence$23:scala.reflect.ClassTag\[V\]\):org.apache.spark.rdd.RDD\[V\] "Permalink") def zipPartitions[B, C, V](rdd2: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[B], rdd3: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[C])(f: (Iterator[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)], Iterator[B], Iterator[C]) => Iterator[V])(implicit arg0: ClassTag[B], arg1: ClassTag[C], arg2: ClassTag[V]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[V] 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  159. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#zipPartitions\[B,C,V\]\(rdd2:org.apache.spark.rdd.RDD\[B\],rdd3:org.apache.spark.rdd.RDD\[C\],preservesPartitioning:Boolean\)\(f:\(Iterator\[T\],Iterator\[B\],Iterator\[C\]\)=>Iterator\[V\]\)\(implicitevidence$18:scala.reflect.ClassTag\[B\],implicitevidence$19:scala.reflect.ClassTag\[C\],implicitevidence$20:scala.reflect.ClassTag\[V\]\):org.apache.spark.rdd.RDD\[V\] "Permalink") def zipPartitions[B, C, V](rdd2: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[B], rdd3: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[C], preservesPartitioning: Boolean)(f: (Iterator[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)], Iterator[B], Iterator[C]) => Iterator[V])(implicit arg0: ClassTag[B], arg1: ClassTag[C], arg2: ClassTag[V]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[V] 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  160. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#zipPartitions\[B,V\]\(rdd2:org.apache.spark.rdd.RDD\[B\]\)\(f:\(Iterator\[T\],Iterator\[B\]\)=>Iterator\[V\]\)\(implicitevidence$16:scala.reflect.ClassTag\[B\],implicitevidence$17:scala.reflect.ClassTag\[V\]\):org.apache.spark.rdd.RDD\[V\] "Permalink") def zipPartitions[B, V](rdd2: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[B])(f: (Iterator[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)], Iterator[B]) => Iterator[V])(implicit arg0: ClassTag[B], arg1: ClassTag[V]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[V] 

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  161. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#zipPartitions\[B,V\]\(rdd2:org.apache.spark.rdd.RDD\[B\],preservesPartitioning:Boolean\)\(f:\(Iterator\[T\],Iterator\[B\]\)=>Iterator\[V\]\)\(implicitevidence$14:scala.reflect.ClassTag\[B\],implicitevidence$15:scala.reflect.ClassTag\[V\]\):org.apache.spark.rdd.RDD\[V\] "Permalink") def zipPartitions[B, V](rdd2: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[B], preservesPartitioning: Boolean)(f: (Iterator[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)], Iterator[B]) => Iterator[V])(implicit arg0: ClassTag[B], arg1: ClassTag[V]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[V]
Zip this RDD's partitions with one (or more) RDD(s) and return a new RDD by applying a function to the zipped partitions.
Zip this RDD's partitions with one (or more) RDD(s) and return a new RDD by applying a function to the zipped partitions. Assumes that all the RDDs have the *same number of partitions*, but does *not* require them to have the same number of elements in each partition.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")
  162. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#zipPartitionsWithEvaluator\[U\]\(rdd2:org.apache.spark.rdd.RDD\[T\],evaluatorFactory:org.apache.spark.PartitionEvaluatorFactory\[T,U\]\)\(implicitevidence$11:scala.reflect.ClassTag\[U\]\):org.apache.spark.rdd.RDD\[U\] "Permalink") def zipPartitionsWithEvaluator[U](rdd2: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)], evaluatorFactory: [PartitionEvaluatorFactory](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/PartitionEvaluatorFactory.html "org.apache.spark.PartitionEvaluatorFactory")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD), U])(implicit arg0: ClassTag[U]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[U]
Zip this RDD's partitions with another RDD and return a new RDD by applying an evaluator to the zipped partitions.
Zip this RDD's partitions with another RDD and return a new RDD by applying an evaluator to the zipped partitions. Assumes that the two RDDs have the *same number of partitions*, but does *not* require them to have the same number of elements in each partition.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Annotations
     @DeveloperApi() @Since("3.5.0")
  163. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#zipWithIndex\(\):org.apache.spark.rdd.RDD\[\(T,Long\)\] "Permalink") def zipWithIndex(): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD), Long)]
Zips this RDD with its element indices.
Zips this RDD with its element indices. The ordering is first based on the partition index and then the ordering of items within each partition. So the first item in the first partition gets index 0, and the last item in the last partition receives the largest index.
This is similar to Scala's zipWithIndex but it uses Long instead of Int as the index type. This method needs to trigger a spark job when this RDD contains more than one partitions.  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Note
    
Some RDDs, such as those returned by groupBy(), do not guarantee order of elements in a partition. The index assigned to each element is therefore not guaranteed, and may even change if the RDD is reevaluated. If a fixed ordering is required to guarantee the same index assignments, you should sort the RDD with sortByKey() or save it to a file.
  164. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#zipWithUniqueId\(\):org.apache.spark.rdd.RDD\[\(T,Long\)\] "Permalink") def zipWithUniqueId(): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD), Long)]
Zips this RDD with generated unique Long ids.
Zips this RDD with generated unique Long ids. Items in the kth partition will get ids k, n+k, 2*n+k, ..., where n is the number of partitions. So there may exist gaps, but this method won't trigger a spark job, which is different from [org.apache.spark.rdd.RDD#zipWithIndex](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html#zipWithIndex\(\):org.apache.spark.rdd.RDD\[\(T,Long\)\]).  

Definition Classes
    [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") 

Note
    
Some RDDs, such as those returned by groupBy(), do not guarantee order of elements in a partition. The unique ID assigned to each element is therefore not guaranteed, and may even change if the RDD is reevaluated. If a fixed ordering is required to guarantee the same index assignments, you should sort the RDD with sortByKey() or save it to a file.
  165. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html#finalize\(\):Unit "Permalink") def finalize(): Unit 

Attributes
    protected[lang]  

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.Throwable]) @Deprecated 

Deprecated
    
_(Since version 9)_


