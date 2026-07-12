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
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/index.html "Permalink") package [scheduler](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/index.html "Spark's scheduling components.")
Spark's scheduling components.
Spark's scheduling components. This includes the `org.apache.spark.scheduler.DAGScheduler` and lower level `org.apache.spark.scheduler.TaskScheduler`.  

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/cluster/index.html "Permalink") package [cluster](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/cluster/index.html) 

Definition Classes
    [scheduler](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/index.html "org.apache.spark.scheduler")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/AccumulableInfo.html ":: DeveloperApi :: Information about an org.apache.spark.util.AccumulatorV2 modified during a task or stage.")[AccumulableInfo](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/AccumulableInfo.html ":: DeveloperApi :: Information about an org.apache.spark.util.AccumulatorV2 modified during a task or stage.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/InputFormatInfo$.html) [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/InputFormatInfo.html ":: DeveloperApi :: Parses and holds information about inputFormat \(and files\) specified as a parameter.")[InputFormatInfo](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/InputFormatInfo.html ":: DeveloperApi :: Parses and holds information about inputFormat \(and files\) specified as a parameter.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/JobFailed.html)[JobFailed](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/JobFailed.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/JobResult.html ":: DeveloperApi :: A result of a job in the DAGScheduler.")[JobResult](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/JobResult.html ":: DeveloperApi :: A result of a job in the DAGScheduler.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/JobSucceeded$.html)[JobSucceeded](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/JobSucceeded$.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/MiscellaneousProcessDetails.html ":: DeveloperApi :: Stores information about an Miscellaneous Process to pass from the scheduler to SparkListeners.")[MiscellaneousProcessDetails](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/MiscellaneousProcessDetails.html ":: DeveloperApi :: Stores information about an Miscellaneous Process to pass from the scheduler to SparkListeners.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SchedulingMode$.html ""FAIR" and "FIFO" determines which policy is used to order tasks amongst a Schedulable's sub-queues "NONE" is used when the a Schedulable has no sub-queues.")[SchedulingMode](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SchedulingMode$.html ""FAIR" and "FIFO" determines which policy is used to order tasks amongst a Schedulable's sub-queues "NONE" is used when the a Schedulable has no sub-queues.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListener.html ":: DeveloperApi :: A default implementation for SparkListenerInterface that has no-op implementations for all callbacks.")[SparkListener](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListener.html ":: DeveloperApi :: A default implementation for SparkListenerInterface that has no-op implementations for all callbacks.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerApplicationEnd.html)[SparkListenerApplicationEnd](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerApplicationEnd.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerApplicationStart.html)[SparkListenerApplicationStart](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerApplicationStart.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerBlockManagerAdded.html)[SparkListenerBlockManagerAdded](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerBlockManagerAdded.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerBlockManagerRemoved.html)[SparkListenerBlockManagerRemoved](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerBlockManagerRemoved.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerBlockUpdated.html)[SparkListenerBlockUpdated](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerBlockUpdated.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEnvironmentUpdate.html)[SparkListenerEnvironmentUpdate](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEnvironmentUpdate.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html)[SparkListenerEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerExecutorAdded.html)[SparkListenerExecutorAdded](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerExecutorAdded.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerExecutorBlacklisted.html)[SparkListenerExecutorBlacklisted](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerExecutorBlacklisted.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerExecutorBlacklistedForStage.html)[SparkListenerExecutorBlacklistedForStage](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerExecutorBlacklistedForStage.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerExecutorExcluded.html)[SparkListenerExecutorExcluded](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerExecutorExcluded.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerExecutorExcludedForStage.html)[SparkListenerExecutorExcludedForStage](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerExecutorExcludedForStage.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerExecutorMetricsUpdate.html "Periodic updates from executors.")[SparkListenerExecutorMetricsUpdate](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerExecutorMetricsUpdate.html "Periodic updates from executors.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerExecutorRemoved.html)[SparkListenerExecutorRemoved](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerExecutorRemoved.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerExecutorUnblacklisted.html)[SparkListenerExecutorUnblacklisted](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerExecutorUnblacklisted.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerExecutorUnexcluded.html)[SparkListenerExecutorUnexcluded](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerExecutorUnexcluded.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerJobEnd.html)[SparkListenerJobEnd](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerJobEnd.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerJobStart.html)[SparkListenerJobStart](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerJobStart.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerLogStart.html "An internal class that describes the metadata of an event log.")[SparkListenerLogStart](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerLogStart.html "An internal class that describes the metadata of an event log.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerMiscellaneousProcessAdded.html)[SparkListenerMiscellaneousProcessAdded](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerMiscellaneousProcessAdded.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerNodeBlacklisted.html)[SparkListenerNodeBlacklisted](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerNodeBlacklisted.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerNodeBlacklistedForStage.html)[SparkListenerNodeBlacklistedForStage](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerNodeBlacklistedForStage.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerNodeExcluded.html)[SparkListenerNodeExcluded](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerNodeExcluded.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerNodeExcludedForStage.html)[SparkListenerNodeExcludedForStage](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerNodeExcludedForStage.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerNodeUnblacklisted.html)[SparkListenerNodeUnblacklisted](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerNodeUnblacklisted.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerNodeUnexcluded.html)[SparkListenerNodeUnexcluded](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerNodeUnexcluded.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerResourceProfileAdded.html)[SparkListenerResourceProfileAdded](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerResourceProfileAdded.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerSpeculativeTaskSubmitted.html)[SparkListenerSpeculativeTaskSubmitted](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerSpeculativeTaskSubmitted.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerStageCompleted.html)[SparkListenerStageCompleted](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerStageCompleted.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerStageExecutorMetrics.html "Peak metric values for the executor for the stage, written to the history log at stage completion.")[SparkListenerStageExecutorMetrics](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerStageExecutorMetrics.html "Peak metric values for the executor for the stage, written to the history log at stage completion.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerStageSubmitted.html)[SparkListenerStageSubmitted](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerStageSubmitted.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerTaskEnd.html)[SparkListenerTaskEnd](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerTaskEnd.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerTaskGettingResult.html)[SparkListenerTaskGettingResult](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerTaskGettingResult.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerTaskStart.html)[SparkListenerTaskStart](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerTaskStart.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerUnpersistRDD.html)[SparkListenerUnpersistRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerUnpersistRDD.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerUnschedulableTaskSetAdded.html)[SparkListenerUnschedulableTaskSetAdded](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerUnschedulableTaskSetAdded.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerUnschedulableTaskSetRemoved.html)[SparkListenerUnschedulableTaskSetRemoved](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerUnschedulableTaskSetRemoved.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SplitInfo$.html) [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SplitInfo.html)[SplitInfo](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SplitInfo.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/StageInfo.html ":: DeveloperApi :: Stores information about a stage to pass from the scheduler to SparkListeners.")[StageInfo](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/StageInfo.html ":: DeveloperApi :: Stores information about a stage to pass from the scheduler to SparkListeners.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/StatsReportListener.html ":: DeveloperApi :: Simple SparkListener that logs a few summary statistics when each stage completes.")[StatsReportListener](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/StatsReportListener.html ":: DeveloperApi :: Simple SparkListener that logs a few summary statistics when each stage completes.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/TaskInfo.html ":: DeveloperApi :: Information about a running task attempt inside a TaskSet.")[TaskInfo](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/TaskInfo.html ":: DeveloperApi :: Information about a running task attempt inside a TaskSet.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/TaskLocality$.html)[TaskLocality](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/TaskLocality$.html)


