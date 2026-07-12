[Skip navigation links](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/expressions/aggregate/package-summary.html#skip-navbar-top "Skip navigation links")
  * [Overview](https://spark.apache.org/docs/latest/api/java/index.html)
  * Package
  * Class
  * [Deprecated](https://spark.apache.org/docs/latest/api/java/deprecated-list.html)
  * [Index](https://spark.apache.org/docs/latest/api/java/index-all.html)
  * [Help](https://spark.apache.org/docs/latest/api/java/help-doc.html#package)


  * Package: 
  * Description | 
  * [Related Packages](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/expressions/aggregate/package-summary.html#related-package-summary) | 
  * [Classes and Interfaces](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/expressions/aggregate/package-summary.html#class-summary)


SEARCH:
# Package org.apache.spark.sql.connector.expressions.aggregate
* * *
package org.apache.spark.sql.connector.expressions.aggregate
  * Related Packages
Package
Description
[org.apache.spark.sql.connector.expressions](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/expressions/package-summary.html)
[org.apache.spark.sql.connector.expressions.filter](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/expressions/filter/package-summary.html)
  * All Classes and InterfacesInterfacesClassesRecord Classes
Class
Description
[AggregateFunc](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/expressions/aggregate/AggregateFunc.html "interface in org.apache.spark.sql.connector.expressions.aggregate")
Base class of the Aggregate Functions.
[Aggregation](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/expressions/aggregate/Aggregation.html "class in org.apache.spark.sql.connector.expressions.aggregate")
Aggregation in SQL statement.
[Avg](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/expressions/aggregate/Avg.html "class in org.apache.spark.sql.connector.expressions.aggregate")
An aggregate function that returns the mean of all the values in a group.
[Count](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/expressions/aggregate/Count.html "class in org.apache.spark.sql.connector.expressions.aggregate")
An aggregate function that returns the number of the specific row in a group.
[CountStar](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/expressions/aggregate/CountStar.html "class in org.apache.spark.sql.connector.expressions.aggregate")
An aggregate function that returns the number of rows in a group.
[GeneralAggregateFunc](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/expressions/aggregate/GeneralAggregateFunc.html "class in org.apache.spark.sql.connector.expressions.aggregate")
The general implementation of [`AggregateFunc`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/expressions/aggregate/AggregateFunc.html "interface in org.apache.spark.sql.connector.expressions.aggregate"), which contains the upper-cased function name, the `isDistinct` flag and all the inputs.
[Max](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/expressions/aggregate/Max.html "class in org.apache.spark.sql.connector.expressions.aggregate")
An aggregate function that returns the maximum value in a group.
[Min](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/expressions/aggregate/Min.html "class in org.apache.spark.sql.connector.expressions.aggregate")
An aggregate function that returns the minimum value in a group.
[Sum](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/expressions/aggregate/Sum.html "class in org.apache.spark.sql.connector.expressions.aggregate")
An aggregate function that returns the summation of all the values in a group.
[UserDefinedAggregateFunc](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/expressions/aggregate/UserDefinedAggregateFunc.html "class in org.apache.spark.sql.connector.expressions.aggregate")
The general representation of user defined aggregate function, which implements [`AggregateFunc`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/expressions/aggregate/AggregateFunc.html "interface in org.apache.spark.sql.connector.expressions.aggregate"), contains the upper-cased function name, the canonical function name, the `isDistinct` flag and all the inputs.


