[Skip navigation links](https://spark.apache.org/docs/latest/api/java/org/apache/spark/package-summary.html#skip-navbar-top "Skip navigation links")
  * [Overview](https://spark.apache.org/docs/latest/api/java/index.html)
  * Package
  * Class
  * [Deprecated](https://spark.apache.org/docs/latest/api/java/deprecated-list.html)
  * [Index](https://spark.apache.org/docs/latest/api/java/index-all.html)
  * [Help](https://spark.apache.org/docs/latest/api/java/help-doc.html#package)

  * Package:
  * [Description](https://spark.apache.org/docs/latest/api/java/org/apache/spark/package-summary.html#package-description) |
  * Related Packages |
  * [Classes and Interfaces](https://spark.apache.org/docs/latest/api/java/org/apache/spark/package-summary.html#class-summary)

SEARCH:
# Package org.apache.spark
* * *
package org.apache.spark
Core Spark classes in Scala. A few classes here, such as [`StorageLevel`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/StorageLevel.html "class in org.apache.spark.storage"), are also used in Java, but the [`org.apache.spark.api.java`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/api/java/package-summary.html) package contains the main Java API.
  * All Classes and InterfacesInterfacesClassesEnum ClassesExceptions
Class
Description
[Aggregator](https://spark.apache.org/docs/latest/api/java/org/apache/spark/Aggregator.html "class in org.apache.spark")<K,V,C>
Developer API A set of functions used to aggregate data.
[BarrierCoordinatorMessage](https://spark.apache.org/docs/latest/api/java/org/apache/spark/BarrierCoordinatorMessage.html "interface in org.apache.spark")
[BarrierTaskContext](https://spark.apache.org/docs/latest/api/java/org/apache/spark/BarrierTaskContext.html "class in org.apache.spark")
Experimental A [`TaskContext`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/TaskContext.html "class in org.apache.spark") with extra contextual info and tooling for tasks in a barrier stage.
[BarrierTaskInfo](https://spark.apache.org/docs/latest/api/java/org/apache/spark/BarrierTaskInfo.html "class in org.apache.spark")
Experimental Carries all task infos of a barrier task.
[BreakingChangeInfo](https://spark.apache.org/docs/latest/api/java/org/apache/spark/BreakingChangeInfo.html "class in org.apache.spark")
Additional information if the error was caused by a breaking change.
[CleanAccum](https://spark.apache.org/docs/latest/api/java/org/apache/spark/CleanAccum.html "class in org.apache.spark")
[CleanBroadcast](https://spark.apache.org/docs/latest/api/java/org/apache/spark/CleanBroadcast.html "class in org.apache.spark")
[CleanCheckpoint](https://spark.apache.org/docs/latest/api/java/org/apache/spark/CleanCheckpoint.html "class in org.apache.spark")
[CleanerListener](https://spark.apache.org/docs/latest/api/java/org/apache/spark/CleanerListener.html "interface in org.apache.spark")
Listener class used when any item has been cleaned by the Cleaner class.
[CleanRDD](https://spark.apache.org/docs/latest/api/java/org/apache/spark/CleanRDD.html "class in org.apache.spark")
[CleanShuffle](https://spark.apache.org/docs/latest/api/java/org/apache/spark/CleanShuffle.html "class in org.apache.spark")
[CleanSparkListener](https://spark.apache.org/docs/latest/api/java/org/apache/spark/CleanSparkListener.html "class in org.apache.spark")
[CleanupTask](https://spark.apache.org/docs/latest/api/java/org/apache/spark/CleanupTask.html "interface in org.apache.spark")
Classes that represent cleaning tasks.
[CleanupTaskWeakReference](https://spark.apache.org/docs/latest/api/java/org/apache/spark/CleanupTaskWeakReference.html "class in org.apache.spark")
A WeakReference associated with a CleanupTask.
[ComplexFutureAction](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ComplexFutureAction.html "class in org.apache.spark")<T>
A [`FutureAction`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/FutureAction.html "interface in org.apache.spark") for actions that could trigger multiple Spark jobs.
[ContextAwareIterator](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ContextAwareIterator.html "class in org.apache.spark")<T>
Deprecated.
since 4.0.0 as its only usage for Python evaluation is now extinct
[ContextBarrierId](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ContextBarrierId.html "class in org.apache.spark")
For each barrier stage attempt, only at most one barrier() call can be active at any time, thus we can use (stageId, stageAttemptId) to identify the stage attempt where the barrier() call is from.
[Dependency](https://spark.apache.org/docs/latest/api/java/org/apache/spark/Dependency.html "class in org.apache.spark")<T>
Developer API Base class for dependencies.
[ErrorClassesJsonReader](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ErrorClassesJsonReader.html "class in org.apache.spark")
A reader to load error information from one or more JSON files.
[ErrorInfo](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ErrorInfo.html "class in org.apache.spark")
Information associated with an error class.
[ErrorMessageFormat](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ErrorMessageFormat.html "class in org.apache.spark")
[ErrorStateInfo](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ErrorStateInfo.html "class in org.apache.spark")
Information associated with an error state / SQLSTATE.
[ErrorSubInfo](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ErrorSubInfo.html "class in org.apache.spark")
Information associated with an error subclass.
[ExceptionFailure](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ExceptionFailure.html "class in org.apache.spark")
Developer API Task failed due to a runtime exception.
[ExecutorLostFailure](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ExecutorLostFailure.html "class in org.apache.spark")
Developer API The task failed because the executor that it was running on was lost.
[ExecutorRegistered](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ExecutorRegistered.html "class in org.apache.spark")
[ExecutorRemoved](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ExecutorRemoved.html "class in org.apache.spark")
[ExpireDeadHosts](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ExpireDeadHosts.html "class in org.apache.spark")
[FetchFailed](https://spark.apache.org/docs/latest/api/java/org/apache/spark/FetchFailed.html "class in org.apache.spark")
Developer API Task failed to fetch shuffle data from a remote node.
[FutureAction](https://spark.apache.org/docs/latest/api/java/org/apache/spark/FutureAction.html "interface in org.apache.spark")<T>
A future for the result of an action to support cancellation.
[HashPartitioner](https://spark.apache.org/docs/latest/api/java/org/apache/spark/HashPartitioner.html "class in org.apache.spark")
A [`Partitioner`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/Partitioner.html "class in org.apache.spark") that implements hash-based partitioning using Java's `Object.hashCode`.
[InternalAccumulator](https://spark.apache.org/docs/latest/api/java/org/apache/spark/InternalAccumulator.html "class in org.apache.spark")
A collection of fields and methods concerned with internal accumulators that represent task level metrics.
[InternalAccumulator.input$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/InternalAccumulator.input$.html "class in org.apache.spark")
[InternalAccumulator.output$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/InternalAccumulator.output$.html "class in org.apache.spark")
[InternalAccumulator.shuffleRead$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/InternalAccumulator.shuffleRead$.html "class in org.apache.spark")
[InternalAccumulator.shuffleWrite$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/InternalAccumulator.shuffleWrite$.html "class in org.apache.spark")
[InterruptibleIterator](https://spark.apache.org/docs/latest/api/java/org/apache/spark/InterruptibleIterator.html "class in org.apache.spark")<T>
Developer API An iterator that wraps around an existing iterator to provide task killing functionality.
[JobExecutionStatus](https://spark.apache.org/docs/latest/api/java/org/apache/spark/JobExecutionStatus.html "enum class in org.apache.spark")
[JobSubmitter](https://spark.apache.org/docs/latest/api/java/org/apache/spark/JobSubmitter.html "interface in org.apache.spark")
Handle via which a "run" function passed to a [`ComplexFutureAction`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ComplexFutureAction.html "class in org.apache.spark") can submit jobs for execution.
[MapOutputTrackerMasterMessage](https://spark.apache.org/docs/latest/api/java/org/apache/spark/MapOutputTrackerMasterMessage.html "interface in org.apache.spark")
[MapOutputTrackerMessage](https://spark.apache.org/docs/latest/api/java/org/apache/spark/MapOutputTrackerMessage.html "interface in org.apache.spark")
[MitigationConfig](https://spark.apache.org/docs/latest/api/java/org/apache/spark/MitigationConfig.html "class in org.apache.spark")
A spark config flag that can be used to mitigate a breaking change.
[NarrowDependency](https://spark.apache.org/docs/latest/api/java/org/apache/spark/NarrowDependency.html "class in org.apache.spark")<T>
Developer API Base class for dependencies where each partition of the child RDD depends on a small number of partitions of the parent RDD.
[OneToOneDependency](https://spark.apache.org/docs/latest/api/java/org/apache/spark/OneToOneDependency.html "class in org.apache.spark")<T>
Developer API Represents a one-to-one dependency between partitions of the parent and child RDDs.
[Partition](https://spark.apache.org/docs/latest/api/java/org/apache/spark/Partition.html "interface in org.apache.spark")
An identifier for a partition in an RDD.
[Partitioner](https://spark.apache.org/docs/latest/api/java/org/apache/spark/Partitioner.html "class in org.apache.spark")
An object that defines how the elements in a key-value pair RDD are partitioned by key.
[PartitionEvaluator](https://spark.apache.org/docs/latest/api/java/org/apache/spark/PartitionEvaluator.html "interface in org.apache.spark")<T,U>
An evaluator for computing RDD partitions.
[PartitionEvaluatorFactory](https://spark.apache.org/docs/latest/api/java/org/apache/spark/PartitionEvaluatorFactory.html "interface in org.apache.spark")<T,U>
A factory to create [`PartitionEvaluator`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/PartitionEvaluator.html "interface in org.apache.spark").
[QueryContext](https://spark.apache.org/docs/latest/api/java/org/apache/spark/QueryContext.html "interface in org.apache.spark")
Query context of a [`SparkThrowable`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/SparkThrowable.html "interface in org.apache.spark").
[QueryContextType](https://spark.apache.org/docs/latest/api/java/org/apache/spark/QueryContextType.html "enum class in org.apache.spark")
The type of [`QueryContext`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/QueryContext.html "interface in org.apache.spark").
[RangeDependency](https://spark.apache.org/docs/latest/api/java/org/apache/spark/RangeDependency.html "class in org.apache.spark")<T>
Developer API Represents a one-to-one dependency between ranges of partitions in the parent and child RDDs.
[RangePartitioner](https://spark.apache.org/docs/latest/api/java/org/apache/spark/RangePartitioner.html "class in org.apache.spark")<K,V>
A [`Partitioner`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/Partitioner.html "class in org.apache.spark") that partitions sortable records by range into roughly equal ranges.
[ReadOnlySparkConf](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ReadOnlySparkConf.html "interface in org.apache.spark")
[RequestMethod](https://spark.apache.org/docs/latest/api/java/org/apache/spark/RequestMethod.html "class in org.apache.spark")
[Resubmitted](https://spark.apache.org/docs/latest/api/java/org/apache/spark/Resubmitted.html "class in org.apache.spark")
Developer API A `org.apache.spark.scheduler.ShuffleMapTask` that completed successfully earlier, but we lost the executor before the stage completed.
[SerializableWritable](https://spark.apache.org/docs/latest/api/java/org/apache/spark/SerializableWritable.html "class in org.apache.spark")<T extends org.apache.hadoop.io.Writable>
[ShuffleDependency](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ShuffleDependency.html "class in org.apache.spark")<K,V,C>
[ShuffleStatus](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ShuffleStatus.html "class in org.apache.spark")
Helper class used by the `MapOutputTrackerMaster` to perform bookkeeping for a single ShuffleMapStage.
[ShuffleStatusNotFoundException](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ShuffleStatusNotFoundException.html "class in org.apache.spark")
[SimpleFutureAction](https://spark.apache.org/docs/latest/api/java/org/apache/spark/SimpleFutureAction.html "class in org.apache.spark")<T>
A [`FutureAction`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/FutureAction.html "interface in org.apache.spark") holding the result of an action that triggers a single job.
[SparkBuildInfo](https://spark.apache.org/docs/latest/api/java/org/apache/spark/SparkBuildInfo.html "class in org.apache.spark")
[SparkConf](https://spark.apache.org/docs/latest/api/java/org/apache/spark/SparkConf.html "class in org.apache.spark")
Configuration for a Spark application.
[SparkContext](https://spark.apache.org/docs/latest/api/java/org/apache/spark/SparkContext.html "class in org.apache.spark")
Main entry point for Spark functionality.
[SparkEnv](https://spark.apache.org/docs/latest/api/java/org/apache/spark/SparkEnv.html "class in org.apache.spark")
Developer API Holds all the runtime environment objects for a running Spark instance (either master or worker), including the serializer, RpcEnv, block manager, map output tracker, etc.
[SparkException](https://spark.apache.org/docs/latest/api/java/org/apache/spark/SparkException.html "class in org.apache.spark")
[SparkExecutorInfo](https://spark.apache.org/docs/latest/api/java/org/apache/spark/SparkExecutorInfo.html "interface in org.apache.spark")
Exposes information about Spark Executors.
[SparkExecutorInfoImpl](https://spark.apache.org/docs/latest/api/java/org/apache/spark/SparkExecutorInfoImpl.html "class in org.apache.spark")
[SparkFiles](https://spark.apache.org/docs/latest/api/java/org/apache/spark/SparkFiles.html "class in org.apache.spark")
Resolves paths to files added through `SparkContext.addFile()`.
[SparkFirehoseListener](https://spark.apache.org/docs/latest/api/java/org/apache/spark/SparkFirehoseListener.html "class in org.apache.spark")
Class that allows users to receive all SparkListener events.
[SparkJobInfo](https://spark.apache.org/docs/latest/api/java/org/apache/spark/SparkJobInfo.html "interface in org.apache.spark")
Exposes information about Spark Jobs.
[SparkJobInfoImpl](https://spark.apache.org/docs/latest/api/java/org/apache/spark/SparkJobInfoImpl.html "class in org.apache.spark")
[SparkMasterRegex](https://spark.apache.org/docs/latest/api/java/org/apache/spark/SparkMasterRegex.html "class in org.apache.spark")
A collection of regexes for extracting information from the master string.
[SparkStageInfo](https://spark.apache.org/docs/latest/api/java/org/apache/spark/SparkStageInfo.html "interface in org.apache.spark")
Exposes information about Spark Stages.
[SparkStageInfoImpl](https://spark.apache.org/docs/latest/api/java/org/apache/spark/SparkStageInfoImpl.html "class in org.apache.spark")
[SparkStatusTracker](https://spark.apache.org/docs/latest/api/java/org/apache/spark/SparkStatusTracker.html "class in org.apache.spark")
Low-level status reporting APIs for monitoring job and stage progress.
[SparkThrowable](https://spark.apache.org/docs/latest/api/java/org/apache/spark/SparkThrowable.html "interface in org.apache.spark")
Interface mixed into Throwables thrown from Spark.
[SparkThrowableHelper](https://spark.apache.org/docs/latest/api/java/org/apache/spark/SparkThrowableHelper.html "class in org.apache.spark")
Companion object used by instances of [`SparkThrowable`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/SparkThrowable.html "interface in org.apache.spark") to access error class information and construct error messages.
[SpillListener](https://spark.apache.org/docs/latest/api/java/org/apache/spark/SpillListener.html "class in org.apache.spark")
A `SparkListener` that detects whether spills have occurred in Spark jobs.
[StopMapOutputTracker](https://spark.apache.org/docs/latest/api/java/org/apache/spark/StopMapOutputTracker.html "class in org.apache.spark")
[StringSubstitutor](https://spark.apache.org/docs/latest/api/java/org/apache/spark/StringSubstitutor.html "class in org.apache.spark")
[Success](https://spark.apache.org/docs/latest/api/java/org/apache/spark/Success.html "class in org.apache.spark")
Developer API Task succeeded.
[TaskCommitDenied](https://spark.apache.org/docs/latest/api/java/org/apache/spark/TaskCommitDenied.html "class in org.apache.spark")
Developer API Task requested the driver to commit, but was denied.
[TaskContext](https://spark.apache.org/docs/latest/api/java/org/apache/spark/TaskContext.html "class in org.apache.spark")
Contextual information about a task which can be read or mutated during execution.
[TaskEndReason](https://spark.apache.org/docs/latest/api/java/org/apache/spark/TaskEndReason.html "interface in org.apache.spark")
Developer API Various possible reasons why a task ended.
[TaskFailedReason](https://spark.apache.org/docs/latest/api/java/org/apache/spark/TaskFailedReason.html "interface in org.apache.spark")
Developer API Various possible reasons why a task failed.
[TaskKilled](https://spark.apache.org/docs/latest/api/java/org/apache/spark/TaskKilled.html "class in org.apache.spark")
Developer API Task was killed intentionally and needs to be rescheduled.
[TaskKilledException](https://spark.apache.org/docs/latest/api/java/org/apache/spark/TaskKilledException.html "class in org.apache.spark")
Developer API Exception thrown when a task is explicitly killed (i.e., task failure is expected).
[TaskResultLost](https://spark.apache.org/docs/latest/api/java/org/apache/spark/TaskResultLost.html "class in org.apache.spark")
Developer API The task finished successfully, but the result was lost from the executor's block manager before it was fetched.
[TaskSchedulerIsSet](https://spark.apache.org/docs/latest/api/java/org/apache/spark/TaskSchedulerIsSet.html "class in org.apache.spark")
An event that SparkContext uses to notify HeartbeatReceiver that SparkContext.taskScheduler is created.
[TaskState](https://spark.apache.org/docs/latest/api/java/org/apache/spark/TaskState.html "class in org.apache.spark")
[TestUtils](https://spark.apache.org/docs/latest/api/java/org/apache/spark/TestUtils.html "class in org.apache.spark")
Utilities for tests.
[UnknownReason](https://spark.apache.org/docs/latest/api/java/org/apache/spark/UnknownReason.html "class in org.apache.spark")
Developer API We don't know why the task ended -- for example, because of a ClassNotFound exception when deserializing the task result.
