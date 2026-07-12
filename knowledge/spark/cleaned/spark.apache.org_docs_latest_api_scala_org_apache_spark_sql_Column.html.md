Spark 4.1.2 ScalaDoc < Back
 __ __
# Packages
  * [__](https://spark.apache.org/docs/latest/api/scala/index.html "Permalink") package [root](https://spark.apache.org/docs/latest/api/scala/index.html)

Definition Classes
    [root](https://spark.apache.org/docs/latest/api/scala/index.html "_root_")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/index.html "Permalink") package [org](https://spark.apache.org/docs/latest/api/scala/org/index.html)

Definition Classes
    [root](https://spark.apache.org/docs/latest/api/scala/index.html "_root_")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/index.html "Permalink") package [apache](https://spark.apache.org/docs/latest/api/scala/org/apache/index.html)

Definition Classes
    [org](https://spark.apache.org/docs/latest/api/scala/org/index.html "org")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "Permalink") package [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "Core Spark functionality.")
Core Spark functionality.
Core Spark functionality. [org.apache.spark.SparkContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkContext.html "org.apache.spark.SparkContext") serves as the main entry point to Spark, while [org.apache.spark.rdd.RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD") is the data type representing a distributed collection, and provides most parallel operations.
In addition, [org.apache.spark.rdd.PairRDDFunctions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/PairRDDFunctions.html "org.apache.spark.rdd.PairRDDFunctions") contains operations available only on RDDs of key-value pairs, such as `groupByKey` and `join`; [org.apache.spark.rdd.DoubleRDDFunctions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/DoubleRDDFunctions.html "org.apache.spark.rdd.DoubleRDDFunctions") contains operations available only on RDDs of Doubles; and [org.apache.spark.rdd.SequenceFileRDDFunctions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/SequenceFileRDDFunctions.html "org.apache.spark.rdd.SequenceFileRDDFunctions") contains operations available on RDDs that can be saved as SequenceFiles. These operations are automatically available on any RDD of the right type (e.g. RDD[(Int, Int)] through implicit conversions.
Java programmers should reference the [org.apache.spark.api.java](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/index.html "org.apache.spark.api.java") package for Spark programming APIs in Java.
Classes and methods marked with  Experimental are user-facing features which have not been officially adopted by the Spark project. These are subject to change or removal in minor releases.
Classes and methods marked with  Developer API are intended for advanced users want to extend Spark through lower level interfaces. These are subject to changes or removal in minor releases.

Definition Classes
    [apache](https://spark.apache.org/docs/latest/api/scala/org/apache/index.html "org.apache")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html "Permalink") package [sql](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html "Allows the execution of relational queries, including those expressed in SQL using Spark.")
Allows the execution of relational queries, including those expressed in SQL using Spark.
Allows the execution of relational queries, including those expressed in SQL using Spark.

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/api/index.html "Permalink") package [api](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/api/index.html "Contains API classes that are specific to a single language \(i.e.")
Contains API classes that are specific to a single language (i.e.
Contains API classes that are specific to a single language (i.e. Java).

Definition Classes
    [sql](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html "org.apache.spark.sql")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/index.html "Permalink") package [catalog](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/index.html)

Definition Classes
    [sql](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html "org.apache.spark.sql")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalyst/index.html "Permalink") package [catalyst](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalyst/index.html)

Definition Classes
    [sql](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html "org.apache.spark.sql")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/columnar/index.html "Permalink") package [columnar](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/columnar/index.html)

Definition Classes
    [sql](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html "org.apache.spark.sql")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/connector/index.html "Permalink") package [connector](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/connector/index.html)

Definition Classes
    [sql](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html "org.apache.spark.sql")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/expressions/index.html "Permalink") package [expressions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/expressions/index.html)

Definition Classes
    [sql](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html "org.apache.spark.sql")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/jdbc/index.html "Permalink") package [jdbc](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/jdbc/index.html)

Definition Classes
    [sql](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html "org.apache.spark.sql")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/protobuf/index.html "Permalink") package [protobuf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/protobuf/index.html)

Definition Classes
    [sql](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html "org.apache.spark.sql")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/sources/index.html "Permalink") package [sources](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/sources/index.html "A set of APIs for adding data sources to Spark SQL.")
A set of APIs for adding data sources to Spark SQL.
A set of APIs for adding data sources to Spark SQL.

Definition Classes
    [sql](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html "org.apache.spark.sql")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/index.html "Permalink") package [streaming](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/index.html)

Definition Classes
    [sql](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html "org.apache.spark.sql")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/types/index.html "Permalink") package [types](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/types/index.html "Contains a type system for attributes produced by relations, including complex types like structs, arrays and maps.")
Contains a type system for attributes produced by relations, including complex types like structs, arrays and maps.
Contains a type system for attributes produced by relations, including complex types like structs, arrays and maps.

Definition Classes
    [sql](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html "org.apache.spark.sql")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/util/index.html "Permalink") package [util](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/util/index.html)

Definition Classes
    [sql](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html "org.apache.spark.sql")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/vectorized/index.html "Permalink") package [vectorized](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/vectorized/index.html)

