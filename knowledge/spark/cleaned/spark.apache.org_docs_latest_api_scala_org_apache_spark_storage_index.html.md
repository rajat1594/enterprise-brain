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
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/index.html "Permalink") package [scheduler](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/index.html "Spark's scheduling components.")
Spark's scheduling components.
Spark's scheduling components. This includes the `org.apache.spark.scheduler.DAGScheduler` and lower level `org.apache.spark.scheduler.TaskScheduler`.

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
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
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/index.html "Permalink") package storage

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BasicBlockReplicationPolicy.html)[BasicBlockReplicationPolicy](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BasicBlockReplicationPolicy.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockId$.html) [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockId.html ":: DeveloperApi :: Identifies a particular Block of data, usually associated with a single file.")[BlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockId.html ":: DeveloperApi :: Identifies a particular Block of data, usually associated with a single file.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html ":: DeveloperApi :: This class represent a unique identifier for a BlockManager.")[BlockManagerId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html ":: DeveloperApi :: This class represent a unique identifier for a BlockManager.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockNotFoundException.html)[BlockNotFoundException](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockNotFoundException.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockReplicationPolicy.html "::DeveloperApi:: BlockReplicationPrioritization provides logic for prioritizing a sequence of peers for replicating blocks.")[BlockReplicationPolicy](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockReplicationPolicy.html "::DeveloperApi:: BlockReplicationPrioritization provides logic for prioritizing a sequence of peers for replicating blocks.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockReplicationUtils$.html)[BlockReplicationUtils](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockReplicationUtils$.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockStatus$.html) [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockStatus.html)[BlockStatus](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockStatus.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockUpdatedInfo.html ":: DeveloperApi :: Stores information about a block status in a block manager.")[BlockUpdatedInfo](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockUpdatedInfo.html ":: DeveloperApi :: Stores information about a block status in a block manager.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BroadcastBlockId.html)[BroadcastBlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BroadcastBlockId.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/CacheId.html)[CacheId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/CacheId.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/DefaultTopologyMapper.html "A TopologyMapper that assumes all nodes are in the same rack")[DefaultTopologyMapper](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/DefaultTopologyMapper.html "A TopologyMapper that assumes all nodes are in the same rack")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/FileBasedTopologyMapper.html "A simple file based topology mapper.")[FileBasedTopologyMapper](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/FileBasedTopologyMapper.html "A simple file based topology mapper.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/LogBlockId$.html) [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/LogBlockId.html "Identifies a block of log data.")[LogBlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/LogBlockId.html "Identifies a block of log data.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/LogBlockIdGenerator.html "LogBlockIdGenerator is responsible for generating unique LogBlockIds for log blocks.")[LogBlockIdGenerator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/LogBlockIdGenerator.html "LogBlockIdGenerator is responsible for generating unique LogBlockIds for log blocks.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/LogBlockType$.html)[LogBlockType](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/LogBlockType$.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/LogLine$.html) [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/LogLine.html "Base class representing a log line.")[LogLine](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/LogLine.html "Base class representing a log line.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/PythonStreamBlockId.html)[PythonStreamBlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/PythonStreamBlockId.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/PythonWorkerLogBlockId.html "Identifies a block of Python worker log data.")[PythonWorkerLogBlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/PythonWorkerLogBlockId.html "Identifies a block of Python worker log data.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/PythonWorkerLogBlockIdGenerator.html)[PythonWorkerLogBlockIdGenerator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/PythonWorkerLogBlockIdGenerator.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/PythonWorkerLogLine.html)[PythonWorkerLogLine](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/PythonWorkerLogLine.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/RDDBlockId.html)[RDDBlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/RDDBlockId.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/RDDInfo.html)[RDDInfo](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/RDDInfo.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/RandomBlockReplicationPolicy.html)[RandomBlockReplicationPolicy](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/RandomBlockReplicationPolicy.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/ShuffleBlockBatchId.html)[ShuffleBlockBatchId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/ShuffleBlockBatchId.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/ShuffleBlockChunkId.html)[ShuffleBlockChunkId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/ShuffleBlockChunkId.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/ShuffleBlockId.html)[ShuffleBlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/ShuffleBlockId.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/ShuffleChecksumBlockId.html)[ShuffleChecksumBlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/ShuffleChecksumBlockId.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/ShuffleDataBlockId.html)[ShuffleDataBlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/ShuffleDataBlockId.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/ShuffleIndexBlockId.html)[ShuffleIndexBlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/ShuffleIndexBlockId.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/ShuffleMergedBlockId.html)[ShuffleMergedBlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/ShuffleMergedBlockId.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/ShuffleMergedDataBlockId.html)[ShuffleMergedDataBlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/ShuffleMergedDataBlockId.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/ShuffleMergedIndexBlockId.html)[ShuffleMergedIndexBlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/ShuffleMergedIndexBlockId.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/ShuffleMergedMetaBlockId.html)[ShuffleMergedMetaBlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/ShuffleMergedMetaBlockId.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/ShufflePushBlockId.html)[ShufflePushBlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/ShufflePushBlockId.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StorageLevel$.html "Various org.apache.spark.storage.StorageLevel defined and utility functions for creating new storage levels.") [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StorageLevel.html ":: DeveloperApi :: Flags for controlling the storage of an RDD.")[StorageLevel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StorageLevel.html ":: DeveloperApi :: Flags for controlling the storage of an RDD.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StorageLevelMapper.html "A mapper class easy to obtain storage levels based on their names.")[StorageLevelMapper](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StorageLevelMapper.html "A mapper class easy to obtain storage levels based on their names.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StreamBlockId.html)[StreamBlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StreamBlockId.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/TaskResultBlockId.html)[TaskResultBlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/TaskResultBlockId.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/TestLogBlockId.html)[TestLogBlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/TestLogBlockId.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/TestLogLine.html)[TestLogLine](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/TestLogLine.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/TimeTrackingOutputStream.html "Intercepts write calls and tracks total time spent writing in order to update shuffle write metrics.")[TimeTrackingOutputStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/TimeTrackingOutputStream.html "Intercepts write calls and tracks total time spent writing in order to update shuffle write metrics.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/TopologyMapper.html "::DeveloperApi:: TopologyMapper provides topology information for a given host")[TopologyMapper](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/TopologyMapper.html "::DeveloperApi:: TopologyMapper provides topology information for a given host")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/UnrecognizedBlockId.html)[UnrecognizedBlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/UnrecognizedBlockId.html)
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
# storage[ __](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/index.html "Permalink")
####  package storage
__ __
Ordering
  1. Alphabetic

