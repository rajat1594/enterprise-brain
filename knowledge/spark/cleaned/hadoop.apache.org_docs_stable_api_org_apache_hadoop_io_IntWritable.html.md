[Skip navigation links](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/IntWritable.html#skip.navbar.top "Skip navigation links")
  * [Overview](https://hadoop.apache.org/docs/stable/api/overview-summary.html)
  * [Package](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/package-summary.html)
  * Class
  * [Use](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/class-use/IntWritable.html)
  * [Tree](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/package-tree.html)
  * [Deprecated](https://hadoop.apache.org/docs/stable/api/deprecated-list.html)
  * [Index](https://hadoop.apache.org/docs/stable/api/index-all.html)
  * [Help](https://hadoop.apache.org/docs/stable/api/help-doc.html)

  * [Prev Class](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/GenericWritable.html "class in org.apache.hadoop.io")
  * [Next Class](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/IOUtils.html "class in org.apache.hadoop.io")

  * [Frames](https://hadoop.apache.org/docs/stable/api/index.html?org/apache/hadoop/io/IntWritable.html)
  * [No Frames](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/IntWritable.html)

  * [All Classes](https://hadoop.apache.org/docs/stable/api/allclasses-noframe.html)

  * Summary:
  * Nested |
  * Field |
  * [Constr](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/IntWritable.html#constructor.summary) |
  * [Method](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/IntWritable.html#method.summary)

  * Detail:
  * Field |
  * [Constr](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/IntWritable.html#constructor.detail) |
  * [Method](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/IntWritable.html#method.detail)

org.apache.hadoop.io
## Class IntWritable
  * [java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true "class or interface in java.lang")
  *     * org.apache.hadoop.io.IntWritable

  *

All Implemented Interfaces:
     [Comparable](https://docs.oracle.com/javase/8/docs/api/java/lang/Comparable.html?is-external=true "class or interface in java.lang")<[IntWritable](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/IntWritable.html "class in org.apache.hadoop.io")>, [Writable](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Writable.html "interface in org.apache.hadoop.io"), [WritableComparable](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/WritableComparable.html "interface in org.apache.hadoop.io")<[IntWritable](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/IntWritable.html "class in org.apache.hadoop.io")>
* * *

```
@InterfaceAudience.Public
 @InterfaceStability.Stable
public class IntWritable
extends Object[](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true "class or interface in java.lang")
implements WritableComparable[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/WritableComparable.html "interface in org.apache.hadoop.io")<IntWritable[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/IntWritable.html "class in org.apache.hadoop.io")>
```

A WritableComparable for ints.

  *     * ### Constructor Summary
Constructors
| Constructor and Description  |
| --- |
|  `IntWritable[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/IntWritable.html#IntWritable--)()`  |
|  `IntWritable[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/IntWritable.html#IntWritable-int-)(int value)`  |
    * ### Method Summary
All Methods[Instance Methods](javascript:show\(2\);)[Concrete Methods](javascript:show\(8\);)
| Modifier and Type  | Method and Description  |
| --- | --- |
| `int`  |  `compareTo[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/IntWritable.html#compareTo-org.apache.hadoop.io.IntWritable-)(IntWritable[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/IntWritable.html "class in org.apache.hadoop.io") o)` Compares two IntWritables.  |
| `boolean`  |  `equals[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/IntWritable.html#equals-java.lang.Object-)(Object[](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true "class or interface in java.lang") o)` Returns true iff `o` is a IntWritable with the same value.  |
| `int`  |  `get[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/IntWritable.html#get--)()` Return the value of this IntWritable.  |
| `int`  |  `hashCode[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/IntWritable.html#hashCode--)()`  |
| `void`  |  `readFields[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/IntWritable.html#readFields-java.io.DataInput-)(DataInput[](https://docs.oracle.com/javase/8/docs/api/java/io/DataInput.html?is-external=true "class or interface in java.io") in)` Deserialize the fields of this object from `in`.  |
| `void`  |  `set[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/IntWritable.html#set-int-)(int value)` Set the value of this IntWritable.  |
| `String[](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true "class or interface in java.lang")`  |  `toString[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/IntWritable.html#toString--)()`  |
| `void`  |  `write[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/IntWritable.html#write-java.io.DataOutput-)(DataOutput[](https://docs.oracle.com/javase/8/docs/api/java/io/DataOutput.html?is-external=true "class or interface in java.io") out)` Serialize the fields of this object to `out`.  |
      * ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true "class or interface in java.lang")
`clone[](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true#clone-- "class or interface in java.lang"), finalize[](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true#finalize-- "class or interface in java.lang"), getClass[](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true#getClass-- "class or interface in java.lang"), notify[](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true#notify-- "class or interface in java.lang"), notifyAll[](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true#notifyAll-- "class or interface in java.lang"), wait[](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true#wait-- "class or interface in java.lang"), wait[](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true#wait-long- "class or interface in java.lang"), wait[](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true#wait-long-int- "class or interface in java.lang")`

  *     * ### Constructor Detail
      * #### IntWritable

```
public IntWritable()
```

      * #### IntWritable

```
public IntWritable(int value)
```

    * ### Method Detail
      * #### set

```
public void set(int value)
```

Set the value of this IntWritable.

Parameters:
     `value` - input value.
      * #### get

```
public int get()
```

Return the value of this IntWritable.

Returns:
    value of this IntWritable.
      * #### readFields

```
public void readFields(DataInput[](https://docs.oracle.com/javase/8/docs/api/java/io/DataInput.html?is-external=true "class or interface in java.io") in)
                throws IOException[](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html?is-external=true "class or interface in java.io")
```

Description copied from interface: `Writable[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Writable.html#readFields-java.io.DataInput-)`
Deserialize the fields of this object from `in`.
For efficiency, implementations should attempt to re-use storage in the existing object where possible.

Specified by:
     `readFields[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Writable.html#readFields-java.io.DataInput-)` in interface `Writable[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Writable.html "interface in org.apache.hadoop.io")`

Parameters:
     `in` - `DataInput` to deseriablize this object from.

Throws:
     `IOException[](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html?is-external=true "class or interface in java.io")` - any other problem for readFields.
      * #### write

```
public void write(DataOutput[](https://docs.oracle.com/javase/8/docs/api/java/io/DataOutput.html?is-external=true "class or interface in java.io") out)
           throws IOException[](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html?is-external=true "class or interface in java.io")
```

Description copied from interface: `Writable[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Writable.html#write-java.io.DataOutput-)`
Serialize the fields of this object to `out`.

Specified by:
     `write[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Writable.html#write-java.io.DataOutput-)` in interface `Writable[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Writable.html "interface in org.apache.hadoop.io")`

Parameters:
     `out` - `DataOuput` to serialize this object into.

Throws:
     `IOException[](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html?is-external=true "class or interface in java.io")` - any other problem for write.
      * #### equals

```
public boolean equals(Object[](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true "class or interface in java.lang") o)
```

Returns true iff `o` is a IntWritable with the same value.

Overrides:
     `equals[](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true#equals-java.lang.Object- "class or interface in java.lang")` in class `Object[](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true "class or interface in java.lang")`
      * #### hashCode

```
public int hashCode()
```

Overrides:
     `hashCode[](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true#hashCode-- "class or interface in java.lang")` in class `Object[](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true "class or interface in java.lang")`
      * #### compareTo

```
public int compareTo(IntWritable[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/IntWritable.html "class in org.apache.hadoop.io") o)
```

Compares two IntWritables.

Specified by:
     `compareTo[](https://docs.oracle.com/javase/8/docs/api/java/lang/Comparable.html?is-external=true#compareTo-T- "class or interface in java.lang")` in interface `Comparable[](https://docs.oracle.com/javase/8/docs/api/java/lang/Comparable.html?is-external=true "class or interface in java.lang")<IntWritable[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/IntWritable.html "class in org.apache.hadoop.io")>`
      * #### toString

```
public String[](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true "class or interface in java.lang") toString()
```

Overrides:
     `toString[](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true#toString-- "class or interface in java.lang")` in class `Object[](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true "class or interface in java.lang")`

[Skip navigation links](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/IntWritable.html#skip.navbar.bottom "Skip navigation links")
  * [Overview](https://hadoop.apache.org/docs/stable/api/overview-summary.html)
  * [Package](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/package-summary.html)
  * Class
  * [Use](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/class-use/IntWritable.html)
  * [Tree](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/package-tree.html)
  * [Deprecated](https://hadoop.apache.org/docs/stable/api/deprecated-list.html)
  * [Index](https://hadoop.apache.org/docs/stable/api/index-all.html)
  * [Help](https://hadoop.apache.org/docs/stable/api/help-doc.html)

  * [Prev Class](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/GenericWritable.html "class in org.apache.hadoop.io")
  * [Next Class](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/IOUtils.html "class in org.apache.hadoop.io")

  * [Frames](https://hadoop.apache.org/docs/stable/api/index.html?org/apache/hadoop/io/IntWritable.html)
  * [No Frames](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/IntWritable.html)

  * [All Classes](https://hadoop.apache.org/docs/stable/api/allclasses-noframe.html)

  * Summary:
  * Nested |
  * Field |
  * [Constr](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/IntWritable.html#constructor.summary) |
  * [Method](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/IntWritable.html#method.summary)

  * Detail:
  * Field |
  * [Constr](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/IntWritable.html#constructor.detail) |
  * [Method](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/IntWritable.html#method.detail)

Copyright © 2023 [Apache Software Foundation](https://www.apache.org). All rights reserved.
