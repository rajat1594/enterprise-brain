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
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/broadcast/index.html "Permalink") package [broadcast](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/broadcast/index.html "Spark's broadcast variables, used to broadcast immutable datasets to all nodes.")
Spark's broadcast variables, used to broadcast immutable datasets to all nodes.
Spark's broadcast variables, used to broadcast immutable datasets to all nodes.

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html "Permalink") package [graphx](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html "ALPHA COMPONENT GraphX is a graph processing framework built on top of Spark.")
ALPHA COMPONENT GraphX is a graph processing framework built on top of Spark.
ALPHA COMPONENT GraphX is a graph processing framework built on top of Spark.

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/input/index.html "Permalink") package [input](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/input/index.html)

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/index.html "Permalink") package [io](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/index.html "IO codecs used for compression.")
IO codecs used for compression.
IO codecs used for compression. See [org.apache.spark.io.CompressionCodec](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/CompressionCodec.html "org.apache.spark.io.CompressionCodec").

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/launcher/index.html "Permalink") package [launcher](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/launcher/index.html)

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/mapred/index.html "Permalink") package [mapred](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/mapred/index.html)

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/metrics/index.html "Permalink") package [metrics](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/metrics/index.html)

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/index.html "Permalink") package [ml](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/index.html "DataFrame-based machine learning APIs to let users quickly assemble and configure practical machine learning pipelines.")
DataFrame-based machine learning APIs to let users quickly assemble and configure practical machine learning pipelines.
DataFrame-based machine learning APIs to let users quickly assemble and configure practical machine learning pipelines.

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/mllib/index.html "Permalink") package [mllib](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/mllib/index.html "RDD-based machine learning APIs \(in maintenance mode\).")
RDD-based machine learning APIs (in maintenance mode).
RDD-based machine learning APIs (in maintenance mode).
The `spark.mllib` package is in maintenance mode as of the Spark 2.0.0 release to encourage migration to the DataFrame-based APIs under the [org.apache.spark.ml](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/index.html "org.apache.spark.ml") package. While in maintenance mode,
    * no new features in the RDD-based `spark.mllib` package will be accepted, unless they block implementing new features in the DataFrame-based `spark.ml` package;
    * bug fixes in the RDD-based APIs will still be accepted.
The developers will continue adding more features to the DataFrame-based APIs in the 2.x series to reach feature parity with the RDD-based APIs. And once we reach feature parity, this package will be deprecated.

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")

See also

[SPARK-4591](https://issues.apache.org/jira/browse/SPARK-4591) to track the progress of feature parity
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/partial/index.html "Permalink") package [partial](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/partial/index.html "Support for approximate results.")
Support for approximate results.
Support for approximate results. This provides convenient api and also implementation for approximate calculation.

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")

See also

[org.apache.spark.rdd.RDD.countApprox](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html#countApprox\(timeout:Long,confidence:Double\):org.apache.spark.partial.PartialResult\[org.apache.spark.partial.BoundedDouble\])
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/paths/index.html "Permalink") package [paths](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/paths/index.html)

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/index.html "Permalink") package [rdd](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/index.html "Provides several RDD implementations.")
Provides several RDD implementations.
Provides several RDD implementations. See [org.apache.spark.rdd.RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD").

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/resource/index.html "Permalink") package [resource](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/resource/index.html)

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/index.html "Permalink") package scheduler
Spark's scheduling components.
Spark's scheduling components. This includes the `org.apache.spark.scheduler.DAGScheduler` and lower level `org.apache.spark.scheduler.TaskScheduler`.

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/cluster/index.html "Permalink") package [cluster](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/cluster/index.html)
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
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/security/index.html "Permalink") package [security](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/security/index.html)

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/index.html "Permalink") package [serializer](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/index.html "Pluggable serializers for RDD and shuffle data.")
Pluggable serializers for RDD and shuffle data.
Pluggable serializers for RDD and shuffle data.

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")

See also

[org.apache.spark.serializer.Serializer](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/Serializer.html "org.apache.spark.serializer.Serializer")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/shuffle/index.html "Permalink") package [shuffle](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/shuffle/index.html)

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html "Permalink") package [sql](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html "Allows the execution of relational queries, including those expressed in SQL using Spark.")
Allows the execution of relational queries, including those expressed in SQL using Spark.
Allows the execution of relational queries, including those expressed in SQL using Spark.

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/status/index.html "Permalink") package [status](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/status/index.html)

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/index.html "Permalink") package [storage](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/index.html)

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/index.html "Permalink") package [streaming](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/index.html "Spark Streaming functionality.")
Spark Streaming functionality.
Spark Streaming functionality. [org.apache.spark.streaming.StreamingContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html "org.apache.spark.streaming.StreamingContext") serves as the main entry point to Spark Streaming, while [org.apache.spark.streaming.dstream.DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream") is the data type representing a continuous sequence of RDDs, representing a continuous stream of data.
In addition, [org.apache.spark.streaming.dstream.PairDStreamFunctions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html "org.apache.spark.streaming.dstream.PairDStreamFunctions") contains operations available only on DStreams of key-value pairs, such as `groupByKey` and `reduceByKey`. These operations are automatically available on any DStream of the right type (e.g. DStream[(Int, Int)] through implicit conversions.
For the Java API of Spark Streaming, take a look at the [org.apache.spark.streaming.api.java.JavaStreamingContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html "org.apache.spark.streaming.api.java.JavaStreamingContext") which serves as the entry point, and the [org.apache.spark.streaming.api.java.JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream") and the [org.apache.spark.streaming.api.java.JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream") which have the DStream functionality.

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ui/index.html "Permalink") package [ui](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ui/index.html)

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/unsafe/index.html "Permalink") package [unsafe](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/unsafe/index.html)

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/index.html "Permalink") package [util](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/index.html "Spark utilities.")
Spark utilities.
Spark utilities.

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")

