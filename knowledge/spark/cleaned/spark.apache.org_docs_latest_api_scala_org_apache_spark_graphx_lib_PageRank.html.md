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
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html "Permalink") package [graphx](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html "ALPHA COMPONENT GraphX is a graph processing framework built on top of Spark.")
ALPHA COMPONENT GraphX is a graph processing framework built on top of Spark.
ALPHA COMPONENT GraphX is a graph processing framework built on top of Spark.

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/index.html "Permalink") package [lib](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/index.html "Various analytics functions for graphs.")
Various analytics functions for graphs.
Various analytics functions for graphs.

Definition Classes
    [graphx](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html "org.apache.spark.graphx")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/ConnectedComponents$.html "Connected components algorithm.")[ConnectedComponents](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/ConnectedComponents$.html "Connected components algorithm.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/LabelPropagation$.html "Label Propagation algorithm.")[LabelPropagation](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/LabelPropagation$.html "Label Propagation algorithm.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html "PageRank algorithm implementation.")[PageRank](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html "PageRank algorithm implementation.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/SVDPlusPlus$.html "Implementation of SVD++ algorithm.")[SVDPlusPlus](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/SVDPlusPlus$.html "Implementation of SVD++ algorithm.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/ShortestPaths$.html "Computes shortest paths to the given set of landmark vertices, returning a graph where each vertex attribute is a map containing the shortest-path distance to each reachable landmark.")[ShortestPaths](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/ShortestPaths$.html "Computes shortest paths to the given set of landmark vertices, returning a graph where each vertex attribute is a map containing the shortest-path distance to each reachable landmark.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/StronglyConnectedComponents$.html "Strongly connected components algorithm implementation.")[StronglyConnectedComponents](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/StronglyConnectedComponents$.html "Strongly connected components algorithm implementation.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/TriangleCount$.html "Compute the number of triangles passing through each vertex.")[TriangleCount](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/TriangleCount$.html "Compute the number of triangles passing through each vertex.")

