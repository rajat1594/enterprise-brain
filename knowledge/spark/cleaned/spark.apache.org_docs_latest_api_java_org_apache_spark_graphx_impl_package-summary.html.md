[Skip navigation links](https://spark.apache.org/docs/latest/api/java/org/apache/spark/graphx/impl/package-summary.html#skip-navbar-top "Skip navigation links")
  * [Overview](https://spark.apache.org/docs/latest/api/java/index.html)
  * Package
  * Class
  * [Deprecated](https://spark.apache.org/docs/latest/api/java/deprecated-list.html)
  * [Index](https://spark.apache.org/docs/latest/api/java/index-all.html)
  * [Help](https://spark.apache.org/docs/latest/api/java/help-doc.html#package)

  * Package:
  * Description |
  * [Related Packages](https://spark.apache.org/docs/latest/api/java/org/apache/spark/graphx/impl/package-summary.html#related-package-summary) |
  * [Classes and Interfaces](https://spark.apache.org/docs/latest/api/java/org/apache/spark/graphx/impl/package-summary.html#class-summary)

SEARCH:
# Package org.apache.spark.graphx.impl
* * *
package org.apache.spark.graphx.impl
  * Related Packages
Package
Description
[org.apache.spark.graphx](https://spark.apache.org/docs/latest/api/java/org/apache/spark/graphx/package-summary.html)
ALPHA COMPONENT GraphX is a graph processing framework built on top of Spark.
[org.apache.spark.graphx.lib](https://spark.apache.org/docs/latest/api/java/org/apache/spark/graphx/lib/package-summary.html)
Various analytics functions for graphs.
[org.apache.spark.graphx.util](https://spark.apache.org/docs/latest/api/java/org/apache/spark/graphx/util/package-summary.html)
Collections of utilities used by graphx.
  * All Classes and InterfacesInterfacesClassesEnum Classes
Class
Description
[AggregatingEdgeContext](https://spark.apache.org/docs/latest/api/java/org/apache/spark/graphx/impl/AggregatingEdgeContext.html "class in org.apache.spark.graphx.impl")<VD,ED,A>
[EdgeActiveness](https://spark.apache.org/docs/latest/api/java/org/apache/spark/graphx/impl/EdgeActiveness.html "enum class in org.apache.spark.graphx.impl")
Criteria for filtering edges based on activeness.
[EdgeRDDImpl](https://spark.apache.org/docs/latest/api/java/org/apache/spark/graphx/impl/EdgeRDDImpl.html "class in org.apache.spark.graphx.impl")<ED,VD>
[GraphImpl](https://spark.apache.org/docs/latest/api/java/org/apache/spark/graphx/impl/GraphImpl.html "class in org.apache.spark.graphx.impl")<VD,ED>
An implementation of [`Graph`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/graphx/Graph.html "class in org.apache.spark.graphx") to support computation on graphs.
[VertexPartitionBaseOpsConstructor](https://spark.apache.org/docs/latest/api/java/org/apache/spark/graphx/impl/VertexPartitionBaseOpsConstructor.html "interface in org.apache.spark.graphx.impl")<T extends org.apache.spark.graphx.impl.VertexPartitionBase<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>>
A typeclass for subclasses of `VertexPartitionBase` representing the ability to wrap them in a `VertexPartitionBaseOps`.
[VertexRDDImpl](https://spark.apache.org/docs/latest/api/java/org/apache/spark/graphx/impl/VertexRDDImpl.html "class in org.apache.spark.graphx.impl")<VD>
