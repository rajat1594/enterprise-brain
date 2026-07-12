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

[o](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "See companion class")
[org](https://spark.apache.org/docs/latest/api/scala/org/index.html "org").[apache](https://spark.apache.org/docs/latest/api/scala/org/apache/index.html "org.apache").[spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark").[graphx](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html "org.apache.spark.graphx")
#  [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "See companion class")[ __](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph$.html "Permalink")
###
Companion [class Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "See companion class")
####  object Graph extends [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable")
The Graph object contains a collection of routines used to construct graphs from RDDs.

Source
    [Graph.scala](https://github.com/apache/spark/tree/v4.1.2/graphx/src/main/scala/org/apache/spark/graphx/Graph.scala)
Linear Supertypes
[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable"), AnyRef, Any
__ __
Ordering
  1. Alphabetic
  2. By Inheritance

Inherited

  1. Graph
  2. Serializable
  3. AnyRef
  4. Any

  1. Hide All
  2. Show All

Visibility
  1. Public
  2. Protected

### Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph$.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph$.html###:Int "Permalink") final  def ##: Int

Definition Classes
    AnyRef → Any
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph$.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph$.html#apply\[VD,ED\]\(vertices:org.apache.spark.rdd.RDD\[\(org.apache.spark.graphx.VertexId,VD\)\],edges:org.apache.spark.rdd.RDD\[org.apache.spark.graphx.Edge\[ED\]\],defaultVertexAttr:VD,edgeStorageLevel:org.apache.spark.storage.StorageLevel,vertexStorageLevel:org.apache.spark.storage.StorageLevel\)\(implicitevidence$18:scala.reflect.ClassTag\[VD\],implicitevidence$19:scala.reflect.ClassTag\[ED\]\):org.apache.spark.graphx.Graph\[VD,ED\] "Permalink") def apply[VD, ED](vertices: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)], edges: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[[Edge](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html "org.apache.spark.graphx.Edge")[ED]], defaultVertexAttr: VD = null.asInstanceOf[VD], edgeStorageLevel: [StorageLevel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StorageLevel.html "org.apache.spark.storage.StorageLevel") = [StorageLevel.MEMORY_ONLY](https://spark.apache.org/docs/latest/api/scala/org/index.html), vertexStorageLevel: [StorageLevel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StorageLevel.html "org.apache.spark.storage.StorageLevel") = [StorageLevel.MEMORY_ONLY](https://spark.apache.org/docs/latest/api/scala/org/index.html))(implicit arg0: ClassTag[VD], arg1: ClassTag[ED]): [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[VD, ED]
Construct a graph from a collection of vertices and edges with attributes.
Construct a graph from a collection of vertices and edges with attributes. Duplicate vertices are picked arbitrarily and vertices found in the edge collection but not in the input vertices are assigned the default attribute.

VD

the vertex attribute type

ED

the edge attribute type

vertices

the "set" of vertices and their attributes

edges

the collection of edges in the graph

defaultVertexAttr

the default vertex attribute to use for vertices that are mentioned in edges but not in vertices

edgeStorageLevel

the desired storage level at which to cache the edges if necessary

vertexStorageLevel

the desired storage level at which to cache the vertices if necessary
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph$.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0

Definition Classes
    Any
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph$.html#clone\(\):Object "Permalink") def clone(): AnyRef

Attributes
    protected[lang]

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph$.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph$.html#equals\(x$1:Object\):Boolean "Permalink") def equals(arg0: AnyRef): Boolean

Definition Classes
    AnyRef → Any
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph$.html#fromEdgeTuples\[VD\]\(rawEdges:org.apache.spark.rdd.RDD\[\(org.apache.spark.graphx.VertexId,org.apache.spark.graphx.VertexId\)\],defaultValue:VD,uniqueEdges:Option\[org.apache.spark.graphx.PartitionStrategy\],edgeStorageLevel:org.apache.spark.storage.StorageLevel,vertexStorageLevel:org.apache.spark.storage.StorageLevel\)\(implicitevidence$15:scala.reflect.ClassTag\[VD\]\):org.apache.spark.graphx.Graph\[VD,Int\] "Permalink") def fromEdgeTuples[VD](rawEdges: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), [VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long))], defaultValue: VD, uniqueEdges: Option[[PartitionStrategy](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/PartitionStrategy.html "org.apache.spark.graphx.PartitionStrategy")] = None, edgeStorageLevel: [StorageLevel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StorageLevel.html "org.apache.spark.storage.StorageLevel") = [StorageLevel.MEMORY_ONLY](https://spark.apache.org/docs/latest/api/scala/org/index.html), vertexStorageLevel: [StorageLevel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StorageLevel.html "org.apache.spark.storage.StorageLevel") = [StorageLevel.MEMORY_ONLY](https://spark.apache.org/docs/latest/api/scala/org/index.html))(implicit arg0: ClassTag[VD]): [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[VD, Int]
Construct a graph from a collection of edges encoded as vertex id pairs.
Construct a graph from a collection of edges encoded as vertex id pairs.

rawEdges

a collection of edges in (src, dst) form

defaultValue

the vertex attributes with which to create vertices referenced by the edges

uniqueEdges

if multiple identical edges are found they are combined and the edge attribute is set to the sum. Otherwise duplicate edges are treated as separate. To enable `uniqueEdges`, a [PartitionStrategy](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/PartitionStrategy.html "org.apache.spark.graphx.PartitionStrategy") must be provided.

edgeStorageLevel

the desired storage level at which to cache the edges if necessary

vertexStorageLevel

the desired storage level at which to cache the vertices if necessary

returns

a graph with edge attributes containing either the count of duplicate edges or 1 (if `uniqueEdges` is `None`) and vertex attributes containing the total degree of each vertex.
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph$.html#fromEdges\[VD,ED\]\(edges:org.apache.spark.rdd.RDD\[org.apache.spark.graphx.Edge\[ED\]\],defaultValue:VD,edgeStorageLevel:org.apache.spark.storage.StorageLevel,vertexStorageLevel:org.apache.spark.storage.StorageLevel\)\(implicitevidence$16:scala.reflect.ClassTag\[VD\],implicitevidence$17:scala.reflect.ClassTag\[ED\]\):org.apache.spark.graphx.Graph\[VD,ED\] "Permalink") def fromEdges[VD, ED](edges: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[[Edge](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html "org.apache.spark.graphx.Edge")[ED]], defaultValue: VD, edgeStorageLevel: [StorageLevel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StorageLevel.html "org.apache.spark.storage.StorageLevel") = [StorageLevel.MEMORY_ONLY](https://spark.apache.org/docs/latest/api/scala/org/index.html), vertexStorageLevel: [StorageLevel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StorageLevel.html "org.apache.spark.storage.StorageLevel") = [StorageLevel.MEMORY_ONLY](https://spark.apache.org/docs/latest/api/scala/org/index.html))(implicit arg0: ClassTag[VD], arg1: ClassTag[ED]): [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[VD, ED]
Construct a graph from a collection of edges.
Construct a graph from a collection of edges.

edges

the RDD containing the set of edges in the graph

defaultValue

the default vertex attribute to use for each vertex

edgeStorageLevel

the desired storage level at which to cache the edges if necessary

vertexStorageLevel

the desired storage level at which to cache the vertices if necessary

returns

a graph with edge attributes described by `edges` and vertices given by all vertices in `edges` with value `defaultValue`
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph$.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef]

Definition Classes
    AnyRef → Any

Annotations
     @IntrinsicCandidate() @native()
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph$.html#graphToGraphOps\[VD,ED\]\(g:org.apache.spark.graphx.Graph\[VD,ED\]\)\(implicitevidence$20:scala.reflect.ClassTag\[VD\],implicitevidence$21:scala.reflect.ClassTag\[ED\]\):org.apache.spark.graphx.GraphOps\[VD,ED\] "Permalink") implicit  def graphToGraphOps[VD, ED](g: [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[VD, ED])(implicit arg0: ClassTag[VD], arg1: ClassTag[ED]): [GraphOps](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html "org.apache.spark.graphx.GraphOps")[VD, ED]
Implicitly extracts the [GraphOps](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html "org.apache.spark.graphx.GraphOps") member from a graph.
Implicitly extracts the [GraphOps](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html "org.apache.spark.graphx.GraphOps") member from a graph.
To improve modularity the Graph type only contains a small set of basic operations. All the convenience operations are defined in the [GraphOps](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html "org.apache.spark.graphx.GraphOps") class which may be shared across multiple graph implementations.
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph$.html#hashCode\(\):Int "Permalink") def hashCode(): Int

Definition Classes
    AnyRef → Any

Annotations
     @IntrinsicCandidate() @native()
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph$.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean

Definition Classes
    Any
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph$.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph$.html#notify\(\):Unit "Permalink") final  def notify(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph$.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph$.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0

Definition Classes
    AnyRef
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph$.html#toString\(\):String "Permalink") def toString(): [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String")

Definition Classes
    AnyRef → Any
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph$.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph$.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph$.html#wait\(\):Unit "Permalink") final  def wait(): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])

### Deprecated Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph$.html#finalize\(\):Unit "Permalink") def finalize(): Unit

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
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph$.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph$.html###:Int "Permalink") final  def ##: Int

Definition Classes
    AnyRef → Any
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph$.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph$.html#clone\(\):Object "Permalink") def clone(): AnyRef

Attributes
    protected[lang]

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph$.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph$.html#equals\(x$1:Object\):Boolean "Permalink") def equals(arg0: AnyRef): Boolean

Definition Classes
    AnyRef → Any
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph$.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef]

Definition Classes
    AnyRef → Any

Annotations
     @IntrinsicCandidate() @native()
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph$.html#hashCode\(\):Int "Permalink") def hashCode(): Int

Definition Classes
    AnyRef → Any

Annotations
     @IntrinsicCandidate() @native()
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph$.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph$.html#notify\(\):Unit "Permalink") final  def notify(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph$.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph$.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0

Definition Classes
    AnyRef
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph$.html#toString\(\):String "Permalink") def toString(): [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String")

Definition Classes
    AnyRef → Any
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph$.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph$.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph$.html#wait\(\):Unit "Permalink") final  def wait(): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph$.html#finalize\(\):Unit "Permalink") def finalize(): Unit

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
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph$.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0

Definition Classes
    Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph$.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean

Definition Classes
    Any

### Ungrouped
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph$.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph$.html###:Int "Permalink") final  def ##: Int

Definition Classes
    AnyRef → Any
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph$.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph$.html#apply\[VD,ED\]\(vertices:org.apache.spark.rdd.RDD\[\(org.apache.spark.graphx.VertexId,VD\)\],edges:org.apache.spark.rdd.RDD\[org.apache.spark.graphx.Edge\[ED\]\],defaultVertexAttr:VD,edgeStorageLevel:org.apache.spark.storage.StorageLevel,vertexStorageLevel:org.apache.spark.storage.StorageLevel\)\(implicitevidence$18:scala.reflect.ClassTag\[VD\],implicitevidence$19:scala.reflect.ClassTag\[ED\]\):org.apache.spark.graphx.Graph\[VD,ED\] "Permalink") def apply[VD, ED](vertices: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)], edges: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[[Edge](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html "org.apache.spark.graphx.Edge")[ED]], defaultVertexAttr: VD = null.asInstanceOf[VD], edgeStorageLevel: [StorageLevel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StorageLevel.html "org.apache.spark.storage.StorageLevel") = [StorageLevel.MEMORY_ONLY](https://spark.apache.org/docs/latest/api/scala/org/index.html), vertexStorageLevel: [StorageLevel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StorageLevel.html "org.apache.spark.storage.StorageLevel") = [StorageLevel.MEMORY_ONLY](https://spark.apache.org/docs/latest/api/scala/org/index.html))(implicit arg0: ClassTag[VD], arg1: ClassTag[ED]): [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[VD, ED]
Construct a graph from a collection of vertices and edges with attributes.
Construct a graph from a collection of vertices and edges with attributes. Duplicate vertices are picked arbitrarily and vertices found in the edge collection but not in the input vertices are assigned the default attribute.

VD

the vertex attribute type

ED

the edge attribute type

vertices

the "set" of vertices and their attributes

edges

the collection of edges in the graph

defaultVertexAttr

the default vertex attribute to use for vertices that are mentioned in edges but not in vertices

edgeStorageLevel

the desired storage level at which to cache the edges if necessary

vertexStorageLevel

the desired storage level at which to cache the vertices if necessary
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph$.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0

Definition Classes
    Any
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph$.html#clone\(\):Object "Permalink") def clone(): AnyRef

Attributes
    protected[lang]

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph$.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph$.html#equals\(x$1:Object\):Boolean "Permalink") def equals(arg0: AnyRef): Boolean

Definition Classes
    AnyRef → Any
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph$.html#fromEdgeTuples\[VD\]\(rawEdges:org.apache.spark.rdd.RDD\[\(org.apache.spark.graphx.VertexId,org.apache.spark.graphx.VertexId\)\],defaultValue:VD,uniqueEdges:Option\[org.apache.spark.graphx.PartitionStrategy\],edgeStorageLevel:org.apache.spark.storage.StorageLevel,vertexStorageLevel:org.apache.spark.storage.StorageLevel\)\(implicitevidence$15:scala.reflect.ClassTag\[VD\]\):org.apache.spark.graphx.Graph\[VD,Int\] "Permalink") def fromEdgeTuples[VD](rawEdges: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), [VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long))], defaultValue: VD, uniqueEdges: Option[[PartitionStrategy](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/PartitionStrategy.html "org.apache.spark.graphx.PartitionStrategy")] = None, edgeStorageLevel: [StorageLevel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StorageLevel.html "org.apache.spark.storage.StorageLevel") = [StorageLevel.MEMORY_ONLY](https://spark.apache.org/docs/latest/api/scala/org/index.html), vertexStorageLevel: [StorageLevel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StorageLevel.html "org.apache.spark.storage.StorageLevel") = [StorageLevel.MEMORY_ONLY](https://spark.apache.org/docs/latest/api/scala/org/index.html))(implicit arg0: ClassTag[VD]): [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[VD, Int]
Construct a graph from a collection of edges encoded as vertex id pairs.
Construct a graph from a collection of edges encoded as vertex id pairs.

rawEdges

a collection of edges in (src, dst) form

defaultValue

the vertex attributes with which to create vertices referenced by the edges

uniqueEdges

if multiple identical edges are found they are combined and the edge attribute is set to the sum. Otherwise duplicate edges are treated as separate. To enable `uniqueEdges`, a [PartitionStrategy](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/PartitionStrategy.html "org.apache.spark.graphx.PartitionStrategy") must be provided.

edgeStorageLevel

the desired storage level at which to cache the edges if necessary

vertexStorageLevel

the desired storage level at which to cache the vertices if necessary

returns

a graph with edge attributes containing either the count of duplicate edges or 1 (if `uniqueEdges` is `None`) and vertex attributes containing the total degree of each vertex.
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph$.html#fromEdges\[VD,ED\]\(edges:org.apache.spark.rdd.RDD\[org.apache.spark.graphx.Edge\[ED\]\],defaultValue:VD,edgeStorageLevel:org.apache.spark.storage.StorageLevel,vertexStorageLevel:org.apache.spark.storage.StorageLevel\)\(implicitevidence$16:scala.reflect.ClassTag\[VD\],implicitevidence$17:scala.reflect.ClassTag\[ED\]\):org.apache.spark.graphx.Graph\[VD,ED\] "Permalink") def fromEdges[VD, ED](edges: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[[Edge](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html "org.apache.spark.graphx.Edge")[ED]], defaultValue: VD, edgeStorageLevel: [StorageLevel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StorageLevel.html "org.apache.spark.storage.StorageLevel") = [StorageLevel.MEMORY_ONLY](https://spark.apache.org/docs/latest/api/scala/org/index.html), vertexStorageLevel: [StorageLevel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StorageLevel.html "org.apache.spark.storage.StorageLevel") = [StorageLevel.MEMORY_ONLY](https://spark.apache.org/docs/latest/api/scala/org/index.html))(implicit arg0: ClassTag[VD], arg1: ClassTag[ED]): [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[VD, ED]
Construct a graph from a collection of edges.
Construct a graph from a collection of edges.

edges

the RDD containing the set of edges in the graph

defaultValue

the default vertex attribute to use for each vertex

edgeStorageLevel

the desired storage level at which to cache the edges if necessary

vertexStorageLevel

the desired storage level at which to cache the vertices if necessary

returns

a graph with edge attributes described by `edges` and vertices given by all vertices in `edges` with value `defaultValue`
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph$.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef]