Definition Classes
    [sql](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html "org.apache.spark.sql")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/AnalysisException.html "Thrown when a query fails to analyze, usually because the query itself is invalid.")[AnalysisException](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/AnalysisException.html "Thrown when a query fails to analyze, usually because the query itself is invalid.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "A column that will be computed based on the data in a DataFrame.")[Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "A column that will be computed based on the data in a DataFrame.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/ColumnName.html "A convenient class used for constructing schema.")[ColumnName](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/ColumnName.html "A convenient class used for constructing schema.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/CreateTableWriter.html "Trait to restrict calls to create and replace operations.")[CreateTableWriter](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/CreateTableWriter.html "Trait to restrict calls to create and replace operations.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/DataFrameNaFunctions.html "Functionality for working with missing data in DataFrames.")[DataFrameNaFunctions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/DataFrameNaFunctions.html "Functionality for working with missing data in DataFrames.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/DataFrameReader.html "Interface used to load a Dataset from external storage systems \(e.g.")[DataFrameReader](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/DataFrameReader.html "Interface used to load a Dataset from external storage systems \(e.g.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/DataFrameStatFunctions.html "Statistic functions for DataFrames.")[DataFrameStatFunctions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/DataFrameStatFunctions.html "Statistic functions for DataFrames.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/DataFrameWriter.html "Interface used to write a org.apache.spark.sql.Dataset to external storage systems \(e.g.")[DataFrameWriter](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/DataFrameWriter.html "Interface used to write a org.apache.spark.sql.Dataset to external storage systems \(e.g.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/DataFrameWriterV2.html "Interface used to write a org.apache.spark.sql.Dataset to external storage using the v2 API.")[DataFrameWriterV2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/DataFrameWriterV2.html "Interface used to write a org.apache.spark.sql.Dataset to external storage using the v2 API.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "A Dataset is a strongly typed collection of domain-specific objects that can be transformed in parallel using functional or relational operations.")[Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "A Dataset is a strongly typed collection of domain-specific objects that can be transformed in parallel using functional or relational operations.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/DatasetHolder.html "A container for a org.apache.spark.sql.Dataset, used for implicit conversions in Scala.")[DatasetHolder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/DatasetHolder.html "A container for a org.apache.spark.sql.Dataset, used for implicit conversions in Scala.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "Used to convert a JVM object of type T to and from the internal Spark SQL representation.")[Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "Used to convert a JVM object of type T to and from the internal Spark SQL representation.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/EncoderImplicits.html "EncoderImplicits used to implicitly generate SQL Encoders.")[EncoderImplicits](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/EncoderImplicits.html "EncoderImplicits used to implicitly generate SQL Encoders.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoders$.html "Methods for creating an Encoder.")[Encoders](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoders$.html "Methods for creating an Encoder.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/ExperimentalMethods.html ":: Experimental :: Holder for experimental methods for the bravest.")[ExperimentalMethods](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/ExperimentalMethods.html ":: Experimental :: Holder for experimental methods for the bravest.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/ExtendedExplainGenerator.html "A trait for a session extension to implement that provides addition explain plan information.")[ExtendedExplainGenerator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/ExtendedExplainGenerator.html "A trait for a session extension to implement that provides addition explain plan information.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/ForeachWriter.html "The abstract class for writing custom logic to process data generated by a query.")[ForeachWriter](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/ForeachWriter.html "The abstract class for writing custom logic to process data generated by a query.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html "A Dataset has been logically grouped by a user specified grouping key.")[KeyValueGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html "A Dataset has been logically grouped by a user specified grouping key.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/LowPrioritySQLImplicits.html "Lower priority implicit methods for converting Scala objects into org.apache.spark.sql.Datasets.")[LowPrioritySQLImplicits](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/LowPrioritySQLImplicits.html "Lower priority implicit methods for converting Scala objects into org.apache.spark.sql.Datasets.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/MergeIntoWriter.html "MergeIntoWriter provides methods to define and execute merge actions based on specified conditions.")[MergeIntoWriter](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/MergeIntoWriter.html "MergeIntoWriter provides methods to define and execute merge actions based on specified conditions.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Observation$.html "\(Scala-specific\) Create instances of Observation via Scala apply.") [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Observation.html "Helper class to simplify usage of Dataset.observe\(String, Column, Column*\):")[Observation](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Observation.html "Helper class to simplify usage of Dataset.observe\(String, Column, Column*\):")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/RelationalGroupedDataset.html "A set of methods for aggregations on a DataFrame, created by groupBy, cube or rollup \(and also pivot\).")[RelationalGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/RelationalGroupedDataset.html "A set of methods for aggregations on a DataFrame, created by groupBy, cube or rollup \(and also pivot\).")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Row$.html) [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Row.html "Represents one row of output from a relational operator.")[Row](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Row.html "Represents one row of output from a relational operator.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/RowFactory.html "A factory class used to construct Row objects.")[RowFactory](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/RowFactory.html "A factory class used to construct Row objects.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/RuntimeConfig.html "Runtime configuration interface for Spark.")[RuntimeConfig](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/RuntimeConfig.html "Runtime configuration interface for Spark.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/SQLContext$.html) [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/SQLContext.html "The entry point for working with structured data \(rows and columns\) in Spark 1.x.")[SQLContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/SQLContext.html "The entry point for working with structured data \(rows and columns\) in Spark 1.x.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/SQLImplicits.html "A collection of implicit methods for converting common Scala objects into org.apache.spark.sql.Datasets.")[SQLImplicits](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/SQLImplicits.html "A collection of implicit methods for converting common Scala objects into org.apache.spark.sql.Datasets.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/SaveMode.html "SaveMode is used to specify the expected behavior of saving a DataFrame to a data source.")[SaveMode](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/SaveMode.html "SaveMode is used to specify the expected behavior of saving a DataFrame to a data source.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/SparkSession$.html) [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/SparkSession.html "The entry point to programming Spark with the Dataset and DataFrame API.")[SparkSession](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/SparkSession.html "The entry point to programming Spark with the Dataset and DataFrame API.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/SparkSessionExtensions.html ":: Experimental :: Holder for injection points to the SparkSession.")[SparkSessionExtensions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/SparkSessionExtensions.html ":: Experimental :: Holder for injection points to the SparkSession.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/SparkSessionExtensionsProvider.html "Base trait for implementations used by SparkSessionExtensions")[SparkSessionExtensionsProvider](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/SparkSessionExtensionsProvider.html "Base trait for implementations used by SparkSessionExtensions")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TableValuedFunction.html "Interface for invoking table-valued functions in Spark SQL.")[TableValuedFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TableValuedFunction.html "Interface for invoking table-valued functions in Spark SQL.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "A Column where an Encoder has been given for the expected input and return type.")[TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "A Column where an Encoder has been given for the expected input and return type.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/UDFRegistration.html "Functions for registering user-defined functions.")[UDFRegistration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/UDFRegistration.html "Functions for registering user-defined functions.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/WhenMatched.html "A class for defining actions to be taken when matching rows in a DataFrame during a merge operation.")[WhenMatched](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/WhenMatched.html "A class for defining actions to be taken when matching rows in a DataFrame during a merge operation.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/WhenNotMatched.html "A class for defining actions to be taken when no matching rows are found in a DataFrame during a merge operation.")[WhenNotMatched](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/WhenNotMatched.html "A class for defining actions to be taken when no matching rows are found in a DataFrame during a merge operation.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/WhenNotMatchedBySource.html "A class for defining actions to be performed when there is no match by source during a merge operation in a MergeIntoWriter.")[WhenNotMatchedBySource](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/WhenNotMatchedBySource.html "A class for defining actions to be performed when there is no match by source during a merge operation in a MergeIntoWriter.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/WriteConfigMethods.html "Configuration methods common to create/replace operations and insert/overwrite operations.")[WriteConfigMethods](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/WriteConfigMethods.html "Configuration methods common to create/replace operations and insert/overwrite operations.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/functions$.html "Commonly used functions available for DataFrame operations.")[functions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/functions$.html "Commonly used functions available for DataFrame operations.")

c
[org](https://spark.apache.org/docs/latest/api/scala/org/index.html "org").[apache](https://spark.apache.org/docs/latest/api/scala/org/apache/index.html "org.apache").[spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark").[sql](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html "org.apache.spark.sql")
# Column[ __](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "Permalink")
####  class Column extends Logging with TableValuedFunctionArgument
A column that will be computed based on the data in a `DataFrame`.
A new column can be constructed based on the input columns present in a DataFrame:

```
df("columnName")            // On a specific `df` DataFrame.
col("columnName")           // A generic column not yet associated with a DataFrame.
col("columnName.field")     // Extracting a struct field
col("`a.column.with.dots`") // Escape `.` in column names.
$"columnName"               // Scala short hand for a named column.
```

[Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column") objects can be composed to form complex expressions:

```
$"a" + 1
$"a" === $"b"
```

Annotations
     @Stable()

Source
    [Column.scala](https://github.com/apache/spark/tree/v4.1.2/sql/api/src/main/scala/org/apache/spark/sql/Column.scala)

Since

1.3.0
Linear Supertypes
TableValuedFunctionArgument, Logging, AnyRef, Any
Known Subclasses
[ColumnName](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/ColumnName.html "org.apache.spark.sql.ColumnName"), [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")
__ __
Ordering
  1. Grouped
  2. Alphabetic
  3. By Inheritance

Inherited

  1. Column
  2. TableValuedFunctionArgument
  3. Logging
  4. AnyRef
  5. Any

  1. Hide All
  2. Show All

Visibility
  1. Public
  2. Protected

### Instance Constructors
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#<init>\(name:String\):org.apache.spark.sql.Column "Permalink") new Column(name: String)
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#<init>\(node:org.apache.spark.sql.internal.ColumnNode\):org.apache.spark.sql.Column "Permalink") new Column(node: ColumnNode)

### Type Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#LogStringContextextendsAnyRef "Permalink") implicit  class LogStringContext extends AnyRef

Definition Classes
    Logging

### Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html###:Int "Permalink") final  def ##: Int

Definition Classes
    AnyRef → Any
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#%\(other:Any\):org.apache.spark.sql.Column "Permalink") def %(other: Any): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Modulo (a.k.a.
Modulo (a.k.a. remainder) expression.

Since

1.3.0
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#&&\(other:Any\):org.apache.spark.sql.Column "Permalink") def &&(other: Any): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Boolean AND.
Boolean AND.

```
// Scala: The following selects people that are in school and employed at the same time.
people.select( people("inSchool") && people("isEmployed") )

// Java:
people.select( people.col("inSchool").and(people.col("isEmployed")) );
```

Since

1.3.0
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#*\(other:Any\):org.apache.spark.sql.Column "Permalink") def *(other: Any): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Multiplication of this expression and another expression.
Multiplication of this expression and another expression.

```
// Scala: The following multiplies a person's height by their weight.
people.select( people("height") * people("weight") )

// Java:
people.select( people.col("height").multiply(people.col("weight")) );
```

Since

1.3.0
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#+\(other:Any\):org.apache.spark.sql.Column "Permalink") def +(other: Any): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Sum of this expression and another expression.
Sum of this expression and another expression.

```
// Scala: The following selects the sum of a person's height and weight.
people.select( people("height") + people("weight") )

// Java:
people.select( people.col("height").plus(people.col("weight")) );
```

Since

1.3.0
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#-\(other:Any\):org.apache.spark.sql.Column "Permalink") def -(other: Any): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Subtraction.
Subtraction. Subtract the other expression from this expression.

```
// Scala: The following selects the difference between people's height and their weight.
people.select( people("height") - people("weight") )

// Java:
people.select( people.col("height").minus(people.col("weight")) );
```

Since

1.3.0
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#/\(other:Any\):org.apache.spark.sql.Column "Permalink") def /(other: Any): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Division this expression by another expression.
Division this expression by another expression.

```
// Scala: The following divides a person's height by their weight.
people.select( people("height") / people("weight") )

// Java:
people.select( people.col("height").divide(people.col("weight")) );
```

Since

1.3.0
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#<\(other:Any\):org.apache.spark.sql.Column "Permalink") def <(other: Any): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Less than.
Less than.

```
// Scala: The following selects people younger than 21.
people.select( people("age") < 21 )

// Java:
people.select( people.col("age").lt(21) );
```

Since

1.3.0
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#<=\(other:Any\):org.apache.spark.sql.Column "Permalink") def <=(other: Any): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Less than or equal to.
Less than or equal to.

```
// Scala: The following selects people age 21 or younger than 21.
people.select( people("age") <= 21 )

// Java:
people.select( people.col("age").leq(21) );
```

Since

1.3.0
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#<=>\(other:Any\):org.apache.spark.sql.Column "Permalink") def <=>(other: Any): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Equality test that is safe for null values.
Equality test that is safe for null values.

Since

1.3.0
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#=!=\(other:Any\):org.apache.spark.sql.Column "Permalink") def =!=(other: Any): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Inequality test.
Inequality test.

```
// Scala:
df.select( df("colA") =!= df("colB") )
df.select( !(df("colA") === df("colB")) )

// Java:
import static org.apache.spark.sql.functions.*;
df.filter( col("colA").notEqual(col("colB")) );
```

Since

2.0.0
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#===\(other:Any\):org.apache.spark.sql.Column "Permalink") def ===(other: Any): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Equality test.
Equality test.

```
// Scala:
df.filter( df("colA") === df("colB") )

// Java
import static org.apache.spark.sql.functions.*;
df.filter( col("colA").equalTo(col("colB")) );
```

Since

1.3.0
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#>\(other:Any\):org.apache.spark.sql.Column "Permalink") def >(other: Any): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Greater than.
Greater than.

```
// Scala: The following selects people older than 21.
people.select( people("age") > 21 )

// Java:
import static org.apache.spark.sql.functions.*;
people.select( people.col("age").gt(21) );
```

Since

1.3.0
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#>=\(other:Any\):org.apache.spark.sql.Column "Permalink") def >=(other: Any): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Greater than or equal to an expression.
Greater than or equal to an expression.

```
// Scala: The following selects people age 21 or older than 21.
people.select( people("age") >= 21 )

// Java:
people.select( people.col("age").geq(21) )
```

Since

1.3.0
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#MDC\(key:org.apache.spark.internal.LogKey,value:Any\):org.apache.spark.internal.MDC "Permalink") def MDC(key: LogKey, value: Any): MDC

Attributes
    protected

Definition Classes
    Logging
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#alias\(alias:String\):org.apache.spark.sql.Column "Permalink") def alias(alias: String): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Gives the column an alias.
Gives the column an alias. Same as `as`.

```
// Renames colA to colB in select output.
df.select($"colA".alias("colB"))
```

Since

1.4.0
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#and\(other:org.apache.spark.sql.Column\):org.apache.spark.sql.Column "Permalink") def and(other: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Boolean AND.
Boolean AND.

```
// Scala: The following selects people that are in school and employed at the same time.
people.select( people("inSchool") && people("isEmployed") )

// Java:
people.select( people.col("inSchool").and(people.col("isEmployed")) );
```

Since

1.3.0
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#apply\(extraction:Any\):org.apache.spark.sql.Column "Permalink") def apply(extraction: Any): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Extracts a value or values from a complex type.
Extracts a value or values from a complex type. The following types of extraction are supported:
     * Given an Array, an integer ordinal can be used to retrieve a single value.
     * Given a Map, a key of the correct type can be used to retrieve an individual value.
     * Given a Struct, a string fieldName can be used to extract that field.
     * Given an Array of Structs, a string fieldName can be used to extract filed of every struct in that array, and return an Array of fields.

Since

1.4.0
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#as\(alias:String,metadata:org.apache.spark.sql.types.Metadata\):org.apache.spark.sql.Column "Permalink") def as(alias: String, metadata: [Metadata](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/types/Metadata.html "org.apache.spark.sql.types.Metadata")): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Gives the column an alias with metadata.
Gives the column an alias with metadata.

```
val metadata: Metadata = ...
df.select($"colA".as("colB", metadata))
```

Since

1.3.0
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#as\(alias:Symbol\):org.apache.spark.sql.Column "Permalink") def as(alias: Symbol): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Gives the column an alias.
Gives the column an alias.

```
// Renames colA to colB in select output.
df.select($"colA".as("colB"))
```

If the current column has metadata associated with it, this metadata will be propagated to the new column. If this not desired, use the API `as(alias: String, metadata: Metadata)` with explicit metadata.

Since

1.3.0
  23. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#as\(aliases:Array\[String\]\):org.apache.spark.sql.Column "Permalink") def as(aliases: Array[String]): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Assigns the given aliases to the results of a table generating function.
Assigns the given aliases to the results of a table generating function.

```
// Renames colA to colB in select output.
df.select(explode($"myMap").as("key" :: "value" :: Nil))
```

Since

1.4.0
  24. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#as\(aliases:Seq\[String\]\):org.apache.spark.sql.Column "Permalink") def as(aliases: Seq[String]): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
(Scala-specific) Assigns the given aliases to the results of a table generating function.
(Scala-specific) Assigns the given aliases to the results of a table generating function.

```
// Renames colA to colB in select output.
df.select(explode($"myMap").as("key" :: "value" :: Nil))
```

Since

1.4.0
  25. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#as\(alias:String\):org.apache.spark.sql.Column "Permalink") def as(alias: String): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Gives the column an alias.
Gives the column an alias.

```
// Renames colA to colB in select output.
df.select($"colA".as("colB"))
```

If the current column has metadata associated with it, this metadata will be propagated to the new column. If this not desired, use the API `as(alias: String, metadata: Metadata)` with explicit metadata.

Since

1.3.0
  26. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#as\[U\]\(implicitevidence$1:org.apache.spark.sql.Encoder\[U\]\):org.apache.spark.sql.TypedColumn\[Any,U\] "Permalink") def as[U](implicit arg0: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[U]): [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[Any, U]
Provides a type hint about the expected return value of this column.
Provides a type hint about the expected return value of this column. This information can be used by operations such as `select` on a [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") to automatically convert the results into the correct JVM types.

Since

1.6.0
  27. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0

Definition Classes
    Any
  28. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#asc:org.apache.spark.sql.Column "Permalink") def asc: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Returns a sort expression based on ascending order of the column.
Returns a sort expression based on ascending order of the column.

```
// Scala: sort a DataFrame by age column in ascending order.
df.sort(df("age").asc)

// Java
df.sort(df.col("age").asc());
```

Since

1.3.0
  29. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#asc_nulls_first:org.apache.spark.sql.Column "Permalink") def asc_nulls_first: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Returns a sort expression based on ascending order of the column, and null values return before non-null values.
Returns a sort expression based on ascending order of the column, and null values return before non-null values.

```
// Scala: sort a DataFrame by age column in ascending order and null values appearing first.
df.sort(df("age").asc_nulls_first)

// Java
df.sort(df.col("age").asc_nulls_first());
```

Since

2.1.0
  30. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#asc_nulls_last:org.apache.spark.sql.Column "Permalink") def asc_nulls_last: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Returns a sort expression based on ascending order of the column, and null values appear after non-null values.
Returns a sort expression based on ascending order of the column, and null values appear after non-null values.

```
// Scala: sort a DataFrame by age column in ascending order and null values appearing last.
df.sort(df("age").asc_nulls_last)

// Java
df.sort(df.col("age").asc_nulls_last());
```

Since

2.1.0
  31. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#between\(lowerBound:Any,upperBound:Any\):org.apache.spark.sql.Column "Permalink") def between(lowerBound: Any, upperBound: Any): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
True if the current column is between the lower bound and upper bound, inclusive.
True if the current column is between the lower bound and upper bound, inclusive.

Since

1.4.0
  32. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#bitwiseAND\(other:Any\):org.apache.spark.sql.Column "Permalink") def bitwiseAND(other: Any): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Compute bitwise AND of this expression with another expression.
Compute bitwise AND of this expression with another expression.

```
df.select($"colA".bitwiseAND($"colB"))
```

Since

1.4.0
  33. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#bitwiseOR\(other:Any\):org.apache.spark.sql.Column "Permalink") def bitwiseOR(other: Any): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Compute bitwise OR of this expression with another expression.
Compute bitwise OR of this expression with another expression.

```
df.select($"colA".bitwiseOR($"colB"))
```

Since

1.4.0
  34. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#bitwiseXOR\(other:Any\):org.apache.spark.sql.Column "Permalink") def bitwiseXOR(other: Any): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Compute bitwise XOR of this expression with another expression.
Compute bitwise XOR of this expression with another expression.

```
df.select($"colA".bitwiseXOR($"colB"))
```

Since

1.4.0
  35. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#cast\(to:String\):org.apache.spark.sql.Column "Permalink") def cast(to: String): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Casts the column to a different data type, using the canonical string representation of the type.
Casts the column to a different data type, using the canonical string representation of the type. The supported types are: `string`, `boolean`, `byte`, `short`, `int`, `long`, `float`, `double`, `decimal`, `date`, `timestamp`.

```
// Casts colA to integer.
df.select(df("colA").cast("int"))
```

Since

1.3.0
  36. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#cast\(to:org.apache.spark.sql.types.DataType\):org.apache.spark.sql.Column "Permalink") def cast(to: [DataType](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/types/DataType.html "org.apache.spark.sql.types.DataType")): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Casts the column to a different data type.
Casts the column to a different data type.

```
// Casts colA to IntegerType.
import org.apache.spark.sql.types.IntegerType
df.select(df("colA").cast(IntegerType))

// equivalent to
df.select(df("colA").cast("int"))
```

Since

1.3.0
  37. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#clone\(\):Object "Permalink") def clone(): AnyRef

Attributes
    protected[lang]

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  38. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#contains\(other:Any\):org.apache.spark.sql.Column "Permalink") def contains(other: Any): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Contains the other element.
Contains the other element. Returns a boolean column based on a string match.

Since

1.3.0
  39. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#desc:org.apache.spark.sql.Column "Permalink") def desc: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Returns a sort expression based on the descending order of the column.
Returns a sort expression based on the descending order of the column.

```
// Scala
df.sort(df("age").desc)

// Java
df.sort(df.col("age").desc());
```

Since

1.3.0
  40. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#desc_nulls_first:org.apache.spark.sql.Column "Permalink") def desc_nulls_first: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Returns a sort expression based on the descending order of the column, and null values appear before non-null values.
Returns a sort expression based on the descending order of the column, and null values appear before non-null values.

```
// Scala: sort a DataFrame by age column in descending order and null values appearing first.
df.sort(df("age").desc_nulls_first)

// Java
df.sort(df.col("age").desc_nulls_first());
```

Since

2.1.0
  41. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#desc_nulls_last:org.apache.spark.sql.Column "Permalink") def desc_nulls_last: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Returns a sort expression based on the descending order of the column, and null values appear after non-null values.
Returns a sort expression based on the descending order of the column, and null values appear after non-null values.

```
// Scala: sort a DataFrame by age column in descending order and null values appearing last.
df.sort(df("age").desc_nulls_last)

// Java
df.sort(df.col("age").desc_nulls_last());
```

Since

2.1.0
  42. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#divide\(other:Any\):org.apache.spark.sql.Column "Permalink") def divide(other: Any): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Division this expression by another expression.
Division this expression by another expression.

```
// Scala: The following divides a person's height by their weight.
people.select( people("height") / people("weight") )

// Java:
people.select( people.col("height").divide(people.col("weight")) );
```

Since

1.3.0
  43. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#dropFields\(fieldNames:String*\):org.apache.spark.sql.Column "Permalink") def dropFields(fieldNames: String*): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
An expression that drops fields in `StructType` by name.
An expression that drops fields in `StructType` by name. This is a no-op if schema doesn't contain field name(s).

```
val df = sql("SELECT named_struct('a', 1, 'b', 2) struct_col")
df.select($"struct_col".dropFields("b"))
// result: {"a":1}

val df = sql("SELECT named_struct('a', 1, 'b', 2) struct_col")
df.select($"struct_col".dropFields("c"))
// result: {"a":1,"b":2}

val df = sql("SELECT named_struct('a', 1, 'b', 2, 'c', 3) struct_col")
df.select($"struct_col".dropFields("b", "c"))
// result: {"a":1}

val df = sql("SELECT named_struct('a', 1, 'b', 2) struct_col")
df.select($"struct_col".dropFields("a", "b"))
// result: org.apache.spark.sql.AnalysisException: [DATATYPE_MISMATCH.CANNOT_DROP_ALL_FIELDS] Cannot resolve "update_fields(struct_col, dropfield(), dropfield())" due to data type mismatch: Cannot drop all fields in struct.;

val df = sql("SELECT CAST(NULL AS struct<a:int,b:int>) struct_col")
df.select($"struct_col".dropFields("b"))
// result: null of type struct<a:int>

val df = sql("SELECT named_struct('a', 1, 'b', 2, 'b', 3) struct_col")
df.select($"struct_col".dropFields("b"))
// result: {"a":1}

val df = sql("SELECT named_struct('a', named_struct('a', 1, 'b', 2)) struct_col")
df.select($"struct_col".dropFields("a.b"))
// result: {"a":{"a":1}}

val df = sql("SELECT named_struct('a', named_struct('b', 1), 'a', named_struct('c', 2)) struct_col")
df.select($"struct_col".dropFields("a.c"))
// result: org.apache.spark.sql.AnalysisException: Ambiguous reference to fields
```

This method supports dropping multiple nested fields directly e.g.

```
val df = sql("SELECT named_struct('a', named_struct('a', 1, 'b', 2)) struct_col")
df.select($"struct_col".dropFields("a.b", "a.c"))
// result: {"a":{"a":1}}
```

However, if you are going to drop multiple nested fields, it is more optimal to extract out the nested struct before dropping multiple fields from it e.g.

```
val df = sql("SELECT named_struct('a', named_struct('a', 1, 'b', 2)) struct_col")
df.select($"struct_col".withField("a", $"struct_col.a".dropFields("b", "c")))
// result: {"a":{"a":1}}
```

Since

3.1.0
  44. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#endsWith\(literal:String\):org.apache.spark.sql.Column "Permalink") def endsWith(literal: String): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
String ends with another string literal.
String ends with another string literal. Returns a boolean column based on a string match.

Since

1.3.0
  45. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#endsWith\(other:org.apache.spark.sql.Column\):org.apache.spark.sql.Column "Permalink") def endsWith(other: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
String ends with.
String ends with. Returns a boolean column based on a string match.

Since

1.3.0
  46. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  47. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#eqNullSafe\(other:Any\):org.apache.spark.sql.Column "Permalink") def eqNullSafe(other: Any): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Equality test that is safe for null values.
Equality test that is safe for null values.

Since

1.3.0
  48. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#equalTo\(other:Any\):org.apache.spark.sql.Column "Permalink") def equalTo(other: Any): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Equality test.
Equality test.

```
// Scala:
df.filter( df("colA") === df("colB") )

// Java
import static org.apache.spark.sql.functions.*;
df.filter( col("colA").equalTo(col("colB")) );
```

Since

1.3.0
  49. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#equals\(that:Any\):Boolean "Permalink") def equals(that: Any): Boolean

Definition Classes
     [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column") → AnyRef → Any
  50. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#explain\(extended:Boolean\):Unit "Permalink") def explain(extended: Boolean): Unit
Prints the expression to the console for debugging purposes.
Prints the expression to the console for debugging purposes.

Since

1.3.0
  51. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#geq\(other:Any\):org.apache.spark.sql.Column "Permalink") def geq(other: Any): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Greater than or equal to an expression.
Greater than or equal to an expression.

```
// Scala: The following selects people age 21 or older than 21.
people.select( people("age") >= 21 )

// Java:
people.select( people.col("age").geq(21) )
```

Since

1.3.0
  52. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef]

Definition Classes
    AnyRef → Any

Annotations
     @IntrinsicCandidate() @native()
  53. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#getField\(fieldName:String\):org.apache.spark.sql.Column "Permalink") def getField(fieldName: String): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
An expression that gets a field by name in a `StructType`.
An expression that gets a field by name in a `StructType`.

Since

1.3.0
  54. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#getItem\(key:Any\):org.apache.spark.sql.Column "Permalink") def getItem(key: Any): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
An expression that gets an item at position `ordinal` out of an array, or gets a value by key `key` in a `MapType`.
An expression that gets an item at position `ordinal` out of an array, or gets a value by key `key` in a `MapType`.

Since

1.3.0
  55. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#gt\(other:Any\):org.apache.spark.sql.Column "Permalink") def gt(other: Any): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Greater than.
Greater than.

```
// Scala: The following selects people older than 21.
people.select( people("age") > lit(21) )

// Java:
import static org.apache.spark.sql.functions.*;
people.select( people.col("age").gt(21) );
```

Since

1.3.0
  56. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#hashCode\(\):Int "Permalink") def hashCode(): Int

Definition Classes
     [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column") → AnyRef → Any
  57. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#ilike\(literal:String\):org.apache.spark.sql.Column "Permalink") def ilike(literal: String): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
SQL ILIKE expression (case insensitive LIKE).
SQL ILIKE expression (case insensitive LIKE).

Since

3.3.0
  58. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#initializeLogIfNecessary\(isInterpreter:Boolean,silent:Boolean\):Boolean "Permalink") def initializeLogIfNecessary(isInterpreter: Boolean, silent: Boolean): Boolean

Attributes
    protected

Definition Classes
    Logging
  59. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#initializeLogIfNecessary\(isInterpreter:Boolean\):Unit "Permalink") def initializeLogIfNecessary(isInterpreter: Boolean): Unit

Attributes
    protected

Definition Classes
    Logging
  60. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#isInCollection\(values:Iterable\[_\]\):org.apache.spark.sql.Column "Permalink") def isInCollection(values: [Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html#java.lang.Iterable "java.lang.Iterable")[_]): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
A boolean expression that is evaluated to true if the value of this expression is contained by the provided collection.
A boolean expression that is evaluated to true if the value of this expression is contained by the provided collection.
Note: Since the type of the elements in the collection are inferred only during the run time, the elements will be "up-casted" to the most common type for comparison. For eg: 1) In the case of "Int vs String", the "Int" will be up-casted to "String" and the comparison will look like "String vs String". 2) In the case of "Float vs Double", the "Float" will be up-casted to "Double" and the comparison will look like "Double vs Double"

Since

2.4.0
  61. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#isInCollection\(values:Iterable\[_\]\):org.apache.spark.sql.Column "Permalink") def isInCollection(values: Iterable[_]): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
A boolean expression that is evaluated to true if the value of this expression is contained by the provided collection.
A boolean expression that is evaluated to true if the value of this expression is contained by the provided collection.
Note: Since the type of the elements in the collection are inferred only during the run time, the elements will be "up-casted" to the most common type for comparison. For eg: 1) In the case of "Int vs String", the "Int" will be up-casted to "String" and the comparison will look like "String vs String". 2) In the case of "Float vs Double", the "Float" will be up-casted to "Double" and the comparison will look like "Double vs Double"

Since

2.4.0
  62. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean

Definition Classes
    Any
  63. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#isNaN:org.apache.spark.sql.Column "Permalink") def isNaN: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
True if the current expression is NaN.
True if the current expression is NaN.

Since

1.5.0
  64. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#isNotNull:org.apache.spark.sql.Column "Permalink") def isNotNull: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
True if the current expression is NOT null.
True if the current expression is NOT null.

Since

1.3.0
  65. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#isNull:org.apache.spark.sql.Column "Permalink") def isNull: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
True if the current expression is null.
True if the current expression is null.

Since

1.3.0
  66. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#isTraceEnabled\(\):Boolean "Permalink") def isTraceEnabled(): Boolean

Attributes
    protected

Definition Classes
    Logging
  67. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#isin\(ds:org.apache.spark.sql.Dataset\[_\]\):org.apache.spark.sql.Column "Permalink") def isin(ds: [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[_]): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
A boolean expression that is evaluated to true if the value of this expression is contained by the provided Dataset/DataFrame.
A boolean expression that is evaluated to true if the value of this expression is contained by the provided Dataset/DataFrame.

Since

4.1.0
  68. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#isin\(list:Any*\):org.apache.spark.sql.Column "Permalink") def isin(list: Any*): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
A boolean expression that is evaluated to true if the value of this expression is contained by the evaluated values of the arguments.
A boolean expression that is evaluated to true if the value of this expression is contained by the evaluated values of the arguments.
Note: Since the type of the elements in the list are inferred only during the run time, the elements will be "up-casted" to the most common type for comparison. For eg: 1) In the case of "Int vs String", the "Int" will be up-casted to "String" and the comparison will look like "String vs String". 2) In the case of "Float vs Double", the "Float" will be up-casted to "Double" and the comparison will look like "Double vs Double"

Annotations
     @varargs()

Since

1.5.0
  69. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#leq\(other:Any\):org.apache.spark.sql.Column "Permalink") def leq(other: Any): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Less than or equal to.
Less than or equal to.

```
// Scala: The following selects people age 21 or younger than 21.
people.select( people("age") <= 21 )

// Java:
people.select( people.col("age").leq(21) );
```

Since

1.3.0
  70. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#like\(literal:String\):org.apache.spark.sql.Column "Permalink") def like(literal: String): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
SQL like expression.
SQL like expression. Returns a boolean column based on a SQL LIKE match.

Since

1.3.0
  71. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#log:org.slf4j.Logger "Permalink") def log: Logger

Attributes
    protected

Definition Classes
    Logging
  72. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#logBasedOnLevel\(level:org.slf4j.event.Level\)\(f:=>org.apache.spark.internal.MessageWithContext\):Unit "Permalink") def logBasedOnLevel(level: Level)(f: => MessageWithContext): Unit

Attributes
    protected

Definition Classes
    Logging
  73. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#logDebug\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logDebug(msg: => String, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  74. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#logDebug\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logDebug(entry: LogEntry, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  75. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#logDebug\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logDebug(entry: LogEntry): Unit

Attributes
    protected

Definition Classes
    Logging
  76. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#logDebug\(msg:=>String\):Unit "Permalink") def logDebug(msg: => String): Unit

Attributes
    protected

Definition Classes
    Logging
  77. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#logError\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logError(msg: => String, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  78. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#logError\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logError(entry: LogEntry, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  79. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#logError\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logError(entry: LogEntry): Unit

Attributes
    protected

Definition Classes
    Logging
  80. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#logError\(msg:=>String\):Unit "Permalink") def logError(msg: => String): Unit

Attributes
    protected

Definition Classes
    Logging
  81. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#logInfo\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logInfo(msg: => String, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  82. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#logInfo\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logInfo(entry: LogEntry, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  83. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#logInfo\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logInfo(entry: LogEntry): Unit

Attributes
    protected

Definition Classes
    Logging
  84. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#logInfo\(msg:=>String\):Unit "Permalink") def logInfo(msg: => String): Unit

Attributes
    protected

Definition Classes
    Logging
  85. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#logName:String "Permalink") def logName: [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String")

Attributes
    protected

Definition Classes
    Logging
  86. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#logTrace\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logTrace(msg: => String, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  87. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#logTrace\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logTrace(entry: LogEntry, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  88. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#logTrace\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logTrace(entry: LogEntry): Unit

Attributes
    protected

Definition Classes
    Logging
  89. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#logTrace\(msg:=>String\):Unit "Permalink") def logTrace(msg: => String): Unit

Attributes
    protected

Definition Classes
    Logging
  90. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#logWarning\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logWarning(msg: => String, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  91. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#logWarning\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logWarning(entry: LogEntry, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  92. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#logWarning\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logWarning(entry: LogEntry): Unit

Attributes
    protected

Definition Classes
    Logging
  93. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#logWarning\(msg:=>String\):Unit "Permalink") def logWarning(msg: => String): Unit

Attributes
    protected

Definition Classes
    Logging
  94. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#lt\(other:Any\):org.apache.spark.sql.Column "Permalink") def lt(other: Any): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Less than.
Less than.

```
// Scala: The following selects people younger than 21.
people.select( people("age") < 21 )

// Java:
people.select( people.col("age").lt(21) );
```

Since

1.3.0
  95. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#minus\(other:Any\):org.apache.spark.sql.Column "Permalink") def minus(other: Any): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Subtraction.
Subtraction. Subtract the other expression from this expression.

```
// Scala: The following selects the difference between people's height and their weight.
people.select( people("height") - people("weight") )

// Java:
people.select( people.col("height").minus(people.col("weight")) );
```

Since

1.3.0
  96. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#mod\(other:Any\):org.apache.spark.sql.Column "Permalink") def mod(other: Any): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Modulo (a.k.a.
Modulo (a.k.a. remainder) expression.

Since

1.3.0
  97. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#multiply\(other:Any\):org.apache.spark.sql.Column "Permalink") def multiply(other: Any): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Multiplication of this expression and another expression.
Multiplication of this expression and another expression.

```
// Scala: The following multiplies a person's height by their weight.
people.select( people("height") * people("weight") )

// Java:
people.select( people.col("height").multiply(people.col("weight")) );
```

Since

1.3.0
  98. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#name\(alias:String\):org.apache.spark.sql.Column "Permalink") def name(alias: String): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Gives the column a name (alias).
Gives the column a name (alias).

```
// Renames colA to colB in select output.
df.select($"colA".name("colB"))
```

If the current column has metadata associated with it, this metadata will be propagated to the new column. If this not desired, use the API `as(alias: String, metadata: Metadata)` with explicit metadata.

Since

2.0.0
  99. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  100. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#node:org.apache.spark.sql.internal.ColumnNode "Permalink") val node: ColumnNode
  101. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#notEqual\(other:Any\):org.apache.spark.sql.Column "Permalink") def notEqual(other: Any): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Inequality test.
Inequality test.

```
// Scala:
df.select( df("colA") !== df("colB") )
df.select( !(df("colA") === df("colB")) )

// Java:
import static org.apache.spark.sql.functions.*;
df.filter( col("colA").notEqual(col("colB")) );
```

Since

1.3.0
  102. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#notify\(\):Unit "Permalink") final  def notify(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  103. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  104. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#or\(other:org.apache.spark.sql.Column\):org.apache.spark.sql.Column "Permalink") def or(other: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Boolean OR.
Boolean OR.

```
// Scala: The following selects people that are in school or employed.
people.filter( people("inSchool") || people("isEmployed") )

// Java:
people.filter( people.col("inSchool").or(people.col("isEmployed")) );
```

Since

1.3.0
  105. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#otherwise\(value:Any\):org.apache.spark.sql.Column "Permalink") def otherwise(value: Any): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Evaluates a list of conditions and returns one of multiple possible result expressions.
Evaluates a list of conditions and returns one of multiple possible result expressions. If otherwise is not defined at the end, null is returned for unmatched conditions.

```
// Example: encoding gender string column into integer.

// Scala:
people.select(when(people("gender") === "male", 0)
  .when(people("gender") === "female", 1)
  .otherwise(2))

// Java:
people.select(when(col("gender").equalTo("male"), 0)
  .when(col("gender").equalTo("female"), 1)
  .otherwise(2))
```

Since

1.4.0
  106. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#outer\(\):org.apache.spark.sql.Column "Permalink") def outer(): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Mark this column as an outer column if its expression refers to columns from an outer query.
Mark this column as an outer column if its expression refers to columns from an outer query. This is used to trigger lazy analysis of Spark Classic DataFrame, so that we can use it to build subquery expressions. Spark Connect DataFrame is always lazily analyzed and does not need to use this function.

```
// Spark can't analyze this `df` now as it doesn't know how to resolve `t1.col`.
val df = spark.table("t2").where($"t2.col" === $"t1.col".outer())

// Since this `df` is lazily analyzed, you won't see any error until you try to execute it.
df.collect()  // Fails with UNRESOLVED_COLUMN error.

// Now Spark can resolve `t1.col` with the outer plan `spark.table("t1")`.
spark.table("t1").where(df.exists())
```

Since

4.0.0
  107. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#over\(\):org.apache.spark.sql.Column "Permalink") def over(): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Defines an empty analytic clause.
Defines an empty analytic clause. In this case the analytic function is applied and presented for all rows in the result set.

```
df.select(
  sum("price").over(),
  avg("price").over()
)
```

Since

2.0.0
  108. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#over\(window:org.apache.spark.sql.expressions.WindowSpec\):org.apache.spark.sql.Column "Permalink") def over(window: [WindowSpec](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/expressions/WindowSpec.html "org.apache.spark.sql.expressions.WindowSpec")): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Defines a windowing column.
Defines a windowing column.

```
val w = Window.partitionBy("name").orderBy("id")
df.select(
  sum("price").over(w.rangeBetween(Window.unboundedPreceding, 2)),
  avg("price").over(w.rowsBetween(Window.currentRow, 4))
)
```

Since

1.4.0
  109. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#plus\(other:Any\):org.apache.spark.sql.Column "Permalink") def plus(other: Any): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Sum of this expression and another expression.
Sum of this expression and another expression.

```
// Scala: The following selects the sum of a person's height and weight.
people.select( people("height") + people("weight") )

// Java:
people.select( people.col("height").plus(people.col("weight")) );
```

Since

1.3.0
  110. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#rlike\(literal:String\):org.apache.spark.sql.Column "Permalink") def rlike(literal: String): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
SQL RLIKE expression (LIKE with Regex).
SQL RLIKE expression (LIKE with Regex). Returns a boolean column based on a regex match.

Since

1.3.0
  111. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#startsWith\(literal:String\):org.apache.spark.sql.Column "Permalink") def startsWith(literal: String): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
String starts with another string literal.
String starts with another string literal. Returns a boolean column based on a string match.

Since

1.3.0
  112. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#startsWith\(other:org.apache.spark.sql.Column\):org.apache.spark.sql.Column "Permalink") def startsWith(other: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
String starts with.
String starts with. Returns a boolean column based on a string match.

Since

1.3.0
  113. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#substr\(startPos:Int,len:Int\):org.apache.spark.sql.Column "Permalink") def substr(startPos: Int, len: Int): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
An expression that returns a substring.
An expression that returns a substring.

startPos

starting position.

len

length of the substring.

Since

1.3.0
  114. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#substr\(startPos:org.apache.spark.sql.Column,len:org.apache.spark.sql.Column\):org.apache.spark.sql.Column "Permalink") def substr(startPos: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column"), len: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
An expression that returns a substring.
An expression that returns a substring.

startPos

expression for the starting position.

len

expression for the length of the substring.

Since

1.3.0
  115. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0

Definition Classes
    AnyRef
  116. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#toString\(\):String "Permalink") def toString(): String

Definition Classes
     [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column") → AnyRef → Any
  117. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#transform\(f:org.apache.spark.sql.Column=>org.apache.spark.sql.Column\):org.apache.spark.sql.Column "Permalink") def transform(f: ([Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")) => [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Concise syntax for chaining custom transformations.
Concise syntax for chaining custom transformations.

```
def addPrefix(c: Column): Column = concat(lit("prefix_"), c)

df.select($"name".transform(addPrefix))

// Chaining multiple transformations
df.select($"name".transform(addPrefix).transform(upper))
```

Since

4.1.0
  118. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#try_cast\(to:String\):org.apache.spark.sql.Column "Permalink") def try_cast(to: String): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Casts the column to a different data type and the result is null on failure.
Casts the column to a different data type and the result is null on failure.

```
// Casts colA to integer.
df.select(df("colA").try_cast("int"))
```

Since

4.0.0
  119. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#try_cast\(to:org.apache.spark.sql.types.DataType\):org.apache.spark.sql.Column "Permalink") def try_cast(to: [DataType](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/types/DataType.html "org.apache.spark.sql.types.DataType")): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Casts the column to a different data type and the result is null on failure.
Casts the column to a different data type and the result is null on failure.

```
// Casts colA to IntegerType.
import org.apache.spark.sql.types.IntegerType
df.select(df("colA").try_cast(IntegerType))

// equivalent to
df.select(df("colA").try_cast("int"))
```

Since

4.0.0
  120. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#unary_!:org.apache.spark.sql.Column "Permalink") def unary_!: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Inversion of boolean expression, i.e.
Inversion of boolean expression, i.e. NOT.

```
// Scala: select rows that are not active (isActive === false)
df.filter( !df("isActive") )

// Java:
import static org.apache.spark.sql.functions.*;
df.filter( not(df.col("isActive")) );
```

Since

1.3.0
  121. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#unary_-:org.apache.spark.sql.Column "Permalink") def unary_-: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Unary minus, i.e.
Unary minus, i.e. negate the expression.

```
// Scala: select the amount column and negates all values.
df.select( -df("amount") )

// Java:
import static org.apache.spark.sql.functions.*;
df.select( negate(col("amount") );
```

Since

1.3.0
  122. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])
  123. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  124. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#wait\(\):Unit "Permalink") final  def wait(): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])
  125. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#when\(condition:org.apache.spark.sql.Column,value:Any\):org.apache.spark.sql.Column "Permalink") def when(condition: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column"), value: Any): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Evaluates a list of conditions and returns one of multiple possible result expressions.
Evaluates a list of conditions and returns one of multiple possible result expressions. If otherwise is not defined at the end, null is returned for unmatched conditions.

```
// Example: encoding gender string column into integer.

// Scala:
people.select(when(people("gender") === "male", 0)
  .when(people("gender") === "female", 1)
  .otherwise(2))

// Java:
people.select(when(col("gender").equalTo("male"), 0)
  .when(col("gender").equalTo("female"), 1)
  .otherwise(2))
```

Since

1.4.0
  126. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#withField\(fieldName:String,col:org.apache.spark.sql.Column\):org.apache.spark.sql.Column "Permalink") def withField(fieldName: String, col: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
An expression that adds/replaces field in `StructType` by name.
An expression that adds/replaces field in `StructType` by name.

```
val df = sql("SELECT named_struct('a', 1, 'b', 2) struct_col")
df.select($"struct_col".withField("c", lit(3)))
// result: {"a":1,"b":2,"c":3}

val df = sql("SELECT named_struct('a', 1, 'b', 2) struct_col")
df.select($"struct_col".withField("b", lit(3)))
// result: {"a":1,"b":3}

val df = sql("SELECT CAST(NULL AS struct<a:int,b:int>) struct_col")
df.select($"struct_col".withField("c", lit(3)))
// result: null of type struct<a:int,b:int,c:int>

val df = sql("SELECT named_struct('a', 1, 'b', 2, 'b', 3) struct_col")
df.select($"struct_col".withField("b", lit(100)))
// result: {"a":1,"b":100,"b":100}

val df = sql("SELECT named_struct('a', named_struct('a', 1, 'b', 2)) struct_col")
df.select($"struct_col".withField("a.c", lit(3)))
// result: {"a":{"a":1,"b":2,"c":3}}

val df = sql("SELECT named_struct('a', named_struct('b', 1), 'a', named_struct('c', 2)) struct_col")
df.select($"struct_col".withField("a.c", lit(3)))
// result: org.apache.spark.sql.AnalysisException: Ambiguous reference to fields
```

This method supports adding/replacing nested fields directly e.g.

```
val df = sql("SELECT named_struct('a', named_struct('a', 1, 'b', 2)) struct_col")
df.select($"struct_col".withField("a.c", lit(3)).withField("a.d", lit(4)))
// result: {"a":{"a":1,"b":2,"c":3,"d":4}}
```

However, if you are going to add/replace multiple nested fields, it is more optimal to extract out the nested struct before adding/replacing multiple fields e.g.

```
val df = sql("SELECT named_struct('a', named_struct('a', 1, 'b', 2)) struct_col")
df.select($"struct_col".withField("a", $"struct_col.a".withField("c", lit(3)).withField("d", lit(4))))
// result: {"a":{"a":1,"b":2,"c":3,"d":4}}
```

Since

3.1.0
  127. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#withLogContext\(context:java.util.Map\[String,String\]\)\(body:=>Unit\):Unit "Permalink") def withLogContext(context: [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#java.util.Map "java.util.Map")[String, String])(body: => Unit): Unit

Attributes
    protected

Definition Classes
    Logging
  128. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#||\(other:Any\):org.apache.spark.sql.Column "Permalink") def ||(other: Any): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Boolean OR.
Boolean OR.

```
// Scala: The following selects people that are in school or employed.
people.filter( people("inSchool") || people("isEmployed") )

// Java:
people.filter( people.col("inSchool").or(people.col("isEmployed")) );
```

Since

1.3.0

### Deprecated Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#!==\(other:Any\):org.apache.spark.sql.Column "Permalink") def !==(other: Any): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Inequality test.
Inequality test.

```
// Scala:
df.select( df("colA") !== df("colB") )
df.select( !(df("colA") === df("colB")) )

// Java:
import static org.apache.spark.sql.functions.*;
df.filter( col("colA").notEqual(col("colB")) );
```

Annotations
     @deprecated

Deprecated

_(Since version 2.0.0)_ !== does not have the same precedence as ===, use =!= instead

Since

1.3.0
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#finalize\(\):Unit "Permalink") def finalize(): Unit

Attributes
    protected[lang]

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.Throwable]) @Deprecated