o
[org](https://spark.apache.org/docs/latest/api/scala/org/index.html "org").[apache](https://spark.apache.org/docs/latest/api/scala/org/apache/index.html "org.apache").[spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark").[graphx](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html "org.apache.spark.graphx").[lib](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/index.html "org.apache.spark.graphx.lib")
# PageRank[ __](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html "Permalink")
####  object PageRank extends Logging
PageRank algorithm implementation. There are two implementations of PageRank implemented.
The first implementation uses the standalone `Graph` interface and runs PageRank for a fixed number of iterations:

```
var PR = Array.fill(n)( 1.0 )
val oldPR = Array.fill(n)( 1.0 )
for( iter <- 0 until numIter ) {
  swap(oldPR, PR)
  for( i <- 0 until n ) {
    PR[i] = alpha + (1 - alpha) * inNbrs[i].map(j => oldPR[j] / outDeg[j]).sum
  }
}
```

The second implementation uses the `Pregel` interface and runs PageRank until convergence:

```
var PR = Array.fill(n)( 1.0 )
val oldPR = Array.fill(n)( 0.0 )
while( max(abs(PR - oldPr)) > tol ) {
  swap(oldPR, PR)
  for( i <- 0 until n if abs(PR[i] - oldPR[i]) > tol ) {
    PR[i] = alpha + (1 - \alpha) * inNbrs[i].map(j => oldPR[j] / outDeg[j]).sum
  }
}
```

`alpha` is the random reset probability (typically 0.15), `inNbrs[i]` is the set of neighbors which link to `i` and `outDeg[j]` is the out degree of vertex `j`.

Source
    [PageRank.scala](https://github.com/apache/spark/tree/v4.1.2/graphx/src/main/scala/org/apache/spark/graphx/lib/PageRank.scala)

Note

This is not the "normalized" PageRank and as a consequence pages that have no inlinks will have a PageRank of alpha.
Linear Supertypes
Logging, AnyRef, Any
__ __
Ordering
  1. Alphabetic
  2. By Inheritance

Inherited

  1. PageRank
  2. Logging
  3. AnyRef
  4. Any

  1. Hide All
  2. Show All

Visibility
  1. Public
  2. Protected

### Type Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#LogStringContextextendsAnyRef "Permalink") implicit  class LogStringContext extends AnyRef

Definition Classes
    Logging

### Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html###:Int "Permalink") final  def ##: Int

Definition Classes
    AnyRef → Any
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#MDC\(key:org.apache.spark.internal.LogKey,value:Any\):org.apache.spark.internal.MDC "Permalink") def MDC(key: LogKey, value: Any): MDC

Attributes
    protected

Definition Classes
    Logging
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0

Definition Classes
    Any
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#clone\(\):Object "Permalink") def clone(): AnyRef

Attributes
    protected[lang]

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#equals\(x$1:Object\):Boolean "Permalink") def equals(arg0: AnyRef): Boolean

Definition Classes
    AnyRef → Any
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef]

Definition Classes
    AnyRef → Any

Annotations
     @IntrinsicCandidate() @native()
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#hashCode\(\):Int "Permalink") def hashCode(): Int

Definition Classes
    AnyRef → Any

Annotations
     @IntrinsicCandidate() @native()
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#initializeLogIfNecessary\(isInterpreter:Boolean,silent:Boolean\):Boolean "Permalink") def initializeLogIfNecessary(isInterpreter: Boolean, silent: Boolean): Boolean

Attributes
    protected

Definition Classes
    Logging
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#initializeLogIfNecessary\(isInterpreter:Boolean\):Unit "Permalink") def initializeLogIfNecessary(isInterpreter: Boolean): Unit

Attributes
    protected

Definition Classes
    Logging
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean

Definition Classes
    Any
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#isTraceEnabled\(\):Boolean "Permalink") def isTraceEnabled(): Boolean

Attributes
    protected

Definition Classes
    Logging
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#log:org.slf4j.Logger "Permalink") def log: Logger

Attributes
    protected

Definition Classes
    Logging
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#logBasedOnLevel\(level:org.slf4j.event.Level\)\(f:=>org.apache.spark.internal.MessageWithContext\):Unit "Permalink") def logBasedOnLevel(level: Level)(f: => MessageWithContext): Unit

Attributes
    protected

Definition Classes
    Logging
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#logDebug\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logDebug(msg: => String, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#logDebug\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logDebug(entry: LogEntry, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#logDebug\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logDebug(entry: LogEntry): Unit

Attributes
    protected

Definition Classes
    Logging
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#logDebug\(msg:=>String\):Unit "Permalink") def logDebug(msg: => String): Unit

Attributes
    protected

Definition Classes
    Logging
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#logError\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logError(msg: => String, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#logError\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logError(entry: LogEntry, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  23. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#logError\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logError(entry: LogEntry): Unit

Attributes
    protected

Definition Classes
    Logging
  24. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#logError\(msg:=>String\):Unit "Permalink") def logError(msg: => String): Unit

Attributes
    protected

Definition Classes
    Logging
  25. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#logInfo\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logInfo(msg: => String, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  26. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#logInfo\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logInfo(entry: LogEntry, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  27. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#logInfo\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logInfo(entry: LogEntry): Unit

Attributes
    protected

Definition Classes
    Logging
  28. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#logInfo\(msg:=>String\):Unit "Permalink") def logInfo(msg: => String): Unit

Attributes
    protected

Definition Classes
    Logging
  29. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#logName:String "Permalink") def logName: [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String")

Attributes
    protected

Definition Classes
    Logging
  30. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#logTrace\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logTrace(msg: => String, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  31. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#logTrace\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logTrace(entry: LogEntry, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  32. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#logTrace\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logTrace(entry: LogEntry): Unit

Attributes
    protected

Definition Classes
    Logging
  33. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#logTrace\(msg:=>String\):Unit "Permalink") def logTrace(msg: => String): Unit

Attributes
    protected

Definition Classes
    Logging
  34. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#logWarning\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logWarning(msg: => String, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  35. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#logWarning\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logWarning(entry: LogEntry, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  36. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#logWarning\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logWarning(entry: LogEntry): Unit

Attributes
    protected

Definition Classes
    Logging
  37. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#logWarning\(msg:=>String\):Unit "Permalink") def logWarning(msg: => String): Unit

Attributes
    protected

Definition Classes
    Logging
  38. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  39. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#notify\(\):Unit "Permalink") final  def notify(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  40. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  41. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#run\[VD,ED\]\(graph:org.apache.spark.graphx.Graph\[VD,ED\],numIter:Int,resetProb:Double\)\(implicitevidence$1:scala.reflect.ClassTag\[VD\],implicitevidence$2:scala.reflect.ClassTag\[ED\]\):org.apache.spark.graphx.Graph\[Double,Double\] "Permalink") def run[VD, ED](graph: [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[VD, ED], numIter: Int, resetProb: Double = 0.15)(implicit arg0: ClassTag[VD], arg1: ClassTag[ED]): [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[Double, Double]
Run PageRank for a fixed number of iterations returning a graph with vertex attributes containing the PageRank and edge attributes the normalized edge weight.
Run PageRank for a fixed number of iterations returning a graph with vertex attributes containing the PageRank and edge attributes the normalized edge weight.

VD

the original vertex attribute (not used)

ED

the original edge attribute (not used)

graph

the graph on which to compute PageRank

numIter

the number of iterations of PageRank to run

resetProb

the random reset probability (alpha)

returns

the graph containing with each vertex containing the PageRank and each edge containing the normalized weight.
  42. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#runParallelPersonalizedPageRank\[VD,ED\]\(graph:org.apache.spark.graphx.Graph\[VD,ED\],numIter:Int,resetProb:Double,sources:Array\[org.apache.spark.graphx.VertexId\]\)\(implicitevidence$11:scala.reflect.ClassTag\[VD\],implicitevidence$12:scala.reflect.ClassTag\[ED\]\):org.apache.spark.graphx.Graph\[org.apache.spark.ml.linalg.Vector,Double\] "Permalink") def runParallelPersonalizedPageRank[VD, ED](graph: [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[VD, ED], numIter: Int, resetProb: Double = 0.15, sources: Array[[VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long)])(implicit arg0: ClassTag[VD], arg1: ClassTag[ED]): [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[[Vector](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/linalg/Vector.html "org.apache.spark.ml.linalg.Vector"), Double]
Run Personalized PageRank for a fixed number of iterations, for a set of starting nodes in parallel.
Run Personalized PageRank for a fixed number of iterations, for a set of starting nodes in parallel. Returns a graph with vertex attributes containing the pagerank relative to all starting nodes (as a sparse vector) and edge attributes the normalized edge weight

VD

The original vertex attribute (not used)

ED

The original edge attribute (not used)

graph

The graph on which to compute personalized pagerank

numIter

The number of iterations to run

resetProb

The random reset probability

sources

The list of sources to compute personalized pagerank from

returns

the graph with vertex attributes containing the pagerank relative to all starting nodes (as a sparse vector indexed by the position of nodes in the sources list) and edge attributes the normalized edge weight
  43. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#runUntilConvergence\[VD,ED\]\(graph:org.apache.spark.graphx.Graph\[VD,ED\],tol:Double,resetProb:Double\)\(implicitevidence$13:scala.reflect.ClassTag\[VD\],implicitevidence$14:scala.reflect.ClassTag\[ED\]\):org.apache.spark.graphx.Graph\[Double,Double\] "Permalink") def runUntilConvergence[VD, ED](graph: [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[VD, ED], tol: Double, resetProb: Double = 0.15)(implicit arg0: ClassTag[VD], arg1: ClassTag[ED]): [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[Double, Double]
Run a dynamic version of PageRank returning a graph with vertex attributes containing the PageRank and edge attributes containing the normalized edge weight.
Run a dynamic version of PageRank returning a graph with vertex attributes containing the PageRank and edge attributes containing the normalized edge weight.

VD

the original vertex attribute (not used)

ED

the original edge attribute (not used)

graph

the graph on which to compute PageRank

tol

the tolerance allowed at convergence (smaller => more accurate).

resetProb

the random reset probability (alpha)

returns

the graph containing with each vertex containing the PageRank and each edge containing the normalized weight.
  44. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#runUntilConvergenceWithOptions\[VD,ED\]\(graph:org.apache.spark.graphx.Graph\[VD,ED\],tol:Double,resetProb:Double,srcId:Option\[org.apache.spark.graphx.VertexId\]\)\(implicitevidence$15:scala.reflect.ClassTag\[VD\],implicitevidence$16:scala.reflect.ClassTag\[ED\]\):org.apache.spark.graphx.Graph\[Double,Double\] "Permalink") def runUntilConvergenceWithOptions[VD, ED](graph: [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[VD, ED], tol: Double, resetProb: Double = 0.15, srcId: Option[[VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long)] = None)(implicit arg0: ClassTag[VD], arg1: ClassTag[ED]): [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[Double, Double]
Run a dynamic version of PageRank returning a graph with vertex attributes containing the PageRank and edge attributes containing the normalized edge weight.
Run a dynamic version of PageRank returning a graph with vertex attributes containing the PageRank and edge attributes containing the normalized edge weight.

VD

the original vertex attribute (not used)

ED

the original edge attribute (not used)

graph

the graph on which to compute PageRank

tol

the tolerance allowed at convergence (smaller => more accurate).

resetProb

the random reset probability (alpha)

srcId

the source vertex for a Personalized Page Rank (optional)

returns

the graph containing with each vertex containing the PageRank and each edge containing the normalized weight.
  45. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#runWithOptions\[VD,ED\]\(graph:org.apache.spark.graphx.Graph\[VD,ED\],numIter:Int,resetProb:Double,srcId:Option\[org.apache.spark.graphx.VertexId\],normalized:Boolean\)\(implicitevidence$5:scala.reflect.ClassTag\[VD\],implicitevidence$6:scala.reflect.ClassTag\[ED\]\):org.apache.spark.graphx.Graph\[Double,Double\] "Permalink") def runWithOptions[VD, ED](graph: [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[VD, ED], numIter: Int, resetProb: Double, srcId: Option[[VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long)], normalized: Boolean)(implicit arg0: ClassTag[VD], arg1: ClassTag[ED]): [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[Double, Double]
Run PageRank for a fixed number of iterations returning a graph with vertex attributes containing the PageRank and edge attributes the normalized edge weight.
Run PageRank for a fixed number of iterations returning a graph with vertex attributes containing the PageRank and edge attributes the normalized edge weight.

VD

the original vertex attribute (not used)

ED

the original edge attribute (not used)

graph

the graph on which to compute PageRank

numIter

the number of iterations of PageRank to run

resetProb

the random reset probability (alpha)

srcId

the source vertex for a Personalized Page Rank (optional)

normalized

whether or not to normalize rank sum

returns

the graph containing with each vertex containing the PageRank and each edge containing the normalized weight.

Since

3.2.0
  46. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#runWithOptions\[VD,ED\]\(graph:org.apache.spark.graphx.Graph\[VD,ED\],numIter:Int,resetProb:Double,srcId:Option\[org.apache.spark.graphx.VertexId\]\)\(implicitevidence$3:scala.reflect.ClassTag\[VD\],implicitevidence$4:scala.reflect.ClassTag\[ED\]\):org.apache.spark.graphx.Graph\[Double,Double\] "Permalink") def runWithOptions[VD, ED](graph: [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[VD, ED], numIter: Int, resetProb: Double = 0.15, srcId: Option[[VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long)] = None)(implicit arg0: ClassTag[VD], arg1: ClassTag[ED]): [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[Double, Double]
Run PageRank for a fixed number of iterations returning a graph with vertex attributes containing the PageRank and edge attributes the normalized edge weight.
Run PageRank for a fixed number of iterations returning a graph with vertex attributes containing the PageRank and edge attributes the normalized edge weight.

VD

the original vertex attribute (not used)

ED

the original edge attribute (not used)

graph

the graph on which to compute PageRank

numIter

the number of iterations of PageRank to run

resetProb

the random reset probability (alpha)

srcId

the source vertex for a Personalized Page Rank (optional)

returns

the graph containing with each vertex containing the PageRank and each edge containing the normalized weight.
  47. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#runWithOptionsWithPreviousPageRank\[VD,ED\]\(graph:org.apache.spark.graphx.Graph\[VD,ED\],numIter:Int,resetProb:Double,srcId:Option\[org.apache.spark.graphx.VertexId\],normalized:Boolean,preRankGraph:org.apache.spark.graphx.Graph\[Double,Double\]\)\(implicitevidence$9:scala.reflect.ClassTag\[VD\],implicitevidence$10:scala.reflect.ClassTag\[ED\]\):org.apache.spark.graphx.Graph\[Double,Double\] "Permalink") def runWithOptionsWithPreviousPageRank[VD, ED](graph: [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[VD, ED], numIter: Int, resetProb: Double, srcId: Option[[VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long)], normalized: Boolean, preRankGraph: [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[Double, Double])(implicit arg0: ClassTag[VD], arg1: ClassTag[ED]): [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[Double, Double]
Run PageRank for a fixed number of iterations returning a graph with vertex attributes containing the PageRank and edge attributes the normalized edge weight.
Run PageRank for a fixed number of iterations returning a graph with vertex attributes containing the PageRank and edge attributes the normalized edge weight.

VD

the original vertex attribute (not used)

ED

the original edge attribute (not used)

graph

the graph on which to compute PageRank

numIter

the number of iterations of PageRank to run

resetProb

the random reset probability (alpha)

srcId

the source vertex for a Personalized Page Rank (optional)

normalized

whether or not to normalize rank sum

preRankGraph

PageRank graph from which to keep iterating

returns

the graph containing with each vertex containing the PageRank and each edge containing the normalized weight.

Since

3.2.0
  48. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#runWithOptionsWithPreviousPageRank\[VD,ED\]\(graph:org.apache.spark.graphx.Graph\[VD,ED\],numIter:Int,resetProb:Double,srcId:Option\[org.apache.spark.graphx.VertexId\],preRankGraph:org.apache.spark.graphx.Graph\[Double,Double\]\)\(implicitevidence$7:scala.reflect.ClassTag\[VD\],implicitevidence$8:scala.reflect.ClassTag\[ED\]\):org.apache.spark.graphx.Graph\[Double,Double\] "Permalink") def runWithOptionsWithPreviousPageRank[VD, ED](graph: [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[VD, ED], numIter: Int, resetProb: Double, srcId: Option[[VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long)], preRankGraph: [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[Double, Double])(implicit arg0: ClassTag[VD], arg1: ClassTag[ED]): [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[Double, Double]
Run PageRank for a fixed number of iterations returning a graph with vertex attributes containing the PageRank and edge attributes the normalized edge weight.
Run PageRank for a fixed number of iterations returning a graph with vertex attributes containing the PageRank and edge attributes the normalized edge weight.

VD

the original vertex attribute (not used)

ED

the original edge attribute (not used)

graph

the graph on which to compute PageRank

numIter

the number of iterations of PageRank to run

resetProb

the random reset probability (alpha)

srcId

the source vertex for a Personalized Page Rank (optional)

preRankGraph

PageRank graph from which to keep iterating

returns

the graph containing with each vertex containing the PageRank and each edge containing the normalized weight.
  49. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0

Definition Classes
    AnyRef
  50. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#toString\(\):String "Permalink") def toString(): [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String")

Definition Classes
    AnyRef → Any
  51. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])
  52. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  53. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#wait\(\):Unit "Permalink") final  def wait(): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])
  54. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#withLogContext\(context:java.util.Map\[String,String\]\)\(body:=>Unit\):Unit "Permalink") def withLogContext(context: [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#java.util.Map "java.util.Map")[String, String])(body: => Unit): Unit