p
[org](https://spark.apache.org/docs/latest/api/scala/org/index.html "org").[apache](https://spark.apache.org/docs/latest/api/scala/org/apache/index.html "org.apache").[spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
# scheduler[ __](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/index.html "Permalink")
####  package scheduler
Spark's scheduling components. This includes the `org.apache.spark.scheduler.DAGScheduler` and lower level `org.apache.spark.scheduler.TaskScheduler`.

Source
    [package.scala](https://github.com/apache/spark/tree/v4.1.2/core/src/main/scala/org/apache/spark/scheduler/package.scala)
Linear Supertypes
AnyRef, Any
__ __
Ordering
  1. Alphabetic
  2. By Inheritance

Inherited

  1. scheduler
  2. AnyRef
  3. Any

  1. Hide All
  2. Show All

Visibility
  1. Public
  2. Protected

### Package Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/cluster/index.html "Permalink") package [cluster](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/cluster/index.html)

### Type Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/AccumulableInfo.html "Permalink") case class [AccumulableInfo](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/AccumulableInfo.html ":: DeveloperApi :: Information about an org.apache.spark.util.AccumulatorV2 modified during a task or stage.") extends Product with Serializable
Information about an [org.apache.spark.util.AccumulatorV2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html "org.apache.spark.util.AccumulatorV2") modified during a task or stage.
Information about an [org.apache.spark.util.AccumulatorV2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html "org.apache.spark.util.AccumulatorV2") modified during a task or stage.

Annotations
     @DeveloperApi()

Note

Once this is JSON serialized the types of `update` and `value` will be lost and be cast to strings. This is because the user can define an accumulator of any type and it will be difficult to preserve the type in consumers of the event log. This does not apply to internal accumulators that represent task level metrics.
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/InputFormatInfo.html "Permalink") class [InputFormatInfo](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/InputFormatInfo.html ":: DeveloperApi :: Parses and holds information about inputFormat \(and files\) specified as a parameter.") extends Logging
Parses and holds information about inputFormat (and files) specified as a parameter.
Parses and holds information about inputFormat (and files) specified as a parameter.

Annotations
     @DeveloperApi()
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/JobFailed.html "Permalink") case class [JobFailed](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/JobFailed.html)(exception: Exception) extends [JobResult](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/JobResult.html "org.apache.spark.scheduler.JobResult") with Product with Serializable

Annotations
     @DeveloperApi()
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/JobResult.html "Permalink") sealed  trait [JobResult](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/JobResult.html ":: DeveloperApi :: A result of a job in the DAGScheduler.") extends AnyRef
A result of a job in the DAGScheduler.
A result of a job in the DAGScheduler.

Annotations
     @DeveloperApi()
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/MiscellaneousProcessDetails.html "Permalink") class [MiscellaneousProcessDetails](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/MiscellaneousProcessDetails.html ":: DeveloperApi :: Stores information about an Miscellaneous Process to pass from the scheduler to SparkListeners.") extends Serializable
Stores information about an Miscellaneous Process to pass from the scheduler to SparkListeners.
Stores information about an Miscellaneous Process to pass from the scheduler to SparkListeners.

Annotations
     @DeveloperApi() @Since("3.2.0")
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListener.html "Permalink") abstract  class [SparkListener](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListener.html ":: DeveloperApi :: A default implementation for SparkListenerInterface that has no-op implementations for all callbacks.") extends SparkListenerInterface
A default implementation for `SparkListenerInterface` that has no-op implementations for all callbacks.
A default implementation for `SparkListenerInterface` that has no-op implementations for all callbacks.
Note that this is an internal interface which might change in different Spark releases.

Annotations
     @DeveloperApi()
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerApplicationEnd.html "Permalink") case class [SparkListenerApplicationEnd](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerApplicationEnd.html)(time: Long, exitCode: Option[Int] = None) extends [SparkListenerEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html "org.apache.spark.scheduler.SparkListenerEvent") with Product with Serializable

Annotations
     @DeveloperApi()
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerApplicationStart.html "Permalink") case class [SparkListenerApplicationStart](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerApplicationStart.html)(appName: String, appId: Option[String], time: Long, sparkUser: String, appAttemptId: Option[String], driverLogs: Option[Map[String, String]] = None, driverAttributes: Option[Map[String, String]] = None) extends [SparkListenerEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html "org.apache.spark.scheduler.SparkListenerEvent") with Product with Serializable

Annotations
     @DeveloperApi()
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerBlockManagerAdded.html "Permalink") case class [SparkListenerBlockManagerAdded](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerBlockManagerAdded.html)(time: Long, blockManagerId: [BlockManagerId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html "org.apache.spark.storage.BlockManagerId"), maxMem: Long, maxOnHeapMem: Option[Long] = None, maxOffHeapMem: Option[Long] = None) extends [SparkListenerEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html "org.apache.spark.scheduler.SparkListenerEvent") with Product with Serializable

Annotations
     @DeveloperApi()
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerBlockManagerRemoved.html "Permalink") case class [SparkListenerBlockManagerRemoved](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerBlockManagerRemoved.html)(time: Long, blockManagerId: [BlockManagerId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html "org.apache.spark.storage.BlockManagerId")) extends [SparkListenerEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html "org.apache.spark.scheduler.SparkListenerEvent") with Product with Serializable

Annotations
     @DeveloperApi()
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerBlockUpdated.html "Permalink") case class [SparkListenerBlockUpdated](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerBlockUpdated.html)(blockUpdatedInfo: [BlockUpdatedInfo](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockUpdatedInfo.html "org.apache.spark.storage.BlockUpdatedInfo")) extends [SparkListenerEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html "org.apache.spark.scheduler.SparkListenerEvent") with Product with Serializable

Annotations
     @DeveloperApi()
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEnvironmentUpdate.html "Permalink") case class [SparkListenerEnvironmentUpdate](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEnvironmentUpdate.html)(environmentDetails: Map[String, Seq[(String, String)]]) extends [SparkListenerEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html "org.apache.spark.scheduler.SparkListenerEvent") with Product with Serializable

Annotations
     @DeveloperApi()
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html "Permalink") trait [SparkListenerEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html) extends AnyRef

