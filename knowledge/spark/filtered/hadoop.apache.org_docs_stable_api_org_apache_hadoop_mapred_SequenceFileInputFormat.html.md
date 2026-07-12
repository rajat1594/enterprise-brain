[Skip navigation links](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/SequenceFileInputFormat.html#skip.navbar.top "Skip navigation links")
  * [Overview](https://hadoop.apache.org/docs/stable/api/overview-summary.html)
  * [Package](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/package-summary.html)
  * Class
  * [Use](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/class-use/SequenceFileInputFormat.html)
  * [Tree](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/package-tree.html)
  * [Deprecated](https://hadoop.apache.org/docs/stable/api/deprecated-list.html)
  * [Index](https://hadoop.apache.org/docs/stable/api/index-all.html)
  * [Help](https://hadoop.apache.org/docs/stable/api/help-doc.html)


  * [Prev Class](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/SequenceFileInputFilter.html "class in org.apache.hadoop.mapred")
  * [Next Class](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/SequenceFileOutputFormat.html "class in org.apache.hadoop.mapred")


  * [Frames](https://hadoop.apache.org/docs/stable/api/index.html?org/apache/hadoop/mapred/SequenceFileInputFormat.html)
  * [No Frames](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/SequenceFileInputFormat.html)


  * [All Classes](https://hadoop.apache.org/docs/stable/api/allclasses-noframe.html)


  * Summary: 
  * Nested | 
  * [Field](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/SequenceFileInputFormat.html#fields.inherited.from.class.org.apache.hadoop.mapred.FileInputFormat) | 
  * [Constr](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/SequenceFileInputFormat.html#constructor.summary) | 
  * [Method](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/SequenceFileInputFormat.html#method.summary)


  * Detail: 
  * Field | 
  * [Constr](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/SequenceFileInputFormat.html#constructor.detail) | 
  * [Method](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/SequenceFileInputFormat.html#method.detail)


org.apache.hadoop.mapred
## Class SequenceFileInputFormat<K,V>
  * [java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true "class or interface in java.lang")
  *     * [org.apache.hadoop.mapred.FileInputFormat](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/FileInputFormat.html "class in org.apache.hadoop.mapred")<K,V>
    *       * org.apache.hadoop.mapred.SequenceFileInputFormat<K,V>


  * 

All Implemented Interfaces:
     [InputFormat](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/InputFormat.html "interface in org.apache.hadoop.mapred")<K,V> 

Direct Known Subclasses:
     [SequenceFileAsBinaryInputFormat](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/SequenceFileAsBinaryInputFormat.html "class in org.apache.hadoop.mapred"), [SequenceFileAsTextInputFormat](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/SequenceFileAsTextInputFormat.html "class in org.apache.hadoop.mapred"), [SequenceFileInputFilter](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/SequenceFileInputFilter.html "class in org.apache.hadoop.mapred")
* * *
  

```
@InterfaceAudience.Public
 @InterfaceStability.Stable
public class SequenceFileInputFormat<K,V>
extends FileInputFormat[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/FileInputFormat.html "class in org.apache.hadoop.mapred")<K,V>
```

An [`InputFormat`](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/InputFormat.html "interface in org.apache.hadoop.mapred") for [`SequenceFile`](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/SequenceFile.html "class in org.apache.hadoop.io")s.


  *     * ### Field Summary
      * ### Fields inherited from class org.apache.hadoop.mapred.[FileInputFormat](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/FileInputFormat.html "class in org.apache.hadoop.mapred")
`INPUT_DIR_NONRECURSIVE_IGNORE_SUBDIRS[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/FileInputFormat.html#INPUT_DIR_NONRECURSIVE_IGNORE_SUBDIRS), INPUT_DIR_RECURSIVE[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/FileInputFormat.html#INPUT_DIR_RECURSIVE), LOG[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/FileInputFormat.html#LOG), NUM_INPUT_FILES[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/FileInputFormat.html#NUM_INPUT_FILES)`
    * ### Constructor Summary  
Constructors  
| Constructor and Description  |  
| --- |  
|  `SequenceFileInputFormat[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/SequenceFileInputFormat.html#SequenceFileInputFormat--)()`  |  
    * ### Method Summary  
All Methods[Instance Methods](javascript:show\(2\);)[Concrete Methods](javascript:show\(8\);)  
| Modifier and Type  | Method and Description  |  
| --- | --- |  
| `RecordReader[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/RecordReader.html "interface in org.apache.hadoop.mapred")<K[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/SequenceFileInputFormat.html "type parameter in SequenceFileInputFormat"),V[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/SequenceFileInputFormat.html "type parameter in SequenceFileInputFormat")>`  |  `getRecordReader[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/SequenceFileInputFormat.html#getRecordReader-org.apache.hadoop.mapred.InputSplit-org.apache.hadoop.mapred.JobConf-org.apache.hadoop.mapred.Reporter-)(InputSplit[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/InputSplit.html "interface in org.apache.hadoop.mapred") split,                JobConf[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/JobConf.html "class in org.apache.hadoop.mapred") job,                Reporter[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/Reporter.html "interface in org.apache.hadoop.mapred") reporter)` Get the [`RecordReader`](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/RecordReader.html "interface in org.apache.hadoop.mapred") for the given [`InputSplit`](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/InputSplit.html "interface in org.apache.hadoop.mapred").  |  
| `protected FileStatus[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/fs/FileStatus.html "class in org.apache.hadoop.fs")[]`  |  `listStatus[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/SequenceFileInputFormat.html#listStatus-org.apache.hadoop.mapred.JobConf-)(JobConf[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/JobConf.html "class in org.apache.hadoop.mapred") job)` List input directories.  |  
      * ### Methods inherited from class org.apache.hadoop.mapred.[FileInputFormat](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/FileInputFormat.html "class in org.apache.hadoop.mapred")
`addInputPath[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/FileInputFormat.html#addInputPath-org.apache.hadoop.mapred.JobConf-org.apache.hadoop.fs.Path-), addInputPathRecursively[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/FileInputFormat.html#addInputPathRecursively-java.util.List-org.apache.hadoop.fs.FileSystem-org.apache.hadoop.fs.Path-org.apache.hadoop.fs.PathFilter-), addInputPaths[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/FileInputFormat.html#addInputPaths-org.apache.hadoop.mapred.JobConf-java.lang.String-), computeSplitSize[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/FileInputFormat.html#computeSplitSize-long-long-long-), getBlockIndex[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/FileInputFormat.html#getBlockIndex-org.apache.hadoop.fs.BlockLocation:A-long-), getInputPathFilter[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/FileInputFormat.html#getInputPathFilter-org.apache.hadoop.mapred.JobConf-), getInputPaths[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/FileInputFormat.html#getInputPaths-org.apache.hadoop.mapred.JobConf-), getSplitHosts[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/FileInputFormat.html#getSplitHosts-org.apache.hadoop.fs.BlockLocation:A-long-long-org.apache.hadoop.net.NetworkTopology-), getSplits[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/FileInputFormat.html#getSplits-org.apache.hadoop.mapred.JobConf-int-), isSplitable[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/FileInputFormat.html#isSplitable-org.apache.hadoop.fs.FileSystem-org.apache.hadoop.fs.Path-), makeSplit[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/FileInputFormat.html#makeSplit-org.apache.hadoop.fs.Path-long-long-java.lang.String:A-), makeSplit[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/FileInputFormat.html#makeSplit-org.apache.hadoop.fs.Path-long-long-java.lang.String:A-java.lang.String:A-), setInputPathFilter[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/FileInputFormat.html#setInputPathFilter-org.apache.hadoop.mapred.JobConf-java.lang.Class-), setInputPaths[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/FileInputFormat.html#setInputPaths-org.apache.hadoop.mapred.JobConf-org.apache.hadoop.fs.Path...-), setInputPaths[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/FileInputFormat.html#setInputPaths-org.apache.hadoop.mapred.JobConf-java.lang.String-), setMinSplitSize[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/FileInputFormat.html#setMinSplitSize-long-)`
      * ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true "class or interface in java.lang")
`clone[](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true#clone-- "class or interface in java.lang"), equals[](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true#equals-java.lang.Object- "class or interface in java.lang"), finalize[](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true#finalize-- "class or interface in java.lang"), getClass[](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true#getClass-- "class or interface in java.lang"), hashCode[](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true#hashCode-- "class or interface in java.lang"), notify[](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true#notify-- "class or interface in java.lang"), notifyAll[](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true#notifyAll-- "class or interface in java.lang"), toString[](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true#toString-- "class or interface in java.lang"), wait[](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true#wait-- "class or interface in java.lang"), wait[](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true#wait-long- "class or interface in java.lang"), wait[](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true#wait-long-int- "class or interface in java.lang")`


  *     * ### Constructor Detail
      * #### SequenceFileInputFormat

```
public SequenceFileInputFormat()
```

    * ### Method Detail
      * #### listStatus

```
protected FileStatus[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/fs/FileStatus.html "class in org.apache.hadoop.fs")[] listStatus(JobConf[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/JobConf.html "class in org.apache.hadoop.mapred") job)
                           throws IOException[](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html?is-external=true "class or interface in java.io")
```

Description copied from class: `FileInputFormat[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/FileInputFormat.html#listStatus-org.apache.hadoop.mapred.JobConf-)`
List input directories. Subclasses may override to, e.g., select only files matching a regular expression. If security is enabled, this method collects delegation tokens from the input paths and adds them to the job's credentials. 

Overrides:
     `listStatus[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/FileInputFormat.html#listStatus-org.apache.hadoop.mapred.JobConf-)` in class `FileInputFormat[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/FileInputFormat.html "class in org.apache.hadoop.mapred")<K[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/SequenceFileInputFormat.html "type parameter in SequenceFileInputFormat"),V[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/SequenceFileInputFormat.html "type parameter in SequenceFileInputFormat")>` 

Parameters:
     `job` - the job to list input paths for and attach tokens to. 

Returns:
    array of FileStatus objects 

Throws:
     `IOException[](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html?is-external=true "class or interface in java.io")` - if zero items.
      * #### getRecordReader

```
public RecordReader[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/RecordReader.html "interface in org.apache.hadoop.mapred")<K[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/SequenceFileInputFormat.html "type parameter in SequenceFileInputFormat"),V[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/SequenceFileInputFormat.html "type parameter in SequenceFileInputFormat")> getRecordReader(InputSplit[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/InputSplit.html "interface in org.apache.hadoop.mapred") split,
                                         JobConf[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/JobConf.html "class in org.apache.hadoop.mapred") job,
                                         Reporter[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/Reporter.html "interface in org.apache.hadoop.mapred") reporter)
                                  throws IOException[](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html?is-external=true "class or interface in java.io")
```

Description copied from interface: `InputFormat[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/InputFormat.html#getRecordReader-org.apache.hadoop.mapred.InputSplit-org.apache.hadoop.mapred.JobConf-org.apache.hadoop.mapred.Reporter-)`
Get the [`RecordReader`](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/RecordReader.html "interface in org.apache.hadoop.mapred") for the given [`InputSplit`](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/InputSplit.html "interface in org.apache.hadoop.mapred"). 
It is the responsibility of the `RecordReader` to respect record boundaries while processing the logical split to present a record-oriented view to the individual task. 

Specified by:
     `getRecordReader[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/InputFormat.html#getRecordReader-org.apache.hadoop.mapred.InputSplit-org.apache.hadoop.mapred.JobConf-org.apache.hadoop.mapred.Reporter-)` in interface `InputFormat[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/InputFormat.html "interface in org.apache.hadoop.mapred")<K[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/SequenceFileInputFormat.html "type parameter in SequenceFileInputFormat"),V[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/SequenceFileInputFormat.html "type parameter in SequenceFileInputFormat")>` 

Specified by:
     `getRecordReader[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/FileInputFormat.html#getRecordReader-org.apache.hadoop.mapred.InputSplit-org.apache.hadoop.mapred.JobConf-org.apache.hadoop.mapred.Reporter-)` in class `FileInputFormat[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/FileInputFormat.html "class in org.apache.hadoop.mapred")<K[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/SequenceFileInputFormat.html "type parameter in SequenceFileInputFormat"),V[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/SequenceFileInputFormat.html "type parameter in SequenceFileInputFormat")>` 

Parameters:
     `split` - the [`InputSplit`](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/InputSplit.html "interface in org.apache.hadoop.mapred")      `job` - the job that this split belongs to 

Returns:
    a [`RecordReader`](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/RecordReader.html "interface in org.apache.hadoop.mapred") 

Throws:
    `IOException[](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html?is-external=true "class or interface in java.io")`


[Skip navigation links](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/SequenceFileInputFormat.html#skip.navbar.bottom "Skip navigation links")
  * [Overview](https://hadoop.apache.org/docs/stable/api/overview-summary.html)
  * [Package](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/package-summary.html)
  * Class
  * [Use](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/class-use/SequenceFileInputFormat.html)
  * [Tree](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/package-tree.html)
  * [Deprecated](https://hadoop.apache.org/docs/stable/api/deprecated-list.html)
  * [Index](https://hadoop.apache.org/docs/stable/api/index-all.html)
  * [Help](https://hadoop.apache.org/docs/stable/api/help-doc.html)


  * [Prev Class](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/SequenceFileInputFilter.html "class in org.apache.hadoop.mapred")
  * [Next Class](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/SequenceFileOutputFormat.html "class in org.apache.hadoop.mapred")


  * [Frames](https://hadoop.apache.org/docs/stable/api/index.html?org/apache/hadoop/mapred/SequenceFileInputFormat.html)
  * [No Frames](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/SequenceFileInputFormat.html)


  * [All Classes](https://hadoop.apache.org/docs/stable/api/allclasses-noframe.html)


  * Summary: 
  * Nested | 
  * [Field](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/SequenceFileInputFormat.html#fields.inherited.from.class.org.apache.hadoop.mapred.FileInputFormat) | 
  * [Constr](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/SequenceFileInputFormat.html#constructor.summary) | 
  * [Method](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/SequenceFileInputFormat.html#method.summary)


  * Detail: 
  * Field | 
  * [Constr](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/SequenceFileInputFormat.html#constructor.detail) | 
  * [Method](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/mapred/SequenceFileInputFormat.html#method.detail)


Copyright © 2023 [Apache Software Foundation](https://www.apache.org). All rights reserved.