Visibility
  1. Public
  2. Protected

### Type Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BasicBlockReplicationPolicy.html "Permalink") class [BasicBlockReplicationPolicy](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BasicBlockReplicationPolicy.html) extends [BlockReplicationPolicy](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockReplicationPolicy.html "org.apache.spark.storage.BlockReplicationPolicy") with Logging

Annotations
     @DeveloperApi()
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockId.html "Permalink") sealed abstract  class [BlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockId.html ":: DeveloperApi :: Identifies a particular Block of data, usually associated with a single file.") extends AnyRef
Identifies a particular Block of data, usually associated with a single file.
Identifies a particular Block of data, usually associated with a single file. A Block can be uniquely identified by its filename, but each type of Block has a different set of keys which produce its unique name.
If your BlockId should be serializable, be sure to add it to the BlockId.apply() method.

Annotations
     @DeveloperApi()
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html "Permalink") class [BlockManagerId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html ":: DeveloperApi :: This class represent a unique identifier for a BlockManager.") extends [Externalizable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Externalizable.html#java.io.Externalizable "java.io.Externalizable")
This class represent a unique identifier for a BlockManager.
This class represent a unique identifier for a BlockManager.
The first 2 constructors of this class are made private to ensure that BlockManagerId objects can be created only using the apply method in the companion object. This allows de-duplication of ID objects. Also, constructor parameters are private to ensure that parameters cannot be modified from outside this class.

Annotations
     @DeveloperApi()
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockNotFoundException.html "Permalink") class [BlockNotFoundException](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockNotFoundException.html) extends Exception
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockReplicationPolicy.html "Permalink") trait [BlockReplicationPolicy](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockReplicationPolicy.html "::DeveloperApi:: BlockReplicationPrioritization provides logic for prioritizing a sequence of peers for replicating blocks.") extends AnyRef
::DeveloperApi:: BlockReplicationPrioritization provides logic for prioritizing a sequence of peers for replicating blocks.
::DeveloperApi:: BlockReplicationPrioritization provides logic for prioritizing a sequence of peers for replicating blocks. BlockManager will replicate to each peer returned in order until the desired replication order is reached. If a replication fails, prioritize() will be called again to get a fresh prioritization.

Annotations
     @DeveloperApi()
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockStatus.html "Permalink") case class [BlockStatus](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockStatus.html)(storageLevel: [StorageLevel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StorageLevel.html "org.apache.spark.storage.StorageLevel"), memSize: Long, diskSize: Long) extends Product with Serializable

Annotations
     @DeveloperApi()
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockUpdatedInfo.html "Permalink") case class [BlockUpdatedInfo](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockUpdatedInfo.html ":: DeveloperApi :: Stores information about a block status in a block manager.")(blockManagerId: [BlockManagerId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html "org.apache.spark.storage.BlockManagerId"), blockId: [BlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockId.html "org.apache.spark.storage.BlockId"), storageLevel: [StorageLevel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StorageLevel.html "org.apache.spark.storage.StorageLevel"), memSize: Long, diskSize: Long) extends Product with Serializable
Stores information about a block status in a block manager.
Stores information about a block status in a block manager.

Annotations
     @DeveloperApi()
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BroadcastBlockId.html "Permalink") case class [BroadcastBlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BroadcastBlockId.html)(broadcastId: Long, field: String = "") extends [BlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockId.html "org.apache.spark.storage.BlockId") with Product with Serializable