c
[org](https://spark.apache.org/docs/latest/api/scala/org/index.html "org").[apache](https://spark.apache.org/docs/latest/api/scala/org/apache/index.html "org.apache").[spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark").[scheduler](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/index.html "org.apache.spark.scheduler")
# AccumulableInfo[ __](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/AccumulableInfo.html "Permalink")
####  case class AccumulableInfo extends Product with Serializable
Developer API
Information about an [org.apache.spark.util.AccumulatorV2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html "org.apache.spark.util.AccumulatorV2") modified during a task or stage.  

Annotations
     @DeveloperApi() 

Source
    [AccumulableInfo.scala](https://github.com/apache/spark/tree/v4.1.2/core/src/main/scala/org/apache/spark/scheduler/AccumulableInfo.scala) 

Note
    
Once this is JSON serialized the types of `update` and `value` will be lost and be cast to strings. This is because the user can define an accumulator of any type and it will be difficult to preserve the type in consumers of the event log. This does not apply to internal accumulators that represent task level metrics.
Linear Supertypes
[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable"), Product, Equals, AnyRef, Any
__ __
Ordering
  1. Alphabetic
  2. By Inheritance


Inherited  

  1. AccumulableInfo
  2. Serializable
  3. Product
  4. Equals
  5. AnyRef
  6. Any


  1. Hide All
  2. Show All


Visibility
  1. Public
  2. Protected


### Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/AccumulableInfo.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/AccumulableInfo.html###:Int "Permalink") final  def ##: Int 

Definition Classes
    AnyRef → Any
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/AccumulableInfo.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/AccumulableInfo.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0 

Definition Classes
    Any
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/AccumulableInfo.html#clone\(\):Object "Permalink") def clone(): AnyRef 

Attributes
    protected[lang]  

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/AccumulableInfo.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/AccumulableInfo.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef] 

Definition Classes
    AnyRef → Any 

Annotations
     @IntrinsicCandidate() @native()
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/AccumulableInfo.html#id:Long "Permalink") val id: Long
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/AccumulableInfo.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean 

Definition Classes
    Any
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/AccumulableInfo.html#name:Option\[String\] "Permalink") val name: Option[String]
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/AccumulableInfo.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/AccumulableInfo.html#notify\(\):Unit "Permalink") final  def notify(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/AccumulableInfo.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/AccumulableInfo.html#productElementNames:Iterator\[String\] "Permalink") def productElementNames: Iterator[String] 

Definition Classes
    Product
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/AccumulableInfo.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0 

Definition Classes
    AnyRef
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/AccumulableInfo.html#update:Option\[Any\] "Permalink") val update: Option[Any]
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/AccumulableInfo.html#value:Option\[Any\] "Permalink") val value: Option[Any]
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/AccumulableInfo.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/AccumulableInfo.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/AccumulableInfo.html#wait\(\):Unit "Permalink") final  def wait(): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])


### Deprecated Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/AccumulableInfo.html#finalize\(\):Unit "Permalink") def finalize(): Unit 

Attributes
    protected[lang]  

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.Throwable]) @Deprecated 

