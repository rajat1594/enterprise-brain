[Skip navigation links](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/package-summary.html#skip-navbar-top "Skip navigation links")
  * [Overview](https://spark.apache.org/docs/latest/api/java/index.html)
  * Package
  * Class
  * [Deprecated](https://spark.apache.org/docs/latest/api/java/deprecated-list.html)
  * [Index](https://spark.apache.org/docs/latest/api/java/index-all.html)
  * [Help](https://spark.apache.org/docs/latest/api/java/help-doc.html#package)


  * Package: 
  * Description | 
  * [Related Packages](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/package-summary.html#related-package-summary) | 
  * [Classes and Interfaces](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/package-summary.html#class-summary)


SEARCH:
# Package org.apache.spark.sql.connector.read
* * *
package org.apache.spark.sql.connector.read
  * Related Packages
Package
Description
[org.apache.spark.sql.connector](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/package-summary.html)
[org.apache.spark.sql.connector.read.colstats](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/colstats/package-summary.html)
[org.apache.spark.sql.connector.read.partitioning](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/partitioning/package-summary.html)
[org.apache.spark.sql.connector.read.streaming](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/streaming/package-summary.html)
  * All Classes and InterfacesInterfacesEnum ClassesRecord Classes
Class
Description
[Batch](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/Batch.html "interface in org.apache.spark.sql.connector.read")
A physical representation of a data source scan for batch queries.
[HasPartitionKey](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/HasPartitionKey.html "interface in org.apache.spark.sql.connector.read")
A mix-in for input partitions whose records are clustered on the same set of partition keys (provided via [`SupportsReportPartitioning`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/SupportsReportPartitioning.html "interface in org.apache.spark.sql.connector.read"), see below).
[HasPartitionStatistics](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/HasPartitionStatistics.html "interface in org.apache.spark.sql.connector.read")
A mix-in for input partitions whose records are clustered on the same set of partition keys (provided via [`SupportsReportPartitioning`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/SupportsReportPartitioning.html "interface in org.apache.spark.sql.connector.read"), see below).
[InputPartition](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/InputPartition.html "interface in org.apache.spark.sql.connector.read")
A serializable representation of an input partition returned by [`Batch.planInputPartitions()`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/Batch.html#planInputPartitions\(\)) and the corresponding ones in streaming .
[LocalScan](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/LocalScan.html "interface in org.apache.spark.sql.connector.read")
A special Scan which will happen on Driver locally instead of Executors.
[PartitionReader](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/PartitionReader.html "interface in org.apache.spark.sql.connector.read")<T>
A partition reader returned by [`PartitionReaderFactory.createReader(InputPartition)`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/PartitionReaderFactory.html#createReader\(org.apache.spark.sql.connector.read.InputPartition\)) or [`PartitionReaderFactory.createColumnarReader(InputPartition)`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/PartitionReaderFactory.html#createColumnarReader\(org.apache.spark.sql.connector.read.InputPartition\)).
[PartitionReaderFactory](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/PartitionReaderFactory.html "interface in org.apache.spark.sql.connector.read")
A factory used to create [`PartitionReader`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/PartitionReader.html "interface in org.apache.spark.sql.connector.read") instances.
[Scan](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/Scan.html "interface in org.apache.spark.sql.connector.read")
A logical representation of a data source scan.
[Scan.ColumnarSupportMode](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/Scan.ColumnarSupportMode.html "enum class in org.apache.spark.sql.connector.read")
This enum defines how the columnar support for the partitions of the data source should be determined.
[ScanBuilder](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/ScanBuilder.html "interface in org.apache.spark.sql.connector.read")
An interface for building the [`Scan`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/Scan.html "interface in org.apache.spark.sql.connector.read").
[Statistics](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/Statistics.html "interface in org.apache.spark.sql.connector.read")
An interface to represent statistics for a data source, which is returned by [`SupportsReportStatistics.estimateStatistics()`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/SupportsReportStatistics.html#estimateStatistics\(\)).
[SupportsPushDownAggregates](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/SupportsPushDownAggregates.html "interface in org.apache.spark.sql.connector.read")
A mix-in interface for [`ScanBuilder`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/ScanBuilder.html "interface in org.apache.spark.sql.connector.read").
[SupportsPushDownFilters](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/SupportsPushDownFilters.html "interface in org.apache.spark.sql.connector.read")
A mix-in interface for [`ScanBuilder`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/ScanBuilder.html "interface in org.apache.spark.sql.connector.read").
[SupportsPushDownJoin](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/SupportsPushDownJoin.html "interface in org.apache.spark.sql.connector.read")
A mix-in interface for [`ScanBuilder`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/ScanBuilder.html "interface in org.apache.spark.sql.connector.read").
[SupportsPushDownJoin.ColumnWithAlias](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/SupportsPushDownJoin.ColumnWithAlias.html "class in org.apache.spark.sql.connector.read")
A helper class used when there are duplicated names coming from 2 sides of the join operator.
[SupportsPushDownLimit](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/SupportsPushDownLimit.html "interface in org.apache.spark.sql.connector.read")
A mix-in interface for [`ScanBuilder`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/ScanBuilder.html "interface in org.apache.spark.sql.connector.read").
[SupportsPushDownOffset](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/SupportsPushDownOffset.html "interface in org.apache.spark.sql.connector.read")
A mix-in interface for [`ScanBuilder`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/ScanBuilder.html "interface in org.apache.spark.sql.connector.read").
[SupportsPushDownRequiredColumns](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/SupportsPushDownRequiredColumns.html "interface in org.apache.spark.sql.connector.read")
A mix-in interface for [`ScanBuilder`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/ScanBuilder.html "interface in org.apache.spark.sql.connector.read").
[SupportsPushDownTableSample](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/SupportsPushDownTableSample.html "interface in org.apache.spark.sql.connector.read")
A mix-in interface for [`Scan`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/Scan.html "interface in org.apache.spark.sql.connector.read").
[SupportsPushDownTopN](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/SupportsPushDownTopN.html "interface in org.apache.spark.sql.connector.read")
A mix-in interface for [`ScanBuilder`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/ScanBuilder.html "interface in org.apache.spark.sql.connector.read").
[SupportsPushDownV2Filters](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/SupportsPushDownV2Filters.html "interface in org.apache.spark.sql.connector.read")
A mix-in interface for [`ScanBuilder`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/ScanBuilder.html "interface in org.apache.spark.sql.connector.read").
[SupportsPushDownVariantExtractions](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/SupportsPushDownVariantExtractions.html "interface in org.apache.spark.sql.connector.read")
A mix-in interface for [`ScanBuilder`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/ScanBuilder.html "interface in org.apache.spark.sql.connector.read").
[SupportsReportOrdering](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/SupportsReportOrdering.html "interface in org.apache.spark.sql.connector.read")
A mix in interface for [`Scan`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/Scan.html "interface in org.apache.spark.sql.connector.read").
[SupportsReportPartitioning](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/SupportsReportPartitioning.html "interface in org.apache.spark.sql.connector.read")
A mix in interface for [`Scan`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/Scan.html "interface in org.apache.spark.sql.connector.read").
[SupportsReportStatistics](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/SupportsReportStatistics.html "interface in org.apache.spark.sql.connector.read")
A mix in interface for [`Scan`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/Scan.html "interface in org.apache.spark.sql.connector.read").
[SupportsRuntimeFiltering](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/SupportsRuntimeFiltering.html "interface in org.apache.spark.sql.connector.read")
A mix-in interface for [`Scan`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/Scan.html "interface in org.apache.spark.sql.connector.read").
[SupportsRuntimeV2Filtering](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/SupportsRuntimeV2Filtering.html "interface in org.apache.spark.sql.connector.read")
A mix-in interface for [`Scan`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/Scan.html "interface in org.apache.spark.sql.connector.read").
[V1Scan](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/V1Scan.html "interface in org.apache.spark.sql.connector.read")
A trait that should be implemented by V1 DataSources that would like to leverage the DataSource V2 read code paths.
[VariantExtraction](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/read/VariantExtraction.html "interface in org.apache.spark.sql.connector.read")
Variant extraction information that describes a single field extraction from a variant column.


