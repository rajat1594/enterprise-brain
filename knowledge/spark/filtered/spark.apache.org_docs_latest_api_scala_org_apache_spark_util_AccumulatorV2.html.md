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
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/index.html "Permalink") package [util](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/index.html "Spark utilities.")
Spark utilities.
Spark utilities.  

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/random/index.html "Permalink") package [random](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/random/index.html "Utilities for random number generation.")
Utilities for random number generation.
Utilities for random number generation.  

Definition Classes
    [util](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/index.html "org.apache.spark.util")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/sketch/index.html "Permalink") package [sketch](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/sketch/index.html) 

Definition Classes
    [util](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/index.html "org.apache.spark.util")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html "The base class for accumulators, that can accumulate inputs of type IN, and produce output of type OUT.")[AccumulatorV2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html "The base class for accumulators, that can accumulate inputs of type IN, and produce output of type OUT.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/ChildFirstURLClassLoader.html "A mutable class loader that gives preference to its own URLs over the parent class loader when loading classes and resources.")[ChildFirstURLClassLoader](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/ChildFirstURLClassLoader.html "A mutable class loader that gives preference to its own URLs over the parent class loader when loading classes and resources.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/CollectionAccumulator.html "An accumulator for collecting a list of elements.")[CollectionAccumulator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/CollectionAccumulator.html "An accumulator for collecting a list of elements.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/DoubleAccumulator.html "An accumulator for computing sum, count, and averages for double precision floating numbers.")[DoubleAccumulator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/DoubleAccumulator.html "An accumulator for computing sum, count, and averages for double precision floating numbers.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/EnumUtil.html)[EnumUtil](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/EnumUtil.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/ExposedBufferByteArrayOutputStream.html "Subclass of ByteArrayOutputStream that exposes buf directly.")[ExposedBufferByteArrayOutputStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/ExposedBufferByteArrayOutputStream.html "Subclass of ByteArrayOutputStream that exposes buf directly.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/LexicalThreadLocal.html "Helper trait for defining thread locals with lexical scoping.")[LexicalThreadLocal](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/LexicalThreadLocal.html "Helper trait for defining thread locals with lexical scoping.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/LogUtils$.html ":: : DeveloperApi :: Utils for querying Spark logs with Spark SQL.")[LogUtils](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/LogUtils$.html ":: : DeveloperApi :: Utils for querying Spark logs with Spark SQL.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/LongAccumulator.html "An accumulator for computing sum, count, and average of 64-bit integers.")[LongAccumulator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/LongAccumulator.html "An accumulator for computing sum, count, and average of 64-bit integers.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/MutablePair.html ":: DeveloperApi :: A tuple of 2 elements.")[MutablePair](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/MutablePair.html ":: DeveloperApi :: A tuple of 2 elements.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/MutableURLClassLoader.html "URL class loader that exposes the addURL method in URLClassLoader.")[MutableURLClassLoader](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/MutableURLClassLoader.html "URL class loader that exposes the addURL method in URLClassLoader.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/Pair.html "An immutable pair of values.")[Pair](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/Pair.html "An immutable pair of values.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/ParentClassLoader.html "A class loader which makes some protected methods in ClassLoader accessible.")[ParentClassLoader](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/ParentClassLoader.html "A class loader which makes some protected methods in ClassLoader accessible.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/SerializableConfiguration.html "Hadoop configuration but serializable.")[SerializableConfiguration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/SerializableConfiguration.html "Hadoop configuration but serializable.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/SizeEstimator$.html ":: DeveloperApi :: Estimates the sizes of Java objects \(number of bytes of memory they occupy\), for use in memory-aware caches.")[SizeEstimator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/SizeEstimator$.html ":: DeveloperApi :: Estimates the sizes of Java objects \(number of bytes of memory they occupy\), for use in memory-aware caches.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/SparkEnvUtils$.html)[SparkEnvUtils](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/SparkEnvUtils$.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/SparkSystemUtils$.html)[SparkSystemUtils](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/SparkSystemUtils$.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/StatCounter$.html) [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/StatCounter.html "A class for tracking the statistics of a set of numbers \(count, mean and variance\) in a numerically robust way.")[StatCounter](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/StatCounter.html "A class for tracking the statistics of a set of numbers \(count, mean and variance\) in a numerically robust way.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/TaskCompletionListener.html ":: DeveloperApi ::")[TaskCompletionListener](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/TaskCompletionListener.html ":: DeveloperApi ::")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/TaskFailureListener.html ":: DeveloperApi ::")[TaskFailureListener](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/TaskFailureListener.html ":: DeveloperApi ::")


c
[org](https://spark.apache.org/docs/latest/api/scala/org/index.html "org").[apache](https://spark.apache.org/docs/latest/api/scala/org/apache/index.html "org.apache").[spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark").[util](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/index.html "org.apache.spark.util")
# AccumulatorV2[ __](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html "Permalink")
####  abstract  class AccumulatorV2[IN, OUT] extends Serializable
The base class for accumulators, that can accumulate inputs of type `IN`, and produce output of type `OUT`.
`OUT` should be a type that can be read atomically (e.g., Int, Long), or thread-safely (e.g., synchronized collections) because it will be read from other threads.  

Source
    [AccumulatorV2.scala](https://github.com/apache/spark/tree/v4.1.2/core/src/main/scala/org/apache/spark/util/AccumulatorV2.scala)
Linear Supertypes
[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable"), AnyRef, Any
Known Subclasses
[MapperRowCounter](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/util/MapperRowCounter.html "org.apache.spark.sql.util.MapperRowCounter"), [CollectionAccumulator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/CollectionAccumulator.html "org.apache.spark.util.CollectionAccumulator"), [DoubleAccumulator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/DoubleAccumulator.html "org.apache.spark.util.DoubleAccumulator"), [LongAccumulator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/LongAccumulator.html "org.apache.spark.util.LongAccumulator")
__ __
Ordering
  1. Alphabetic
  2. By Inheritance


Inherited  

  1. AccumulatorV2
  2. Serializable
  3. AnyRef
  4. Any


  1. Hide All
  2. Show All


Visibility
  1. Public
  2. Protected


### Instance Constructors
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#<init>\(\):org.apache.spark.util.AccumulatorV2\[IN,OUT\] "Permalink") new AccumulatorV2()


### Abstract Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#add\(v:IN\):Unit "Permalink") abstract  def add(v: IN): Unit
Takes the inputs and accumulates.
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#copy\(\):org.apache.spark.util.AccumulatorV2\[IN,OUT\] "Permalink") abstract  def copy(): [AccumulatorV2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html "org.apache.spark.util.AccumulatorV2")[IN, OUT]
Creates a new copy of this accumulator.
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#isZero:Boolean "Permalink") abstract  def isZero: Boolean
Returns if this accumulator is zero value or not.
Returns if this accumulator is zero value or not. e.g. for a counter accumulator, 0 is zero value; for a list accumulator, Nil is zero value. 
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#merge\(other:org.apache.spark.util.AccumulatorV2\[IN,OUT\]\):Unit "Permalink") abstract  def merge(other: [AccumulatorV2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html "org.apache.spark.util.AccumulatorV2")[IN, OUT]): Unit
Merges another same-type accumulator into this one and update its state, i.e.
Merges another same-type accumulator into this one and update its state, i.e. this should be merge-in-place. 
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#reset\(\):Unit "Permalink") abstract  def reset(): Unit
Resets this accumulator, which is zero value.
Resets this accumulator, which is zero value. i.e. call `isZero` must return true. 
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#value:OUT "Permalink") abstract  def value: OUT
Defines the current value of this accumulator 


### Concrete Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html###:Int "Permalink") final  def ##: Int 

Definition Classes
    AnyRef → Any
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0 

Definition Classes
    Any
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#clone\(\):Object "Permalink") def clone(): AnyRef 

Attributes
    protected[lang]  

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#copyAndReset\(\):org.apache.spark.util.AccumulatorV2\[IN,OUT\] "Permalink") def copyAndReset(): [AccumulatorV2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html "org.apache.spark.util.AccumulatorV2")[IN, OUT]
Creates a new copy of this accumulator, which is zero value.
Creates a new copy of this accumulator, which is zero value. i.e. call `isZero` on the copy must return true. 
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#equals\(x$1:Object\):Boolean "Permalink") def equals(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef → Any
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#excludeFromHeartbeat:Boolean "Permalink") def excludeFromHeartbeat: Boolean
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef] 

Definition Classes
    AnyRef → Any 

Annotations
     @IntrinsicCandidate() @native()
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#hashCode\(\):Int "Permalink") def hashCode(): Int 

Definition Classes
    AnyRef → Any 

Annotations
     @IntrinsicCandidate() @native()
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#id:Long "Permalink") final  def id: Long
Returns the id of this accumulator, can only be called after registration.
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean 

Definition Classes
    Any
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#isRegistered:Boolean "Permalink") final  def isRegistered: Boolean
Returns true if this accumulator has been registered.
Returns true if this accumulator has been registered.  

Note
    
All accumulators must be registered before use, or it will throw exception.
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#name:Option\[String\] "Permalink") final  def name: Option[String]
Returns the name of this accumulator, can only be called after registration.
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#notify\(\):Unit "Permalink") final  def notify(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0 

Definition Classes
    AnyRef
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#toString\(\):String "Permalink") def toString(): String 

Definition Classes
     [AccumulatorV2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html "org.apache.spark.util.AccumulatorV2") → AnyRef → Any
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  23. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#wait\(\):Unit "Permalink") final  def wait(): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  24. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#withBufferSerialized\(\):org.apache.spark.util.AccumulatorV2\[IN,OUT\] "Permalink") def withBufferSerialized(): [AccumulatorV2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html "org.apache.spark.util.AccumulatorV2")[IN, OUT] 

Attributes
    protected 
  25. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#writeReplace\(\):Any "Permalink") final  def writeReplace(): Any 

Attributes
    protected 


### Deprecated Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#finalize\(\):Unit "Permalink") def finalize(): Unit 

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
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html###:Int "Permalink") final  def ##: Int 

Definition Classes
    AnyRef → Any
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#clone\(\):Object "Permalink") def clone(): AnyRef 

Attributes
    protected[lang]  

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#equals\(x$1:Object\):Boolean "Permalink") def equals(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef → Any
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef] 

Definition Classes
    AnyRef → Any 

Annotations
     @IntrinsicCandidate() @native()
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#hashCode\(\):Int "Permalink") def hashCode(): Int 

Definition Classes
    AnyRef → Any 

Annotations
     @IntrinsicCandidate() @native()
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#notify\(\):Unit "Permalink") final  def notify(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0 

Definition Classes
    AnyRef
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#wait\(\):Unit "Permalink") final  def wait(): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#finalize\(\):Unit "Permalink") def finalize(): Unit 

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
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0 

Definition Classes
    Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean 

Definition Classes
    Any


### Ungrouped
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#add\(v:IN\):Unit "Permalink") abstract  def add(v: IN): Unit
Takes the inputs and accumulates.
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#copy\(\):org.apache.spark.util.AccumulatorV2\[IN,OUT\] "Permalink") abstract  def copy(): [AccumulatorV2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html "org.apache.spark.util.AccumulatorV2")[IN, OUT]
Creates a new copy of this accumulator.
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#isZero:Boolean "Permalink") abstract  def isZero: Boolean
Returns if this accumulator is zero value or not.
Returns if this accumulator is zero value or not. e.g. for a counter accumulator, 0 is zero value; for a list accumulator, Nil is zero value. 
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#merge\(other:org.apache.spark.util.AccumulatorV2\[IN,OUT\]\):Unit "Permalink") abstract  def merge(other: [AccumulatorV2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html "org.apache.spark.util.AccumulatorV2")[IN, OUT]): Unit
Merges another same-type accumulator into this one and update its state, i.e.
Merges another same-type accumulator into this one and update its state, i.e. this should be merge-in-place. 
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#reset\(\):Unit "Permalink") abstract  def reset(): Unit
Resets this accumulator, which is zero value.
Resets this accumulator, which is zero value. i.e. call `isZero` must return true. 
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#value:OUT "Permalink") abstract  def value: OUT
Defines the current value of this accumulator 
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html###:Int "Permalink") final  def ##: Int 

Definition Classes
    AnyRef → Any
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0 

Definition Classes
    Any
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#clone\(\):Object "Permalink") def clone(): AnyRef 

Attributes
    protected[lang]  

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#copyAndReset\(\):org.apache.spark.util.AccumulatorV2\[IN,OUT\] "Permalink") def copyAndReset(): [AccumulatorV2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html "org.apache.spark.util.AccumulatorV2")[IN, OUT]
Creates a new copy of this accumulator, which is zero value.
Creates a new copy of this accumulator, which is zero value. i.e. call `isZero` on the copy must return true. 
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#equals\(x$1:Object\):Boolean "Permalink") def equals(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef → Any
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#excludeFromHeartbeat:Boolean "Permalink") def excludeFromHeartbeat: Boolean
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef] 

Definition Classes
    AnyRef → Any 

Annotations
     @IntrinsicCandidate() @native()
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#hashCode\(\):Int "Permalink") def hashCode(): Int 

Definition Classes
    AnyRef → Any 

Annotations
     @IntrinsicCandidate() @native()
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#id:Long "Permalink") final  def id: Long
Returns the id of this accumulator, can only be called after registration.
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean 

Definition Classes
    Any
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#isRegistered:Boolean "Permalink") final  def isRegistered: Boolean
Returns true if this accumulator has been registered.
Returns true if this accumulator has been registered.  

Note
    
All accumulators must be registered before use, or it will throw exception.
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#name:Option\[String\] "Permalink") final  def name: Option[String]
Returns the name of this accumulator, can only be called after registration.
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  23. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#notify\(\):Unit "Permalink") final  def notify(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  24. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  25. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0 

Definition Classes
    AnyRef
  26. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#toString\(\):String "Permalink") def toString(): String 

Definition Classes
     [AccumulatorV2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html "org.apache.spark.util.AccumulatorV2") → AnyRef → Any
  27. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  28. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  29. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#wait\(\):Unit "Permalink") final  def wait(): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  30. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#withBufferSerialized\(\):org.apache.spark.util.AccumulatorV2\[IN,OUT\] "Permalink") def withBufferSerialized(): [AccumulatorV2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html "org.apache.spark.util.AccumulatorV2")[IN, OUT] 

Attributes
    protected 
  31. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#writeReplace\(\):Any "Permalink") final  def writeReplace(): Any 

Attributes
    protected 
  32. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html#finalize\(\):Unit "Permalink") def finalize(): Unit 

Attributes
    protected[lang]  

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.Throwable]) @Deprecated 

Deprecated
    
_(Since version 9)_