Annotations
     @DeveloperApi() @JsonTypeInfo()
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerExecutorAdded.html "Permalink") case class [SparkListenerExecutorAdded](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerExecutorAdded.html)(time: Long, executorId: String, executorInfo: [ExecutorInfo](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/cluster/ExecutorInfo.html "org.apache.spark.scheduler.cluster.ExecutorInfo")) extends [SparkListenerEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html "org.apache.spark.scheduler.SparkListenerEvent") with Product with Serializable

Annotations
     @DeveloperApi()
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerExecutorExcluded.html "Permalink") case class [SparkListenerExecutorExcluded](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerExecutorExcluded.html)(time: Long, executorId: String, taskFailures: Int) extends [SparkListenerEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html "org.apache.spark.scheduler.SparkListenerEvent") with Product with Serializable

Annotations
     @DeveloperApi() @Since("3.1.0")
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerExecutorExcludedForStage.html "Permalink") case class [SparkListenerExecutorExcludedForStage](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerExecutorExcludedForStage.html)(time: Long, executorId: String, taskFailures: Int, stageId: Int, stageAttemptId: Int) extends [SparkListenerEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html "org.apache.spark.scheduler.SparkListenerEvent") with Product with Serializable

Annotations
     @DeveloperApi() @Since("3.1.0")
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerExecutorMetricsUpdate.html "Permalink") case class [SparkListenerExecutorMetricsUpdate](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerExecutorMetricsUpdate.html "Periodic updates from executors.")(execId: String, accumUpdates: Seq[(Long, Int, Int, Seq[[AccumulableInfo](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/AccumulableInfo.html "org.apache.spark.scheduler.AccumulableInfo")])], executorUpdates: Map[(Int, Int), ExecutorMetrics] = Map.empty) extends [SparkListenerEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html "org.apache.spark.scheduler.SparkListenerEvent") with Product with Serializable
Periodic updates from executors.
Periodic updates from executors.

execId

executor id

accumUpdates

sequence of (taskId, stageId, stageAttemptId, accumUpdates)

executorUpdates

executor level per-stage metrics updates

Annotations
     @DeveloperApi()

Since

3.1.0
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerExecutorRemoved.html "Permalink") case class [SparkListenerExecutorRemoved](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerExecutorRemoved.html)(time: Long, executorId: String, reason: String) extends [SparkListenerEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html "org.apache.spark.scheduler.SparkListenerEvent") with Product with Serializable

Annotations
     @DeveloperApi()
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerExecutorUnexcluded.html "Permalink") case class [SparkListenerExecutorUnexcluded](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerExecutorUnexcluded.html)(time: Long, executorId: String) extends [SparkListenerEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html "org.apache.spark.scheduler.SparkListenerEvent") with Product with Serializable

Annotations
     @DeveloperApi()
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerJobEnd.html "Permalink") case class [SparkListenerJobEnd](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerJobEnd.html)(jobId: Int, time: Long, jobResult: [JobResult](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/JobResult.html "org.apache.spark.scheduler.JobResult")) extends [SparkListenerEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html "org.apache.spark.scheduler.SparkListenerEvent") with Product with Serializable

Annotations
     @DeveloperApi()
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerJobStart.html "Permalink") case class [SparkListenerJobStart](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerJobStart.html)(jobId: Int, time: Long, stageInfos: Seq[[StageInfo](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/StageInfo.html "org.apache.spark.scheduler.StageInfo")], properties: [Properties](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Properties.html#java.util.Properties "java.util.Properties") = null) extends [SparkListenerEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html "org.apache.spark.scheduler.SparkListenerEvent") with Product with Serializable

Annotations
     @DeveloperApi()
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerLogStart.html "Permalink") case class [SparkListenerLogStart](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerLogStart.html "An internal class that describes the metadata of an event log.")(sparkVersion: String) extends [SparkListenerEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html "org.apache.spark.scheduler.SparkListenerEvent") with Product with Serializable
An internal class that describes the metadata of an event log.
An internal class that describes the metadata of an event log.

Annotations
     @DeveloperApi()
  23. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerMiscellaneousProcessAdded.html "Permalink") case class [SparkListenerMiscellaneousProcessAdded](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerMiscellaneousProcessAdded.html)(time: Long, processId: String, info: [MiscellaneousProcessDetails](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/MiscellaneousProcessDetails.html "org.apache.spark.scheduler.MiscellaneousProcessDetails")) extends [SparkListenerEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html "org.apache.spark.scheduler.SparkListenerEvent") with Product with Serializable

Annotations
     @DeveloperApi() @Since("3.2.0")
  24. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerNodeExcluded.html "Permalink") case class [SparkListenerNodeExcluded](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerNodeExcluded.html)(time: Long, hostId: String, executorFailures: Int) extends [SparkListenerEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html "org.apache.spark.scheduler.SparkListenerEvent") with Product with Serializable

Annotations
     @DeveloperApi() @Since("3.1.0")
  25. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerNodeExcludedForStage.html "Permalink") case class [SparkListenerNodeExcludedForStage](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerNodeExcludedForStage.html)(time: Long, hostId: String, executorFailures: Int, stageId: Int, stageAttemptId: Int) extends [SparkListenerEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html "org.apache.spark.scheduler.SparkListenerEvent") with Product with Serializable

Annotations
     @DeveloperApi() @Since("3.1.0")
  26. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerNodeUnexcluded.html "Permalink") case class [SparkListenerNodeUnexcluded](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerNodeUnexcluded.html)(time: Long, hostId: String) extends [SparkListenerEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html "org.apache.spark.scheduler.SparkListenerEvent") with Product with Serializable

Annotations
     @DeveloperApi() @Since("3.1.0")
  27. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerResourceProfileAdded.html "Permalink") case class [SparkListenerResourceProfileAdded](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerResourceProfileAdded.html)(resourceProfile: [ResourceProfile](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/resource/ResourceProfile.html "org.apache.spark.resource.ResourceProfile")) extends [SparkListenerEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html "org.apache.spark.scheduler.SparkListenerEvent") with Product with Serializable

Annotations
     @DeveloperApi() @Since("3.1.0")
  28. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerSpeculativeTaskSubmitted.html "Permalink") case class [SparkListenerSpeculativeTaskSubmitted](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerSpeculativeTaskSubmitted.html)(stageId: Int, stageAttemptId: Int = 0) extends [SparkListenerEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html "org.apache.spark.scheduler.SparkListenerEvent") with Product with Serializable

