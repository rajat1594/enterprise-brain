[Skip navigation links](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/package-summary.html#skip-navbar-top "Skip navigation links")
  * [Overview](https://spark.apache.org/docs/latest/api/java/index.html)
  * Package
  * Class
  * [Deprecated](https://spark.apache.org/docs/latest/api/java/deprecated-list.html)
  * [Index](https://spark.apache.org/docs/latest/api/java/index-all.html)
  * [Help](https://spark.apache.org/docs/latest/api/java/help-doc.html#package)

  * Package:
  * [Description](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/package-summary.html#package-description) |
  * [Related Packages](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/package-summary.html#related-package-summary) |
  * [Classes and Interfaces](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/package-summary.html#class-summary)

SEARCH:
# Package org.apache.spark.scheduler
* * *
package org.apache.spark.scheduler
Spark's DAG scheduler.
  * Related Packages
Package
Description
[org.apache.spark](https://spark.apache.org/docs/latest/api/java/org/apache/spark/package-summary.html)
Core Spark classes in Scala.
[org.apache.spark.scheduler.cluster](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/cluster/package-summary.html)
[org.apache.spark.scheduler.local](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/local/package-summary.html)
  * All Classes and InterfacesInterfacesClasses
Class
Description
[AccumulableInfo](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/AccumulableInfo.html "class in org.apache.spark.scheduler")
Developer API Information about an [`AccumulatorV2`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/util/AccumulatorV2.html "class in org.apache.spark.util") modified during a task or stage.
[AllJobsCancelled](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/AllJobsCancelled.html "class in org.apache.spark.scheduler")
[AskPermissionToCommitOutput](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/AskPermissionToCommitOutput.html "class in org.apache.spark.scheduler")
[AsyncEventQueue](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/AsyncEventQueue.html "class in org.apache.spark.scheduler")
An asynchronous queue for events.
[DAGSchedulerEvent](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/DAGSchedulerEvent.html "interface in org.apache.spark.scheduler")
Types of events that can be handled by the DAGScheduler.
[ExcludedExecutor](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/ExcludedExecutor.html "class in org.apache.spark.scheduler")
[ExecutorKilled](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/ExecutorKilled.html "class in org.apache.spark.scheduler")
[ExecutorLossMessage](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/ExecutorLossMessage.html "class in org.apache.spark.scheduler")
[ExternalClusterManager](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/ExternalClusterManager.html "interface in org.apache.spark.scheduler")
A cluster manager interface to plugin external scheduler.
[InputFormatInfo](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/InputFormatInfo.html "class in org.apache.spark.scheduler")
Developer API Parses and holds information about inputFormat (and files) specified as a parameter.
[JobFailed](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/JobFailed.html "class in org.apache.spark.scheduler")
[JobListener](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/JobListener.html "interface in org.apache.spark.scheduler")
Interface used to listen for job completion or failure events after submitting a job to the DAGScheduler.
[JobResult](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/JobResult.html "interface in org.apache.spark.scheduler")
Developer API A result of a job in the DAGScheduler.
[JobSucceeded](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/JobSucceeded.html "class in org.apache.spark.scheduler")
[LossReasonPending](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/LossReasonPending.html "class in org.apache.spark.scheduler")
A loss reason that means we don't yet know why the executor exited.
[MapStatus](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/MapStatus.html "interface in org.apache.spark.scheduler")
Result returned by a ShuffleMapTask to a scheduler.
[MiscellaneousProcessDetails](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/MiscellaneousProcessDetails.html "class in org.apache.spark.scheduler")
Developer API Stores information about an Miscellaneous Process to pass from the scheduler to SparkListeners.
[OutputCommitCoordinationMessage](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/OutputCommitCoordinationMessage.html "interface in org.apache.spark.scheduler")
[ResubmitFailedStages](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/ResubmitFailedStages.html "class in org.apache.spark.scheduler")
[RuntimePercentage](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/RuntimePercentage.html "class in org.apache.spark.scheduler")
[Schedulable](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/Schedulable.html "interface in org.apache.spark.scheduler")
An interface for schedulable entities.
[SchedulableBuilder](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/SchedulableBuilder.html "interface in org.apache.spark.scheduler")
An interface to build Schedulable tree buildPools: build the tree nodes(pools) addTaskSetManager: build the leaf nodes(TaskSetManagers)
[SchedulerBackend](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/SchedulerBackend.html "interface in org.apache.spark.scheduler")
A backend interface for scheduling systems that allows plugging in different ones under TaskSchedulerImpl.
[SchedulingAlgorithm](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/SchedulingAlgorithm.html "interface in org.apache.spark.scheduler")
An interface for sort algorithm FIFO: FIFO algorithm between TaskSetManagers FS: FS algorithm between Pools, and FIFO or FS within Pools
[SchedulingMode](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/SchedulingMode.html "class in org.apache.spark.scheduler")
"FAIR" and "FIFO" determines which policy is used to order tasks amongst a Schedulable's sub-queues "NONE" is used when the a Schedulable has no sub-queues.
[ShuffleOutputStatus](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/ShuffleOutputStatus.html "interface in org.apache.spark.scheduler")
A common trait between [`MapStatus`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/MapStatus.html "interface in org.apache.spark.scheduler") and `MergeStatus`.
[SparkListener](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/SparkListener.html "class in org.apache.spark.scheduler")
Developer API A default implementation for `SparkListenerInterface` that has no-op implementations for all callbacks.
[SparkListenerApplicationEnd](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/SparkListenerApplicationEnd.html "class in org.apache.spark.scheduler")
[SparkListenerApplicationStart](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/SparkListenerApplicationStart.html "class in org.apache.spark.scheduler")
[SparkListenerBlockManagerAdded](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/SparkListenerBlockManagerAdded.html "class in org.apache.spark.scheduler")
[SparkListenerBlockManagerRemoved](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/SparkListenerBlockManagerRemoved.html "class in org.apache.spark.scheduler")
[SparkListenerBlockUpdated](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/SparkListenerBlockUpdated.html "class in org.apache.spark.scheduler")
[SparkListenerBus](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/SparkListenerBus.html "interface in org.apache.spark.scheduler")
A [`SparkListenerEvent`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/SparkListenerEvent.html "interface in org.apache.spark.scheduler") bus that relays [`SparkListenerEvent`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/SparkListenerEvent.html "interface in org.apache.spark.scheduler")s to its listeners
[SparkListenerEnvironmentUpdate](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/SparkListenerEnvironmentUpdate.html "class in org.apache.spark.scheduler")
[SparkListenerEvent](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/SparkListenerEvent.html "interface in org.apache.spark.scheduler")
[SparkListenerExecutorAdded](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/SparkListenerExecutorAdded.html "class in org.apache.spark.scheduler")
[SparkListenerExecutorBlacklisted](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/SparkListenerExecutorBlacklisted.html "class in org.apache.spark.scheduler")
Deprecated.
use SparkListenerExecutorExcluded instead.
[SparkListenerExecutorBlacklistedForStage](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/SparkListenerExecutorBlacklistedForStage.html "class in org.apache.spark.scheduler")
Deprecated.
use SparkListenerExecutorExcludedForStage instead.
[SparkListenerExecutorExcluded](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/SparkListenerExecutorExcluded.html "class in org.apache.spark.scheduler")
[SparkListenerExecutorExcludedForStage](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/SparkListenerExecutorExcludedForStage.html "class in org.apache.spark.scheduler")
[SparkListenerExecutorMetricsUpdate](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/SparkListenerExecutorMetricsUpdate.html "class in org.apache.spark.scheduler")
Periodic updates from executors.
[SparkListenerExecutorRemoved](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/SparkListenerExecutorRemoved.html "class in org.apache.spark.scheduler")
[SparkListenerExecutorUnblacklisted](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/SparkListenerExecutorUnblacklisted.html "class in org.apache.spark.scheduler")
Deprecated.
use SparkListenerExecutorUnexcluded instead.
[SparkListenerExecutorUnexcluded](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/SparkListenerExecutorUnexcluded.html "class in org.apache.spark.scheduler")
[SparkListenerInterface](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/SparkListenerInterface.html "interface in org.apache.spark.scheduler")
Interface for listening to events from the Spark scheduler.
[SparkListenerJobEnd](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/SparkListenerJobEnd.html "class in org.apache.spark.scheduler")
[SparkListenerJobStart](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/SparkListenerJobStart.html "class in org.apache.spark.scheduler")
[SparkListenerLogStart](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/SparkListenerLogStart.html "class in org.apache.spark.scheduler")
An internal class that describes the metadata of an event log.
[SparkListenerMiscellaneousProcessAdded](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/SparkListenerMiscellaneousProcessAdded.html "class in org.apache.spark.scheduler")
[SparkListenerNodeBlacklisted](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/SparkListenerNodeBlacklisted.html "class in org.apache.spark.scheduler")
Deprecated.
use SparkListenerNodeExcluded instead.
[SparkListenerNodeBlacklistedForStage](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/SparkListenerNodeBlacklistedForStage.html "class in org.apache.spark.scheduler")
Deprecated.
use SparkListenerNodeExcludedForStage instead.
[SparkListenerNodeExcluded](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/SparkListenerNodeExcluded.html "class in org.apache.spark.scheduler")
[SparkListenerNodeExcludedForStage](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/SparkListenerNodeExcludedForStage.html "class in org.apache.spark.scheduler")
[SparkListenerNodeUnblacklisted](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/SparkListenerNodeUnblacklisted.html "class in org.apache.spark.scheduler")
Deprecated.
use SparkListenerNodeUnexcluded instead.
[SparkListenerNodeUnexcluded](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/SparkListenerNodeUnexcluded.html "class in org.apache.spark.scheduler")
[SparkListenerResourceProfileAdded](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/SparkListenerResourceProfileAdded.html "class in org.apache.spark.scheduler")
[SparkListenerSpeculativeTaskSubmitted](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/SparkListenerSpeculativeTaskSubmitted.html "class in org.apache.spark.scheduler")
[SparkListenerStageCompleted](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/SparkListenerStageCompleted.html "class in org.apache.spark.scheduler")
[SparkListenerStageExecutorMetrics](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/SparkListenerStageExecutorMetrics.html "class in org.apache.spark.scheduler")
Peak metric values for the executor for the stage, written to the history log at stage completion.
[SparkListenerStageSubmitted](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/SparkListenerStageSubmitted.html "class in org.apache.spark.scheduler")
[SparkListenerTaskEnd](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/SparkListenerTaskEnd.html "class in org.apache.spark.scheduler")
[SparkListenerTaskGettingResult](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/SparkListenerTaskGettingResult.html "class in org.apache.spark.scheduler")
[SparkListenerTaskStart](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/SparkListenerTaskStart.html "class in org.apache.spark.scheduler")
[SparkListenerUnpersistRDD](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/SparkListenerUnpersistRDD.html "class in org.apache.spark.scheduler")
[SparkListenerUnschedulableTaskSetAdded](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/SparkListenerUnschedulableTaskSetAdded.html "class in org.apache.spark.scheduler")
[SparkListenerUnschedulableTaskSetRemoved](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/SparkListenerUnschedulableTaskSetRemoved.html "class in org.apache.spark.scheduler")
[SplitInfo](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/SplitInfo.html "class in org.apache.spark.scheduler")
[StageInfo](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/StageInfo.html "class in org.apache.spark.scheduler")
Developer API Stores information about a stage to pass from the scheduler to SparkListeners.
[StatsReportListener](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/StatsReportListener.html "class in org.apache.spark.scheduler")
Developer API Simple SparkListener that logs a few summary statistics when each stage completes.
[StopCoordinator](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/StopCoordinator.html "class in org.apache.spark.scheduler")
[TaskInfo](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/TaskInfo.html "class in org.apache.spark.scheduler")
Developer API Information about a running task attempt inside a TaskSet.
[TaskLocality](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/TaskLocality.html "class in org.apache.spark.scheduler")
[TaskLocation](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/TaskLocation.html "interface in org.apache.spark.scheduler")
A location where a task should run.
[TaskResult](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/TaskResult.html "interface in org.apache.spark.scheduler")<T>
[TaskScheduler](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/TaskScheduler.html "interface in org.apache.spark.scheduler")
Low-level task scheduler interface, currently implemented exclusively by `TaskSchedulerImpl`.
