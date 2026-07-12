[Skip navigation links](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/package-summary.html#skip-navbar-top "Skip navigation links")
  * [Overview](https://spark.apache.org/docs/latest/api/java/index.html)
  * Package
  * Class
  * [Deprecated](https://spark.apache.org/docs/latest/api/java/deprecated-list.html)
  * [Index](https://spark.apache.org/docs/latest/api/java/index-all.html)
  * [Help](https://spark.apache.org/docs/latest/api/java/help-doc.html#package)

  * Package:
  * Description |
  * [Related Packages](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/package-summary.html#related-package-summary) |
  * [Classes and Interfaces](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/package-summary.html#class-summary)

SEARCH:
# Package org.apache.spark.sql
* * *
package org.apache.spark.sql
  * Related Packages
Package
Description
[org.apache.spark](https://spark.apache.org/docs/latest/api/java/org/apache/spark/package-summary.html)
Core Spark classes in Scala.
[org.apache.spark.sql.catalog](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/catalog/package-summary.html)
[org.apache.spark.sql.columnar](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/columnar/package-summary.html)
[org.apache.spark.sql.connector](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/package-summary.html)
[org.apache.spark.sql.expressions](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/expressions/package-summary.html)
[org.apache.spark.sql.jdbc](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/jdbc/package-summary.html)
[org.apache.spark.sql.protobuf](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/protobuf/package-summary.html)
[org.apache.spark.sql.sources](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/sources/package-summary.html)
[org.apache.spark.sql.streaming](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/streaming/package-summary.html)
[org.apache.spark.sql.types](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/types/package-summary.html)
[org.apache.spark.sql.util](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/util/package-summary.html)
[org.apache.spark.sql.vectorized](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/vectorized/package-summary.html)
  * All Classes and InterfacesInterfacesClassesEnum ClassesExceptions
Class
Description
[AnalysisException](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/AnalysisException.html "class in org.apache.spark.sql")
Thrown when a query fails to analyze, usually because the query itself is invalid.
[Column](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/Column.html "class in org.apache.spark.sql")
A column that will be computed based on the data in a `DataFrame`.
[ColumnName](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/ColumnName.html "class in org.apache.spark.sql")
A convenient class used for constructing schema.
[CreateTableWriter](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/CreateTableWriter.html "interface in org.apache.spark.sql")<T>
Trait to restrict calls to create and replace operations.
[DataFrameNaFunctions](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/DataFrameNaFunctions.html "class in org.apache.spark.sql")
Functionality for working with missing data in `DataFrame`s.
[DataFrameReader](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/DataFrameReader.html "class in org.apache.spark.sql")
Interface used to load a [`Dataset`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/Dataset.html "class in org.apache.spark.sql") from external storage systems (e.g.
[DataFrameStatFunctions](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/DataFrameStatFunctions.html "class in org.apache.spark.sql")
Statistic functions for `DataFrame`s.
[DataFrameWriter](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/DataFrameWriter.html "class in org.apache.spark.sql")<T>
Interface used to write a [`Dataset`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/Dataset.html "class in org.apache.spark.sql") to external storage systems (e.g.
[DataFrameWriterV2](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/DataFrameWriterV2.html "class in org.apache.spark.sql")<T>
Interface used to write a [`Dataset`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/Dataset.html "class in org.apache.spark.sql") to external storage using the v2 API.
[Dataset](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/Dataset.html "class in org.apache.spark.sql")<T>
A Dataset is a strongly typed collection of domain-specific objects that can be transformed in parallel using functional or relational operations.
[DatasetHolder](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/DatasetHolder.html "class in org.apache.spark.sql")<T>
A container for a [`Dataset`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/Dataset.html "class in org.apache.spark.sql"), used for implicit conversions in Scala.
[Encoder](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/Encoder.html "interface in org.apache.spark.sql")<T>
Used to convert a JVM object of type `T` to and from the internal Spark SQL representation.
[EncoderImplicits](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/EncoderImplicits.html "interface in org.apache.spark.sql")
EncoderImplicits used to implicitly generate SQL Encoders.
[Encoders](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/Encoders.html "class in org.apache.spark.sql")
Methods for creating an [`Encoder`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/Encoder.html "interface in org.apache.spark.sql").
[ExperimentalMethods](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/ExperimentalMethods.html "class in org.apache.spark.sql")
Experimental Holder for experimental methods for the bravest.
[ExtendedExplainGenerator](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/ExtendedExplainGenerator.html "interface in org.apache.spark.sql")
A trait for a session extension to implement that provides addition explain plan information.
[ForeachWriter](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/ForeachWriter.html "class in org.apache.spark.sql")<T>
The abstract class for writing custom logic to process data generated by a query.
[functions](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/functions.html "class in org.apache.spark.sql")
Commonly used functions available for DataFrame operations.
[functions.partitioning$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/functions.partitioning$.html "class in org.apache.spark.sql")
[KeyValueGroupedDataset](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/KeyValueGroupedDataset.html "class in org.apache.spark.sql")<K,V>
A [`Dataset`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/Dataset.html "class in org.apache.spark.sql") has been logically grouped by a user specified grouping key.
[LowPrioritySQLImplicits](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/LowPrioritySQLImplicits.html "interface in org.apache.spark.sql")
Lower priority implicit methods for converting Scala objects into [`Dataset`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/Dataset.html "class in org.apache.spark.sql")s.
[MergeIntoWriter](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/MergeIntoWriter.html "class in org.apache.spark.sql")<T>
`MergeIntoWriter` provides methods to define and execute merge actions based on specified conditions.
[Observation](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/Observation.html "class in org.apache.spark.sql")
Helper class to simplify usage of `Dataset.observe(String, Column, Column*)`:
[RelationalGroupedDataset](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/RelationalGroupedDataset.html "class in org.apache.spark.sql")
A set of methods for aggregations on a `DataFrame`, created by [`groupBy`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/Dataset.html#groupBy\(org.apache.spark.sql.Column...\)), [`cube`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/Dataset.html#cube\(org.apache.spark.sql.Column...\)) or [`rollup`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/Dataset.html#rollup\(org.apache.spark.sql.Column...\)) (and also `pivot`).
[Row](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/Row.html "interface in org.apache.spark.sql")
Represents one row of output from a relational operator.
[RowFactory](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/RowFactory.html "class in org.apache.spark.sql")
A factory class used to construct [`Row`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/Row.html "interface in org.apache.spark.sql") objects.
[RuntimeConfig](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/RuntimeConfig.html "class in org.apache.spark.sql")
Runtime configuration interface for Spark.
[SaveMode](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/SaveMode.html "enum class in org.apache.spark.sql")
SaveMode is used to specify the expected behavior of saving a DataFrame to a data source.
[SparkSession](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/SparkSession.html "class in org.apache.spark.sql")
The entry point to programming Spark with the Dataset and DataFrame API.
[SparkSession.Builder](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/SparkSession.Builder.html "class in org.apache.spark.sql")
[SparkSessionExtensions](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/SparkSessionExtensions.html "class in org.apache.spark.sql")
Experimental Holder for injection points to the [`SparkSession`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/SparkSession.html "class in org.apache.spark.sql").
[SparkSessionExtensionsProvider](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/SparkSessionExtensionsProvider.html "interface in org.apache.spark.sql")
Base trait for implementations used by [`SparkSessionExtensions`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/SparkSessionExtensions.html "class in org.apache.spark.sql")
[SQLContext](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/SQLContext.html "class in org.apache.spark.sql")
The entry point for working with structured data (rows and columns) in Spark 1.x.
[SQLContextCompanion](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/SQLContextCompanion.html "interface in org.apache.spark.sql")
This SQLContext object contains utility functions to create a singleton SQLContext instance, or to get the created SQLContext instance.
[SQLImplicits](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/SQLImplicits.html "class in org.apache.spark.sql")
A collection of implicit methods for converting common Scala objects into [`Dataset`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/Dataset.html "class in org.apache.spark.sql")s.
[TableValuedFunction](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/TableValuedFunction.html "class in org.apache.spark.sql")
Interface for invoking table-valued functions in Spark SQL.
[TypedColumn](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/TypedColumn.html "class in org.apache.spark.sql")<T,U>
A [`Column`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/Column.html "class in org.apache.spark.sql") where an [`Encoder`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/Encoder.html "interface in org.apache.spark.sql") has been given for the expected input and return type.
[UDFRegistration](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/UDFRegistration.html "class in org.apache.spark.sql")
Functions for registering user-defined functions.
[WhenMatched](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/WhenMatched.html "class in org.apache.spark.sql")<T>
A class for defining actions to be taken when matching rows in a DataFrame during a merge operation.
[WhenNotMatched](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/WhenNotMatched.html "class in org.apache.spark.sql")<T>
A class for defining actions to be taken when no matching rows are found in a DataFrame during a merge operation.
[WhenNotMatchedBySource](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/WhenNotMatchedBySource.html "class in org.apache.spark.sql")<T>
A class for defining actions to be performed when there is no match by source during a merge operation in a MergeIntoWriter.
[WriteConfigMethods](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/WriteConfigMethods.html "interface in org.apache.spark.sql")<R>
Configuration methods common to create/replace operations and insert/overwrite operations.