Annotations
     @DeveloperApi()
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/CacheId.html "Permalink") case class [CacheId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/CacheId.html)(sessionUUID: String, hash: String) extends [BlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockId.html "org.apache.spark.storage.BlockId") with Product with Serializable

Annotations
     @DeveloperApi()
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/DefaultTopologyMapper.html "Permalink") class [DefaultTopologyMapper](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/DefaultTopologyMapper.html "A TopologyMapper that assumes all nodes are in the same rack") extends [TopologyMapper](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/TopologyMapper.html "org.apache.spark.storage.TopologyMapper") with Logging
A TopologyMapper that assumes all nodes are in the same rack
A TopologyMapper that assumes all nodes are in the same rack

Annotations
     @DeveloperApi()
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/FileBasedTopologyMapper.html "Permalink") class [FileBasedTopologyMapper](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/FileBasedTopologyMapper.html "A simple file based topology mapper.") extends [TopologyMapper](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/TopologyMapper.html "org.apache.spark.storage.TopologyMapper") with Logging
A simple file based topology mapper.
A simple file based topology mapper. This expects topology information provided as a `java.util.Properties` file. The name of the file is obtained from SparkConf property `spark.storage.replication.topologyFile`. To use this topology mapper, set the `spark.storage.replication.topologyMapper` property to [org.apache.spark.storage.FileBasedTopologyMapper](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/FileBasedTopologyMapper.html "org.apache.spark.storage.FileBasedTopologyMapper")

Annotations
     @DeveloperApi()
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/LogBlockId.html "Permalink") sealed abstract  class [LogBlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/LogBlockId.html "Identifies a block of log data.") extends [BlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockId.html "org.apache.spark.storage.BlockId")
Identifies a block of log data.
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/LogBlockIdGenerator.html "Permalink") trait [LogBlockIdGenerator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/LogBlockIdGenerator.html "LogBlockIdGenerator is responsible for generating unique LogBlockIds for log blocks.") extends AnyRef
LogBlockIdGenerator is responsible for generating unique LogBlockIds for log blocks.
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/LogLine.html "Permalink") trait [LogLine](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/LogLine.html "Base class representing a log line.") extends AnyRef
Base class representing a log line.
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/PythonStreamBlockId.html "Permalink") case class [PythonStreamBlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/PythonStreamBlockId.html)(streamId: Int, uniqueId: Long) extends [BlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockId.html "org.apache.spark.storage.BlockId") with Product with Serializable

Annotations
     @DeveloperApi()
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/PythonWorkerLogBlockId.html "Permalink") case class [PythonWorkerLogBlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/PythonWorkerLogBlockId.html "Identifies a block of Python worker log data.")(lastLogTime: Long, executorId: String, sessionId: String, workerId: String) extends [LogBlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/LogBlockId.html "org.apache.spark.storage.LogBlockId") with Product with Serializable
Identifies a block of Python worker log data.
Identifies a block of Python worker log data.

lastLogTime

the timestamp of the last log entry in this block, used for filtering and log management.

executorId

the ID of the executor that produced this log block.

sessionId

the session ID to isolate the logs.

workerId

the worker ID to distinguish the Python worker process.

Annotations
     @DeveloperApi()
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/PythonWorkerLogBlockIdGenerator.html "Permalink") class [PythonWorkerLogBlockIdGenerator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/PythonWorkerLogBlockIdGenerator.html) extends [LogBlockIdGenerator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/LogBlockIdGenerator.html "org.apache.spark.storage.LogBlockIdGenerator")
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/PythonWorkerLogLine.html "Permalink") case class [PythonWorkerLogLine](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/PythonWorkerLogLine.html)(eventTime: Long, sequenceId: Long, message: String) extends [LogLine](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/LogLine.html "org.apache.spark.storage.LogLine") with Product with Serializable
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/RDDBlockId.html "Permalink") case class [RDDBlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/RDDBlockId.html)(rddId: Int, splitIndex: Int) extends [BlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockId.html "org.apache.spark.storage.BlockId") with Product with Serializable

Annotations
     @DeveloperApi()
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/RDDInfo.html "Permalink") class [RDDInfo](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/RDDInfo.html) extends Ordered[[RDDInfo](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/RDDInfo.html "org.apache.spark.storage.RDDInfo")]

Annotations
     @DeveloperApi()
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/RandomBlockReplicationPolicy.html "Permalink") class [RandomBlockReplicationPolicy](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/RandomBlockReplicationPolicy.html) extends [BlockReplicationPolicy](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockReplicationPolicy.html "org.apache.spark.storage.BlockReplicationPolicy") with Logging

Annotations
     @DeveloperApi()
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/ShuffleBlockBatchId.html "Permalink") case class [ShuffleBlockBatchId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/ShuffleBlockBatchId.html)(shuffleId: Int, mapId: Long, startReduceId: Int, endReduceId: Int) extends [BlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockId.html "org.apache.spark.storage.BlockId") with Product with Serializable

