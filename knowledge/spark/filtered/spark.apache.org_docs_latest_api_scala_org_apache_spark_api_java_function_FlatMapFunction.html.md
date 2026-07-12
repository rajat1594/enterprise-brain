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
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/index.html "Permalink") package [api](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/index.html) 

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/index.html "Permalink") package [java](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/index.html "Spark Java programming APIs.")
Spark Java programming APIs.
Spark Java programming APIs. 

Definition Classes
    [api](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/index.html "org.apache.spark.api")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/index.html "Permalink") package [function](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/index.html "Set of interfaces to represent functions in Spark's Java API.")
Set of interfaces to represent functions in Spark's Java API.
Set of interfaces to represent functions in Spark's Java API. Users create implementations of these interfaces to pass functions to various Java API methods for Spark. Please visit Spark's Java programming guide for more details.  

Definition Classes
    [java](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/index.html "org.apache.spark.api.java")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/CoGroupFunction.html "A function that returns zero or more output records from each grouping key and its values from 2 Datasets.")[CoGroupFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/CoGroupFunction.html "A function that returns zero or more output records from each grouping key and its values from 2 Datasets.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/DoubleFlatMapFunction.html "A function that returns zero or more records of type Double from each input record.")[DoubleFlatMapFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/DoubleFlatMapFunction.html "A function that returns zero or more records of type Double from each input record.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/DoubleFunction.html "A function that returns Doubles, and can be used to construct DoubleRDDs.")[DoubleFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/DoubleFunction.html "A function that returns Doubles, and can be used to construct DoubleRDDs.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FilterFunction.html "Base interface for a function used in Dataset's filter function.")[FilterFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FilterFunction.html "Base interface for a function used in Dataset's filter function.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction.html "A function that returns zero or more output records from each input record.")[FlatMapFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction.html "A function that returns zero or more output records from each input record.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction2.html "A function that takes two inputs and returns zero or more output records.")[FlatMapFunction2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction2.html "A function that takes two inputs and returns zero or more output records.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapGroupsFunction.html "A function that returns zero or more output records from each grouping key and its values.")[FlatMapGroupsFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapGroupsFunction.html "A function that returns zero or more output records from each grouping key and its values.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapGroupsWithStateFunction.html "::Experimental:: Base interface for a map function used in org.apache.spark.sql.KeyValueGroupedDataset.flatMapGroupsWithState\( FlatMapGroupsWithStateFunction, org.apache.spark.sql.streaming.OutputMode, org.apache.spark.sql.Encoder, org.apache.spark.sql.Encoder\)")[FlatMapGroupsWithStateFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapGroupsWithStateFunction.html "::Experimental:: Base interface for a map function used in org.apache.spark.sql.KeyValueGroupedDataset.flatMapGroupsWithState\( FlatMapGroupsWithStateFunction, org.apache.spark.sql.streaming.OutputMode, org.apache.spark.sql.Encoder, org.apache.spark.sql.Encoder\)")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/ForeachFunction.html "Base interface for a function used in Dataset's foreach function.")[ForeachFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/ForeachFunction.html "Base interface for a function used in Dataset's foreach function.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/ForeachPartitionFunction.html "Base interface for a function used in Dataset's foreachPartition function.")[ForeachPartitionFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/ForeachPartitionFunction.html "Base interface for a function used in Dataset's foreachPartition function.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function.html "Base interface for functions whose return types do not create special RDDs.")[Function](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function.html "Base interface for functions whose return types do not create special RDDs.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function0.html "A zero-argument function that returns an R.")[Function0](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function0.html "A zero-argument function that returns an R.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "A two-argument function that takes arguments of type T1 and T2 and returns an R.")[Function2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function2.html "A two-argument function that takes arguments of type T1 and T2 and returns an R.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function3.html "A three-argument function that takes arguments of type T1, T2 and T3 and returns an R.")[Function3](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function3.html "A three-argument function that takes arguments of type T1, T2 and T3 and returns an R.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function4.html "A four-argument function that takes arguments of type T1, T2, T3 and T4 and returns an R.")[Function4](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/Function4.html "A four-argument function that takes arguments of type T1, T2, T3 and T4 and returns an R.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/MapFunction.html "Base interface for a map function used in Dataset's map function.")[MapFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/MapFunction.html "Base interface for a map function used in Dataset's map function.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/MapGroupsFunction.html "Base interface for a map function used in GroupedDataset's mapGroup function.")[MapGroupsFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/MapGroupsFunction.html "Base interface for a map function used in GroupedDataset's mapGroup function.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/MapGroupsWithStateFunction.html "::Experimental:: Base interface for a map function used in MapGroupsWithStateFunction, org.apache.spark.sql.Encoder, org.apache.spark.sql.Encoder\)")[MapGroupsWithStateFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/MapGroupsWithStateFunction.html "::Experimental:: Base interface for a map function used in MapGroupsWithStateFunction, org.apache.spark.sql.Encoder, org.apache.spark.sql.Encoder\)")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/MapPartitionsFunction.html "Base interface for function used in Dataset's mapPartitions.")[MapPartitionsFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/MapPartitionsFunction.html "Base interface for function used in Dataset's mapPartitions.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/PairFlatMapFunction.html "A function that returns zero or more key-value pair records from each input record.")[PairFlatMapFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/PairFlatMapFunction.html "A function that returns zero or more key-value pair records from each input record.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/PairFunction.html "A function that returns key-value pairs \(Tuple2&lt;K, V&gt;\), and can be used to construct PairRDDs.")[PairFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/PairFunction.html "A function that returns key-value pairs \(Tuple2&lt;K, V&gt;\), and can be used to construct PairRDDs.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/ReduceFunction.html "Base interface for function used in Dataset's reduce.")[ReduceFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/ReduceFunction.html "Base interface for function used in Dataset's reduce.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/VoidFunction.html "A function with no return value.")[VoidFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/VoidFunction.html "A function with no return value.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/VoidFunction2.html "A two-argument function that takes arguments of type T1 and T2 with no return value.")[VoidFunction2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/VoidFunction2.html "A two-argument function that takes arguments of type T1 and T2 with no return value.")


t
[org](https://spark.apache.org/docs/latest/api/scala/org/index.html "org").[apache](https://spark.apache.org/docs/latest/api/scala/org/apache/index.html "org.apache").[spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark").[api](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/index.html "org.apache.spark.api").[java](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/index.html "org.apache.spark.api.java").[function](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/index.html "org.apache.spark.api.java.function")
# FlatMapFunction[ __](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction.html "Permalink")
####  trait FlatMapFunction[T, R] extends [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable")
A function that returns zero or more output records from each input record.  

Annotations
     @FunctionalInterface() 

Source
    [FlatMapFunction.java](https://github.com/apache/spark/tree/v4.1.2/common/utils-java/src/main/java/org/apache/spark/api/java/function/FlatMapFunction.java)
Linear Supertypes
[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable"), AnyRef, Any
__ __
Ordering
  1. Alphabetic
  2. By Inheritance


Inherited  

  1. FlatMapFunction
  2. Serializable
  3. AnyRef
  4. Any


  1. Hide All
  2. Show All


Visibility
  1. Public
  2. Protected


### Abstract Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction.html#call\(t:T\):java.util.Iterator\[R\] "Permalink") abstract  def call(t: T): [Iterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html#java.util.Iterator "java.util.Iterator")[R]


### Concrete Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction.html###:Int "Permalink") final  def ##: Int 

Definition Classes
    AnyRef → Any
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0 

Definition Classes
    Any
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction.html#clone\(\):Object "Permalink") def clone(): AnyRef 

Attributes
    protected[lang]  

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction.html#equals\(x$1:Object\):Boolean "Permalink") def equals(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef → Any
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef] 

Definition Classes
    AnyRef → Any 

Annotations
     @IntrinsicCandidate() @native()
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction.html#hashCode\(\):Int "Permalink") def hashCode(): Int 

Definition Classes
    AnyRef → Any 

Annotations
     @IntrinsicCandidate() @native()
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean 

Definition Classes
    Any
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction.html#notify\(\):Unit "Permalink") final  def notify(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0 

Definition Classes
    AnyRef
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction.html#toString\(\):String "Permalink") def toString(): [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String") 

Definition Classes
    AnyRef → Any
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction.html#wait\(\):Unit "Permalink") final  def wait(): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])


### Deprecated Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction.html#finalize\(\):Unit "Permalink") def finalize(): Unit 

Attributes
    protected[lang]  

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.Throwable]) @Deprecated 

Deprecated
    
_(Since version 9)_


### Inherited from AnyRef
### Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction.html###:Int "Permalink") final  def ##: Int 

Definition Classes
    AnyRef → Any
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction.html#clone\(\):Object "Permalink") def clone(): AnyRef 

Attributes
    protected[lang]  

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction.html#equals\(x$1:Object\):Boolean "Permalink") def equals(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef → Any
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef] 

