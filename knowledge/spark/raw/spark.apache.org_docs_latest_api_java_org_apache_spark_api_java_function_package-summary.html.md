[Skip navigation links](https://spark.apache.org/docs/latest/api/java/org/apache/spark/api/java/function/package-summary.html#skip-navbar-top "Skip navigation links")
  * [Overview](https://spark.apache.org/docs/latest/api/java/index.html)
  * Package
  * Class
  * [Deprecated](https://spark.apache.org/docs/latest/api/java/deprecated-list.html)
  * [Index](https://spark.apache.org/docs/latest/api/java/index-all.html)
  * [Help](https://spark.apache.org/docs/latest/api/java/help-doc.html#package)


  * Package: 
  * [Description](https://spark.apache.org/docs/latest/api/java/org/apache/spark/api/java/function/package-summary.html#package-description) | 
  * [Related Packages](https://spark.apache.org/docs/latest/api/java/org/apache/spark/api/java/function/package-summary.html#related-package-summary) | 
  * [Classes and Interfaces](https://spark.apache.org/docs/latest/api/java/org/apache/spark/api/java/function/package-summary.html#class-summary)


SEARCH:
# Package org.apache.spark.api.java.function
* * *
package org.apache.spark.api.java.function
Set of interfaces to represent functions in Spark's Java API. Users create implementations of these interfaces to pass functions to various Java API methods for Spark. Please visit Spark's Java programming guide for more details.
  * Related Packages
Package
Description
[org.apache.spark.api.java](https://spark.apache.org/docs/latest/api/java/org/apache/spark/api/java/package-summary.html)
Spark Java programming APIs.
  * Interfaces
Class
Description
[CoGroupFunction](https://spark.apache.org/docs/latest/api/java/org/apache/spark/api/java/function/CoGroupFunction.html "interface in org.apache.spark.api.java.function")<K,V1,V2,R>
A function that returns zero or more output records from each grouping key and its values from 2 Datasets.
[DoubleFlatMapFunction](https://spark.apache.org/docs/latest/api/java/org/apache/spark/api/java/function/DoubleFlatMapFunction.html "interface in org.apache.spark.api.java.function")<T>
A function that returns zero or more records of type Double from each input record.
[DoubleFunction](https://spark.apache.org/docs/latest/api/java/org/apache/spark/api/java/function/DoubleFunction.html "interface in org.apache.spark.api.java.function")<T>
A function that returns Doubles, and can be used to construct DoubleRDDs.
[FilterFunction](https://spark.apache.org/docs/latest/api/java/org/apache/spark/api/java/function/FilterFunction.html "interface in org.apache.spark.api.java.function")<T>
Base interface for a function used in Dataset's filter function.
[FlatMapFunction](https://spark.apache.org/docs/latest/api/java/org/apache/spark/api/java/function/FlatMapFunction.html "interface in org.apache.spark.api.java.function")<T,R>
A function that returns zero or more output records from each input record.
[FlatMapFunction2](https://spark.apache.org/docs/latest/api/java/org/apache/spark/api/java/function/FlatMapFunction2.html "interface in org.apache.spark.api.java.function")<T1,T2,R>
A function that takes two inputs and returns zero or more output records.
[FlatMapGroupsFunction](https://spark.apache.org/docs/latest/api/java/org/apache/spark/api/java/function/FlatMapGroupsFunction.html "interface in org.apache.spark.api.java.function")<K,V,R>
A function that returns zero or more output records from each grouping key and its values.
[FlatMapGroupsWithStateFunction](https://spark.apache.org/docs/latest/api/java/org/apache/spark/api/java/function/FlatMapGroupsWithStateFunction.html "interface in org.apache.spark.api.java.function")<K,V,S,R>
::Experimental:: Base interface for a map function used in `org.apache.spark.sql.KeyValueGroupedDataset.flatMapGroupsWithState(  FlatMapGroupsWithStateFunction, org.apache.spark.sql.streaming.OutputMode,  org.apache.spark.sql.Encoder, org.apache.spark.sql.Encoder)`
[ForeachFunction](https://spark.apache.org/docs/latest/api/java/org/apache/spark/api/java/function/ForeachFunction.html "interface in org.apache.spark.api.java.function")<T>
Base interface for a function used in Dataset's foreach function.
[ForeachPartitionFunction](https://spark.apache.org/docs/latest/api/java/org/apache/spark/api/java/function/ForeachPartitionFunction.html "interface in org.apache.spark.api.java.function")<T>
Base interface for a function used in Dataset's foreachPartition function.
[Function](https://spark.apache.org/docs/latest/api/java/org/apache/spark/api/java/function/Function.html "interface in org.apache.spark.api.java.function")<T1,R>
Base interface for functions whose return types do not create special RDDs.
[Function0](https://spark.apache.org/docs/latest/api/java/org/apache/spark/api/java/function/Function0.html "interface in org.apache.spark.api.java.function")<R>
A zero-argument function that returns an R.
[Function2](https://spark.apache.org/docs/latest/api/java/org/apache/spark/api/java/function/Function2.html "interface in org.apache.spark.api.java.function")<T1,T2,R>
A two-argument function that takes arguments of type T1 and T2 and returns an R.
[Function3](https://spark.apache.org/docs/latest/api/java/org/apache/spark/api/java/function/Function3.html "interface in org.apache.spark.api.java.function")<T1,T2,T3,R>
A three-argument function that takes arguments of type T1, T2 and T3 and returns an R.
[Function4](https://spark.apache.org/docs/latest/api/java/org/apache/spark/api/java/function/Function4.html "interface in org.apache.spark.api.java.function")<T1,T2,T3,T4,R>
A four-argument function that takes arguments of type T1, T2, T3 and T4 and returns an R.
[MapFunction](https://spark.apache.org/docs/latest/api/java/org/apache/spark/api/java/function/MapFunction.html "interface in org.apache.spark.api.java.function")<T,U>
Base interface for a map function used in Dataset's map function.
[MapGroupsFunction](https://spark.apache.org/docs/latest/api/java/org/apache/spark/api/java/function/MapGroupsFunction.html "interface in org.apache.spark.api.java.function")<K,V,R>
Base interface for a map function used in GroupedDataset's mapGroup function.
[MapGroupsWithStateFunction](https://spark.apache.org/docs/latest/api/java/org/apache/spark/api/java/function/MapGroupsWithStateFunction.html "interface in org.apache.spark.api.java.function")<K,V,S,R>
::Experimental:: Base interface for a map function used in [`KeyValueGroupedDataset.mapGroupsWithState(MapGroupsWithStateFunction, org.apache.spark.sql.Encoder, org.apache.spark.sql.Encoder)`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/KeyValueGroupedDataset.html#mapGroupsWithState\(org.apache.spark.api.java.function.MapGroupsWithStateFunction,org.apache.spark.sql.Encoder,org.apache.spark.sql.Encoder\))
[MapPartitionsFunction](https://spark.apache.org/docs/latest/api/java/org/apache/spark/api/java/function/MapPartitionsFunction.html "interface in org.apache.spark.api.java.function")<T,U>
Base interface for function used in Dataset's mapPartitions.
[PairFlatMapFunction](https://spark.apache.org/docs/latest/api/java/org/apache/spark/api/java/function/PairFlatMapFunction.html "interface in org.apache.spark.api.java.function")<T,K,V>
A function that returns zero or more key-value pair records from each input record.
[PairFunction](https://spark.apache.org/docs/latest/api/java/org/apache/spark/api/java/function/PairFunction.html "interface in org.apache.spark.api.java.function")<T,K,V>
A function that returns key-value pairs (Tuple2<K, V>), and can be used to construct PairRDDs.
[ReduceFunction](https://spark.apache.org/docs/latest/api/java/org/apache/spark/api/java/function/ReduceFunction.html "interface in org.apache.spark.api.java.function")<T>
Base interface for function used in Dataset's reduce.
[VoidFunction](https://spark.apache.org/docs/latest/api/java/org/apache/spark/api/java/function/VoidFunction.html "interface in org.apache.spark.api.java.function")<T>
A function with no return value.
[VoidFunction2](https://spark.apache.org/docs/latest/api/java/org/apache/spark/api/java/function/VoidFunction2.html "interface in org.apache.spark.api.java.function")<T1,T2>
A two-argument function that takes arguments of type T1 and T2 with no return value.


