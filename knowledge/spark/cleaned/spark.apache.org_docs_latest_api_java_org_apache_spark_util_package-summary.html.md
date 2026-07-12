[Skip navigation links](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/package-summary.html#skip-navbar-top "Skip navigation links")
  * [Overview](https://spark.apache.org/docs/latest/api/java/index.html)
  * Package
  * Class
  * [Deprecated](https://spark.apache.org/docs/latest/api/java/deprecated-list.html)
  * [Index](https://spark.apache.org/docs/latest/api/java/index-all.html)
  * [Help](https://spark.apache.org/docs/latest/api/java/help-doc.html#package)

  * Package:
  * [Description](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/package-summary.html#package-description) |
  * [Related Packages](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/package-summary.html#related-package-summary) |
  * [Classes and Interfaces](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/package-summary.html#class-summary)

SEARCH:
# Package org.apache.spark.util
* * *
package org.apache.spark.util
Spark utilities.
  * Related Packages
Package
Description
[org.apache.spark](https://spark.apache.org/docs/latest/api/java/org/apache/spark/package-summary.html)
Core Spark classes in Scala.
[org.apache.spark.util.logging](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/logging/package-summary.html)
[org.apache.spark.util.random](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/random/package-summary.html)
Utilities for random number generation.
[org.apache.spark.util.sketch](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/sketch/package-summary.html)
  * All Classes and InterfacesInterfacesClassesRecord ClassesExceptions
Class
Description
[AccumulatorContext](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/AccumulatorContext.html "class in org.apache.spark.util")
An internal class used to track accumulators by Spark itself.
[AccumulatorV2](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/AccumulatorV2.html "class in org.apache.spark.util")<IN,OUT>
The base class for accumulators, that can accumulate inputs of type `IN`, and produce output of type `OUT`.
[ArrayImplicits](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/ArrayImplicits.html "class in org.apache.spark.util")
Implicit methods related to Scala Array.
[ArrayImplicits.SparkArrayOps](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/ArrayImplicits.SparkArrayOps.html "class in org.apache.spark.util")<T>
[CausedBy](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/CausedBy.html "class in org.apache.spark.util")
Extractor Object for pulling out the root cause of an error.
[ChildFirstURLClassLoader](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/ChildFirstURLClassLoader.html "class in org.apache.spark.util")
A mutable class loader that gives preference to its own URLs over the parent class loader when loading classes and resources.
[Clock](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/Clock.html "interface in org.apache.spark.util")
An interface to represent clocks, so that they can be mocked out in unit tests.
[ClosureCleaner](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/ClosureCleaner.html "class in org.apache.spark.util")
A cleaner that renders closures serializable if they can be done so safely.
[CollectionAccumulator](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/CollectionAccumulator.html "class in org.apache.spark.util")<T>
An [`accumulator`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/AccumulatorV2.html "class in org.apache.spark.util") for collecting a list of elements.
[CollectionsUtils](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/CollectionsUtils.html "class in org.apache.spark.util")
[CommandLineLoggingUtils](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/CommandLineLoggingUtils.html "interface in org.apache.spark.util")
[CommandLineUtils](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/CommandLineUtils.html "interface in org.apache.spark.util")
Contains basic command line parsing functionality and methods to parse some common Spark CLI options.
[DependencyUtils](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/DependencyUtils.html "class in org.apache.spark.util")
[DoubleAccumulator](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/DoubleAccumulator.html "class in org.apache.spark.util")
An [`accumulator`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/AccumulatorV2.html "class in org.apache.spark.util") for computing sum, count, and averages for double precision floating numbers.
[EnumUtil](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/EnumUtil.html "class in org.apache.spark.util")
[ExposedBufferByteArrayOutputStream](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/ExposedBufferByteArrayOutputStream.html "class in org.apache.spark.util")
Subclass of ByteArrayOutputStream that exposes `buf` directly.
[HadoopFSUtils](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/HadoopFSUtils.html "class in org.apache.spark.util")
Utility functions to simplify and speed-up file listing.
[IndylambdaScalaClosures](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/IndylambdaScalaClosures.html "class in org.apache.spark.util")
[InnerClosureFinder](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/InnerClosureFinder.html "class in org.apache.spark.util")
[IntParam](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/IntParam.html "class in org.apache.spark.util")
An extractor object for parsing strings into integers.
[JsonProtocol](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/JsonProtocol.html "class in org.apache.spark.util")
Serializes SparkListener events to/from JSON.
[JsonUtils](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/JsonUtils.html "interface in org.apache.spark.util")
[KnownSizeEstimation](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/KnownSizeEstimation.html "interface in org.apache.spark.util")
A trait that allows a class to give [`SizeEstimator`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/SizeEstimator.html "class in org.apache.spark.util") more accurate size estimation.
[LexicalThreadLocal](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/LexicalThreadLocal.html "interface in org.apache.spark.util")<T>
Helper trait for defining thread locals with lexical scoping.
[LexicalThreadLocal.Handle](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/LexicalThreadLocal.Handle.html "class in org.apache.spark.util")
Final class representing a handle to a thread local value.
[ListenerBus](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/ListenerBus.html "interface in org.apache.spark.util")<L,E>
An event bus which posts events to its listeners.
[LogUtils](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/LogUtils.html "class in org.apache.spark.util")
:: : DeveloperApi :: Utils for querying Spark logs with Spark SQL.
[LongAccumulator](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/LongAccumulator.html "class in org.apache.spark.util")
An [`accumulator`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/AccumulatorV2.html "class in org.apache.spark.util") for computing sum, count, and average of 64-bit integers.
[MavenUtils](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/MavenUtils.html "class in org.apache.spark.util")
Provides utility functions to be used inside SparkSubmit.
[MavenUtils.MavenCoordinate$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/MavenUtils.MavenCoordinate$.html "class in org.apache.spark.util")
[MemoryParam](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/MemoryParam.html "class in org.apache.spark.util")
An extractor object for parsing JVM memory strings, such as "10g", into an Int representing the number of megabytes.
[MethodIdentifier](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/MethodIdentifier.html "class in org.apache.spark.util")<T>
Helper class to identify a method.
[MetricUtils](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/MetricUtils.html "class in org.apache.spark.util")
[MutablePair](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/MutablePair.html "class in org.apache.spark.util")<T1,T2>
Developer API A tuple of 2 elements.
[MutableURLClassLoader](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/MutableURLClassLoader.html "class in org.apache.spark.util")
URL class loader that exposes the `addURL` method in URLClassLoader.
[Pair](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/Pair.html "class in org.apache.spark.util")<L,R>
An immutable pair of values.
[ParentClassLoader](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/ParentClassLoader.html "class in org.apache.spark.util")
A class loader which makes some protected methods in ClassLoader accessible.
[ReturnStatementFinder](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/ReturnStatementFinder.html "class in org.apache.spark.util")
[RpcUtils](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/RpcUtils.html "class in org.apache.spark.util")
[SecurityUtils](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/SecurityUtils.html "class in org.apache.spark.util")
Various utility methods used by Spark Security.
[SerializableConfiguration](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/SerializableConfiguration.html "class in org.apache.spark.util")
Hadoop configuration but serializable.
[ShutdownHookManager](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/ShutdownHookManager.html "class in org.apache.spark.util")
Various utility methods used by Spark.
[SignalUtils](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/SignalUtils.html "class in org.apache.spark.util")
Contains utilities for working with posix signals.
[SizeEstimator](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/SizeEstimator.html "class in org.apache.spark.util")
Developer API Estimates the sizes of Java objects (number of bytes of memory they occupy), for use in memory-aware caches.
[SparkClassUtils](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/SparkClassUtils.html "interface in org.apache.spark.util")
[SparkClosureCleaner](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/SparkClosureCleaner.html "class in org.apache.spark.util")
[SparkCollectionUtils](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/SparkCollectionUtils.html "interface in org.apache.spark.util")
[SparkEnvUtils](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/SparkEnvUtils.html "interface in org.apache.spark.util")
[SparkErrorUtils](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/SparkErrorUtils.html "interface in org.apache.spark.util")
[SparkExitCode](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/SparkExitCode.html "class in org.apache.spark.util")
[SparkFileUtils](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/SparkFileUtils.html "interface in org.apache.spark.util")
[SparkSchemaUtils](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/SparkSchemaUtils.html "class in org.apache.spark.util")
Utils for handling schemas.
[SparkSerDeUtils](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/SparkSerDeUtils.html "interface in org.apache.spark.util")
[SparkShutdownHook](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/SparkShutdownHook.html "class in org.apache.spark.util")
[SparkStreamUtils](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/SparkStreamUtils.html "interface in org.apache.spark.util")
[SparkStringUtils](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/SparkStringUtils.html "interface in org.apache.spark.util")
[SparkSystemUtils](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/SparkSystemUtils.html "interface in org.apache.spark.util")
[SparkTestUtils](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/SparkTestUtils.html "interface in org.apache.spark.util")
[SparkTestUtils.JavaSourceFromString](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/SparkTestUtils.JavaSourceFromString.html "class in org.apache.spark.util")
[SparkThreadUtils](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/SparkThreadUtils.html "class in org.apache.spark.util")
[StatCounter](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/StatCounter.html "class in org.apache.spark.util")
A class for tracking the statistics of a set of numbers (count, mean and variance) in a numerically robust way.
[TaskCompletionListener](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/TaskCompletionListener.html "interface in org.apache.spark.util")
Developer API
[TaskFailureListener](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/TaskFailureListener.html "interface in org.apache.spark.util")
Developer API
[ThreadUtils](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/ThreadUtils.html "class in org.apache.spark.util")
[Utils](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/Utils.html "class in org.apache.spark.util")
Various utility methods used by Spark.
[Utils.OriginalTryStackTraceException](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/Utils.OriginalTryStackTraceException.html "class in org.apache.spark.util")
[VersionUtils](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/VersionUtils.html "class in org.apache.spark.util")
Utilities for working with Spark version strings
