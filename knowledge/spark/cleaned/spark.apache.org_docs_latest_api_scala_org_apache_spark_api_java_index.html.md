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
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/index.html "Permalink") package java
Spark Java programming APIs.
Spark Java programming APIs.

Definition Classes
    [api](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/index.html "org.apache.spark.api")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/index.html "Permalink") package [function](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/index.html "Set of interfaces to represent functions in Spark's Java API.")
Set of interfaces to represent functions in Spark's Java API.
Set of interfaces to represent functions in Spark's Java API. Users create implementations of these interfaces to pass functions to various Java API methods for Spark. Please visit Spark's Java programming guide for more details.
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaDoubleRDD$.html) [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaDoubleRDD.html)[JavaDoubleRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaDoubleRDD.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaFutureAction.html)[JavaFutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaFutureAction.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaHadoopRDD.html)[JavaHadoopRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaHadoopRDD.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaNewHadoopRDD.html)[JavaNewHadoopRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaNewHadoopRDD.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD$.html) [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html)[JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD$.html) [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html)[JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDDLike.html "Defines operations common to several Java RDD implementations.")[JavaRDDLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDDLike.html "Defines operations common to several Java RDD implementations.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaSparkContext$.html) [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaSparkContext.html "A Java-friendly version of org.apache.spark.SparkContext that returns org.apache.spark.api.java.JavaRDDs and works with Java collections instead of Scala ones.")[JavaSparkContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaSparkContext.html "A Java-friendly version of org.apache.spark.SparkContext that returns org.apache.spark.api.java.JavaRDDs and works with Java collections instead of Scala ones.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaSparkStatusTracker.html "Low-level status reporting APIs for monitoring job and stage progress.")[JavaSparkStatusTracker](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaSparkStatusTracker.html "Low-level status reporting APIs for monitoring job and stage progress.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/Optional.html "Like java.util.Optional in Java 8, scala.Option in Scala, and com.google.common.base.Optional in Google Guava, this class represents a value of a given type that may or may not exist.")[Optional](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/Optional.html "Like java.util.Optional in Java 8, scala.Option in Scala, and com.google.common.base.Optional in Google Guava, this class represents a value of a given type that may or may not exist.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/StorageLevels.html "Expose some commonly useful storage level constants.")[StorageLevels](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/StorageLevels.html "Expose some commonly useful storage level constants.")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/plugin/index.html "Permalink") package [plugin](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/plugin/index.html)

Definition Classes
    [api](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/index.html "org.apache.spark.api")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/resource/index.html "Permalink") package [resource](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/resource/index.html)

Definition Classes
    [api](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/index.html "org.apache.spark.api")

p
[org](https://spark.apache.org/docs/latest/api/scala/org/index.html "org").[apache](https://spark.apache.org/docs/latest/api/scala/org/apache/index.html "org.apache").[spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark").[api](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/index.html "org.apache.spark.api")
# java[ __](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/index.html "Permalink")
####  package java
Spark Java programming APIs.

Source
    [package.scala](https://github.com/apache/spark/tree/v4.1.2/core/src/main/scala/org/apache/spark/api/java/package.scala)
Linear Supertypes
AnyRef, Any
__ __
Ordering
  1. Alphabetic
  2. By Inheritance

Inherited

  1. java
  2. AnyRef
  3. Any

  1. Hide All
  2. Show All

Visibility
  1. Public
  2. Protected

### Package Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/index.html "Permalink") package [function](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/index.html "Set of interfaces to represent functions in Spark's Java API.")
Set of interfaces to represent functions in Spark's Java API.
Set of interfaces to represent functions in Spark's Java API. Users create implementations of these interfaces to pass functions to various Java API methods for Spark. Please visit Spark's Java programming guide for more details.

### Type Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaDoubleRDD.html "Permalink") class [JavaDoubleRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaDoubleRDD.html) extends AbstractJavaRDDLike[[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html#java.lang.Double "java.lang.Double"), [JavaDoubleRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaDoubleRDD.html "org.apache.spark.api.java.JavaDoubleRDD")]
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaFutureAction.html "Permalink") trait [JavaFutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaFutureAction.html)[T] extends [Future](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/Future.html#java.util.concurrent.Future "java.util.concurrent.Future")[T]
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaHadoopRDD.html "Permalink") class [JavaHadoopRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaHadoopRDD.html)[K, V] extends [JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K, V]

Annotations
     @DeveloperApi()
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaNewHadoopRDD.html "Permalink") class [JavaNewHadoopRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaNewHadoopRDD.html)[K, V] extends [JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K, V]