Annotations
     @DeveloperApi()
  29. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerStageCompleted.html "Permalink") case class [SparkListenerStageCompleted](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerStageCompleted.html)(stageInfo: [StageInfo](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/StageInfo.html "org.apache.spark.scheduler.StageInfo")) extends [SparkListenerEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html "org.apache.spark.scheduler.SparkListenerEvent") with Product with Serializable

Annotations
     @DeveloperApi()
  30. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerStageExecutorMetrics.html "Permalink") case class [SparkListenerStageExecutorMetrics](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerStageExecutorMetrics.html "Peak metric values for the executor for the stage, written to the history log at stage completion.")(execId: String, stageId: Int, stageAttemptId: Int, executorMetrics: ExecutorMetrics) extends [SparkListenerEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html "org.apache.spark.scheduler.SparkListenerEvent") with Product with Serializable
Peak metric values for the executor for the stage, written to the history log at stage completion.
Peak metric values for the executor for the stage, written to the history log at stage completion.

execId

executor id

stageId

stage id

stageAttemptId

stage attempt

executorMetrics

executor level metrics peak values

Annotations
     @DeveloperApi()
  31. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerStageSubmitted.html "Permalink") case class [SparkListenerStageSubmitted](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerStageSubmitted.html)(stageInfo: [StageInfo](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/StageInfo.html "org.apache.spark.scheduler.StageInfo"), properties: [Properties](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Properties.html#java.util.Properties "java.util.Properties") = null) extends [SparkListenerEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html "org.apache.spark.scheduler.SparkListenerEvent") with Product with Serializable

Annotations
     @DeveloperApi()
  32. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerTaskEnd.html "Permalink") case class [SparkListenerTaskEnd](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerTaskEnd.html)(stageId: Int, stageAttemptId: Int, taskType: String, reason: [TaskEndReason](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskEndReason.html "org.apache.spark.TaskEndReason"), taskInfo: [TaskInfo](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/TaskInfo.html "org.apache.spark.scheduler.TaskInfo"), taskExecutorMetrics: ExecutorMetrics, taskMetrics: TaskMetrics) extends [SparkListenerEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html "org.apache.spark.scheduler.SparkListenerEvent") with Product with Serializable

Annotations
     @DeveloperApi()
  33. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerTaskGettingResult.html "Permalink") case class [SparkListenerTaskGettingResult](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerTaskGettingResult.html)(taskInfo: [TaskInfo](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/TaskInfo.html "org.apache.spark.scheduler.TaskInfo")) extends [SparkListenerEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html "org.apache.spark.scheduler.SparkListenerEvent") with Product with Serializable

Annotations
     @DeveloperApi()
  34. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerTaskStart.html "Permalink") case class [SparkListenerTaskStart](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerTaskStart.html)(stageId: Int, stageAttemptId: Int, taskInfo: [TaskInfo](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/TaskInfo.html "org.apache.spark.scheduler.TaskInfo")) extends [SparkListenerEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html "org.apache.spark.scheduler.SparkListenerEvent") with Product with Serializable

Annotations
     @DeveloperApi()
  35. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerUnpersistRDD.html "Permalink") case class [SparkListenerUnpersistRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerUnpersistRDD.html)(rddId: Int) extends [SparkListenerEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html "org.apache.spark.scheduler.SparkListenerEvent") with Product with Serializable

Annotations
     @DeveloperApi()
  36. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerUnschedulableTaskSetAdded.html "Permalink") case class [SparkListenerUnschedulableTaskSetAdded](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerUnschedulableTaskSetAdded.html)(stageId: Int, stageAttemptId: Int) extends [SparkListenerEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html "org.apache.spark.scheduler.SparkListenerEvent") with Product with Serializable

Annotations
     @DeveloperApi() @Since("3.1.0")
  37. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerUnschedulableTaskSetRemoved.html "Permalink") case class [SparkListenerUnschedulableTaskSetRemoved](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerUnschedulableTaskSetRemoved.html)(stageId: Int, stageAttemptId: Int) extends [SparkListenerEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html "org.apache.spark.scheduler.SparkListenerEvent") with Product with Serializable

Annotations
     @DeveloperApi() @Since("3.1.0")
  38. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SplitInfo.html "Permalink") class [SplitInfo](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SplitInfo.html) extends AnyRef

Annotations
     @DeveloperApi()
  39. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/StageInfo.html "Permalink") class [StageInfo](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/StageInfo.html ":: DeveloperApi :: Stores information about a stage to pass from the scheduler to SparkListeners.") extends AnyRef
Stores information about a stage to pass from the scheduler to SparkListeners.
Stores information about a stage to pass from the scheduler to SparkListeners.

Annotations
     @DeveloperApi()
  40. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/StatsReportListener.html "Permalink") class [StatsReportListener](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/StatsReportListener.html ":: DeveloperApi :: Simple SparkListener that logs a few summary statistics when each stage completes.") extends [SparkListener](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListener.html "org.apache.spark.scheduler.SparkListener") with Logging
Simple SparkListener that logs a few summary statistics when each stage completes.
Simple SparkListener that logs a few summary statistics when each stage completes.

Annotations
     @DeveloperApi()
  41. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/TaskInfo.html "Permalink") class [TaskInfo](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/TaskInfo.html ":: DeveloperApi :: Information about a running task attempt inside a TaskSet.") extends Cloneable
Information about a running task attempt inside a TaskSet.
Information about a running task attempt inside a TaskSet.

Annotations
     @DeveloperApi()

### Deprecated Type Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerExecutorBlacklisted.html "Permalink") case class [SparkListenerExecutorBlacklisted](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerExecutorBlacklisted.html)(time: Long, executorId: String, taskFailures: Int) extends [SparkListenerEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html "org.apache.spark.scheduler.SparkListenerEvent") with Product with Serializable

Annotations
     @DeveloperApi() @deprecated

Deprecated

