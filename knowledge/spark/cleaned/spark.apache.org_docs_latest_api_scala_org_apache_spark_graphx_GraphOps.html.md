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

c
[org](https://spark.apache.org/docs/latest/api/scala/org/index.html "org").[apache](https://spark.apache.org/docs/latest/api/scala/org/apache/index.html "org.apache").[spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark").[graphx](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html "org.apache.spark.graphx")
# GraphOps[ __](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html "Permalink")
####  class GraphOps[VD, ED] extends Serializable
Contains additional functionality for [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph"). All operations are expressed in terms of the efficient GraphX API. This class is implicitly constructed for each Graph object.

VD

the vertex attribute type

ED

the edge attribute type

Source
    [GraphOps.scala](https://github.com/apache/spark/tree/v4.1.2/graphx/src/main/scala/org/apache/spark/graphx/GraphOps.scala)
Linear Supertypes
[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable"), AnyRef, Any
__ __
Ordering
  1. Alphabetic
  2. By Inheritance

Inherited

  1. GraphOps
  2. Serializable
  3. AnyRef
  4. Any

  1. Hide All
  2. Show All

Visibility
  1. Public
  2. Protected

### Instance Constructors
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#<init>\(graph:org.apache.spark.graphx.Graph\[VD,ED\]\)\(implicitevidence$1:scala.reflect.ClassTag\[VD\],implicitevidence$2:scala.reflect.ClassTag\[ED\]\):org.apache.spark.graphx.GraphOps\[VD,ED\] "Permalink") new GraphOps(graph: [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[VD, ED])(implicit arg0: ClassTag[VD], arg1: ClassTag[ED])

### Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html###:Int "Permalink") final  def ##: Int

Definition Classes
    AnyRef → Any
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0

Definition Classes
    Any
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#clone\(\):Object "Permalink") def clone(): AnyRef

Attributes
    protected[lang]

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#collectEdges\(edgeDirection:org.apache.spark.graphx.EdgeDirection\):org.apache.spark.graphx.VertexRDD\[Array\[org.apache.spark.graphx.Edge\[ED\]\]\] "Permalink") def collectEdges(edgeDirection: [EdgeDirection](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/EdgeDirection.html "org.apache.spark.graphx.EdgeDirection")): [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "org.apache.spark.graphx.VertexRDD")[Array[[Edge](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html "org.apache.spark.graphx.Edge")[ED]]]
Returns an RDD that contains for each vertex v its local edges, i.e., the edges that are incident on v, in the user-specified direction.
Returns an RDD that contains for each vertex v its local edges, i.e., the edges that are incident on v, in the user-specified direction. Warning: note that singleton vertices, those with no edges in the given direction will not be part of the return value.

edgeDirection

the direction along which to collect the local edges of vertices

returns

the local edges for each vertex

Note

This function could be highly inefficient on power-law graphs where high degree vertices may force a large amount of information to be collected to a single location.
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#collectNeighborIds\(edgeDirection:org.apache.spark.graphx.EdgeDirection\):org.apache.spark.graphx.VertexRDD\[Array\[org.apache.spark.graphx.VertexId\]\] "Permalink") def collectNeighborIds(edgeDirection: [EdgeDirection](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/EdgeDirection.html "org.apache.spark.graphx.EdgeDirection")): [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "org.apache.spark.graphx.VertexRDD")[Array[[VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long)]]
Collect the neighbor vertex ids for each vertex.
Collect the neighbor vertex ids for each vertex.

edgeDirection

the direction along which to collect neighboring vertices

returns

the set of neighboring ids for each vertex
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#collectNeighbors\(edgeDirection:org.apache.spark.graphx.EdgeDirection\):org.apache.spark.graphx.VertexRDD\[Array\[\(org.apache.spark.graphx.VertexId,VD\)\]\] "Permalink") def collectNeighbors(edgeDirection: [EdgeDirection](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/EdgeDirection.html "org.apache.spark.graphx.EdgeDirection")): [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "org.apache.spark.graphx.VertexRDD")[Array[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]]
Collect the neighbor vertex attributes for each vertex.
Collect the neighbor vertex attributes for each vertex.

edgeDirection

the direction along which to collect neighboring vertices

returns

the vertex set of neighboring vertex attributes for each vertex

Note

This function could be highly inefficient on power-law graphs where high degree vertices may force a large amount of information to be collected to a single location.
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#connectedComponents\(maxIterations:Int\):org.apache.spark.graphx.Graph\[org.apache.spark.graphx.VertexId,ED\] "Permalink") def connectedComponents(maxIterations: Int): [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[[VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), ED]
Compute the connected component membership of each vertex and return a graph with the vertex value containing the lowest vertex id in the connected component containing that vertex.
Compute the connected component membership of each vertex and return a graph with the vertex value containing the lowest vertex id in the connected component containing that vertex.

See also

`org.apache.spark.graphx.lib.ConnectedComponents.run`
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#connectedComponents\(\):org.apache.spark.graphx.Graph\[org.apache.spark.graphx.VertexId,ED\] "Permalink") def connectedComponents(): [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[[VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), ED]
Compute the connected component membership of each vertex and return a graph with the vertex value containing the lowest vertex id in the connected component containing that vertex.
Compute the connected component membership of each vertex and return a graph with the vertex value containing the lowest vertex id in the connected component containing that vertex.

See also

`org.apache.spark.graphx.lib.ConnectedComponents.run`
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#convertToCanonicalEdges\(mergeFunc:\(ED,ED\)=>ED\):org.apache.spark.graphx.Graph\[VD,ED\] "Permalink") def convertToCanonicalEdges(mergeFunc: (ED, ED) => ED = (e1, e2) => e1): [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[VD, ED]
Convert bi-directional edges into uni-directional ones.
Convert bi-directional edges into uni-directional ones. Some graph algorithms (e.g., TriangleCount) assume that an input graph has its edges in canonical direction. This function rewrites the vertex ids of edges so that srcIds are smaller than dstIds, and merges the duplicated edges.

mergeFunc

the user defined reduce function which should be commutative and associative and is used to combine the output of the map phase

returns

the resulting graph with canonical edges
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#degrees:org.apache.spark.graphx.VertexRDD\[Int\] "Permalink") lazy val degrees: [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "org.apache.spark.graphx.VertexRDD")[Int]
The degree of each vertex in the graph.
The degree of each vertex in the graph.

Annotations
     @transient()

Note

Vertices with no edges are not returned in the resulting RDD.
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#equals\(x$1:Object\):Boolean "Permalink") def equals(arg0: AnyRef): Boolean

Definition Classes
    AnyRef → Any
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#filter\[VD2,ED2\]\(preprocess:org.apache.spark.graphx.Graph\[VD,ED\]=>org.apache.spark.graphx.Graph\[VD2,ED2\],epred:org.apache.spark.graphx.EdgeTriplet\[VD2,ED2\]=>Boolean,vpred:\(org.apache.spark.graphx.VertexId,VD2\)=>Boolean\)\(implicitevidence$4:scala.reflect.ClassTag\[VD2\],implicitevidence$5:scala.reflect.ClassTag\[ED2\]\):org.apache.spark.graphx.Graph\[VD,ED\] "Permalink") def filter[VD2, ED2](preprocess: ([Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[VD, ED]) => [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[VD2, ED2], epred: ([EdgeTriplet](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/EdgeTriplet.html "org.apache.spark.graphx.EdgeTriplet")[VD2, ED2]) => Boolean = (x: EdgeTriplet[VD2, ED2]) => true, vpred: ([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD2) => Boolean = (v: VertexId, d: VD2) => true)(implicit arg0: ClassTag[VD2], arg1: ClassTag[ED2]): [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[VD, ED]
Filter the graph by computing some values to filter on, and applying the predicates.
Filter the graph by computing some values to filter on, and applying the predicates.

VD2

vertex type the vpred operates on

ED2

edge type the epred operates on

preprocess

a function to compute new vertex and edge data before filtering

epred

edge pred to filter on after preprocess, see more details under [org.apache.spark.graphx.Graph#subgraph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html#subgraph\(epred:org.apache.spark.graphx.EdgeTriplet\[VD,ED\]=>Boolean,vpred:\(org.apache.spark.graphx.VertexId,VD\)=>Boolean\):org.apache.spark.graphx.Graph\[VD,ED\])

vpred

vertex pred to filter on after preprocess, see more details under [org.apache.spark.graphx.Graph#subgraph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html#subgraph\(epred:org.apache.spark.graphx.EdgeTriplet\[VD,ED\]=>Boolean,vpred:\(org.apache.spark.graphx.VertexId,VD\)=>Boolean\):org.apache.spark.graphx.Graph\[VD,ED\])

returns

a subgraph of the original graph, with its data unchanged
Example:
    1. This function can be used to filter the graph based on some property, without changing the vertex and edge values in your program. For example, we could remove the vertices in a graph with 0 outdegree

```
graph.filter(
  graph => {
    val degrees: VertexRDD[Int] = graph.outDegrees
    graph.outerJoinVertices(degrees) {(vid, data, deg) => deg.getOrElse(0)}
  },
  vpred = (vid: VertexId, deg:Int) => deg > 0
)
```

  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef]

Definition Classes
    AnyRef → Any

Annotations
     @IntrinsicCandidate() @native()
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#hashCode\(\):Int "Permalink") def hashCode(): Int

Definition Classes
    AnyRef → Any

Annotations
     @IntrinsicCandidate() @native()
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#inDegrees:org.apache.spark.graphx.VertexRDD\[Int\] "Permalink") lazy val inDegrees: [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "org.apache.spark.graphx.VertexRDD")[Int]
The in-degree of each vertex in the graph.
The in-degree of each vertex in the graph.

Annotations
     @transient()

Note

Vertices with no in-edges are not returned in the resulting RDD.
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean

Definition Classes
    Any
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#joinVertices\[U\]\(table:org.apache.spark.rdd.RDD\[\(org.apache.spark.graphx.VertexId,U\)\]\)\(mapFunc:\(org.apache.spark.graphx.VertexId,VD,U\)=>VD\)\(implicitevidence$3:scala.reflect.ClassTag\[U\]\):org.apache.spark.graphx.Graph\[VD,ED\] "Permalink") def joinVertices[U](table: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), U)])(mapFunc: ([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD, U) => VD)(implicit arg0: ClassTag[U]): [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[VD, ED]
Join the vertices with an RDD and then apply a function from the vertex and RDD entry to a new vertex value.
Join the vertices with an RDD and then apply a function from the vertex and RDD entry to a new vertex value. The input table should contain at most one entry for each vertex. If no entry is provided the map function is skipped and the old value is used.

U

the type of entry in the table of updates

table

the table to join with the vertices in the graph. The table should contain at most one entry for each vertex.

mapFunc

the function used to compute the new vertex values. The map function is invoked only for vertices with a corresponding entry in the table otherwise the old vertex value is used.
Example:
    1. This function is used to update the vertices with new values based on external data. For example we could add the out degree to each vertex record

```
val rawGraph: Graph[Int, Int] = GraphLoader.edgeListFile(sc, "webgraph")
  .mapVertices((_, _) => 0)
val outDeg = rawGraph.outDegrees
val graph = rawGraph.joinVertices[Int](outDeg)
  ((_, _, outDeg) => outDeg)
```

  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#notify\(\):Unit "Permalink") final  def notify(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  23. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  24. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#numEdges:Long "Permalink") lazy val numEdges: Long
The number of edges in the graph.
The number of edges in the graph.

Annotations
     @transient()
  25. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#numVertices:Long "Permalink") lazy val numVertices: Long
The number of vertices in the graph.
The number of vertices in the graph.

Annotations
     @transient()
  26. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#outDegrees:org.apache.spark.graphx.VertexRDD\[Int\] "Permalink") lazy val outDegrees: [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "org.apache.spark.graphx.VertexRDD")[Int]
The out-degree of each vertex in the graph.
The out-degree of each vertex in the graph.

Annotations
     @transient()

Note

Vertices with no out-edges are not returned in the resulting RDD.
  27. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#pageRank\(tol:Double,resetProb:Double\):org.apache.spark.graphx.Graph\[Double,Double\] "Permalink") def pageRank(tol: Double, resetProb: Double = 0.15): [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[Double, Double]
Run a dynamic version of PageRank returning a graph with vertex attributes containing the PageRank and edge attributes containing the normalized edge weight.
Run a dynamic version of PageRank returning a graph with vertex attributes containing the PageRank and edge attributes containing the normalized edge weight.

See also

[org.apache.spark.graphx.lib.PageRank$#runUntilConvergence](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#runUntilConvergence\[VD,ED\]\(graph:org.apache.spark.graphx.Graph\[VD,ED\],tol:Double,resetProb:Double\)\(implicitevidence$13:scala.reflect.ClassTag\[VD\],implicitevidence$14:scala.reflect.ClassTag\[ED\]\):org.apache.spark.graphx.Graph\[Double,Double\])
  28. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#personalizedPageRank\(src:org.apache.spark.graphx.VertexId,tol:Double,resetProb:Double\):org.apache.spark.graphx.Graph\[Double,Double\] "Permalink") def personalizedPageRank(src: [VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), tol: Double, resetProb: Double = 0.15): [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[Double, Double]
Run personalized PageRank for a given vertex, such that all random walks are started relative to the source node.
Run personalized PageRank for a given vertex, such that all random walks are started relative to the source node.

See also

[org.apache.spark.graphx.lib.PageRank$#runUntilConvergenceWithOptions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#runUntilConvergenceWithOptions\[VD,ED\]\(graph:org.apache.spark.graphx.Graph\[VD,ED\],tol:Double,resetProb:Double,srcId:Option\[org.apache.spark.graphx.VertexId\]\)\(implicitevidence$15:scala.reflect.ClassTag\[VD\],implicitevidence$16:scala.reflect.ClassTag\[ED\]\):org.apache.spark.graphx.Graph\[Double,Double\])
  29. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#pickRandomVertex\(\):org.apache.spark.graphx.VertexId "Permalink") def pickRandomVertex(): [VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long)
Picks a random vertex from the graph and returns its ID.
  30. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#pregel\[A\]\(initialMsg:A,maxIterations:Int,activeDirection:org.apache.spark.graphx.EdgeDirection\)\(vprog:\(org.apache.spark.graphx.VertexId,VD,A\)=>VD,sendMsg:org.apache.spark.graphx.EdgeTriplet\[VD,ED\]=>Iterator\[\(org.apache.spark.graphx.VertexId,A\)\],mergeMsg:\(A,A\)=>A\)\(implicitevidence$6:scala.reflect.ClassTag\[A\]\):org.apache.spark.graphx.Graph\[VD,ED\] "Permalink") def pregel[A](initialMsg: A, maxIterations: Int = Int.MaxValue, activeDirection: [EdgeDirection](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/EdgeDirection.html "org.apache.spark.graphx.EdgeDirection") = [EdgeDirection.Either](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/EdgeDirection$.html))(vprog: ([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD, A) => VD, sendMsg: ([EdgeTriplet](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/EdgeTriplet.html "org.apache.spark.graphx.EdgeTriplet")[VD, ED]) => Iterator[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), A)], mergeMsg: (A, A) => A)(implicit arg0: ClassTag[A]): [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[VD, ED]
Execute a Pregel-like iterative vertex-parallel abstraction.
Execute a Pregel-like iterative vertex-parallel abstraction. The user-defined vertex-program `vprog` is executed in parallel on each vertex receiving any inbound messages and computing a new value for the vertex. The `sendMsg` function is then invoked on all out-edges and is used to compute an optional message to the destination vertex. The `mergeMsg` function is a commutative associative function used to combine messages destined to the same vertex.
On the first iteration all vertices receive the `initialMsg` and on subsequent iterations if a vertex does not receive a message then the vertex-program is not invoked.
This function iterates until there are no remaining messages, or for `maxIterations` iterations.

A

the Pregel message type

initialMsg

the message each vertex will receive at the on the first iteration

maxIterations

the maximum number of iterations to run for

activeDirection

the direction of edges incident to a vertex that received a message in the previous round on which to run `sendMsg`. For example, if this is `EdgeDirection.Out`, only out-edges of vertices that received a message in the previous round will run.

vprog

the user-defined vertex program which runs on each vertex and receives the inbound message and computes a new vertex value. On the first iteration the vertex program is invoked on all vertices and is passed the default message. On subsequent iterations the vertex program is only invoked on those vertices that receive messages.

sendMsg

a user supplied function that is applied to out edges of vertices that received messages in the current iteration

mergeMsg

a user supplied function that takes two incoming messages of type A and merges them into a single message of type A. _This function must be commutative and associative and ideally the size of A should not increase._

returns

the resulting graph at the end of the computation
  31. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#removeSelfEdges\(\):org.apache.spark.graphx.Graph\[VD,ED\] "Permalink") def removeSelfEdges(): [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[VD, ED]
Remove self edges.
Remove self edges.

returns

a graph with all self edges removed
  32. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#staticPageRank\(numIter:Int,resetProb:Double,prePageRank:org.apache.spark.graphx.Graph\[Double,Double\]\):org.apache.spark.graphx.Graph\[Double,Double\] "Permalink") def staticPageRank(numIter: Int, resetProb: Double, prePageRank: [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[Double, Double]): [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[Double, Double]
Run PageRank for a fixed number of iterations returning a graph with vertex attributes containing the PageRank and edge attributes the normalized edge weight, optionally including including a previous pageRank computation to be used as a start point for the new iterations
Run PageRank for a fixed number of iterations returning a graph with vertex attributes containing the PageRank and edge attributes the normalized edge weight, optionally including including a previous pageRank computation to be used as a start point for the new iterations

See also

[org.apache.spark.graphx.lib.PageRank$#runWithOptionsWithPreviousPageRank](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#runWithOptionsWithPreviousPageRank\[VD,ED\]\(graph:org.apache.spark.graphx.Graph\[VD,ED\],numIter:Int,resetProb:Double,srcId:Option\[org.apache.spark.graphx.VertexId\],normalized:Boolean,preRankGraph:org.apache.spark.graphx.Graph\[Double,Double\]\)\(implicitevidence$9:scala.reflect.ClassTag\[VD\],implicitevidence$10:scala.reflect.ClassTag\[ED\]\):org.apache.spark.graphx.Graph\[Double,Double\])
  33. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#staticPageRank\(numIter:Int,resetProb:Double\):org.apache.spark.graphx.Graph\[Double,Double\] "Permalink") def staticPageRank(numIter: Int, resetProb: Double = 0.15): [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[Double, Double]
Run PageRank for a fixed number of iterations returning a graph with vertex attributes containing the PageRank and edge attributes the normalized edge weight.
Run PageRank for a fixed number of iterations returning a graph with vertex attributes containing the PageRank and edge attributes the normalized edge weight.

See also

[org.apache.spark.graphx.lib.PageRank$#run](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#run\[VD,ED\]\(graph:org.apache.spark.graphx.Graph\[VD,ED\],numIter:Int,resetProb:Double\)\(implicitevidence$1:scala.reflect.ClassTag\[VD\],implicitevidence$2:scala.reflect.ClassTag\[ED\]\):org.apache.spark.graphx.Graph\[Double,Double\])
  34. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#staticParallelPersonalizedPageRank\(sources:Array\[org.apache.spark.graphx.VertexId\],numIter:Int,resetProb:Double\):org.apache.spark.graphx.Graph\[org.apache.spark.ml.linalg.Vector,Double\] "Permalink") def staticParallelPersonalizedPageRank(sources: Array[[VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long)], numIter: Int, resetProb: Double = 0.15): [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[[Vector](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/linalg/Vector.html "org.apache.spark.ml.linalg.Vector"), Double]
Run parallel personalized PageRank for a given array of source vertices, such that all random walks are started relative to the source vertices
  35. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#staticPersonalizedPageRank\(src:org.apache.spark.graphx.VertexId,numIter:Int,resetProb:Double\):org.apache.spark.graphx.Graph\[Double,Double\] "Permalink") def staticPersonalizedPageRank(src: [VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), numIter: Int, resetProb: Double = 0.15): [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[Double, Double]
Run Personalized PageRank for a fixed number of iterations with with all iterations originating at the source node returning a graph with vertex attributes containing the PageRank and edge attributes the normalized edge weight.
Run Personalized PageRank for a fixed number of iterations with with all iterations originating at the source node returning a graph with vertex attributes containing the PageRank and edge attributes the normalized edge weight.

See also

[org.apache.spark.graphx.lib.PageRank$#runWithOptions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#runWithOptions\[VD,ED\]\(graph:org.apache.spark.graphx.Graph\[VD,ED\],numIter:Int,resetProb:Double,srcId:Option\[org.apache.spark.graphx.VertexId\],normalized:Boolean\)\(implicitevidence$5:scala.reflect.ClassTag\[VD\],implicitevidence$6:scala.reflect.ClassTag\[ED\]\):org.apache.spark.graphx.Graph\[Double,Double\])
  36. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#stronglyConnectedComponents\(numIter:Int\):org.apache.spark.graphx.Graph\[org.apache.spark.graphx.VertexId,ED\] "Permalink") def stronglyConnectedComponents(numIter: Int): [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[[VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), ED]
Compute the strongly connected component (SCC) of each vertex and return a graph with the vertex value containing the lowest vertex id in the SCC containing that vertex.
Compute the strongly connected component (SCC) of each vertex and return a graph with the vertex value containing the lowest vertex id in the SCC containing that vertex.

See also

[org.apache.spark.graphx.lib.StronglyConnectedComponents$#run](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/StronglyConnectedComponents$.html#run\[VD,ED\]\(graph:org.apache.spark.graphx.Graph\[VD,ED\],numIter:Int\)\(implicitevidence$1:scala.reflect.ClassTag\[VD\],implicitevidence$2:scala.reflect.ClassTag\[ED\]\):org.apache.spark.graphx.Graph\[org.apache.spark.graphx.VertexId,ED\])
  37. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0

Definition Classes
    AnyRef
  38. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#toString\(\):String "Permalink") def toString(): [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String")

Definition Classes
    AnyRef → Any
  39. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#triangleCount\(\):org.apache.spark.graphx.Graph\[Int,ED\] "Permalink") def triangleCount(): [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[Int, ED]
Compute the number of triangles passing through each vertex.
Compute the number of triangles passing through each vertex.

See also

[org.apache.spark.graphx.lib.TriangleCount$#run](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/TriangleCount$.html#run\[VD,ED\]\(graph:org.apache.spark.graphx.Graph\[VD,ED\]\)\(implicitevidence$1:scala.reflect.ClassTag\[VD\],implicitevidence$2:scala.reflect.ClassTag\[ED\]\):org.apache.spark.graphx.Graph\[Int,ED\])
  40. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])
  41. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  42. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#wait\(\):Unit "Permalink") final  def wait(): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])

### Deprecated Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#finalize\(\):Unit "Permalink") def finalize(): Unit

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
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html###:Int "Permalink") final  def ##: Int

Definition Classes
    AnyRef → Any
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#clone\(\):Object "Permalink") def clone(): AnyRef

Attributes
    protected[lang]

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#equals\(x$1:Object\):Boolean "Permalink") def equals(arg0: AnyRef): Boolean

Definition Classes
    AnyRef → Any
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef]

Definition Classes
    AnyRef → Any

Annotations
     @IntrinsicCandidate() @native()
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#hashCode\(\):Int "Permalink") def hashCode(): Int

Definition Classes
    AnyRef → Any

Annotations
     @IntrinsicCandidate() @native()
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#notify\(\):Unit "Permalink") final  def notify(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0

Definition Classes
    AnyRef
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#toString\(\):String "Permalink") def toString(): [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String")

Definition Classes
    AnyRef → Any
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#wait\(\):Unit "Permalink") final  def wait(): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#finalize\(\):Unit "Permalink") def finalize(): Unit

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
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0

Definition Classes
    Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean

Definition Classes
    Any

### Ungrouped
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html###:Int "Permalink") final  def ##: Int

Definition Classes
    AnyRef → Any
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0

Definition Classes
    Any
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#clone\(\):Object "Permalink") def clone(): AnyRef

Attributes
    protected[lang]

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#collectEdges\(edgeDirection:org.apache.spark.graphx.EdgeDirection\):org.apache.spark.graphx.VertexRDD\[Array\[org.apache.spark.graphx.Edge\[ED\]\]\] "Permalink") def collectEdges(edgeDirection: [EdgeDirection](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/EdgeDirection.html "org.apache.spark.graphx.EdgeDirection")): [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "org.apache.spark.graphx.VertexRDD")[Array[[Edge](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html "org.apache.spark.graphx.Edge")[ED]]]
Returns an RDD that contains for each vertex v its local edges, i.e., the edges that are incident on v, in the user-specified direction.
Returns an RDD that contains for each vertex v its local edges, i.e., the edges that are incident on v, in the user-specified direction. Warning: note that singleton vertices, those with no edges in the given direction will not be part of the return value.

edgeDirection

the direction along which to collect the local edges of vertices

returns

the local edges for each vertex

Note

This function could be highly inefficient on power-law graphs where high degree vertices may force a large amount of information to be collected to a single location.
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#collectNeighborIds\(edgeDirection:org.apache.spark.graphx.EdgeDirection\):org.apache.spark.graphx.VertexRDD\[Array\[org.apache.spark.graphx.VertexId\]\] "Permalink") def collectNeighborIds(edgeDirection: [EdgeDirection](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/EdgeDirection.html "org.apache.spark.graphx.EdgeDirection")): [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "org.apache.spark.graphx.VertexRDD")[Array[[VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long)]]
Collect the neighbor vertex ids for each vertex.
Collect the neighbor vertex ids for each vertex.

edgeDirection

the direction along which to collect neighboring vertices

returns

the set of neighboring ids for each vertex
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#collectNeighbors\(edgeDirection:org.apache.spark.graphx.EdgeDirection\):org.apache.spark.graphx.VertexRDD\[Array\[\(org.apache.spark.graphx.VertexId,VD\)\]\] "Permalink") def collectNeighbors(edgeDirection: [EdgeDirection](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/EdgeDirection.html "org.apache.spark.graphx.EdgeDirection")): [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "org.apache.spark.graphx.VertexRDD")[Array[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD)]]
Collect the neighbor vertex attributes for each vertex.
Collect the neighbor vertex attributes for each vertex.

edgeDirection

the direction along which to collect neighboring vertices

returns

the vertex set of neighboring vertex attributes for each vertex

Note

This function could be highly inefficient on power-law graphs where high degree vertices may force a large amount of information to be collected to a single location.
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#connectedComponents\(maxIterations:Int\):org.apache.spark.graphx.Graph\[org.apache.spark.graphx.VertexId,ED\] "Permalink") def connectedComponents(maxIterations: Int): [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[[VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), ED]
Compute the connected component membership of each vertex and return a graph with the vertex value containing the lowest vertex id in the connected component containing that vertex.
Compute the connected component membership of each vertex and return a graph with the vertex value containing the lowest vertex id in the connected component containing that vertex.

See also

`org.apache.spark.graphx.lib.ConnectedComponents.run`
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#connectedComponents\(\):org.apache.spark.graphx.Graph\[org.apache.spark.graphx.VertexId,ED\] "Permalink") def connectedComponents(): [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[[VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), ED]
Compute the connected component membership of each vertex and return a graph with the vertex value containing the lowest vertex id in the connected component containing that vertex.
Compute the connected component membership of each vertex and return a graph with the vertex value containing the lowest vertex id in the connected component containing that vertex.

See also

`org.apache.spark.graphx.lib.ConnectedComponents.run`
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#convertToCanonicalEdges\(mergeFunc:\(ED,ED\)=>ED\):org.apache.spark.graphx.Graph\[VD,ED\] "Permalink") def convertToCanonicalEdges(mergeFunc: (ED, ED) => ED = (e1, e2) => e1): [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[VD, ED]
Convert bi-directional edges into uni-directional ones.
Convert bi-directional edges into uni-directional ones. Some graph algorithms (e.g., TriangleCount) assume that an input graph has its edges in canonical direction. This function rewrites the vertex ids of edges so that srcIds are smaller than dstIds, and merges the duplicated edges.

mergeFunc

the user defined reduce function which should be commutative and associative and is used to combine the output of the map phase

returns

the resulting graph with canonical edges
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#degrees:org.apache.spark.graphx.VertexRDD\[Int\] "Permalink") lazy val degrees: [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "org.apache.spark.graphx.VertexRDD")[Int]
The degree of each vertex in the graph.
The degree of each vertex in the graph.

Annotations
     @transient()

Note

Vertices with no edges are not returned in the resulting RDD.
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#equals\(x$1:Object\):Boolean "Permalink") def equals(arg0: AnyRef): Boolean

Definition Classes
    AnyRef → Any
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#filter\[VD2,ED2\]\(preprocess:org.apache.spark.graphx.Graph\[VD,ED\]=>org.apache.spark.graphx.Graph\[VD2,ED2\],epred:org.apache.spark.graphx.EdgeTriplet\[VD2,ED2\]=>Boolean,vpred:\(org.apache.spark.graphx.VertexId,VD2\)=>Boolean\)\(implicitevidence$4:scala.reflect.ClassTag\[VD2\],implicitevidence$5:scala.reflect.ClassTag\[ED2\]\):org.apache.spark.graphx.Graph\[VD,ED\] "Permalink") def filter[VD2, ED2](preprocess: ([Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[VD, ED]) => [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[VD2, ED2], epred: ([EdgeTriplet](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/EdgeTriplet.html "org.apache.spark.graphx.EdgeTriplet")[VD2, ED2]) => Boolean = (x: EdgeTriplet[VD2, ED2]) => true, vpred: ([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD2) => Boolean = (v: VertexId, d: VD2) => true)(implicit arg0: ClassTag[VD2], arg1: ClassTag[ED2]): [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[VD, ED]
Filter the graph by computing some values to filter on, and applying the predicates.
Filter the graph by computing some values to filter on, and applying the predicates.

VD2

vertex type the vpred operates on

ED2

edge type the epred operates on

preprocess

a function to compute new vertex and edge data before filtering

epred

edge pred to filter on after preprocess, see more details under [org.apache.spark.graphx.Graph#subgraph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html#subgraph\(epred:org.apache.spark.graphx.EdgeTriplet\[VD,ED\]=>Boolean,vpred:\(org.apache.spark.graphx.VertexId,VD\)=>Boolean\):org.apache.spark.graphx.Graph\[VD,ED\])

vpred

vertex pred to filter on after preprocess, see more details under [org.apache.spark.graphx.Graph#subgraph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html#subgraph\(epred:org.apache.spark.graphx.EdgeTriplet\[VD,ED\]=>Boolean,vpred:\(org.apache.spark.graphx.VertexId,VD\)=>Boolean\):org.apache.spark.graphx.Graph\[VD,ED\])

returns

a subgraph of the original graph, with its data unchanged
Example:
    1. This function can be used to filter the graph based on some property, without changing the vertex and edge values in your program. For example, we could remove the vertices in a graph with 0 outdegree

```
graph.filter(
  graph => {
    val degrees: VertexRDD[Int] = graph.outDegrees
    graph.outerJoinVertices(degrees) {(vid, data, deg) => deg.getOrElse(0)}
  },
  vpred = (vid: VertexId, deg:Int) => deg > 0
)
```

  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef]

Definition Classes
    AnyRef → Any

Annotations
     @IntrinsicCandidate() @native()
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#hashCode\(\):Int "Permalink") def hashCode(): Int

Definition Classes
    AnyRef → Any

Annotations
     @IntrinsicCandidate() @native()
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#inDegrees:org.apache.spark.graphx.VertexRDD\[Int\] "Permalink") lazy val inDegrees: [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "org.apache.spark.graphx.VertexRDD")[Int]
The in-degree of each vertex in the graph.
The in-degree of each vertex in the graph.

Annotations
     @transient()

Note

Vertices with no in-edges are not returned in the resulting RDD.
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean

Definition Classes
    Any
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#joinVertices\[U\]\(table:org.apache.spark.rdd.RDD\[\(org.apache.spark.graphx.VertexId,U\)\]\)\(mapFunc:\(org.apache.spark.graphx.VertexId,VD,U\)=>VD\)\(implicitevidence$3:scala.reflect.ClassTag\[U\]\):org.apache.spark.graphx.Graph\[VD,ED\] "Permalink") def joinVertices[U](table: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), U)])(mapFunc: ([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD, U) => VD)(implicit arg0: ClassTag[U]): [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[VD, ED]
Join the vertices with an RDD and then apply a function from the vertex and RDD entry to a new vertex value.
Join the vertices with an RDD and then apply a function from the vertex and RDD entry to a new vertex value. The input table should contain at most one entry for each vertex. If no entry is provided the map function is skipped and the old value is used.

U

the type of entry in the table of updates

table

the table to join with the vertices in the graph. The table should contain at most one entry for each vertex.

mapFunc

the function used to compute the new vertex values. The map function is invoked only for vertices with a corresponding entry in the table otherwise the old vertex value is used.
Example:
    1. This function is used to update the vertices with new values based on external data. For example we could add the out degree to each vertex record

```
val rawGraph: Graph[Int, Int] = GraphLoader.edgeListFile(sc, "webgraph")
  .mapVertices((_, _) => 0)
val outDeg = rawGraph.outDegrees
val graph = rawGraph.joinVertices[Int](outDeg)
  ((_, _, outDeg) => outDeg)
```

  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#notify\(\):Unit "Permalink") final  def notify(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  23. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  24. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#numEdges:Long "Permalink") lazy val numEdges: Long
The number of edges in the graph.
The number of edges in the graph.

Annotations
     @transient()
  25. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#numVertices:Long "Permalink") lazy val numVertices: Long
The number of vertices in the graph.
The number of vertices in the graph.

Annotations
     @transient()
  26. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#outDegrees:org.apache.spark.graphx.VertexRDD\[Int\] "Permalink") lazy val outDegrees: [VertexRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/VertexRDD.html "org.apache.spark.graphx.VertexRDD")[Int]
The out-degree of each vertex in the graph.
The out-degree of each vertex in the graph.

Annotations
     @transient()

Note

Vertices with no out-edges are not returned in the resulting RDD.
  27. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#pageRank\(tol:Double,resetProb:Double\):org.apache.spark.graphx.Graph\[Double,Double\] "Permalink") def pageRank(tol: Double, resetProb: Double = 0.15): [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[Double, Double]
Run a dynamic version of PageRank returning a graph with vertex attributes containing the PageRank and edge attributes containing the normalized edge weight.
Run a dynamic version of PageRank returning a graph with vertex attributes containing the PageRank and edge attributes containing the normalized edge weight.

See also

[org.apache.spark.graphx.lib.PageRank$#runUntilConvergence](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#runUntilConvergence\[VD,ED\]\(graph:org.apache.spark.graphx.Graph\[VD,ED\],tol:Double,resetProb:Double\)\(implicitevidence$13:scala.reflect.ClassTag\[VD\],implicitevidence$14:scala.reflect.ClassTag\[ED\]\):org.apache.spark.graphx.Graph\[Double,Double\])
  28. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#personalizedPageRank\(src:org.apache.spark.graphx.VertexId,tol:Double,resetProb:Double\):org.apache.spark.graphx.Graph\[Double,Double\] "Permalink") def personalizedPageRank(src: [VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), tol: Double, resetProb: Double = 0.15): [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[Double, Double]
Run personalized PageRank for a given vertex, such that all random walks are started relative to the source node.
Run personalized PageRank for a given vertex, such that all random walks are started relative to the source node.

See also

[org.apache.spark.graphx.lib.PageRank$#runUntilConvergenceWithOptions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#runUntilConvergenceWithOptions\[VD,ED\]\(graph:org.apache.spark.graphx.Graph\[VD,ED\],tol:Double,resetProb:Double,srcId:Option\[org.apache.spark.graphx.VertexId\]\)\(implicitevidence$15:scala.reflect.ClassTag\[VD\],implicitevidence$16:scala.reflect.ClassTag\[ED\]\):org.apache.spark.graphx.Graph\[Double,Double\])
  29. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#pickRandomVertex\(\):org.apache.spark.graphx.VertexId "Permalink") def pickRandomVertex(): [VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long)
Picks a random vertex from the graph and returns its ID.
  30. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#pregel\[A\]\(initialMsg:A,maxIterations:Int,activeDirection:org.apache.spark.graphx.EdgeDirection\)\(vprog:\(org.apache.spark.graphx.VertexId,VD,A\)=>VD,sendMsg:org.apache.spark.graphx.EdgeTriplet\[VD,ED\]=>Iterator\[\(org.apache.spark.graphx.VertexId,A\)\],mergeMsg:\(A,A\)=>A\)\(implicitevidence$6:scala.reflect.ClassTag\[A\]\):org.apache.spark.graphx.Graph\[VD,ED\] "Permalink") def pregel[A](initialMsg: A, maxIterations: Int = Int.MaxValue, activeDirection: [EdgeDirection](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/EdgeDirection.html "org.apache.spark.graphx.EdgeDirection") = [EdgeDirection.Either](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/EdgeDirection$.html))(vprog: ([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), VD, A) => VD, sendMsg: ([EdgeTriplet](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/EdgeTriplet.html "org.apache.spark.graphx.EdgeTriplet")[VD, ED]) => Iterator[([VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), A)], mergeMsg: (A, A) => A)(implicit arg0: ClassTag[A]): [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[VD, ED]
Execute a Pregel-like iterative vertex-parallel abstraction.
Execute a Pregel-like iterative vertex-parallel abstraction. The user-defined vertex-program `vprog` is executed in parallel on each vertex receiving any inbound messages and computing a new value for the vertex. The `sendMsg` function is then invoked on all out-edges and is used to compute an optional message to the destination vertex. The `mergeMsg` function is a commutative associative function used to combine messages destined to the same vertex.
On the first iteration all vertices receive the `initialMsg` and on subsequent iterations if a vertex does not receive a message then the vertex-program is not invoked.
This function iterates until there are no remaining messages, or for `maxIterations` iterations.

A

the Pregel message type

initialMsg

the message each vertex will receive at the on the first iteration

maxIterations

the maximum number of iterations to run for

activeDirection

the direction of edges incident to a vertex that received a message in the previous round on which to run `sendMsg`. For example, if this is `EdgeDirection.Out`, only out-edges of vertices that received a message in the previous round will run.

vprog

the user-defined vertex program which runs on each vertex and receives the inbound message and computes a new vertex value. On the first iteration the vertex program is invoked on all vertices and is passed the default message. On subsequent iterations the vertex program is only invoked on those vertices that receive messages.

sendMsg

a user supplied function that is applied to out edges of vertices that received messages in the current iteration

mergeMsg

a user supplied function that takes two incoming messages of type A and merges them into a single message of type A. _This function must be commutative and associative and ideally the size of A should not increase._

returns

the resulting graph at the end of the computation
  31. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#removeSelfEdges\(\):org.apache.spark.graphx.Graph\[VD,ED\] "Permalink") def removeSelfEdges(): [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[VD, ED]
Remove self edges.
Remove self edges.

returns

a graph with all self edges removed
  32. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#staticPageRank\(numIter:Int,resetProb:Double,prePageRank:org.apache.spark.graphx.Graph\[Double,Double\]\):org.apache.spark.graphx.Graph\[Double,Double\] "Permalink") def staticPageRank(numIter: Int, resetProb: Double, prePageRank: [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[Double, Double]): [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[Double, Double]
Run PageRank for a fixed number of iterations returning a graph with vertex attributes containing the PageRank and edge attributes the normalized edge weight, optionally including including a previous pageRank computation to be used as a start point for the new iterations
Run PageRank for a fixed number of iterations returning a graph with vertex attributes containing the PageRank and edge attributes the normalized edge weight, optionally including including a previous pageRank computation to be used as a start point for the new iterations

See also

[org.apache.spark.graphx.lib.PageRank$#runWithOptionsWithPreviousPageRank](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#runWithOptionsWithPreviousPageRank\[VD,ED\]\(graph:org.apache.spark.graphx.Graph\[VD,ED\],numIter:Int,resetProb:Double,srcId:Option\[org.apache.spark.graphx.VertexId\],normalized:Boolean,preRankGraph:org.apache.spark.graphx.Graph\[Double,Double\]\)\(implicitevidence$9:scala.reflect.ClassTag\[VD\],implicitevidence$10:scala.reflect.ClassTag\[ED\]\):org.apache.spark.graphx.Graph\[Double,Double\])
  33. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#staticPageRank\(numIter:Int,resetProb:Double\):org.apache.spark.graphx.Graph\[Double,Double\] "Permalink") def staticPageRank(numIter: Int, resetProb: Double = 0.15): [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[Double, Double]
Run PageRank for a fixed number of iterations returning a graph with vertex attributes containing the PageRank and edge attributes the normalized edge weight.
Run PageRank for a fixed number of iterations returning a graph with vertex attributes containing the PageRank and edge attributes the normalized edge weight.

See also

[org.apache.spark.graphx.lib.PageRank$#run](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#run\[VD,ED\]\(graph:org.apache.spark.graphx.Graph\[VD,ED\],numIter:Int,resetProb:Double\)\(implicitevidence$1:scala.reflect.ClassTag\[VD\],implicitevidence$2:scala.reflect.ClassTag\[ED\]\):org.apache.spark.graphx.Graph\[Double,Double\])
  34. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#staticParallelPersonalizedPageRank\(sources:Array\[org.apache.spark.graphx.VertexId\],numIter:Int,resetProb:Double\):org.apache.spark.graphx.Graph\[org.apache.spark.ml.linalg.Vector,Double\] "Permalink") def staticParallelPersonalizedPageRank(sources: Array[[VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long)], numIter: Int, resetProb: Double = 0.15): [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[[Vector](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/linalg/Vector.html "org.apache.spark.ml.linalg.Vector"), Double]
Run parallel personalized PageRank for a given array of source vertices, such that all random walks are started relative to the source vertices
  35. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#staticPersonalizedPageRank\(src:org.apache.spark.graphx.VertexId,numIter:Int,resetProb:Double\):org.apache.spark.graphx.Graph\[Double,Double\] "Permalink") def staticPersonalizedPageRank(src: [VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), numIter: Int, resetProb: Double = 0.15): [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[Double, Double]
Run Personalized PageRank for a fixed number of iterations with with all iterations originating at the source node returning a graph with vertex attributes containing the PageRank and edge attributes the normalized edge weight.
Run Personalized PageRank for a fixed number of iterations with with all iterations originating at the source node returning a graph with vertex attributes containing the PageRank and edge attributes the normalized edge weight.

See also

[org.apache.spark.graphx.lib.PageRank$#runWithOptions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#runWithOptions\[VD,ED\]\(graph:org.apache.spark.graphx.Graph\[VD,ED\],numIter:Int,resetProb:Double,srcId:Option\[org.apache.spark.graphx.VertexId\],normalized:Boolean\)\(implicitevidence$5:scala.reflect.ClassTag\[VD\],implicitevidence$6:scala.reflect.ClassTag\[ED\]\):org.apache.spark.graphx.Graph\[Double,Double\])
  36. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#stronglyConnectedComponents\(numIter:Int\):org.apache.spark.graphx.Graph\[org.apache.spark.graphx.VertexId,ED\] "Permalink") def stronglyConnectedComponents(numIter: Int): [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[[VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long), ED]
Compute the strongly connected component (SCC) of each vertex and return a graph with the vertex value containing the lowest vertex id in the SCC containing that vertex.
Compute the strongly connected component (SCC) of each vertex and return a graph with the vertex value containing the lowest vertex id in the SCC containing that vertex.

See also

[org.apache.spark.graphx.lib.StronglyConnectedComponents$#run](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/StronglyConnectedComponents$.html#run\[VD,ED\]\(graph:org.apache.spark.graphx.Graph\[VD,ED\],numIter:Int\)\(implicitevidence$1:scala.reflect.ClassTag\[VD\],implicitevidence$2:scala.reflect.ClassTag\[ED\]\):org.apache.spark.graphx.Graph\[org.apache.spark.graphx.VertexId,ED\])
  37. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0

Definition Classes
    AnyRef
  38. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#toString\(\):String "Permalink") def toString(): [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String")

Definition Classes
    AnyRef → Any
  39. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#triangleCount\(\):org.apache.spark.graphx.Graph\[Int,ED\] "Permalink") def triangleCount(): [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[Int, ED]
Compute the number of triangles passing through each vertex.
Compute the number of triangles passing through each vertex.

See also

[org.apache.spark.graphx.lib.TriangleCount$#run](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/TriangleCount$.html#run\[VD,ED\]\(graph:org.apache.spark.graphx.Graph\[VD,ED\]\)\(implicitevidence$1:scala.reflect.ClassTag\[VD\],implicitevidence$2:scala.reflect.ClassTag\[ED\]\):org.apache.spark.graphx.Graph\[Int,ED\])
  40. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])
  41. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  42. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#wait\(\):Unit "Permalink") final  def wait(): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])
  43. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/GraphOps.html#finalize\(\):Unit "Permalink") def finalize(): Unit

Attributes
    protected[lang]

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.Throwable]) @Deprecated

Deprecated

_(Since version 9)_