Deprecated

_(Since version 9)_

### Inherited from Logging
### Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#MDC\(key:org.apache.spark.internal.LogKey,value:Any\):org.apache.spark.internal.MDC "Permalink") def MDC(key: LogKey, value: Any): MDC

Attributes
    protected

Definition Classes
    Logging
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#initializeLogIfNecessary\(isInterpreter:Boolean,silent:Boolean\):Boolean "Permalink") def initializeLogIfNecessary(isInterpreter: Boolean, silent: Boolean): Boolean

Attributes
    protected

Definition Classes
    Logging
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#initializeLogIfNecessary\(isInterpreter:Boolean\):Unit "Permalink") def initializeLogIfNecessary(isInterpreter: Boolean): Unit

Attributes
    protected

Definition Classes
    Logging
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#isTraceEnabled\(\):Boolean "Permalink") def isTraceEnabled(): Boolean

Attributes
    protected

Definition Classes
    Logging
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#log:org.slf4j.Logger "Permalink") def log: Logger

Attributes
    protected

Definition Classes
    Logging
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#logBasedOnLevel\(level:org.slf4j.event.Level\)\(f:=>org.apache.spark.internal.MessageWithContext\):Unit "Permalink") def logBasedOnLevel(level: Level)(f: => MessageWithContext): Unit