Annotations
     @DeveloperApi()
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "Permalink") class [JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html)[K, V] extends AbstractJavaRDDLike[(K, V), [JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K, V]]
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "Permalink") class [JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html)[T] extends AbstractJavaRDDLike[T, [JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[T]]
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDDLike.html "Permalink") trait [JavaRDDLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDDLike.html "Defines operations common to several Java RDD implementations.")[T, This <: [JavaRDDLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDDLike.html "org.apache.spark.api.java.JavaRDDLike")[T, This]] extends Serializable
Defines operations common to several Java RDD implementations.
Defines operations common to several Java RDD implementations.

Note

This trait is not intended to be implemented by user code.
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaSparkContext.html "Permalink") class [JavaSparkContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaSparkContext.html "A Java-friendly version of org.apache.spark.SparkContext that returns org.apache.spark.api.java.JavaRDDs and works with Java collections instead of Scala ones.") extends [Closeable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Closeable.html#java.io.Closeable "java.io.Closeable")
A Java-friendly version of [org.apache.spark.SparkContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html "org.apache.spark.SparkContext") that returns [org.apache.spark.api.java.JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")s and works with Java collections instead of Scala ones.
A Java-friendly version of [org.apache.spark.SparkContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html "org.apache.spark.SparkContext") that returns [org.apache.spark.api.java.JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")s and works with Java collections instead of Scala ones.

Note

Only one `SparkContext` should be active per JVM. You must `stop()` the active `SparkContext` before creating a new one.
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaSparkStatusTracker.html "Permalink") class [JavaSparkStatusTracker](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaSparkStatusTracker.html "Low-level status reporting APIs for monitoring job and stage progress.") extends AnyRef
Low-level status reporting APIs for monitoring job and stage progress.
Low-level status reporting APIs for monitoring job and stage progress.
These APIs intentionally provide very weak consistency semantics; consumers of these APIs should be prepared to handle empty / missing information. For example, a job's stage ids may be known but the status API may not have any information about the details of those stages, so `getStageInfo` could potentially return `null` for a valid stage id.
To limit memory usage, these APIs only provide information on recent jobs / stages. These APIs will provide information for the last `spark.ui.retainedStages` stages and `spark.ui.retainedJobs` jobs.

Note

This class's constructor should be considered private and may be subject to change.
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/Optional.html "Permalink") final  class [Optional](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/Optional.html "Like java.util.Optional in Java 8, scala.Option in Scala, and com.google.common.base.Optional in Google Guava, this class represents a value of a given type that may or may not exist.")[T] extends [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable")
Like `java.util.Optional` in Java 8, `scala.Option` in Scala, and `com.google.common.base.Optional` in Google Guava, this class represents a value of a given type that may or may not exist.
Like `java.util.Optional` in Java 8, `scala.Option` in Scala, and `com.google.common.base.Optional` in Google Guava, this class represents a value of a given type that may or may not exist. It is used in methods that wish to optionally return a value, in preference to returning `null`.
In fact, the class here is a reimplementation of the essential API of both `java.util.Optional` and `com.google.common.base.Optional`. From `java.util.Optional`, it implements:
     * `#empty()`
     * `#of(Object)`
     * `#ofNullable(Object)`
     * `#get()`
     * `#orElse(Object)`
     * `#isPresent()`
From `com.google.common.base.Optional` it implements:
     * `#absent()`
     * `#of(Object)`
     * `#fromNullable(Object)`
     * `#get()`
     * `#or(Object)`
     * `#orNull()`
     * `#isPresent()`
`java.util.Optional` itself was not used because at the time, the project did not require Java 8. Using `com.google.common.base.Optional` has in the past caused serious library version conflicts with Guava that can't be resolved by shading. Hence this work-alike clone.
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/StorageLevels.html "Permalink") class [StorageLevels](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/StorageLevels.html "Expose some commonly useful storage level constants.") extends AnyRef
Expose some commonly useful storage level constants.

### Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaDoubleRDD$.html "Permalink") object [JavaDoubleRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaDoubleRDD$.html) extends [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable")
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD$.html "Permalink") object [JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD$.html) extends [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable")
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD$.html "Permalink") object [JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD$.html) extends [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable")
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaSparkContext$.html "Permalink") object [JavaSparkContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaSparkContext$.html)

### Ungrouped
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaDoubleRDD.html "Permalink") class [JavaDoubleRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaDoubleRDD.html) extends AbstractJavaRDDLike[[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html#java.lang.Double "java.lang.Double"), [JavaDoubleRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaDoubleRDD.html "org.apache.spark.api.java.JavaDoubleRDD")]
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaFutureAction.html "Permalink") trait [JavaFutureAction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaFutureAction.html)[T] extends [Future](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/Future.html#java.util.concurrent.Future "java.util.concurrent.Future")[T]
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaHadoopRDD.html "Permalink") class [JavaHadoopRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaHadoopRDD.html)[K, V] extends [JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K, V]

Annotations
     @DeveloperApi()
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaNewHadoopRDD.html "Permalink") class [JavaNewHadoopRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaNewHadoopRDD.html)[K, V] extends [JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K, V]

