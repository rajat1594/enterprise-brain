[Skip navigation links](https://spark.apache.org/docs/latest/api/java/org/apache/spark/graphx/package-summary.html#skip-navbar-top "Skip navigation links")
  * [Overview](https://spark.apache.org/docs/latest/api/java/index.html)
  * Package
  * Class
  * [Deprecated](https://spark.apache.org/docs/latest/api/java/deprecated-list.html)
  * [Index](https://spark.apache.org/docs/latest/api/java/index-all.html)
  * [Help](https://spark.apache.org/docs/latest/api/java/help-doc.html#package)


  * Package: 
  * [Description](https://spark.apache.org/docs/latest/api/java/org/apache/spark/graphx/package-summary.html#package-description) | 
  * [Related Packages](https://spark.apache.org/docs/latest/api/java/org/apache/spark/graphx/package-summary.html#related-package-summary) | 
  * [Classes and Interfaces](https://spark.apache.org/docs/latest/api/java/org/apache/spark/graphx/package-summary.html#class-summary)


SEARCH:
# Package org.apache.spark.graphx
* * *
package org.apache.spark.graphx
ALPHA COMPONENT GraphX is a graph processing framework built on top of Spark.
  * Related Packages
Package
Description
[org.apache.spark](https://spark.apache.org/docs/latest/api/java/org/apache/spark/package-summary.html)
Core Spark classes in Scala.
[org.apache.spark.graphx.impl](https://spark.apache.org/docs/latest/api/java/org/apache/spark/graphx/impl/package-summary.html)
[org.apache.spark.graphx.lib](https://spark.apache.org/docs/latest/api/java/org/apache/spark/graphx/lib/package-summary.html)
Various analytics functions for graphs.
[org.apache.spark.graphx.util](https://spark.apache.org/docs/latest/api/java/org/apache/spark/graphx/util/package-summary.html)
Collections of utilities used by graphx.
  * All Classes and InterfacesInterfacesClasses
Class
Description
[Edge](https://spark.apache.org/docs/latest/api/java/org/apache/spark/graphx/Edge.html "class in org.apache.spark.graphx")<ED>
A single directed edge consisting of a source id, target id, and the data associated with the edge.
[EdgeContext](https://spark.apache.org/docs/latest/api/java/org/apache/spark/graphx/EdgeContext.html "class in org.apache.spark.graphx")<VD,ED,A>
Represents an edge along with its neighboring vertices and allows sending messages along the edge.
[EdgeDirection](https://spark.apache.org/docs/latest/api/java/org/apache/spark/graphx/EdgeDirection.html "class in org.apache.spark.graphx")
The direction of a directed edge relative to a vertex.
[EdgeRDD](https://spark.apache.org/docs/latest/api/java/org/apache/spark/graphx/EdgeRDD.html "class in org.apache.spark.graphx")<ED>
`EdgeRDD[ED, VD]` extends `RDD[Edge[ED}` by storing the edges in columnar format on each partition for performance.
[EdgeTriplet](https://spark.apache.org/docs/latest/api/java/org/apache/spark/graphx/EdgeTriplet.html "class in org.apache.spark.graphx")<VD,ED>
An edge triplet represents an edge along with the vertex attributes of its neighboring vertices.
[Graph](https://spark.apache.org/docs/latest/api/java/org/apache/spark/graphx/Graph.html "class in org.apache.spark.graphx")<VD,ED>
The Graph abstractly represents a graph with arbitrary objects associated with vertices and edges.
[GraphLoader](https://spark.apache.org/docs/latest/api/java/org/apache/spark/graphx/GraphLoader.html "class in org.apache.spark.graphx")
Provides utilities for loading [`Graph`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/graphx/Graph.html "class in org.apache.spark.graphx")s from files.
[GraphOps](https://spark.apache.org/docs/latest/api/java/org/apache/spark/graphx/GraphOps.html "class in org.apache.spark.graphx")<VD,ED>
Contains additional functionality for [`Graph`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/graphx/Graph.html "class in org.apache.spark.graphx").
[GraphXUtils](https://spark.apache.org/docs/latest/api/java/org/apache/spark/graphx/GraphXUtils.html "class in org.apache.spark.graphx")
[PartitionStrategy](https://spark.apache.org/docs/latest/api/java/org/apache/spark/graphx/PartitionStrategy.html "interface in org.apache.spark.graphx")
Represents the way edges are assigned to edge partitions based on their source and destination vertex IDs.
[PartitionStrategy.CanonicalRandomVertexCut$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/graphx/PartitionStrategy.CanonicalRandomVertexCut$.html "class in org.apache.spark.graphx")
Assigns edges to partitions by hashing the source and destination vertex IDs in a canonical direction, resulting in a random vertex cut that colocates all edges between two vertices, regardless of direction.
[PartitionStrategy.EdgePartition1D$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/graphx/PartitionStrategy.EdgePartition1D$.html "class in org.apache.spark.graphx")
Assigns edges to partitions using only the source vertex ID, colocating edges with the same source.
[PartitionStrategy.EdgePartition2D$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/graphx/PartitionStrategy.EdgePartition2D$.html "class in org.apache.spark.graphx")
Assigns edges to partitions using a 2D partitioning of the sparse edge adjacency matrix, guaranteeing a `2 * sqrt(numParts)` bound on vertex replication.
[PartitionStrategy.RandomVertexCut$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/graphx/PartitionStrategy.RandomVertexCut$.html "class in org.apache.spark.graphx")
Assigns edges to partitions by hashing the source and destination vertex IDs, resulting in a random vertex cut that colocates all same-direction edges between two vertices.
[Pregel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/graphx/Pregel.html "class in org.apache.spark.graphx")
Implements a Pregel-like bulk-synchronous message-passing API.
[TripletFields](https://spark.apache.org/docs/latest/api/java/org/apache/spark/graphx/TripletFields.html "class in org.apache.spark.graphx")
Represents a subset of the fields of an [[EdgeTriplet]] or [[EdgeContext]].
[VertexRDD](https://spark.apache.org/docs/latest/api/java/org/apache/spark/graphx/VertexRDD.html "class in org.apache.spark.graphx")<VD>
Extends `RDD[(VertexId, VD)]` by ensuring that there is only one entry for each vertex and by pre-indexing the entries for fast, efficient joins.