Attributes
    protected

Definition Classes
    Logging
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#logDebug\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logDebug(msg: => String, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#logDebug\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logDebug(entry: LogEntry, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#logDebug\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logDebug(entry: LogEntry): Unit

Attributes
    protected

Definition Classes
    Logging
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#logDebug\(msg:=>String\):Unit "Permalink") def logDebug(msg: => String): Unit

Attributes
    protected

Definition Classes
    Logging
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#logError\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logError(msg: => String, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#logError\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logError(entry: LogEntry, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#logError\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logError(entry: LogEntry): Unit

Attributes
    protected

Definition Classes
    Logging
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#logError\(msg:=>String\):Unit "Permalink") def logError(msg: => String): Unit

Attributes
    protected

Definition Classes
    Logging
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#logInfo\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logInfo(msg: => String, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#logInfo\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logInfo(entry: LogEntry, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#logInfo\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logInfo(entry: LogEntry): Unit

Attributes
    protected

Definition Classes
    Logging
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#logInfo\(msg:=>String\):Unit "Permalink") def logInfo(msg: => String): Unit

Attributes
    protected

Definition Classes
    Logging
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#logName:String "Permalink") def logName: [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String")

Attributes
    protected

Definition Classes
    Logging
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#logTrace\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logTrace(msg: => String, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#logTrace\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logTrace(entry: LogEntry, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#logTrace\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logTrace(entry: LogEntry): Unit