Annotations
     @DeveloperApi()
  23. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/ShuffleBlockChunkId.html "Permalink") case class [ShuffleBlockChunkId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/ShuffleBlockChunkId.html)(shuffleId: Int, shuffleMergeId: Int, reduceId: Int, chunkId: Int) extends [BlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockId.html "org.apache.spark.storage.BlockId") with Product with Serializable

Annotations
     @Since("3.2.0") @DeveloperApi()
  24. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/ShuffleBlockId.html "Permalink") case class [ShuffleBlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/ShuffleBlockId.html)(shuffleId: Int, mapId: Long, reduceId: Int) extends [BlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockId.html "org.apache.spark.storage.BlockId") with Product with Serializable

Annotations
     @DeveloperApi()
  25. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/ShuffleChecksumBlockId.html "Permalink") case class [ShuffleChecksumBlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/ShuffleChecksumBlockId.html)(shuffleId: Int, mapId: Long, reduceId: Int) extends [BlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockId.html "org.apache.spark.storage.BlockId") with Product with Serializable

Annotations
     @Since("3.2.0") @DeveloperApi()
  26. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/ShuffleDataBlockId.html "Permalink") case class [ShuffleDataBlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/ShuffleDataBlockId.html)(shuffleId: Int, mapId: Long, reduceId: Int) extends [BlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockId.html "org.apache.spark.storage.BlockId") with Product with Serializable

Annotations
     @DeveloperApi()
  27. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/ShuffleIndexBlockId.html "Permalink") case class [ShuffleIndexBlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/ShuffleIndexBlockId.html)(shuffleId: Int, mapId: Long, reduceId: Int) extends [BlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockId.html "org.apache.spark.storage.BlockId") with Product with Serializable

Annotations
     @DeveloperApi()
  28. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/ShuffleMergedBlockId.html "Permalink") case class [ShuffleMergedBlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/ShuffleMergedBlockId.html)(shuffleId: Int, shuffleMergeId: Int, reduceId: Int) extends [BlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockId.html "org.apache.spark.storage.BlockId") with Product with Serializable

Annotations
     @Since("3.2.0") @DeveloperApi()
  29. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/ShuffleMergedDataBlockId.html "Permalink") case class [ShuffleMergedDataBlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/ShuffleMergedDataBlockId.html)(appId: String, shuffleId: Int, shuffleMergeId: Int, reduceId: Int) extends [BlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockId.html "org.apache.spark.storage.BlockId") with Product with Serializable

Annotations
     @Since("3.2.0") @DeveloperApi()
  30. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/ShuffleMergedIndexBlockId.html "Permalink") case class [ShuffleMergedIndexBlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/ShuffleMergedIndexBlockId.html)(appId: String, shuffleId: Int, shuffleMergeId: Int, reduceId: Int) extends [BlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockId.html "org.apache.spark.storage.BlockId") with Product with Serializable

Annotations
     @Since("3.2.0") @DeveloperApi()
  31. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/ShuffleMergedMetaBlockId.html "Permalink") case class [ShuffleMergedMetaBlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/ShuffleMergedMetaBlockId.html)(appId: String, shuffleId: Int, shuffleMergeId: Int, reduceId: Int) extends [BlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockId.html "org.apache.spark.storage.BlockId") with Product with Serializable

Annotations
     @Since("3.2.0") @DeveloperApi()
  32. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/ShufflePushBlockId.html "Permalink") case class [ShufflePushBlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/ShufflePushBlockId.html)(shuffleId: Int, shuffleMergeId: Int, mapIndex: Int, reduceId: Int) extends [BlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockId.html "org.apache.spark.storage.BlockId") with Product with Serializable

Annotations
     @Since("3.2.0") @DeveloperApi()
  33. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StorageLevel.html "Permalink") class [StorageLevel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StorageLevel.html ":: DeveloperApi :: Flags for controlling the storage of an RDD.") extends [Externalizable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Externalizable.html#java.io.Externalizable "java.io.Externalizable")
Flags for controlling the storage of an RDD.
Flags for controlling the storage of an RDD. Each StorageLevel records whether to use memory, or ExternalBlockStore, whether to drop the RDD to disk if it falls out of memory or ExternalBlockStore, whether to keep the data in memory in a serialized format, and whether to replicate the RDD partitions on multiple nodes.
The [org.apache.spark.storage.StorageLevel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StorageLevel.html "org.apache.spark.storage.StorageLevel") singleton object contains some static constants for commonly useful storage levels. To create your own storage level object, use the factory method of the singleton object (`StorageLevel(...)`).

Annotations
     @DeveloperApi()
  34. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StorageLevelMapper.html "Permalink") sealed final  class [StorageLevelMapper](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StorageLevelMapper.html "A mapper class easy to obtain storage levels based on their names.") extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#java.lang.Enum "java.lang.Enum")[[StorageLevelMapper](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StorageLevelMapper.html "org.apache.spark.storage.StorageLevelMapper")]