Attributes
    protected

Definition Classes
    Logging

### Deprecated Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#finalize\(\):Unit "Permalink") def finalize(): Unit

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
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#MDC\(key:org.apache.spark.internal.LogKey,value:Any\):org.apache.spark.internal.MDC "Permalink") def MDC(key: LogKey, value: Any): MDC

Attributes
    protected

Definition Classes
    Logging
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#initializeLogIfNecessary\(isInterpreter:Boolean,silent:Boolean\):Boolean "Permalink") def initializeLogIfNecessary(isInterpreter: Boolean, silent: Boolean): Boolean

Attributes
    protected

Definition Classes
    Logging
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#initializeLogIfNecessary\(isInterpreter:Boolean\):Unit "Permalink") def initializeLogIfNecessary(isInterpreter: Boolean): Unit

Attributes
    protected

Definition Classes
    Logging
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#isTraceEnabled\(\):Boolean "Permalink") def isTraceEnabled(): Boolean

Attributes
    protected

Definition Classes
    Logging
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#log:org.slf4j.Logger "Permalink") def log: Logger

Attributes
    protected

Definition Classes
    Logging
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#logBasedOnLevel\(level:org.slf4j.event.Level\)\(f:=>org.apache.spark.internal.MessageWithContext\):Unit "Permalink") def logBasedOnLevel(level: Level)(f: => MessageWithContext): Unit

