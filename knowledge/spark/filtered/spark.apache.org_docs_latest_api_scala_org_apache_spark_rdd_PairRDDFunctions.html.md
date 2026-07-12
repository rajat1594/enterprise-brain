Spark 4.1.2 ScalaDoc < Back
 __ __
# Packages
  * [__](https://spark.apache.org/docs/latest/api/scala/index.html "Permalink") package [root](https://spark.apache.org/docs/latest/api/scala/index.html) 

Definition Classes
    [root](https://spark.apache.org/docs/latest/api/scala/index.html "_root_")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/index.html "Permalink") package [org](https://spark.apache.org/docs/latest/api/scala/org/index.html) 

Definition Classes
    [root](https://spark.apache.org/docs/latest/api/scala/index.html "_root_")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/index.html "Permalink") package [apache](https://spark.apache.org/docs/latest/api/scala/org/apache/index.html) 

Definition Classes
    [org](https://spark.apache.org/docs/latest/api/scala/org/index.html "org")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "Permalink") package [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "Core Spark functionality.")
Core Spark functionality.
Core Spark functionality. [org.apache.spark.SparkContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html "org.apache.spark.SparkContext") serves as the main entry point to Spark, while [org.apache.spark.rdd.RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") is the data type representing a distributed collection, and provides most parallel operations.
In addition, [org.apache.spark.rdd.PairRDDFunctions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html "org.apache.spark.rdd.PairRDDFunctions") contains operations available only on RDDs of key-value pairs, such as `groupByKey` and `join`; [org.apache.spark.rdd.DoubleRDDFunctions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/DoubleRDDFunctions.html "org.apache.spark.rdd.DoubleRDDFunctions") contains operations available only on RDDs of Doubles; and [org.apache.spark.rdd.SequenceFileRDDFunctions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/SequenceFileRDDFunctions.html "org.apache.spark.rdd.SequenceFileRDDFunctions") contains operations available on RDDs that can be saved as SequenceFiles. These operations are automatically available on any RDD of the right type (e.g. RDD[(Int, Int)] through implicit conversions.
Java programmers should reference the [org.apache.spark.api.java](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/index.html "org.apache.spark.api.java") package for Spark programming APIs in Java.
Classes and methods marked with  Experimental are user-facing features which have not been officially adopted by the Spark project. These are subject to change or removal in minor releases.
Classes and methods marked with  Developer API are intended for advanced users want to extend Spark through lower level interfaces. These are subject to changes or removal in minor releases.  

Definition Classes
    [apache](https://spark.apache.org/docs/latest/api/scala/org/apache/index.html "org.apache")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/index.html "Permalink") package [rdd](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/index.html "Provides several RDD implementations.")
Provides several RDD implementations.
Provides several RDD implementations. See [org.apache.spark.rdd.RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD").  

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/AsyncRDDActions.html "A set of asynchronous RDD actions available through an implicit conversion.")[AsyncRDDActions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/AsyncRDDActions.html "A set of asynchronous RDD actions available through an implicit conversion.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/CoGroupedRDD.html ":: DeveloperApi :: An RDD that cogroups its parents.")[CoGroupedRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/CoGroupedRDD.html ":: DeveloperApi :: An RDD that cogroups its parents.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/DeterministicLevel$.html "The deterministic level of RDD's output \(i.e.")[DeterministicLevel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/DeterministicLevel$.html "The deterministic level of RDD's output \(i.e.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/DoubleRDDFunctions.html "Extra functions available on RDDs of Doubles through an implicit conversion.")[DoubleRDDFunctions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/DoubleRDDFunctions.html "Extra functions available on RDDs of Doubles through an implicit conversion.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/HadoopRDD.html ":: DeveloperApi :: An RDD that provides core functionality for reading data stored in Hadoop \(e.g., files in HDFS, sources in HBase, or S3\), using the older MapReduce API \(org.apache.hadoop.mapred\).")[HadoopRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/HadoopRDD.html ":: DeveloperApi :: An RDD that provides core functionality for reading data stored in Hadoop \(e.g., files in HDFS, sources in HBase, or S3\), using the older MapReduce API \(org.apache.hadoop.mapred\).")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/JdbcRDD$.html) [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/JdbcRDD.html "An RDD that executes a SQL query on a JDBC connection and reads results.")[JdbcRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/JdbcRDD.html "An RDD that executes a SQL query on a JDBC connection and reads results.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/NewHadoopRDD.html ":: DeveloperApi :: An RDD that provides core functionality for reading data stored in Hadoop \(e.g., files in HDFS, sources in HBase, or S3\), using the new MapReduce API \(org.apache.hadoop.mapreduce\).")[NewHadoopRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/NewHadoopRDD.html ":: DeveloperApi :: An RDD that provides core functionality for reading data stored in Hadoop \(e.g., files in HDFS, sources in HBase, or S3\), using the new MapReduce API \(org.apache.hadoop.mapreduce\).")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/OrderedRDDFunctions.html "Extra functions available on RDDs of \(key, value\) pairs where the key is sortable through an implicit conversion.")[OrderedRDDFunctions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/OrderedRDDFunctions.html "Extra functions available on RDDs of \(key, value\) pairs where the key is sortable through an implicit conversion.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html "Extra functions available on RDDs of \(key, value\) pairs through an implicit conversion.")[PairRDDFunctions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html "Extra functions available on RDDs of \(key, value\) pairs through an implicit conversion.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PartitionCoalescer.html "::DeveloperApi:: A PartitionCoalescer defines how to coalesce the partitions of a given RDD.")[PartitionCoalescer](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PartitionCoalescer.html "::DeveloperApi:: A PartitionCoalescer defines how to coalesce the partitions of a given RDD.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PartitionGroup.html "::DeveloperApi:: A group of Partitions")[PartitionGroup](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PartitionGroup.html "::DeveloperApi:: A group of Partitions")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PartitionPruningRDD$.html) [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PartitionPruningRDD.html ":: DeveloperApi :: An RDD used to prune RDD partitions/partitions so we can avoid launching tasks on all partitions.")[PartitionPruningRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PartitionPruningRDD.html ":: DeveloperApi :: An RDD used to prune RDD partitions/partitions so we can avoid launching tasks on all partitions.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD$.html "Defines implicit functions that provide extra functionalities on RDDs of specific types.") [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "A Resilient Distributed Dataset \(RDD\), the basic abstraction in Spark.")[RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "A Resilient Distributed Dataset \(RDD\), the basic abstraction in Spark.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDDBarrier.html ":: Experimental :: Wraps an RDD in a barrier stage, which forces Spark to launch tasks of this stage together.")[RDDBarrier](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDDBarrier.html ":: Experimental :: Wraps an RDD in a barrier stage, which forces Spark to launch tasks of this stage together.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/SequenceFileRDDFunctions.html "Extra functions available on RDDs of \(key, value\) pairs to create a Hadoop SequenceFile, through an implicit conversion.")[SequenceFileRDDFunctions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/SequenceFileRDDFunctions.html "Extra functions available on RDDs of \(key, value\) pairs to create a Hadoop SequenceFile, through an implicit conversion.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/ShuffledRDD.html ":: DeveloperApi :: The resulting RDD from a shuffle \(e.g.")[ShuffledRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/ShuffledRDD.html ":: DeveloperApi :: The resulting RDD from a shuffle \(e.g.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/UnionRDD$.html) [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/UnionRDD.html)[UnionRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/UnionRDD.html)


c
[org](https://spark.apache.org/docs/latest/api/scala/org/index.html "org").[apache](https://spark.apache.org/docs/latest/api/scala/org/apache/index.html "org.apache").[spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark").[rdd](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/index.html "org.apache.spark.rdd")
# PairRDDFunctions[ __](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html "Permalink")
####  class PairRDDFunctions[K, V] extends Logging with Serializable
Extra functions available on RDDs of (key, value) pairs through an implicit conversion.  

Source
    [PairRDDFunctions.scala](https://github.com/apache/spark/tree/v4.1.2/core/src/main/scala/org/apache/spark/rdd/PairRDDFunctions.scala)
Linear Supertypes
[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable"), Logging, AnyRef, Any
__ __
Ordering
  1. Alphabetic
  2. By Inheritance


Inherited  

  1. PairRDDFunctions
  2. Serializable
  3. Logging
  4. AnyRef
  5. Any


  1. Hide All
  2. Show All


Visibility
  1. Public
  2. Protected


### Instance Constructors
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#<init>\(self:org.apache.spark.rdd.RDD\[\(K,V\)\]\)\(implicitkt:scala.reflect.ClassTag\[K\],implicitvt:scala.reflect.ClassTag\[V\],implicitord:Ordering\[K\]\):org.apache.spark.rdd.PairRDDFunctions\[K,V\] "Permalink") new PairRDDFunctions(self: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, V)])(implicit kt: ClassTag[K], vt: ClassTag[V], ord: Ordering[K] = null)


### Type Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#LogStringContextextendsAnyRef "Permalink") implicit  class LogStringContext extends AnyRef 

Definition Classes
    Logging


### Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html###:Int "Permalink") final  def ##: Int 

Definition Classes
    AnyRef → Any
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#MDC\(key:org.apache.spark.internal.LogKey,value:Any\):org.apache.spark.internal.MDC "Permalink") def MDC(key: LogKey, value: Any): MDC 

Attributes
    protected  

Definition Classes
    Logging
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#aggregateByKey\[U\]\(zeroValue:U\)\(seqOp:\(U,V\)=>U,combOp:\(U,U\)=>U\)\(implicitevidence$3:scala.reflect.ClassTag\[U\]\):org.apache.spark.rdd.RDD\[\(K,U\)\] "Permalink") def aggregateByKey[U](zeroValue: U)(seqOp: (U, V) => U, combOp: (U, U) => U)(implicit arg0: ClassTag[U]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, U)]
Aggregate the values of each key, using given combine functions and a neutral "zero value".
Aggregate the values of each key, using given combine functions and a neutral "zero value". This function can return a different result type, U, than the type of the values in this RDD, V. Thus, we need one operation for merging a V into a U and one operation for merging two U's, as in scala.IterableOnce. The former operation is used for merging values within a partition, and the latter is used for merging values between partitions. To avoid memory allocation, both of these functions are allowed to modify and return their first argument instead of creating a new U. 
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#aggregateByKey\[U\]\(zeroValue:U,numPartitions:Int\)\(seqOp:\(U,V\)=>U,combOp:\(U,U\)=>U\)\(implicitevidence$2:scala.reflect.ClassTag\[U\]\):org.apache.spark.rdd.RDD\[\(K,U\)\] "Permalink") def aggregateByKey[U](zeroValue: U, numPartitions: Int)(seqOp: (U, V) => U, combOp: (U, U) => U)(implicit arg0: ClassTag[U]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, U)]
Aggregate the values of each key, using given combine functions and a neutral "zero value".
Aggregate the values of each key, using given combine functions and a neutral "zero value". This function can return a different result type, U, than the type of the values in this RDD, V. Thus, we need one operation for merging a V into a U and one operation for merging two U's, as in scala.IterableOnce. The former operation is used for merging values within a partition, and the latter is used for merging values between partitions. To avoid memory allocation, both of these functions are allowed to modify and return their first argument instead of creating a new U. 
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#aggregateByKey\[U\]\(zeroValue:U,partitioner:org.apache.spark.Partitioner\)\(seqOp:\(U,V\)=>U,combOp:\(U,U\)=>U\)\(implicitevidence$1:scala.reflect.ClassTag\[U\]\):org.apache.spark.rdd.RDD\[\(K,U\)\] "Permalink") def aggregateByKey[U](zeroValue: U, partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner"))(seqOp: (U, V) => U, combOp: (U, U) => U)(implicit arg0: ClassTag[U]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, U)]
Aggregate the values of each key, using given combine functions and a neutral "zero value".
Aggregate the values of each key, using given combine functions and a neutral "zero value". This function can return a different result type, U, than the type of the values in this RDD, V. Thus, we need one operation for merging a V into a U and one operation for merging two U's, as in scala.IterableOnce. The former operation is used for merging values within a partition, and the latter is used for merging values between partitions. To avoid memory allocation, both of these functions are allowed to modify and return their first argument instead of creating a new U. 
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0 

Definition Classes
    Any
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#clone\(\):Object "Permalink") def clone(): AnyRef 

Attributes
    protected[lang]  

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#cogroup\[W1,W2,W3\]\(other1:org.apache.spark.rdd.RDD\[\(K,W1\)\],other2:org.apache.spark.rdd.RDD\[\(K,W2\)\],other3:org.apache.spark.rdd.RDD\[\(K,W3\)\],numPartitions:Int\):org.apache.spark.rdd.RDD\[\(K,\(Iterable\[V\],Iterable\[W1\],Iterable\[W2\],Iterable\[W3\]\)\)\] "Permalink") def cogroup[W1, W2, W3](other1: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, W1)], other2: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, W2)], other3: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, W3)], numPartitions: Int): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, (Iterable[V], Iterable[W1], Iterable[W2], Iterable[W3]))]
For each key k in `this` or `other1` or `other2` or `other3`, return a resulting RDD that contains a tuple with the list of values for that key in `this`, `other1`, `other2` and `other3`.
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#cogroup\[W1,W2\]\(other1:org.apache.spark.rdd.RDD\[\(K,W1\)\],other2:org.apache.spark.rdd.RDD\[\(K,W2\)\],numPartitions:Int\):org.apache.spark.rdd.RDD\[\(K,\(Iterable\[V\],Iterable\[W1\],Iterable\[W2\]\)\)\] "Permalink") def cogroup[W1, W2](other1: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, W1)], other2: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, W2)], numPartitions: Int): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, (Iterable[V], Iterable[W1], Iterable[W2]))]
For each key k in `this` or `other1` or `other2`, return a resulting RDD that contains a tuple with the list of values for that key in `this`, `other1` and `other2`.
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#cogroup\[W\]\(other:org.apache.spark.rdd.RDD\[\(K,W\)\],numPartitions:Int\):org.apache.spark.rdd.RDD\[\(K,\(Iterable\[V\],Iterable\[W\]\)\)\] "Permalink") def cogroup[W](other: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, W)], numPartitions: Int): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, (Iterable[V], Iterable[W]))]
For each key k in `this` or `other`, return a resulting RDD that contains a tuple with the list of values for that key in `this` as well as `other`.
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#cogroup\[W1,W2\]\(other1:org.apache.spark.rdd.RDD\[\(K,W1\)\],other2:org.apache.spark.rdd.RDD\[\(K,W2\)\]\):org.apache.spark.rdd.RDD\[\(K,\(Iterable\[V\],Iterable\[W1\],Iterable\[W2\]\)\)\] "Permalink") def cogroup[W1, W2](other1: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, W1)], other2: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, W2)]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, (Iterable[V], Iterable[W1], Iterable[W2]))]
For each key k in `this` or `other1` or `other2`, return a resulting RDD that contains a tuple with the list of values for that key in `this`, `other1` and `other2`.
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#cogroup\[W\]\(other:org.apache.spark.rdd.RDD\[\(K,W\)\]\):org.apache.spark.rdd.RDD\[\(K,\(Iterable\[V\],Iterable\[W\]\)\)\] "Permalink") def cogroup[W](other: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, W)]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, (Iterable[V], Iterable[W]))]
For each key k in `this` or `other`, return a resulting RDD that contains a tuple with the list of values for that key in `this` as well as `other`.
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#cogroup\[W1,W2,W3\]\(other1:org.apache.spark.rdd.RDD\[\(K,W1\)\],other2:org.apache.spark.rdd.RDD\[\(K,W2\)\],other3:org.apache.spark.rdd.RDD\[\(K,W3\)\]\):org.apache.spark.rdd.RDD\[\(K,\(Iterable\[V\],Iterable\[W1\],Iterable\[W2\],Iterable\[W3\]\)\)\] "Permalink") def cogroup[W1, W2, W3](other1: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, W1)], other2: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, W2)], other3: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, W3)]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, (Iterable[V], Iterable[W1], Iterable[W2], Iterable[W3]))]
For each key k in `this` or `other1` or `other2` or `other3`, return a resulting RDD that contains a tuple with the list of values for that key in `this`, `other1`, `other2` and `other3`.
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#cogroup\[W1,W2\]\(other1:org.apache.spark.rdd.RDD\[\(K,W1\)\],other2:org.apache.spark.rdd.RDD\[\(K,W2\)\],partitioner:org.apache.spark.Partitioner\):org.apache.spark.rdd.RDD\[\(K,\(Iterable\[V\],Iterable\[W1\],Iterable\[W2\]\)\)\] "Permalink") def cogroup[W1, W2](other1: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, W1)], other2: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, W2)], partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner")): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, (Iterable[V], Iterable[W1], Iterable[W2]))]
For each key k in `this` or `other1` or `other2`, return a resulting RDD that contains a tuple with the list of values for that key in `this`, `other1` and `other2`.
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#cogroup\[W\]\(other:org.apache.spark.rdd.RDD\[\(K,W\)\],partitioner:org.apache.spark.Partitioner\):org.apache.spark.rdd.RDD\[\(K,\(Iterable\[V\],Iterable\[W\]\)\)\] "Permalink") def cogroup[W](other: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, W)], partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner")): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, (Iterable[V], Iterable[W]))]
For each key k in `this` or `other`, return a resulting RDD that contains a tuple with the list of values for that key in `this` as well as `other`.
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#cogroup\[W1,W2,W3\]\(other1:org.apache.spark.rdd.RDD\[\(K,W1\)\],other2:org.apache.spark.rdd.RDD\[\(K,W2\)\],other3:org.apache.spark.rdd.RDD\[\(K,W3\)\],partitioner:org.apache.spark.Partitioner\):org.apache.spark.rdd.RDD\[\(K,\(Iterable\[V\],Iterable\[W1\],Iterable\[W2\],Iterable\[W3\]\)\)\] "Permalink") def cogroup[W1, W2, W3](other1: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, W1)], other2: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, W2)], other3: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, W3)], partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner")): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, (Iterable[V], Iterable[W1], Iterable[W2], Iterable[W3]))]
For each key k in `this` or `other1` or `other2` or `other3`, return a resulting RDD that contains a tuple with the list of values for that key in `this`, `other1`, `other2` and `other3`.
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#collectAsMap\(\):scala.collection.Map\[K,V\] "Permalink") def collectAsMap(): Map[K, V]
Return the key-value pairs in this RDD to the master as a Map.
Return the key-value pairs in this RDD to the master as a Map.
Warning: this doesn't return a multimap (so if you have multiple values to the same key, only one value per key is preserved in the map returned)  

Note
    
this method should only be used if the resulting data is expected to be small, as all the data is loaded into the driver's memory.
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#combineByKey\[C\]\(createCombiner:V=>C,mergeValue:\(C,V\)=>C,mergeCombiners:\(C,C\)=>C\):org.apache.spark.rdd.RDD\[\(K,C\)\] "Permalink") def combineByKey[C](createCombiner: (V) => C, mergeValue: (C, V) => C, mergeCombiners: (C, C) => C): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, C)]
Simplified version of combineByKeyWithClassTag that hash-partitions the resulting RDD using the existing partitioner/parallelism level.
Simplified version of combineByKeyWithClassTag that hash-partitions the resulting RDD using the existing partitioner/parallelism level. This method is here for backward compatibility. It does not provide combiner classtag information to the shuffle.  

See also
    
`combineByKeyWithClassTag`
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#combineByKey\[C\]\(createCombiner:V=>C,mergeValue:\(C,V\)=>C,mergeCombiners:\(C,C\)=>C,numPartitions:Int\):org.apache.spark.rdd.RDD\[\(K,C\)\] "Permalink") def combineByKey[C](createCombiner: (V) => C, mergeValue: (C, V) => C, mergeCombiners: (C, C) => C, numPartitions: Int): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, C)]
Simplified version of combineByKeyWithClassTag that hash-partitions the output RDD.
Simplified version of combineByKeyWithClassTag that hash-partitions the output RDD. This method is here for backward compatibility. It does not provide combiner classtag information to the shuffle.  

See also
    
`combineByKeyWithClassTag`
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#combineByKey\[C\]\(createCombiner:V=>C,mergeValue:\(C,V\)=>C,mergeCombiners:\(C,C\)=>C,partitioner:org.apache.spark.Partitioner,mapSideCombine:Boolean,serializer:org.apache.spark.serializer.Serializer\):org.apache.spark.rdd.RDD\[\(K,C\)\] "Permalink") def combineByKey[C](createCombiner: (V) => C, mergeValue: (C, V) => C, mergeCombiners: (C, C) => C, partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner"), mapSideCombine: Boolean = true, serializer: [Serializer](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/Serializer.html "org.apache.spark.serializer.Serializer") = null): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, C)]
Generic function to combine the elements for each key using a custom set of aggregation functions.
Generic function to combine the elements for each key using a custom set of aggregation functions. This method is here for backward compatibility. It does not provide combiner classtag information to the shuffle.  

See also
    
`combineByKeyWithClassTag`
  23. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#combineByKeyWithClassTag\[C\]\(createCombiner:V=>C,mergeValue:\(C,V\)=>C,mergeCombiners:\(C,C\)=>C\)\(implicitct:scala.reflect.ClassTag\[C\]\):org.apache.spark.rdd.RDD\[\(K,C\)\] "Permalink") def combineByKeyWithClassTag[C](createCombiner: (V) => C, mergeValue: (C, V) => C, mergeCombiners: (C, C) => C)(implicit ct: ClassTag[C]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, C)]
Simplified version of combineByKeyWithClassTag that hash-partitions the resulting RDD using the existing partitioner/parallelism level.
  24. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#combineByKeyWithClassTag\[C\]\(createCombiner:V=>C,mergeValue:\(C,V\)=>C,mergeCombiners:\(C,C\)=>C,numPartitions:Int\)\(implicitct:scala.reflect.ClassTag\[C\]\):org.apache.spark.rdd.RDD\[\(K,C\)\] "Permalink") def combineByKeyWithClassTag[C](createCombiner: (V) => C, mergeValue: (C, V) => C, mergeCombiners: (C, C) => C, numPartitions: Int)(implicit ct: ClassTag[C]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, C)]
Simplified version of combineByKeyWithClassTag that hash-partitions the output RDD.
  25. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#combineByKeyWithClassTag\[C\]\(createCombiner:V=>C,mergeValue:\(C,V\)=>C,mergeCombiners:\(C,C\)=>C,partitioner:org.apache.spark.Partitioner,mapSideCombine:Boolean,serializer:org.apache.spark.serializer.Serializer\)\(implicitct:scala.reflect.ClassTag\[C\]\):org.apache.spark.rdd.RDD\[\(K,C\)\] "Permalink") def combineByKeyWithClassTag[C](createCombiner: (V) => C, mergeValue: (C, V) => C, mergeCombiners: (C, C) => C, partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner"), mapSideCombine: Boolean = true, serializer: [Serializer](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/Serializer.html "org.apache.spark.serializer.Serializer") = null)(implicit ct: ClassTag[C]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, C)]
Generic function to combine the elements for each key using a custom set of aggregation functions.
Generic function to combine the elements for each key using a custom set of aggregation functions. Turns an RDD[(K, V)] into a result of type RDD[(K, C)], for a "combined type" C
Users provide three functions:
     * `createCombiner`, which turns a V into a C (e.g., creates a one-element list)
     * `mergeValue`, to merge a V into a C (e.g., adds it to the end of a list)
     * `mergeCombiners`, to combine two C's into a single one.
In addition, users can control the partitioning of the output RDD, and whether to perform map-side aggregation (if a mapper can produce multiple items with the same key).  

Note
    
V and C can be different -- for example, one might group an RDD of type (Int, Int) into an RDD of type (Int, Seq[Int]).
  26. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#countApproxDistinctByKey\(relativeSD:Double\):org.apache.spark.rdd.RDD\[\(K,Long\)\] "Permalink") def countApproxDistinctByKey(relativeSD: Double = 0.05): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, Long)]
Return approximate number of distinct values for each key in this RDD.
Return approximate number of distinct values for each key in this RDD.
The algorithm used is based on streamlib's implementation of "HyperLogLog in Practice: Algorithmic Engineering of a State of The Art Cardinality Estimation Algorithm", available [here](https://doi.org/10.1145/2452376.2452456).  

relativeSD
    
Relative accuracy. Smaller values create counters that require more space. It must be greater than 0.000017.
  27. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#countApproxDistinctByKey\(relativeSD:Double,numPartitions:Int\):org.apache.spark.rdd.RDD\[\(K,Long\)\] "Permalink") def countApproxDistinctByKey(relativeSD: Double, numPartitions: Int): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, Long)]
Return approximate number of distinct values for each key in this RDD.
Return approximate number of distinct values for each key in this RDD.
The algorithm used is based on streamlib's implementation of "HyperLogLog in Practice: Algorithmic Engineering of a State of The Art Cardinality Estimation Algorithm", available [here](https://doi.org/10.1145/2452376.2452456).  

relativeSD
    
Relative accuracy. Smaller values create counters that require more space. It must be greater than 0.000017. 

numPartitions
    
number of partitions of the resulting RDD
  28. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#countApproxDistinctByKey\(relativeSD:Double,partitioner:org.apache.spark.Partitioner\):org.apache.spark.rdd.RDD\[\(K,Long\)\] "Permalink") def countApproxDistinctByKey(relativeSD: Double, partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner")): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, Long)]
Return approximate number of distinct values for each key in this RDD.
Return approximate number of distinct values for each key in this RDD.
The algorithm used is based on streamlib's implementation of "HyperLogLog in Practice: Algorithmic Engineering of a State of The Art Cardinality Estimation Algorithm", available [here](https://doi.org/10.1145/2452376.2452456).  

relativeSD
    
Relative accuracy. Smaller values create counters that require more space. It must be greater than 0.000017. 

partitioner
    
partitioner of the resulting RDD
  29. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#countApproxDistinctByKey\(p:Int,sp:Int,partitioner:org.apache.spark.Partitioner\):org.apache.spark.rdd.RDD\[\(K,Long\)\] "Permalink") def countApproxDistinctByKey(p: Int, sp: Int, partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner")): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, Long)]
Return approximate number of distinct values for each key in this RDD.
Return approximate number of distinct values for each key in this RDD.
The algorithm used is based on streamlib's implementation of "HyperLogLog in Practice: Algorithmic Engineering of a State of The Art Cardinality Estimation Algorithm", available [here](https://doi.org/10.1145/2452376.2452456).
The relative accuracy is approximately `1.054 / sqrt(2^p)`. Setting a nonzero (`sp` is greater than `p`) would trigger sparse representation of registers, which may reduce the memory consumption and increase accuracy when the cardinality is small. `` 

p
    
The precision value for the normal set. `p` must be a value between 4 and `sp` if `sp` is not zero (32 max). 

sp
    
The precision value for the sparse set, between 0 and 32. If `sp` equals 0, the sparse representation is skipped. 

partitioner
    
Partitioner to use for the resulting RDD.
  30. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#countByKey\(\):scala.collection.Map\[K,Long\] "Permalink") def countByKey(): Map[K, Long]
Count the number of elements for each key, collecting the results to a local Map.
Count the number of elements for each key, collecting the results to a local Map.  

Note
    
This method should only be used if the resulting map is expected to be small, as the whole thing is loaded into the driver's memory. To handle very large results, consider using rdd.mapValues(_ => 1L).reduceByKey(_ + _), which returns an RDD[T, Long] instead of a map.
  31. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#countByKeyApprox\(timeout:Long,confidence:Double\):org.apache.spark.partial.PartialResult\[scala.collection.Map\[K,org.apache.spark.partial.BoundedDouble\]\] "Permalink") def countByKeyApprox(timeout: Long, confidence: Double = 0.95): [PartialResult](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/partial/PartialResult.html "org.apache.spark.partial.PartialResult")[Map[K, [BoundedDouble](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/partial/BoundedDouble.html "org.apache.spark.partial.BoundedDouble")]]
Approximate version of countByKey that can return a partial result if it does not finish within a timeout.
Approximate version of countByKey that can return a partial result if it does not finish within a timeout.
The confidence is the probability that the error bounds of the result will contain the true value. That is, if countApprox were called repeatedly with confidence 0.9, we would expect 90% of the results to contain the true count. The confidence must be in the range [0,1] or an exception will be thrown.  

timeout
    
maximum time to wait for the job, in milliseconds 

confidence
    
the desired statistical confidence in the result 

returns
    
a potentially incomplete result, with error bounds
  32. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  33. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#equals\(x$1:Object\):Boolean "Permalink") def equals(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef → Any
  34. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#flatMapValues\[U\]\(f:V=>IterableOnce\[U\]\):org.apache.spark.rdd.RDD\[\(K,U\)\] "Permalink") def flatMapValues[U](f: (V) => IterableOnce[U]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, U)]
Pass each value in the key-value pair RDD through a flatMap function without changing the keys; this also retains the original RDD's partitioning.
  35. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#foldByKey\(zeroValue:V\)\(func:\(V,V\)=>V\):org.apache.spark.rdd.RDD\[\(K,V\)\] "Permalink") def foldByKey(zeroValue: V)(func: (V, V) => V): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, V)]
Merge the values for each key using an associative function and a neutral "zero value" which may be added to the result an arbitrary number of times, and must not change the result (e.g., Nil for list concatenation, 0 for addition, or 1 for multiplication.).
  36. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#foldByKey\(zeroValue:V,numPartitions:Int\)\(func:\(V,V\)=>V\):org.apache.spark.rdd.RDD\[\(K,V\)\] "Permalink") def foldByKey(zeroValue: V, numPartitions: Int)(func: (V, V) => V): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, V)]
Merge the values for each key using an associative function and a neutral "zero value" which may be added to the result an arbitrary number of times, and must not change the result (e.g., Nil for list concatenation, 0 for addition, or 1 for multiplication.).
  37. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#foldByKey\(zeroValue:V,partitioner:org.apache.spark.Partitioner\)\(func:\(V,V\)=>V\):org.apache.spark.rdd.RDD\[\(K,V\)\] "Permalink") def foldByKey(zeroValue: V, partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner"))(func: (V, V) => V): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, V)]
Merge the values for each key using an associative function and a neutral "zero value" which may be added to the result an arbitrary number of times, and must not change the result (e.g., Nil for list concatenation, 0 for addition, or 1 for multiplication.).
  38. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#fullOuterJoin\[W\]\(other:org.apache.spark.rdd.RDD\[\(K,W\)\],numPartitions:Int\):org.apache.spark.rdd.RDD\[\(K,\(Option\[V\],Option\[W\]\)\)\] "Permalink") def fullOuterJoin[W](other: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, W)], numPartitions: Int): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, (Option[V], Option[W]))]
Perform a full outer join of `this` and `other`.
Perform a full outer join of `this` and `other`. For each element (k, v) in `this`, the resulting RDD will either contain all pairs (k, (Some(v), Some(w))) for w in `other`, or the pair (k, (Some(v), None)) if no elements in `other` have key k. Similarly, for each element (k, w) in `other`, the resulting RDD will either contain all pairs (k, (Some(v), Some(w))) for v in `this`, or the pair (k, (None, Some(w))) if no elements in `this` have key k. Hash-partitions the resulting RDD into the given number of partitions. 
  39. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#fullOuterJoin\[W\]\(other:org.apache.spark.rdd.RDD\[\(K,W\)\]\):org.apache.spark.rdd.RDD\[\(K,\(Option\[V\],Option\[W\]\)\)\] "Permalink") def fullOuterJoin[W](other: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, W)]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, (Option[V], Option[W]))]
Perform a full outer join of `this` and `other`.
Perform a full outer join of `this` and `other`. For each element (k, v) in `this`, the resulting RDD will either contain all pairs (k, (Some(v), Some(w))) for w in `other`, or the pair (k, (Some(v), None)) if no elements in `other` have key k. Similarly, for each element (k, w) in `other`, the resulting RDD will either contain all pairs (k, (Some(v), Some(w))) for v in `this`, or the pair (k, (None, Some(w))) if no elements in `this` have key k. Hash-partitions the resulting RDD using the existing partitioner/ parallelism level. 
  40. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#fullOuterJoin\[W\]\(other:org.apache.spark.rdd.RDD\[\(K,W\)\],partitioner:org.apache.spark.Partitioner\):org.apache.spark.rdd.RDD\[\(K,\(Option\[V\],Option\[W\]\)\)\] "Permalink") def fullOuterJoin[W](other: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, W)], partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner")): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, (Option[V], Option[W]))]
Perform a full outer join of `this` and `other`.
Perform a full outer join of `this` and `other`. For each element (k, v) in `this`, the resulting RDD will either contain all pairs (k, (Some(v), Some(w))) for w in `other`, or the pair (k, (Some(v), None)) if no elements in `other` have key k. Similarly, for each element (k, w) in `other`, the resulting RDD will either contain all pairs (k, (Some(v), Some(w))) for v in `this`, or the pair (k, (None, Some(w))) if no elements in `this` have key k. Uses the given Partitioner to partition the output RDD. 
  41. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef] 

Definition Classes
    AnyRef → Any 

Annotations
     @IntrinsicCandidate() @native()
  42. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#groupByKey\(\):org.apache.spark.rdd.RDD\[\(K,Iterable\[V\]\)\] "Permalink") def groupByKey(): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, Iterable[V])]
Group the values for each key in the RDD into a single sequence.
Group the values for each key in the RDD into a single sequence. Hash-partitions the resulting RDD with the existing partitioner/parallelism level. The ordering of elements within each group is not guaranteed, and may even differ each time the resulting RDD is evaluated.  

Note
    
This operation may be very expensive. If you are grouping in order to perform an aggregation (such as a sum or average) over each key, using `PairRDDFunctions.aggregateByKey` or `PairRDDFunctions.reduceByKey` will provide much better performance.
  43. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#groupByKey\(numPartitions:Int\):org.apache.spark.rdd.RDD\[\(K,Iterable\[V\]\)\] "Permalink") def groupByKey(numPartitions: Int): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, Iterable[V])]
Group the values for each key in the RDD into a single sequence.
Group the values for each key in the RDD into a single sequence. Hash-partitions the resulting RDD with into `numPartitions` partitions. The ordering of elements within each group is not guaranteed, and may even differ each time the resulting RDD is evaluated.  

Note
    
This operation may be very expensive. If you are grouping in order to perform an aggregation (such as a sum or average) over each key, using `PairRDDFunctions.aggregateByKey` or `PairRDDFunctions.reduceByKey` will provide much better performance.
, 
As currently implemented, groupByKey must be able to hold all the key-value pairs for any key in memory. If a key has too many values, it can result in an `OutOfMemoryError`.
  44. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#groupByKey\(partitioner:org.apache.spark.Partitioner\):org.apache.spark.rdd.RDD\[\(K,Iterable\[V\]\)\] "Permalink") def groupByKey(partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner")): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, Iterable[V])]
Group the values for each key in the RDD into a single sequence.
Group the values for each key in the RDD into a single sequence. Allows controlling the partitioning of the resulting key-value pair RDD by passing a Partitioner. The ordering of elements within each group is not guaranteed, and may even differ each time the resulting RDD is evaluated.  

Note
    
This operation may be very expensive. If you are grouping in order to perform an aggregation (such as a sum or average) over each key, using `PairRDDFunctions.aggregateByKey` or `PairRDDFunctions.reduceByKey` will provide much better performance.
, 
As currently implemented, groupByKey must be able to hold all the key-value pairs for any key in memory. If a key has too many values, it can result in an `OutOfMemoryError`.
  45. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#groupWith\[W1,W2,W3\]\(other1:org.apache.spark.rdd.RDD\[\(K,W1\)\],other2:org.apache.spark.rdd.RDD\[\(K,W2\)\],other3:org.apache.spark.rdd.RDD\[\(K,W3\)\]\):org.apache.spark.rdd.RDD\[\(K,\(Iterable\[V\],Iterable\[W1\],Iterable\[W2\],Iterable\[W3\]\)\)\] "Permalink") def groupWith[W1, W2, W3](other1: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, W1)], other2: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, W2)], other3: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, W3)]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, (Iterable[V], Iterable[W1], Iterable[W2], Iterable[W3]))]
Alias for cogroup.
  46. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#groupWith\[W1,W2\]\(other1:org.apache.spark.rdd.RDD\[\(K,W1\)\],other2:org.apache.spark.rdd.RDD\[\(K,W2\)\]\):org.apache.spark.rdd.RDD\[\(K,\(Iterable\[V\],Iterable\[W1\],Iterable\[W2\]\)\)\] "Permalink") def groupWith[W1, W2](other1: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, W1)], other2: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, W2)]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, (Iterable[V], Iterable[W1], Iterable[W2]))]
Alias for cogroup.
  47. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#groupWith\[W\]\(other:org.apache.spark.rdd.RDD\[\(K,W\)\]\):org.apache.spark.rdd.RDD\[\(K,\(Iterable\[V\],Iterable\[W\]\)\)\] "Permalink") def groupWith[W](other: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, W)]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, (Iterable[V], Iterable[W]))]
Alias for cogroup.
  48. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#hashCode\(\):Int "Permalink") def hashCode(): Int 

Definition Classes
    AnyRef → Any 

Annotations
     @IntrinsicCandidate() @native()
  49. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#initializeLogIfNecessary\(isInterpreter:Boolean,silent:Boolean\):Boolean "Permalink") def initializeLogIfNecessary(isInterpreter: Boolean, silent: Boolean): Boolean 

Attributes
    protected  

Definition Classes
    Logging
  50. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#initializeLogIfNecessary\(isInterpreter:Boolean\):Unit "Permalink") def initializeLogIfNecessary(isInterpreter: Boolean): Unit 

Attributes
    protected  

Definition Classes
    Logging
  51. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean 

Definition Classes
    Any
  52. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#isTraceEnabled\(\):Boolean "Permalink") def isTraceEnabled(): Boolean 

Attributes
    protected  

Definition Classes
    Logging
  53. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#join\[W\]\(other:org.apache.spark.rdd.RDD\[\(K,W\)\],numPartitions:Int\):org.apache.spark.rdd.RDD\[\(K,\(V,W\)\)\] "Permalink") def join[W](other: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, W)], numPartitions: Int): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, (V, W))]
Return an RDD containing all pairs of elements with matching keys in `this` and `other`.
Return an RDD containing all pairs of elements with matching keys in `this` and `other`. Each pair of elements will be returned as a (k, (v1, v2)) tuple, where (k, v1) is in `this` and (k, v2) is in `other`. Performs a hash join across the cluster. 
  54. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#join\[W\]\(other:org.apache.spark.rdd.RDD\[\(K,W\)\]\):org.apache.spark.rdd.RDD\[\(K,\(V,W\)\)\] "Permalink") def join[W](other: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, W)]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, (V, W))]
Return an RDD containing all pairs of elements with matching keys in `this` and `other`.
Return an RDD containing all pairs of elements with matching keys in `this` and `other`. Each pair of elements will be returned as a (k, (v1, v2)) tuple, where (k, v1) is in `this` and (k, v2) is in `other`. Performs a hash join across the cluster. 
  55. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#join\[W\]\(other:org.apache.spark.rdd.RDD\[\(K,W\)\],partitioner:org.apache.spark.Partitioner\):org.apache.spark.rdd.RDD\[\(K,\(V,W\)\)\] "Permalink") def join[W](other: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, W)], partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner")): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, (V, W))]
Return an RDD containing all pairs of elements with matching keys in `this` and `other`.
Return an RDD containing all pairs of elements with matching keys in `this` and `other`. Each pair of elements will be returned as a (k, (v1, v2)) tuple, where (k, v1) is in `this` and (k, v2) is in `other`. Uses the given Partitioner to partition the output RDD. 
  56. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#keys:org.apache.spark.rdd.RDD\[K\] "Permalink") def keys: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[K]
Return an RDD with the keys of each tuple.
  57. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#leftOuterJoin\[W\]\(other:org.apache.spark.rdd.RDD\[\(K,W\)\],numPartitions:Int\):org.apache.spark.rdd.RDD\[\(K,\(V,Option\[W\]\)\)\] "Permalink") def leftOuterJoin[W](other: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, W)], numPartitions: Int): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, (V, Option[W]))]
Perform a left outer join of `this` and `other`.
Perform a left outer join of `this` and `other`. For each element (k, v) in `this`, the resulting RDD will either contain all pairs (k, (v, Some(w))) for w in `other`, or the pair (k, (v, None)) if no elements in `other` have key k. Hash-partitions the output into `numPartitions` partitions. 
  58. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#leftOuterJoin\[W\]\(other:org.apache.spark.rdd.RDD\[\(K,W\)\]\):org.apache.spark.rdd.RDD\[\(K,\(V,Option\[W\]\)\)\] "Permalink") def leftOuterJoin[W](other: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, W)]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, (V, Option[W]))]
Perform a left outer join of `this` and `other`.
Perform a left outer join of `this` and `other`. For each element (k, v) in `this`, the resulting RDD will either contain all pairs (k, (v, Some(w))) for w in `other`, or the pair (k, (v, None)) if no elements in `other` have key k. Hash-partitions the output using the existing partitioner/parallelism level. 
  59. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#leftOuterJoin\[W\]\(other:org.apache.spark.rdd.RDD\[\(K,W\)\],partitioner:org.apache.spark.Partitioner\):org.apache.spark.rdd.RDD\[\(K,\(V,Option\[W\]\)\)\] "Permalink") def leftOuterJoin[W](other: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, W)], partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner")): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, (V, Option[W]))]
Perform a left outer join of `this` and `other`.
Perform a left outer join of `this` and `other`. For each element (k, v) in `this`, the resulting RDD will either contain all pairs (k, (v, Some(w))) for w in `other`, or the pair (k, (v, None)) if no elements in `other` have key k. Uses the given Partitioner to partition the output RDD. 
  60. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#log:org.slf4j.Logger "Permalink") def log: Logger 

Attributes
    protected  

Definition Classes
    Logging
  61. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#logBasedOnLevel\(level:org.slf4j.event.Level\)\(f:=>org.apache.spark.internal.MessageWithContext\):Unit "Permalink") def logBasedOnLevel(level: Level)(f: => MessageWithContext): Unit 

Attributes
    protected  

Definition Classes
    Logging
  62. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#logDebug\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logDebug(msg: => String, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  63. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#logDebug\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logDebug(entry: LogEntry, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  64. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#logDebug\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logDebug(entry: LogEntry): Unit 

Attributes
    protected  

Definition Classes
    Logging
  65. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#logDebug\(msg:=>String\):Unit "Permalink") def logDebug(msg: => String): Unit 

Attributes
    protected  

Definition Classes
    Logging
  66. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#logError\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logError(msg: => String, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  67. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#logError\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logError(entry: LogEntry, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  68. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#logError\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logError(entry: LogEntry): Unit 

Attributes
    protected  

Definition Classes
    Logging
  69. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#logError\(msg:=>String\):Unit "Permalink") def logError(msg: => String): Unit 

Attributes
    protected  

Definition Classes
    Logging
  70. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#logInfo\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logInfo(msg: => String, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  71. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#logInfo\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logInfo(entry: LogEntry, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  72. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#logInfo\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logInfo(entry: LogEntry): Unit 

Attributes
    protected  

Definition Classes
    Logging
  73. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#logInfo\(msg:=>String\):Unit "Permalink") def logInfo(msg: => String): Unit 

Attributes
    protected  

Definition Classes
    Logging
  74. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#logName:String "Permalink") def logName: [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String") 

Attributes
    protected  

Definition Classes
    Logging
  75. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#logTrace\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logTrace(msg: => String, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  76. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#logTrace\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logTrace(entry: LogEntry, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  77. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#logTrace\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logTrace(entry: LogEntry): Unit 

Attributes
    protected  

Definition Classes
    Logging
  78. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#logTrace\(msg:=>String\):Unit "Permalink") def logTrace(msg: => String): Unit 

Attributes
    protected  

Definition Classes
    Logging
  79. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#logWarning\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logWarning(msg: => String, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  80. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#logWarning\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logWarning(entry: LogEntry, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  81. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#logWarning\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logWarning(entry: LogEntry): Unit 

Attributes
    protected  

Definition Classes
    Logging
  82. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#logWarning\(msg:=>String\):Unit "Permalink") def logWarning(msg: => String): Unit 

Attributes
    protected  

Definition Classes
    Logging
  83. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#lookup\(key:K\):Seq\[V\] "Permalink") def lookup(key: K): Seq[V]
Return the list of values in the RDD for key `key`.
Return the list of values in the RDD for key `key`. This operation is done efficiently if the RDD has a known partitioner by only searching the partition that the key maps to. 
  84. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#mapValues\[U\]\(f:V=>U\):org.apache.spark.rdd.RDD\[\(K,U\)\] "Permalink") def mapValues[U](f: (V) => U): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, U)]
Pass each value in the key-value pair RDD through a map function without changing the keys; this also retains the original RDD's partitioning.
  85. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  86. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#notify\(\):Unit "Permalink") final  def notify(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  87. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  88. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#partitionBy\(partitioner:org.apache.spark.Partitioner\):org.apache.spark.rdd.RDD\[\(K,V\)\] "Permalink") def partitionBy(partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner")): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, V)]
Return a copy of the RDD partitioned using the specified partitioner.
  89. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#reduceByKey\(func:\(V,V\)=>V\):org.apache.spark.rdd.RDD\[\(K,V\)\] "Permalink") def reduceByKey(func: (V, V) => V): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, V)]
Merge the values for each key using an associative and commutative reduce function.
Merge the values for each key using an associative and commutative reduce function. This will also perform the merging locally on each mapper before sending results to a reducer, similarly to a "combiner" in MapReduce. Output will be hash-partitioned with the existing partitioner/ parallelism level. 
  90. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#reduceByKey\(func:\(V,V\)=>V,numPartitions:Int\):org.apache.spark.rdd.RDD\[\(K,V\)\] "Permalink") def reduceByKey(func: (V, V) => V, numPartitions: Int): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, V)]
Merge the values for each key using an associative and commutative reduce function.
Merge the values for each key using an associative and commutative reduce function. This will also perform the merging locally on each mapper before sending results to a reducer, similarly to a "combiner" in MapReduce. Output will be hash-partitioned with numPartitions partitions. 
  91. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#reduceByKey\(partitioner:org.apache.spark.Partitioner,func:\(V,V\)=>V\):org.apache.spark.rdd.RDD\[\(K,V\)\] "Permalink") def reduceByKey(partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner"), func: (V, V) => V): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, V)]
Merge the values for each key using an associative and commutative reduce function.
Merge the values for each key using an associative and commutative reduce function. This will also perform the merging locally on each mapper before sending results to a reducer, similarly to a "combiner" in MapReduce. 
  92. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#reduceByKeyLocally\(func:\(V,V\)=>V\):scala.collection.Map\[K,V\] "Permalink") def reduceByKeyLocally(func: (V, V) => V): Map[K, V]
Merge the values for each key using an associative and commutative reduce function, but return the results immediately to the master as a Map.
Merge the values for each key using an associative and commutative reduce function, but return the results immediately to the master as a Map. This will also perform the merging locally on each mapper before sending results to a reducer, similarly to a "combiner" in MapReduce. 
  93. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#rightOuterJoin\[W\]\(other:org.apache.spark.rdd.RDD\[\(K,W\)\],numPartitions:Int\):org.apache.spark.rdd.RDD\[\(K,\(Option\[V\],W\)\)\] "Permalink") def rightOuterJoin[W](other: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, W)], numPartitions: Int): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, (Option[V], W))]
Perform a right outer join of `this` and `other`.
Perform a right outer join of `this` and `other`. For each element (k, w) in `other`, the resulting RDD will either contain all pairs (k, (Some(v), w)) for v in `this`, or the pair (k, (None, w)) if no elements in `this` have key k. Hash-partitions the resulting RDD into the given number of partitions. 
  94. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#rightOuterJoin\[W\]\(other:org.apache.spark.rdd.RDD\[\(K,W\)\]\):org.apache.spark.rdd.RDD\[\(K,\(Option\[V\],W\)\)\] "Permalink") def rightOuterJoin[W](other: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, W)]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, (Option[V], W))]
Perform a right outer join of `this` and `other`.
Perform a right outer join of `this` and `other`. For each element (k, w) in `other`, the resulting RDD will either contain all pairs (k, (Some(v), w)) for v in `this`, or the pair (k, (None, w)) if no elements in `this` have key k. Hash-partitions the resulting RDD using the existing partitioner/parallelism level. 
  95. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#rightOuterJoin\[W\]\(other:org.apache.spark.rdd.RDD\[\(K,W\)\],partitioner:org.apache.spark.Partitioner\):org.apache.spark.rdd.RDD\[\(K,\(Option\[V\],W\)\)\] "Permalink") def rightOuterJoin[W](other: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, W)], partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner")): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, (Option[V], W))]
Perform a right outer join of `this` and `other`.
Perform a right outer join of `this` and `other`. For each element (k, w) in `other`, the resulting RDD will either contain all pairs (k, (Some(v), w)) for v in `this`, or the pair (k, (None, w)) if no elements in `this` have key k. Uses the given Partitioner to partition the output RDD. 
  96. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#sampleByKey\(withReplacement:Boolean,fractions:scala.collection.Map\[K,Double\],seed:Long\):org.apache.spark.rdd.RDD\[\(K,V\)\] "Permalink") def sampleByKey(withReplacement: Boolean, fractions: Map[K, Double], seed: Long = [Utils.random.nextLong](https://spark.apache.org/docs/latest/api/scala/org/index.html)): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, V)]
Return a subset of this RDD sampled by key (via stratified sampling).
Return a subset of this RDD sampled by key (via stratified sampling).
Create a sample of this RDD using variable sampling rates for different keys as specified by `fractions`, a key to sampling rate map, via simple random sampling with one pass over the RDD, to produce a sample of size that's approximately equal to the sum of math.ceil(numItems * samplingRate) over all key values.  

withReplacement
    
whether to sample with or without replacement 

fractions
    
map of specific keys to sampling rates 

seed
    
seed for the random number generator 

returns
    
RDD containing the sampled subset
  97. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#sampleByKeyExact\(withReplacement:Boolean,fractions:scala.collection.Map\[K,Double\],seed:Long\):org.apache.spark.rdd.RDD\[\(K,V\)\] "Permalink") def sampleByKeyExact(withReplacement: Boolean, fractions: Map[K, Double], seed: Long = [Utils.random.nextLong](https://spark.apache.org/docs/latest/api/scala/org/index.html)): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, V)]
Return a subset of this RDD sampled by key (via stratified sampling) containing exactly math.ceil(numItems * samplingRate) for each stratum (group of pairs with the same key).
Return a subset of this RDD sampled by key (via stratified sampling) containing exactly math.ceil(numItems * samplingRate) for each stratum (group of pairs with the same key).
This method differs from [sampleByKey](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#sampleByKey\(withReplacement:Boolean,fractions:scala.collection.Map\[K,Double\],seed:Long\):org.apache.spark.rdd.RDD\[\(K,V\)\]) in that we make additional passes over the RDD to create a sample size that's exactly equal to the sum of math.ceil(numItems * samplingRate) over all key values with a 99.99% confidence. When sampling without replacement, we need one additional pass over the RDD to guarantee sample size; when sampling with replacement, we need two additional passes.  

withReplacement
    
whether to sample with or without replacement 

fractions
    
map of specific keys to sampling rates 

seed
    
seed for the random number generator 

returns
    
RDD containing the sampled subset
  98. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#saveAsHadoopDataset\(conf:org.apache.hadoop.mapred.JobConf\):Unit "Permalink") def saveAsHadoopDataset(conf: JobConf): Unit
Output the RDD to any Hadoop-supported storage system, using a Hadoop JobConf object for that storage system.
Output the RDD to any Hadoop-supported storage system, using a Hadoop JobConf object for that storage system. The JobConf should set an OutputFormat and any output paths required (e.g. a table name to write to) in the same way as it would be configured for a Hadoop MapReduce job. 
  99. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#saveAsHadoopFile\(path:String,keyClass:Class\[_\],valueClass:Class\[_\],outputFormatClass:Class\[_<:org.apache.hadoop.mapred.OutputFormat\[_,_\]\],conf:org.apache.hadoop.mapred.JobConf,codec:Option\[Class\[_<:org.apache.hadoop.io.compress.CompressionCodec\]\]\):Unit "Permalink") def saveAsHadoopFile(path: String, keyClass: Class[_], valueClass: Class[_], outputFormatClass: Class[_ <: OutputFormat[_, _]], conf: JobConf = [new JobConf(self.context.hadoopConfiguration)](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html#context:org.apache.spark.SparkContext), codec: Option[Class[_ <: CompressionCodec]] = None): Unit
Output the RDD to any Hadoop-supported file system, using a Hadoop `OutputFormat` class supporting the key and value types K and V in this RDD.
Output the RDD to any Hadoop-supported file system, using a Hadoop `OutputFormat` class supporting the key and value types K and V in this RDD.  

Note
    
We should make sure our tasks are idempotent when speculation is enabled, i.e. do not use output committer that writes data directly. There is an example in https://issues.apache.org/jira/browse/SPARK-10063 to show the bad result of using direct output committer with speculation enabled.
  100. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#saveAsHadoopFile\(path:String,keyClass:Class\[_\],valueClass:Class\[_\],outputFormatClass:Class\[_<:org.apache.hadoop.mapred.OutputFormat\[_,_\]\],codec:Class\[_<:org.apache.hadoop.io.compress.CompressionCodec\]\):Unit "Permalink") def saveAsHadoopFile(path: String, keyClass: Class[_], valueClass: Class[_], outputFormatClass: Class[_ <: OutputFormat[_, _]], codec: Class[_ <: CompressionCodec]): Unit
Output the RDD to any Hadoop-supported file system, using a Hadoop `OutputFormat` class supporting the key and value types K and V in this RDD.
Output the RDD to any Hadoop-supported file system, using a Hadoop `OutputFormat` class supporting the key and value types K and V in this RDD. Compress with the supplied codec. 
  101. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#saveAsHadoopFile\[F<:org.apache.hadoop.mapred.OutputFormat\[K,V\]\]\(path:String,codec:Class\[_<:org.apache.hadoop.io.compress.CompressionCodec\]\)\(implicitfm:scala.reflect.ClassTag\[F\]\):Unit "Permalink") def saveAsHadoopFile[F <: OutputFormat[K, V]](path: String, codec: Class[_ <: CompressionCodec])(implicit fm: ClassTag[F]): Unit
Output the RDD to any Hadoop-supported file system, using a Hadoop `OutputFormat` class supporting the key and value types K and V in this RDD.
Output the RDD to any Hadoop-supported file system, using a Hadoop `OutputFormat` class supporting the key and value types K and V in this RDD. Compress the result with the supplied codec. 
  102. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#saveAsHadoopFile\[F<:org.apache.hadoop.mapred.OutputFormat\[K,V\]\]\(path:String\)\(implicitfm:scala.reflect.ClassTag\[F\]\):Unit "Permalink") def saveAsHadoopFile[F <: OutputFormat[K, V]](path: String)(implicit fm: ClassTag[F]): Unit
Output the RDD to any Hadoop-supported file system, using a Hadoop `OutputFormat` class supporting the key and value types K and V in this RDD.
  103. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#saveAsNewAPIHadoopDataset\(conf:org.apache.hadoop.conf.Configuration\):Unit "Permalink") def saveAsNewAPIHadoopDataset(conf: Configuration): Unit
Output the RDD to any Hadoop-supported storage system with new Hadoop API, using a Hadoop Configuration object for that storage system.
Output the RDD to any Hadoop-supported storage system with new Hadoop API, using a Hadoop Configuration object for that storage system. The Conf should set an OutputFormat and any output paths required (e.g. a table name to write to) in the same way as it would be configured for a Hadoop MapReduce job.  

Note
    
We should make sure our tasks are idempotent when speculation is enabled, i.e. do not use output committer that writes data directly. There is an example in https://issues.apache.org/jira/browse/SPARK-10063 to show the bad result of using direct output committer with speculation enabled.
  104. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#saveAsNewAPIHadoopFile\(path:String,keyClass:Class\[_\],valueClass:Class\[_\],outputFormatClass:Class\[_<:org.apache.hadoop.mapreduce.OutputFormat\[_,_\]\],conf:org.apache.hadoop.conf.Configuration\):Unit "Permalink") def saveAsNewAPIHadoopFile(path: String, keyClass: Class[_], valueClass: Class[_], outputFormatClass: Class[_ <: OutputFormat[_, _]], conf: Configuration = [self.context.hadoopConfiguration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html#context:org.apache.spark.SparkContext)): Unit
Output the RDD to any Hadoop-supported file system, using a new Hadoop API `OutputFormat` (mapreduce.OutputFormat) object supporting the key and value types K and V in this RDD.
  105. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#saveAsNewAPIHadoopFile\[F<:org.apache.hadoop.mapreduce.OutputFormat\[K,V\]\]\(path:String\)\(implicitfm:scala.reflect.ClassTag\[F\]\):Unit "Permalink") def saveAsNewAPIHadoopFile[F <: OutputFormat[K, V]](path: String)(implicit fm: ClassTag[F]): Unit
Output the RDD to any Hadoop-supported file system, using a new Hadoop API `OutputFormat` (mapreduce.OutputFormat) object supporting the key and value types K and V in this RDD.
  106. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#subtractByKey\[W\]\(other:org.apache.spark.rdd.RDD\[\(K,W\)\],p:org.apache.spark.Partitioner\)\(implicitevidence$6:scala.reflect.ClassTag\[W\]\):org.apache.spark.rdd.RDD\[\(K,V\)\] "Permalink") def subtractByKey[W](other: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, W)], p: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner"))(implicit arg0: ClassTag[W]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, V)]
Return an RDD with the pairs from `this` whose keys are not in `other`.
  107. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#subtractByKey\[W\]\(other:org.apache.spark.rdd.RDD\[\(K,W\)\],numPartitions:Int\)\(implicitevidence$5:scala.reflect.ClassTag\[W\]\):org.apache.spark.rdd.RDD\[\(K,V\)\] "Permalink") def subtractByKey[W](other: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, W)], numPartitions: Int)(implicit arg0: ClassTag[W]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, V)]
Return an RDD with the pairs from `this` whose keys are not in `other`.
  108. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#subtractByKey\[W\]\(other:org.apache.spark.rdd.RDD\[\(K,W\)\]\)\(implicitevidence$4:scala.reflect.ClassTag\[W\]\):org.apache.spark.rdd.RDD\[\(K,V\)\] "Permalink") def subtractByKey[W](other: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, W)])(implicit arg0: ClassTag[W]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, V)]
Return an RDD with the pairs from `this` whose keys are not in `other`.
Return an RDD with the pairs from `this` whose keys are not in `other`.
Uses `this` partitioner/partition size, because even if `other` is huge, the resulting RDD will be less than or equal to us. 
  109. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0 

Definition Classes
    AnyRef
  110. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#toString\(\):String "Permalink") def toString(): [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String") 

Definition Classes
    AnyRef → Any
  111. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#values:org.apache.spark.rdd.RDD\[V\] "Permalink") def values: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[V]
Return an RDD with the values of each tuple.
  112. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  113. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  114. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#wait\(\):Unit "Permalink") final  def wait(): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  115. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#withLogContext\(context:java.util.Map\[String,String\]\)\(body:=>Unit\):Unit "Permalink") def withLogContext(context: [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#java.util.Map "java.util.Map")[String, String])(body: => Unit): Unit 

Attributes
    protected  

Definition Classes
    Logging


### Deprecated Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#finalize\(\):Unit "Permalink") def finalize(): Unit 

Attributes
    protected[lang]  

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.Throwable]) @Deprecated 

Deprecated
    
_(Since version 9)_


### Inherited from Logging
### Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#MDC\(key:org.apache.spark.internal.LogKey,value:Any\):org.apache.spark.internal.MDC "Permalink") def MDC(key: LogKey, value: Any): MDC 

Attributes
    protected  

Definition Classes
    Logging
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#initializeLogIfNecessary\(isInterpreter:Boolean,silent:Boolean\):Boolean "Permalink") def initializeLogIfNecessary(isInterpreter: Boolean, silent: Boolean): Boolean 

Attributes
    protected  

Definition Classes
    Logging
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#initializeLogIfNecessary\(isInterpreter:Boolean\):Unit "Permalink") def initializeLogIfNecessary(isInterpreter: Boolean): Unit 

Attributes
    protected  

Definition Classes
    Logging
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#isTraceEnabled\(\):Boolean "Permalink") def isTraceEnabled(): Boolean 

Attributes
    protected  

Definition Classes
    Logging
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#log:org.slf4j.Logger "Permalink") def log: Logger 

Attributes
    protected  

Definition Classes
    Logging
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#logBasedOnLevel\(level:org.slf4j.event.Level\)\(f:=>org.apache.spark.internal.MessageWithContext\):Unit "Permalink") def logBasedOnLevel(level: Level)(f: => MessageWithContext): Unit 

Attributes
    protected  

Definition Classes
    Logging
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#logDebug\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logDebug(msg: => String, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#logDebug\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logDebug(entry: LogEntry, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#logDebug\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logDebug(entry: LogEntry): Unit 

Attributes
    protected  

Definition Classes
    Logging
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#logDebug\(msg:=>String\):Unit "Permalink") def logDebug(msg: => String): Unit 

Attributes
    protected  

Definition Classes
    Logging
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#logError\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logError(msg: => String, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#logError\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logError(entry: LogEntry, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#logError\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logError(entry: LogEntry): Unit 

Attributes
    protected  

Definition Classes
    Logging
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#logError\(msg:=>String\):Unit "Permalink") def logError(msg: => String): Unit 

Attributes
    protected  

Definition Classes
    Logging
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#logInfo\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logInfo(msg: => String, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#logInfo\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logInfo(entry: LogEntry, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#logInfo\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logInfo(entry: LogEntry): Unit 

Attributes
    protected  

Definition Classes
    Logging
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#logInfo\(msg:=>String\):Unit "Permalink") def logInfo(msg: => String): Unit 

Attributes
    protected  

Definition Classes
    Logging
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#logName:String "Permalink") def logName: [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String") 

Attributes
    protected  

Definition Classes
    Logging
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#logTrace\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logTrace(msg: => String, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#logTrace\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logTrace(entry: LogEntry, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#logTrace\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logTrace(entry: LogEntry): Unit 

Attributes
    protected  

Definition Classes
    Logging
  23. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#logTrace\(msg:=>String\):Unit "Permalink") def logTrace(msg: => String): Unit 

Attributes
    protected  

Definition Classes
    Logging
  24. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#logWarning\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logWarning(msg: => String, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  25. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#logWarning\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logWarning(entry: LogEntry, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  26. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#logWarning\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logWarning(entry: LogEntry): Unit 

Attributes
    protected  

Definition Classes
    Logging
  27. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#logWarning\(msg:=>String\):Unit "Permalink") def logWarning(msg: => String): Unit 

Attributes
    protected  

Definition Classes
    Logging
  28. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#withLogContext\(context:java.util.Map\[String,String\]\)\(body:=>Unit\):Unit "Permalink") def withLogContext(context: [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#java.util.Map "java.util.Map")[String, String])(body: => Unit): Unit 

Attributes
    protected  

Definition Classes
    Logging


### Inherited from AnyRef
### Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html###:Int "Permalink") final  def ##: Int 

Definition Classes
    AnyRef → Any
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#clone\(\):Object "Permalink") def clone(): AnyRef 

Attributes
    protected[lang]  

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#equals\(x$1:Object\):Boolean "Permalink") def equals(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef → Any
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef] 

Definition Classes
    AnyRef → Any 

Annotations
     @IntrinsicCandidate() @native()
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#hashCode\(\):Int "Permalink") def hashCode(): Int 

Definition Classes
    AnyRef → Any 

Annotations
     @IntrinsicCandidate() @native()
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#notify\(\):Unit "Permalink") final  def notify(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0 

Definition Classes
    AnyRef
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#toString\(\):String "Permalink") def toString(): [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String") 

Definition Classes
    AnyRef → Any
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#wait\(\):Unit "Permalink") final  def wait(): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#finalize\(\):Unit "Permalink") def finalize(): Unit 

Attributes
    protected[lang]  

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.Throwable]) @Deprecated 

Deprecated
    
_(Since version 9)_


### Inherited from Any
### Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0 

Definition Classes
    Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean 

Definition Classes
    Any


### Ungrouped
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#LogStringContextextendsAnyRef "Permalink") implicit  class LogStringContext extends AnyRef 

Definition Classes
    Logging


  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html###:Int "Permalink") final  def ##: Int 

Definition Classes
    AnyRef → Any
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#MDC\(key:org.apache.spark.internal.LogKey,value:Any\):org.apache.spark.internal.MDC "Permalink") def MDC(key: LogKey, value: Any): MDC 

Attributes
    protected  

Definition Classes
    Logging
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#aggregateByKey\[U\]\(zeroValue:U\)\(seqOp:\(U,V\)=>U,combOp:\(U,U\)=>U\)\(implicitevidence$3:scala.reflect.ClassTag\[U\]\):org.apache.spark.rdd.RDD\[\(K,U\)\] "Permalink") def aggregateByKey[U](zeroValue: U)(seqOp: (U, V) => U, combOp: (U, U) => U)(implicit arg0: ClassTag[U]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, U)]
Aggregate the values of each key, using given combine functions and a neutral "zero value".
Aggregate the values of each key, using given combine functions and a neutral "zero value". This function can return a different result type, U, than the type of the values in this RDD, V. Thus, we need one operation for merging a V into a U and one operation for merging two U's, as in scala.IterableOnce. The former operation is used for merging values within a partition, and the latter is used for merging values between partitions. To avoid memory allocation, both of these functions are allowed to modify and return their first argument instead of creating a new U. 
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#aggregateByKey\[U\]\(zeroValue:U,numPartitions:Int\)\(seqOp:\(U,V\)=>U,combOp:\(U,U\)=>U\)\(implicitevidence$2:scala.reflect.ClassTag\[U\]\):org.apache.spark.rdd.RDD\[\(K,U\)\] "Permalink") def aggregateByKey[U](zeroValue: U, numPartitions: Int)(seqOp: (U, V) => U, combOp: (U, U) => U)(implicit arg0: ClassTag[U]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, U)]
Aggregate the values of each key, using given combine functions and a neutral "zero value".
Aggregate the values of each key, using given combine functions and a neutral "zero value". This function can return a different result type, U, than the type of the values in this RDD, V. Thus, we need one operation for merging a V into a U and one operation for merging two U's, as in scala.IterableOnce. The former operation is used for merging values within a partition, and the latter is used for merging values between partitions. To avoid memory allocation, both of these functions are allowed to modify and return their first argument instead of creating a new U. 
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#aggregateByKey\[U\]\(zeroValue:U,partitioner:org.apache.spark.Partitioner\)\(seqOp:\(U,V\)=>U,combOp:\(U,U\)=>U\)\(implicitevidence$1:scala.reflect.ClassTag\[U\]\):org.apache.spark.rdd.RDD\[\(K,U\)\] "Permalink") def aggregateByKey[U](zeroValue: U, partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner"))(seqOp: (U, V) => U, combOp: (U, U) => U)(implicit arg0: ClassTag[U]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, U)]
Aggregate the values of each key, using given combine functions and a neutral "zero value".
Aggregate the values of each key, using given combine functions and a neutral "zero value". This function can return a different result type, U, than the type of the values in this RDD, V. Thus, we need one operation for merging a V into a U and one operation for merging two U's, as in scala.IterableOnce. The former operation is used for merging values within a partition, and the latter is used for merging values between partitions. To avoid memory allocation, both of these functions are allowed to modify and return their first argument instead of creating a new U. 
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0 

Definition Classes
    Any
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#clone\(\):Object "Permalink") def clone(): AnyRef 

Attributes
    protected[lang]  

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#cogroup\[W1,W2,W3\]\(other1:org.apache.spark.rdd.RDD\[\(K,W1\)\],other2:org.apache.spark.rdd.RDD\[\(K,W2\)\],other3:org.apache.spark.rdd.RDD\[\(K,W3\)\],numPartitions:Int\):org.apache.spark.rdd.RDD\[\(K,\(Iterable\[V\],Iterable\[W1\],Iterable\[W2\],Iterable\[W3\]\)\)\] "Permalink") def cogroup[W1, W2, W3](other1: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, W1)], other2: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, W2)], other3: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, W3)], numPartitions: Int): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, (Iterable[V], Iterable[W1], Iterable[W2], Iterable[W3]))]
For each key k in `this` or `other1` or `other2` or `other3`, return a resulting RDD that contains a tuple with the list of values for that key in `this`, `other1`, `other2` and `other3`.
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#cogroup\[W1,W2\]\(other1:org.apache.spark.rdd.RDD\[\(K,W1\)\],other2:org.apache.spark.rdd.RDD\[\(K,W2\)\],numPartitions:Int\):org.apache.spark.rdd.RDD\[\(K,\(Iterable\[V\],Iterable\[W1\],Iterable\[W2\]\)\)\] "Permalink") def cogroup[W1, W2](other1: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, W1)], other2: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, W2)], numPartitions: Int): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, (Iterable[V], Iterable[W1], Iterable[W2]))]
For each key k in `this` or `other1` or `other2`, return a resulting RDD that contains a tuple with the list of values for that key in `this`, `other1` and `other2`.
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#cogroup\[W\]\(other:org.apache.spark.rdd.RDD\[\(K,W\)\],numPartitions:Int\):org.apache.spark.rdd.RDD\[\(K,\(Iterable\[V\],Iterable\[W\]\)\)\] "Permalink") def cogroup[W](other: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, W)], numPartitions: Int): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, (Iterable[V], Iterable[W]))]
For each key k in `this` or `other`, return a resulting RDD that contains a tuple with the list of values for that key in `this` as well as `other`.
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#cogroup\[W1,W2\]\(other1:org.apache.spark.rdd.RDD\[\(K,W1\)\],other2:org.apache.spark.rdd.RDD\[\(K,W2\)\]\):org.apache.spark.rdd.RDD\[\(K,\(Iterable\[V\],Iterable\[W1\],Iterable\[W2\]\)\)\] "Permalink") def cogroup[W1, W2](other1: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, W1)], other2: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, W2)]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, (Iterable[V], Iterable[W1], Iterable[W2]))]
For each key k in `this` or `other1` or `other2`, return a resulting RDD that contains a tuple with the list of values for that key in `this`, `other1` and `other2`.
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#cogroup\[W\]\(other:org.apache.spark.rdd.RDD\[\(K,W\)\]\):org.apache.spark.rdd.RDD\[\(K,\(Iterable\[V\],Iterable\[W\]\)\)\] "Permalink") def cogroup[W](other: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, W)]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, (Iterable[V], Iterable[W]))]
For each key k in `this` or `other`, return a resulting RDD that contains a tuple with the list of values for that key in `this` as well as `other`.
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#cogroup\[W1,W2,W3\]\(other1:org.apache.spark.rdd.RDD\[\(K,W1\)\],other2:org.apache.spark.rdd.RDD\[\(K,W2\)\],other3:org.apache.spark.rdd.RDD\[\(K,W3\)\]\):org.apache.spark.rdd.RDD\[\(K,\(Iterable\[V\],Iterable\[W1\],Iterable\[W2\],Iterable\[W3\]\)\)\] "Permalink") def cogroup[W1, W2, W3](other1: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, W1)], other2: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, W2)], other3: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, W3)]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, (Iterable[V], Iterable[W1], Iterable[W2], Iterable[W3]))]
For each key k in `this` or `other1` or `other2` or `other3`, return a resulting RDD that contains a tuple with the list of values for that key in `this`, `other1`, `other2` and `other3`.
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#cogroup\[W1,W2\]\(other1:org.apache.spark.rdd.RDD\[\(K,W1\)\],other2:org.apache.spark.rdd.RDD\[\(K,W2\)\],partitioner:org.apache.spark.Partitioner\):org.apache.spark.rdd.RDD\[\(K,\(Iterable\[V\],Iterable\[W1\],Iterable\[W2\]\)\)\] "Permalink") def cogroup[W1, W2](other1: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, W1)], other2: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, W2)], partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner")): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, (Iterable[V], Iterable[W1], Iterable[W2]))]
For each key k in `this` or `other1` or `other2`, return a resulting RDD that contains a tuple with the list of values for that key in `this`, `other1` and `other2`.
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#cogroup\[W\]\(other:org.apache.spark.rdd.RDD\[\(K,W\)\],partitioner:org.apache.spark.Partitioner\):org.apache.spark.rdd.RDD\[\(K,\(Iterable\[V\],Iterable\[W\]\)\)\] "Permalink") def cogroup[W](other: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, W)], partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner")): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, (Iterable[V], Iterable[W]))]
For each key k in `this` or `other`, return a resulting RDD that contains a tuple with the list of values for that key in `this` as well as `other`.
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#cogroup\[W1,W2,W3\]\(other1:org.apache.spark.rdd.RDD\[\(K,W1\)\],other2:org.apache.spark.rdd.RDD\[\(K,W2\)\],other3:org.apache.spark.rdd.RDD\[\(K,W3\)\],partitioner:org.apache.spark.Partitioner\):org.apache.spark.rdd.RDD\[\(K,\(Iterable\[V\],Iterable\[W1\],Iterable\[W2\],Iterable\[W3\]\)\)\] "Permalink") def cogroup[W1, W2, W3](other1: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, W1)], other2: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, W2)], other3: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, W3)], partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner")): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, (Iterable[V], Iterable[W1], Iterable[W2], Iterable[W3]))]
For each key k in `this` or `other1` or `other2` or `other3`, return a resulting RDD that contains a tuple with the list of values for that key in `this`, `other1`, `other2` and `other3`.
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#collectAsMap\(\):scala.collection.Map\[K,V\] "Permalink") def collectAsMap(): Map[K, V]
Return the key-value pairs in this RDD to the master as a Map.
Return the key-value pairs in this RDD to the master as a Map.
Warning: this doesn't return a multimap (so if you have multiple values to the same key, only one value per key is preserved in the map returned)  

Note
    
this method should only be used if the resulting data is expected to be small, as all the data is loaded into the driver's memory.
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#combineByKey\[C\]\(createCombiner:V=>C,mergeValue:\(C,V\)=>C,mergeCombiners:\(C,C\)=>C\):org.apache.spark.rdd.RDD\[\(K,C\)\] "Permalink") def combineByKey[C](createCombiner: (V) => C, mergeValue: (C, V) => C, mergeCombiners: (C, C) => C): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, C)]
Simplified version of combineByKeyWithClassTag that hash-partitions the resulting RDD using the existing partitioner/parallelism level.
Simplified version of combineByKeyWithClassTag that hash-partitions the resulting RDD using the existing partitioner/parallelism level. This method is here for backward compatibility. It does not provide combiner classtag information to the shuffle.  

See also
    
`combineByKeyWithClassTag`
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#combineByKey\[C\]\(createCombiner:V=>C,mergeValue:\(C,V\)=>C,mergeCombiners:\(C,C\)=>C,numPartitions:Int\):org.apache.spark.rdd.RDD\[\(K,C\)\] "Permalink") def combineByKey[C](createCombiner: (V) => C, mergeValue: (C, V) => C, mergeCombiners: (C, C) => C, numPartitions: Int): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, C)]
Simplified version of combineByKeyWithClassTag that hash-partitions the output RDD.
Simplified version of combineByKeyWithClassTag that hash-partitions the output RDD. This method is here for backward compatibility. It does not provide combiner classtag information to the shuffle.  

See also
    
`combineByKeyWithClassTag`
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#combineByKey\[C\]\(createCombiner:V=>C,mergeValue:\(C,V\)=>C,mergeCombiners:\(C,C\)=>C,partitioner:org.apache.spark.Partitioner,mapSideCombine:Boolean,serializer:org.apache.spark.serializer.Serializer\):org.apache.spark.rdd.RDD\[\(K,C\)\] "Permalink") def combineByKey[C](createCombiner: (V) => C, mergeValue: (C, V) => C, mergeCombiners: (C, C) => C, partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner"), mapSideCombine: Boolean = true, serializer: [Serializer](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/Serializer.html "org.apache.spark.serializer.Serializer") = null): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, C)]
Generic function to combine the elements for each key using a custom set of aggregation functions.
Generic function to combine the elements for each key using a custom set of aggregation functions. This method is here for backward compatibility. It does not provide combiner classtag information to the shuffle.  

See also
    
`combineByKeyWithClassTag`
  23. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#combineByKeyWithClassTag\[C\]\(createCombiner:V=>C,mergeValue:\(C,V\)=>C,mergeCombiners:\(C,C\)=>C\)\(implicitct:scala.reflect.ClassTag\[C\]\):org.apache.spark.rdd.RDD\[\(K,C\)\] "Permalink") def combineByKeyWithClassTag[C](createCombiner: (V) => C, mergeValue: (C, V) => C, mergeCombiners: (C, C) => C)(implicit ct: ClassTag[C]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, C)]
Simplified version of combineByKeyWithClassTag that hash-partitions the resulting RDD using the existing partitioner/parallelism level.
  24. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#combineByKeyWithClassTag\[C\]\(createCombiner:V=>C,mergeValue:\(C,V\)=>C,mergeCombiners:\(C,C\)=>C,numPartitions:Int\)\(implicitct:scala.reflect.ClassTag\[C\]\):org.apache.spark.rdd.RDD\[\(K,C\)\] "Permalink") def combineByKeyWithClassTag[C](createCombiner: (V) => C, mergeValue: (C, V) => C, mergeCombiners: (C, C) => C, numPartitions: Int)(implicit ct: ClassTag[C]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, C)]
Simplified version of combineByKeyWithClassTag that hash-partitions the output RDD.
  25. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#combineByKeyWithClassTag\[C\]\(createCombiner:V=>C,mergeValue:\(C,V\)=>C,mergeCombiners:\(C,C\)=>C,partitioner:org.apache.spark.Partitioner,mapSideCombine:Boolean,serializer:org.apache.spark.serializer.Serializer\)\(implicitct:scala.reflect.ClassTag\[C\]\):org.apache.spark.rdd.RDD\[\(K,C\)\] "Permalink") def combineByKeyWithClassTag[C](createCombiner: (V) => C, mergeValue: (C, V) => C, mergeCombiners: (C, C) => C, partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner"), mapSideCombine: Boolean = true, serializer: [Serializer](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/Serializer.html "org.apache.spark.serializer.Serializer") = null)(implicit ct: ClassTag[C]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, C)]
Generic function to combine the elements for each key using a custom set of aggregation functions.
Generic function to combine the elements for each key using a custom set of aggregation functions. Turns an RDD[(K, V)] into a result of type RDD[(K, C)], for a "combined type" C
Users provide three functions:
     * `createCombiner`, which turns a V into a C (e.g., creates a one-element list)
     * `mergeValue`, to merge a V into a C (e.g., adds it to the end of a list)
     * `mergeCombiners`, to combine two C's into a single one.
In addition, users can control the partitioning of the output RDD, and whether to perform map-side aggregation (if a mapper can produce multiple items with the same key).  

Note
    
V and C can be different -- for example, one might group an RDD of type (Int, Int) into an RDD of type (Int, Seq[Int]).
  26. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#countApproxDistinctByKey\(relativeSD:Double\):org.apache.spark.rdd.RDD\[\(K,Long\)\] "Permalink") def countApproxDistinctByKey(relativeSD: Double = 0.05): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, Long)]
Return approximate number of distinct values for each key in this RDD.
Return approximate number of distinct values for each key in this RDD.
The algorithm used is based on streamlib's implementation of "HyperLogLog in Practice: Algorithmic Engineering of a State of The Art Cardinality Estimation Algorithm", available [here](https://doi.org/10.1145/2452376.2452456).  

relativeSD
    
Relative accuracy. Smaller values create counters that require more space. It must be greater than 0.000017.
  27. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#countApproxDistinctByKey\(relativeSD:Double,numPartitions:Int\):org.apache.spark.rdd.RDD\[\(K,Long\)\] "Permalink") def countApproxDistinctByKey(relativeSD: Double, numPartitions: Int): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, Long)]
Return approximate number of distinct values for each key in this RDD.
Return approximate number of distinct values for each key in this RDD.
The algorithm used is based on streamlib's implementation of "HyperLogLog in Practice: Algorithmic Engineering of a State of The Art Cardinality Estimation Algorithm", available [here](https://doi.org/10.1145/2452376.2452456).  

relativeSD
    
Relative accuracy. Smaller values create counters that require more space. It must be greater than 0.000017. 

numPartitions
    
number of partitions of the resulting RDD
  28. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#countApproxDistinctByKey\(relativeSD:Double,partitioner:org.apache.spark.Partitioner\):org.apache.spark.rdd.RDD\[\(K,Long\)\] "Permalink") def countApproxDistinctByKey(relativeSD: Double, partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner")): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, Long)]
Return approximate number of distinct values for each key in this RDD.
Return approximate number of distinct values for each key in this RDD.
The algorithm used is based on streamlib's implementation of "HyperLogLog in Practice: Algorithmic Engineering of a State of The Art Cardinality Estimation Algorithm", available [here](https://doi.org/10.1145/2452376.2452456).  

relativeSD
    
Relative accuracy. Smaller values create counters that require more space. It must be greater than 0.000017. 

partitioner
    
partitioner of the resulting RDD
  29. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#countApproxDistinctByKey\(p:Int,sp:Int,partitioner:org.apache.spark.Partitioner\):org.apache.spark.rdd.RDD\[\(K,Long\)\] "Permalink") def countApproxDistinctByKey(p: Int, sp: Int, partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner")): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, Long)]
Return approximate number of distinct values for each key in this RDD.
Return approximate number of distinct values for each key in this RDD.
The algorithm used is based on streamlib's implementation of "HyperLogLog in Practice: Algorithmic Engineering of a State of The Art Cardinality Estimation Algorithm", available [here](https://doi.org/10.1145/2452376.2452456).
The relative accuracy is approximately `1.054 / sqrt(2^p)`. Setting a nonzero (`sp` is greater than `p`) would trigger sparse representation of registers, which may reduce the memory consumption and increase accuracy when the cardinality is small. `` 

p
    
The precision value for the normal set. `p` must be a value between 4 and `sp` if `sp` is not zero (32 max). 

sp
    
The precision value for the sparse set, between 0 and 32. If `sp` equals 0, the sparse representation is skipped. 

partitioner
    
Partitioner to use for the resulting RDD.
  30. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#countByKey\(\):scala.collection.Map\[K,Long\] "Permalink") def countByKey(): Map[K, Long]
Count the number of elements for each key, collecting the results to a local Map.
Count the number of elements for each key, collecting the results to a local Map.  

Note
    
This method should only be used if the resulting map is expected to be small, as the whole thing is loaded into the driver's memory. To handle very large results, consider using rdd.mapValues(_ => 1L).reduceByKey(_ + _), which returns an RDD[T, Long] instead of a map.
  31. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#countByKeyApprox\(timeout:Long,confidence:Double\):org.apache.spark.partial.PartialResult\[scala.collection.Map\[K,org.apache.spark.partial.BoundedDouble\]\] "Permalink") def countByKeyApprox(timeout: Long, confidence: Double = 0.95): [PartialResult](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/partial/PartialResult.html "org.apache.spark.partial.PartialResult")[Map[K, [BoundedDouble](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/partial/BoundedDouble.html "org.apache.spark.partial.BoundedDouble")]]
Approximate version of countByKey that can return a partial result if it does not finish within a timeout.
Approximate version of countByKey that can return a partial result if it does not finish within a timeout.
The confidence is the probability that the error bounds of the result will contain the true value. That is, if countApprox were called repeatedly with confidence 0.9, we would expect 90% of the results to contain the true count. The confidence must be in the range [0,1] or an exception will be thrown.  

timeout
    
maximum time to wait for the job, in milliseconds 

confidence
    
the desired statistical confidence in the result 

returns
    
a potentially incomplete result, with error bounds
  32. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  33. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#equals\(x$1:Object\):Boolean "Permalink") def equals(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef → Any
  34. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#flatMapValues\[U\]\(f:V=>IterableOnce\[U\]\):org.apache.spark.rdd.RDD\[\(K,U\)\] "Permalink") def flatMapValues[U](f: (V) => IterableOnce[U]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, U)]
Pass each value in the key-value pair RDD through a flatMap function without changing the keys; this also retains the original RDD's partitioning.
  35. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#foldByKey\(zeroValue:V\)\(func:\(V,V\)=>V\):org.apache.spark.rdd.RDD\[\(K,V\)\] "Permalink") def foldByKey(zeroValue: V)(func: (V, V) => V): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, V)]
Merge the values for each key using an associative function and a neutral "zero value" which may be added to the result an arbitrary number of times, and must not change the result (e.g., Nil for list concatenation, 0 for addition, or 1 for multiplication.).
  36. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#foldByKey\(zeroValue:V,numPartitions:Int\)\(func:\(V,V\)=>V\):org.apache.spark.rdd.RDD\[\(K,V\)\] "Permalink") def foldByKey(zeroValue: V, numPartitions: Int)(func: (V, V) => V): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, V)]
Merge the values for each key using an associative function and a neutral "zero value" which may be added to the result an arbitrary number of times, and must not change the result (e.g., Nil for list concatenation, 0 for addition, or 1 for multiplication.).
  37. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#foldByKey\(zeroValue:V,partitioner:org.apache.spark.Partitioner\)\(func:\(V,V\)=>V\):org.apache.spark.rdd.RDD\[\(K,V\)\] "Permalink") def foldByKey(zeroValue: V, partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner"))(func: (V, V) => V): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, V)]
Merge the values for each key using an associative function and a neutral "zero value" which may be added to the result an arbitrary number of times, and must not change the result (e.g., Nil for list concatenation, 0 for addition, or 1 for multiplication.).
  38. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#fullOuterJoin\[W\]\(other:org.apache.spark.rdd.RDD\[\(K,W\)\],numPartitions:Int\):org.apache.spark.rdd.RDD\[\(K,\(Option\[V\],Option\[W\]\)\)\] "Permalink") def fullOuterJoin[W](other: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, W)], numPartitions: Int): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, (Option[V], Option[W]))]
Perform a full outer join of `this` and `other`.
Perform a full outer join of `this` and `other`. For each element (k, v) in `this`, the resulting RDD will either contain all pairs (k, (Some(v), Some(w))) for w in `other`, or the pair (k, (Some(v), None)) if no elements in `other` have key k. Similarly, for each element (k, w) in `other`, the resulting RDD will either contain all pairs (k, (Some(v), Some(w))) for v in `this`, or the pair (k, (None, Some(w))) if no elements in `this` have key k. Hash-partitions the resulting RDD into the given number of partitions. 
  39. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#fullOuterJoin\[W\]\(other:org.apache.spark.rdd.RDD\[\(K,W\)\]\):org.apache.spark.rdd.RDD\[\(K,\(Option\[V\],Option\[W\]\)\)\] "Permalink") def fullOuterJoin[W](other: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, W)]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, (Option[V], Option[W]))]
Perform a full outer join of `this` and `other`.
Perform a full outer join of `this` and `other`. For each element (k, v) in `this`, the resulting RDD will either contain all pairs (k, (Some(v), Some(w))) for w in `other`, or the pair (k, (Some(v), None)) if no elements in `other` have key k. Similarly, for each element (k, w) in `other`, the resulting RDD will either contain all pairs (k, (Some(v), Some(w))) for v in `this`, or the pair (k, (None, Some(w))) if no elements in `this` have key k. Hash-partitions the resulting RDD using the existing partitioner/ parallelism level. 
  40. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#fullOuterJoin\[W\]\(other:org.apache.spark.rdd.RDD\[\(K,W\)\],partitioner:org.apache.spark.Partitioner\):org.apache.spark.rdd.RDD\[\(K,\(Option\[V\],Option\[W\]\)\)\] "Permalink") def fullOuterJoin[W](other: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, W)], partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner")): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, (Option[V], Option[W]))]
Perform a full outer join of `this` and `other`.
Perform a full outer join of `this` and `other`. For each element (k, v) in `this`, the resulting RDD will either contain all pairs (k, (Some(v), Some(w))) for w in `other`, or the pair (k, (Some(v), None)) if no elements in `other` have key k. Similarly, for each element (k, w) in `other`, the resulting RDD will either contain all pairs (k, (Some(v), Some(w))) for v in `this`, or the pair (k, (None, Some(w))) if no elements in `this` have key k. Uses the given Partitioner to partition the output RDD. 
  41. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef] 

Definition Classes
    AnyRef → Any 

Annotations
     @IntrinsicCandidate() @native()
  42. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#groupByKey\(\):org.apache.spark.rdd.RDD\[\(K,Iterable\[V\]\)\] "Permalink") def groupByKey(): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, Iterable[V])]
Group the values for each key in the RDD into a single sequence.
Group the values for each key in the RDD into a single sequence. Hash-partitions the resulting RDD with the existing partitioner/parallelism level. The ordering of elements within each group is not guaranteed, and may even differ each time the resulting RDD is evaluated.  

Note
    
This operation may be very expensive. If you are grouping in order to perform an aggregation (such as a sum or average) over each key, using `PairRDDFunctions.aggregateByKey` or `PairRDDFunctions.reduceByKey` will provide much better performance.
  43. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#groupByKey\(numPartitions:Int\):org.apache.spark.rdd.RDD\[\(K,Iterable\[V\]\)\] "Permalink") def groupByKey(numPartitions: Int): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, Iterable[V])]
Group the values for each key in the RDD into a single sequence.
Group the values for each key in the RDD into a single sequence. Hash-partitions the resulting RDD with into `numPartitions` partitions. The ordering of elements within each group is not guaranteed, and may even differ each time the resulting RDD is evaluated.  

Note
    
This operation may be very expensive. If you are grouping in order to perform an aggregation (such as a sum or average) over each key, using `PairRDDFunctions.aggregateByKey` or `PairRDDFunctions.reduceByKey` will provide much better performance.
, 
As currently implemented, groupByKey must be able to hold all the key-value pairs for any key in memory. If a key has too many values, it can result in an `OutOfMemoryError`.
  44. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#groupByKey\(partitioner:org.apache.spark.Partitioner\):org.apache.spark.rdd.RDD\[\(K,Iterable\[V\]\)\] "Permalink") def groupByKey(partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner")): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, Iterable[V])]
Group the values for each key in the RDD into a single sequence.
Group the values for each key in the RDD into a single sequence. Allows controlling the partitioning of the resulting key-value pair RDD by passing a Partitioner. The ordering of elements within each group is not guaranteed, and may even differ each time the resulting RDD is evaluated.  

Note
    
This operation may be very expensive. If you are grouping in order to perform an aggregation (such as a sum or average) over each key, using `PairRDDFunctions.aggregateByKey` or `PairRDDFunctions.reduceByKey` will provide much better performance.
, 
As currently implemented, groupByKey must be able to hold all the key-value pairs for any key in memory. If a key has too many values, it can result in an `OutOfMemoryError`.
  45. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#groupWith\[W1,W2,W3\]\(other1:org.apache.spark.rdd.RDD\[\(K,W1\)\],other2:org.apache.spark.rdd.RDD\[\(K,W2\)\],other3:org.apache.spark.rdd.RDD\[\(K,W3\)\]\):org.apache.spark.rdd.RDD\[\(K,\(Iterable\[V\],Iterable\[W1\],Iterable\[W2\],Iterable\[W3\]\)\)\] "Permalink") def groupWith[W1, W2, W3](other1: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, W1)], other2: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, W2)], other3: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, W3)]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, (Iterable[V], Iterable[W1], Iterable[W2], Iterable[W3]))]
Alias for cogroup.
  46. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#groupWith\[W1,W2\]\(other1:org.apache.spark.rdd.RDD\[\(K,W1\)\],other2:org.apache.spark.rdd.RDD\[\(K,W2\)\]\):org.apache.spark.rdd.RDD\[\(K,\(Iterable\[V\],Iterable\[W1\],Iterable\[W2\]\)\)\] "Permalink") def groupWith[W1, W2](other1: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, W1)], other2: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, W2)]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, (Iterable[V], Iterable[W1], Iterable[W2]))]
Alias for cogroup.
  47. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#groupWith\[W\]\(other:org.apache.spark.rdd.RDD\[\(K,W\)\]\):org.apache.spark.rdd.RDD\[\(K,\(Iterable\[V\],Iterable\[W\]\)\)\] "Permalink") def groupWith[W](other: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, W)]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, (Iterable[V], Iterable[W]))]
Alias for cogroup.
  48. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#hashCode\(\):Int "Permalink") def hashCode(): Int 

Definition Classes
    AnyRef → Any 

Annotations
     @IntrinsicCandidate() @native()
  49. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#initializeLogIfNecessary\(isInterpreter:Boolean,silent:Boolean\):Boolean "Permalink") def initializeLogIfNecessary(isInterpreter: Boolean, silent: Boolean): Boolean 

Attributes
    protected  

Definition Classes
    Logging
  50. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#initializeLogIfNecessary\(isInterpreter:Boolean\):Unit "Permalink") def initializeLogIfNecessary(isInterpreter: Boolean): Unit 

Attributes
    protected  

Definition Classes
    Logging
  51. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean 

Definition Classes
    Any
  52. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#isTraceEnabled\(\):Boolean "Permalink") def isTraceEnabled(): Boolean 

Attributes
    protected  

Definition Classes
    Logging
  53. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#join\[W\]\(other:org.apache.spark.rdd.RDD\[\(K,W\)\],numPartitions:Int\):org.apache.spark.rdd.RDD\[\(K,\(V,W\)\)\] "Permalink") def join[W](other: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, W)], numPartitions: Int): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, (V, W))]
Return an RDD containing all pairs of elements with matching keys in `this` and `other`.
Return an RDD containing all pairs of elements with matching keys in `this` and `other`. Each pair of elements will be returned as a (k, (v1, v2)) tuple, where (k, v1) is in `this` and (k, v2) is in `other`. Performs a hash join across the cluster. 
  54. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#join\[W\]\(other:org.apache.spark.rdd.RDD\[\(K,W\)\]\):org.apache.spark.rdd.RDD\[\(K,\(V,W\)\)\] "Permalink") def join[W](other: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, W)]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, (V, W))]
Return an RDD containing all pairs of elements with matching keys in `this` and `other`.
Return an RDD containing all pairs of elements with matching keys in `this` and `other`. Each pair of elements will be returned as a (k, (v1, v2)) tuple, where (k, v1) is in `this` and (k, v2) is in `other`. Performs a hash join across the cluster. 
  55. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#join\[W\]\(other:org.apache.spark.rdd.RDD\[\(K,W\)\],partitioner:org.apache.spark.Partitioner\):org.apache.spark.rdd.RDD\[\(K,\(V,W\)\)\] "Permalink") def join[W](other: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, W)], partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner")): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, (V, W))]
Return an RDD containing all pairs of elements with matching keys in `this` and `other`.
Return an RDD containing all pairs of elements with matching keys in `this` and `other`. Each pair of elements will be returned as a (k, (v1, v2)) tuple, where (k, v1) is in `this` and (k, v2) is in `other`. Uses the given Partitioner to partition the output RDD. 
  56. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#keys:org.apache.spark.rdd.RDD\[K\] "Permalink") def keys: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[K]
Return an RDD with the keys of each tuple.
  57. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#leftOuterJoin\[W\]\(other:org.apache.spark.rdd.RDD\[\(K,W\)\],numPartitions:Int\):org.apache.spark.rdd.RDD\[\(K,\(V,Option\[W\]\)\)\] "Permalink") def leftOuterJoin[W](other: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, W)], numPartitions: Int): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, (V, Option[W]))]
Perform a left outer join of `this` and `other`.
Perform a left outer join of `this` and `other`. For each element (k, v) in `this`, the resulting RDD will either contain all pairs (k, (v, Some(w))) for w in `other`, or the pair (k, (v, None)) if no elements in `other` have key k. Hash-partitions the output into `numPartitions` partitions. 
  58. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#leftOuterJoin\[W\]\(other:org.apache.spark.rdd.RDD\[\(K,W\)\]\):org.apache.spark.rdd.RDD\[\(K,\(V,Option\[W\]\)\)\] "Permalink") def leftOuterJoin[W](other: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, W)]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, (V, Option[W]))]
Perform a left outer join of `this` and `other`.
Perform a left outer join of `this` and `other`. For each element (k, v) in `this`, the resulting RDD will either contain all pairs (k, (v, Some(w))) for w in `other`, or the pair (k, (v, None)) if no elements in `other` have key k. Hash-partitions the output using the existing partitioner/parallelism level. 
  59. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#leftOuterJoin\[W\]\(other:org.apache.spark.rdd.RDD\[\(K,W\)\],partitioner:org.apache.spark.Partitioner\):org.apache.spark.rdd.RDD\[\(K,\(V,Option\[W\]\)\)\] "Permalink") def leftOuterJoin[W](other: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, W)], partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner")): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, (V, Option[W]))]
Perform a left outer join of `this` and `other`.
Perform a left outer join of `this` and `other`. For each element (k, v) in `this`, the resulting RDD will either contain all pairs (k, (v, Some(w))) for w in `other`, or the pair (k, (v, None)) if no elements in `other` have key k. Uses the given Partitioner to partition the output RDD. 
  60. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#log:org.slf4j.Logger "Permalink") def log: Logger 

Attributes
    protected  

Definition Classes
    Logging
  61. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#logBasedOnLevel\(level:org.slf4j.event.Level\)\(f:=>org.apache.spark.internal.MessageWithContext\):Unit "Permalink") def logBasedOnLevel(level: Level)(f: => MessageWithContext): Unit 

Attributes
    protected  

Definition Classes
    Logging
  62. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#logDebug\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logDebug(msg: => String, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  63. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#logDebug\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logDebug(entry: LogEntry, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  64. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#logDebug\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logDebug(entry: LogEntry): Unit 

Attributes
    protected  

Definition Classes
    Logging
  65. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#logDebug\(msg:=>String\):Unit "Permalink") def logDebug(msg: => String): Unit 

Attributes
    protected  

Definition Classes
    Logging
  66. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#logError\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logError(msg: => String, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  67. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#logError\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logError(entry: LogEntry, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  68. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#logError\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logError(entry: LogEntry): Unit 

Attributes
    protected  

Definition Classes
    Logging
  69. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#logError\(msg:=>String\):Unit "Permalink") def logError(msg: => String): Unit 

Attributes
    protected  

Definition Classes
    Logging
  70. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#logInfo\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logInfo(msg: => String, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  71. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#logInfo\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logInfo(entry: LogEntry, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  72. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#logInfo\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logInfo(entry: LogEntry): Unit 

Attributes
    protected  

Definition Classes
    Logging
  73. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#logInfo\(msg:=>String\):Unit "Permalink") def logInfo(msg: => String): Unit 

Attributes
    protected  

Definition Classes
    Logging
  74. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#logName:String "Permalink") def logName: [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String") 

Attributes
    protected  

Definition Classes
    Logging
  75. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#logTrace\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logTrace(msg: => String, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  76. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#logTrace\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logTrace(entry: LogEntry, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  77. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#logTrace\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logTrace(entry: LogEntry): Unit 

Attributes
    protected  

Definition Classes
    Logging
  78. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#logTrace\(msg:=>String\):Unit "Permalink") def logTrace(msg: => String): Unit 

Attributes
    protected  

Definition Classes
    Logging
  79. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#logWarning\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logWarning(msg: => String, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  80. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#logWarning\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logWarning(entry: LogEntry, throwable: Throwable): Unit 

Attributes
    protected  

Definition Classes
    Logging
  81. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#logWarning\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logWarning(entry: LogEntry): Unit 

Attributes
    protected  

Definition Classes
    Logging
  82. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#logWarning\(msg:=>String\):Unit "Permalink") def logWarning(msg: => String): Unit 

Attributes
    protected  

Definition Classes
    Logging
  83. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#lookup\(key:K\):Seq\[V\] "Permalink") def lookup(key: K): Seq[V]
Return the list of values in the RDD for key `key`.
Return the list of values in the RDD for key `key`. This operation is done efficiently if the RDD has a known partitioner by only searching the partition that the key maps to. 
  84. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#mapValues\[U\]\(f:V=>U\):org.apache.spark.rdd.RDD\[\(K,U\)\] "Permalink") def mapValues[U](f: (V) => U): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, U)]
Pass each value in the key-value pair RDD through a map function without changing the keys; this also retains the original RDD's partitioning.
  85. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  86. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#notify\(\):Unit "Permalink") final  def notify(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  87. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  88. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#partitionBy\(partitioner:org.apache.spark.Partitioner\):org.apache.spark.rdd.RDD\[\(K,V\)\] "Permalink") def partitionBy(partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner")): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, V)]
Return a copy of the RDD partitioned using the specified partitioner.
  89. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#reduceByKey\(func:\(V,V\)=>V\):org.apache.spark.rdd.RDD\[\(K,V\)\] "Permalink") def reduceByKey(func: (V, V) => V): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, V)]
Merge the values for each key using an associative and commutative reduce function.
Merge the values for each key using an associative and commutative reduce function. This will also perform the merging locally on each mapper before sending results to a reducer, similarly to a "combiner" in MapReduce. Output will be hash-partitioned with the existing partitioner/ parallelism level. 
  90. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#reduceByKey\(func:\(V,V\)=>V,numPartitions:Int\):org.apache.spark.rdd.RDD\[\(K,V\)\] "Permalink") def reduceByKey(func: (V, V) => V, numPartitions: Int): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, V)]
Merge the values for each key using an associative and commutative reduce function.
Merge the values for each key using an associative and commutative reduce function. This will also perform the merging locally on each mapper before sending results to a reducer, similarly to a "combiner" in MapReduce. Output will be hash-partitioned with numPartitions partitions. 
  91. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#reduceByKey\(partitioner:org.apache.spark.Partitioner,func:\(V,V\)=>V\):org.apache.spark.rdd.RDD\[\(K,V\)\] "Permalink") def reduceByKey(partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner"), func: (V, V) => V): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, V)]
Merge the values for each key using an associative and commutative reduce function.
Merge the values for each key using an associative and commutative reduce function. This will also perform the merging locally on each mapper before sending results to a reducer, similarly to a "combiner" in MapReduce. 
  92. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#reduceByKeyLocally\(func:\(V,V\)=>V\):scala.collection.Map\[K,V\] "Permalink") def reduceByKeyLocally(func: (V, V) => V): Map[K, V]
Merge the values for each key using an associative and commutative reduce function, but return the results immediately to the master as a Map.
Merge the values for each key using an associative and commutative reduce function, but return the results immediately to the master as a Map. This will also perform the merging locally on each mapper before sending results to a reducer, similarly to a "combiner" in MapReduce. 
  93. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#rightOuterJoin\[W\]\(other:org.apache.spark.rdd.RDD\[\(K,W\)\],numPartitions:Int\):org.apache.spark.rdd.RDD\[\(K,\(Option\[V\],W\)\)\] "Permalink") def rightOuterJoin[W](other: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, W)], numPartitions: Int): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, (Option[V], W))]
Perform a right outer join of `this` and `other`.
Perform a right outer join of `this` and `other`. For each element (k, w) in `other`, the resulting RDD will either contain all pairs (k, (Some(v), w)) for v in `this`, or the pair (k, (None, w)) if no elements in `this` have key k. Hash-partitions the resulting RDD into the given number of partitions. 
  94. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#rightOuterJoin\[W\]\(other:org.apache.spark.rdd.RDD\[\(K,W\)\]\):org.apache.spark.rdd.RDD\[\(K,\(Option\[V\],W\)\)\] "Permalink") def rightOuterJoin[W](other: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, W)]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, (Option[V], W))]
Perform a right outer join of `this` and `other`.
Perform a right outer join of `this` and `other`. For each element (k, w) in `other`, the resulting RDD will either contain all pairs (k, (Some(v), w)) for v in `this`, or the pair (k, (None, w)) if no elements in `this` have key k. Hash-partitions the resulting RDD using the existing partitioner/parallelism level. 
  95. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#rightOuterJoin\[W\]\(other:org.apache.spark.rdd.RDD\[\(K,W\)\],partitioner:org.apache.spark.Partitioner\):org.apache.spark.rdd.RDD\[\(K,\(Option\[V\],W\)\)\] "Permalink") def rightOuterJoin[W](other: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, W)], partitioner: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner")): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, (Option[V], W))]
Perform a right outer join of `this` and `other`.
Perform a right outer join of `this` and `other`. For each element (k, w) in `other`, the resulting RDD will either contain all pairs (k, (Some(v), w)) for v in `this`, or the pair (k, (None, w)) if no elements in `this` have key k. Uses the given Partitioner to partition the output RDD. 
  96. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#sampleByKey\(withReplacement:Boolean,fractions:scala.collection.Map\[K,Double\],seed:Long\):org.apache.spark.rdd.RDD\[\(K,V\)\] "Permalink") def sampleByKey(withReplacement: Boolean, fractions: Map[K, Double], seed: Long = [Utils.random.nextLong](https://spark.apache.org/docs/latest/api/scala/org/index.html)): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, V)]
Return a subset of this RDD sampled by key (via stratified sampling).
Return a subset of this RDD sampled by key (via stratified sampling).
Create a sample of this RDD using variable sampling rates for different keys as specified by `fractions`, a key to sampling rate map, via simple random sampling with one pass over the RDD, to produce a sample of size that's approximately equal to the sum of math.ceil(numItems * samplingRate) over all key values.  

withReplacement
    
whether to sample with or without replacement 

fractions
    
map of specific keys to sampling rates 

seed
    
seed for the random number generator 

returns
    
RDD containing the sampled subset
  97. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#sampleByKeyExact\(withReplacement:Boolean,fractions:scala.collection.Map\[K,Double\],seed:Long\):org.apache.spark.rdd.RDD\[\(K,V\)\] "Permalink") def sampleByKeyExact(withReplacement: Boolean, fractions: Map[K, Double], seed: Long = [Utils.random.nextLong](https://spark.apache.org/docs/latest/api/scala/org/index.html)): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, V)]
Return a subset of this RDD sampled by key (via stratified sampling) containing exactly math.ceil(numItems * samplingRate) for each stratum (group of pairs with the same key).
Return a subset of this RDD sampled by key (via stratified sampling) containing exactly math.ceil(numItems * samplingRate) for each stratum (group of pairs with the same key).
This method differs from [sampleByKey](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#sampleByKey\(withReplacement:Boolean,fractions:scala.collection.Map\[K,Double\],seed:Long\):org.apache.spark.rdd.RDD\[\(K,V\)\]) in that we make additional passes over the RDD to create a sample size that's exactly equal to the sum of math.ceil(numItems * samplingRate) over all key values with a 99.99% confidence. When sampling without replacement, we need one additional pass over the RDD to guarantee sample size; when sampling with replacement, we need two additional passes.  

withReplacement
    
whether to sample with or without replacement 

fractions
    
map of specific keys to sampling rates 

seed
    
seed for the random number generator 

returns
    
RDD containing the sampled subset
  98. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#saveAsHadoopDataset\(conf:org.apache.hadoop.mapred.JobConf\):Unit "Permalink") def saveAsHadoopDataset(conf: JobConf): Unit
Output the RDD to any Hadoop-supported storage system, using a Hadoop JobConf object for that storage system.
Output the RDD to any Hadoop-supported storage system, using a Hadoop JobConf object for that storage system. The JobConf should set an OutputFormat and any output paths required (e.g. a table name to write to) in the same way as it would be configured for a Hadoop MapReduce job. 
  99. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#saveAsHadoopFile\(path:String,keyClass:Class\[_\],valueClass:Class\[_\],outputFormatClass:Class\[_<:org.apache.hadoop.mapred.OutputFormat\[_,_\]\],conf:org.apache.hadoop.mapred.JobConf,codec:Option\[Class\[_<:org.apache.hadoop.io.compress.CompressionCodec\]\]\):Unit "Permalink") def saveAsHadoopFile(path: String, keyClass: Class[_], valueClass: Class[_], outputFormatClass: Class[_ <: OutputFormat[_, _]], conf: JobConf = [new JobConf(self.context.hadoopConfiguration)](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html#context:org.apache.spark.SparkContext), codec: Option[Class[_ <: CompressionCodec]] = None): Unit
Output the RDD to any Hadoop-supported file system, using a Hadoop `OutputFormat` class supporting the key and value types K and V in this RDD.
Output the RDD to any Hadoop-supported file system, using a Hadoop `OutputFormat` class supporting the key and value types K and V in this RDD.  

Note
    
We should make sure our tasks are idempotent when speculation is enabled, i.e. do not use output committer that writes data directly. There is an example in https://issues.apache.org/jira/browse/SPARK-10063 to show the bad result of using direct output committer with speculation enabled.
  100. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#saveAsHadoopFile\(path:String,keyClass:Class\[_\],valueClass:Class\[_\],outputFormatClass:Class\[_<:org.apache.hadoop.mapred.OutputFormat\[_,_\]\],codec:Class\[_<:org.apache.hadoop.io.compress.CompressionCodec\]\):Unit "Permalink") def saveAsHadoopFile(path: String, keyClass: Class[_], valueClass: Class[_], outputFormatClass: Class[_ <: OutputFormat[_, _]], codec: Class[_ <: CompressionCodec]): Unit
Output the RDD to any Hadoop-supported file system, using a Hadoop `OutputFormat` class supporting the key and value types K and V in this RDD.
Output the RDD to any Hadoop-supported file system, using a Hadoop `OutputFormat` class supporting the key and value types K and V in this RDD. Compress with the supplied codec. 
  101. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#saveAsHadoopFile\[F<:org.apache.hadoop.mapred.OutputFormat\[K,V\]\]\(path:String,codec:Class\[_<:org.apache.hadoop.io.compress.CompressionCodec\]\)\(implicitfm:scala.reflect.ClassTag\[F\]\):Unit "Permalink") def saveAsHadoopFile[F <: OutputFormat[K, V]](path: String, codec: Class[_ <: CompressionCodec])(implicit fm: ClassTag[F]): Unit
Output the RDD to any Hadoop-supported file system, using a Hadoop `OutputFormat` class supporting the key and value types K and V in this RDD.
Output the RDD to any Hadoop-supported file system, using a Hadoop `OutputFormat` class supporting the key and value types K and V in this RDD. Compress the result with the supplied codec. 
  102. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#saveAsHadoopFile\[F<:org.apache.hadoop.mapred.OutputFormat\[K,V\]\]\(path:String\)\(implicitfm:scala.reflect.ClassTag\[F\]\):Unit "Permalink") def saveAsHadoopFile[F <: OutputFormat[K, V]](path: String)(implicit fm: ClassTag[F]): Unit
Output the RDD to any Hadoop-supported file system, using a Hadoop `OutputFormat` class supporting the key and value types K and V in this RDD.
  103. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#saveAsNewAPIHadoopDataset\(conf:org.apache.hadoop.conf.Configuration\):Unit "Permalink") def saveAsNewAPIHadoopDataset(conf: Configuration): Unit
Output the RDD to any Hadoop-supported storage system with new Hadoop API, using a Hadoop Configuration object for that storage system.
Output the RDD to any Hadoop-supported storage system with new Hadoop API, using a Hadoop Configuration object for that storage system. The Conf should set an OutputFormat and any output paths required (e.g. a table name to write to) in the same way as it would be configured for a Hadoop MapReduce job.  

Note
    
We should make sure our tasks are idempotent when speculation is enabled, i.e. do not use output committer that writes data directly. There is an example in https://issues.apache.org/jira/browse/SPARK-10063 to show the bad result of using direct output committer with speculation enabled.
  104. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#saveAsNewAPIHadoopFile\(path:String,keyClass:Class\[_\],valueClass:Class\[_\],outputFormatClass:Class\[_<:org.apache.hadoop.mapreduce.OutputFormat\[_,_\]\],conf:org.apache.hadoop.conf.Configuration\):Unit "Permalink") def saveAsNewAPIHadoopFile(path: String, keyClass: Class[_], valueClass: Class[_], outputFormatClass: Class[_ <: OutputFormat[_, _]], conf: Configuration = [self.context.hadoopConfiguration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html#context:org.apache.spark.SparkContext)): Unit
Output the RDD to any Hadoop-supported file system, using a new Hadoop API `OutputFormat` (mapreduce.OutputFormat) object supporting the key and value types K and V in this RDD.
  105. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#saveAsNewAPIHadoopFile\[F<:org.apache.hadoop.mapreduce.OutputFormat\[K,V\]\]\(path:String\)\(implicitfm:scala.reflect.ClassTag\[F\]\):Unit "Permalink") def saveAsNewAPIHadoopFile[F <: OutputFormat[K, V]](path: String)(implicit fm: ClassTag[F]): Unit
Output the RDD to any Hadoop-supported file system, using a new Hadoop API `OutputFormat` (mapreduce.OutputFormat) object supporting the key and value types K and V in this RDD.
  106. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#subtractByKey\[W\]\(other:org.apache.spark.rdd.RDD\[\(K,W\)\],p:org.apache.spark.Partitioner\)\(implicitevidence$6:scala.reflect.ClassTag\[W\]\):org.apache.spark.rdd.RDD\[\(K,V\)\] "Permalink") def subtractByKey[W](other: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, W)], p: [Partitioner](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/Partitioner.html "org.apache.spark.Partitioner"))(implicit arg0: ClassTag[W]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, V)]
Return an RDD with the pairs from `this` whose keys are not in `other`.
  107. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#subtractByKey\[W\]\(other:org.apache.spark.rdd.RDD\[\(K,W\)\],numPartitions:Int\)\(implicitevidence$5:scala.reflect.ClassTag\[W\]\):org.apache.spark.rdd.RDD\[\(K,V\)\] "Permalink") def subtractByKey[W](other: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, W)], numPartitions: Int)(implicit arg0: ClassTag[W]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, V)]
Return an RDD with the pairs from `this` whose keys are not in `other`.
  108. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#subtractByKey\[W\]\(other:org.apache.spark.rdd.RDD\[\(K,W\)\]\)\(implicitevidence$4:scala.reflect.ClassTag\[W\]\):org.apache.spark.rdd.RDD\[\(K,V\)\] "Permalink") def subtractByKey[W](other: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, W)])(implicit arg0: ClassTag[W]): [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[(K, V)]
Return an RDD with the pairs from `this` whose keys are not in `other`.
Return an RDD with the pairs from `this` whose keys are not in `other`.
Uses `this` partitioner/partition size, because even if `other` is huge, the resulting RDD will be less than or equal to us. 
  109. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0 

Definition Classes
    AnyRef
  110. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#toString\(\):String "Permalink") def toString(): [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String") 

Definition Classes
    AnyRef → Any
  111. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#values:org.apache.spark.rdd.RDD\[V\] "Permalink") def values: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[V]
Return an RDD with the values of each tuple.
  112. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  113. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  114. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#wait\(\):Unit "Permalink") final  def wait(): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  115. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#withLogContext\(context:java.util.Map\[String,String\]\)\(body:=>Unit\):Unit "Permalink") def withLogContext(context: [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#java.util.Map "java.util.Map")[String, String])(body: => Unit): Unit 

Attributes
    protected  

Definition Classes
    Logging
  116. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html#finalize\(\):Unit "Permalink") def finalize(): Unit 

Attributes
    protected[lang]  

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.Throwable]) @Deprecated 

Deprecated
    
_(Since version 9)_


