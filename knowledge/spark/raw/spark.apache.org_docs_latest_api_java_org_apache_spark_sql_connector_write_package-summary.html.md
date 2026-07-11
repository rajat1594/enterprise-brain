[Skip navigation links](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/write/package-summary.html#skip-navbar-top "Skip navigation links")
  * [Overview](https://spark.apache.org/docs/latest/api/java/index.html)
  * Package
  * Class
  * [Deprecated](https://spark.apache.org/docs/latest/api/java/deprecated-list.html)
  * [Index](https://spark.apache.org/docs/latest/api/java/index-all.html)
  * [Help](https://spark.apache.org/docs/latest/api/java/help-doc.html#package)


  * Package: 
  * Description | 
  * [Related Packages](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/write/package-summary.html#related-package-summary) | 
  * [Classes and Interfaces](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/write/package-summary.html#class-summary)


SEARCH:
# Package org.apache.spark.sql.connector.write
* * *
package org.apache.spark.sql.connector.write
  * Related Packages
Package
Description
[org.apache.spark.sql.connector](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/package-summary.html)
[org.apache.spark.sql.connector.write.streaming](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/write/streaming/package-summary.html)
  * All Classes and InterfacesInterfacesEnum Classes
Class
Description
[BatchWrite](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/write/BatchWrite.html "interface in org.apache.spark.sql.connector.write")
An interface that defines how to write the data to data source for batch processing.
[DataWriter](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/write/DataWriter.html "interface in org.apache.spark.sql.connector.write")<T>
A data writer returned by [`DataWriterFactory.createWriter(int, long)`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/write/DataWriterFactory.html#createWriter\(int,long\)) and is responsible for writing data for an input RDD partition.
[DataWriterFactory](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/write/DataWriterFactory.html "interface in org.apache.spark.sql.connector.write")
A factory of [`DataWriter`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/write/DataWriter.html "interface in org.apache.spark.sql.connector.write") returned by [`BatchWrite.createBatchWriterFactory(PhysicalWriteInfo)`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/write/BatchWrite.html#createBatchWriterFactory\(org.apache.spark.sql.connector.write.PhysicalWriteInfo\)), which is responsible for creating and initializing the actual data writer at executor side.
[DeltaBatchWrite](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/write/DeltaBatchWrite.html "interface in org.apache.spark.sql.connector.write")
An interface that defines how to write a delta of rows during batch processing.
[DeltaWrite](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/write/DeltaWrite.html "interface in org.apache.spark.sql.connector.write")
A logical representation of a data source write that handles a delta of rows.
[DeltaWriteBuilder](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/write/DeltaWriteBuilder.html "interface in org.apache.spark.sql.connector.write")
An interface for building a [`DeltaWrite`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/write/DeltaWrite.html "interface in org.apache.spark.sql.connector.write").
[DeltaWriter](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/write/DeltaWriter.html "interface in org.apache.spark.sql.connector.write")<T>
A data writer returned by [`DeltaWriterFactory.createWriter(int, long)`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/write/DeltaWriterFactory.html#createWriter\(int,long\)) and is responsible for writing a delta of rows.
[DeltaWriterFactory](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/write/DeltaWriterFactory.html "interface in org.apache.spark.sql.connector.write")
A factory for creating [`DeltaWriter`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/write/DeltaWriter.html "interface in org.apache.spark.sql.connector.write")s returned by [`DeltaBatchWrite.createBatchWriterFactory(PhysicalWriteInfo)`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/write/DeltaBatchWrite.html#createBatchWriterFactory\(org.apache.spark.sql.connector.write.PhysicalWriteInfo\)), which is responsible for creating and initializing writers at the executor side.
[LogicalWriteInfo](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/write/LogicalWriteInfo.html "interface in org.apache.spark.sql.connector.write")
This interface contains logical write information that data sources can use when generating a [`WriteBuilder`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/write/WriteBuilder.html "interface in org.apache.spark.sql.connector.write").
[MergeSummary](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/write/MergeSummary.html "interface in org.apache.spark.sql.connector.write")
Provides an informational summary of the MERGE operation producing write.
[PhysicalWriteInfo](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/write/PhysicalWriteInfo.html "interface in org.apache.spark.sql.connector.write")
This interface contains physical write information that data sources can use when generating a [`DataWriterFactory`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/write/DataWriterFactory.html "interface in org.apache.spark.sql.connector.write") or a [`StreamingDataWriterFactory`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/write/streaming/StreamingDataWriterFactory.html "interface in org.apache.spark.sql.connector.write.streaming").
[RequiresDistributionAndOrdering](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/write/RequiresDistributionAndOrdering.html "interface in org.apache.spark.sql.connector.write")
A write that requires a specific distribution and ordering of data.
[RowLevelOperation](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/write/RowLevelOperation.html "interface in org.apache.spark.sql.connector.write")
A logical representation of a data source DELETE, UPDATE, or MERGE operation that requires rewriting data.
[RowLevelOperation.Command](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/write/RowLevelOperation.Command.html "enum class in org.apache.spark.sql.connector.write")
A row-level SQL command.
[RowLevelOperationBuilder](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/write/RowLevelOperationBuilder.html "interface in org.apache.spark.sql.connector.write")
An interface for building a [`RowLevelOperation`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/write/RowLevelOperation.html "interface in org.apache.spark.sql.connector.write").
[RowLevelOperationInfo](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/write/RowLevelOperationInfo.html "interface in org.apache.spark.sql.connector.write")
An interface with logical information for a row-level operation such as DELETE, UPDATE, MERGE.
[SupportsDelta](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/write/SupportsDelta.html "interface in org.apache.spark.sql.connector.write")
A mix-in interface for [`RowLevelOperation`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/write/RowLevelOperation.html "interface in org.apache.spark.sql.connector.write").
[SupportsDynamicOverwrite](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/write/SupportsDynamicOverwrite.html "interface in org.apache.spark.sql.connector.write")
Write builder trait for tables that support dynamic partition overwrite.
[SupportsOverwrite](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/write/SupportsOverwrite.html "interface in org.apache.spark.sql.connector.write")
Write builder trait for tables that support overwrite by filter.
[SupportsOverwriteV2](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/write/SupportsOverwriteV2.html "interface in org.apache.spark.sql.connector.write")
Write builder trait for tables that support overwrite by filter.
[SupportsTruncate](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/write/SupportsTruncate.html "interface in org.apache.spark.sql.connector.write")
Write builder trait for tables that support truncation.
[V1Write](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/write/V1Write.html "interface in org.apache.spark.sql.connector.write")
A logical write that should be executed using V1 InsertableRelation interface.
[Write](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/write/Write.html "interface in org.apache.spark.sql.connector.write")
A logical representation of a data source write.
[WriteBuilder](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/write/WriteBuilder.html "interface in org.apache.spark.sql.connector.write")
An interface for building the [`Write`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/write/Write.html "interface in org.apache.spark.sql.connector.write").
[WriterCommitMessage](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/write/WriterCommitMessage.html "interface in org.apache.spark.sql.connector.write")
A commit message returned by [`DataWriter.commit()`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/write/DataWriter.html#commit\(\)) and will be sent back to the driver side as the input parameter of [`BatchWrite.commit(WriterCommitMessage[])`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/write/BatchWrite.html#commit\(org.apache.spark.sql.connector.write.WriterCommitMessage%5B%5D\)) or [`StreamingWrite.commit(long, WriterCommitMessage[])`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/write/streaming/StreamingWrite.html#commit\(long,org.apache.spark.sql.connector.write.WriterCommitMessage%5B%5D\)).
[WriteSummary](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/write/WriteSummary.html "interface in org.apache.spark.sql.connector.write")
An informational summary of the operation producing write.


