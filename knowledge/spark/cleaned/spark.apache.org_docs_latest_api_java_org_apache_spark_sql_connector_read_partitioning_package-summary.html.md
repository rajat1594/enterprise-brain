[Skip navigation links](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/partitioning/package-summary.html#skip-navbar-top "Skip navigation links")
  * [Overview](https://spark.apache.org/docs/latest/api/java/index.html)
  * Package
  * Class
  * [Deprecated](https://spark.apache.org/docs/latest/api/java/deprecated-list.html)
  * [Index](https://spark.apache.org/docs/latest/api/java/index-all.html)
  * [Help](https://spark.apache.org/docs/latest/api/java/help-doc.html#package)

  * Package:
  * Description |
  * [Related Packages](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/partitioning/package-summary.html#related-package-summary) |
  * [Classes and Interfaces](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/partitioning/package-summary.html#class-summary)

SEARCH:
# Package org.apache.spark.sql.connector.read.partitioning
* * *
package org.apache.spark.sql.connector.read.partitioning
  * Related Packages
Package
Description
[org.apache.spark.sql.connector.read](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/package-summary.html)
[org.apache.spark.sql.connector.read.colstats](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/colstats/package-summary.html)
[org.apache.spark.sql.connector.read.streaming](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/streaming/package-summary.html)
  * All Classes and InterfacesInterfacesClasses
Class
Description
[KeyGroupedPartitioning](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/partitioning/KeyGroupedPartitioning.html "class in org.apache.spark.sql.connector.read.partitioning")
Represents a partitioning where rows are split across partitions based on the partition transform expressions returned by `KeyGroupedPartitioning.keys`.
[Partitioning](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/partitioning/Partitioning.html "interface in org.apache.spark.sql.connector.read.partitioning")
An interface to represent the output data partitioning for a data source, which is returned by [`SupportsReportPartitioning.outputPartitioning()`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/SupportsReportPartitioning.html#outputPartitioning\(\)).
[UnknownPartitioning](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/partitioning/UnknownPartitioning.html "class in org.apache.spark.sql.connector.read.partitioning")
Represents a partitioning where rows are split across partitions in an unknown pattern.
