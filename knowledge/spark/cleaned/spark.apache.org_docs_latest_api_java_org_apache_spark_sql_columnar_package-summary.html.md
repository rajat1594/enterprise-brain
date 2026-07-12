[Skip navigation links](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/columnar/package-summary.html#skip-navbar-top "Skip navigation links")
  * [Overview](https://spark.apache.org/docs/latest/api/java/index.html)
  * Package
  * Class
  * [Deprecated](https://spark.apache.org/docs/latest/api/java/deprecated-list.html)
  * [Index](https://spark.apache.org/docs/latest/api/java/index-all.html)
  * [Help](https://spark.apache.org/docs/latest/api/java/help-doc.html#package)

  * Package:
  * Description |
  * [Related Packages](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/columnar/package-summary.html#related-package-summary) |
  * [Classes and Interfaces](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/columnar/package-summary.html#class-summary)

SEARCH:
# Package org.apache.spark.sql.columnar
* * *
package org.apache.spark.sql.columnar
  * Related Packages
Package
Description
[org.apache.spark.sql](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/package-summary.html)
  * All Classes and InterfacesInterfacesClasses
Class
Description
[CachedBatch](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/columnar/CachedBatch.html "interface in org.apache.spark.sql.columnar")
Basic interface that all cached batches of data must support.
[CachedBatchSerializer](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/columnar/CachedBatchSerializer.html "interface in org.apache.spark.sql.columnar")
Provides APIs that handle transformations of SQL data associated with the cache/persist APIs.
[ExtractableLiteral](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/columnar/ExtractableLiteral.html "class in org.apache.spark.sql.columnar")
[SimpleMetricsCachedBatch](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/columnar/SimpleMetricsCachedBatch.html "interface in org.apache.spark.sql.columnar")
A [`CachedBatch`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/columnar/CachedBatch.html "interface in org.apache.spark.sql.columnar") that stores some simple metrics that can be used for filtering of batches with the [`SimpleMetricsCachedBatchSerializer`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/columnar/SimpleMetricsCachedBatchSerializer.html "class in org.apache.spark.sql.columnar").
[SimpleMetricsCachedBatchSerializer](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/columnar/SimpleMetricsCachedBatchSerializer.html "class in org.apache.spark.sql.columnar")
Provides basic filtering for [`CachedBatchSerializer`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/columnar/CachedBatchSerializer.html "interface in org.apache.spark.sql.columnar") implementations.