_(Since version 3.1.0)_ use SparkListenerExecutorExcluded instead
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerExecutorBlacklistedForStage.html "Permalink") case class [SparkListenerExecutorBlacklistedForStage](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerExecutorBlacklistedForStage.html)(time: Long, executorId: String, taskFailures: Int, stageId: Int, stageAttemptId: Int) extends [SparkListenerEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html "org.apache.spark.scheduler.SparkListenerEvent") with Product with Serializable

Annotations
     @deprecated @DeveloperApi()

Deprecated

_(Since version 3.1.0)_ use SparkListenerExecutorExcludedForStage instead
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerExecutorUnblacklisted.html "Permalink") case class [SparkListenerExecutorUnblacklisted](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerExecutorUnblacklisted.html)(time: Long, executorId: String) extends [SparkListenerEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html "org.apache.spark.scheduler.SparkListenerEvent") with Product with Serializable

Annotations
     @deprecated @DeveloperApi()

Deprecated

_(Since version 3.1.0)_ use SparkListenerExecutorUnexcluded instead
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerNodeBlacklisted.html "Permalink") case class [SparkListenerNodeBlacklisted](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerNodeBlacklisted.html)(time: Long, hostId: String, executorFailures: Int) extends [SparkListenerEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html "org.apache.spark.scheduler.SparkListenerEvent") with Product with Serializable

Annotations
     @deprecated @DeveloperApi()

Deprecated

_(Since version 3.1.0)_ use SparkListenerNodeExcluded instead
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerNodeBlacklistedForStage.html "Permalink") case class [SparkListenerNodeBlacklistedForStage](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerNodeBlacklistedForStage.html)(time: Long, hostId: String, executorFailures: Int, stageId: Int, stageAttemptId: Int) extends [SparkListenerEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html "org.apache.spark.scheduler.SparkListenerEvent") with Product with Serializable

Annotations
     @deprecated @DeveloperApi()

Deprecated

_(Since version 3.1.0)_ use SparkListenerNodeExcludedForStage instead
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerNodeUnblacklisted.html "Permalink") case class [SparkListenerNodeUnblacklisted](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerNodeUnblacklisted.html)(time: Long, hostId: String) extends [SparkListenerEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html "org.apache.spark.scheduler.SparkListenerEvent") with Product with Serializable

Annotations
     @deprecated @DeveloperApi()

Deprecated

_(Since version 3.1.0)_ use SparkListenerNodeUnexcluded instead

### Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/InputFormatInfo$.html "Permalink") object [InputFormatInfo](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/InputFormatInfo$.html)
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/JobSucceeded$.html "Permalink") case object [JobSucceeded](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/JobSucceeded$.html) extends [JobResult](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/JobResult.html "org.apache.spark.scheduler.JobResult") with Product with Serializable

Annotations
     @DeveloperApi()
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SchedulingMode$.html "Permalink") object [SchedulingMode](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SchedulingMode$.html ""FAIR" and "FIFO" determines which policy is used to order tasks amongst a Schedulable's sub-queues "NONE" is used when the a Schedulable has no sub-queues.") extends Enumeration
"FAIR" and "FIFO" determines which policy is used to order tasks amongst a Schedulable's sub-queues "NONE" is used when the a Schedulable has no sub-queues.
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SplitInfo$.html "Permalink") object [SplitInfo](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SplitInfo$.html)
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/TaskLocality$.html "Permalink") object [TaskLocality](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/TaskLocality$.html) extends Enumeration

Annotations
     @DeveloperApi()

### Ungrouped
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/AccumulableInfo.html "Permalink") case class [AccumulableInfo](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/AccumulableInfo.html ":: DeveloperApi :: Information about an org.apache.spark.util.AccumulatorV2 modified during a task or stage.") extends Product with Serializable
Information about an [org.apache.spark.util.AccumulatorV2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html "org.apache.spark.util.AccumulatorV2") modified during a task or stage.
Information about an [org.apache.spark.util.AccumulatorV2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/AccumulatorV2.html "org.apache.spark.util.AccumulatorV2") modified during a task or stage.

Annotations
     @DeveloperApi()

Note

Once this is JSON serialized the types of `update` and `value` will be lost and be cast to strings. This is because the user can define an accumulator of any type and it will be difficult to preserve the type in consumers of the event log. This does not apply to internal accumulators that represent task level metrics.
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/InputFormatInfo.html "Permalink") class [InputFormatInfo](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/InputFormatInfo.html ":: DeveloperApi :: Parses and holds information about inputFormat \(and files\) specified as a parameter.") extends Logging
Parses and holds information about inputFormat (and files) specified as a parameter.
Parses and holds information about inputFormat (and files) specified as a parameter.

Annotations
     @DeveloperApi()
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/JobFailed.html "Permalink") case class [JobFailed](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/JobFailed.html)(exception: Exception) extends [JobResult](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/JobResult.html "org.apache.spark.scheduler.JobResult") with Product with Serializable

Annotations
     @DeveloperApi()
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/JobResult.html "Permalink") sealed  trait [JobResult](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/JobResult.html ":: DeveloperApi :: A result of a job in the DAGScheduler.") extends AnyRef
A result of a job in the DAGScheduler.
A result of a job in the DAGScheduler.

Annotations
     @DeveloperApi()
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/MiscellaneousProcessDetails.html "Permalink") class [MiscellaneousProcessDetails](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/MiscellaneousProcessDetails.html ":: DeveloperApi :: Stores information about an Miscellaneous Process to pass from the scheduler to SparkListeners.") extends Serializable
Stores information about an Miscellaneous Process to pass from the scheduler to SparkListeners.
Stores information about an Miscellaneous Process to pass from the scheduler to SparkListeners.

Annotations
     @DeveloperApi() @Since("3.2.0")
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListener.html "Permalink") abstract  class [SparkListener](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListener.html ":: DeveloperApi :: A default implementation for SparkListenerInterface that has no-op implementations for all callbacks.") extends SparkListenerInterface
A default implementation for `SparkListenerInterface` that has no-op implementations for all callbacks.
A default implementation for `SparkListenerInterface` that has no-op implementations for all callbacks.
Note that this is an internal interface which might change in different Spark releases.

