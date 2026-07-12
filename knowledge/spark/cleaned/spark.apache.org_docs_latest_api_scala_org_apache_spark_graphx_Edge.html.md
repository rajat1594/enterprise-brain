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

[c](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge$.html "See companion object")
[org](https://spark.apache.org/docs/latest/api/scala/org/index.html "org").[apache](https://spark.apache.org/docs/latest/api/scala/org/apache/index.html "org.apache").[spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark").[graphx](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html "org.apache.spark.graphx")
#  [Edge](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge$.html "See companion object")[ __](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html "Permalink")
###
Companion [object Edge](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge$.html "See companion object")
####  case class Edge[ED](srcId: [VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long) = 0, dstId: [VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long) = 0, attr: ED = null.asInstanceOf[ED]) extends Serializable with Product
A single directed edge consisting of a source id, target id, and the data associated with the edge.

ED

type of the edge attribute

srcId

The vertex id of the source vertex

dstId

The vertex id of the target vertex

attr

The attribute associated with the edge

Source
    [Edge.scala](https://github.com/apache/spark/tree/v4.1.2/graphx/src/main/scala/org/apache/spark/graphx/Edge.scala)
Linear Supertypes
Product, Equals, [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable"), AnyRef, Any
Known Subclasses
[EdgeTriplet](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/EdgeTriplet.html "org.apache.spark.graphx.EdgeTriplet")
__ __
Ordering
  1. Alphabetic
  2. By Inheritance

Inherited

  1. Edge
  2. Product
  3. Equals
  4. Serializable
  5. AnyRef
  6. Any

  1. Hide All
  2. Show All

Visibility
  1. Public
  2. Protected

### Instance Constructors
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html#<init>\(srcId:org.apache.spark.graphx.VertexId,dstId:org.apache.spark.graphx.VertexId,attr:ED\):org.apache.spark.graphx.Edge\[ED\] "Permalink") new Edge(srcId: [VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long) = 0, dstId: [VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long) = 0, attr: ED = null.asInstanceOf[ED])

srcId

The vertex id of the source vertex

dstId

The vertex id of the target vertex

attr

The attribute associated with the edge

### Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html###:Int "Permalink") final  def ##: Int

Definition Classes
    AnyRef → Any
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0

Definition Classes
    Any
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html#attr:ED "Permalink") var attr: ED
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html#clone\(\):Object "Permalink") def clone(): AnyRef

Attributes
    protected[lang]

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html#dstId:org.apache.spark.graphx.VertexId "Permalink") var dstId: [VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long)
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef]

Definition Classes
    AnyRef → Any

Annotations
     @IntrinsicCandidate() @native()
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean

Definition Classes
    Any
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html#notify\(\):Unit "Permalink") final  def notify(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html#otherVertexId\(vid:org.apache.spark.graphx.VertexId\):org.apache.spark.graphx.VertexId "Permalink") def otherVertexId(vid: [VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long)): [VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long)
Given one vertex in the edge return the other vertex.
Given one vertex in the edge return the other vertex.

vid

the id one of the two vertices on the edge.

returns

the id of the other vertex on the edge.
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html#productElementNames:Iterator\[String\] "Permalink") def productElementNames: Iterator[String]

Definition Classes
    Product
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html#relativeDirection\(vid:org.apache.spark.graphx.VertexId\):org.apache.spark.graphx.EdgeDirection "Permalink") def relativeDirection(vid: [VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long)): [EdgeDirection](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/EdgeDirection.html "org.apache.spark.graphx.EdgeDirection")
Return the relative direction of the edge to the corresponding vertex.
Return the relative direction of the edge to the corresponding vertex.

vid

the id of one of the two vertices in the edge.

returns

the relative direction of the edge to the corresponding vertex.
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html#srcId:org.apache.spark.graphx.VertexId "Permalink") var srcId: [VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long)
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0

Definition Classes
    AnyRef
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html#wait\(\):Unit "Permalink") final  def wait(): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])

### Deprecated Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html#finalize\(\):Unit "Permalink") def finalize(): Unit

Attributes
    protected[lang]

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.Throwable]) @Deprecated

Deprecated

_(Since version 9)_

### Inherited from Product
### Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html#productElementNames:Iterator\[String\] "Permalink") def productElementNames: Iterator[String]

Definition Classes
    Product

### Inherited from AnyRef
### Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html###:Int "Permalink") final  def ##: Int

Definition Classes
    AnyRef → Any
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html#clone\(\):Object "Permalink") def clone(): AnyRef

Attributes
    protected[lang]

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef]

Definition Classes
    AnyRef → Any

Annotations
     @IntrinsicCandidate() @native()
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html#notify\(\):Unit "Permalink") final  def notify(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0

Definition Classes
    AnyRef
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html#wait\(\):Unit "Permalink") final  def wait(): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html#finalize\(\):Unit "Permalink") def finalize(): Unit

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
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0

Definition Classes
    Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean

Definition Classes
    Any

### Ungrouped
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html###:Int "Permalink") final  def ##: Int

Definition Classes
    AnyRef → Any
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0

Definition Classes
    Any
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html#attr:ED "Permalink") var attr: ED
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html#clone\(\):Object "Permalink") def clone(): AnyRef

Attributes
    protected[lang]

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html#dstId:org.apache.spark.graphx.VertexId "Permalink") var dstId: [VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long)
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef]

Definition Classes
    AnyRef → Any

Annotations
     @IntrinsicCandidate() @native()
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean

Definition Classes
    Any
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html#notify\(\):Unit "Permalink") final  def notify(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html#otherVertexId\(vid:org.apache.spark.graphx.VertexId\):org.apache.spark.graphx.VertexId "Permalink") def otherVertexId(vid: [VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long)): [VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long)
Given one vertex in the edge return the other vertex.
Given one vertex in the edge return the other vertex.

vid

the id one of the two vertices on the edge.

returns

the id of the other vertex on the edge.
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html#productElementNames:Iterator\[String\] "Permalink") def productElementNames: Iterator[String]

Definition Classes
    Product
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html#relativeDirection\(vid:org.apache.spark.graphx.VertexId\):org.apache.spark.graphx.EdgeDirection "Permalink") def relativeDirection(vid: [VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long)): [EdgeDirection](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/EdgeDirection.html "org.apache.spark.graphx.EdgeDirection")
Return the relative direction of the edge to the corresponding vertex.
Return the relative direction of the edge to the corresponding vertex.

vid

the id of one of the two vertices in the edge.

returns

the relative direction of the edge to the corresponding vertex.
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html#srcId:org.apache.spark.graphx.VertexId "Permalink") var srcId: [VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long)
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0

Definition Classes
    AnyRef
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html#wait\(\):Unit "Permalink") final  def wait(): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Edge.html#finalize\(\):Unit "Permalink") def finalize(): Unit

Attributes
    protected[lang]

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.Throwable]) @Deprecated

Deprecated

_(Since version 9)_