Attributes
    protected

Definition Classes
    Logging
  23. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#logTrace\(msg:=>String\):Unit "Permalink") def logTrace(msg: => String): Unit

Attributes
    protected

Definition Classes
    Logging
  24. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#logWarning\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logWarning(msg: => String, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  25. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#logWarning\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logWarning(entry: LogEntry, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  26. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#logWarning\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logWarning(entry: LogEntry): Unit

Attributes
    protected

Definition Classes
    Logging
  27. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#logWarning\(msg:=>String\):Unit "Permalink") def logWarning(msg: => String): Unit

Attributes
    protected

Definition Classes
    Logging
  28. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#withLogContext\(context:java.util.Map\[String,String\]\)\(body:=>Unit\):Unit "Permalink") def withLogContext(context: [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#java.util.Map "java.util.Map")[String, String])(body: => Unit): Unit

Attributes
    protected

Definition Classes
    Logging

### Inherited from AnyRef
### Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html###:Int "Permalink") final  def ##: Int

Definition Classes
    AnyRef → Any
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#clone\(\):Object "Permalink") def clone(): AnyRef

Attributes
    protected[lang]

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef]

Definition Classes
    AnyRef → Any

Annotations
     @IntrinsicCandidate() @native()
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#notify\(\):Unit "Permalink") final  def notify(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0

Definition Classes
    AnyRef
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#wait\(\):Unit "Permalink") final  def wait(): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#finalize\(\):Unit "Permalink") def finalize(): Unit

Attributes
    protected[lang]

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.Throwable]) @Deprecated

Deprecated

_(Since version 9)_

### Inherited from Any
### Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0

Definition Classes
    Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean

Definition Classes
    Any

### DataFrame functions
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#explain\(extended:Boolean\):Unit "Permalink") def explain(extended: Boolean): Unit
Prints the expression to the console for debugging purposes.
Prints the expression to the console for debugging purposes.

Since

1.3.0

### Expression operators
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#%\(other:Any\):org.apache.spark.sql.Column "Permalink") def %(other: Any): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Modulo (a.k.a.
Modulo (a.k.a. remainder) expression.

Since

1.3.0
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#&&\(other:Any\):org.apache.spark.sql.Column "Permalink") def &&(other: Any): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Boolean AND.
Boolean AND.

```
// Scala: The following selects people that are in school and employed at the same time.
people.select( people("inSchool") && people("isEmployed") )

// Java:
people.select( people.col("inSchool").and(people.col("isEmployed")) );
```

Since

1.3.0
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#*\(other:Any\):org.apache.spark.sql.Column "Permalink") def *(other: Any): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Multiplication of this expression and another expression.
Multiplication of this expression and another expression.

```
// Scala: The following multiplies a person's height by their weight.
people.select( people("height") * people("weight") )

// Java:
people.select( people.col("height").multiply(people.col("weight")) );
```

Since

1.3.0
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#+\(other:Any\):org.apache.spark.sql.Column "Permalink") def +(other: Any): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Sum of this expression and another expression.
Sum of this expression and another expression.

```
// Scala: The following selects the sum of a person's height and weight.
people.select( people("height") + people("weight") )

// Java:
people.select( people.col("height").plus(people.col("weight")) );
```

Since

1.3.0
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#-\(other:Any\):org.apache.spark.sql.Column "Permalink") def -(other: Any): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Subtraction.
Subtraction. Subtract the other expression from this expression.

```
// Scala: The following selects the difference between people's height and their weight.
people.select( people("height") - people("weight") )

// Java:
people.select( people.col("height").minus(people.col("weight")) );
```

Since

1.3.0
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#/\(other:Any\):org.apache.spark.sql.Column "Permalink") def /(other: Any): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Division this expression by another expression.
Division this expression by another expression.

```
// Scala: The following divides a person's height by their weight.
people.select( people("height") / people("weight") )

// Java:
people.select( people.col("height").divide(people.col("weight")) );
```

Since

1.3.0
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#<\(other:Any\):org.apache.spark.sql.Column "Permalink") def <(other: Any): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Less than.
Less than.

```
// Scala: The following selects people younger than 21.
people.select( people("age") < 21 )

// Java:
people.select( people.col("age").lt(21) );
```

Since

1.3.0
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#<=\(other:Any\):org.apache.spark.sql.Column "Permalink") def <=(other: Any): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Less than or equal to.
Less than or equal to.

```
// Scala: The following selects people age 21 or younger than 21.
people.select( people("age") <= 21 )

// Java:
people.select( people.col("age").leq(21) );
```

Since

1.3.0
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#<=>\(other:Any\):org.apache.spark.sql.Column "Permalink") def <=>(other: Any): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Equality test that is safe for null values.
Equality test that is safe for null values.

Since