A mapper class easy to obtain storage levels based on their names.
  35. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StreamBlockId.html "Permalink") case class [StreamBlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StreamBlockId.html)(streamId: Int, uniqueId: Long) extends [BlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockId.html "org.apache.spark.storage.BlockId") with Product with Serializable

Annotations
     @DeveloperApi()
  36. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/TaskResultBlockId.html "Permalink") case class [TaskResultBlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/TaskResultBlockId.html)(taskId: Long) extends [BlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockId.html "org.apache.spark.storage.BlockId") with Product with Serializable

Annotations
     @DeveloperApi()
  37. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/TestLogBlockId.html "Permalink") case class [TestLogBlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/TestLogBlockId.html)(lastLogTime: Long, executorId: String) extends [LogBlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/LogBlockId.html "org.apache.spark.storage.LogBlockId") with Product with Serializable
  38. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/TestLogLine.html "Permalink") case class [TestLogLine](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/TestLogLine.html)(eventTime: Long, sequenceId: Long, message: String) extends [LogLine](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/LogLine.html "org.apache.spark.storage.LogLine") with Product with Serializable
  39. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/TimeTrackingOutputStream.html "Permalink") final  class [TimeTrackingOutputStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/TimeTrackingOutputStream.html "Intercepts write calls and tracks total time spent writing in order to update shuffle write metrics.") extends [OutputStream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/OutputStream.html#java.io.OutputStream "java.io.OutputStream")
Intercepts write calls and tracks total time spent writing in order to update shuffle write metrics.
Intercepts write calls and tracks total time spent writing in order to update shuffle write metrics. Not thread safe.

Annotations
     @Private()
  40. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/TopologyMapper.html "Permalink") abstract  class [TopologyMapper](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/TopologyMapper.html "::DeveloperApi:: TopologyMapper provides topology information for a given host") extends AnyRef
::DeveloperApi:: TopologyMapper provides topology information for a given host
::DeveloperApi:: TopologyMapper provides topology information for a given host

Annotations
     @DeveloperApi()
  41. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/UnrecognizedBlockId.html "Permalink") class [UnrecognizedBlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/UnrecognizedBlockId.html) extends [SparkException](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkException.html "org.apache.spark.SparkException")

Annotations
     @DeveloperApi()

### Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockId$.html "Permalink") object [BlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockId$.html)

Annotations
     @DeveloperApi()
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockReplicationUtils$.html "Permalink") object [BlockReplicationUtils](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockReplicationUtils$.html)
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockStatus$.html "Permalink") object [BlockStatus](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockStatus$.html) extends [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable")

Annotations
     @DeveloperApi()
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/LogBlockId$.html "Permalink") object [LogBlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/LogBlockId$.html)
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/LogBlockType$.html "Permalink") object [LogBlockType](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/LogBlockType$.html) extends Enumeration
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/LogLine$.html "Permalink") object [LogLine](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/LogLine$.html)
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StorageLevel$.html "Permalink") object [StorageLevel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StorageLevel$.html "Various org.apache.spark.storage.StorageLevel defined and utility functions for creating new storage levels.") extends [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable")
Various [org.apache.spark.storage.StorageLevel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StorageLevel.html "org.apache.spark.storage.StorageLevel") defined and utility functions for creating new storage levels.

### Ungrouped
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BasicBlockReplicationPolicy.html "Permalink") class [BasicBlockReplicationPolicy](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BasicBlockReplicationPolicy.html) extends [BlockReplicationPolicy](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockReplicationPolicy.html "org.apache.spark.storage.BlockReplicationPolicy") with Logging

Annotations
     @DeveloperApi()
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockId.html "Permalink") sealed abstract  class [BlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockId.html ":: DeveloperApi :: Identifies a particular Block of data, usually associated with a single file.") extends AnyRef
Identifies a particular Block of data, usually associated with a single file.
Identifies a particular Block of data, usually associated with a single file. A Block can be uniquely identified by its filename, but each type of Block has a different set of keys which produce its unique name.
If your BlockId should be serializable, be sure to add it to the BlockId.apply() method.

Annotations
     @DeveloperApi()
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html "Permalink") class [BlockManagerId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html ":: DeveloperApi :: This class represent a unique identifier for a BlockManager.") extends [Externalizable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Externalizable.html#java.io.Externalizable "java.io.Externalizable")
This class represent a unique identifier for a BlockManager.
This class represent a unique identifier for a BlockManager.
The first 2 constructors of this class are made private to ensure that BlockManagerId objects can be created only using the apply method in the companion object. This allows de-duplication of ID objects. Also, constructor parameters are private to ensure that parameters cannot be modified from outside this class.

Annotations
     @DeveloperApi()
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockNotFoundException.html "Permalink") class [BlockNotFoundException](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockNotFoundException.html) extends Exception
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockReplicationPolicy.html "Permalink") trait [BlockReplicationPolicy](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockReplicationPolicy.html "::DeveloperApi:: BlockReplicationPrioritization provides logic for prioritizing a sequence of peers for replicating blocks.") extends AnyRef
::DeveloperApi:: BlockReplicationPrioritization provides logic for prioritizing a sequence of peers for replicating blocks.
::DeveloperApi:: BlockReplicationPrioritization provides logic for prioritizing a sequence of peers for replicating blocks. BlockManager will replicate to each peer returned in order until the desired replication order is reached. If a replication fails, prioritize() will be called again to get a fresh prioritization.

