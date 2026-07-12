[Skip navigation links](https://spark.apache.org/docs/latest/api/java/org/apache/spark/io/package-summary.html#skip-navbar-top "Skip navigation links")
  * [Overview](https://spark.apache.org/docs/latest/api/java/index.html)
  * Package
  * Class
  * [Deprecated](https://spark.apache.org/docs/latest/api/java/deprecated-list.html)
  * [Index](https://spark.apache.org/docs/latest/api/java/index-all.html)
  * [Help](https://spark.apache.org/docs/latest/api/java/help-doc.html#package)

  * Package:
  * [Description](https://spark.apache.org/docs/latest/api/java/org/apache/spark/io/package-summary.html#package-description) |
  * [Related Packages](https://spark.apache.org/docs/latest/api/java/org/apache/spark/io/package-summary.html#related-package-summary) |
  * [Classes and Interfaces](https://spark.apache.org/docs/latest/api/java/org/apache/spark/io/package-summary.html#class-summary)

SEARCH:
# Package org.apache.spark.io
* * *
package org.apache.spark.io
IO codecs used for compression.
  * Related Packages
Package
Description
[org.apache.spark](https://spark.apache.org/docs/latest/api/java/org/apache/spark/package-summary.html)
Core Spark classes in Scala.
  * All Classes and InterfacesInterfacesClasses
Class
Description
[CompressionCodec](https://spark.apache.org/docs/latest/api/java/org/apache/spark/io/CompressionCodec.html "interface in org.apache.spark.io")
Developer API CompressionCodec allows the customization of choosing different compression implementations to be used in block storage.
[HadoopCodecStreams](https://spark.apache.org/docs/latest/api/java/org/apache/spark/io/HadoopCodecStreams.html "class in org.apache.spark.io")
An utility object to look up Hadoop compression codecs and create input streams.
[LZ4CompressionCodec](https://spark.apache.org/docs/latest/api/java/org/apache/spark/io/LZ4CompressionCodec.html "class in org.apache.spark.io")
Developer API LZ4 implementation of [`CompressionCodec`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/io/CompressionCodec.html "interface in org.apache.spark.io").
[LZFCompressionCodec](https://spark.apache.org/docs/latest/api/java/org/apache/spark/io/LZFCompressionCodec.html "class in org.apache.spark.io")
Developer API LZF implementation of [`CompressionCodec`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/io/CompressionCodec.html "interface in org.apache.spark.io").
[NioBufferedFileInputStream](https://spark.apache.org/docs/latest/api/java/org/apache/spark/io/NioBufferedFileInputStream.html "class in org.apache.spark.io")
[`InputStream`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html "class or interface in java.io") implementation which uses direct buffer to read a file to avoid extra copy of data between Java and native memory which happens when using [`BufferedInputStream`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/BufferedInputStream.html "class or interface in java.io").
[ReadAheadInputStream](https://spark.apache.org/docs/latest/api/java/org/apache/spark/io/ReadAheadInputStream.html "class in org.apache.spark.io")
[`InputStream`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html "class or interface in java.io") implementation which asynchronously reads ahead from the underlying input stream when specified amount of data has been read from the current buffer.
[SnappyCompressionCodec](https://spark.apache.org/docs/latest/api/java/org/apache/spark/io/SnappyCompressionCodec.html "class in org.apache.spark.io")
Developer API Snappy implementation of [`CompressionCodec`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/io/CompressionCodec.html "interface in org.apache.spark.io").
[ZStdCompressionCodec](https://spark.apache.org/docs/latest/api/java/org/apache/spark/io/ZStdCompressionCodec.html "class in org.apache.spark.io")
Developer API ZStandard implementation of [`CompressionCodec`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/io/CompressionCodec.html "interface in org.apache.spark.io").