Attributes
    protected

Definition Classes
    Logging
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#logDebug\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logDebug(msg: => String, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#logDebug\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logDebug(entry: LogEntry, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#logDebug\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logDebug(entry: LogEntry): Unit

Attributes
    protected

Definition Classes
    Logging
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#logDebug\(msg:=>String\):Unit "Permalink") def logDebug(msg: => String): Unit

Attributes
    protected

Definition Classes
    Logging
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#logError\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logError(msg: => String, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#logError\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logError(entry: LogEntry, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#logError\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logError(entry: LogEntry): Unit

Attributes
    protected

Definition Classes
    Logging
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#logError\(msg:=>String\):Unit "Permalink") def logError(msg: => String): Unit

Attributes
    protected

Definition Classes
    Logging
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#logInfo\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logInfo(msg: => String, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#logInfo\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logInfo(entry: LogEntry, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#logInfo\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logInfo(entry: LogEntry): Unit

Attributes
    protected

Definition Classes
    Logging
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#logInfo\(msg:=>String\):Unit "Permalink") def logInfo(msg: => String): Unit

Attributes
    protected

Definition Classes
    Logging
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#logName:String "Permalink") def logName: [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String")

Attributes
    protected

Definition Classes
    Logging
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#logTrace\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logTrace(msg: => String, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#logTrace\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logTrace(entry: LogEntry, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#logTrace\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logTrace(entry: LogEntry): Unit

