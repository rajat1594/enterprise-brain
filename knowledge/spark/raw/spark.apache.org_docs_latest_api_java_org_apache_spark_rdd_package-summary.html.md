[Skip navigation links](https://spark.apache.org/docs/latest/api/java/org/apache/spark/rdd/package-summary.html#skip-navbar-top "Skip navigation links")
  * [Overview](https://spark.apache.org/docs/latest/api/java/index.html)
  * Package
  * Class
  * [Deprecated](https://spark.apache.org/docs/latest/api/java/deprecated-list.html)
  * [Index](https://spark.apache.org/docs/latest/api/java/index-all.html)
  * [Help](https://spark.apache.org/docs/latest/api/java/help-doc.html#package)


  * Package: 
  * [Description](https://spark.apache.org/docs/latest/api/java/org/apache/spark/rdd/package-summary.html#package-description) | 
  * [Related Packages](https://spark.apache.org/docs/latest/api/java/org/apache/spark/rdd/package-summary.html#related-package-summary) | 
  * [Classes and Interfaces](https://spark.apache.org/docs/latest/api/java/org/apache/spark/rdd/package-summary.html#class-summary)


SEARCH:
# Package org.apache.spark.rdd
* * *
package org.apache.spark.rdd
Provides implementation's of various RDDs.
  * Related Packages
Package
Description
[org.apache.spark](https://spark.apache.org/docs/latest/api/java/org/apache/spark/package-summary.html)
Core Spark classes in Scala.
  * All Classes and InterfacesInterfacesClasses
Class
Description
[AsyncRDDActions](https://spark.apache.org/docs/latest/api/java/org/apache/spark/rdd/AsyncRDDActions.html "class in org.apache.spark.rdd")<T>
A set of asynchronous RDD actions available through an implicit conversion.
[CheckpointState](https://spark.apache.org/docs/latest/api/java/org/apache/spark/rdd/CheckpointState.html "class in org.apache.spark.rdd")
Enumeration to manage state transitions of an RDD through checkpointing
[CoGroupedRDD](https://spark.apache.org/docs/latest/api/java/org/apache/spark/rdd/CoGroupedRDD.html "class in org.apache.spark.rdd")<K>
Developer API An RDD that cogroups its parents.
[DefaultPartitionCoalescer](https://spark.apache.org/docs/latest/api/java/org/apache/spark/rdd/DefaultPartitionCoalescer.html "class in org.apache.spark.rdd")
Coalesce the partitions of a parent RDD (`prev`) into fewer partitions, so that each partition of this RDD computes one or more of the parent ones.
[DeterministicLevel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/rdd/DeterministicLevel.html "class in org.apache.spark.rdd")
The deterministic level of RDD's output (i.e.
[DoubleRDDFunctions](https://spark.apache.org/docs/latest/api/java/org/apache/spark/rdd/DoubleRDDFunctions.html "class in org.apache.spark.rdd")
Extra functions available on RDDs of Doubles through an implicit conversion.
[HadoopRDD](https://spark.apache.org/docs/latest/api/java/org/apache/spark/rdd/HadoopRDD.html "class in org.apache.spark.rdd")<K,V>
Developer API An RDD that provides core functionality for reading data stored in Hadoop (e.g., files in HDFS, sources in HBase, or S3), using the older MapReduce API (`org.apache.hadoop.mapred`).
[HadoopRDD.HadoopMapPartitionsWithSplitRDD$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/rdd/HadoopRDD.HadoopMapPartitionsWithSplitRDD$.html "class in org.apache.spark.rdd")
[InputFileBlockHolder](https://spark.apache.org/docs/latest/api/java/org/apache/spark/rdd/InputFileBlockHolder.html "class in org.apache.spark.rdd")
This holds file names of the current Spark task.
[JdbcRDD](https://spark.apache.org/docs/latest/api/java/org/apache/spark/rdd/JdbcRDD.html "class in org.apache.spark.rdd")<T>
Deprecated. 
Jdbc RDD is deprecated, consider using JDBC data source instead.
[JdbcRDD.ConnectionFactory](https://spark.apache.org/docs/latest/api/java/org/apache/spark/rdd/JdbcRDD.ConnectionFactory.html "interface in org.apache.spark.rdd")
[NewHadoopRDD](https://spark.apache.org/docs/latest/api/java/org/apache/spark/rdd/NewHadoopRDD.html "class in org.apache.spark.rdd")<K,V>
Developer API An RDD that provides core functionality for reading data stored in Hadoop (e.g., files in HDFS, sources in HBase, or S3), using the new MapReduce API (`org.apache.hadoop.mapreduce`).
[NewHadoopRDD.NewHadoopMapPartitionsWithSplitRDD$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/rdd/NewHadoopRDD.NewHadoopMapPartitionsWithSplitRDD$.html "class in org.apache.spark.rdd")
[OrderedRDDFunctions](https://spark.apache.org/docs/latest/api/java/org/apache/spark/rdd/OrderedRDDFunctions.html "class in org.apache.spark.rdd")<K,V,P extends scala.Product2<K,V>>
Extra functions available on RDDs of (key, value) pairs where the key is sortable through an implicit conversion.
[PairRDDFunctions](https://spark.apache.org/docs/latest/api/java/org/apache/spark/rdd/PairRDDFunctions.html "class in org.apache.spark.rdd")<K,V>
Extra functions available on RDDs of (key, value) pairs through an implicit conversion.
[PartitionCoalescer](https://spark.apache.org/docs/latest/api/java/org/apache/spark/rdd/PartitionCoalescer.html "interface in org.apache.spark.rdd")
::DeveloperApi:: A PartitionCoalescer defines how to coalesce the partitions of a given RDD.
[PartitionGroup](https://spark.apache.org/docs/latest/api/java/org/apache/spark/rdd/PartitionGroup.html "class in org.apache.spark.rdd")
::DeveloperApi:: A group of `Partition`s param: prefLoc preferred location for the partition group
[PartitionPruningRDD](https://spark.apache.org/docs/latest/api/java/org/apache/spark/rdd/PartitionPruningRDD.html "class in org.apache.spark.rdd")<T>
Developer API An RDD used to prune RDD partitions/partitions so we can avoid launching tasks on all partitions.
[RDD](https://spark.apache.org/docs/latest/api/java/org/apache/spark/rdd/RDD.html "class in org.apache.spark.rdd")<T>
A Resilient Distributed Dataset (RDD), the basic abstraction in Spark.
[RDDBarrier](https://spark.apache.org/docs/latest/api/java/org/apache/spark/rdd/RDDBarrier.html "class in org.apache.spark.rdd")<T>
Experimental Wraps an RDD in a barrier stage, which forces Spark to launch tasks of this stage together.
[SequenceFileRDDFunctions](https://spark.apache.org/docs/latest/api/java/org/apache/spark/rdd/SequenceFileRDDFunctions.html "class in org.apache.spark.rdd")<K,V>
Extra functions available on RDDs of (key, value) pairs to create a Hadoop SequenceFile, through an implicit conversion.
[ShuffledRDD](https://spark.apache.org/docs/latest/api/java/org/apache/spark/rdd/ShuffledRDD.html "class in org.apache.spark.rdd")<K,V,C>
Developer API The resulting RDD from a shuffle (e.g.
[UnionRDD](https://spark.apache.org/docs/latest/api/java/org/apache/spark/rdd/UnionRDD.html "class in org.apache.spark.rdd")<T>


