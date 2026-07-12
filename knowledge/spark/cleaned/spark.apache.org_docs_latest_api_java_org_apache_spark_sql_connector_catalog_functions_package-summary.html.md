[Skip navigation links](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/functions/package-summary.html#skip-navbar-top "Skip navigation links")
  * [Overview](https://spark.apache.org/docs/latest/api/java/index.html)
  * Package
  * Class
  * [Deprecated](https://spark.apache.org/docs/latest/api/java/deprecated-list.html)
  * [Index](https://spark.apache.org/docs/latest/api/java/index-all.html)
  * [Help](https://spark.apache.org/docs/latest/api/java/help-doc.html#package)

  * Package:
  * Description |
  * [Related Packages](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/functions/package-summary.html#related-package-summary) |
  * [Classes and Interfaces](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/functions/package-summary.html#class-summary)

SEARCH:
# Package org.apache.spark.sql.connector.catalog.functions
* * *
package org.apache.spark.sql.connector.catalog.functions
  * Related Packages
Package
Description
[org.apache.spark.sql.connector.catalog](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/package-summary.html)
[org.apache.spark.sql.connector.catalog.constraints](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/constraints/package-summary.html)
[org.apache.spark.sql.connector.catalog.index](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/index/package-summary.html)
[org.apache.spark.sql.connector.catalog.procedures](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/procedures/package-summary.html)
  * Interfaces
Class
Description
[AggregateFunction](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/functions/AggregateFunction.html "interface in org.apache.spark.sql.connector.catalog.functions")<S extends [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html "class or interface in java.io"),R>
Interface for a function that produces a result value by aggregating over multiple input rows.
[BoundFunction](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/functions/BoundFunction.html "interface in org.apache.spark.sql.connector.catalog.functions")
Represents a function that is bound to an input type.
[Function](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/functions/Function.html "interface in org.apache.spark.sql.connector.catalog.functions")
Base class for user-defined functions.
[Reducer](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/functions/Reducer.html "interface in org.apache.spark.sql.connector.catalog.functions")<I,O>
A 'reducer' for output of user-defined functions.
[ReducibleFunction](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/functions/ReducibleFunction.html "interface in org.apache.spark.sql.connector.catalog.functions")<I,O>
Base class for user-defined functions that can be 'reduced' on another function.
[ScalarFunction](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/functions/ScalarFunction.html "interface in org.apache.spark.sql.connector.catalog.functions")<R>
Interface for a function that produces a result value for each input row.
[UnboundFunction](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/functions/UnboundFunction.html "interface in org.apache.spark.sql.connector.catalog.functions")
Represents a user-defined function that is not bound to input types.
