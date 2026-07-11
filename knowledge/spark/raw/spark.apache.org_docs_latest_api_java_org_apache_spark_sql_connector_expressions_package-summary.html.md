[Skip navigation links](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/expressions/package-summary.html#skip-navbar-top "Skip navigation links")
  * [Overview](https://spark.apache.org/docs/latest/api/java/index.html)
  * Package
  * Class
  * [Deprecated](https://spark.apache.org/docs/latest/api/java/deprecated-list.html)
  * [Index](https://spark.apache.org/docs/latest/api/java/index-all.html)
  * [Help](https://spark.apache.org/docs/latest/api/java/help-doc.html#package)


  * Package: 
  * Description | 
  * [Related Packages](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/expressions/package-summary.html#related-package-summary) | 
  * [Classes and Interfaces](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/expressions/package-summary.html#class-summary)


SEARCH:
# Package org.apache.spark.sql.connector.expressions
* * *
package org.apache.spark.sql.connector.expressions
  * Related Packages
Package
Description
[org.apache.spark.sql.connector](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/package-summary.html)
[org.apache.spark.sql.connector.expressions.aggregate](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/expressions/aggregate/package-summary.html)
[org.apache.spark.sql.connector.expressions.filter](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/expressions/filter/package-summary.html)
  * All Classes and InterfacesInterfacesClassesEnum Classes
Class
Description
[Cast](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/expressions/Cast.html "class in org.apache.spark.sql.connector.expressions")
Represents a cast expression in the public logical expression API.
[ClusterByTransform](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/expressions/ClusterByTransform.html "class in org.apache.spark.sql.connector.expressions")
This class represents a transform for `ClusterBySpec`.
[Expression](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/expressions/Expression.html "interface in org.apache.spark.sql.connector.expressions")
Base class of the public logical expression API.
[Expressions](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/expressions/Expressions.html "class in org.apache.spark.sql.connector.expressions")
Helper methods to create logical transforms to pass into Spark.
[Extract](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/expressions/Extract.html "class in org.apache.spark.sql.connector.expressions")
Represent an extract function, which extracts and returns the value of a specified datetime field from a datetime or interval value expression.
[GeneralScalarExpression](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/expressions/GeneralScalarExpression.html "class in org.apache.spark.sql.connector.expressions")
The general representation of SQL scalar expressions, which contains the upper-cased expression name and all the children expressions.
[GetArrayItem](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/expressions/GetArrayItem.html "class in org.apache.spark.sql.connector.expressions")
Get array item expression.
[Lit](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/expressions/Lit.html "class in org.apache.spark.sql.connector.expressions")
Convenience extractor for any Literal.
[Literal](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/expressions/Literal.html "interface in org.apache.spark.sql.connector.expressions")<T>
Represents a constant literal value in the public expression API.
[LogicalExpressions](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/expressions/LogicalExpressions.html "class in org.apache.spark.sql.connector.expressions")
Helper methods for working with the logical expressions API.
[NamedReference](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/expressions/NamedReference.html "interface in org.apache.spark.sql.connector.expressions")
Represents a field or column reference in the public logical expression API.
[NamedTransform](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/expressions/NamedTransform.html "class in org.apache.spark.sql.connector.expressions")
Convenience extractor for any Transform.
[NullOrdering](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/expressions/NullOrdering.html "enum class in org.apache.spark.sql.connector.expressions")
A null order used in sorting expressions.
[Ref](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/expressions/Ref.html "class in org.apache.spark.sql.connector.expressions")
Convenience extractor for any NamedReference.
[RewritableTransform](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/expressions/RewritableTransform.html "interface in org.apache.spark.sql.connector.expressions")
Allows Spark to rewrite the given references of the transform during analysis.
[SortDirection](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/expressions/SortDirection.html "enum class in org.apache.spark.sql.connector.expressions")
A sort direction used in sorting expressions.
[SortOrder](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/expressions/SortOrder.html "interface in org.apache.spark.sql.connector.expressions")
Represents a sort order in the public expression API.
[Transform](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/expressions/Transform.html "interface in org.apache.spark.sql.connector.expressions")
Represents a transform function in the public logical expression API.
[UserDefinedScalarFunc](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/expressions/UserDefinedScalarFunc.html "class in org.apache.spark.sql.connector.expressions")
The general representation of user defined scalar function, which contains the upper-cased function name, canonical function name and all the children expressions.