Annotations
     @DeveloperApi()
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerApplicationEnd.html "Permalink") case class [SparkListenerApplicationEnd](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerApplicationEnd.html)(time: Long, exitCode: Option[Int] = None) extends [SparkListenerEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html "org.apache.spark.scheduler.SparkListenerEvent") with Product with Serializable

Annotations
     @DeveloperApi()
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerApplicationStart.html "Permalink") case class [SparkListenerApplicationStart](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerApplicationStart.html)(appName: String, appId: Option[String], time: Long, sparkUser: String, appAttemptId: Option[String], driverLogs: Option[Map[String, String]] = None, driverAttributes: Option[Map[String, String]] = None) extends [SparkListenerEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html "org.apache.spark.scheduler.SparkListenerEvent") with Product with Serializable

Annotations
     @DeveloperApi()
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerBlockManagerAdded.html "Permalink") case class [SparkListenerBlockManagerAdded](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerBlockManagerAdded.html)(time: Long, blockManagerId: [BlockManagerId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html "org.apache.spark.storage.BlockManagerId"), maxMem: Long, maxOnHeapMem: Option[Long] = None, maxOffHeapMem: Option[Long] = None) extends [SparkListenerEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html "org.apache.spark.scheduler.SparkListenerEvent") with Product with Serializable

Annotations
     @DeveloperApi()
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerBlockManagerRemoved.html "Permalink") case class [SparkListenerBlockManagerRemoved](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerBlockManagerRemoved.html)(time: Long, blockManagerId: [BlockManagerId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html "org.apache.spark.storage.BlockManagerId")) extends [SparkListenerEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html "org.apache.spark.scheduler.SparkListenerEvent") with Product with Serializable

Annotations
     @DeveloperApi()
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerBlockUpdated.html "Permalink") case class [SparkListenerBlockUpdated](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerBlockUpdated.html)(blockUpdatedInfo: [BlockUpdatedInfo](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockUpdatedInfo.html "org.apache.spark.storage.BlockUpdatedInfo")) extends [SparkListenerEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html "org.apache.spark.scheduler.SparkListenerEvent") with Product with Serializable

Annotations
     @DeveloperApi()
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEnvironmentUpdate.html "Permalink") case class [SparkListenerEnvironmentUpdate](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEnvironmentUpdate.html)(environmentDetails: Map[String, Seq[(String, String)]]) extends [SparkListenerEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html "org.apache.spark.scheduler.SparkListenerEvent") with Product with Serializable

Annotations
     @DeveloperApi()
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html "Permalink") trait [SparkListenerEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html) extends AnyRef

Annotations
     @DeveloperApi() @JsonTypeInfo()
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerExecutorAdded.html "Permalink") case class [SparkListenerExecutorAdded](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerExecutorAdded.html)(time: Long, executorId: String, executorInfo: [ExecutorInfo](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/cluster/ExecutorInfo.html "org.apache.spark.scheduler.cluster.ExecutorInfo")) extends [SparkListenerEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html "org.apache.spark.scheduler.SparkListenerEvent") with Product with Serializable

Annotations
     @DeveloperApi()
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerExecutorExcluded.html "Permalink") case class [SparkListenerExecutorExcluded](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerExecutorExcluded.html)(time: Long, executorId: String, taskFailures: Int) extends [SparkListenerEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html "org.apache.spark.scheduler.SparkListenerEvent") with Product with Serializable

Annotations
     @DeveloperApi() @Since("3.1.0")
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerExecutorExcludedForStage.html "Permalink") case class [SparkListenerExecutorExcludedForStage](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerExecutorExcludedForStage.html)(time: Long, executorId: String, taskFailures: Int, stageId: Int, stageAttemptId: Int) extends [SparkListenerEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html "org.apache.spark.scheduler.SparkListenerEvent") with Product with Serializable

Annotations
     @DeveloperApi() @Since("3.1.0")
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerExecutorMetricsUpdate.html "Permalink") case class [SparkListenerExecutorMetricsUpdate](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerExecutorMetricsUpdate.html "Periodic updates from executors.")(execId: String, accumUpdates: Seq[(Long, Int, Int, Seq[[AccumulableInfo](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/AccumulableInfo.html "org.apache.spark.scheduler.AccumulableInfo")])], executorUpdates: Map[(Int, Int), ExecutorMetrics] = Map.empty) extends [SparkListenerEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html "org.apache.spark.scheduler.SparkListenerEvent") with Product with Serializable
Periodic updates from executors.
Periodic updates from executors.

execId

executor id

accumUpdates

sequence of (taskId, stageId, stageAttemptId, accumUpdates)

executorUpdates

executor level per-stage metrics updates

Annotations
     @DeveloperApi()

Since

3.1.0
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerExecutorRemoved.html "Permalink") case class [SparkListenerExecutorRemoved](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerExecutorRemoved.html)(time: Long, executorId: String, reason: String) extends [SparkListenerEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html "org.apache.spark.scheduler.SparkListenerEvent") with Product with Serializable

Annotations
     @DeveloperApi()
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerExecutorUnexcluded.html "Permalink") case class [SparkListenerExecutorUnexcluded](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerExecutorUnexcluded.html)(time: Long, executorId: String) extends [SparkListenerEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html "org.apache.spark.scheduler.SparkListenerEvent") with Product with Serializable

Annotations
     @DeveloperApi()
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerJobEnd.html "Permalink") case class [SparkListenerJobEnd](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerJobEnd.html)(jobId: Int, time: Long, jobResult: [JobResult](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/JobResult.html "org.apache.spark.scheduler.JobResult")) extends [SparkListenerEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html "org.apache.spark.scheduler.SparkListenerEvent") with Product with Serializable