Attributes
    protected

Definition Classes
    Logging
  23. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#logTrace\(msg:=>String\):Unit "Permalink") def logTrace(msg: => String): Unit

Attributes
    protected

Definition Classes
    Logging
  24. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#logWarning\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logWarning(msg: => String, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  25. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#logWarning\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logWarning(entry: LogEntry, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  26. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#logWarning\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logWarning(entry: LogEntry): Unit

Attributes
    protected

Definition Classes
    Logging
  27. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#logWarning\(msg:=>String\):Unit "Permalink") def logWarning(msg: => String): Unit

Attributes
    protected

Definition Classes
    Logging
  28. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#withLogContext\(context:java.util.Map\[String,String\]\)\(body:=>Unit\):Unit "Permalink") def withLogContext(context: [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#java.util.Map "java.util.Map")[String, String])(body: => Unit): Unit

Attributes
    protected

Definition Classes
    Logging

### Inherited from AnyRef
### Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html###:Int "Permalink") final  def ##: Int

Definition Classes
    AnyRef → Any
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#clone\(\):Object "Permalink") def clone(): AnyRef

Attributes
    protected[lang]

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#equals\(x$1:Object\):Boolean "Permalink") def equals(arg0: AnyRef): Boolean

Definition Classes
    AnyRef → Any
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef]

Definition Classes
    AnyRef → Any

Annotations
     @IntrinsicCandidate() @native()
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#hashCode\(\):Int "Permalink") def hashCode(): Int

Definition Classes
    AnyRef → Any

Annotations
     @IntrinsicCandidate() @native()
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#notify\(\):Unit "Permalink") final  def notify(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0

Definition Classes
    AnyRef
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#toString\(\):String "Permalink") def toString(): [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String")

Definition Classes
    AnyRef → Any
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#wait\(\):Unit "Permalink") final  def wait(): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#finalize\(\):Unit "Permalink") def finalize(): Unit

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
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0

Definition Classes
    Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean

Definition Classes
    Any

### Ungrouped
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#LogStringContextextendsAnyRef "Permalink") implicit  class LogStringContext extends AnyRef

Definition Classes
    Logging

  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html###:Int "Permalink") final  def ##: Int

Definition Classes
    AnyRef → Any
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#MDC\(key:org.apache.spark.internal.LogKey,value:Any\):org.apache.spark.internal.MDC "Permalink") def MDC(key: LogKey, value: Any): MDC

Attributes
    protected

Definition Classes
    Logging
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0

Definition Classes
    Any
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#clone\(\):Object "Permalink") def clone(): AnyRef

Attributes
    protected[lang]

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#equals\(x$1:Object\):Boolean "Permalink") def equals(arg0: AnyRef): Boolean

Definition Classes
    AnyRef → Any
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef]

Definition Classes
    AnyRef → Any