1.3.0
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#=!=\(other:Any\):org.apache.spark.sql.Column "Permalink") def =!=(other: Any): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Inequality test.
Inequality test.

```
// Scala:
df.select( df("colA") =!= df("colB") )
df.select( !(df("colA") === df("colB")) )

// Java:
import static org.apache.spark.sql.functions.*;
df.filter( col("colA").notEqual(col("colB")) );
```

Since

2.0.0
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#===\(other:Any\):org.apache.spark.sql.Column "Permalink") def ===(other: Any): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Equality test.
Equality test.

```
// Scala:
df.filter( df("colA") === df("colB") )

// Java
import static org.apache.spark.sql.functions.*;
df.filter( col("colA").equalTo(col("colB")) );
```

Since

1.3.0
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#>\(other:Any\):org.apache.spark.sql.Column "Permalink") def >(other: Any): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Greater than.
Greater than.

```
// Scala: The following selects people older than 21.
people.select( people("age") > 21 )

// Java:
import static org.apache.spark.sql.functions.*;
people.select( people.col("age").gt(21) );
```

Since

1.3.0
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#>=\(other:Any\):org.apache.spark.sql.Column "Permalink") def >=(other: Any): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Greater than or equal to an expression.
Greater than or equal to an expression.

```
// Scala: The following selects people age 21 or older than 21.
people.select( people("age") >= 21 )

// Java:
people.select( people.col("age").geq(21) )
```

Since

1.3.0
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#alias\(alias:String\):org.apache.spark.sql.Column "Permalink") def alias(alias: String): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Gives the column an alias.
Gives the column an alias. Same as `as`.

```
// Renames colA to colB in select output.
df.select($"colA".alias("colB"))
```

Since

1.4.0
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#apply\(extraction:Any\):org.apache.spark.sql.Column "Permalink") def apply(extraction: Any): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Extracts a value or values from a complex type.
Extracts a value or values from a complex type. The following types of extraction are supported:
     * Given an Array, an integer ordinal can be used to retrieve a single value.
     * Given a Map, a key of the correct type can be used to retrieve an individual value.
     * Given a Struct, a string fieldName can be used to extract that field.
     * Given an Array of Structs, a string fieldName can be used to extract filed of every struct in that array, and return an Array of fields.

Since

1.4.0
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#as\(alias:String,metadata:org.apache.spark.sql.types.Metadata\):org.apache.spark.sql.Column "Permalink") def as(alias: String, metadata: [Metadata](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/types/Metadata.html "org.apache.spark.sql.types.Metadata")): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Gives the column an alias with metadata.
Gives the column an alias with metadata.

```
val metadata: Metadata = ...
df.select($"colA".as("colB", metadata))
```

Since

1.3.0
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#as\(alias:Symbol\):org.apache.spark.sql.Column "Permalink") def as(alias: Symbol): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Gives the column an alias.
Gives the column an alias.

```
// Renames colA to colB in select output.
df.select($"colA".as("colB"))
```

If the current column has metadata associated with it, this metadata will be propagated to the new column. If this not desired, use the API `as(alias: String, metadata: Metadata)` with explicit metadata.

Since

1.3.0
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#as\(aliases:Array\[String\]\):org.apache.spark.sql.Column "Permalink") def as(aliases: Array[String]): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Assigns the given aliases to the results of a table generating function.
Assigns the given aliases to the results of a table generating function.

```
// Renames colA to colB in select output.
df.select(explode($"myMap").as("key" :: "value" :: Nil))
```

Since

1.4.0
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#as\(aliases:Seq\[String\]\):org.apache.spark.sql.Column "Permalink") def as(aliases: Seq[String]): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
(Scala-specific) Assigns the given aliases to the results of a table generating function.
(Scala-specific) Assigns the given aliases to the results of a table generating function.

```
// Renames colA to colB in select output.
df.select(explode($"myMap").as("key" :: "value" :: Nil))
```

Since

1.4.0
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#as\(alias:String\):org.apache.spark.sql.Column "Permalink") def as(alias: String): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Gives the column an alias.
Gives the column an alias.

```
// Renames colA to colB in select output.
df.select($"colA".as("colB"))
```

If the current column has metadata associated with it, this metadata will be propagated to the new column. If this not desired, use the API `as(alias: String, metadata: Metadata)` with explicit metadata.

Since

1.3.0
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#asc:org.apache.spark.sql.Column "Permalink") def asc: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Returns a sort expression based on ascending order of the column.
Returns a sort expression based on ascending order of the column.

```
// Scala: sort a DataFrame by age column in ascending order.
df.sort(df("age").asc)

// Java
df.sort(df.col("age").asc());
```

Since

1.3.0
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#asc_nulls_first:org.apache.spark.sql.Column "Permalink") def asc_nulls_first: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Returns a sort expression based on ascending order of the column, and null values return before non-null values.
Returns a sort expression based on ascending order of the column, and null values return before non-null values.

```
// Scala: sort a DataFrame by age column in ascending order and null values appearing first.
df.sort(df("age").asc_nulls_first)

// Java
df.sort(df.col("age").asc_nulls_first());
```

Since

2.1.0
  23. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#asc_nulls_last:org.apache.spark.sql.Column "Permalink") def asc_nulls_last: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Returns a sort expression based on ascending order of the column, and null values appear after non-null values.
Returns a sort expression based on ascending order of the column, and null values appear after non-null values.

```
// Scala: sort a DataFrame by age column in ascending order and null values appearing last.
df.sort(df("age").asc_nulls_last)

// Java
df.sort(df.col("age").asc_nulls_last());
```

Since

2.1.0
  24. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#bitwiseAND\(other:Any\):org.apache.spark.sql.Column "Permalink") def bitwiseAND(other: Any): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Compute bitwise AND of this expression with another expression.
Compute bitwise AND of this expression with another expression.

```
df.select($"colA".bitwiseAND($"colB"))
```

Since

1.4.0
  25. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#bitwiseOR\(other:Any\):org.apache.spark.sql.Column "Permalink") def bitwiseOR(other: Any): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Compute bitwise OR of this expression with another expression.
Compute bitwise OR of this expression with another expression.

```
df.select($"colA".bitwiseOR($"colB"))
```

Since

1.4.0
  26. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#bitwiseXOR\(other:Any\):org.apache.spark.sql.Column "Permalink") def bitwiseXOR(other: Any): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Compute bitwise XOR of this expression with another expression.
Compute bitwise XOR of this expression with another expression.

```
df.select($"colA".bitwiseXOR($"colB"))
```

Since

1.4.0
  27. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#cast\(to:String\):org.apache.spark.sql.Column "Permalink") def cast(to: String): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Casts the column to a different data type, using the canonical string representation of the type.
Casts the column to a different data type, using the canonical string representation of the type. The supported types are: `string`, `boolean`, `byte`, `short`, `int`, `long`, `float`, `double`, `decimal`, `date`, `timestamp`.

```
// Casts colA to integer.
df.select(df("colA").cast("int"))
```

Since

1.3.0
  28. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#cast\(to:org.apache.spark.sql.types.DataType\):org.apache.spark.sql.Column "Permalink") def cast(to: [DataType](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/types/DataType.html "org.apache.spark.sql.types.DataType")): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Casts the column to a different data type.
Casts the column to a different data type.

```
// Casts colA to IntegerType.
import org.apache.spark.sql.types.IntegerType
df.select(df("colA").cast(IntegerType))

// equivalent to
df.select(df("colA").cast("int"))
```

Since

1.3.0
  29. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#contains\(other:Any\):org.apache.spark.sql.Column "Permalink") def contains(other: Any): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Contains the other element.
Contains the other element. Returns a boolean column based on a string match.

Since

1.3.0
  30. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#desc:org.apache.spark.sql.Column "Permalink") def desc: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Returns a sort expression based on the descending order of the column.
Returns a sort expression based on the descending order of the column.

```
// Scala
df.sort(df("age").desc)

// Java
df.sort(df.col("age").desc());
```

Since

1.3.0
  31. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#desc_nulls_first:org.apache.spark.sql.Column "Permalink") def desc_nulls_first: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Returns a sort expression based on the descending order of the column, and null values appear before non-null values.
Returns a sort expression based on the descending order of the column, and null values appear before non-null values.

```
// Scala: sort a DataFrame by age column in descending order and null values appearing first.
df.sort(df("age").desc_nulls_first)

// Java
df.sort(df.col("age").desc_nulls_first());
```

Since

2.1.0
  32. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#desc_nulls_last:org.apache.spark.sql.Column "Permalink") def desc_nulls_last: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Returns a sort expression based on the descending order of the column, and null values appear after non-null values.
Returns a sort expression based on the descending order of the column, and null values appear after non-null values.

```
// Scala: sort a DataFrame by age column in descending order and null values appearing last.
df.sort(df("age").desc_nulls_last)

// Java
df.sort(df.col("age").desc_nulls_last());
```

Since

2.1.0
  33. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#dropFields\(fieldNames:String*\):org.apache.spark.sql.Column "Permalink") def dropFields(fieldNames: String*): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
An expression that drops fields in `StructType` by name.
An expression that drops fields in `StructType` by name. This is a no-op if schema doesn't contain field name(s).

```
val df = sql("SELECT named_struct('a', 1, 'b', 2) struct_col")
df.select($"struct_col".dropFields("b"))
// result: {"a":1}

val df = sql("SELECT named_struct('a', 1, 'b', 2) struct_col")
df.select($"struct_col".dropFields("c"))
// result: {"a":1,"b":2}

val df = sql("SELECT named_struct('a', 1, 'b', 2, 'c', 3) struct_col")
df.select($"struct_col".dropFields("b", "c"))
// result: {"a":1}

val df = sql("SELECT named_struct('a', 1, 'b', 2) struct_col")
df.select($"struct_col".dropFields("a", "b"))
// result: org.apache.spark.sql.AnalysisException: [DATATYPE_MISMATCH.CANNOT_DROP_ALL_FIELDS] Cannot resolve "update_fields(struct_col, dropfield(), dropfield())" due to data type mismatch: Cannot drop all fields in struct.;

val df = sql("SELECT CAST(NULL AS struct<a:int,b:int>) struct_col")
df.select($"struct_col".dropFields("b"))
// result: null of type struct<a:int>

val df = sql("SELECT named_struct('a', 1, 'b', 2, 'b', 3) struct_col")
df.select($"struct_col".dropFields("b"))
// result: {"a":1}

val df = sql("SELECT named_struct('a', named_struct('a', 1, 'b', 2)) struct_col")
df.select($"struct_col".dropFields("a.b"))
// result: {"a":{"a":1}}

val df = sql("SELECT named_struct('a', named_struct('b', 1), 'a', named_struct('c', 2)) struct_col")
df.select($"struct_col".dropFields("a.c"))
// result: org.apache.spark.sql.AnalysisException: Ambiguous reference to fields
```

This method supports dropping multiple nested fields directly e.g.

```
val df = sql("SELECT named_struct('a', named_struct('a', 1, 'b', 2)) struct_col")
df.select($"struct_col".dropFields("a.b", "a.c"))
// result: {"a":{"a":1}}
```

However, if you are going to drop multiple nested fields, it is more optimal to extract out the nested struct before dropping multiple fields from it e.g.

```
val df = sql("SELECT named_struct('a', named_struct('a', 1, 'b', 2)) struct_col")
df.select($"struct_col".withField("a", $"struct_col.a".dropFields("b", "c")))
// result: {"a":{"a":1}}
```

Since

3.1.0
  34. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#endsWith\(literal:String\):org.apache.spark.sql.Column "Permalink") def endsWith(literal: String): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
String ends with another string literal.
String ends with another string literal. Returns a boolean column based on a string match.

Since

1.3.0
  35. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#endsWith\(other:org.apache.spark.sql.Column\):org.apache.spark.sql.Column "Permalink") def endsWith(other: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
String ends with.
String ends with. Returns a boolean column based on a string match.

Since

1.3.0
  36. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#equalTo\(other:Any\):org.apache.spark.sql.Column "Permalink") def equalTo(other: Any): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Equality test.
Equality test.

```
// Scala:
df.filter( df("colA") === df("colB") )

// Java
import static org.apache.spark.sql.functions.*;
df.filter( col("colA").equalTo(col("colB")) );
```

Since

1.3.0
  37. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#getField\(fieldName:String\):org.apache.spark.sql.Column "Permalink") def getField(fieldName: String): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
