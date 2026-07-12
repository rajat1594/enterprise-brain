[Skip navigation links](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/write/streaming/package-summary.html#skip-navbar-top "Skip navigation links")
  * [Overview](https://spark.apache.org/docs/latest/api/java/index.html)
  * Package
  * Class
  * [Deprecated](https://spark.apache.org/docs/latest/api/java/deprecated-list.html)
  * [Index](https://spark.apache.org/docs/latest/api/java/index-all.html)
  * [Help](https://spark.apache.org/docs/latest/api/java/help-doc.html#package)

  * Package:
  * Description |
  * [Related Packages](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/write/streaming/package-summary.html#related-package-summary) |
  * [Classes and Interfaces](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/write/streaming/package-summary.html#class-summary)

SEARCH:
# Package org.apache.spark.sql.connector.write.streaming
* * *
package org.apache.spark.sql.connector.write.streaming
  * Related Packages
Package
Description
[org.apache.spark.sql.connector.write](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/write/package-summary.html)
  * Interfaces
Class
Description
[StreamingDataWriterFactory](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/write/streaming/StreamingDataWriterFactory.html "interface in org.apache.spark.sql.connector.write.streaming")
A factory of [`DataWriter`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/write/DataWriter.html "interface in org.apache.spark.sql.connector.write") returned by [`StreamingWrite.createStreamingWriterFactory(PhysicalWriteInfo)`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/write/streaming/StreamingWrite.html#createStreamingWriterFactory\(org.apache.spark.sql.connector.write.PhysicalWriteInfo\)), which is responsible for creating and initializing the actual data writer at executor side.
[StreamingWrite](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/write/streaming/StreamingWrite.html "interface in org.apache.spark.sql.connector.write.streaming")
An interface that defines how to write the data to data source in streaming queries.