Annotations
     @IntrinsicCandidate() @native()
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#hashCode\(\):Int "Permalink") def hashCode(): Int

Definition Classes
    AnyRef → Any

Annotations
     @IntrinsicCandidate() @native()
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#initializeLogIfNecessary\(isInterpreter:Boolean,silent:Boolean\):Boolean "Permalink") def initializeLogIfNecessary(isInterpreter: Boolean, silent: Boolean): Boolean

Attributes
    protected

Definition Classes
    Logging
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#initializeLogIfNecessary\(isInterpreter:Boolean\):Unit "Permalink") def initializeLogIfNecessary(isInterpreter: Boolean): Unit

Attributes
    protected

Definition Classes
    Logging
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean

Definition Classes
    Any
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#isTraceEnabled\(\):Boolean "Permalink") def isTraceEnabled(): Boolean

Attributes
    protected

Definition Classes
    Logging
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#log:org.slf4j.Logger "Permalink") def log: Logger

Attributes
    protected

Definition Classes
    Logging
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#logBasedOnLevel\(level:org.slf4j.event.Level\)\(f:=>org.apache.spark.internal.MessageWithContext\):Unit "Permalink") def logBasedOnLevel(level: Level)(f: => MessageWithContext): Unit

Attributes
    protected

Definition Classes
    Logging
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#logDebug\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logDebug(msg: => String, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#logDebug\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logDebug(entry: LogEntry, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#logDebug\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logDebug(entry: LogEntry): Unit

Attributes
    protected

Definition Classes
    Logging
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#logDebug\(msg:=>String\):Unit "Permalink") def logDebug(msg: => String): Unit

Attributes
    protected

Definition Classes
    Logging
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#logError\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logError(msg: => String, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#logError\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logError(entry: LogEntry, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  23. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#logError\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logError(entry: LogEntry): Unit

Attributes
    protected

Definition Classes
    Logging
  24. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#logError\(msg:=>String\):Unit "Permalink") def logError(msg: => String): Unit

Attributes
    protected

Definition Classes
    Logging
  25. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#logInfo\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logInfo(msg: => String, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  26. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#logInfo\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logInfo(entry: LogEntry, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  27. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#logInfo\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logInfo(entry: LogEntry): Unit

Attributes
    protected

Definition Classes
    Logging
  28. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#logInfo\(msg:=>String\):Unit "Permalink") def logInfo(msg: => String): Unit

Attributes
    protected

Definition Classes
    Logging
  29. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#logName:String "Permalink") def logName: [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String")

Attributes
    protected

Definition Classes
    Logging
  30. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#logTrace\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logTrace(msg: => String, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  31. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#logTrace\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logTrace(entry: LogEntry, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  32. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#logTrace\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logTrace(entry: LogEntry): Unit

Attributes
    protected

Definition Classes
    Logging
  33. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#logTrace\(msg:=>String\):Unit "Permalink") def logTrace(msg: => String): Unit

Attributes
    protected

Definition Classes
    Logging
  34. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#logWarning\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logWarning(msg: => String, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  35. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#logWarning\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logWarning(entry: LogEntry, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  36. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#logWarning\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logWarning(entry: LogEntry): Unit

Attributes
    protected

Definition Classes
    Logging
  37. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#logWarning\(msg:=>String\):Unit "Permalink") def logWarning(msg: => String): Unit

Attributes
    protected

Definition Classes
    Logging
  38. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  39. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#notify\(\):Unit "Permalink") final  def notify(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  40. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  41. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#run\[VD,ED\]\(graph:org.apache.spark.graphx.Graph\[VD,ED\],numIter:Int,resetProb:Double\)\(implicitevidence$1:scala.reflect.ClassTag\[VD\],implicitevidence$2:scala.reflect.ClassTag\[ED\]\):org.apache.spark.graphx.Graph\[Double,Double\] "Permalink") def run[VD, ED](graph: [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[VD, ED], numIter: Int, resetProb: Double = 0.15)(implicit arg0: ClassTag[VD], arg1: ClassTag[ED]): [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[Double, Double]
Run PageRank for a fixed number of iterations returning a graph with vertex attributes containing the PageRank and edge attributes the normalized edge weight.
Run PageRank for a fixed number of iterations returning a graph with vertex attributes containing the PageRank and edge attributes the normalized edge weight.

VD

the original vertex attribute (not used)

ED

the original edge attribute (not used)

graph

the graph on which to compute PageRank

numIter

the number of iterations of PageRank to run

resetProb

the random reset probability (alpha)

returns

the graph containing with each vertex containing the PageRank and each edge containing the normalized weight.
  42. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#runParallelPersonalizedPageRank\[VD,ED\]\(graph:org.apache.spark.graphx.Graph\[VD,ED\],numIter:Int,resetProb:Double,sources:Array\[org.apache.spark.graphx.VertexId\]\)\(implicitevidence$11:scala.reflect.ClassTag\[VD\],implicitevidence$12:scala.reflect.ClassTag\[ED\]\):org.apache.spark.graphx.Graph\[org.apache.spark.ml.linalg.Vector,Double\] "Permalink") def runParallelPersonalizedPageRank[VD, ED](graph: [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[VD, ED], numIter: Int, resetProb: Double = 0.15, sources: Array[[VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long)])(implicit arg0: ClassTag[VD], arg1: ClassTag[ED]): [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[[Vector](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/linalg/Vector.html "org.apache.spark.ml.linalg.Vector"), Double]
