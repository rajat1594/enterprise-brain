[Skip navigation links](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/expressions/filter/package-summary.html#skip-navbar-top "Skip navigation links")
  * [Overview](https://spark.apache.org/docs/latest/api/java/index.html)
  * Package
  * Class
  * [Deprecated](https://spark.apache.org/docs/latest/api/java/deprecated-list.html)
  * [Index](https://spark.apache.org/docs/latest/api/java/index-all.html)
  * [Help](https://spark.apache.org/docs/latest/api/java/help-doc.html#package)

  * Package:
  * Description |
  * [Related Packages](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/expressions/filter/package-summary.html#related-package-summary) |
  * [Classes and Interfaces](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/expressions/filter/package-summary.html#class-summary)

SEARCH:
# Package org.apache.spark.sql.connector.expressions.filter
* * *
package org.apache.spark.sql.connector.expressions.filter
  * Related Packages
Package
Description
[org.apache.spark.sql.connector.expressions](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/expressions/package-summary.html)
[org.apache.spark.sql.connector.expressions.aggregate](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/expressions/aggregate/package-summary.html)
  * Classes
Class
Description
[AlwaysFalse](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/expressions/filter/AlwaysFalse.html "class in org.apache.spark.sql.connector.expressions.filter")
A predicate that always evaluates to `false`.
[AlwaysTrue](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/expressions/filter/AlwaysTrue.html "class in org.apache.spark.sql.connector.expressions.filter")
A predicate that always evaluates to `true`.
[And](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/expressions/filter/And.html "class in org.apache.spark.sql.connector.expressions.filter")
A predicate that evaluates to `true` iff both `left` and `right` evaluate to `true`.
[Not](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/expressions/filter/Not.html "class in org.apache.spark.sql.connector.expressions.filter")
A predicate that evaluates to `true` iff `child` is evaluated to `false`.
[Or](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/expressions/filter/Or.html "class in org.apache.spark.sql.connector.expressions.filter")
A predicate that evaluates to `true` iff at least one of `left` or `right` evaluates to `true`.
[Predicate](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/expressions/filter/Predicate.html "class in org.apache.spark.sql.connector.expressions.filter")
The general representation of predicate expressions, which contains the upper-cased expression name and all the children expressions.