Definition Classes
    AnyRef → Any

Annotations
     @IntrinsicCandidate() @native()
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph$.html#graphToGraphOps\[VD,ED\]\(g:org.apache.spark.graphx.Graph\[VD,ED\]\)\(implicitevidence$20:scala.reflect.ClassTag\[VD\],implicitevidence$21:scala.reflect.ClassTag\[ED\]\):org.apache.spark.graphx.GraphOps\[VD,ED\] "Permalink") implicit  def graphToGraphOps[VD, ED](g: [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[VD, ED])(implicit arg0: ClassTag[VD], arg1: ClassTag[ED]): [GraphOps](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html "org.apache.spark.graphx.GraphOps")[VD, ED]
Implicitly extracts the [GraphOps](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html "org.apache.spark.graphx.GraphOps") member from a graph.
Implicitly extracts the [GraphOps](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html "org.apache.spark.graphx.GraphOps") member from a graph.
To improve modularity the Graph type only contains a small set of basic operations. All the convenience operations are defined in the [GraphOps](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html "org.apache.spark.graphx.GraphOps") class which may be shared across multiple graph implementations.
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph$.html#hashCode\(\):Int "Permalink") def hashCode(): Int

Definition Classes
    AnyRef → Any

Annotations
     @IntrinsicCandidate() @native()
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph$.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean

Definition Classes
    Any
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph$.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph$.html#notify\(\):Unit "Permalink") final  def notify(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph$.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph$.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0

Definition Classes
    AnyRef
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph$.html#toString\(\):String "Permalink") def toString(): [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String")

Definition Classes
    AnyRef → Any
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph$.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph$.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph$.html#wait\(\):Unit "Permalink") final  def wait(): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])
  23. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph$.html#finalize\(\):Unit "Permalink") def finalize(): Unit

Attributes
    protected[lang]

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.Throwable]) @Deprecated

Deprecated

_(Since version 9)_