Run Personalized PageRank for a fixed number of iterations, for a set of starting nodes in parallel.
Run Personalized PageRank for a fixed number of iterations, for a set of starting nodes in parallel. Returns a graph with vertex attributes containing the pagerank relative to all starting nodes (as a sparse vector) and edge attributes the normalized edge weight

VD

The original vertex attribute (not used)

ED

The original edge attribute (not used)

graph

The graph on which to compute personalized pagerank

numIter

The number of iterations to run

resetProb

The random reset probability

sources

The list of sources to compute personalized pagerank from

returns

the graph with vertex attributes containing the pagerank relative to all starting nodes (as a sparse vector indexed by the position of nodes in the sources list) and edge attributes the normalized edge weight
  43. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#runUntilConvergence\[VD,ED\]\(graph:org.apache.spark.graphx.Graph\[VD,ED\],tol:Double,resetProb:Double\)\(implicitevidence$13:scala.reflect.ClassTag\[VD\],implicitevidence$14:scala.reflect.ClassTag\[ED\]\):org.apache.spark.graphx.Graph\[Double,Double\] "Permalink") def runUntilConvergence[VD, ED](graph: [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[VD, ED], tol: Double, resetProb: Double = 0.15)(implicit arg0: ClassTag[VD], arg1: ClassTag[ED]): [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[Double, Double]
Run a dynamic version of PageRank returning a graph with vertex attributes containing the PageRank and edge attributes containing the normalized edge weight.
Run a dynamic version of PageRank returning a graph with vertex attributes containing the PageRank and edge attributes containing the normalized edge weight.

VD

the original vertex attribute (not used)

ED

the original edge attribute (not used)

graph

the graph on which to compute PageRank

tol

the tolerance allowed at convergence (smaller => more accurate).

resetProb

the random reset probability (alpha)

returns

the graph containing with each vertex containing the PageRank and each edge containing the normalized weight.
  44. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#runUntilConvergenceWithOptions\[VD,ED\]\(graph:org.apache.spark.graphx.Graph\[VD,ED\],tol:Double,resetProb:Double,srcId:Option\[org.apache.spark.graphx.VertexId\]\)\(implicitevidence$15:scala.reflect.ClassTag\[VD\],implicitevidence$16:scala.reflect.ClassTag\[ED\]\):org.apache.spark.graphx.Graph\[Double,Double\] "Permalink") def runUntilConvergenceWithOptions[VD, ED](graph: [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[VD, ED], tol: Double, resetProb: Double = 0.15, srcId: Option[[VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long)] = None)(implicit arg0: ClassTag[VD], arg1: ClassTag[ED]): [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[Double, Double]
Run a dynamic version of PageRank returning a graph with vertex attributes containing the PageRank and edge attributes containing the normalized edge weight.
Run a dynamic version of PageRank returning a graph with vertex attributes containing the PageRank and edge attributes containing the normalized edge weight.

VD

the original vertex attribute (not used)

ED

the original edge attribute (not used)

graph

the graph on which to compute PageRank

tol

the tolerance allowed at convergence (smaller => more accurate).

resetProb

the random reset probability (alpha)

srcId

the source vertex for a Personalized Page Rank (optional)

returns

the graph containing with each vertex containing the PageRank and each edge containing the normalized weight.
  45. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#runWithOptions\[VD,ED\]\(graph:org.apache.spark.graphx.Graph\[VD,ED\],numIter:Int,resetProb:Double,srcId:Option\[org.apache.spark.graphx.VertexId\],normalized:Boolean\)\(implicitevidence$5:scala.reflect.ClassTag\[VD\],implicitevidence$6:scala.reflect.ClassTag\[ED\]\):org.apache.spark.graphx.Graph\[Double,Double\] "Permalink") def runWithOptions[VD, ED](graph: [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[VD, ED], numIter: Int, resetProb: Double, srcId: Option[[VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long)], normalized: Boolean)(implicit arg0: ClassTag[VD], arg1: ClassTag[ED]): [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[Double, Double]
Run PageRank for a fixed number of iterations returning a graph with vertex attributes containing the PageRank and edge attributes the normalized edge weight.
Run PageRank for a fixed number of iterations returning a graph with vertex attributes containing the PageRank and edge attributes the normalized edge weight.

VD

the original vertex attribute (not used)

ED

the original edge attribute (not used)

graph

the graph on which to compute PageRank

numIter

the number of iterations of PageRank to run

resetProb

the random reset probability (alpha)

srcId

the source vertex for a Personalized Page Rank (optional)

normalized

whether or not to normalize rank sum

returns

the graph containing with each vertex containing the PageRank and each edge containing the normalized weight.

Since

