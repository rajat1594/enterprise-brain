[Skip navigation links](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/streaming/package-summary.html#skip-navbar-top "Skip navigation links")
  * [Overview](https://spark.apache.org/docs/latest/api/java/index.html)
  * Package
  * Class
  * [Deprecated](https://spark.apache.org/docs/latest/api/java/deprecated-list.html)
  * [Index](https://spark.apache.org/docs/latest/api/java/index-all.html)
  * [Help](https://spark.apache.org/docs/latest/api/java/help-doc.html#package)


  * Package: 
  * Description | 
  * [Related Packages](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/streaming/package-summary.html#related-package-summary) | 
  * [Classes and Interfaces](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/streaming/package-summary.html#class-summary)


SEARCH:
# Package org.apache.spark.sql.connector.read.streaming
* * *
package org.apache.spark.sql.connector.read.streaming
  * Related Packages
Package
Description
[org.apache.spark.sql.connector.read](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/package-summary.html)
[org.apache.spark.sql.connector.read.colstats](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/colstats/package-summary.html)
[org.apache.spark.sql.connector.read.partitioning](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/partitioning/package-summary.html)
  * All Classes and InterfacesInterfacesClasses
Class
Description
[AcceptsLatestSeenOffset](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/streaming/AcceptsLatestSeenOffset.html "interface in org.apache.spark.sql.connector.read.streaming")
Indicates that the source accepts the latest seen offset, which requires streaming execution to provide the latest seen offset when restarting the streaming query from checkpoint.
[CompositeReadLimit](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/streaming/CompositeReadLimit.html "class in org.apache.spark.sql.connector.read.streaming")
/** Represents a [`ReadLimit`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/streaming/ReadLimit.html "interface in org.apache.spark.sql.connector.read.streaming") where the [`MicroBatchStream`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/streaming/MicroBatchStream.html "interface in org.apache.spark.sql.connector.read.streaming") should scan approximately given maximum number of rows with at least the given minimum number of rows.
[ContinuousPartitionReader](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/streaming/ContinuousPartitionReader.html "interface in org.apache.spark.sql.connector.read.streaming")<T>
A variation on [`PartitionReader`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/PartitionReader.html "interface in org.apache.spark.sql.connector.read") for use with continuous streaming processing.
[ContinuousPartitionReaderFactory](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/streaming/ContinuousPartitionReaderFactory.html "interface in org.apache.spark.sql.connector.read.streaming")
A variation on [`PartitionReaderFactory`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/PartitionReaderFactory.html "interface in org.apache.spark.sql.connector.read") that returns [`ContinuousPartitionReader`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/streaming/ContinuousPartitionReader.html "interface in org.apache.spark.sql.connector.read.streaming") instead of [`PartitionReader`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/PartitionReader.html "interface in org.apache.spark.sql.connector.read").
[ContinuousStream](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/streaming/ContinuousStream.html "interface in org.apache.spark.sql.connector.read.streaming")
A [`SparkDataStream`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/streaming/SparkDataStream.html "interface in org.apache.spark.sql.connector.read.streaming") for streaming queries with continuous mode.
[MicroBatchStream](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/streaming/MicroBatchStream.html "interface in org.apache.spark.sql.connector.read.streaming")
A [`SparkDataStream`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/streaming/SparkDataStream.html "interface in org.apache.spark.sql.connector.read.streaming") for streaming queries with micro-batch mode.
[Offset](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/streaming/Offset.html "class in org.apache.spark.sql.connector.read.streaming")
An abstract representation of progress through a [`MicroBatchStream`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/streaming/MicroBatchStream.html "interface in org.apache.spark.sql.connector.read.streaming") or [`ContinuousStream`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/streaming/ContinuousStream.html "interface in org.apache.spark.sql.connector.read.streaming").
[PartitionOffset](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/streaming/PartitionOffset.html "interface in org.apache.spark.sql.connector.read.streaming")
Used for per-partition offsets in continuous processing.
[ReadAllAvailable](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/streaming/ReadAllAvailable.html "class in org.apache.spark.sql.connector.read.streaming")
Represents a [`ReadLimit`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/streaming/ReadLimit.html "interface in org.apache.spark.sql.connector.read.streaming") where the [`MicroBatchStream`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/streaming/MicroBatchStream.html "interface in org.apache.spark.sql.connector.read.streaming") must scan all the data available at the streaming source.
[ReadLimit](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/streaming/ReadLimit.html "interface in org.apache.spark.sql.connector.read.streaming")
Interface representing limits on how much to read from a [`MicroBatchStream`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/streaming/MicroBatchStream.html "interface in org.apache.spark.sql.connector.read.streaming") when it implements [`SupportsAdmissionControl`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/streaming/SupportsAdmissionControl.html "interface in org.apache.spark.sql.connector.read.streaming").
[ReadMaxBytes](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/streaming/ReadMaxBytes.html "class in org.apache.spark.sql.connector.read.streaming")
Represents a [`ReadLimit`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/streaming/ReadLimit.html "interface in org.apache.spark.sql.connector.read.streaming") where the [`MicroBatchStream`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/streaming/MicroBatchStream.html "interface in org.apache.spark.sql.connector.read.streaming") should scan files which total size doesn't go beyond a given maximum total size.
[ReadMaxFiles](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/streaming/ReadMaxFiles.html "class in org.apache.spark.sql.connector.read.streaming")
Represents a [`ReadLimit`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/streaming/ReadLimit.html "interface in org.apache.spark.sql.connector.read.streaming") where the [`MicroBatchStream`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/streaming/MicroBatchStream.html "interface in org.apache.spark.sql.connector.read.streaming") should scan approximately the given maximum number of files.
[ReadMaxRows](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/streaming/ReadMaxRows.html "class in org.apache.spark.sql.connector.read.streaming")
Represents a [`ReadLimit`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/streaming/ReadLimit.html "interface in org.apache.spark.sql.connector.read.streaming") where the [`MicroBatchStream`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/streaming/MicroBatchStream.html "interface in org.apache.spark.sql.connector.read.streaming") should scan approximately the given maximum number of rows.
[ReadMinRows](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/streaming/ReadMinRows.html "class in org.apache.spark.sql.connector.read.streaming")
Represents a [`ReadLimit`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/streaming/ReadLimit.html "interface in org.apache.spark.sql.connector.read.streaming") where the [`MicroBatchStream`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/streaming/MicroBatchStream.html "interface in org.apache.spark.sql.connector.read.streaming") should scan approximately at least the given minimum number of rows.
[ReportsSinkMetrics](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/streaming/ReportsSinkMetrics.html "interface in org.apache.spark.sql.connector.read.streaming")
A mix-in interface for streaming sinks to signal that they can report metrics.
[ReportsSourceMetrics](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/streaming/ReportsSourceMetrics.html "interface in org.apache.spark.sql.connector.read.streaming")
A mix-in interface for [`SparkDataStream`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/streaming/SparkDataStream.html "interface in org.apache.spark.sql.connector.read.streaming") streaming sources to signal that they can report metrics.
[SparkDataStream](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/streaming/SparkDataStream.html "interface in org.apache.spark.sql.connector.read.streaming")
The base interface representing a readable data stream in a Spark streaming query.
[SupportsAdmissionControl](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/streaming/SupportsAdmissionControl.html "interface in org.apache.spark.sql.connector.read.streaming")
A mix-in interface for [`SparkDataStream`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/streaming/SparkDataStream.html "interface in org.apache.spark.sql.connector.read.streaming") streaming sources to signal that they can control the rate of data ingested into the system.
[SupportsRealTimeMode](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/streaming/SupportsRealTimeMode.html "interface in org.apache.spark.sql.connector.read.streaming")
A [`MicroBatchStream`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/streaming/MicroBatchStream.html "interface in org.apache.spark.sql.connector.read.streaming") for streaming queries with real time mode.
[SupportsRealTimeRead](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/streaming/SupportsRealTimeRead.html "interface in org.apache.spark.sql.connector.read.streaming")<T>
A variation on [`PartitionReader`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/PartitionReader.html "interface in org.apache.spark.sql.connector.read") for use with low latency streaming processing.
[SupportsRealTimeRead.RecordStatus](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/streaming/SupportsRealTimeRead.RecordStatus.html "class in org.apache.spark.sql.connector.read.streaming")
A class to represent the status of a record to be read as the return type of nextWithTimeout.
[SupportsTriggerAvailableNow](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/streaming/SupportsTriggerAvailableNow.html "interface in org.apache.spark.sql.connector.read.streaming")
An interface for streaming sources that supports running in Trigger.AvailableNow mode, which will process all the available data at the beginning of the query in (possibly) multiple batches.


