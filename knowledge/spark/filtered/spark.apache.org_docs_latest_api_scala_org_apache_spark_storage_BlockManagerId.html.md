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
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/index.html "Permalink") package [storage](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/index.html) 

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


c
[org](https://spark.apache.org/docs/latest/api/scala/org/index.html "org").[apache](https://spark.apache.org/docs/latest/api/scala/org/apache/index.html "org.apache").[spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark").[storage](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/index.html "org.apache.spark.storage")
# BlockManagerId[ __](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html "Permalink")
####  class BlockManagerId extends [Externalizable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Externalizable.html#java.io.Externalizable "java.io.Externalizable")
Developer API
This class represent a unique identifier for a BlockManager.
The first 2 constructors of this class are made private to ensure that BlockManagerId objects can be created only using the apply method in the companion object. This allows de-duplication of ID objects. Also, constructor parameters are private to ensure that parameters cannot be modified from outside this class.  

Annotations
     @DeveloperApi() 

Source
    [BlockManagerId.scala](https://github.com/apache/spark/tree/v4.1.2/core/src/main/scala/org/apache/spark/storage/BlockManagerId.scala)
Linear Supertypes
[Externalizable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Externalizable.html#java.io.Externalizable "java.io.Externalizable"), [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable"), AnyRef, Any
__ __
Ordering
  1. Alphabetic
  2. By Inheritance


Inherited  

  1. BlockManagerId
  2. Externalizable
  3. Serializable
  4. AnyRef
  5. Any


  1. Hide All
  2. Show All


Visibility
  1. Public
  2. Protected


### Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html###:Int "Permalink") final  def ##: Int 

Definition Classes
    AnyRef → Any
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0 

Definition Classes
    Any
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html#clone\(\):Object "Permalink") def clone(): AnyRef 

Attributes
    protected[lang]  

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html#equals\(that:Any\):Boolean "Permalink") def equals(that: Any): Boolean 

Definition Classes
     [BlockManagerId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html "org.apache.spark.storage.BlockManagerId") → AnyRef → Any
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html#executorId:String "Permalink") def executorId: String
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef] 

Definition Classes
    AnyRef → Any 

Annotations
     @IntrinsicCandidate() @native()
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html#hashCode\(\):Int "Permalink") def hashCode(): Int 

Definition Classes
     [BlockManagerId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html "org.apache.spark.storage.BlockManagerId") → AnyRef → Any
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html#host:String "Permalink") def host: String
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html#hostPort:String "Permalink") def hostPort: String
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html#isDriver:Boolean "Permalink") def isDriver: Boolean
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean 

Definition Classes
    Any
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html#notify\(\):Unit "Permalink") final  def notify(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html#port:Int "Permalink") def port: Int
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html#readExternal\(in:java.io.ObjectInput\):Unit "Permalink") def readExternal(in: [ObjectInput](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/ObjectInput.html#java.io.ObjectInput "java.io.ObjectInput")): Unit 

Definition Classes
     [BlockManagerId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html "org.apache.spark.storage.BlockManagerId") → Externalizable
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0 

Definition Classes
    AnyRef
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html#toString\(\):String "Permalink") def toString(): String 

Definition Classes
     [BlockManagerId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html "org.apache.spark.storage.BlockManagerId") → AnyRef → Any
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html#topologyInfo:Option\[String\] "Permalink") def topologyInfo: Option[String]
  23. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  24. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  25. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html#wait\(\):Unit "Permalink") final  def wait(): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  26. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html#writeExternal\(out:java.io.ObjectOutput\):Unit "Permalink") def writeExternal(out: [ObjectOutput](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/ObjectOutput.html#java.io.ObjectOutput "java.io.ObjectOutput")): Unit 

Definition Classes
     [BlockManagerId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html "org.apache.spark.storage.BlockManagerId") → Externalizable


### Deprecated Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html#finalize\(\):Unit "Permalink") def finalize(): Unit 

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
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html###:Int "Permalink") final  def ##: Int 

Definition Classes
    AnyRef → Any
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html#clone\(\):Object "Permalink") def clone(): AnyRef 

Attributes
    protected[lang]  

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef] 

Definition Classes
    AnyRef → Any 

Annotations
     @IntrinsicCandidate() @native()
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html#notify\(\):Unit "Permalink") final  def notify(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0 

Definition Classes
    AnyRef
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html#wait\(\):Unit "Permalink") final  def wait(): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html#finalize\(\):Unit "Permalink") def finalize(): Unit 

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
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0 

Definition Classes
    Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean 

Definition Classes
    Any


### Ungrouped
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html###:Int "Permalink") final  def ##: Int 

Definition Classes
    AnyRef → Any
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0 

Definition Classes
    Any
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html#clone\(\):Object "Permalink") def clone(): AnyRef 

Attributes
    protected[lang]  

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html#equals\(that:Any\):Boolean "Permalink") def equals(that: Any): Boolean 

Definition Classes
     [BlockManagerId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html "org.apache.spark.storage.BlockManagerId") → AnyRef → Any
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html#executorId:String "Permalink") def executorId: String
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef] 

Definition Classes
    AnyRef → Any 

Annotations
     @IntrinsicCandidate() @native()
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html#hashCode\(\):Int "Permalink") def hashCode(): Int 

Definition Classes
     [BlockManagerId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html "org.apache.spark.storage.BlockManagerId") → AnyRef → Any
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html#host:String "Permalink") def host: String
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html#hostPort:String "Permalink") def hostPort: String
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html#isDriver:Boolean "Permalink") def isDriver: Boolean
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean 

Definition Classes
    Any
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html#notify\(\):Unit "Permalink") final  def notify(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html#port:Int "Permalink") def port: Int
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html#readExternal\(in:java.io.ObjectInput\):Unit "Permalink") def readExternal(in: [ObjectInput](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/ObjectInput.html#java.io.ObjectInput "java.io.ObjectInput")): Unit 

Definition Classes
     [BlockManagerId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html "org.apache.spark.storage.BlockManagerId") → Externalizable
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0 

Definition Classes
    AnyRef
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html#toString\(\):String "Permalink") def toString(): String 

Definition Classes
     [BlockManagerId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html "org.apache.spark.storage.BlockManagerId") → AnyRef → Any
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html#topologyInfo:Option\[String\] "Permalink") def topologyInfo: Option[String]
  23. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  24. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  25. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html#wait\(\):Unit "Permalink") final  def wait(): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  26. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html#writeExternal\(out:java.io.ObjectOutput\):Unit "Permalink") def writeExternal(out: [ObjectOutput](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/ObjectOutput.html#java.io.ObjectOutput "java.io.ObjectOutput")): Unit 

Definition Classes
     [BlockManagerId](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html "org.apache.spark.storage.BlockManagerId") → Externalizable
  27. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/BlockManagerId.html#finalize\(\):Unit "Permalink") def finalize(): Unit 

Attributes
    protected[lang]  

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.Throwable]) @Deprecated 

Deprecated
    
_(Since version 9)_