Annotations
     @DeveloperApi()
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockStatus.html "Permalink") case class [BlockStatus](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockStatus.html)(storageLevel: [StorageLevel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StorageLevel.html "org.apache.spark.storage.StorageLevel"), memSize: Long, diskSize: Long) extends Product with Serializable

Annotations
     @DeveloperApi()
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockUpdatedInfo.html "Permalink") case class [BlockUpdatedInfo](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockUpdatedInfo.html ":: DeveloperApi :: Stores information about a block status in a block manager.")(blockManagerId: [BlockManagerId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html "org.apache.spark.storage.BlockManagerId"), blockId: [BlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockId.html "org.apache.spark.storage.BlockId"), storageLevel: [StorageLevel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StorageLevel.html "org.apache.spark.storage.StorageLevel"), memSize: Long, diskSize: Long) extends Product with Serializable
Stores information about a block status in a block manager.
Stores information about a block status in a block manager.

Annotations
     @DeveloperApi()
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BroadcastBlockId.html "Permalink") case class [BroadcastBlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BroadcastBlockId.html)(broadcastId: Long, field: String = "") extends [BlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockId.html "org.apache.spark.storage.BlockId") with Product with Serializable

Annotations
     @DeveloperApi()
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/CacheId.html "Permalink") case class [CacheId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/CacheId.html)(sessionUUID: String, hash: String) extends [BlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockId.html "org.apache.spark.storage.BlockId") with Product with Serializable

Annotations
     @DeveloperApi()
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/DefaultTopologyMapper.html "Permalink") class [DefaultTopologyMapper](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/DefaultTopologyMapper.html "A TopologyMapper that assumes all nodes are in the same rack") extends [TopologyMapper](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/TopologyMapper.html "org.apache.spark.storage.TopologyMapper") with Logging
A TopologyMapper that assumes all nodes are in the same rack
A TopologyMapper that assumes all nodes are in the same rack

Annotations
     @DeveloperApi()
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/FileBasedTopologyMapper.html "Permalink") class [FileBasedTopologyMapper](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/FileBasedTopologyMapper.html "A simple file based topology mapper.") extends [TopologyMapper](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/TopologyMapper.html "org.apache.spark.storage.TopologyMapper") with Logging
A simple file based topology mapper.
A simple file based topology mapper. This expects topology information provided as a `java.util.Properties` file. The name of the file is obtained from SparkConf property `spark.storage.replication.topologyFile`. To use this topology mapper, set the `spark.storage.replication.topologyMapper` property to [org.apache.spark.storage.FileBasedTopologyMapper](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/FileBasedTopologyMapper.html "org.apache.spark.storage.FileBasedTopologyMapper")

Annotations
     @DeveloperApi()
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/LogBlockId.html "Permalink") sealed abstract  class [LogBlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/LogBlockId.html "Identifies a block of log data.") extends [BlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockId.html "org.apache.spark.storage.BlockId")
Identifies a block of log data.
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/LogBlockIdGenerator.html "Permalink") trait [LogBlockIdGenerator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/LogBlockIdGenerator.html "LogBlockIdGenerator is responsible for generating unique LogBlockIds for log blocks.") extends AnyRef
LogBlockIdGenerator is responsible for generating unique LogBlockIds for log blocks.
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/LogLine.html "Permalink") trait [LogLine](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/LogLine.html "Base class representing a log line.") extends AnyRef
Base class representing a log line.
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/PythonStreamBlockId.html "Permalink") case class [PythonStreamBlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/PythonStreamBlockId.html)(streamId: Int, uniqueId: Long) extends [BlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockId.html "org.apache.spark.storage.BlockId") with Product with Serializable

Annotations
     @DeveloperApi()
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/PythonWorkerLogBlockId.html "Permalink") case class [PythonWorkerLogBlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/PythonWorkerLogBlockId.html "Identifies a block of Python worker log data.")(lastLogTime: Long, executorId: String, sessionId: String, workerId: String) extends [LogBlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/LogBlockId.html "org.apache.spark.storage.LogBlockId") with Product with Serializable
Identifies a block of Python worker log data.
Identifies a block of Python worker log data.

lastLogTime

the timestamp of the last log entry in this block, used for filtering and log management.

executorId

the ID of the executor that produced this log block.

sessionId

the session ID to isolate the logs.

workerId

the worker ID to distinguish the Python worker process.

