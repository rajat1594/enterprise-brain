[Skip navigation links](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Text.html#skip.navbar.top "Skip navigation links")
  * [Overview](https://hadoop.apache.org/docs/stable/api/overview-summary.html)
  * [Package](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/package-summary.html)
  * Class
  * [Use](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/class-use/Text.html)
  * [Tree](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/package-tree.html)
  * [Deprecated](https://hadoop.apache.org/docs/stable/api/deprecated-list.html)
  * [Index](https://hadoop.apache.org/docs/stable/api/index-all.html)
  * [Help](https://hadoop.apache.org/docs/stable/api/help-doc.html)


  * [Prev Class](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Stringifier.html "interface in org.apache.hadoop.io")
  * [Next Class](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/TwoDArrayWritable.html "class in org.apache.hadoop.io")


  * [Frames](https://hadoop.apache.org/docs/stable/api/index.html?org/apache/hadoop/io/Text.html)
  * [No Frames](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Text.html)


  * [All Classes](https://hadoop.apache.org/docs/stable/api/allclasses-noframe.html)


  * Summary: 
  * Nested | 
  * [Field](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Text.html#field.summary) | 
  * [Constr](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Text.html#constructor.summary) | 
  * [Method](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Text.html#method.summary)


  * Detail: 
  * [Field](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Text.html#field.detail) | 
  * [Constr](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Text.html#constructor.detail) | 
  * [Method](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Text.html#method.detail)


org.apache.hadoop.io
## Class Text
  * [java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true "class or interface in java.lang")
  *     * [org.apache.hadoop.io.BinaryComparable](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/BinaryComparable.html "class in org.apache.hadoop.io")
    *       * org.apache.hadoop.io.Text


  * 

All Implemented Interfaces:
     [Comparable](https://docs.oracle.com/javase/8/docs/api/java/lang/Comparable.html?is-external=true "class or interface in java.lang")<[BinaryComparable](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/BinaryComparable.html "class in org.apache.hadoop.io")>, [Writable](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Writable.html "interface in org.apache.hadoop.io"), [WritableComparable](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/WritableComparable.html "interface in org.apache.hadoop.io")<[BinaryComparable](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/BinaryComparable.html "class in org.apache.hadoop.io")>
* * *
  

```
@Stringable
 @InterfaceAudience.Public
 @InterfaceStability.Stable
public class Text
extends BinaryComparable[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/BinaryComparable.html "class in org.apache.hadoop.io")
implements WritableComparable[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/WritableComparable.html "interface in org.apache.hadoop.io")<BinaryComparable[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/BinaryComparable.html "class in org.apache.hadoop.io")>
```

This class stores text using standard UTF8 encoding. It provides methods to serialize, deserialize, and compare texts at byte level. The type of length is integer and is serialized using zero-compressed format. 
In addition, it provides methods for string traversal without converting the byte array to a string. 
Also includes utilities for serializing/deserialing a string, coding/decoding a string, checking if a byte array contains valid UTF8 code, calculating the length of an encoded string.


  *     * ### Field Summary  
Fields  
| Modifier and Type  | Field and Description  |  
| --- | --- |  
| `static int`  |  `DEFAULT_MAX_LEN[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Text.html#DEFAULT_MAX_LEN)`  |  
    * ### Constructor Summary  
Constructors  
| Constructor and Description  |  
| --- |  
|  `Text[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Text.html#Text--)()`  |  
|  `Text[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Text.html#Text-byte:A-)(byte[] utf8)` Construct from a byte array.  |  
|  `Text[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Text.html#Text-java.lang.String-)(String[](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true "class or interface in java.lang") string)` Construct from a string.  |  
|  `Text[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Text.html#Text-org.apache.hadoop.io.Text-)(Text[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Text.html "class in org.apache.hadoop.io") utf8)` Construct from another text.  |  
    * ### Method Summary  
All Methods[Static Methods](javascript:show\(1\);)[Instance Methods](javascript:show\(2\);)[Concrete Methods](javascript:show\(8\);)  
| Modifier and Type  | Method and Description  |  
| --- | --- |  
| `void`  |  `append[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Text.html#append-byte:A-int-int-)(byte[] utf8,       int start,       int len)` Append a range of bytes to the end of the given text  |  
| `static int`  |  `bytesToCodePoint[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Text.html#bytesToCodePoint-java.nio.ByteBuffer-)(ByteBuffer[](https://docs.oracle.com/javase/8/docs/api/java/nio/ByteBuffer.html?is-external=true "class or interface in java.nio") bytes)`  |  
| `int`  |  `charAt[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Text.html#charAt-int-)(int position)` Returns the Unicode Scalar Value (32-bit integer value) for the character at `position`.  |  
| `void`  |  `clear[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Text.html#clear--)()` Clear the string to empty.  |  
| `byte[]`  |  `copyBytes[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Text.html#copyBytes--)()`  |  
| `static String[](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true "class or interface in java.lang")`  |  `decode[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Text.html#decode-byte:A-)(byte[] utf8)`  |  
| `static String[](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true "class or interface in java.lang")`  |  `decode[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Text.html#decode-byte:A-int-int-)(byte[] utf8,       int start,       int length)`  |  
| `static String[](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true "class or interface in java.lang")`  |  `decode[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Text.html#decode-byte:A-int-int-boolean-)(byte[] utf8,       int start,       int length,       boolean replace)`  |  
| `static ByteBuffer[](https://docs.oracle.com/javase/8/docs/api/java/nio/ByteBuffer.html?is-external=true "class or interface in java.nio")`  |  `encode[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Text.html#encode-java.lang.String-)(String[](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true "class or interface in java.lang") string)` Converts the provided String to bytes using the UTF-8 encoding.  |  
| `static ByteBuffer[](https://docs.oracle.com/javase/8/docs/api/java/nio/ByteBuffer.html?is-external=true "class or interface in java.nio")`  |  `encode[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Text.html#encode-java.lang.String-boolean-)(String[](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true "class or interface in java.lang") string,       boolean replace)` Converts the provided String to bytes using the UTF-8 encoding.  |  
| `boolean`  |  `equals[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Text.html#equals-java.lang.Object-)(Object[](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true "class or interface in java.lang") o)` Returns true iff `o` is a Text with the same contents.  |  
| `int`  |  `find[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Text.html#find-java.lang.String-)(String[](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true "class or interface in java.lang") what)`  |  
| `int`  |  `find[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Text.html#find-java.lang.String-int-)(String[](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true "class or interface in java.lang") what,     int start)` Finds any occurrence of `what` in the backing buffer, starting as position `start`.  |  
| `byte[]`  |  `getBytes[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Text.html#getBytes--)()` Returns the raw bytes; however, only data up to [`getLength()`](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Text.html#getLength--) is valid.  |  
| `int`  |  `getLength[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Text.html#getLength--)()` Returns the number of bytes in the byte array  |  
| `int`  |  `hashCode[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Text.html#hashCode--)()` Return a hash of the bytes returned from {#getBytes()}.  |  
| `void`  |  `readFields[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Text.html#readFields-java.io.DataInput-)(DataInput[](https://docs.oracle.com/javase/8/docs/api/java/io/DataInput.html?is-external=true "class or interface in java.io") in)` deserialize  |  
| `void`  |  `readFields[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Text.html#readFields-java.io.DataInput-int-)(DataInput[](https://docs.oracle.com/javase/8/docs/api/java/io/DataInput.html?is-external=true "class or interface in java.io") in,           int maxLength)`  |  
| `static String[](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true "class or interface in java.lang")`  |  `readString[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Text.html#readString-java.io.DataInput-)(DataInput[](https://docs.oracle.com/javase/8/docs/api/java/io/DataInput.html?is-external=true "class or interface in java.io") in)`  |  
| `static String[](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true "class or interface in java.lang")`  |  `readString[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Text.html#readString-java.io.DataInput-int-)(DataInput[](https://docs.oracle.com/javase/8/docs/api/java/io/DataInput.html?is-external=true "class or interface in java.io") in,           int maxLength)`  |  
| `void`  |  `readWithKnownLength[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Text.html#readWithKnownLength-java.io.DataInput-int-)(DataInput[](https://docs.oracle.com/javase/8/docs/api/java/io/DataInput.html?is-external=true "class or interface in java.io") in,                    int len)` Read a Text object whose length is already known.  |  
| `void`  |  `set[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Text.html#set-byte:A-)(byte[] utf8)` Set to a utf8 byte array.  |  
| `void`  |  `set[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Text.html#set-byte:A-int-int-)(byte[] utf8,    int start,    int len)` Set the Text to range of bytes  |  
| `void`  |  `set[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Text.html#set-java.lang.String-)(String[](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true "class or interface in java.lang") string)` Set to contain the contents of a string.  |  
| `void`  |  `set[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Text.html#set-org.apache.hadoop.io.Text-)(Text[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Text.html "class in org.apache.hadoop.io") other)` copy a text.  |  
| `static void`  |  `skip[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Text.html#skip-java.io.DataInput-)(DataInput[](https://docs.oracle.com/javase/8/docs/api/java/io/DataInput.html?is-external=true "class or interface in java.io") in)` Skips over one Text in the input.  |  
| `String[](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true "class or interface in java.lang")`  |  `toString[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Text.html#toString--)()` Convert text back to string  |  
| `static int`  |  `utf8Length[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Text.html#utf8Length-java.lang.String-)(String[](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true "class or interface in java.lang") string)` For the given string, returns the number of UTF-8 bytes required to encode the string.  |  
| `static void`  |  `validateUTF8[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Text.html#validateUTF8-byte:A-)(byte[] utf8)` Check if a byte array contains valid utf-8  |  
| `static void`  |  `validateUTF8[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Text.html#validateUTF8-byte:A-int-int-)(byte[] utf8,             int start,             int len)` Check to see if a byte array is valid utf-8  |  
| `void`  |  `write[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Text.html#write-java.io.DataOutput-)(DataOutput[](https://docs.oracle.com/javase/8/docs/api/java/io/DataOutput.html?is-external=true "class or interface in java.io") out)` serialize write this object to out length uses zero-compressed encoding  |  
| `void`  |  `write[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Text.html#write-java.io.DataOutput-int-)(DataOutput[](https://docs.oracle.com/javase/8/docs/api/java/io/DataOutput.html?is-external=true "class or interface in java.io") out,      int maxLength)`  |  
| `static int`  |  `writeString[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Text.html#writeString-java.io.DataOutput-java.lang.String-)(DataOutput[](https://docs.oracle.com/javase/8/docs/api/java/io/DataOutput.html?is-external=true "class or interface in java.io") out,            String[](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true "class or interface in java.lang") s)`  |  
| `static int`  |  `writeString[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Text.html#writeString-java.io.DataOutput-java.lang.String-int-)(DataOutput[](https://docs.oracle.com/javase/8/docs/api/java/io/DataOutput.html?is-external=true "class or interface in java.io") out,            String[](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true "class or interface in java.lang") s,            int maxLength)`  |  
      * ### Methods inherited from class org.apache.hadoop.io.[BinaryComparable](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/BinaryComparable.html "class in org.apache.hadoop.io")
`compareTo[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/BinaryComparable.html#compareTo-org.apache.hadoop.io.BinaryComparable-), compareTo[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/BinaryComparable.html#compareTo-byte:A-int-int-)`
      * ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true "class or interface in java.lang")
`clone[](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true#clone-- "class or interface in java.lang"), finalize[](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true#finalize-- "class or interface in java.lang"), getClass[](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true#getClass-- "class or interface in java.lang"), notify[](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true#notify-- "class or interface in java.lang"), notifyAll[](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true#notifyAll-- "class or interface in java.lang"), wait[](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true#wait-- "class or interface in java.lang"), wait[](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true#wait-long- "class or interface in java.lang"), wait[](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true#wait-long-int- "class or interface in java.lang")`
      * ### Methods inherited from interface java.lang.[Comparable](https://docs.oracle.com/javase/8/docs/api/java/lang/Comparable.html?is-external=true "class or interface in java.lang")
`compareTo[](https://docs.oracle.com/javase/8/docs/api/java/lang/Comparable.html?is-external=true#compareTo-T- "class or interface in java.lang")`


  *     * ### Field Detail
      * #### DEFAULT_MAX_LEN

```
public static final int DEFAULT_MAX_LEN
```


See Also:
    [Constant Field Values](https://hadoop.apache.org/docs/stable/api/constant-values.html#org.apache.hadoop.io.Text.DEFAULT_MAX_LEN)
    * ### Constructor Detail
      * #### Text

```
public Text()
```

      * #### Text

```
public Text(String[](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true "class or interface in java.lang") string)
```

Construct from a string. 

Parameters:
     `string` - input string.
      * #### Text

```
public Text(Text[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Text.html "class in org.apache.hadoop.io") utf8)
```

Construct from another text. 

Parameters:
     `utf8` - input utf8.
      * #### Text

```
public Text(byte[] utf8)
```

Construct from a byte array. 

Parameters:
     `utf8` - input utf8.
    * ### Method Detail
      * #### copyBytes

```
public byte[] copyBytes()
```


Returns:
    Get a copy of the bytes that is exactly the length of the data. See [`getBytes()`](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Text.html#getBytes--) for faster access to the underlying array.
      * #### getBytes

```
public byte[] getBytes()
```

Returns the raw bytes; however, only data up to [`getLength()`](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Text.html#getLength--) is valid. Please use [`copyBytes()`](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Text.html#copyBytes--) if you need the returned array to be precisely the length of the data. 

Specified by:
     `getBytes[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/BinaryComparable.html#getBytes--)` in class `BinaryComparable[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/BinaryComparable.html "class in org.apache.hadoop.io")` 

Returns:
    getBytes.
      * #### getLength

```
public int getLength()
```

Returns the number of bytes in the byte array 

Specified by:
     `getLength[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/BinaryComparable.html#getLength--)` in class `BinaryComparable[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/BinaryComparable.html "class in org.apache.hadoop.io")` 

Returns:
    length.
      * #### charAt

```
public int charAt(int position)
```

Returns the Unicode Scalar Value (32-bit integer value) for the character at `position`. Note that this method avoids using the converter or doing String instantiation. 

Parameters:
     `position` - input position. 

Returns:
    the Unicode scalar value at position or -1 if the position is invalid or points to a trailing byte.
      * #### find

```
public int find(String[](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true "class or interface in java.lang") what)
```

      * #### find

```
public int find(String[](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true "class or interface in java.lang") what,
                int start)
```

Finds any occurrence of `what` in the backing buffer, starting as position `start`. The starting position is measured in bytes and the return value is in terms of byte position in the buffer. The backing buffer is not converted to a string for this operation. 

Parameters:
     `what` - input what.      `start` - input start. 

Returns:
    byte position of the first occurrence of the search string in the UTF-8 buffer or -1 if not found
      * #### set

```
public void set(String[](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true "class or interface in java.lang") string)
```

Set to contain the contents of a string. 

Parameters:
     `string` - input string.
      * #### set

```
public void set(byte[] utf8)
```

Set to a utf8 byte array. 

Parameters:
     `utf8` - input utf8.
      * #### set

```
public void set(Text[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Text.html "class in org.apache.hadoop.io") other)
```

copy a text. 

Parameters:
     `other` - input other.
      * #### set

```
public void set(byte[] utf8,
                int start,
                int len)
```

Set the Text to range of bytes 

Parameters:
     `utf8` - the data to copy from      `start` - the first position of the new string      `len` - the number of bytes of the new string
      * #### append

```
public void append(byte[] utf8,
                   int start,
                   int len)
```

Append a range of bytes to the end of the given text 

Parameters:
     `utf8` - the data to copy from      `start` - the first position to append from utf8      `len` - the number of bytes to append
      * #### clear

```
public void clear()
```

Clear the string to empty. _Note_ : For performance reasons, this call does not clear the underlying byte array that is retrievable via [`getBytes()`](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Text.html#getBytes--). In order to free the byte-array memory, call [`set(byte[])`](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Text.html#set-byte:A-) with an empty byte array (For example, `new byte[0]`).
      * #### toString

```
public String[](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true "class or interface in java.lang") toString()
```

Convert text back to string 

Overrides:
     `toString[](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true#toString-- "class or interface in java.lang")` in class `Object[](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true "class or interface in java.lang")` 

See Also:
    [`Object.toString()`](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true#toString-- "class or interface in java.lang")
      * #### readFields

```
public void readFields(DataInput[](https://docs.oracle.com/javase/8/docs/api/java/io/DataInput.html?is-external=true "class or interface in java.io") in)
                throws IOException[](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html?is-external=true "class or interface in java.io")
```

deserialize 

Specified by:
     `readFields[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Writable.html#readFields-java.io.DataInput-)` in interface `Writable[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Writable.html "interface in org.apache.hadoop.io")` 

Parameters:
     `in` - `DataInput` to deseriablize this object from. 

Throws:
     `IOException[](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html?is-external=true "class or interface in java.io")` - any other problem for readFields.
      * #### readFields

```
public void readFields(DataInput[](https://docs.oracle.com/javase/8/docs/api/java/io/DataInput.html?is-external=true "class or interface in java.io") in,
                       int maxLength)
                throws IOException[](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html?is-external=true "class or interface in java.io")
```


Throws:
    `IOException[](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html?is-external=true "class or interface in java.io")`
      * #### skip

```
public static void skip(DataInput[](https://docs.oracle.com/javase/8/docs/api/java/io/DataInput.html?is-external=true "class or interface in java.io") in)
                 throws IOException[](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html?is-external=true "class or interface in java.io")
```

Skips over one Text in the input. 

Parameters:
     `in` - input in. 

Throws:
     `IOException[](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html?is-external=true "class or interface in java.io")` - raised on errors performing I/O.
      * #### readWithKnownLength

```
public void readWithKnownLength(DataInput[](https://docs.oracle.com/javase/8/docs/api/java/io/DataInput.html?is-external=true "class or interface in java.io") in,
                                int len)
                         throws IOException[](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html?is-external=true "class or interface in java.io")
```

Read a Text object whose length is already known. This allows creating Text from a stream which uses a different serialization format. 

Parameters:
     `in` - input in.      `len` - input len. 

Throws:
     `IOException[](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html?is-external=true "class or interface in java.io")` - raised on errors performing I/O.
      * #### write

```
public void write(DataOutput[](https://docs.oracle.com/javase/8/docs/api/java/io/DataOutput.html?is-external=true "class or interface in java.io") out)
           throws IOException[](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html?is-external=true "class or interface in java.io")
```

serialize write this object to out length uses zero-compressed encoding 

Specified by:
     `write[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Writable.html#write-java.io.DataOutput-)` in interface `Writable[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Writable.html "interface in org.apache.hadoop.io")` 

Parameters:
     `out` - `DataOuput` to serialize this object into. 

Throws:
     `IOException[](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html?is-external=true "class or interface in java.io")` - any other problem for write. 

See Also:
    [`Writable.write(DataOutput)`](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Writable.html#write-java.io.DataOutput-)
      * #### write

```
public void write(DataOutput[](https://docs.oracle.com/javase/8/docs/api/java/io/DataOutput.html?is-external=true "class or interface in java.io") out,
                  int maxLength)
           throws IOException[](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html?is-external=true "class or interface in java.io")
```


Throws:
    `IOException[](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html?is-external=true "class or interface in java.io")`
      * #### equals

```
public boolean equals(Object[](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true "class or interface in java.lang") o)
```

Returns true iff `o` is a Text with the same contents. 

Overrides:
     `equals[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/BinaryComparable.html#equals-java.lang.Object-)` in class `BinaryComparable[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/BinaryComparable.html "class in org.apache.hadoop.io")`
      * #### hashCode

```
public int hashCode()
```

Description copied from class: `BinaryComparable[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/BinaryComparable.html#hashCode--)`
Return a hash of the bytes returned from {#getBytes()}. 

Overrides:
     `hashCode[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/BinaryComparable.html#hashCode--)` in class `BinaryComparable[](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/BinaryComparable.html "class in org.apache.hadoop.io")` 

See Also:
    [`WritableComparator.hashBytes(byte[],int)`](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/WritableComparator.html#hashBytes-byte:A-int-)
      * #### decode

```
public static String[](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true "class or interface in java.lang") decode(byte[] utf8)
                     throws CharacterCodingException[](https://docs.oracle.com/javase/8/docs/api/java/nio/charset/CharacterCodingException.html?is-external=true "class or interface in java.nio.charset")
```


Parameters:
     `utf8` - input utf8. 

Returns:
    Converts the provided byte array to a String using the UTF-8 encoding. If the input is malformed, replace by a default value. 

Throws:
     `CharacterCodingException[](https://docs.oracle.com/javase/8/docs/api/java/nio/charset/CharacterCodingException.html?is-external=true "class or interface in java.nio.charset")` - a character encoding or decoding error occurs.
      * #### decode

```
public static String[](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true "class or interface in java.lang") decode(byte[] utf8,
                            int start,
                            int length)
                     throws CharacterCodingException[](https://docs.oracle.com/javase/8/docs/api/java/nio/charset/CharacterCodingException.html?is-external=true "class or interface in java.nio.charset")
```


Throws:
    `CharacterCodingException[](https://docs.oracle.com/javase/8/docs/api/java/nio/charset/CharacterCodingException.html?is-external=true "class or interface in java.nio.charset")`
      * #### decode

```
public static String[](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true "class or interface in java.lang") decode(byte[] utf8,
                            int start,
                            int length,
                            boolean replace)
                     throws CharacterCodingException[](https://docs.oracle.com/javase/8/docs/api/java/nio/charset/CharacterCodingException.html?is-external=true "class or interface in java.nio.charset")
```


Parameters:
     `utf8` - input utf8.      `start` - input start.      `length` - input length.      `replace` - input replace. 

Returns:
    Converts the provided byte array to a String using the UTF-8 encoding. If `replace` is true, then malformed input is replaced with the substitution character, which is U+FFFD. Otherwise the method throws a MalformedInputException. 

Throws:
     `CharacterCodingException[](https://docs.oracle.com/javase/8/docs/api/java/nio/charset/CharacterCodingException.html?is-external=true "class or interface in java.nio.charset")` - a character encoding or decoding error occurs.
      * #### encode

```
public static ByteBuffer[](https://docs.oracle.com/javase/8/docs/api/java/nio/ByteBuffer.html?is-external=true "class or interface in java.nio") encode(String[](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true "class or interface in java.lang") string)
                         throws CharacterCodingException[](https://docs.oracle.com/javase/8/docs/api/java/nio/charset/CharacterCodingException.html?is-external=true "class or interface in java.nio.charset")
```

Converts the provided String to bytes using the UTF-8 encoding. If the input is malformed, invalid chars are replaced by a default value. 

Parameters:
     `string` - input string. 

Returns:
    ByteBuffer: bytes stores at ByteBuffer.array() and length is ByteBuffer.limit() 

Throws:
     `CharacterCodingException[](https://docs.oracle.com/javase/8/docs/api/java/nio/charset/CharacterCodingException.html?is-external=true "class or interface in java.nio.charset")` - a character encoding or decoding error occurs.
      * #### encode

```
public static ByteBuffer[](https://docs.oracle.com/javase/8/docs/api/java/nio/ByteBuffer.html?is-external=true "class or interface in java.nio") encode(String[](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true "class or interface in java.lang") string,
                                boolean replace)
                         throws CharacterCodingException[](https://docs.oracle.com/javase/8/docs/api/java/nio/charset/CharacterCodingException.html?is-external=true "class or interface in java.nio.charset")
```

Converts the provided String to bytes using the UTF-8 encoding. If `replace` is true, then malformed input is replaced with the substitution character, which is U+FFFD. Otherwise the method throws a MalformedInputException. 

Parameters:
     `string` - input string.      `replace` - input replace. 

Returns:
    ByteBuffer: bytes stores at ByteBuffer.array() and length is ByteBuffer.limit() 

Throws:
     `CharacterCodingException[](https://docs.oracle.com/javase/8/docs/api/java/nio/charset/CharacterCodingException.html?is-external=true "class or interface in java.nio.charset")` - a character encoding or decoding error occurs.
      * #### readString

```
public static String[](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true "class or interface in java.lang") readString(DataInput[](https://docs.oracle.com/javase/8/docs/api/java/io/DataInput.html?is-external=true "class or interface in java.io") in)
                         throws IOException[](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html?is-external=true "class or interface in java.io")
```


Parameters:
     `in` - input in. 

Returns:
    Read a UTF8 encoded string from in. 

Throws:
     `IOException[](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html?is-external=true "class or interface in java.io")` - raised on errors performing I/O.
      * #### readString

```
public static String[](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true "class or interface in java.lang") readString(DataInput[](https://docs.oracle.com/javase/8/docs/api/java/io/DataInput.html?is-external=true "class or interface in java.io") in,
                                int maxLength)
                         throws IOException[](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html?is-external=true "class or interface in java.io")
```


Parameters:
     `in` - input in.      `maxLength` - input maxLength. 

Returns:
    Read a UTF8 encoded string with a maximum size. 

Throws:
     `IOException[](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html?is-external=true "class or interface in java.io")` - raised on errors performing I/O.
      * #### writeString

```
public static int writeString(DataOutput[](https://docs.oracle.com/javase/8/docs/api/java/io/DataOutput.html?is-external=true "class or interface in java.io") out,
                              String[](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true "class or interface in java.lang") s)
                       throws IOException[](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html?is-external=true "class or interface in java.io")
```


Parameters:
     `out` - input out.      `s` - input s. 

Returns:
    Write a UTF8 encoded string to out. 

Throws:
     `IOException[](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html?is-external=true "class or interface in java.io")` - raised on errors performing I/O.
      * #### writeString

```
public static int writeString(DataOutput[](https://docs.oracle.com/javase/8/docs/api/java/io/DataOutput.html?is-external=true "class or interface in java.io") out,
                              String[](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true "class or interface in java.lang") s,
                              int maxLength)
                       throws IOException[](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html?is-external=true "class or interface in java.io")
```


Parameters:
     `out` - input out.      `s` - input s.      `maxLength` - input maxLength. 

Returns:
    Write a UTF8 encoded string with a maximum size to out. 

Throws:
     `IOException[](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html?is-external=true "class or interface in java.io")` - raised on errors performing I/O.
      * #### validateUTF8

```
public static void validateUTF8(byte[] utf8)
                         throws MalformedInputException[](https://docs.oracle.com/javase/8/docs/api/java/nio/charset/MalformedInputException.html?is-external=true "class or interface in java.nio.charset")
```

Check if a byte array contains valid utf-8 

Parameters:
     `utf8` - byte array 

Throws:
     `MalformedInputException[](https://docs.oracle.com/javase/8/docs/api/java/nio/charset/MalformedInputException.html?is-external=true "class or interface in java.nio.charset")` - if the byte array contains invalid utf-8
      * #### validateUTF8

```
public static void validateUTF8(byte[] utf8,
                                int start,
                                int len)
                         throws MalformedInputException[](https://docs.oracle.com/javase/8/docs/api/java/nio/charset/MalformedInputException.html?is-external=true "class or interface in java.nio.charset")
```

Check to see if a byte array is valid utf-8 

Parameters:
     `utf8` - the array of bytes      `start` - the offset of the first byte in the array      `len` - the length of the byte sequence 

Throws:
     `MalformedInputException[](https://docs.oracle.com/javase/8/docs/api/java/nio/charset/MalformedInputException.html?is-external=true "class or interface in java.nio.charset")` - if the byte array contains invalid bytes
      * #### bytesToCodePoint

```
public static int bytesToCodePoint(ByteBuffer[](https://docs.oracle.com/javase/8/docs/api/java/nio/ByteBuffer.html?is-external=true "class or interface in java.nio") bytes)
```


Parameters:
     `bytes` - input bytes. 

Returns:
    Returns the next code point at the current position in the buffer. The buffer's position will be incremented. Any mark set on this buffer will be changed by this method!
      * #### utf8Length

```
public static int utf8Length(String[](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true "class or interface in java.lang") string)
```

For the given string, returns the number of UTF-8 bytes required to encode the string. 

Parameters:
     `string` - text to encode 

Returns:
    number of UTF-8 bytes required to encode


[Skip navigation links](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Text.html#skip.navbar.bottom "Skip navigation links")
  * [Overview](https://hadoop.apache.org/docs/stable/api/overview-summary.html)
  * [Package](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/package-summary.html)
  * Class
  * [Use](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/class-use/Text.html)
  * [Tree](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/package-tree.html)
  * [Deprecated](https://hadoop.apache.org/docs/stable/api/deprecated-list.html)
  * [Index](https://hadoop.apache.org/docs/stable/api/index-all.html)
  * [Help](https://hadoop.apache.org/docs/stable/api/help-doc.html)


  * [Prev Class](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Stringifier.html "interface in org.apache.hadoop.io")
  * [Next Class](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/TwoDArrayWritable.html "class in org.apache.hadoop.io")


  * [Frames](https://hadoop.apache.org/docs/stable/api/index.html?org/apache/hadoop/io/Text.html)
  * [No Frames](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Text.html)


  * [All Classes](https://hadoop.apache.org/docs/stable/api/allclasses-noframe.html)


  * Summary: 
  * Nested | 
  * [Field](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Text.html#field.summary) | 
  * [Constr](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Text.html#constructor.summary) | 
  * [Method](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Text.html#method.summary)


  * Detail: 
  * [Field](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Text.html#field.detail) | 
  * [Constr](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Text.html#constructor.detail) | 
  * [Method](https://hadoop.apache.org/docs/stable/api/org/apache/hadoop/io/Text.html#method.detail)


Copyright © 2023 [Apache Software Foundation](https://www.apache.org). All rights reserved.