An expression that gets a field by name in a `StructType`.
An expression that gets a field by name in a `StructType`.

Since

1.3.0
  38. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#getItem\(key:Any\):org.apache.spark.sql.Column "Permalink") def getItem(key: Any): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
An expression that gets an item at position `ordinal` out of an array, or gets a value by key `key` in a `MapType`.
An expression that gets an item at position `ordinal` out of an array, or gets a value by key `key` in a `MapType`.

Since

1.3.0
  39. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#ilike\(literal:String\):org.apache.spark.sql.Column "Permalink") def ilike(literal: String): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
SQL ILIKE expression (case insensitive LIKE).
SQL ILIKE expression (case insensitive LIKE).

Since

3.3.0
  40. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#isInCollection\(values:Iterable\[_\]\):org.apache.spark.sql.Column "Permalink") def isInCollection(values: Iterable[_]): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
A boolean expression that is evaluated to true if the value of this expression is contained by the provided collection.
A boolean expression that is evaluated to true if the value of this expression is contained by the provided collection.
Note: Since the type of the elements in the collection are inferred only during the run time, the elements will be "up-casted" to the most common type for comparison. For eg: 1) In the case of "Int vs String", the "Int" will be up-casted to "String" and the comparison will look like "String vs String". 2) In the case of "Float vs Double", the "Float" will be up-casted to "Double" and the comparison will look like "Double vs Double"

Since

2.4.0
  41. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#isNaN:org.apache.spark.sql.Column "Permalink") def isNaN: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
True if the current expression is NaN.
True if the current expression is NaN.

Since

1.5.0
  42. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#isNotNull:org.apache.spark.sql.Column "Permalink") def isNotNull: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
True if the current expression is NOT null.
True if the current expression is NOT null.

Since

1.3.0
  43. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#isNull:org.apache.spark.sql.Column "Permalink") def isNull: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
True if the current expression is null.
True if the current expression is null.

Since

1.3.0
  44. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#isin\(list:Any*\):org.apache.spark.sql.Column "Permalink") def isin(list: Any*): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
A boolean expression that is evaluated to true if the value of this expression is contained by the evaluated values of the arguments.
A boolean expression that is evaluated to true if the value of this expression is contained by the evaluated values of the arguments.
Note: Since the type of the elements in the list are inferred only during the run time, the elements will be "up-casted" to the most common type for comparison. For eg: 1) In the case of "Int vs String", the "Int" will be up-casted to "String" and the comparison will look like "String vs String". 2) In the case of "Float vs Double", the "Float" will be up-casted to "Double" and the comparison will look like "Double vs Double"

Annotations
     @varargs()

Since

1.5.0
  45. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#like\(literal:String\):org.apache.spark.sql.Column "Permalink") def like(literal: String): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
SQL like expression.
SQL like expression. Returns a boolean column based on a SQL LIKE match.

Since

1.3.0
  46. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#name\(alias:String\):org.apache.spark.sql.Column "Permalink") def name(alias: String): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Gives the column a name (alias).
Gives the column a name (alias).

```
// Renames colA to colB in select output.
df.select($"colA".name("colB"))
```

If the current column has metadata associated with it, this metadata will be propagated to the new column. If this not desired, use the API `as(alias: String, metadata: Metadata)` with explicit metadata.

Since

2.0.0
  47. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#otherwise\(value:Any\):org.apache.spark.sql.Column "Permalink") def otherwise(value: Any): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Evaluates a list of conditions and returns one of multiple possible result expressions.
Evaluates a list of conditions and returns one of multiple possible result expressions. If otherwise is not defined at the end, null is returned for unmatched conditions.

```
// Example: encoding gender string column into integer.

// Scala:
people.select(when(people("gender") === "male", 0)
  .when(people("gender") === "female", 1)
  .otherwise(2))

// Java:
people.select(when(col("gender").equalTo("male"), 0)
  .when(col("gender").equalTo("female"), 1)
  .otherwise(2))
```

Since

1.4.0
  48. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#outer\(\):org.apache.spark.sql.Column "Permalink") def outer(): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Mark this column as an outer column if its expression refers to columns from an outer query.
Mark this column as an outer column if its expression refers to columns from an outer query. This is used to trigger lazy analysis of Spark Classic DataFrame, so that we can use it to build subquery expressions. Spark Connect DataFrame is always lazily analyzed and does not need to use this function.

```
// Spark can't analyze this `df` now as it doesn't know how to resolve `t1.col`.
val df = spark.table("t2").where($"t2.col" === $"t1.col".outer())

// Since this `df` is lazily analyzed, you won't see any error until you try to execute it.
df.collect()  // Fails with UNRESOLVED_COLUMN error.

// Now Spark can resolve `t1.col` with the outer plan `spark.table("t1")`.
spark.table("t1").where(df.exists())
```

Since

4.0.0
  49. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#over\(\):org.apache.spark.sql.Column "Permalink") def over(): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Defines an empty analytic clause.
Defines an empty analytic clause. In this case the analytic function is applied and presented for all rows in the result set.

```
df.select(
  sum("price").over(),
  avg("price").over()
)
```

Since

2.0.0
  50. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#over\(window:org.apache.spark.sql.expressions.WindowSpec\):org.apache.spark.sql.Column "Permalink") def over(window: [WindowSpec](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/expressions/WindowSpec.html "org.apache.spark.sql.expressions.WindowSpec")): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Defines a windowing column.
Defines a windowing column.

```
val w = Window.partitionBy("name").orderBy("id")
df.select(
  sum("price").over(w.rangeBetween(Window.unboundedPreceding, 2)),
  avg("price").over(w.rowsBetween(Window.currentRow, 4))
)
```

Since

1.4.0
  51. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#rlike\(literal:String\):org.apache.spark.sql.Column "Permalink") def rlike(literal: String): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
SQL RLIKE expression (LIKE with Regex).
SQL RLIKE expression (LIKE with Regex). Returns a boolean column based on a regex match.

Since

1.3.0
  52. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#startsWith\(literal:String\):org.apache.spark.sql.Column "Permalink") def startsWith(literal: String): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
String starts with another string literal.
String starts with another string literal. Returns a boolean column based on a string match.

Since

1.3.0
  53. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#startsWith\(other:org.apache.spark.sql.Column\):org.apache.spark.sql.Column "Permalink") def startsWith(other: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
String starts with.
String starts with. Returns a boolean column based on a string match.

Since

1.3.0
  54. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#substr\(startPos:Int,len:Int\):org.apache.spark.sql.Column "Permalink") def substr(startPos: Int, len: Int): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
An expression that returns a substring.
An expression that returns a substring.

startPos

starting position.

len

length of the substring.

Since

1.3.0
  55. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#substr\(startPos:org.apache.spark.sql.Column,len:org.apache.spark.sql.Column\):org.apache.spark.sql.Column "Permalink") def substr(startPos: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column"), len: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
An expression that returns a substring.
An expression that returns a substring.

startPos

expression for the starting position.

len

expression for the length of the substring.

Since

1.3.0
  56. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#transform\(f:org.apache.spark.sql.Column=>org.apache.spark.sql.Column\):org.apache.spark.sql.Column "Permalink") def transform(f: ([Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")) => [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Concise syntax for chaining custom transformations.
Concise syntax for chaining custom transformations.

```
def addPrefix(c: Column): Column = concat(lit("prefix_"), c)

df.select($"name".transform(addPrefix))

// Chaining multiple transformations
df.select($"name".transform(addPrefix).transform(upper))
```

Since

4.1.0
  57. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#try_cast\(to:String\):org.apache.spark.sql.Column "Permalink") def try_cast(to: String): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Casts the column to a different data type and the result is null on failure.
Casts the column to a different data type and the result is null on failure.

```
// Casts colA to integer.
df.select(df("colA").try_cast("int"))
```

Since

4.0.0
  58. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#try_cast\(to:org.apache.spark.sql.types.DataType\):org.apache.spark.sql.Column "Permalink") def try_cast(to: [DataType](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/types/DataType.html "org.apache.spark.sql.types.DataType")): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Casts the column to a different data type and the result is null on failure.
Casts the column to a different data type and the result is null on failure.

```
// Casts colA to IntegerType.
import org.apache.spark.sql.types.IntegerType
df.select(df("colA").try_cast(IntegerType))

// equivalent to
df.select(df("colA").try_cast("int"))
```

Since

4.0.0
  59. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#unary_!:org.apache.spark.sql.Column "Permalink") def unary_!: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Inversion of boolean expression, i.e.
Inversion of boolean expression, i.e. NOT.

```
// Scala: select rows that are not active (isActive === false)
df.filter( !df("isActive") )

// Java:
import static org.apache.spark.sql.functions.*;
df.filter( not(df.col("isActive")) );
```

Since

1.3.0
  60. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#unary_-:org.apache.spark.sql.Column "Permalink") def unary_-: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Unary minus, i.e.
Unary minus, i.e. negate the expression.

```
// Scala: select the amount column and negates all values.
df.select( -df("amount") )

// Java:
import static org.apache.spark.sql.functions.*;
df.select( negate(col("amount") );
```

Since

1.3.0
  61. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#when\(condition:org.apache.spark.sql.Column,value:Any\):org.apache.spark.sql.Column "Permalink") def when(condition: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column"), value: Any): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Evaluates a list of conditions and returns one of multiple possible result expressions.
Evaluates a list of conditions and returns one of multiple possible result expressions. If otherwise is not defined at the end, null is returned for unmatched conditions.

```
// Example: encoding gender string column into integer.

// Scala:
people.select(when(people("gender") === "male", 0)
  .when(people("gender") === "female", 1)
  .otherwise(2))

// Java:
people.select(when(col("gender").equalTo("male"), 0)
  .when(col("gender").equalTo("female"), 1)
  .otherwise(2))
```

Since

1.4.0
  62. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#withField\(fieldName:String,col:org.apache.spark.sql.Column\):org.apache.spark.sql.Column "Permalink") def withField(fieldName: String, col: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
An expression that adds/replaces field in `StructType` by name.
An expression that adds/replaces field in `StructType` by name.

```
val df = sql("SELECT named_struct('a', 1, 'b', 2) struct_col")
df.select($"struct_col".withField("c", lit(3)))
// result: {"a":1,"b":2,"c":3}

val df = sql("SELECT named_struct('a', 1, 'b', 2) struct_col")
df.select($"struct_col".withField("b", lit(3)))
// result: {"a":1,"b":3}

val df = sql("SELECT CAST(NULL AS struct<a:int,b:int>) struct_col")
df.select($"struct_col".withField("c", lit(3)))
// result: null of type struct<a:int,b:int,c:int>

val df = sql("SELECT named_struct('a', 1, 'b', 2, 'b', 3) struct_col")
df.select($"struct_col".withField("b", lit(100)))
// result: {"a":1,"b":100,"b":100}

val df = sql("SELECT named_struct('a', named_struct('a', 1, 'b', 2)) struct_col")
df.select($"struct_col".withField("a.c", lit(3)))
// result: {"a":{"a":1,"b":2,"c":3}}

val df = sql("SELECT named_struct('a', named_struct('b', 1), 'a', named_struct('c', 2)) struct_col")
df.select($"struct_col".withField("a.c", lit(3)))
// result: org.apache.spark.sql.AnalysisException: Ambiguous reference to fields
```

This method supports adding/replacing nested fields directly e.g.

```
val df = sql("SELECT named_struct('a', named_struct('a', 1, 'b', 2)) struct_col")
df.select($"struct_col".withField("a.c", lit(3)).withField("a.d", lit(4)))
// result: {"a":{"a":1,"b":2,"c":3,"d":4}}
```

However, if you are going to add/replace multiple nested fields, it is more optimal to extract out the nested struct before adding/replacing multiple fields e.g.

```
val df = sql("SELECT named_struct('a', named_struct('a', 1, 'b', 2)) struct_col")
df.select($"struct_col".withField("a", $"struct_col.a".withField("c", lit(3)).withField("d", lit(4))))
// result: {"a":{"a":1,"b":2,"c":3,"d":4}}
```

Since

3.1.0
  63. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#||\(other:Any\):org.apache.spark.sql.Column "Permalink") def ||(other: Any): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Boolean OR.
Boolean OR.

```
// Scala: The following selects people that are in school or employed.
people.filter( people("inSchool") || people("isEmployed") )

// Java:
people.filter( people.col("inSchool").or(people.col("isEmployed")) );
```