Annotations
     @DeveloperApi()
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerJobStart.html "Permalink") case class [SparkListenerJobStart](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerJobStart.html)(jobId: Int, time: Long, stageInfos: Seq[[StageInfo](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/StageInfo.html "org.apache.spark.scheduler.StageInfo")], properties: [Properties](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Properties.html#java.util.Properties "java.util.Properties") = null) extends [SparkListenerEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html "org.apache.spark.scheduler.SparkListenerEvent") with Product with Serializable

Annotations
     @DeveloperApi()
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerLogStart.html "Permalink") case class [SparkListenerLogStart](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerLogStart.html "An internal class that describes the metadata of an event log.")(sparkVersion: String) extends [SparkListenerEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html "org.apache.spark.scheduler.SparkListenerEvent") with Product with Serializable
An internal class that describes the metadata of an event log.
An internal class that describes the metadata of an event log.

Annotations
     @DeveloperApi()
  23. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerMiscellaneousProcessAdded.html "Permalink") case class [SparkListenerMiscellaneousProcessAdded](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerMiscellaneousProcessAdded.html)(time: Long, processId: String, info: [MiscellaneousProcessDetails](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/MiscellaneousProcessDetails.html "org.apache.spark.scheduler.MiscellaneousProcessDetails")) extends [SparkListenerEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html "org.apache.spark.scheduler.SparkListenerEvent") with Product with Serializable

Annotations
     @DeveloperApi() @Since("3.2.0")
  24. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerNodeExcluded.html "Permalink") case class [SparkListenerNodeExcluded](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerNodeExcluded.html)(time: Long, hostId: String, executorFailures: Int) extends [SparkListenerEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html "org.apache.spark.scheduler.SparkListenerEvent") with Product with Serializable

Annotations
     @DeveloperApi() @Since("3.1.0")
  25. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerNodeExcludedForStage.html "Permalink") case class [SparkListenerNodeExcludedForStage](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerNodeExcludedForStage.html)(time: Long, hostId: String, executorFailures: Int, stageId: Int, stageAttemptId: Int) extends [SparkListenerEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html "org.apache.spark.scheduler.SparkListenerEvent") with Product with Serializable

Annotations
     @DeveloperApi() @Since("3.1.0")
  26. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerNodeUnexcluded.html "Permalink") case class [SparkListenerNodeUnexcluded](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerNodeUnexcluded.html)(time: Long, hostId: String) extends [SparkListenerEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html "org.apache.spark.scheduler.SparkListenerEvent") with Product with Serializable

Annotations
     @DeveloperApi() @Since("3.1.0")
  27. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerResourceProfileAdded.html "Permalink") case class [SparkListenerResourceProfileAdded](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerResourceProfileAdded.html)(resourceProfile: [ResourceProfile](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/resource/ResourceProfile.html "org.apache.spark.resource.ResourceProfile")) extends [SparkListenerEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html "org.apache.spark.scheduler.SparkListenerEvent") with Product with Serializable

Annotations
     @DeveloperApi() @Since("3.1.0")
  28. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerSpeculativeTaskSubmitted.html "Permalink") case class [SparkListenerSpeculativeTaskSubmitted](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerSpeculativeTaskSubmitted.html)(stageId: Int, stageAttemptId: Int = 0) extends [SparkListenerEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html "org.apache.spark.scheduler.SparkListenerEvent") with Product with Serializable

Annotations
     @DeveloperApi()
  29. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerStageCompleted.html "Permalink") case class [SparkListenerStageCompleted](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerStageCompleted.html)(stageInfo: [StageInfo](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/StageInfo.html "org.apache.spark.scheduler.StageInfo")) extends [SparkListenerEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html "org.apache.spark.scheduler.SparkListenerEvent") with Product with Serializable

Annotations
     @DeveloperApi()
  30. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerStageExecutorMetrics.html "Permalink") case class [SparkListenerStageExecutorMetrics](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerStageExecutorMetrics.html "Peak metric values for the executor for the stage, written to the history log at stage completion.")(execId: String, stageId: Int, stageAttemptId: Int, executorMetrics: ExecutorMetrics) extends [SparkListenerEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html "org.apache.spark.scheduler.SparkListenerEvent") with Product with Serializable
Peak metric values for the executor for the stage, written to the history log at stage completion.
Peak metric values for the executor for the stage, written to the history log at stage completion.

execId

executor id

stageId

stage id

stageAttemptId

stage attempt

executorMetrics

executor level metrics peak values

Annotations
     @DeveloperApi()
  31. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerStageSubmitted.html "Permalink") case class [SparkListenerStageSubmitted](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerStageSubmitted.html)(stageInfo: [StageInfo](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/StageInfo.html "org.apache.spark.scheduler.StageInfo"), properties: [Properties](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Properties.html#java.util.Properties "java.util.Properties") = null) extends [SparkListenerEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html "org.apache.spark.scheduler.SparkListenerEvent") with Product with Serializable

Annotations
     @DeveloperApi()
  32. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerTaskEnd.html "Permalink") case class [SparkListenerTaskEnd](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerTaskEnd.html)(stageId: Int, stageAttemptId: Int, taskType: String, reason: [TaskEndReason](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/TaskEndReason.html "org.apache.spark.TaskEndReason"), taskInfo: [TaskInfo](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/TaskInfo.html "org.apache.spark.scheduler.TaskInfo"), taskExecutorMetrics: ExecutorMetrics, taskMetrics: TaskMetrics) extends [SparkListenerEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html "org.apache.spark.scheduler.SparkListenerEvent") with Product with Serializable

Annotations
     @DeveloperApi()
  33. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerTaskGettingResult.html "Permalink") case class [SparkListenerTaskGettingResult](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerTaskGettingResult.html)(taskInfo: [TaskInfo](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/TaskInfo.html "org.apache.spark.scheduler.TaskInfo")) extends [SparkListenerEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html "org.apache.spark.scheduler.SparkListenerEvent") with Product with Serializable

Annotations
     @DeveloperApi()
  34. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerTaskStart.html "Permalink") case class [SparkListenerTaskStart](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerTaskStart.html)(stageId: Int, stageAttemptId: Int, taskInfo: [TaskInfo](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/TaskInfo.html "org.apache.spark.scheduler.TaskInfo")) extends [SparkListenerEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html "org.apache.spark.scheduler.SparkListenerEvent") with Product with Serializable

Annotations
     @DeveloperApi()
  35. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerUnpersistRDD.html "Permalink") case class [SparkListenerUnpersistRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerUnpersistRDD.html)(rddId: Int) extends [SparkListenerEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html "org.apache.spark.scheduler.SparkListenerEvent") with Product with Serializable

