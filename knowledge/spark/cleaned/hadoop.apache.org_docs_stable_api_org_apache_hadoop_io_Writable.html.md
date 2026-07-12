[Skip navigation links](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Writable.html#skip.navbar.top "Skip navigation links")
  * [Overview](https://hadoop.apache.org/docs/stable/api/overview-summary.html)
  * [Package](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/package-summary.html)
  * Class
  * [Use](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/class-use/Writable.html)
  * [Tree](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/package-tree.html)
  * [Deprecated](https://hadoop.apache.org/docs/stable/api/deprecated-list.html)
  * [Index](https://hadoop.apache.org/docs/stable/api/index-all.html)
  * [Help](https://hadoop.apache.org/docs/stable/api/help-doc.html)

  * [Prev Class](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/VLongWritable.html "class in org.apache.hadoop.io")
  * [Next Class](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/WritableComparable.html "interface in org.apache.hadoop.io")

  * [Frames](https://hadoop.apache.org/docs/stable/api/index.html?org/apache/hadoop/io/Writable.html)
  * [No Frames](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Writable.html)

  * [All Classes](https://hadoop.apache.org/docs/stable/api/allclasses-noframe.html)

  * Summary:
  * Nested |
  * Field |
  * Constr |
  * [Method](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Writable.html#method.summary)

  * Detail:
  * Field |
  * Constr |
  * [Method](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Writable.html#method.detail)

org.apache.hadoop.io
## Interface Writable
  *

All Known Subinterfaces:
     [Counter](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapreduce/Counter.html "interface in org.apache.hadoop.mapreduce"), [CounterGroup](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapreduce/CounterGroup.html "interface in org.apache.hadoop.mapreduce"), [CounterGroupBase](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapreduce/counters/CounterGroupBase.html "interface in org.apache.hadoop.mapreduce.counters")<T>, [InputSplit](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/InputSplit.html "interface in org.apache.hadoop.mapred"), [InputSplitWithLocationInfo](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/InputSplitWithLocationInfo.html "interface in org.apache.hadoop.mapred"), [WritableComparable](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/WritableComparable.html "interface in org.apache.hadoop.io")<T>

All Known Implementing Classes:
     [AbstractCounters](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapreduce/counters/AbstractCounters.html "class in org.apache.hadoop.mapreduce.counters"), [AbstractDelegationTokenIdentifier](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/security/token/delegation/AbstractDelegationTokenIdentifier.html "class in org.apache.hadoop.security.token.delegation"), [AbstractMapWritable](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/AbstractMapWritable.html "class in org.apache.hadoop.io"), [AccessControlList](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/security/authorize/AccessControlList.html "class in org.apache.hadoop.security.authorize"), [AggregatedLogFormat.LogKey](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/yarn/logaggregation/AggregatedLogFormat.LogKey.html "class in org.apache.hadoop.yarn.logaggregation"), [AMRMTokenIdentifier](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/yarn/security/AMRMTokenIdentifier.html "class in org.apache.hadoop.yarn.security"), [ArrayPrimitiveWritable](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/ArrayPrimitiveWritable.html "class in org.apache.hadoop.io"), [ArrayWritable](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/ArrayWritable.html "class in org.apache.hadoop.io"), [BloomFilter](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/util/bloom/BloomFilter.html "class in org.apache.hadoop.util.bloom"), [BooleanWritable](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/BooleanWritable.html "class in org.apache.hadoop.io"), [BytesWritable](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/BytesWritable.html "class in org.apache.hadoop.io"), [ByteWritable](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/ByteWritable.html "class in org.apache.hadoop.io"), [ClientToAMTokenIdentifier](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/yarn/security/client/ClientToAMTokenIdentifier.html "class in org.apache.hadoop.yarn.security.client"), [ClusterMetrics](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapreduce/ClusterMetrics.html "class in org.apache.hadoop.mapreduce"), [ClusterStatus](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/ClusterStatus.html "class in org.apache.hadoop.mapred"), [CombineFileSplit](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapreduce/lib/input/CombineFileSplit.html "class in org.apache.hadoop.mapreduce.lib.input"), [CombineFileSplit](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/lib/CombineFileSplit.html "class in org.apache.hadoop.mapred.lib"), [CompositeInputSplit](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapreduce/lib/join/CompositeInputSplit.html "class in org.apache.hadoop.mapreduce.lib.join"), [CompositeInputSplit](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/join/CompositeInputSplit.html "class in org.apache.hadoop.mapred.join"), [CompressedWritable](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/CompressedWritable.html "class in org.apache.hadoop.io"), [Configuration](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/conf/Configuration.html "class in org.apache.hadoop.conf"), [ContainerTokenIdentifier](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/yarn/security/ContainerTokenIdentifier.html "class in org.apache.hadoop.yarn.security"), [ContentSummary](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/fs/ContentSummary.html "class in org.apache.hadoop.fs"), [Counters](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapreduce/Counters.html "class in org.apache.hadoop.mapreduce"), [Counters](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/Counters.html "class in org.apache.hadoop.mapred"), [Counters.Counter](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/Counters.Counter.html "class in org.apache.hadoop.mapred"), [Counters.Group](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/Counters.Group.html "class in org.apache.hadoop.mapred"), [CountingBloomFilter](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/util/bloom/CountingBloomFilter.html "class in org.apache.hadoop.util.bloom"), [Credentials](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/security/Credentials.html "class in org.apache.hadoop.security"), [DoubleWritable](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/DoubleWritable.html "class in org.apache.hadoop.io"), [DynamicBloomFilter](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/util/bloom/DynamicBloomFilter.html "class in org.apache.hadoop.util.bloom"), [EnumSetWritable](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/EnumSetWritable.html "class in org.apache.hadoop.io"), [FileChecksum](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/fs/FileChecksum.html "class in org.apache.hadoop.fs"), [FileSplit](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapreduce/lib/input/FileSplit.html "class in org.apache.hadoop.mapreduce.lib.input"), [FileSplit](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/FileSplit.html "class in org.apache.hadoop.mapred"), [FileStatus](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/fs/FileStatus.html "class in org.apache.hadoop.fs"), org.apache.hadoop.util.bloom.Filter, [FloatWritable](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/FloatWritable.html "class in org.apache.hadoop.io"), [FsCreateModes](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/fs/permission/FsCreateModes.html "class in org.apache.hadoop.fs.permission"), [FsPermission](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/fs/permission/FsPermission.html "class in org.apache.hadoop.fs.permission"), [FsServerDefaults](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/fs/FsServerDefaults.html "class in org.apache.hadoop.fs"), [FsStatus](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/fs/FsStatus.html "class in org.apache.hadoop.fs"), [GenericWritable](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/GenericWritable.html "class in org.apache.hadoop.io"), [ID](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapreduce/ID.html "class in org.apache.hadoop.mapreduce"), [ID](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/ID.html "class in org.apache.hadoop.mapred"), [IntWritable](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/IntWritable.html "class in org.apache.hadoop.io"), [JobConf](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/JobConf.html "class in org.apache.hadoop.mapred"), [JobID](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapreduce/JobID.html "class in org.apache.hadoop.mapreduce"), [JobID](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/JobID.html "class in org.apache.hadoop.mapred"), [JobQueueInfo](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/JobQueueInfo.html "class in org.apache.hadoop.mapred"), [JobStatus](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapreduce/JobStatus.html "class in org.apache.hadoop.mapreduce"), [JobStatus](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/JobStatus.html "class in org.apache.hadoop.mapred"), [LocatedFileStatus](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/fs/LocatedFileStatus.html "class in org.apache.hadoop.fs"), [LongWritable](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/LongWritable.html "class in org.apache.hadoop.io"), [MapWritable](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/MapWritable.html "class in org.apache.hadoop.io"), [MD5Hash](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/MD5Hash.html "class in org.apache.hadoop.io"), [MultiFileSplit](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/MultiFileSplit.html "class in org.apache.hadoop.mapred"), [NMTokenIdentifier](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/yarn/security/NMTokenIdentifier.html "class in org.apache.hadoop.yarn.security"), [NullWritable](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/NullWritable.html "class in org.apache.hadoop.io"), [ObjectWritable](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/ObjectWritable.html "class in org.apache.hadoop.io"), [QueueAclsInfo](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapreduce/QueueAclsInfo.html "class in org.apache.hadoop.mapreduce"), [QueueInfo](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapreduce/QueueInfo.html "class in org.apache.hadoop.mapreduce"), [Record](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/record/Record.html "class in org.apache.hadoop.record"), [RetouchedBloomFilter](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/util/bloom/RetouchedBloomFilter.html "class in org.apache.hadoop.util.bloom"), [RMDelegationTokenIdentifier](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/yarn/security/client/RMDelegationTokenIdentifier.html "class in org.apache.hadoop.yarn.security.client"), [ShortWritable](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/ShortWritable.html "class in org.apache.hadoop.io"), [SortedMapWritable](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/SortedMapWritable.html "class in org.apache.hadoop.io"), [TaskAttemptID](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapreduce/TaskAttemptID.html "class in org.apache.hadoop.mapreduce"), [TaskAttemptID](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/TaskAttemptID.html "class in org.apache.hadoop.mapred"), [TaskCompletionEvent](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapreduce/TaskCompletionEvent.html "class in org.apache.hadoop.mapreduce"), [TaskCompletionEvent](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/TaskCompletionEvent.html "class in org.apache.hadoop.mapred"), [TaskID](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapreduce/TaskID.html "class in org.apache.hadoop.mapreduce"), [TaskID](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/TaskID.html "class in org.apache.hadoop.mapred"), org.apache.hadoop.mapreduce.TaskReport, [TaskReport](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/TaskReport.html "class in org.apache.hadoop.mapred"), [TaskTrackerInfo](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapreduce/TaskTrackerInfo.html "class in org.apache.hadoop.mapreduce"), [Text](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Text.html "class in org.apache.hadoop.io"), [TimelineDelegationTokenIdentifier](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/yarn/security/client/TimelineDelegationTokenIdentifier.html "class in org.apache.hadoop.yarn.security.client"), [Token](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/security/token/Token.html "class in org.apache.hadoop.security.token"), [TokenIdentifier](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/security/token/TokenIdentifier.html "class in org.apache.hadoop.security.token"), [TupleWritable](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapreduce/lib/join/TupleWritable.html "class in org.apache.hadoop.mapreduce.lib.join"), [TupleWritable](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/join/TupleWritable.html "class in org.apache.hadoop.mapred.join"), [TwoDArrayWritable](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/TwoDArrayWritable.html "class in org.apache.hadoop.io"), [VersionedWritable](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/VersionedWritable.html "class in org.apache.hadoop.io"), [VIntWritable](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/VIntWritable.html "class in org.apache.hadoop.io"), [VLongWritable](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/VLongWritable.html "class in org.apache.hadoop.io"), [YarnConfiguration](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/yarn/conf/YarnConfiguration.html "class in org.apache.hadoop.yarn.conf"), org.apache.hadoop.yarn.security.client.YARNDelegationTokenIdentifier
* * *

```
@InterfaceAudience.Public
 @InterfaceStability.Stable
public interface Writable
```

A serializable object which implements a simple, efficient, serialization protocol, based on [`DataInput`](https://docs.oracle.com/javase/8/docs/api/java/io/DataInput.html?is-external=true "class or interface in java.io") and [`DataOutput`](https://docs.oracle.com/javase/8/docs/api/java/io/DataOutput.html?is-external=true "class or interface in java.io").
Any `key` or `value` type in the Hadoop Map-Reduce framework implements this interface.
Implementations typically implement a static `read(DataInput)` method which constructs a new instance, calls [`readFields(DataInput)`](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Writable.html#readFields-java.io.DataInput-) and returns the instance.
Example:
>
```
     public class MyWritable implements Writable {
       // Some data
       private int counter;
       private long timestamp;

       // Default constructor to allow (de)serialization
       MyWritable() { }

       public void write(DataOutput out) throws IOException {
         out.writeInt(counter);
         out.writeLong(timestamp);
       }

       public void readFields(DataInput in) throws IOException {
         counter = in.readInt();
         timestamp = in.readLong();
       }

       public static MyWritable read(DataInput in) throws IOException {
         MyWritable w = new MyWritable();
         w.readFields(in);
         return w;
       }
     }

```

  *     * ### Method Summary
All Methods[Instance Methods](javascript:show\(2\);)[Abstract Methods](javascript:show\(4\);)
| Modifier and Type  | Method and Description  |
| --- | --- |
| `void`  |  `readFields[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Writable.html#readFields-java.io.DataInput-)(DataInput[](https://docs.oracle.com/javase/8/docs/api/java/io/DataInput.html?is-external=true "class or interface in java.io") in)` Deserialize the fields of this object from `in`.  |
| `void`  |  `write[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Writable.html#write-java.io.DataOutput-)(DataOutput[](https://docs.oracle.com/javase/8/docs/api/java/io/DataOutput.html?is-external=true "class or interface in java.io") out)` Serialize the fields of this object to `out`.  |

  *     * ### Method Detail
      * #### write

```
void write(DataOutput[](https://docs.oracle.com/javase/8/docs/api/java/io/DataOutput.html?is-external=true "class or interface in java.io") out)
    throws IOException[](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html?is-external=true "class or interface in java.io")
```

Serialize the fields of this object to `out`.

Parameters:
     `out` - `DataOuput` to serialize this object into.

Throws:
     `IOException[](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html?is-external=true "class or interface in java.io")` - any other problem for write.
      * #### readFields

```
void readFields(DataInput[](https://docs.oracle.com/javase/8/docs/api/java/io/DataInput.html?is-external=true "class or interface in java.io") in)
         throws IOException[](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html?is-external=true "class or interface in java.io")
```

Deserialize the fields of this object from `in`.
For efficiency, implementations should attempt to re-use storage in the existing object where possible.

Parameters:
     `in` - `DataInput` to deseriablize this object from.

Throws:
     `IOException[](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html?is-external=true "class or interface in java.io")` - any other problem for readFields.

[Skip navigation links](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Writable.html#skip.navbar.bottom "Skip navigation links")
  * [Overview](https://hadoop.apache.org/docs/stable/api/overview-summary.html)
  * [Package](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/package-summary.html)
  * Class
  * [Use](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/class-use/Writable.html)
  * [Tree](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/package-tree.html)
  * [Deprecated](https://hadoop.apache.org/docs/stable/api/deprecated-list.html)
  * [Index](https://hadoop.apache.org/docs/stable/api/index-all.html)
  * [Help](https://hadoop.apache.org/docs/stable/api/help-doc.html)

  * [Prev Class](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/VLongWritable.html "class in org.apache.hadoop.io")
  * [Next Class](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/WritableComparable.html "interface in org.apache.hadoop.io")

  * [Frames](https://hadoop.apache.org/docs/stable/api/index.html?org/apache/hadoop/io/Writable.html)
  * [No Frames](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Writable.html)

  * [All Classes](https://hadoop.apache.org/docs/stable/api/allclasses-noframe.html)

  * Summary:
  * Nested |
  * Field |
  * Constr |
  * [Method](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Writable.html#method.summary)

  * Detail:
  * Field |
  * Constr |
  * [Method](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Writable.html#method.detail)

Copyright © 2023 [Apache Software Foundation](https://www.apache.org). All rights reserved.