Annotations
     @DeveloperApi()
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "Permalink") class [JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html)[K, V] extends AbstractJavaRDDLike[(K, V), [JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD.html "org.apache.spark.api.java.JavaPairRDD")[K, V]]
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "Permalink") class [JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html)[T] extends AbstractJavaRDDLike[T, [JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[T]]
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDDLike.html "Permalink") trait [JavaRDDLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDDLike.html "Defines operations common to several Java RDD implementations.")[T, This <: [JavaRDDLike](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDDLike.html "org.apache.spark.api.java.JavaRDDLike")[T, This]] extends Serializable
Defines operations common to several Java RDD implementations.
Defines operations common to several Java RDD implementations.

Note

This trait is not intended to be implemented by user code.
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaSparkContext.html "Permalink") class [JavaSparkContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaSparkContext.html "A Java-friendly version of org.apache.spark.SparkContext that returns org.apache.spark.api.java.JavaRDDs and works with Java collections instead of Scala ones.") extends [Closeable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Closeable.html#java.io.Closeable "java.io.Closeable")
A Java-friendly version of [org.apache.spark.SparkContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html "org.apache.spark.SparkContext") that returns [org.apache.spark.api.java.JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")s and works with Java collections instead of Scala ones.
A Java-friendly version of [org.apache.spark.SparkContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html "org.apache.spark.SparkContext") that returns [org.apache.spark.api.java.JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")s and works with Java collections instead of Scala ones.

Note

Only one `SparkContext` should be active per JVM. You must `stop()` the active `SparkContext` before creating a new one.
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaSparkStatusTracker.html "Permalink") class [JavaSparkStatusTracker](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaSparkStatusTracker.html "Low-level status reporting APIs for monitoring job and stage progress.") extends AnyRef
Low-level status reporting APIs for monitoring job and stage progress.
Low-level status reporting APIs for monitoring job and stage progress.
These APIs intentionally provide very weak consistency semantics; consumers of these APIs should be prepared to handle empty / missing information. For example, a job's stage ids may be known but the status API may not have any information about the details of those stages, so `getStageInfo` could potentially return `null` for a valid stage id.
To limit memory usage, these APIs only provide information on recent jobs / stages. These APIs will provide information for the last `spark.ui.retainedStages` stages and `spark.ui.retainedJobs` jobs.

Note

This class's constructor should be considered private and may be subject to change.
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/Optional.html "Permalink") final  class [Optional](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/Optional.html "Like java.util.Optional in Java 8, scala.Option in Scala, and com.google.common.base.Optional in Google Guava, this class represents a value of a given type that may or may not exist.")[T] extends [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable")
Like `java.util.Optional` in Java 8, `scala.Option` in Scala, and `com.google.common.base.Optional` in Google Guava, this class represents a value of a given type that may or may not exist.
Like `java.util.Optional` in Java 8, `scala.Option` in Scala, and `com.google.common.base.Optional` in Google Guava, this class represents a value of a given type that may or may not exist. It is used in methods that wish to optionally return a value, in preference to returning `null`.
In fact, the class here is a reimplementation of the essential API of both `java.util.Optional` and `com.google.common.base.Optional`. From `java.util.Optional`, it implements:
     * `#empty()`
     * `#of(Object)`
     * `#ofNullable(Object)`
     * `#get()`
     * `#orElse(Object)`
     * `#isPresent()`
From `com.google.common.base.Optional` it implements:
     * `#absent()`
     * `#of(Object)`
     * `#fromNullable(Object)`
     * `#get()`
     * `#or(Object)`
     * `#orNull()`
     * `#isPresent()`
`java.util.Optional` itself was not used because at the time, the project did not require Java 8. Using `com.google.common.base.Optional` has in the past caused serious library version conflicts with Guava that can't be resolved by shading. Hence this work-alike clone.
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/StorageLevels.html "Permalink") class [StorageLevels](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/StorageLevels.html "Expose some commonly useful storage level constants.") extends AnyRef
Expose some commonly useful storage level constants.

  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaDoubleRDD$.html "Permalink") object [JavaDoubleRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaDoubleRDD$.html) extends [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable")
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD$.html "Permalink") object [JavaPairRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaPairRDD$.html) extends [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable")
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD$.html "Permalink") object [JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD$.html) extends [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable")
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaSparkContext$.html "Permalink") object [JavaSparkContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaSparkContext$.html)
