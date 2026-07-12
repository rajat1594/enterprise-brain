[Skip navigation links](https://spark.apache.org/docs/latest/api/java/org/apache/spark/serializer/package-summary.html#skip-navbar-top "Skip navigation links")
  * [Overview](https://spark.apache.org/docs/latest/api/java/index.html)
  * Package
  * Class
  * [Deprecated](https://spark.apache.org/docs/latest/api/java/deprecated-list.html)
  * [Index](https://spark.apache.org/docs/latest/api/java/index-all.html)
  * [Help](https://spark.apache.org/docs/latest/api/java/help-doc.html#package)

  * Package:
  * [Description](https://spark.apache.org/docs/latest/api/java/org/apache/spark/serializer/package-summary.html#package-description) |
  * [Related Packages](https://spark.apache.org/docs/latest/api/java/org/apache/spark/serializer/package-summary.html#related-package-summary) |
  * [Classes and Interfaces](https://spark.apache.org/docs/latest/api/java/org/apache/spark/serializer/package-summary.html#class-summary)

SEARCH:
# Package org.apache.spark.serializer
* * *
package org.apache.spark.serializer
Pluggable serializers for RDD and shuffle data.
  * Related Packages
Package
Description
[org.apache.spark](https://spark.apache.org/docs/latest/api/java/org/apache/spark/package-summary.html)
Core Spark classes in Scala.
  * All Classes and InterfacesInterfacesClasses
Class
Description
[DeserializationStream](https://spark.apache.org/docs/latest/api/java/org/apache/spark/serializer/DeserializationStream.html "class in org.apache.spark.serializer")
Developer API A stream for reading serialized objects.
[DummyInvocationHandler](https://spark.apache.org/docs/latest/api/java/org/apache/spark/serializer/DummyInvocationHandler.html "class in org.apache.spark.serializer")
[DummySerializerInstance](https://spark.apache.org/docs/latest/api/java/org/apache/spark/serializer/DummySerializerInstance.html "class in org.apache.spark.serializer")
Unfortunately, we need a serializer instance in order to construct a DiskBlockObjectWriter.
[JavaIterableWrapperSerializer](https://spark.apache.org/docs/latest/api/java/org/apache/spark/serializer/JavaIterableWrapperSerializer.html "class in org.apache.spark.serializer")
A Kryo serializer for serializing results returned by asJavaIterable.
[JavaSerializer](https://spark.apache.org/docs/latest/api/java/org/apache/spark/serializer/JavaSerializer.html "class in org.apache.spark.serializer")
Developer API A Spark serializer that uses Java's built-in serialization.
[KryoRegistrator](https://spark.apache.org/docs/latest/api/java/org/apache/spark/serializer/KryoRegistrator.html "interface in org.apache.spark.serializer")
Interface implemented by clients to register their classes with Kryo when using Kryo serialization.
[KryoSerializer](https://spark.apache.org/docs/latest/api/java/org/apache/spark/serializer/KryoSerializer.html "class in org.apache.spark.serializer")
A Spark serializer that uses the [ Kryo serialization library](https://code.google.com/p/kryo/).
[SerializationDebugger](https://spark.apache.org/docs/latest/api/java/org/apache/spark/serializer/SerializationDebugger.html "class in org.apache.spark.serializer")
[SerializationDebugger.ObjectStreamClassMethods](https://spark.apache.org/docs/latest/api/java/org/apache/spark/serializer/SerializationDebugger.ObjectStreamClassMethods.html "class in org.apache.spark.serializer")
An implicit class that allows us to call private methods of ObjectStreamClass.
[SerializationDebugger.ObjectStreamClassMethods$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/serializer/SerializationDebugger.ObjectStreamClassMethods$.html "class in org.apache.spark.serializer")
[SerializationStream](https://spark.apache.org/docs/latest/api/java/org/apache/spark/serializer/SerializationStream.html "class in org.apache.spark.serializer")
Developer API A stream for writing serialized objects.
[Serializer](https://spark.apache.org/docs/latest/api/java/org/apache/spark/serializer/Serializer.html "class in org.apache.spark.serializer")
Developer API A serializer.
[SerializerHelper](https://spark.apache.org/docs/latest/api/java/org/apache/spark/serializer/SerializerHelper.html "class in org.apache.spark.serializer")
[SerializerInstance](https://spark.apache.org/docs/latest/api/java/org/apache/spark/serializer/SerializerInstance.html "class in org.apache.spark.serializer")
Developer API An instance of a serializer, for use by one thread at a time.