Annotations
     @DeveloperApi()
  36. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerUnschedulableTaskSetAdded.html "Permalink") case class [SparkListenerUnschedulableTaskSetAdded](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerUnschedulableTaskSetAdded.html)(stageId: Int, stageAttemptId: Int) extends [SparkListenerEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html "org.apache.spark.scheduler.SparkListenerEvent") with Product with Serializable

Annotations
     @DeveloperApi() @Since("3.1.0")
  37. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerUnschedulableTaskSetRemoved.html "Permalink") case class [SparkListenerUnschedulableTaskSetRemoved](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerUnschedulableTaskSetRemoved.html)(stageId: Int, stageAttemptId: Int) extends [SparkListenerEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html "org.apache.spark.scheduler.SparkListenerEvent") with Product with Serializable

Annotations
     @DeveloperApi() @Since("3.1.0")
  38. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SplitInfo.html "Permalink") class [SplitInfo](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SplitInfo.html) extends AnyRef

Annotations
     @DeveloperApi()
  39. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/StageInfo.html "Permalink") class [StageInfo](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/StageInfo.html ":: DeveloperApi :: Stores information about a stage to pass from the scheduler to SparkListeners.") extends AnyRef
Stores information about a stage to pass from the scheduler to SparkListeners.
Stores information about a stage to pass from the scheduler to SparkListeners.

Annotations
     @DeveloperApi()
  40. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/StatsReportListener.html "Permalink") class [StatsReportListener](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/StatsReportListener.html ":: DeveloperApi :: Simple SparkListener that logs a few summary statistics when each stage completes.") extends [SparkListener](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListener.html "org.apache.spark.scheduler.SparkListener") with Logging
Simple SparkListener that logs a few summary statistics when each stage completes.
Simple SparkListener that logs a few summary statistics when each stage completes.

Annotations
     @DeveloperApi()
  41. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/TaskInfo.html "Permalink") class [TaskInfo](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/TaskInfo.html ":: DeveloperApi :: Information about a running task attempt inside a TaskSet.") extends Cloneable
Information about a running task attempt inside a TaskSet.
Information about a running task attempt inside a TaskSet.

Annotations
     @DeveloperApi()
  42. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerExecutorBlacklisted.html "Permalink") case class [SparkListenerExecutorBlacklisted](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerExecutorBlacklisted.html)(time: Long, executorId: String, taskFailures: Int) extends [SparkListenerEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html "org.apache.spark.scheduler.SparkListenerEvent") with Product with Serializable

Annotations
     @DeveloperApi() @deprecated

Deprecated

_(Since version 3.1.0)_ use SparkListenerExecutorExcluded instead
  43. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerExecutorBlacklistedForStage.html "Permalink") case class [SparkListenerExecutorBlacklistedForStage](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerExecutorBlacklistedForStage.html)(time: Long, executorId: String, taskFailures: Int, stageId: Int, stageAttemptId: Int) extends [SparkListenerEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html "org.apache.spark.scheduler.SparkListenerEvent") with Product with Serializable

Annotations
     @deprecated @DeveloperApi()

Deprecated

_(Since version 3.1.0)_ use SparkListenerExecutorExcludedForStage instead
  44. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerExecutorUnblacklisted.html "Permalink") case class [SparkListenerExecutorUnblacklisted](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerExecutorUnblacklisted.html)(time: Long, executorId: String) extends [SparkListenerEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html "org.apache.spark.scheduler.SparkListenerEvent") with Product with Serializable

Annotations
     @deprecated @DeveloperApi()

Deprecated

_(Since version 3.1.0)_ use SparkListenerExecutorUnexcluded instead
  45. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerNodeBlacklisted.html "Permalink") case class [SparkListenerNodeBlacklisted](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerNodeBlacklisted.html)(time: Long, hostId: String, executorFailures: Int) extends [SparkListenerEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html "org.apache.spark.scheduler.SparkListenerEvent") with Product with Serializable

Annotations
     @deprecated @DeveloperApi()

Deprecated

_(Since version 3.1.0)_ use SparkListenerNodeExcluded instead
  46. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerNodeBlacklistedForStage.html "Permalink") case class [SparkListenerNodeBlacklistedForStage](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerNodeBlacklistedForStage.html)(time: Long, hostId: String, executorFailures: Int, stageId: Int, stageAttemptId: Int) extends [SparkListenerEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html "org.apache.spark.scheduler.SparkListenerEvent") with Product with Serializable

Annotations
     @deprecated @DeveloperApi()

Deprecated

_(Since version 3.1.0)_ use SparkListenerNodeExcludedForStage instead
  47. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerNodeUnblacklisted.html "Permalink") case class [SparkListenerNodeUnblacklisted](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerNodeUnblacklisted.html)(time: Long, hostId: String) extends [SparkListenerEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html "org.apache.spark.scheduler.SparkListenerEvent") with Product with Serializable

Annotations
     @deprecated @DeveloperApi()

Deprecated

_(Since version 3.1.0)_ use SparkListenerNodeUnexcluded instead

  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/InputFormatInfo$.html "Permalink") object [InputFormatInfo](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/InputFormatInfo$.html)
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/JobSucceeded$.html "Permalink") case object [JobSucceeded](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/JobSucceeded$.html) extends [JobResult](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/JobResult.html "org.apache.spark.scheduler.JobResult") with Product with Serializable

Annotations
     @DeveloperApi()
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SchedulingMode$.html "Permalink") object [SchedulingMode](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SchedulingMode$.html ""FAIR" and "FIFO" determines which policy is used to order tasks amongst a Schedulable's sub-queues "NONE" is used when the a Schedulable has no sub-queues.") extends Enumeration
"FAIR" and "FIFO" determines which policy is used to order tasks amongst a Schedulable's sub-queues "NONE" is used when the a Schedulable has no sub-queues.
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SplitInfo$.html "Permalink") object [SplitInfo](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SplitInfo$.html)
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/TaskLocality$.html "Permalink") object [TaskLocality](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/TaskLocality$.html) extends Enumeration

Annotations
     @DeveloperApi()
