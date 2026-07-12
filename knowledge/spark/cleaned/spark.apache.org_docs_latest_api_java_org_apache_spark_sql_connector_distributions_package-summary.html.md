[Skip navigation links](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/distributions/package-summary.html#skip-navbar-top "Skip navigation links")
  * [Overview](https://spark.apache.org/docs/latest/api/java/index.html)
  * Package
  * Class
  * [Deprecated](https://spark.apache.org/docs/latest/api/java/deprecated-list.html)
  * [Index](https://spark.apache.org/docs/latest/api/java/index-all.html)
  * [Help](https://spark.apache.org/docs/latest/api/java/help-doc.html#package)

  * Package:
  * Description |
  * [Related Packages](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/distributions/package-summary.html#related-package-summary) |
  * [Classes and Interfaces](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/distributions/package-summary.html#class-summary)

SEARCH:
# Package org.apache.spark.sql.connector.distributions
* * *
package org.apache.spark.sql.connector.distributions
  * Related Packages
Package
Description
[org.apache.spark.sql.connector](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/package-summary.html)
  * All Classes and InterfacesInterfacesClasses
Class
Description
[ClusteredDistribution](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/distributions/ClusteredDistribution.html "interface in org.apache.spark.sql.connector.distributions")
A distribution where tuples that share the same values for clustering expressions are co-located in the same partition.
[Distribution](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/distributions/Distribution.html "interface in org.apache.spark.sql.connector.distributions")
An interface that defines how data is distributed across partitions.
[Distributions](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/distributions/Distributions.html "class in org.apache.spark.sql.connector.distributions")
Helper methods to create distributions to pass into Spark.
[LogicalDistributions](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/distributions/LogicalDistributions.html "class in org.apache.spark.sql.connector.distributions")
[OrderedDistribution](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/distributions/OrderedDistribution.html "interface in org.apache.spark.sql.connector.distributions")
A distribution where tuples have been ordered across partitions according to ordering expressions, but not necessarily within a given partition.
[UnspecifiedDistribution](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/distributions/UnspecifiedDistribution.html "interface in org.apache.spark.sql.connector.distributions")
A distribution where no promises are made about co-location of data.
[UnspecifiedDistributionImpl](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/distributions/UnspecifiedDistributionImpl.html "class in org.apache.spark.sql.connector.distributions")