Since

1.3.0
  64. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#!==\(other:Any\):org.apache.spark.sql.Column "Permalink") def !==(other: Any): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Inequality test.
Inequality test.

```
// Scala:
df.select( df("colA") !== df("colB") )
df.select( !(df("colA") === df("colB")) )

// Java:
import static org.apache.spark.sql.functions.*;
df.filter( col("colA").notEqual(col("colB")) );
```

Annotations
     @deprecated

Deprecated

_(Since version 2.0.0)_ !== does not have the same precedence as ===, use =!= instead

Since

1.3.0

### Java-specific expression operators
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#and\(other:org.apache.spark.sql.Column\):org.apache.spark.sql.Column "Permalink") def and(other: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Boolean AND.
Boolean AND.

```
// Scala: The following selects people that are in school and employed at the same time.
people.select( people("inSchool") && people("isEmployed") )

// Java:
people.select( people.col("inSchool").and(people.col("isEmployed")) );
```

Since

1.3.0
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#between\(lowerBound:Any,upperBound:Any\):org.apache.spark.sql.Column "Permalink") def between(lowerBound: Any, upperBound: Any): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
True if the current column is between the lower bound and upper bound, inclusive.
True if the current column is between the lower bound and upper bound, inclusive.

Since

1.4.0
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#divide\(other:Any\):org.apache.spark.sql.Column "Permalink") def divide(other: Any): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Division this expression by another expression.
Division this expression by another expression.

```
// Scala: The following divides a person's height by their weight.
people.select( people("height") / people("weight") )

// Java:
people.select( people.col("height").divide(people.col("weight")) );
```

Since

1.3.0
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#eqNullSafe\(other:Any\):org.apache.spark.sql.Column "Permalink") def eqNullSafe(other: Any): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Equality test that is safe for null values.
Equality test that is safe for null values.

Since

1.3.0
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#geq\(other:Any\):org.apache.spark.sql.Column "Permalink") def geq(other: Any): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Greater than or equal to an expression.
Greater than or equal to an expression.

```
// Scala: The following selects people age 21 or older than 21.
people.select( people("age") >= 21 )

// Java:
people.select( people.col("age").geq(21) )
```

Since

1.3.0
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#gt\(other:Any\):org.apache.spark.sql.Column "Permalink") def gt(other: Any): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Greater than.
Greater than.

```
// Scala: The following selects people older than 21.
people.select( people("age") > lit(21) )

// Java:
import static org.apache.spark.sql.functions.*;
people.select( people.col("age").gt(21) );
```

Since

1.3.0
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#isInCollection\(values:Iterable\[_\]\):org.apache.spark.sql.Column "Permalink") def isInCollection(values: [Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html#java.lang.Iterable "java.lang.Iterable")[_]): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
A boolean expression that is evaluated to true if the value of this expression is contained by the provided collection.
A boolean expression that is evaluated to true if the value of this expression is contained by the provided collection.
Note: Since the type of the elements in the collection are inferred only during the run time, the elements will be "up-casted" to the most common type for comparison. For eg: 1) In the case of "Int vs String", the "Int" will be up-casted to "String" and the comparison will look like "String vs String". 2) In the case of "Float vs Double", the "Float" will be up-casted to "Double" and the comparison will look like "Double vs Double"

Since

2.4.0
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#leq\(other:Any\):org.apache.spark.sql.Column "Permalink") def leq(other: Any): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Less than or equal to.
Less than or equal to.

```
// Scala: The following selects people age 21 or younger than 21.
people.select( people("age") <= 21 )

// Java:
people.select( people.col("age").leq(21) );
```

Since

1.3.0
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#lt\(other:Any\):org.apache.spark.sql.Column "Permalink") def lt(other: Any): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Less than.
Less than.

```
// Scala: The following selects people younger than 21.
people.select( people("age") < 21 )

// Java:
people.select( people.col("age").lt(21) );
```

Since

1.3.0
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#minus\(other:Any\):org.apache.spark.sql.Column "Permalink") def minus(other: Any): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Subtraction.
Subtraction. Subtract the other expression from this expression.

```
// Scala: The following selects the difference between people's height and their weight.
people.select( people("height") - people("weight") )

// Java:
people.select( people.col("height").minus(people.col("weight")) );
```

Since

1.3.0
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#mod\(other:Any\):org.apache.spark.sql.Column "Permalink") def mod(other: Any): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Modulo (a.k.a.
Modulo (a.k.a. remainder) expression.

Since

1.3.0
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#multiply\(other:Any\):org.apache.spark.sql.Column "Permalink") def multiply(other: Any): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Multiplication of this expression and another expression.
Multiplication of this expression and another expression.

```
// Scala: The following multiplies a person's height by their weight.
people.select( people("height") * people("weight") )

// Java:
people.select( people.col("height").multiply(people.col("weight")) );
```

Since

1.3.0
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#notEqual\(other:Any\):org.apache.spark.sql.Column "Permalink") def notEqual(other: Any): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Inequality test.
Inequality test.

```
// Scala:
df.select( df("colA") !== df("colB") )
df.select( !(df("colA") === df("colB")) )

// Java:
import static org.apache.spark.sql.functions.*;
df.filter( col("colA").notEqual(col("colB")) );
```

Since

1.3.0
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#or\(other:org.apache.spark.sql.Column\):org.apache.spark.sql.Column "Permalink") def or(other: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Boolean OR.
Boolean OR.

```
// Scala: The following selects people that are in school or employed.
people.filter( people("inSchool") || people("isEmployed") )

// Java:
people.filter( people.col("inSchool").or(people.col("isEmployed")) );
```

Since

1.3.0
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#plus\(other:Any\):org.apache.spark.sql.Column "Permalink") def plus(other: Any): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Sum of this expression and another expression.
Sum of this expression and another expression.

```
// Scala: The following selects the sum of a person's height and weight.
people.select( people("height") + people("weight") )

// Java:
people.select( people.col("height").plus(people.col("weight")) );
```

Since

1.3.0

### subquery
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#isin\(ds:org.apache.spark.sql.Dataset\[_\]\):org.apache.spark.sql.Column "Permalink") def isin(ds: [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[_]): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
A boolean expression that is evaluated to true if the value of this expression is contained by the provided Dataset/DataFrame.
A boolean expression that is evaluated to true if the value of this expression is contained by the provided Dataset/DataFrame.

Since

4.1.0

### Support functions for DataFrames
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#LogStringContextextendsAnyRef "Permalink") implicit  class LogStringContext extends AnyRef

Definition Classes
    Logging

  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html###:Int "Permalink") final  def ##: Int

Definition Classes
    AnyRef → Any
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean

Definition Classes
    AnyRef → Any
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#MDC\(key:org.apache.spark.internal.LogKey,value:Any\):org.apache.spark.internal.MDC "Permalink") def MDC(key: LogKey, value: Any): MDC

Attributes
    protected

Definition Classes
    Logging
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#as\[U\]\(implicitevidence$1:org.apache.spark.sql.Encoder\[U\]\):org.apache.spark.sql.TypedColumn\[Any,U\] "Permalink") def as[U](implicit arg0: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[U]): [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[Any, U]
Provides a type hint about the expected return value of this column.
Provides a type hint about the expected return value of this column. This information can be used by operations such as `select` on a [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") to automatically convert the results into the correct JVM types.

Since

1.6.0
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0

Definition Classes
    Any
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#clone\(\):Object "Permalink") def clone(): AnyRef

Attributes
    protected[lang]

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#equals\(that:Any\):Boolean "Permalink") def equals(that: Any): Boolean

Definition Classes
     [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column") → AnyRef → Any
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef]

Definition Classes
    AnyRef → Any

Annotations
     @IntrinsicCandidate() @native()
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#hashCode\(\):Int "Permalink") def hashCode(): Int

Definition Classes
     [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column") → AnyRef → Any
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#initializeLogIfNecessary\(isInterpreter:Boolean,silent:Boolean\):Boolean "Permalink") def initializeLogIfNecessary(isInterpreter: Boolean, silent: Boolean): Boolean

Attributes
    protected

Definition Classes
    Logging
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#initializeLogIfNecessary\(isInterpreter:Boolean\):Unit "Permalink") def initializeLogIfNecessary(isInterpreter: Boolean): Unit

Attributes
    protected

Definition Classes
    Logging
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean

Definition Classes
    Any
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#isTraceEnabled\(\):Boolean "Permalink") def isTraceEnabled(): Boolean

Attributes
    protected

Definition Classes
    Logging
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#log:org.slf4j.Logger "Permalink") def log: Logger

Attributes
    protected

Definition Classes
    Logging
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#logBasedOnLevel\(level:org.slf4j.event.Level\)\(f:=>org.apache.spark.internal.MessageWithContext\):Unit "Permalink") def logBasedOnLevel(level: Level)(f: => MessageWithContext): Unit

Attributes
    protected

Definition Classes
    Logging
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#logDebug\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logDebug(msg: => String, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#logDebug\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logDebug(entry: LogEntry, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#logDebug\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logDebug(entry: LogEntry): Unit

Attributes
    protected

Definition Classes
    Logging
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#logDebug\(msg:=>String\):Unit "Permalink") def logDebug(msg: => String): Unit

Attributes
    protected

Definition Classes
    Logging
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#logError\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logError(msg: => String, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  23. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#logError\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logError(entry: LogEntry, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  24. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#logError\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logError(entry: LogEntry): Unit

Attributes
    protected

Definition Classes
    Logging
  25. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#logError\(msg:=>String\):Unit "Permalink") def logError(msg: => String): Unit

Attributes
    protected

Definition Classes
    Logging
  26. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#logInfo\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logInfo(msg: => String, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  27. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#logInfo\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logInfo(entry: LogEntry, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  28. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#logInfo\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logInfo(entry: LogEntry): Unit

Attributes
    protected

Definition Classes
    Logging
  29. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#logInfo\(msg:=>String\):Unit "Permalink") def logInfo(msg: => String): Unit

Attributes
    protected

Definition Classes
    Logging
  30. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#logName:String "Permalink") def logName: [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String")

Attributes
    protected

Definition Classes
    Logging
  31. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#logTrace\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logTrace(msg: => String, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  32. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#logTrace\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logTrace(entry: LogEntry, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  33. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#logTrace\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logTrace(entry: LogEntry): Unit

Attributes
    protected

Definition Classes
    Logging
  34. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#logTrace\(msg:=>String\):Unit "Permalink") def logTrace(msg: => String): Unit

Attributes
    protected

Definition Classes
    Logging
  35. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#logWarning\(msg:=>String,throwable:Throwable\):Unit "Permalink") def logWarning(msg: => String, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  36. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#logWarning\(entry:org.apache.spark.internal.LogEntry,throwable:Throwable\):Unit "Permalink") def logWarning(entry: LogEntry, throwable: Throwable): Unit

Attributes
    protected

Definition Classes
    Logging
  37. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#logWarning\(entry:org.apache.spark.internal.LogEntry\):Unit "Permalink") def logWarning(entry: LogEntry): Unit

Attributes
    protected

Definition Classes
    Logging
  38. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#logWarning\(msg:=>String\):Unit "Permalink") def logWarning(msg: => String): Unit

Attributes
    protected

Definition Classes
    Logging
  39. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean

Definition Classes
    AnyRef
  40. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#node:org.apache.spark.sql.internal.ColumnNode "Permalink") val node: ColumnNode
  41. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#notify\(\):Unit "Permalink") final  def notify(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  42. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit

Definition Classes
    AnyRef

Annotations
     @IntrinsicCandidate() @native()
  43. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0

Definition Classes
    AnyRef
  44. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#toString\(\):String "Permalink") def toString(): String

Definition Classes
     [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column") → AnyRef → Any
  45. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])
  46. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  47. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#wait\(\):Unit "Permalink") final  def wait(): Unit

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.InterruptedException])
  48. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#withLogContext\(context:java.util.Map\[String,String\]\)\(body:=>Unit\):Unit "Permalink") def withLogContext(context: [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#java.util.Map "java.util.Map")[String, String])(body: => Unit): Unit

Attributes
    protected

Definition Classes
    Logging
  49. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html#finalize\(\):Unit "Permalink") def finalize(): Unit

Attributes
    protected[lang]

Definition Classes
    AnyRef

Annotations
     @throws(classOf[java.lang.Throwable]) @Deprecated

Deprecated

_(Since version 9)_