Annotations
     @DeveloperApi()
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/PythonWorkerLogBlockIdGenerator.html "Permalink") class [PythonWorkerLogBlockIdGenerator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/PythonWorkerLogBlockIdGenerator.html) extends [LogBlockIdGenerator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/LogBlockIdGenerator.html "org.apache.spark.storage.LogBlockIdGenerator")
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/PythonWorkerLogLine.html "Permalink") case class [PythonWorkerLogLine](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/PythonWorkerLogLine.html)(eventTime: Long, sequenceId: Long, message: String) extends [LogLine](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/LogLine.html "org.apache.spark.storage.LogLine") with Product with Serializable
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/RDDBlockId.html "Permalink") case class [RDDBlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/RDDBlockId.html)(rddId: Int, splitIndex: Int) extends [BlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockId.html "org.apache.spark.storage.BlockId") with Product with Serializable

Annotations
     @DeveloperApi()
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/RDDInfo.html "Permalink") class [RDDInfo](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/RDDInfo.html) extends Ordered[[RDDInfo](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/RDDInfo.html "org.apache.spark.storage.RDDInfo")]

Annotations
     @DeveloperApi()
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/RandomBlockReplicationPolicy.html "Permalink") class [RandomBlockReplicationPolicy](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/RandomBlockReplicationPolicy.html) extends [BlockReplicationPolicy](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockReplicationPolicy.html "org.apache.spark.storage.BlockReplicationPolicy") with Logging

Annotations
     @DeveloperApi()
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/ShuffleBlockBatchId.html "Permalink") case class [ShuffleBlockBatchId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/ShuffleBlockBatchId.html)(shuffleId: Int, mapId: Long, startReduceId: Int, endReduceId: Int) extends [BlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockId.html "org.apache.spark.storage.BlockId") with Product with Serializable

Annotations
     @DeveloperApi()
  23. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/ShuffleBlockChunkId.html "Permalink") case class [ShuffleBlockChunkId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/ShuffleBlockChunkId.html)(shuffleId: Int, shuffleMergeId: Int, reduceId: Int, chunkId: Int) extends [BlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockId.html "org.apache.spark.storage.BlockId") with Product with Serializable

Annotations
     @Since("3.2.0") @DeveloperApi()
  24. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/ShuffleBlockId.html "Permalink") case class [ShuffleBlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/ShuffleBlockId.html)(shuffleId: Int, mapId: Long, reduceId: Int) extends [BlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockId.html "org.apache.spark.storage.BlockId") with Product with Serializable

Annotations
     @DeveloperApi()
  25. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/ShuffleChecksumBlockId.html "Permalink") case class [ShuffleChecksumBlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/ShuffleChecksumBlockId.html)(shuffleId: Int, mapId: Long, reduceId: Int) extends [BlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockId.html "org.apache.spark.storage.BlockId") with Product with Serializable

Annotations
     @Since("3.2.0") @DeveloperApi()
  26. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/ShuffleDataBlockId.html "Permalink") case class [ShuffleDataBlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/ShuffleDataBlockId.html)(shuffleId: Int, mapId: Long, reduceId: Int) extends [BlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockId.html "org.apache.spark.storage.BlockId") with Product with Serializable

Annotations
     @DeveloperApi()
  27. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/ShuffleIndexBlockId.html "Permalink") case class [ShuffleIndexBlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/ShuffleIndexBlockId.html)(shuffleId: Int, mapId: Long, reduceId: Int) extends [BlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockId.html "org.apache.spark.storage.BlockId") with Product with Serializable

Annotations
     @DeveloperApi()
  28. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/ShuffleMergedBlockId.html "Permalink") case class [ShuffleMergedBlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/ShuffleMergedBlockId.html)(shuffleId: Int, shuffleMergeId: Int, reduceId: Int) extends [BlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockId.html "org.apache.spark.storage.BlockId") with Product with Serializable

Annotations
     @Since("3.2.0") @DeveloperApi()
  29. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/ShuffleMergedDataBlockId.html "Permalink") case class [ShuffleMergedDataBlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/ShuffleMergedDataBlockId.html)(appId: String, shuffleId: Int, shuffleMergeId: Int, reduceId: Int) extends [BlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockId.html "org.apache.spark.storage.BlockId") with Product with Serializable

Annotations
     @Since("3.2.0") @DeveloperApi()
  30. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/ShuffleMergedIndexBlockId.html "Permalink") case class [ShuffleMergedIndexBlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/ShuffleMergedIndexBlockId.html)(appId: String, shuffleId: Int, shuffleMergeId: Int, reduceId: Int) extends [BlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockId.html "org.apache.spark.storage.BlockId") with Product with Serializable

Annotations
     @Since("3.2.0") @DeveloperApi()
  31. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/ShuffleMergedMetaBlockId.html "Permalink") case class [ShuffleMergedMetaBlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/ShuffleMergedMetaBlockId.html)(appId: String, shuffleId: Int, shuffleMergeId: Int, reduceId: Int) extends [BlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockId.html "org.apache.spark.storage.BlockId") with Product with Serializable

