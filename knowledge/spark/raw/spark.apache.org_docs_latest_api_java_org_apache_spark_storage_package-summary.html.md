[Skip navigation links](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/package-summary.html#skip-navbar-top "Skip navigation links")
  * [Overview](https://spark.apache.org/docs/latest/api/java/index.html)
  * Package
  * Class
  * [Deprecated](https://spark.apache.org/docs/latest/api/java/deprecated-list.html)
  * [Index](https://spark.apache.org/docs/latest/api/java/index-all.html)
  * [Help](https://spark.apache.org/docs/latest/api/java/help-doc.html#package)


  * Package: 
  * Description | 
  * [Related Packages](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/package-summary.html#related-package-summary) | 
  * [Classes and Interfaces](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/package-summary.html#class-summary)


SEARCH:
# Package org.apache.spark.storage
* * *
package org.apache.spark.storage
  * Related Packages
Package
Description
[org.apache.spark](https://spark.apache.org/docs/latest/api/java/org/apache/spark/package-summary.html)
Core Spark classes in Scala.
[org.apache.spark.storage.memory](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/memory/package-summary.html)
  * All Classes and InterfacesInterfacesClassesEnum ClassesExceptions
Class
Description
[BasicBlockReplicationPolicy](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/BasicBlockReplicationPolicy.html "class in org.apache.spark.storage")
[BlockData](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/BlockData.html "interface in org.apache.spark.storage")
Abstracts away how blocks are stored and provides different ways to read the underlying block data.
[BlockId](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/BlockId.html "class in org.apache.spark.storage")
Developer API Identifies a particular Block of data, usually associated with a single file.
[BlockInfoWrapper](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/BlockInfoWrapper.html "class in org.apache.spark.storage")
[BlockManagerId](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/BlockManagerId.html "class in org.apache.spark.storage")
Developer API This class represent a unique identifier for a BlockManager.
[BlockManagerMessages](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/BlockManagerMessages.html "class in org.apache.spark.storage")
[BlockManagerMessages.BlockLocationsAndStatus](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/BlockManagerMessages.BlockLocationsAndStatus.html "class in org.apache.spark.storage")
The response message of `GetLocationsAndStatus` request.
[BlockManagerMessages.BlockLocationsAndStatus$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/BlockManagerMessages.BlockLocationsAndStatus$.html "class in org.apache.spark.storage")
[BlockManagerMessages.BlockManagerHeartbeat](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/BlockManagerMessages.BlockManagerHeartbeat.html "class in org.apache.spark.storage")
[BlockManagerMessages.BlockManagerHeartbeat$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/BlockManagerMessages.BlockManagerHeartbeat$.html "class in org.apache.spark.storage")
[BlockManagerMessages.DecommissionBlockManager$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/BlockManagerMessages.DecommissionBlockManager$.html "class in org.apache.spark.storage")
[BlockManagerMessages.DecommissionBlockManagers](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/BlockManagerMessages.DecommissionBlockManagers.html "class in org.apache.spark.storage")
[BlockManagerMessages.DecommissionBlockManagers$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/BlockManagerMessages.DecommissionBlockManagers$.html "class in org.apache.spark.storage")
[BlockManagerMessages.GetBlockStatus](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/BlockManagerMessages.GetBlockStatus.html "class in org.apache.spark.storage")
[BlockManagerMessages.GetBlockStatus$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/BlockManagerMessages.GetBlockStatus$.html "class in org.apache.spark.storage")
[BlockManagerMessages.GetExecutorEndpointRef](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/BlockManagerMessages.GetExecutorEndpointRef.html "class in org.apache.spark.storage")
[BlockManagerMessages.GetExecutorEndpointRef$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/BlockManagerMessages.GetExecutorEndpointRef$.html "class in org.apache.spark.storage")
[BlockManagerMessages.GetLocations](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/BlockManagerMessages.GetLocations.html "class in org.apache.spark.storage")
[BlockManagerMessages.GetLocations$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/BlockManagerMessages.GetLocations$.html "class in org.apache.spark.storage")
[BlockManagerMessages.GetLocationsAndStatus](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/BlockManagerMessages.GetLocationsAndStatus.html "class in org.apache.spark.storage")
[BlockManagerMessages.GetLocationsAndStatus$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/BlockManagerMessages.GetLocationsAndStatus$.html "class in org.apache.spark.storage")
[BlockManagerMessages.GetLocationsMultipleBlockIds](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/BlockManagerMessages.GetLocationsMultipleBlockIds.html "class in org.apache.spark.storage")
[BlockManagerMessages.GetLocationsMultipleBlockIds$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/BlockManagerMessages.GetLocationsMultipleBlockIds$.html "class in org.apache.spark.storage")
[BlockManagerMessages.GetMatchingBlockIds](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/BlockManagerMessages.GetMatchingBlockIds.html "class in org.apache.spark.storage")
[BlockManagerMessages.GetMatchingBlockIds$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/BlockManagerMessages.GetMatchingBlockIds$.html "class in org.apache.spark.storage")
[BlockManagerMessages.GetMemoryStatus$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/BlockManagerMessages.GetMemoryStatus$.html "class in org.apache.spark.storage")
[BlockManagerMessages.GetPeers](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/BlockManagerMessages.GetPeers.html "class in org.apache.spark.storage")
[BlockManagerMessages.GetPeers$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/BlockManagerMessages.GetPeers$.html "class in org.apache.spark.storage")
[BlockManagerMessages.GetRDDBlockVisibility](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/BlockManagerMessages.GetRDDBlockVisibility.html "class in org.apache.spark.storage")
[BlockManagerMessages.GetRDDBlockVisibility$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/BlockManagerMessages.GetRDDBlockVisibility$.html "class in org.apache.spark.storage")
[BlockManagerMessages.GetReplicateInfoForRDDBlocks](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/BlockManagerMessages.GetReplicateInfoForRDDBlocks.html "class in org.apache.spark.storage")
[BlockManagerMessages.GetReplicateInfoForRDDBlocks$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/BlockManagerMessages.GetReplicateInfoForRDDBlocks$.html "class in org.apache.spark.storage")
[BlockManagerMessages.GetShufflePushMergerLocations](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/BlockManagerMessages.GetShufflePushMergerLocations.html "class in org.apache.spark.storage")
[BlockManagerMessages.GetShufflePushMergerLocations$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/BlockManagerMessages.GetShufflePushMergerLocations$.html "class in org.apache.spark.storage")
[BlockManagerMessages.GetStorageStatus$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/BlockManagerMessages.GetStorageStatus$.html "class in org.apache.spark.storage")
[BlockManagerMessages.IsExecutorAlive](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/BlockManagerMessages.IsExecutorAlive.html "class in org.apache.spark.storage")
[BlockManagerMessages.IsExecutorAlive$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/BlockManagerMessages.IsExecutorAlive$.html "class in org.apache.spark.storage")
[BlockManagerMessages.MarkRDDBlockAsVisible](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/BlockManagerMessages.MarkRDDBlockAsVisible.html "class in org.apache.spark.storage")
[BlockManagerMessages.MarkRDDBlockAsVisible$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/BlockManagerMessages.MarkRDDBlockAsVisible$.html "class in org.apache.spark.storage")
[BlockManagerMessages.RegisterBlockManager](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/BlockManagerMessages.RegisterBlockManager.html "class in org.apache.spark.storage")
[BlockManagerMessages.RegisterBlockManager$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/BlockManagerMessages.RegisterBlockManager$.html "class in org.apache.spark.storage")
[BlockManagerMessages.RemoveBlock](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/BlockManagerMessages.RemoveBlock.html "class in org.apache.spark.storage")
[BlockManagerMessages.RemoveBlock$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/BlockManagerMessages.RemoveBlock$.html "class in org.apache.spark.storage")
[BlockManagerMessages.RemoveBroadcast](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/BlockManagerMessages.RemoveBroadcast.html "class in org.apache.spark.storage")
[BlockManagerMessages.RemoveBroadcast$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/BlockManagerMessages.RemoveBroadcast$.html "class in org.apache.spark.storage")
[BlockManagerMessages.RemoveExecutor](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/BlockManagerMessages.RemoveExecutor.html "class in org.apache.spark.storage")
[BlockManagerMessages.RemoveExecutor$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/BlockManagerMessages.RemoveExecutor$.html "class in org.apache.spark.storage")
[BlockManagerMessages.RemoveRdd](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/BlockManagerMessages.RemoveRdd.html "class in org.apache.spark.storage")
[BlockManagerMessages.RemoveRdd$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/BlockManagerMessages.RemoveRdd$.html "class in org.apache.spark.storage")
[BlockManagerMessages.RemoveShuffle](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/BlockManagerMessages.RemoveShuffle.html "class in org.apache.spark.storage")
[BlockManagerMessages.RemoveShuffle$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/BlockManagerMessages.RemoveShuffle$.html "class in org.apache.spark.storage")
[BlockManagerMessages.RemoveShufflePushMergerLocation](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/BlockManagerMessages.RemoveShufflePushMergerLocation.html "class in org.apache.spark.storage")
[BlockManagerMessages.RemoveShufflePushMergerLocation$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/BlockManagerMessages.RemoveShufflePushMergerLocation$.html "class in org.apache.spark.storage")
[BlockManagerMessages.ReplicateBlock](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/BlockManagerMessages.ReplicateBlock.html "class in org.apache.spark.storage")
[BlockManagerMessages.ReplicateBlock$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/BlockManagerMessages.ReplicateBlock$.html "class in org.apache.spark.storage")
[BlockManagerMessages.StopBlockManagerMaster$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/BlockManagerMessages.StopBlockManagerMaster$.html "class in org.apache.spark.storage")
[BlockManagerMessages.ToBlockManagerMaster](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/BlockManagerMessages.ToBlockManagerMaster.html "interface in org.apache.spark.storage")
[BlockManagerMessages.ToBlockManagerMasterStorageEndpoint](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/BlockManagerMessages.ToBlockManagerMasterStorageEndpoint.html "interface in org.apache.spark.storage")
[BlockManagerMessages.TriggerHeapHistogram$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/BlockManagerMessages.TriggerHeapHistogram$.html "class in org.apache.spark.storage")
Driver to Executor message to get a heap histogram.
[BlockManagerMessages.TriggerThreadDump$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/BlockManagerMessages.TriggerThreadDump$.html "class in org.apache.spark.storage")
Driver to Executor message to trigger a thread dump.
[BlockManagerMessages.UpdateBlockInfo](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/BlockManagerMessages.UpdateBlockInfo.html "class in org.apache.spark.storage")
[BlockManagerMessages.UpdateBlockInfo$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/BlockManagerMessages.UpdateBlockInfo$.html "class in org.apache.spark.storage")
[BlockManagerMessages.UpdateRDDBlockTaskInfo](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/BlockManagerMessages.UpdateRDDBlockTaskInfo.html "class in org.apache.spark.storage")
[BlockManagerMessages.UpdateRDDBlockTaskInfo$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/BlockManagerMessages.UpdateRDDBlockTaskInfo$.html "class in org.apache.spark.storage")
[BlockManagerMessages.UpdateRDDBlockVisibility](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/BlockManagerMessages.UpdateRDDBlockVisibility.html "class in org.apache.spark.storage")
[BlockManagerMessages.UpdateRDDBlockVisibility$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/BlockManagerMessages.UpdateRDDBlockVisibility$.html "class in org.apache.spark.storage")
[BlockNotFoundException](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/BlockNotFoundException.html "class in org.apache.spark.storage")
[BlockReplicationPolicy](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/BlockReplicationPolicy.html "interface in org.apache.spark.storage")
::DeveloperApi:: BlockReplicationPrioritization provides logic for prioritizing a sequence of peers for replicating blocks.
[BlockReplicationUtils](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/BlockReplicationUtils.html "class in org.apache.spark.storage")
[BlockStatus](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/BlockStatus.html "class in org.apache.spark.storage")
[BlockUpdatedInfo](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/BlockUpdatedInfo.html "class in org.apache.spark.storage")
Developer API Stores information about a block status in a block manager.
[BroadcastBlockId](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/BroadcastBlockId.html "class in org.apache.spark.storage")
[BufferReleasingInputStream](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/BufferReleasingInputStream.html "class in org.apache.spark.storage")
Helper class that ensures a ManagedBuffer is released upon InputStream.close() and also detects stream corruption if streamCompressedOrEncrypted is true
[CacheId](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/CacheId.html "class in org.apache.spark.storage")
[CountingWritableChannel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/CountingWritableChannel.html "class in org.apache.spark.storage")
[DefaultTopologyMapper](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/DefaultTopologyMapper.html "class in org.apache.spark.storage")
A TopologyMapper that assumes all nodes are in the same rack
[DiskBlockData](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/DiskBlockData.html "class in org.apache.spark.storage")
[FileBasedTopologyMapper](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/FileBasedTopologyMapper.html "class in org.apache.spark.storage")
A simple file based topology mapper.
[LogBlockId](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/LogBlockId.html "class in org.apache.spark.storage")
Identifies a block of log data.
[LogBlockIdGenerator](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/LogBlockIdGenerator.html "interface in org.apache.spark.storage")
LogBlockIdGenerator is responsible for generating unique LogBlockIds for log blocks.
[LogBlockType](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/LogBlockType.html "class in org.apache.spark.storage")
[LogLine](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/LogLine.html "interface in org.apache.spark.storage")
Base class representing a log line.
[PushBasedFetchHelper](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/PushBasedFetchHelper.html "class in org.apache.spark.storage")
Helper class for `ShuffleBlockFetcherIterator` that encapsulates all the push-based functionality to fetch push-merged block meta and shuffle chunks.
[PythonStreamBlockId](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/PythonStreamBlockId.html "class in org.apache.spark.storage")
[PythonWorkerLogBlockId](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/PythonWorkerLogBlockId.html "class in org.apache.spark.storage")
Identifies a block of Python worker log data.
[PythonWorkerLogBlockIdGenerator](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/PythonWorkerLogBlockIdGenerator.html "class in org.apache.spark.storage")
[PythonWorkerLogLine](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/PythonWorkerLogLine.html "class in org.apache.spark.storage")
[RandomBlockReplicationPolicy](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/RandomBlockReplicationPolicy.html "class in org.apache.spark.storage")
[RDDBlockId](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/RDDBlockId.html "class in org.apache.spark.storage")
[RDDInfo](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/RDDInfo.html "class in org.apache.spark.storage")
[ReadableChannelFileRegion](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/ReadableChannelFileRegion.html "class in org.apache.spark.storage")
[ShuffleBlockBatchId](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/ShuffleBlockBatchId.html "class in org.apache.spark.storage")
[ShuffleBlockChunkId](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/ShuffleBlockChunkId.html "class in org.apache.spark.storage")
[ShuffleBlockId](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/ShuffleBlockId.html "class in org.apache.spark.storage")
[ShuffleChecksumBlockId](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/ShuffleChecksumBlockId.html "class in org.apache.spark.storage")
[ShuffleDataBlockId](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/ShuffleDataBlockId.html "class in org.apache.spark.storage")
[ShuffleFetchCompletionListener](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/ShuffleFetchCompletionListener.html "class in org.apache.spark.storage")
A listener to be called at the completion of the ShuffleBlockFetcherIterator param: data the ShuffleBlockFetcherIterator to process
[ShuffleIndexBlockId](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/ShuffleIndexBlockId.html "class in org.apache.spark.storage")
[ShuffleMergedBlockId](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/ShuffleMergedBlockId.html "class in org.apache.spark.storage")
[ShuffleMergedDataBlockId](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/ShuffleMergedDataBlockId.html "class in org.apache.spark.storage")
[ShuffleMergedIndexBlockId](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/ShuffleMergedIndexBlockId.html "class in org.apache.spark.storage")
[ShuffleMergedMetaBlockId](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/ShuffleMergedMetaBlockId.html "class in org.apache.spark.storage")
[ShufflePushBlockId](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/ShufflePushBlockId.html "class in org.apache.spark.storage")
[StorageLevel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/StorageLevel.html "class in org.apache.spark.storage")
Developer API Flags for controlling the storage of an RDD.
[StorageLevelMapper](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/StorageLevelMapper.html "enum class in org.apache.spark.storage")
A mapper class easy to obtain storage levels based on their names.
[StorageUtils](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/StorageUtils.html "class in org.apache.spark.storage")
Helper methods for storage-related objects.
[StreamBlockId](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/StreamBlockId.html "class in org.apache.spark.storage")
[TaskResultBlockId](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/TaskResultBlockId.html "class in org.apache.spark.storage")
[TestLogBlockId](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/TestLogBlockId.html "class in org.apache.spark.storage")
[TestLogLine](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/TestLogLine.html "class in org.apache.spark.storage")
[TimeTrackingOutputStream](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/TimeTrackingOutputStream.html "class in org.apache.spark.storage")
Intercepts write calls and tracks total time spent writing in order to update shuffle write metrics.
[TopologyMapper](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/TopologyMapper.html "class in org.apache.spark.storage")
::DeveloperApi:: TopologyMapper provides topology information for a given host param: conf SparkConf to get required properties, if needed
[UnrecognizedBlockId](https://spark.apache.org/docs/latest/api/java/org/apache/spark/storage/UnrecognizedBlockId.html "class in org.apache.spark.storage")


