[Skip navigation links](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/InputFormat.html#skip.navbar.top "Skip navigation links")
  * [Overview](https://hadoop.apache.org/docs/stable/api/overview-summary.html)
  * [Package](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/package-summary.html)
  * Class
  * [Use](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/class-use/InputFormat.html)
  * [Tree](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/package-tree.html)
  * [Deprecated](https://hadoop.apache.org/docs/stable/api/deprecated-list.html)
  * [Index](https://hadoop.apache.org/docs/stable/api/index-all.html)
  * [Help](https://hadoop.apache.org/docs/stable/api/help-doc.html)


  * [Prev Class](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/ID.html "class in org.apache.hadoop.mapred")
  * [Next Class](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/InputSplit.html "interface in org.apache.hadoop.mapred")


  * [Frames](https://hadoop.apache.org/docs/stable/api/index.html?org/apache/hadoop/mapred/InputFormat.html)
  * [No Frames](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/InputFormat.html)


  * [All Classes](https://hadoop.apache.org/docs/stable/api/allclasses-noframe.html)


  * Summary: 
  * Nested | 
  * Field | 
  * Constr | 
  * [Method](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/InputFormat.html#method.summary)


  * Detail: 
  * Field | 
  * Constr | 
  * [Method](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/InputFormat.html#method.detail)


org.apache.hadoop.mapred
## Interface InputFormat<K,V>
  * 

All Known Subinterfaces:
     [ComposableInputFormat](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/join/ComposableInputFormat.html "interface in org.apache.hadoop.mapred.join")<K,V> 

All Known Implementing Classes:
     [CombineFileInputFormat](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/lib/CombineFileInputFormat.html "class in org.apache.hadoop.mapred.lib"), [CombineSequenceFileInputFormat](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/lib/CombineSequenceFileInputFormat.html "class in org.apache.hadoop.mapred.lib"), [CombineTextInputFormat](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/lib/CombineTextInputFormat.html "class in org.apache.hadoop.mapred.lib"), [CompositeInputFormat](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/join/CompositeInputFormat.html "class in org.apache.hadoop.mapred.join"), [DBInputFormat](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/lib/db/DBInputFormat.html "class in org.apache.hadoop.mapred.lib.db"), [FileInputFormat](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/FileInputFormat.html "class in org.apache.hadoop.mapred"), [FixedLengthInputFormat](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/FixedLengthInputFormat.html "class in org.apache.hadoop.mapred"), [KeyValueTextInputFormat](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/KeyValueTextInputFormat.html "class in org.apache.hadoop.mapred"), [MultiFileInputFormat](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/MultiFileInputFormat.html "class in org.apache.hadoop.mapred"), [NLineInputFormat](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/lib/NLineInputFormat.html "class in org.apache.hadoop.mapred.lib"), [Parser.Node](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/join/Parser.Node.html "class in org.apache.hadoop.mapred.join"), [SequenceFileAsBinaryInputFormat](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/SequenceFileAsBinaryInputFormat.html "class in org.apache.hadoop.mapred"), [SequenceFileAsTextInputFormat](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/SequenceFileAsTextInputFormat.html "class in org.apache.hadoop.mapred"), [SequenceFileInputFilter](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/SequenceFileInputFilter.html "class in org.apache.hadoop.mapred"), [SequenceFileInputFormat](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/SequenceFileInputFormat.html "class in org.apache.hadoop.mapred"), [TextInputFormat](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/TextInputFormat.html "class in org.apache.hadoop.mapred")
* * *
  

```
@InterfaceAudience.Public
 @InterfaceStability.Stable
public interface InputFormat<K,V>
```

`InputFormat` describes the input-specification for a Map-Reduce job. 
The Map-Reduce framework relies on the `InputFormat` of the job to:
    1. Validate the input-specification of the job. 
    2. Split-up the input file(s) into logical [`InputSplit`](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/InputSplit.html "interface in org.apache.hadoop.mapred")s, each of which is then assigned to an individual [`Mapper`](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/Mapper.html "interface in org.apache.hadoop.mapred"). 
    3. Provide the [`RecordReader`](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/RecordReader.html "interface in org.apache.hadoop.mapred") implementation to be used to glean input records from the logical `InputSplit` for processing by the [`Mapper`](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/Mapper.html "interface in org.apache.hadoop.mapred"). 
The default behavior of file-based [`InputFormat`](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/InputFormat.html "interface in org.apache.hadoop.mapred")s, typically sub-classes of [`FileInputFormat`](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/FileInputFormat.html "class in org.apache.hadoop.mapred"), is to split the input into _logical_ [`InputSplit`](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/InputSplit.html "interface in org.apache.hadoop.mapred")s based on the total size, in bytes, of the input files. However, the [`FileSystem`](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/fs/FileSystem.html "class in org.apache.hadoop.fs") blocksize of the input files is treated as an upper bound for input splits. A lower bound on the split size can be set via [ mapreduce.input.fileinputformat.split.minsize](https://hadoop.apache.org/docs/stable/hadoop-mapreduce-client/hadoop-mapreduce-client-core/mapred-default.xml#mapreduce.input.fileinputformat.split.minsize).
Clearly, logical splits based on input-size is insufficient for many applications since record boundaries are to be respected. In such cases, the application has to also implement a [`RecordReader`](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/RecordReader.html "interface in org.apache.hadoop.mapred") on whom lies the responsibilty to respect record-boundaries and present a record-oriented view of the logical `InputSplit` to the individual task. 

See Also:
     [`InputSplit`](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/InputSplit.html "interface in org.apache.hadoop.mapred"), [`RecordReader`](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/RecordReader.html "interface in org.apache.hadoop.mapred"), [`JobClient`](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/JobClient.html "class in org.apache.hadoop.mapred"), [`FileInputFormat`](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/FileInputFormat.html "class in org.apache.hadoop.mapred")


  *     * ### Method Summary  
All Methods[Instance Methods](javascript:show\(2\);)[Abstract Methods](javascript:show\(4\);)  
| Modifier and Type  | Method and Description  |  
| --- | --- |  
| `RecordReader[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/RecordReader.html "interface in org.apache.hadoop.mapred")<K[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/InputFormat.html "type parameter in InputFormat"),V[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/InputFormat.html "type parameter in InputFormat")>`  |  `getRecordReader[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/InputFormat.html#getRecordReader-org.apache.hadoop.mapred.InputSplit-org.apache.hadoop.mapred.JobConf-org.apache.hadoop.mapred.Reporter-)(InputSplit[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/InputSplit.html "interface in org.apache.hadoop.mapred") split,                JobConf[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/JobConf.html "class in org.apache.hadoop.mapred") job,                Reporter[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/Reporter.html "interface in org.apache.hadoop.mapred") reporter)` Get the [`RecordReader`](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/RecordReader.html "interface in org.apache.hadoop.mapred") for the given [`InputSplit`](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/InputSplit.html "interface in org.apache.hadoop.mapred").  |  
| `InputSplit[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/InputSplit.html "interface in org.apache.hadoop.mapred")[]`  |  `getSplits[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/InputFormat.html#getSplits-org.apache.hadoop.mapred.JobConf-int-)(JobConf[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/JobConf.html "class in org.apache.hadoop.mapred") job,          int numSplits)` Logically split the set of input files for the job.  |  


  *     * ### Method Detail
      * #### getSplits

```
InputSplit[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/InputSplit.html "interface in org.apache.hadoop.mapred")[] getSplits(JobConf[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/JobConf.html "class in org.apache.hadoop.mapred") job,
                       int numSplits)
                throws IOException[](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html?is-external=true "class or interface in java.io")
```

Logically split the set of input files for the job. 
Each [`InputSplit`](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/InputSplit.html "interface in org.apache.hadoop.mapred") is then assigned to an individual [`Mapper`](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/Mapper.html "interface in org.apache.hadoop.mapred") for processing.
_Note_ : The split is a _logical_ split of the inputs and the input files are not physically split into chunks. For e.g. a split could be _< input-file-path, start, offset>_ tuple. 

Parameters:
     `job` - job configuration.      `numSplits` - the desired number of splits, a hint. 

Returns:
    an array of [`InputSplit`](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/InputSplit.html "interface in org.apache.hadoop.mapred")s for the job. 

Throws:
    `IOException[](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html?is-external=true "class or interface in java.io")`
      * #### getRecordReader

```
RecordReader[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/RecordReader.html "interface in org.apache.hadoop.mapred")<K[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/InputFormat.html "type parameter in InputFormat"),V[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/InputFormat.html "type parameter in InputFormat")> getRecordReader(InputSplit[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/InputSplit.html "interface in org.apache.hadoop.mapred") split,
                                  JobConf[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/JobConf.html "class in org.apache.hadoop.mapred") job,
                                  Reporter[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/Reporter.html "interface in org.apache.hadoop.mapred") reporter)
                           throws IOException[](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html?is-external=true "class or interface in java.io")
```

Get the [`RecordReader`](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/RecordReader.html "interface in org.apache.hadoop.mapred") for the given [`InputSplit`](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/InputSplit.html "interface in org.apache.hadoop.mapred"). 
It is the responsibility of the `RecordReader` to respect record boundaries while processing the logical split to present a record-oriented view to the individual task. 

Parameters:
     `split` - the [`InputSplit`](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/InputSplit.html "interface in org.apache.hadoop.mapred")      `job` - the job that this split belongs to 

Returns:
    a [`RecordReader`](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/RecordReader.html "interface in org.apache.hadoop.mapred") 

Throws:
    `IOException[](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html?is-external=true "class or interface in java.io")`


[Skip navigation links](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/InputFormat.html#skip.navbar.bottom "Skip navigation links")
  * [Overview](https://hadoop.apache.org/docs/stable/api/overview-summary.html)
  * [Package](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/package-summary.html)
  * Class
  * [Use](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/class-use/InputFormat.html)
  * [Tree](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/package-tree.html)
  * [Deprecated](https://hadoop.apache.org/docs/stable/api/deprecated-list.html)
  * [Index](https://hadoop.apache.org/docs/stable/api/index-all.html)
  * [Help](https://hadoop.apache.org/docs/stable/api/help-doc.html)


  * [Prev Class](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/ID.html "class in org.apache.hadoop.mapred")
  * [Next Class](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/InputSplit.html "interface in org.apache.hadoop.mapred")


  * [Frames](https://hadoop.apache.org/docs/stable/api/index.html?org/apache/hadoop/mapred/InputFormat.html)
  * [No Frames](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/InputFormat.html)


  * [All Classes](https://hadoop.apache.org/docs/stable/api/allclasses-noframe.html)


  * Summary: 
  * Nested | 
  * Field | 
  * Constr | 
  * [Method](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/InputFormat.html#method.summary)


  * Detail: 
  * Field | 
  * Constr | 
  * [Method](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/InputFormat.html#method.detail)


Copyright © 2023 [Apache Software Foundation](https://www.apache.org). All rights reserved.