Deprecated
    
_(Since version 9)_


### Inherited from Product
### Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/AccumulableInfo.html#productElementNames:Iterator\[String\] "Permalink") def productElementNames: Iterator[String] 

Definition Classes
    Product


### Inherited from AnyRef
### Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/AccumulableInfo.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/AccumulableInfo.html###:Int "Permalink") final  def ##: Int 

Definition Classes
    AnyRef → Any
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/AccumulableInfo.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/AccumulableInfo.html#clone\(\):Object "Permalink") def clone(): AnyRef 

Attributes
    protected[lang]  

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/AccumulableInfo.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/AccumulableInfo.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef] 

Definition Classes
    AnyRef → Any 

Annotations
     @IntrinsicCandidate() @native()
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/AccumulableInfo.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/AccumulableInfo.html#notify\(\):Unit "Permalink") final  def notify(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/AccumulableInfo.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/AccumulableInfo.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0 

Definition Classes
    AnyRef
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/AccumulableInfo.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/AccumulableInfo.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/AccumulableInfo.html#wait\(\):Unit "Permalink") final  def wait(): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/AccumulableInfo.html#finalize\(\):Unit "Permalink") def finalize(): Unit 

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
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/AccumulableInfo.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0 

Definition Classes
    Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/AccumulableInfo.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean 

Definition Classes
    Any


### Ungrouped
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/AccumulableInfo.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/AccumulableInfo.html###:Int "Permalink") final  def ##: Int 

Definition Classes
    AnyRef → Any
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/AccumulableInfo.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/AccumulableInfo.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0 

Definition Classes
    Any
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/AccumulableInfo.html#clone\(\):Object "Permalink") def clone(): AnyRef 

Attributes
    protected[lang]  

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/AccumulableInfo.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/AccumulableInfo.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef] 

Definition Classes
    AnyRef → Any 

Annotations
     @IntrinsicCandidate() @native()
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/AccumulableInfo.html#id:Long "Permalink") val id: Long
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/AccumulableInfo.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean 

Definition Classes
    Any
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/AccumulableInfo.html#name:Option\[String\] "Permalink") val name: Option[String]
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/AccumulableInfo.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/AccumulableInfo.html#notify\(\):Unit "Permalink") final  def notify(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/AccumulableInfo.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/AccumulableInfo.html#productElementNames:Iterator\[String\] "Permalink") def productElementNames: Iterator[String] 

Definition Classes
    Product
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/AccumulableInfo.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0 

Definition Classes
    AnyRef
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/AccumulableInfo.html#update:Option\[Any\] "Permalink") val update: Option[Any]
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/AccumulableInfo.html#value:Option\[Any\] "Permalink") val value: Option[Any]
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/AccumulableInfo.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/AccumulableInfo.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/AccumulableInfo.html#wait\(\):Unit "Permalink") final  def wait(): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/AccumulableInfo.html#finalize\(\):Unit "Permalink") def finalize(): Unit 

Attributes
    protected[lang]  

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.Throwable]) @Deprecated 

Deprecated
    
_(Since version 9)_


