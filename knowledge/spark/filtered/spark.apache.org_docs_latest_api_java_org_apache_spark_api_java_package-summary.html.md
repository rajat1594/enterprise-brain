[Skip navigation links](https://spark.apache.org/docs/latest/api/java/org/apache/spark/api/java/package-summary.html#skip-navbar-top "Skip navigation links")
  * [Overview](https://spark.apache.org/docs/latest/api/java/index.html)
  * Package
  * Class
  * [Deprecated](https://spark.apache.org/docs/latest/api/java/deprecated-list.html)
  * [Index](https://spark.apache.org/docs/latest/api/java/index-all.html)
  * [Help](https://spark.apache.org/docs/latest/api/java/help-doc.html#package)


  * Package: 
  * [Description](https://spark.apache.org/docs/latest/api/java/org/apache/spark/api/java/package-summary.html#package-description) | 
  * [Related Packages](https://spark.apache.org/docs/latest/api/java/org/apache/spark/api/java/package-summary.html#related-package-summary) | 
  * [Classes and Interfaces](https://spark.apache.org/docs/latest/api/java/org/apache/spark/api/java/package-summary.html#class-summary)


SEARCH:
# Package org.apache.spark.api.java
* * *
package org.apache.spark.api.java
Spark Java programming APIs.
  * Related Packages
Package
Description
[org.apache.spark.api.java.function](https://spark.apache.org/docs/latest/api/java/org/apache/spark/api/java/function/package-summary.html)
Set of interfaces to represent functions in Spark's Java API.
  * All Classes and InterfacesInterfacesClasses
Class
Description
[JavaDoubleRDD](https://spark.apache.org/docs/latest/api/java/org/apache/spark/api/java/JavaDoubleRDD.html "class in org.apache.spark.api.java")
[JavaFutureAction](https://spark.apache.org/docs/latest/api/java/org/apache/spark/api/java/JavaFutureAction.html "interface in org.apache.spark.api.java")<T>
[JavaHadoopRDD](https://spark.apache.org/docs/latest/api/java/org/apache/spark/api/java/JavaHadoopRDD.html "class in org.apache.spark.api.java")<K,V>
[JavaNewHadoopRDD](https://spark.apache.org/docs/latest/api/java/org/apache/spark/api/java/JavaNewHadoopRDD.html "class in org.apache.spark.api.java")<K,V>
[JavaPairRDD](https://spark.apache.org/docs/latest/api/java/org/apache/spark/api/java/JavaPairRDD.html "class in org.apache.spark.api.java")<K,V>
[JavaRDD](https://spark.apache.org/docs/latest/api/java/org/apache/spark/api/java/JavaRDD.html "class in org.apache.spark.api.java")<T>
[JavaRDDLike](https://spark.apache.org/docs/latest/api/java/org/apache/spark/api/java/JavaRDDLike.html "interface in org.apache.spark.api.java")<T,This extends [JavaRDDLike](https://spark.apache.org/docs/latest/api/java/org/apache/spark/api/java/JavaRDDLike.html "interface in org.apache.spark.api.java")<T,This>>
Defines operations common to several Java RDD implementations.
[JavaSparkContext](https://spark.apache.org/docs/latest/api/java/org/apache/spark/api/java/JavaSparkContext.html "class in org.apache.spark.api.java")
A Java-friendly version of [`SparkContext`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/SparkContext.html "class in org.apache.spark") that returns [`JavaRDD`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/api/java/JavaRDD.html "class in org.apache.spark.api.java")s and works with Java collections instead of Scala ones.
[JavaSparkStatusTracker](https://spark.apache.org/docs/latest/api/java/org/apache/spark/api/java/JavaSparkStatusTracker.html "class in org.apache.spark.api.java")
Low-level status reporting APIs for monitoring job and stage progress.
[JavaUtils](https://spark.apache.org/docs/latest/api/java/org/apache/spark/api/java/JavaUtils.html "class in org.apache.spark.api.java")
[JavaUtils.SerializableMapWrapper](https://spark.apache.org/docs/latest/api/java/org/apache/spark/api/java/JavaUtils.SerializableMapWrapper.html "class in org.apache.spark.api.java")<A,B>
[Optional](https://spark.apache.org/docs/latest/api/java/org/apache/spark/api/java/Optional.html "class in org.apache.spark.api.java")<T>
Like `java.util.Optional` in Java 8, `scala.Option` in Scala, and `com.google.common.base.Optional` in Google Guava, this class represents a value of a given type that may or may not exist.
[StorageLevels](https://spark.apache.org/docs/latest/api/java/org/apache/spark/api/java/StorageLevels.html "class in org.apache.spark.api.java")
Expose some commonly useful storage level constants.