Annotations
     @Since("3.2.0") @DeveloperApi()
  32. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/ShufflePushBlockId.html "Permalink") case class [ShufflePushBlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/ShufflePushBlockId.html)(shuffleId: Int, shuffleMergeId: Int, mapIndex: Int, reduceId: Int) extends [BlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockId.html "org.apache.spark.storage.BlockId") with Product with Serializable

Annotations
     @Since("3.2.0") @DeveloperApi()
  33. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StorageLevel.html "Permalink") class [StorageLevel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StorageLevel.html ":: DeveloperApi :: Flags for controlling the storage of an RDD.") extends [Externalizable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Externalizable.html#java.io.Externalizable "java.io.Externalizable")
Flags for controlling the storage of an RDD.
Flags for controlling the storage of an RDD. Each StorageLevel records whether to use memory, or ExternalBlockStore, whether to drop the RDD to disk if it falls out of memory or ExternalBlockStore, whether to keep the data in memory in a serialized format, and whether to replicate the RDD partitions on multiple nodes.
The [org.apache.spark.storage.StorageLevel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StorageLevel.html "org.apache.spark.storage.StorageLevel") singleton object contains some static constants for commonly useful storage levels. To create your own storage level object, use the factory method of the singleton object (`StorageLevel(...)`).

Annotations
     @DeveloperApi()
  34. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StorageLevelMapper.html "Permalink") sealed final  class [StorageLevelMapper](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StorageLevelMapper.html "A mapper class easy to obtain storage levels based on their names.") extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#java.lang.Enum "java.lang.Enum")[[StorageLevelMapper](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StorageLevelMapper.html "org.apache.spark.storage.StorageLevelMapper")]
A mapper class easy to obtain storage levels based on their names.
  35. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StreamBlockId.html "Permalink") case class [StreamBlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StreamBlockId.html)(streamId: Int, uniqueId: Long) extends [BlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockId.html "org.apache.spark.storage.BlockId") with Product with Serializable

Annotations
     @DeveloperApi()
  36. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/TaskResultBlockId.html "Permalink") case class [TaskResultBlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/TaskResultBlockId.html)(taskId: Long) extends [BlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockId.html "org.apache.spark.storage.BlockId") with Product with Serializable

Annotations
     @DeveloperApi()
  37. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/TestLogBlockId.html "Permalink") case class [TestLogBlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/TestLogBlockId.html)(lastLogTime: Long, executorId: String) extends [LogBlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/LogBlockId.html "org.apache.spark.storage.LogBlockId") with Product with Serializable
  38. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/TestLogLine.html "Permalink") case class [TestLogLine](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/TestLogLine.html)(eventTime: Long, sequenceId: Long, message: String) extends [LogLine](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/LogLine.html "org.apache.spark.storage.LogLine") with Product with Serializable
  39. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/TimeTrackingOutputStream.html "Permalink") final  class [TimeTrackingOutputStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/TimeTrackingOutputStream.html "Intercepts write calls and tracks total time spent writing in order to update shuffle write metrics.") extends [OutputStream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/OutputStream.html#java.io.OutputStream "java.io.OutputStream")
Intercepts write calls and tracks total time spent writing in order to update shuffle write metrics.
Intercepts write calls and tracks total time spent writing in order to update shuffle write metrics. Not thread safe.

Annotations
     @Private()
  40. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/TopologyMapper.html "Permalink") abstract  class [TopologyMapper](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/TopologyMapper.html "::DeveloperApi:: TopologyMapper provides topology information for a given host") extends AnyRef
::DeveloperApi:: TopologyMapper provides topology information for a given host
::DeveloperApi:: TopologyMapper provides topology information for a given host

Annotations
     @DeveloperApi()
  41. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/UnrecognizedBlockId.html "Permalink") class [UnrecognizedBlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/UnrecognizedBlockId.html) extends [SparkException](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkException.html "org.apache.spark.SparkException")

Annotations
     @DeveloperApi()

  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockId$.html "Permalink") object [BlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockId$.html)

Annotations
     @DeveloperApi()
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockReplicationUtils$.html "Permalink") object [BlockReplicationUtils](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockReplicationUtils$.html)
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockStatus$.html "Permalink") object [BlockStatus](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockStatus$.html) extends [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable")

Annotations
     @DeveloperApi()
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/LogBlockId$.html "Permalink") object [LogBlockId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/LogBlockId$.html)
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/LogBlockType$.html "Permalink") object [LogBlockType](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/LogBlockType$.html) extends Enumeration
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/LogLine$.html "Permalink") object [LogLine](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/LogLine$.html)
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StorageLevel$.html "Permalink") object [StorageLevel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StorageLevel$.html "Various org.apache.spark.storage.StorageLevel defined and utility functions for creating new storage levels.") extends [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable")
Various [org.apache.spark.storage.StorageLevel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StorageLevel.html "org.apache.spark.storage.StorageLevel") defined and utility functions for creating new storage levels.