Definition Classes
    AnyRef → Any 

Annotations
     @IntrinsicCandidate() @native()
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction.html#hashCode\(\):Int "Permalink") def hashCode(): Int 

Definition Classes
    AnyRef → Any 

Annotations
     @IntrinsicCandidate() @native()
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction.html#notify\(\):Unit "Permalink") final  def notify(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0 

Definition Classes
    AnyRef
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction.html#toString\(\):String "Permalink") def toString(): [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String") 

Definition Classes
    AnyRef → Any
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction.html#wait\(\):Unit "Permalink") final  def wait(): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction.html#finalize\(\):Unit "Permalink") def finalize(): Unit 

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
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0 

Definition Classes
    Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean 

Definition Classes
    Any


### Ungrouped
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction.html#call\(t:T\):java.util.Iterator\[R\] "Permalink") abstract  def call(t: T): [Iterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html#java.util.Iterator "java.util.Iterator")[R]
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction.html###:Int "Permalink") final  def ##: Int 

Definition Classes
    AnyRef → Any
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0 

Definition Classes
    Any
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction.html#clone\(\):Object "Permalink") def clone(): AnyRef 

Attributes
    protected[lang]  

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction.html#equals\(x$1:Object\):Boolean "Permalink") def equals(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef → Any
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef] 

Definition Classes
    AnyRef → Any 

Annotations
     @IntrinsicCandidate() @native()
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction.html#hashCode\(\):Int "Permalink") def hashCode(): Int 

Definition Classes
    AnyRef → Any 

Annotations
     @IntrinsicCandidate() @native()
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean 

Definition Classes
    Any
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction.html#notify\(\):Unit "Permalink") final  def notify(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0 

Definition Classes
    AnyRef
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction.html#toString\(\):String "Permalink") def toString(): [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String") 

Definition Classes
    AnyRef → Any
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction.html#wait\(\):Unit "Permalink") final  def wait(): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction.html#finalize\(\):Unit "Permalink") def finalize(): Unit 

Attributes
    protected[lang]  

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.Throwable]) @Deprecated 

Deprecated
    
_(Since version 9)_