3.2.0
  46. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#runWithOptions\[VD,ED\]\(graph:org.apache.spark.graphx.Graph\[VD,ED\],numIter:Int,resetProb:Double,srcId:Option\[org.apache.spark.graphx.VertexId\]\)\(implicitevidence$3:scala.reflect.ClassTag\[VD\],implicitevidence$4:scala.reflect.ClassTag\[ED\]\):org.apache.spark.graphx.Graph\[Double,Double\] "Permalink") def runWithOptions[VD, ED](graph: [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[VD, ED], numIter: Int, resetProb: Double = 0.15, srcId: Option[[VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long)] = None)(implicit arg0: ClassTag[VD], arg1: ClassTag[ED]): [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[Double, Double]
Run PageRank for a fixed number of iterations returning a graph with vertex attributes containing the PageRank and edge attributes the normalized edge weight.
Run PageRank for a fixed number of iterations returning a graph with vertex attributes containing the PageRank and edge attributes the normalized edge weight.

VD

the original vertex attribute (not used)

ED

the original edge attribute (not used)

graph

the graph on which to compute PageRank

numIter

the number of iterations of PageRank to run

resetProb

the random reset probability (alpha)

srcId

the source vertex for a Personalized Page Rank (optional)

returns

the graph containing with each vertex containing the PageRank and each edge containing the normalized weight.
  47. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#runWithOptionsWithPreviousPageRank\[VD,ED\]\(graph:org.apache.spark.graphx.Graph\[VD,ED\],numIter:Int,resetProb:Double,srcId:Option\[org.apache.spark.graphx.VertexId\],normalized:Boolean,preRankGraph:org.apache.spark.graphx.Graph\[Double,Double\]\)\(implicitevidence$9:scala.reflect.ClassTag\[VD\],implicitevidence$10:scala.reflect.ClassTag\[ED\]\):org.apache.spark.graphx.Graph\[Double,Double\] "Permalink") def runWithOptionsWithPreviousPageRank[VD, ED](graph: [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[VD, ED], numIter: Int, resetProb: Double, srcId: Option[[VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long)], normalized: Boolean, preRankGraph: [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[Double, Double])(implicit arg0: ClassTag[VD], arg1: ClassTag[ED]): [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[Double, Double]
Run PageRank for a fixed number of iterations returning a graph with vertex attributes containing the PageRank and edge attributes the normalized edge weight.
Run PageRank for a fixed number of iterations returning a graph with vertex attributes containing the PageRank and edge attributes the normalized edge weight.

VD

the original vertex attribute (not used)

ED

the original edge attribute (not used)

graph

the graph on which to compute PageRank

numIter

the number of iterations of PageRank to run

resetProb

the random reset probability (alpha)

srcId

the source vertex for a Personalized Page Rank (optional)

normalized

whether or not to normalize rank sum

preRankGraph

PageRank graph from which to keep iterating

returns

the graph containing with each vertex containing the PageRank and each edge containing the normalized weight.

Since

3.2.0
  48. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#runWithOptionsWithPreviousPageRank\[VD,ED\]\(graph:org.apache.spark.graphx.Graph\[VD,ED\],numIter:Int,resetProb:Double,srcId:Option\[org.apache.spark.graphx.VertexId\],preRankGraph:org.apache.spark.graphx.Graph\[Double,Double\]\)\(implicitevidence$7:scala.reflect.ClassTag\[VD\],implicitevidence$8:scala.reflect.ClassTag\[ED\]\):org.apache.spark.graphx.Graph\[Double,Double\] "Permalink") def runWithOptionsWithPreviousPageRank[VD, ED](graph: [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[VD, ED], numIter: Int, resetProb: Double, srcId: Option[[VertexId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html#VertexId=Long)], preRankGraph: [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[Double, Double])(implicit arg0: ClassTag[VD], arg1: ClassTag[ED]): [Graph](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/Graph.html "org.apache.spark.graphx.Graph")[Double, Double]
Run PageRank for a fixed number of iterations returning a graph with vertex attributes containing the PageRank and edge attributes the normalized edge weight.
Run PageRank for a fixed number of iterations returning a graph with vertex attributes containing the PageRank and edge attributes the normalized edge weight.

VD

the original vertex attribute (not used)

ED

the original edge attribute (not used)

graph

the graph on which to compute PageRank

numIter

the number of iterations of PageRank to run

resetProb

the random reset probability (alpha)

srcId

the source vertex for a Personalized Page Rank (optional)

preRankGraph

PageRank graph from which to keep iterating

returns

the graph containing with each vertex containing the PageRank and each edge containing the normalized weight.
  49. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0

Definition Classes
    AnyRef
  50. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#toString\(\):String "Permalink") def toString(): [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String")

Definition Classes
    AnyRef → Any
  51. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])
  52. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  53. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#wait\(\):Unit "Permalink") final  def wait(): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])
  54. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#withLogContext\(context:java.util.Map\[String,String\]\)\(body:=>Unit\):Unit "Permalink") def withLogContext(context: [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#java.util.Map "java.util.Map")[String, String])(body: => Unit): Unit

Attributes
    protected

Definition Classes
    Logging
  55. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/lib/PageRank$.html#finalize\(\):Unit "Permalink") def finalize(): Unit

Attributes
    protected[lang]

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.Throwable]) @Deprecated

Deprecated

_(Since version 9)_
