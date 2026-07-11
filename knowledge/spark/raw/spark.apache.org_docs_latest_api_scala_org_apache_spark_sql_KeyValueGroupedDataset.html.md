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
# KeyValueGroupedDataset[ __](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html "Permalink")
####  abstract  class KeyValueGroupedDataset[K, V] extends Serializable
A [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") has been logically grouped by a user specified grouping key. Users should not construct a [KeyValueGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html "org.apache.spark.sql.KeyValueGroupedDataset") directly, but should instead call `groupByKey` on an existing [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset").  

Source
    [KeyValueGroupedDataset.scala](https://github.com/apache/spark/tree/v4.1.2/sql/api/src/main/scala/org/apache/spark/sql/KeyValueGroupedDataset.scala) 

Since
    
2.0.0
Linear Supertypes
[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable"), AnyRef, Any
__ __
Ordering
  1. Alphabetic
  2. By Inheritance


Inherited  

  1. KeyValueGroupedDataset
  2. Serializable
  3. AnyRef
  4. Any


  1. Hide All
  2. Show All


Visibility
  1. Public
  2. Protected


### Instance Constructors
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#<init>\(\):org.apache.spark.sql.KeyValueGroupedDataset\[K,V\] "Permalink") new KeyValueGroupedDataset()


### Abstract Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#aggUntyped\(columns:org.apache.spark.sql.TypedColumn\[_,_\]*\):org.apache.spark.sql.Dataset\[_\] "Permalink") abstract  def aggUntyped(columns: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[_, _]*): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[_]
Internal helper function for building typed aggregations that return tuples.
Internal helper function for building typed aggregations that return tuples. For simplicity and code reuse, we do this without the help of the type system and then use helper functions that cast appropriately for the user facing interface.  

Attributes
    protected 
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#cogroupSorted\[U,R\]\(other:org.apache.spark.sql.KeyValueGroupedDataset\[K,U\]\)\(thisSortExprs:org.apache.spark.sql.Column*\)\(otherSortExprs:org.apache.spark.sql.Column*\)\(f:\(K,Iterator\[V\],Iterator\[U\]\)=>IterableOnce\[R\]\)\(implicitevidence$29:org.apache.spark.sql.Encoder\[R\]\):org.apache.spark.sql.Dataset\[R\] "Permalink") abstract  def cogroupSorted[U, R](other: [KeyValueGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html "org.apache.spark.sql.KeyValueGroupedDataset")[K, U])(thisSortExprs: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")*)(otherSortExprs: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")*)(f: (K, Iterator[V], Iterator[U]) => IterableOnce[R])(implicit arg0: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[R]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[R]
(Scala-specific) Applies the given function to each sorted cogrouped data.
(Scala-specific) Applies the given function to each sorted cogrouped data. For each unique group, the function will be passed the grouping key and 2 sorted iterators containing all elements in the group from [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") `this` and `other`. The function can return an iterator containing elements of an arbitrary type which will be returned as a new [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset").
This is equivalent to [KeyValueGroupedDataset#cogroup](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#cogroup\[U,R\]\(other:org.apache.spark.sql.KeyValueGroupedDataset\[K,U\],f:org.apache.spark.api.java.function.CoGroupFunction\[K,V,U,R\],encoder:org.apache.spark.sql.Encoder\[R\]\):org.apache.spark.sql.Dataset\[R\]), except for the iterators to be sorted according to the given sort expressions. That sorting does not add computational complexity.  

Since
    
3.4.0 

See also
    
`org.apache.spark.sql.api.KeyValueGroupedDataset#cogroup`
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#flatMapGroupsWithState\[S,U\]\(outputMode:org.apache.spark.sql.streaming.OutputMode,timeoutConf:org.apache.spark.sql.streaming.GroupStateTimeout,initialState:org.apache.spark.sql.KeyValueGroupedDataset\[K,S\]\)\(func:\(K,Iterator\[V\],org.apache.spark.sql.streaming.GroupState\[S\]\)=>Iterator\[U\]\)\(implicitevidence$14:org.apache.spark.sql.Encoder\[S\],implicitevidence$15:org.apache.spark.sql.Encoder\[U\]\):org.apache.spark.sql.Dataset\[U\] "Permalink") abstract  def flatMapGroupsWithState[S, U](outputMode: [OutputMode](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/OutputMode.html "org.apache.spark.sql.streaming.OutputMode"), timeoutConf: [GroupStateTimeout](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/GroupStateTimeout.html "org.apache.spark.sql.streaming.GroupStateTimeout"), initialState: [KeyValueGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html "org.apache.spark.sql.KeyValueGroupedDataset")[K, S])(func: (K, Iterator[V], [GroupState](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/GroupState.html "org.apache.spark.sql.streaming.GroupState")[S]) => Iterator[U])(implicit arg0: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[S], arg1: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[U]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[U]
(Scala-specific) Applies the given function to each group of data, while maintaining a user-defined per-group state.
(Scala-specific) Applies the given function to each group of data, while maintaining a user-defined per-group state. The result Dataset will represent the objects returned by the function. For a static batch Dataset, the function will be invoked once per group. For a streaming Dataset, the function will be invoked for each group repeatedly in every trigger, and updates to each group's state will be saved across invocations. See `GroupState` for more details.  

S
    
The type of the user-defined state. Must be encodable to Spark SQL types. 

U
    
The type of the output objects. Must be encodable to Spark SQL types. 

outputMode
    
The output mode of the function. 

timeoutConf
    
Timeout configuration for groups that do not receive data for a while. 

initialState
    
The user provided state that will be initialized when the first batch of data is processed in the streaming query. The user defined function will be called on the state data even if there are no other values in the group. To covert a Dataset `ds` of type of type `Dataset[(K, S)]` to a `KeyValueGroupedDataset[K, S]`, use

```
ds.groupByKey(x => x._1).mapValues(_._2)
```

See [org.apache.spark.sql.Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder") for more details on what types are encodable to Spark SQL. 

func
    
Function to be called on every group. 

Since
    
3.2.0
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#flatMapGroupsWithState\[S,U\]\(outputMode:org.apache.spark.sql.streaming.OutputMode,timeoutConf:org.apache.spark.sql.streaming.GroupStateTimeout\)\(func:\(K,Iterator\[V\],org.apache.spark.sql.streaming.GroupState\[S\]\)=>Iterator\[U\]\)\(implicitevidence$12:org.apache.spark.sql.Encoder\[S\],implicitevidence$13:org.apache.spark.sql.Encoder\[U\]\):org.apache.spark.sql.Dataset\[U\] "Permalink") abstract  def flatMapGroupsWithState[S, U](outputMode: [OutputMode](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/OutputMode.html "org.apache.spark.sql.streaming.OutputMode"), timeoutConf: [GroupStateTimeout](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/GroupStateTimeout.html "org.apache.spark.sql.streaming.GroupStateTimeout"))(func: (K, Iterator[V], [GroupState](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/GroupState.html "org.apache.spark.sql.streaming.GroupState")[S]) => Iterator[U])(implicit arg0: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[S], arg1: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[U]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[U]
(Scala-specific) Applies the given function to each group of data, while maintaining a user-defined per-group state.
(Scala-specific) Applies the given function to each group of data, while maintaining a user-defined per-group state. The result Dataset will represent the objects returned by the function. For a static batch Dataset, the function will be invoked once per group. For a streaming Dataset, the function will be invoked for each group repeatedly in every trigger, and updates to each group's state will be saved across invocations. See `GroupState` for more details.  

S
    
The type of the user-defined state. Must be encodable to Spark SQL types. 

U
    
The type of the output objects. Must be encodable to Spark SQL types. 

outputMode
    
The output mode of the function. 

timeoutConf
    
Timeout configuration for groups that do not receive data for a while. See [org.apache.spark.sql.Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder") for more details on what types are encodable to Spark SQL. 

func
    
Function to be called on every group. 

Since
    
2.2.0
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#flatMapSortedGroups\[U\]\(sortExprs:org.apache.spark.sql.Column*\)\(f:\(K,Iterator\[V\]\)=>IterableOnce\[U\]\)\(implicitevidence$4:org.apache.spark.sql.Encoder\[U\]\):org.apache.spark.sql.Dataset\[U\] "Permalink") abstract  def flatMapSortedGroups[U](sortExprs: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")*)(f: (K, Iterator[V]) => IterableOnce[U])(implicit arg0: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[U]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[U]
(Scala-specific) Applies the given function to each group of data.
(Scala-specific) Applies the given function to each group of data. For each unique group, the function will be passed the group key and a sorted iterator that contains all of the elements in the group. The function can return an iterator containing elements of an arbitrary type which will be returned as a new [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset").
This function does not support partial aggregation, and as a result requires shuffling all the data in the [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset"). If an application intends to perform an aggregation over each key, it is best to use the reduce function or an `org.apache.spark.sql.expressions#Aggregator`.
Internally, the implementation will spill to disk if any given group is too large to fit into memory. However, users must take care to avoid materializing the whole iterator for a group (for example, by calling `toList`) unless they are sure that this is possible given the memory constraints of their cluster.
This is equivalent to [KeyValueGroupedDataset#flatMapGroups](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#flatMapGroups\[U\]\(f:org.apache.spark.api.java.function.FlatMapGroupsFunction\[K,V,U\],encoder:org.apache.spark.sql.Encoder\[U\]\):org.apache.spark.sql.Dataset\[U\]), except for the iterator to be sorted according to the given sort expressions. That sorting does not add computational complexity.  

Since
    
3.4.0 

See also
    
`org.apache.spark.sql.api.KeyValueGroupedDataset#flatMapGroups`
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#keyAs\[L\]\(implicitevidence$1:org.apache.spark.sql.Encoder\[L\]\):org.apache.spark.sql.KeyValueGroupedDataset\[L,V\] "Permalink") abstract  def keyAs[L](implicit arg0: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[L]): [KeyValueGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html "org.apache.spark.sql.KeyValueGroupedDataset")[L, V]
Returns a new [KeyValueGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html "org.apache.spark.sql.KeyValueGroupedDataset") where the type of the key has been mapped to the specified type.
Returns a new [KeyValueGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html "org.apache.spark.sql.KeyValueGroupedDataset") where the type of the key has been mapped to the specified type. The mapping of key columns to the type follows the same rules as `as` on [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset").  

Since
    
1.6.0
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#keys:org.apache.spark.sql.Dataset\[K\] "Permalink") abstract  def keys: [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[K]
Returns a [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") that contains each unique key.
Returns a [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") that contains each unique key. This is equivalent to doing mapping over the Dataset to extract the keys and then running a distinct operation on those.  

Since
    
1.6.0
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#mapGroupsWithState\[S,U\]\(timeoutConf:org.apache.spark.sql.streaming.GroupStateTimeout,initialState:org.apache.spark.sql.KeyValueGroupedDataset\[K,S\]\)\(func:\(K,Iterator\[V\],org.apache.spark.sql.streaming.GroupState\[S\]\)=>U\)\(implicitevidence$10:org.apache.spark.sql.Encoder\[S\],implicitevidence$11:org.apache.spark.sql.Encoder\[U\]\):org.apache.spark.sql.Dataset\[U\] "Permalink") abstract  def mapGroupsWithState[S, U](timeoutConf: [GroupStateTimeout](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/GroupStateTimeout.html "org.apache.spark.sql.streaming.GroupStateTimeout"), initialState: [KeyValueGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html "org.apache.spark.sql.KeyValueGroupedDataset")[K, S])(func: (K, Iterator[V], [GroupState](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/GroupState.html "org.apache.spark.sql.streaming.GroupState")[S]) => U)(implicit arg0: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[S], arg1: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[U]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[U]
(Scala-specific) Applies the given function to each group of data, while maintaining a user-defined per-group state.
(Scala-specific) Applies the given function to each group of data, while maintaining a user-defined per-group state. The result Dataset will represent the objects returned by the function. For a static batch Dataset, the function will be invoked once per group. For a streaming Dataset, the function will be invoked for each group repeatedly in every trigger, and updates to each group's state will be saved across invocations. See [org.apache.spark.sql.streaming.GroupState](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/GroupState.html "org.apache.spark.sql.streaming.GroupState") for more details.  

S
    
The type of the user-defined state. Must be encodable to Spark SQL types. 

U
    
The type of the output objects. Must be encodable to Spark SQL types. 

timeoutConf
    
Timeout Conf, see GroupStateTimeout for more details 

initialState
    
The user provided state that will be initialized when the first batch of data is processed in the streaming query. The user defined function will be called on the state data even if there are no other values in the group. To convert a Dataset ds of type Dataset[(K, S)] to a KeyValueGroupedDataset[K, S] do 

```
ds.groupByKey(x => x._1).mapValues(_._2)
```

See [org.apache.spark.sql.Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder") for more details on what types are encodable to Spark SQL. 

func
    
Function to be called on every group. 

Since
    
3.2.0
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#mapGroupsWithState\[S,U\]\(timeoutConf:org.apache.spark.sql.streaming.GroupStateTimeout\)\(func:\(K,Iterator\[V\],org.apache.spark.sql.streaming.GroupState\[S\]\)=>U\)\(implicitevidence$8:org.apache.spark.sql.Encoder\[S\],implicitevidence$9:org.apache.spark.sql.Encoder\[U\]\):org.apache.spark.sql.Dataset\[U\] "Permalink") abstract  def mapGroupsWithState[S, U](timeoutConf: [GroupStateTimeout](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/GroupStateTimeout.html "org.apache.spark.sql.streaming.GroupStateTimeout"))(func: (K, Iterator[V], [GroupState](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/GroupState.html "org.apache.spark.sql.streaming.GroupState")[S]) => U)(implicit arg0: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[S], arg1: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[U]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[U]
(Scala-specific) Applies the given function to each group of data, while maintaining a user-defined per-group state.
(Scala-specific) Applies the given function to each group of data, while maintaining a user-defined per-group state. The result Dataset will represent the objects returned by the function. For a static batch Dataset, the function will be invoked once per group. For a streaming Dataset, the function will be invoked for each group repeatedly in every trigger, and updates to each group's state will be saved across invocations. See [org.apache.spark.sql.streaming.GroupState](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/GroupState.html "org.apache.spark.sql.streaming.GroupState") for more details.  

S
    
The type of the user-defined state. Must be encodable to Spark SQL types. 

U
    
The type of the output objects. Must be encodable to Spark SQL types. 

timeoutConf
    
Timeout configuration for groups that do not receive data for a while. See [org.apache.spark.sql.Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder") for more details on what types are encodable to Spark SQL. 

func
    
Function to be called on every group. 

Since
    
2.2.0
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#mapGroupsWithState\[S,U\]\(func:\(K,Iterator\[V\],org.apache.spark.sql.streaming.GroupState\[S\]\)=>U\)\(implicitevidence$6:org.apache.spark.sql.Encoder\[S\],implicitevidence$7:org.apache.spark.sql.Encoder\[U\]\):org.apache.spark.sql.Dataset\[U\] "Permalink") abstract  def mapGroupsWithState[S, U](func: (K, Iterator[V], [GroupState](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/GroupState.html "org.apache.spark.sql.streaming.GroupState")[S]) => U)(implicit arg0: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[S], arg1: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[U]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[U]
(Scala-specific) Applies the given function to each group of data, while maintaining a user-defined per-group state.
(Scala-specific) Applies the given function to each group of data, while maintaining a user-defined per-group state. The result Dataset will represent the objects returned by the function. For a static batch Dataset, the function will be invoked once per group. For a streaming Dataset, the function will be invoked for each group repeatedly in every trigger, and updates to each group's state will be saved across invocations. See [org.apache.spark.sql.streaming.GroupState](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/GroupState.html "org.apache.spark.sql.streaming.GroupState") for more details.  

S
    
The type of the user-defined state. Must be encodable to Spark SQL types. 

U
    
The type of the output objects. Must be encodable to Spark SQL types. 

func
    
Function to be called on every group. See [org.apache.spark.sql.Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder") for more details on what types are encodable to Spark SQL. 

Since
    
2.2.0
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#mapValues\[W\]\(func:V=>W\)\(implicitevidence$2:org.apache.spark.sql.Encoder\[W\]\):org.apache.spark.sql.KeyValueGroupedDataset\[K,W\] "Permalink") abstract  def mapValues[W](func: (V) => W)(implicit arg0: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[W]): [KeyValueGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html "org.apache.spark.sql.KeyValueGroupedDataset")[K, W]
Returns a new [KeyValueGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html "org.apache.spark.sql.KeyValueGroupedDataset") where the given function `func` has been applied to the data.
Returns a new [KeyValueGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html "org.apache.spark.sql.KeyValueGroupedDataset") where the given function `func` has been applied to the data. The grouping key is unchanged by this.

```
// Create values grouped by key from a Dataset[(K, V)]
ds.groupByKey(_._1).mapValues(_._2) // Scala
```


Since
    
2.1.0
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#reduceGroups\(f:\(V,V\)=>V\):org.apache.spark.sql.Dataset\[\(K,V\)\] "Permalink") abstract  def reduceGroups(f: (V, V) => V): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[(K, V)]
(Scala-specific) Reduces the elements of each group of data using the specified binary function.
(Scala-specific) Reduces the elements of each group of data using the specified binary function. The given function must be commutative and associative or the result may be non-deterministic.  

Since
    
1.6.0
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#transformWithState\[U,S\]\(statefulProcessor:org.apache.spark.sql.streaming.StatefulProcessorWithInitialState\[K,V,U,S\],eventTimeColumnName:String,outputMode:org.apache.spark.sql.streaming.OutputMode,initialState:org.apache.spark.sql.KeyValueGroupedDataset\[K,S\]\)\(implicitevidence$22:org.apache.spark.sql.Encoder\[U\],implicitevidence$23:org.apache.spark.sql.Encoder\[S\]\):org.apache.spark.sql.Dataset\[U\] "Permalink") abstract  def transformWithState[U, S](statefulProcessor: [StatefulProcessorWithInitialState](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StatefulProcessorWithInitialState.html "org.apache.spark.sql.streaming.StatefulProcessorWithInitialState")[K, V, U, S], eventTimeColumnName: String, outputMode: [OutputMode](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/OutputMode.html "org.apache.spark.sql.streaming.OutputMode"), initialState: [KeyValueGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html "org.apache.spark.sql.KeyValueGroupedDataset")[K, S])(implicit arg0: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[U], arg1: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[S]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[U]
(Scala-specific) Invokes methods defined in the stateful processor used in arbitrary state API v2.
(Scala-specific) Invokes methods defined in the stateful processor used in arbitrary state API v2. Functions as the function above, but with additional eventTimeColumnName for output.  

U
    
The type of the output objects. Must be encodable to Spark SQL types. 

S
    
The type of initial state objects. Must be encodable to Spark SQL types. Downstream operators would use specified eventTimeColumnName to calculate watermark. Note that TimeMode is set to EventTime to ensure correct flow of watermark. 

statefulProcessor
    
Instance of statefulProcessor whose functions will be invoked by the operator. 

eventTimeColumnName
    
eventTime column in the output dataset. Any operations after transformWithState will use the new eventTimeColumn. The user needs to ensure that the eventTime for emitted output adheres to the watermark boundary, otherwise streaming query will fail. 

outputMode
    
The output mode of the stateful processor. 

initialState
    
User provided initial state that will be used to initiate state for the query in the first batch. See [org.apache.spark.sql.Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder") for more details on what types are encodable to Spark SQL.
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#transformWithState\[U,S\]\(statefulProcessor:org.apache.spark.sql.streaming.StatefulProcessorWithInitialState\[K,V,U,S\],timeMode:org.apache.spark.sql.streaming.TimeMode,outputMode:org.apache.spark.sql.streaming.OutputMode,initialState:org.apache.spark.sql.KeyValueGroupedDataset\[K,S\]\)\(implicitevidence$20:org.apache.spark.sql.Encoder\[U\],implicitevidence$21:org.apache.spark.sql.Encoder\[S\]\):org.apache.spark.sql.Dataset\[U\] "Permalink") abstract  def transformWithState[U, S](statefulProcessor: [StatefulProcessorWithInitialState](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StatefulProcessorWithInitialState.html "org.apache.spark.sql.streaming.StatefulProcessorWithInitialState")[K, V, U, S], timeMode: [TimeMode](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/TimeMode.html "org.apache.spark.sql.streaming.TimeMode"), outputMode: [OutputMode](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/OutputMode.html "org.apache.spark.sql.streaming.OutputMode"), initialState: [KeyValueGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html "org.apache.spark.sql.KeyValueGroupedDataset")[K, S])(implicit arg0: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[U], arg1: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[S]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[U]
(Scala-specific) Invokes methods defined in the stateful processor used in arbitrary state API v2.
(Scala-specific) Invokes methods defined in the stateful processor used in arbitrary state API v2. Functions as the function above, but with additional initial state.  

U
    
The type of the output objects. Must be encodable to Spark SQL types. 

S
    
The type of initial state objects. Must be encodable to Spark SQL types. 

statefulProcessor
    
Instance of statefulProcessor whose functions will be invoked by the operator. 

timeMode
    
The time mode semantics of the stateful processor for timers and TTL. 

outputMode
    
The output mode of the stateful processor. 

initialState
    
User provided initial state that will be used to initiate state for the query in the first batch. See [org.apache.spark.sql.Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder") for more details on what types are encodable to Spark SQL.
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#transformWithState\[U\]\(statefulProcessor:org.apache.spark.sql.streaming.StatefulProcessor\[K,V,U\],eventTimeColumnName:String,outputMode:org.apache.spark.sql.streaming.OutputMode\)\(implicitevidence$17:org.apache.spark.sql.Encoder\[U\]\):org.apache.spark.sql.Dataset\[U\] "Permalink") abstract  def transformWithState[U](statefulProcessor: [StatefulProcessor](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StatefulProcessor.html "org.apache.spark.sql.streaming.StatefulProcessor")[K, V, U], eventTimeColumnName: String, outputMode: [OutputMode](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/OutputMode.html "org.apache.spark.sql.streaming.OutputMode"))(implicit arg0: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[U]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[U]
(Scala-specific) Invokes methods defined in the stateful processor used in arbitrary state API v2.
(Scala-specific) Invokes methods defined in the stateful processor used in arbitrary state API v2. We allow the user to act on per-group set of input rows along with keyed state and the user can choose to output/return 0 or more rows. For a streaming dataframe, we will repeatedly invoke the interface methods for new rows in each trigger and the user's state/state variables will be stored persistently across invocations.
Downstream operators would use specified eventTimeColumnName to calculate watermark. Note that TimeMode is set to EventTime to ensure correct flow of watermark.  

U
    
The type of the output objects. Must be encodable to Spark SQL types. 

statefulProcessor
    
Instance of statefulProcessor whose functions will be invoked by the operator. 

eventTimeColumnName
    
eventTime column in the output dataset. Any operations after transformWithState will use the new eventTimeColumn. The user needs to ensure that the eventTime for emitted output adheres to the watermark boundary, otherwise streaming query will fail. 

outputMode
    
The output mode of the stateful processor. See [org.apache.spark.sql.Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder") for more details on what types are encodable to Spark SQL.
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#transformWithState\[U\]\(statefulProcessor:org.apache.spark.sql.streaming.StatefulProcessor\[K,V,U\],timeMode:org.apache.spark.sql.streaming.TimeMode,outputMode:org.apache.spark.sql.streaming.OutputMode\)\(implicitevidence$16:org.apache.spark.sql.Encoder\[U\]\):org.apache.spark.sql.Dataset\[U\] "Permalink") abstract  def transformWithState[U](statefulProcessor: [StatefulProcessor](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StatefulProcessor.html "org.apache.spark.sql.streaming.StatefulProcessor")[K, V, U], timeMode: [TimeMode](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/TimeMode.html "org.apache.spark.sql.streaming.TimeMode"), outputMode: [OutputMode](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/OutputMode.html "org.apache.spark.sql.streaming.OutputMode"))(implicit arg0: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[U]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[U]
(Scala-specific) Invokes methods defined in the stateful processor used in arbitrary state API v2.
(Scala-specific) Invokes methods defined in the stateful processor used in arbitrary state API v2. We allow the user to act on per-group set of input rows along with keyed state and the user can choose to output/return 0 or more rows. For a streaming dataframe, we will repeatedly invoke the interface methods for new rows in each trigger and the user's state/state variables will be stored persistently across invocations.  

U
    
The type of the output objects. Must be encodable to Spark SQL types. 

statefulProcessor
    
Instance of statefulProcessor whose functions will be invoked by the operator. 

timeMode
    
The time mode semantics of the stateful processor for timers and TTL. 

outputMode
    
The output mode of the stateful processor. See [org.apache.spark.sql.Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder") for more details on what types are encodable to Spark SQL.


### Concrete Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html###:Int "Permalink") final  def ##: Int 

Definition Classes
    AnyRef → Any
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#agg\[U1,U2,U3,U4,U5,U6,U7,U8\]\(col1:org.apache.spark.sql.TypedColumn\[V,U1\],col2:org.apache.spark.sql.TypedColumn\[V,U2\],col3:org.apache.spark.sql.TypedColumn\[V,U3\],col4:org.apache.spark.sql.TypedColumn\[V,U4\],col5:org.apache.spark.sql.TypedColumn\[V,U5\],col6:org.apache.spark.sql.TypedColumn\[V,U6\],col7:org.apache.spark.sql.TypedColumn\[V,U7\],col8:org.apache.spark.sql.TypedColumn\[V,U8\]\):org.apache.spark.sql.Dataset\[\(K,U1,U2,U3,U4,U5,U6,U7,U8\)\] "Permalink") def agg[U1, U2, U3, U4, U5, U6, U7, U8](col1: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[V, U1], col2: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[V, U2], col3: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[V, U3], col4: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[V, U4], col5: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[V, U5], col6: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[V, U6], col7: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[V, U7], col8: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[V, U8]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[(K, U1, U2, U3, U4, U5, U6, U7, U8)]
Computes the given aggregations, returning a [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") of tuples for each unique key and the result of computing these aggregations over all elements in the group.
Computes the given aggregations, returning a [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") of tuples for each unique key and the result of computing these aggregations over all elements in the group.  

Since
    
3.0.0
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#agg\[U1,U2,U3,U4,U5,U6,U7\]\(col1:org.apache.spark.sql.TypedColumn\[V,U1\],col2:org.apache.spark.sql.TypedColumn\[V,U2\],col3:org.apache.spark.sql.TypedColumn\[V,U3\],col4:org.apache.spark.sql.TypedColumn\[V,U4\],col5:org.apache.spark.sql.TypedColumn\[V,U5\],col6:org.apache.spark.sql.TypedColumn\[V,U6\],col7:org.apache.spark.sql.TypedColumn\[V,U7\]\):org.apache.spark.sql.Dataset\[\(K,U1,U2,U3,U4,U5,U6,U7\)\] "Permalink") def agg[U1, U2, U3, U4, U5, U6, U7](col1: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[V, U1], col2: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[V, U2], col3: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[V, U3], col4: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[V, U4], col5: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[V, U5], col6: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[V, U6], col7: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[V, U7]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[(K, U1, U2, U3, U4, U5, U6, U7)]
Computes the given aggregations, returning a [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") of tuples for each unique key and the result of computing these aggregations over all elements in the group.
Computes the given aggregations, returning a [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") of tuples for each unique key and the result of computing these aggregations over all elements in the group.  

Since
    
3.0.0
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#agg\[U1,U2,U3,U4,U5,U6\]\(col1:org.apache.spark.sql.TypedColumn\[V,U1\],col2:org.apache.spark.sql.TypedColumn\[V,U2\],col3:org.apache.spark.sql.TypedColumn\[V,U3\],col4:org.apache.spark.sql.TypedColumn\[V,U4\],col5:org.apache.spark.sql.TypedColumn\[V,U5\],col6:org.apache.spark.sql.TypedColumn\[V,U6\]\):org.apache.spark.sql.Dataset\[\(K,U1,U2,U3,U4,U5,U6\)\] "Permalink") def agg[U1, U2, U3, U4, U5, U6](col1: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[V, U1], col2: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[V, U2], col3: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[V, U3], col4: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[V, U4], col5: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[V, U5], col6: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[V, U6]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[(K, U1, U2, U3, U4, U5, U6)]
Computes the given aggregations, returning a [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") of tuples for each unique key and the result of computing these aggregations over all elements in the group.
Computes the given aggregations, returning a [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") of tuples for each unique key and the result of computing these aggregations over all elements in the group.  

Since
    
3.0.0
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#agg\[U1,U2,U3,U4,U5\]\(col1:org.apache.spark.sql.TypedColumn\[V,U1\],col2:org.apache.spark.sql.TypedColumn\[V,U2\],col3:org.apache.spark.sql.TypedColumn\[V,U3\],col4:org.apache.spark.sql.TypedColumn\[V,U4\],col5:org.apache.spark.sql.TypedColumn\[V,U5\]\):org.apache.spark.sql.Dataset\[\(K,U1,U2,U3,U4,U5\)\] "Permalink") def agg[U1, U2, U3, U4, U5](col1: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[V, U1], col2: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[V, U2], col3: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[V, U3], col4: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[V, U4], col5: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[V, U5]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[(K, U1, U2, U3, U4, U5)]
Computes the given aggregations, returning a [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") of tuples for each unique key and the result of computing these aggregations over all elements in the group.
Computes the given aggregations, returning a [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") of tuples for each unique key and the result of computing these aggregations over all elements in the group.  

Since
    
3.0.0
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#agg\[U1,U2,U3,U4\]\(col1:org.apache.spark.sql.TypedColumn\[V,U1\],col2:org.apache.spark.sql.TypedColumn\[V,U2\],col3:org.apache.spark.sql.TypedColumn\[V,U3\],col4:org.apache.spark.sql.TypedColumn\[V,U4\]\):org.apache.spark.sql.Dataset\[\(K,U1,U2,U3,U4\)\] "Permalink") def agg[U1, U2, U3, U4](col1: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[V, U1], col2: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[V, U2], col3: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[V, U3], col4: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[V, U4]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[(K, U1, U2, U3, U4)]
Computes the given aggregations, returning a [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") of tuples for each unique key and the result of computing these aggregations over all elements in the group.
Computes the given aggregations, returning a [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") of tuples for each unique key and the result of computing these aggregations over all elements in the group.  

Since
    
1.6.0
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#agg\[U1,U2,U3\]\(col1:org.apache.spark.sql.TypedColumn\[V,U1\],col2:org.apache.spark.sql.TypedColumn\[V,U2\],col3:org.apache.spark.sql.TypedColumn\[V,U3\]\):org.apache.spark.sql.Dataset\[\(K,U1,U2,U3\)\] "Permalink") def agg[U1, U2, U3](col1: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[V, U1], col2: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[V, U2], col3: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[V, U3]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[(K, U1, U2, U3)]
Computes the given aggregations, returning a [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") of tuples for each unique key and the result of computing these aggregations over all elements in the group.
Computes the given aggregations, returning a [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") of tuples for each unique key and the result of computing these aggregations over all elements in the group.  

Since
    
1.6.0
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#agg\[U1,U2\]\(col1:org.apache.spark.sql.TypedColumn\[V,U1\],col2:org.apache.spark.sql.TypedColumn\[V,U2\]\):org.apache.spark.sql.Dataset\[\(K,U1,U2\)\] "Permalink") def agg[U1, U2](col1: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[V, U1], col2: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[V, U2]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[(K, U1, U2)]
Computes the given aggregations, returning a [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") of tuples for each unique key and the result of computing these aggregations over all elements in the group.
Computes the given aggregations, returning a [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") of tuples for each unique key and the result of computing these aggregations over all elements in the group.  

Since
    
1.6.0
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#agg\[U1\]\(col1:org.apache.spark.sql.TypedColumn\[V,U1\]\):org.apache.spark.sql.Dataset\[\(K,U1\)\] "Permalink") def agg[U1](col1: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[V, U1]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[(K, U1)]
Computes the given aggregation, returning a [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") of tuples for each unique key and the result of computing this aggregation over all elements in the group.
Computes the given aggregation, returning a [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") of tuples for each unique key and the result of computing this aggregation over all elements in the group.  

Since
    
1.6.0
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0 

Definition Classes
    Any
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#clone\(\):Object "Permalink") def clone(): AnyRef 

Attributes
    protected[lang]  

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#cogroup\[U,R\]\(other:org.apache.spark.sql.KeyValueGroupedDataset\[K,U\],f:org.apache.spark.api.java.function.CoGroupFunction\[K,V,U,R\],encoder:org.apache.spark.sql.Encoder\[R\]\):org.apache.spark.sql.Dataset\[R\] "Permalink") def cogroup[U, R](other: [KeyValueGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html "org.apache.spark.sql.KeyValueGroupedDataset")[K, U], f: [CoGroupFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/CoGroupFunction.html "org.apache.spark.api.java.function.CoGroupFunction")[K, V, U, R], encoder: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[R]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[R]
(Java-specific) Applies the given function to each cogrouped data.
(Java-specific) Applies the given function to each cogrouped data. For each unique group, the function will be passed the grouping key and 2 iterators containing all elements in the group from [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") `this` and `other`. The function can return an iterator containing elements of an arbitrary type which will be returned as a new [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset").  

Since
    
1.6.0
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#cogroup\[U,R\]\(other:org.apache.spark.sql.KeyValueGroupedDataset\[K,U\]\)\(f:\(K,Iterator\[V\],Iterator\[U\]\)=>IterableOnce\[R\]\)\(implicitevidence$28:org.apache.spark.sql.Encoder\[R\]\):org.apache.spark.sql.Dataset\[R\] "Permalink") def cogroup[U, R](other: [KeyValueGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html "org.apache.spark.sql.KeyValueGroupedDataset")[K, U])(f: (K, Iterator[V], Iterator[U]) => IterableOnce[R])(implicit arg0: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[R]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[R]
(Scala-specific) Applies the given function to each cogrouped data.
(Scala-specific) Applies the given function to each cogrouped data. For each unique group, the function will be passed the grouping key and 2 iterators containing all elements in the group from [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") `this` and `other`. The function can return an iterator containing elements of an arbitrary type which will be returned as a new [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset").  

Since
    
1.6.0
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#cogroupSorted\[U,R\]\(other:org.apache.spark.sql.KeyValueGroupedDataset\[K,U\],thisSortExprs:Array\[org.apache.spark.sql.Column\],otherSortExprs:Array\[org.apache.spark.sql.Column\],f:org.apache.spark.api.java.function.CoGroupFunction\[K,V,U,R\],encoder:org.apache.spark.sql.Encoder\[R\]\):org.apache.spark.sql.Dataset\[R\] "Permalink") def cogroupSorted[U, R](other: [KeyValueGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html "org.apache.spark.sql.KeyValueGroupedDataset")[K, U], thisSortExprs: Array[[Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")], otherSortExprs: Array[[Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")], f: [CoGroupFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/CoGroupFunction.html "org.apache.spark.api.java.function.CoGroupFunction")[K, V, U, R], encoder: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[R]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[R]
(Java-specific) Applies the given function to each sorted cogrouped data.
(Java-specific) Applies the given function to each sorted cogrouped data. For each unique group, the function will be passed the grouping key and 2 sorted iterators containing all elements in the group from [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") `this` and `other`. The function can return an iterator containing elements of an arbitrary type which will be returned as a new [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset").
This is equivalent to [KeyValueGroupedDataset#cogroup](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#cogroup\[U,R\]\(other:org.apache.spark.sql.KeyValueGroupedDataset\[K,U\],f:org.apache.spark.api.java.function.CoGroupFunction\[K,V,U,R\],encoder:org.apache.spark.sql.Encoder\[R\]\):org.apache.spark.sql.Dataset\[R\]), except for the iterators to be sorted according to the given sort expressions. That sorting does not add computational complexity.  

Since
    
3.4.0 

See also
    
`org.apache.spark.sql.api.KeyValueGroupedDataset#cogroup`
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#count\(\):org.apache.spark.sql.Dataset\[\(K,Long\)\] "Permalink") def count(): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[(K, Long)]
Returns a [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") that contains a tuple with each key and the number of items present for that key.
Returns a [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") that contains a tuple with each key and the number of items present for that key.  

Since
    
1.6.0
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#equals\(x$1:Object\):Boolean "Permalink") def equals(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef → Any
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#flatMapGroups\[U\]\(f:org.apache.spark.api.java.function.FlatMapGroupsFunction\[K,V,U\],encoder:org.apache.spark.sql.Encoder\[U\]\):org.apache.spark.sql.Dataset\[U\] "Permalink") def flatMapGroups[U](f: [FlatMapGroupsFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapGroupsFunction.html "org.apache.spark.api.java.function.FlatMapGroupsFunction")[K, V, U], encoder: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[U]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[U]
(Java-specific) Applies the given function to each group of data.
(Java-specific) Applies the given function to each group of data. For each unique group, the function will be passed the group key and an iterator that contains all of the elements in the group. The function can return an iterator containing elements of an arbitrary type which will be returned as a new [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset").
This function does not support partial aggregation, and as a result requires shuffling all the data in the [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset"). If an application intends to perform an aggregation over each key, it is best to use the reduce function or an `org.apache.spark.sql.expressions#Aggregator`.
Internally, the implementation will spill to disk if any given group is too large to fit into memory. However, users must take care to avoid materializing the whole iterator for a group (for example, by calling `toList`) unless they are sure that this is possible given the memory constraints of their cluster.  

Since
    
1.6.0
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#flatMapGroups\[U\]\(f:\(K,Iterator\[V\]\)=>IterableOnce\[U\]\)\(implicitevidence$3:org.apache.spark.sql.Encoder\[U\]\):org.apache.spark.sql.Dataset\[U\] "Permalink") def flatMapGroups[U](f: (K, Iterator[V]) => IterableOnce[U])(implicit arg0: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[U]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[U]
(Scala-specific) Applies the given function to each group of data.
(Scala-specific) Applies the given function to each group of data. For each unique group, the function will be passed the group key and an iterator that contains all of the elements in the group. The function can return an iterator containing elements of an arbitrary type which will be returned as a new [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset").
This function does not support partial aggregation, and as a result requires shuffling all the data in the [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset"). If an application intends to perform an aggregation over each key, it is best to use the reduce function or an `org.apache.spark.sql.expressions#Aggregator`.
Internally, the implementation will spill to disk if any given group is too large to fit into memory. However, users must take care to avoid materializing the whole iterator for a group (for example, by calling `toList`) unless they are sure that this is possible given the memory constraints of their cluster.  

Since
    
1.6.0
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#flatMapGroupsWithState\[S,U\]\(func:org.apache.spark.api.java.function.FlatMapGroupsWithStateFunction\[K,V,S,U\],outputMode:org.apache.spark.sql.streaming.OutputMode,stateEncoder:org.apache.spark.sql.Encoder\[S\],outputEncoder:org.apache.spark.sql.Encoder\[U\],timeoutConf:org.apache.spark.sql.streaming.GroupStateTimeout,initialState:org.apache.spark.sql.KeyValueGroupedDataset\[K,S\]\):org.apache.spark.sql.Dataset\[U\] "Permalink") def flatMapGroupsWithState[S, U](func: [FlatMapGroupsWithStateFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapGroupsWithStateFunction.html "org.apache.spark.api.java.function.FlatMapGroupsWithStateFunction")[K, V, S, U], outputMode: [OutputMode](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/OutputMode.html "org.apache.spark.sql.streaming.OutputMode"), stateEncoder: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[S], outputEncoder: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[U], timeoutConf: [GroupStateTimeout](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/GroupStateTimeout.html "org.apache.spark.sql.streaming.GroupStateTimeout"), initialState: [KeyValueGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html "org.apache.spark.sql.KeyValueGroupedDataset")[K, S]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[U]
(Java-specific) Applies the given function to each group of data, while maintaining a user-defined per-group state.
(Java-specific) Applies the given function to each group of data, while maintaining a user-defined per-group state. The result Dataset will represent the objects returned by the function. For a static batch Dataset, the function will be invoked once per group. For a streaming Dataset, the function will be invoked for each group repeatedly in every trigger, and updates to each group's state will be saved across invocations. See `GroupState` for more details.  

S
    
The type of the user-defined state. Must be encodable to Spark SQL types. 

U
    
The type of the output objects. Must be encodable to Spark SQL types. 

func
    
Function to be called on every group. 

outputMode
    
The output mode of the function. 

stateEncoder
    
Encoder for the state type. 

outputEncoder
    
Encoder for the output type. 

timeoutConf
    
Timeout configuration for groups that do not receive data for a while. 

initialState
    
The user provided state that will be initialized when the first batch of data is processed in the streaming query. The user defined function will be called on the state data even if there are no other values in the group. To covert a Dataset `ds` of type of type `Dataset[(K, S)]` to a `KeyValueGroupedDataset[K, S]`, use

```
ds.groupByKey(x => x._1).mapValues(_._2)
```

See [org.apache.spark.sql.Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder") for more details on what types are encodable to Spark SQL. 

Since
    
3.2.0
  23. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#flatMapGroupsWithState\[S,U\]\(func:org.apache.spark.api.java.function.FlatMapGroupsWithStateFunction\[K,V,S,U\],outputMode:org.apache.spark.sql.streaming.OutputMode,stateEncoder:org.apache.spark.sql.Encoder\[S\],outputEncoder:org.apache.spark.sql.Encoder\[U\],timeoutConf:org.apache.spark.sql.streaming.GroupStateTimeout\):org.apache.spark.sql.Dataset\[U\] "Permalink") def flatMapGroupsWithState[S, U](func: [FlatMapGroupsWithStateFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapGroupsWithStateFunction.html "org.apache.spark.api.java.function.FlatMapGroupsWithStateFunction")[K, V, S, U], outputMode: [OutputMode](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/OutputMode.html "org.apache.spark.sql.streaming.OutputMode"), stateEncoder: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[S], outputEncoder: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[U], timeoutConf: [GroupStateTimeout](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/GroupStateTimeout.html "org.apache.spark.sql.streaming.GroupStateTimeout")): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[U]
(Java-specific) Applies the given function to each group of data, while maintaining a user-defined per-group state.
(Java-specific) Applies the given function to each group of data, while maintaining a user-defined per-group state. The result Dataset will represent the objects returned by the function. For a static batch Dataset, the function will be invoked once per group. For a streaming Dataset, the function will be invoked for each group repeatedly in every trigger, and updates to each group's state will be saved across invocations. See `GroupState` for more details.  

S
    
The type of the user-defined state. Must be encodable to Spark SQL types. 

U
    
The type of the output objects. Must be encodable to Spark SQL types. 

func
    
Function to be called on every group. 

outputMode
    
The output mode of the function. 

stateEncoder
    
Encoder for the state type. 

outputEncoder
    
Encoder for the output type. 

timeoutConf
    
Timeout configuration for groups that do not receive data for a while. See [org.apache.spark.sql.Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder") for more details on what types are encodable to Spark SQL. 

Since
    
2.2.0
  24. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#flatMapSortedGroups\[U\]\(SortExprs:Array\[org.apache.spark.sql.Column\],f:org.apache.spark.api.java.function.FlatMapGroupsFunction\[K,V,U\],encoder:org.apache.spark.sql.Encoder\[U\]\):org.apache.spark.sql.Dataset\[U\] "Permalink") def flatMapSortedGroups[U](SortExprs: Array[[Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")], f: [FlatMapGroupsFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapGroupsFunction.html "org.apache.spark.api.java.function.FlatMapGroupsFunction")[K, V, U], encoder: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[U]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[U]
(Java-specific) Applies the given function to each group of data.
(Java-specific) Applies the given function to each group of data. For each unique group, the function will be passed the group key and a sorted iterator that contains all of the elements in the group. The function can return an iterator containing elements of an arbitrary type which will be returned as a new [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset").
This function does not support partial aggregation, and as a result requires shuffling all the data in the [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset"). If an application intends to perform an aggregation over each key, it is best to use the reduce function or an `org.apache.spark.sql.expressions#Aggregator`.
Internally, the implementation will spill to disk if any given group is too large to fit into memory. However, users must take care to avoid materializing the whole iterator for a group (for example, by calling `toList`) unless they are sure that this is possible given the memory constraints of their cluster.
This is equivalent to [KeyValueGroupedDataset#flatMapGroups](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#flatMapGroups\[U\]\(f:org.apache.spark.api.java.function.FlatMapGroupsFunction\[K,V,U\],encoder:org.apache.spark.sql.Encoder\[U\]\):org.apache.spark.sql.Dataset\[U\]), except for the iterator to be sorted according to the given sort expressions. That sorting does not add computational complexity.  

Since
    
3.4.0 

See also
    
`org.apache.spark.sql.api.KeyValueGroupedDataset#flatMapGroups`
  25. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef] 

Definition Classes
    AnyRef → Any 

Annotations
     @IntrinsicCandidate() @native()
  26. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#hashCode\(\):Int "Permalink") def hashCode(): Int 

Definition Classes
    AnyRef → Any 

Annotations
     @IntrinsicCandidate() @native()
  27. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean 

Definition Classes
    Any
  28. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#mapGroups\[U\]\(f:org.apache.spark.api.java.function.MapGroupsFunction\[K,V,U\],encoder:org.apache.spark.sql.Encoder\[U\]\):org.apache.spark.sql.Dataset\[U\] "Permalink") def mapGroups[U](f: [MapGroupsFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/MapGroupsFunction.html "org.apache.spark.api.java.function.MapGroupsFunction")[K, V, U], encoder: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[U]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[U]
(Java-specific) Applies the given function to each group of data.
(Java-specific) Applies the given function to each group of data. For each unique group, the function will be passed the group key and an iterator that contains all of the elements in the group. The function can return an element of arbitrary type which will be returned as a new [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset").
This function does not support partial aggregation, and as a result requires shuffling all the data in the [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset"). If an application intends to perform an aggregation over each key, it is best to use the reduce function or an `org.apache.spark.sql.expressions#Aggregator`.
Internally, the implementation will spill to disk if any given group is too large to fit into memory. However, users must take care to avoid materializing the whole iterator for a group (for example, by calling `toList`) unless they are sure that this is possible given the memory constraints of their cluster.  

Since
    
1.6.0
  29. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#mapGroups\[U\]\(f:\(K,Iterator\[V\]\)=>U\)\(implicitevidence$5:org.apache.spark.sql.Encoder\[U\]\):org.apache.spark.sql.Dataset\[U\] "Permalink") def mapGroups[U](f: (K, Iterator[V]) => U)(implicit arg0: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[U]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[U]
(Scala-specific) Applies the given function to each group of data.
(Scala-specific) Applies the given function to each group of data. For each unique group, the function will be passed the group key and an iterator that contains all of the elements in the group. The function can return an element of arbitrary type which will be returned as a new [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset").
This function does not support partial aggregation, and as a result requires shuffling all the data in the [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset"). If an application intends to perform an aggregation over each key, it is best to use the reduce function or an `org.apache.spark.sql.expressions#Aggregator`.
Internally, the implementation will spill to disk if any given group is too large to fit into memory. However, users must take care to avoid materializing the whole iterator for a group (for example, by calling `toList`) unless they are sure that this is possible given the memory constraints of their cluster.  

Since
    
1.6.0
  30. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#mapGroupsWithState\[S,U\]\(func:org.apache.spark.api.java.function.MapGroupsWithStateFunction\[K,V,S,U\],stateEncoder:org.apache.spark.sql.Encoder\[S\],outputEncoder:org.apache.spark.sql.Encoder\[U\],timeoutConf:org.apache.spark.sql.streaming.GroupStateTimeout,initialState:org.apache.spark.sql.KeyValueGroupedDataset\[K,S\]\):org.apache.spark.sql.Dataset\[U\] "Permalink") def mapGroupsWithState[S, U](func: [MapGroupsWithStateFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/MapGroupsWithStateFunction.html "org.apache.spark.api.java.function.MapGroupsWithStateFunction")[K, V, S, U], stateEncoder: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[S], outputEncoder: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[U], timeoutConf: [GroupStateTimeout](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/GroupStateTimeout.html "org.apache.spark.sql.streaming.GroupStateTimeout"), initialState: [KeyValueGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html "org.apache.spark.sql.KeyValueGroupedDataset")[K, S]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[U]
(Java-specific) Applies the given function to each group of data, while maintaining a user-defined per-group state.
(Java-specific) Applies the given function to each group of data, while maintaining a user-defined per-group state. The result Dataset will represent the objects returned by the function. For a static batch Dataset, the function will be invoked once per group. For a streaming Dataset, the function will be invoked for each group repeatedly in every trigger, and updates to each group's state will be saved across invocations. See `GroupState` for more details.  

S
    
The type of the user-defined state. Must be encodable to Spark SQL types. 

U
    
The type of the output objects. Must be encodable to Spark SQL types. 

func
    
Function to be called on every group. 

stateEncoder
    
Encoder for the state type. 

outputEncoder
    
Encoder for the output type. 

timeoutConf
    
Timeout configuration for groups that do not receive data for a while. 

initialState
    
The user provided state that will be initialized when the first batch of data is processed in the streaming query. The user defined function will be called on the state data even if there are no other values in the group. See [org.apache.spark.sql.Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder") for more details on what types are encodable to Spark SQL. 

Since
    
3.2.0
  31. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#mapGroupsWithState\[S,U\]\(func:org.apache.spark.api.java.function.MapGroupsWithStateFunction\[K,V,S,U\],stateEncoder:org.apache.spark.sql.Encoder\[S\],outputEncoder:org.apache.spark.sql.Encoder\[U\],timeoutConf:org.apache.spark.sql.streaming.GroupStateTimeout\):org.apache.spark.sql.Dataset\[U\] "Permalink") def mapGroupsWithState[S, U](func: [MapGroupsWithStateFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/MapGroupsWithStateFunction.html "org.apache.spark.api.java.function.MapGroupsWithStateFunction")[K, V, S, U], stateEncoder: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[S], outputEncoder: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[U], timeoutConf: [GroupStateTimeout](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/GroupStateTimeout.html "org.apache.spark.sql.streaming.GroupStateTimeout")): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[U]
(Java-specific) Applies the given function to each group of data, while maintaining a user-defined per-group state.
(Java-specific) Applies the given function to each group of data, while maintaining a user-defined per-group state. The result Dataset will represent the objects returned by the function. For a static batch Dataset, the function will be invoked once per group. For a streaming Dataset, the function will be invoked for each group repeatedly in every trigger, and updates to each group's state will be saved across invocations. See `GroupState` for more details.  

S
    
The type of the user-defined state. Must be encodable to Spark SQL types. 

U
    
The type of the output objects. Must be encodable to Spark SQL types. 

func
    
Function to be called on every group. 

stateEncoder
    
Encoder for the state type. 

outputEncoder
    
Encoder for the output type. 

timeoutConf
    
Timeout configuration for groups that do not receive data for a while. See [org.apache.spark.sql.Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder") for more details on what types are encodable to Spark SQL. 

Since
    
2.2.0
  32. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#mapGroupsWithState\[S,U\]\(func:org.apache.spark.api.java.function.MapGroupsWithStateFunction\[K,V,S,U\],stateEncoder:org.apache.spark.sql.Encoder\[S\],outputEncoder:org.apache.spark.sql.Encoder\[U\]\):org.apache.spark.sql.Dataset\[U\] "Permalink") def mapGroupsWithState[S, U](func: [MapGroupsWithStateFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/MapGroupsWithStateFunction.html "org.apache.spark.api.java.function.MapGroupsWithStateFunction")[K, V, S, U], stateEncoder: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[S], outputEncoder: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[U]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[U]
(Java-specific) Applies the given function to each group of data, while maintaining a user-defined per-group state.
(Java-specific) Applies the given function to each group of data, while maintaining a user-defined per-group state. The result Dataset will represent the objects returned by the function. For a static batch Dataset, the function will be invoked once per group. For a streaming Dataset, the function will be invoked for each group repeatedly in every trigger, and updates to each group's state will be saved across invocations. See `GroupState` for more details.  

S
    
The type of the user-defined state. Must be encodable to Spark SQL types. 

U
    
The type of the output objects. Must be encodable to Spark SQL types. 

func
    
Function to be called on every group. 

stateEncoder
    
Encoder for the state type. 

outputEncoder
    
Encoder for the output type. See [org.apache.spark.sql.Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder") for more details on what types are encodable to Spark SQL. 

Since
    
2.2.0
  33. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#mapValues\[W\]\(func:org.apache.spark.api.java.function.MapFunction\[V,W\],encoder:org.apache.spark.sql.Encoder\[W\]\):org.apache.spark.sql.KeyValueGroupedDataset\[K,W\] "Permalink") def mapValues[W](func: [MapFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/MapFunction.html "org.apache.spark.api.java.function.MapFunction")[V, W], encoder: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[W]): [KeyValueGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html "org.apache.spark.sql.KeyValueGroupedDataset")[K, W]
Returns a new [KeyValueGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html "org.apache.spark.sql.KeyValueGroupedDataset") where the given function `func` has been applied to the data.
Returns a new [KeyValueGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html "org.apache.spark.sql.KeyValueGroupedDataset") where the given function `func` has been applied to the data. The grouping key is unchanged by this.

```
// Create Integer values grouped by String key from a Dataset<Tuple2<String, Integer>>
Dataset<Tuple2<String, Integer>> ds = ...;
KeyValueGroupedDataset<String, Integer> grouped =
  ds.groupByKey(t -> t._1, Encoders.STRING()).mapValues(t -> t._2, Encoders.INT());
```


Since
    
2.1.0
  34. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  35. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#notify\(\):Unit "Permalink") final  def notify(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  36. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  37. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#reduceGroups\(f:org.apache.spark.api.java.function.ReduceFunction\[V\]\):org.apache.spark.sql.Dataset\[\(K,V\)\] "Permalink") def reduceGroups(f: [ReduceFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/ReduceFunction.html "org.apache.spark.api.java.function.ReduceFunction")[V]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[(K, V)]
(Java-specific) Reduces the elements of each group of data using the specified binary function.
(Java-specific) Reduces the elements of each group of data using the specified binary function. The given function must be commutative and associative or the result may be non-deterministic.  

Since
    
1.6.0
  38. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0 

Definition Classes
    AnyRef
  39. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#toString\(\):String "Permalink") def toString(): [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String") 

Definition Classes
    AnyRef → Any
  40. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#transformWithState\[U,S\]\(statefulProcessor:org.apache.spark.sql.streaming.StatefulProcessorWithInitialState\[K,V,U,S\],outputMode:org.apache.spark.sql.streaming.OutputMode,initialState:org.apache.spark.sql.KeyValueGroupedDataset\[K,S\],eventTimeColumnName:String,outputEncoder:org.apache.spark.sql.Encoder\[U\],initialStateEncoder:org.apache.spark.sql.Encoder\[S\]\)\(implicitevidence$26:org.apache.spark.sql.Encoder\[U\],implicitevidence$27:org.apache.spark.sql.Encoder\[S\]\):org.apache.spark.sql.Dataset\[U\] "Permalink") def transformWithState[U, S](statefulProcessor: [StatefulProcessorWithInitialState](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StatefulProcessorWithInitialState.html "org.apache.spark.sql.streaming.StatefulProcessorWithInitialState")[K, V, U, S], outputMode: [OutputMode](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/OutputMode.html "org.apache.spark.sql.streaming.OutputMode"), initialState: [KeyValueGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html "org.apache.spark.sql.KeyValueGroupedDataset")[K, S], eventTimeColumnName: String, outputEncoder: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[U], initialStateEncoder: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[S])(implicit arg0: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[U], arg1: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[S]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[U]
(Java-specific) Invokes methods defined in the stateful processor used in arbitrary state API v2.
(Java-specific) Invokes methods defined in the stateful processor used in arbitrary state API v2. Functions as the function above, but with additional eventTimeColumnName for output.
Downstream operators would use specified eventTimeColumnName to calculate watermark. Note that TimeMode is set to EventTime to ensure correct flow of watermark.  

U
    
The type of the output objects. Must be encodable to Spark SQL types. 

S
    
The type of initial state objects. Must be encodable to Spark SQL types. 

statefulProcessor
    
Instance of statefulProcessor whose functions will be invoked by the operator. 

outputMode
    
The output mode of the stateful processor. 

initialState
    
User provided initial state that will be used to initiate state for the query in the first batch. 

eventTimeColumnName
    
event column in the output dataset. Any operations after transformWithState will use the new eventTimeColumn. The user needs to ensure that the eventTime for emitted output adheres to the watermark boundary, otherwise streaming query will fail. 

outputEncoder
    
Encoder for the output type. 

initialStateEncoder
    
Encoder for the initial state type. See [org.apache.spark.sql.Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder") for more details on what types are encodable to Spark SQL.
  41. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#transformWithState\[U,S\]\(statefulProcessor:org.apache.spark.sql.streaming.StatefulProcessorWithInitialState\[K,V,U,S\],timeMode:org.apache.spark.sql.streaming.TimeMode,outputMode:org.apache.spark.sql.streaming.OutputMode,initialState:org.apache.spark.sql.KeyValueGroupedDataset\[K,S\],outputEncoder:org.apache.spark.sql.Encoder\[U\],initialStateEncoder:org.apache.spark.sql.Encoder\[S\]\)\(implicitevidence$24:org.apache.spark.sql.Encoder\[U\],implicitevidence$25:org.apache.spark.sql.Encoder\[S\]\):org.apache.spark.sql.Dataset\[U\] "Permalink") def transformWithState[U, S](statefulProcessor: [StatefulProcessorWithInitialState](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StatefulProcessorWithInitialState.html "org.apache.spark.sql.streaming.StatefulProcessorWithInitialState")[K, V, U, S], timeMode: [TimeMode](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/TimeMode.html "org.apache.spark.sql.streaming.TimeMode"), outputMode: [OutputMode](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/OutputMode.html "org.apache.spark.sql.streaming.OutputMode"), initialState: [KeyValueGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html "org.apache.spark.sql.KeyValueGroupedDataset")[K, S], outputEncoder: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[U], initialStateEncoder: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[S])(implicit arg0: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[U], arg1: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[S]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[U]
(Java-specific) Invokes methods defined in the stateful processor used in arbitrary state API v2.
(Java-specific) Invokes methods defined in the stateful processor used in arbitrary state API v2. Functions as the function above, but with additional initialStateEncoder for state encoding.  

U
    
The type of the output objects. Must be encodable to Spark SQL types. 

S
    
The type of initial state objects. Must be encodable to Spark SQL types. 

statefulProcessor
    
Instance of statefulProcessor whose functions will be invoked by the operator. 

timeMode
    
The time mode semantics of the stateful processor for timers and TTL. 

outputMode
    
The output mode of the stateful processor. 

initialState
    
User provided initial state that will be used to initiate state for the query in the first batch. 

outputEncoder
    
Encoder for the output type. 

initialStateEncoder
    
Encoder for the initial state type. See [org.apache.spark.sql.Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder") for more details on what types are encodable to Spark SQL.
  42. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#transformWithState\[U\]\(statefulProcessor:org.apache.spark.sql.streaming.StatefulProcessor\[K,V,U\],eventTimeColumnName:String,outputMode:org.apache.spark.sql.streaming.OutputMode,outputEncoder:org.apache.spark.sql.Encoder\[U\]\)\(implicitevidence$19:org.apache.spark.sql.Encoder\[U\]\):org.apache.spark.sql.Dataset\[U\] "Permalink") def transformWithState[U](statefulProcessor: [StatefulProcessor](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StatefulProcessor.html "org.apache.spark.sql.streaming.StatefulProcessor")[K, V, U], eventTimeColumnName: String, outputMode: [OutputMode](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/OutputMode.html "org.apache.spark.sql.streaming.OutputMode"), outputEncoder: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[U])(implicit arg0: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[U]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[U]
(Java-specific) Invokes methods defined in the stateful processor used in arbitrary state API v2.
(Java-specific) Invokes methods defined in the stateful processor used in arbitrary state API v2. We allow the user to act on per-group set of input rows along with keyed state and the user can choose to output/return 0 or more rows.
For a streaming dataframe, we will repeatedly invoke the interface methods for new rows in each trigger and the user's state/state variables will be stored persistently across invocations.
Downstream operators would use specified eventTimeColumnName to calculate watermark. Note that TimeMode is set to EventTime to ensure correct flow of watermark.  

U
    
The type of the output objects. Must be encodable to Spark SQL types. 

statefulProcessor
    
Instance of statefulProcessor whose functions will be invoked by the operator. 

eventTimeColumnName
    
eventTime column in the output dataset. Any operations after transformWithState will use the new eventTimeColumn. The user needs to ensure that the eventTime for emitted output adheres to the watermark boundary, otherwise streaming query will fail. 

outputMode
    
The output mode of the stateful processor. 

outputEncoder
    
Encoder for the output type. See [org.apache.spark.sql.Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder") for more details on what types are encodable to Spark SQL.
  43. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#transformWithState\[U\]\(statefulProcessor:org.apache.spark.sql.streaming.StatefulProcessor\[K,V,U\],timeMode:org.apache.spark.sql.streaming.TimeMode,outputMode:org.apache.spark.sql.streaming.OutputMode,outputEncoder:org.apache.spark.sql.Encoder\[U\]\)\(implicitevidence$18:org.apache.spark.sql.Encoder\[U\]\):org.apache.spark.sql.Dataset\[U\] "Permalink") def transformWithState[U](statefulProcessor: [StatefulProcessor](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StatefulProcessor.html "org.apache.spark.sql.streaming.StatefulProcessor")[K, V, U], timeMode: [TimeMode](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/TimeMode.html "org.apache.spark.sql.streaming.TimeMode"), outputMode: [OutputMode](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/OutputMode.html "org.apache.spark.sql.streaming.OutputMode"), outputEncoder: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[U])(implicit arg0: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[U]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[U]
(Java-specific) Invokes methods defined in the stateful processor used in arbitrary state API v2.
(Java-specific) Invokes methods defined in the stateful processor used in arbitrary state API v2. We allow the user to act on per-group set of input rows along with keyed state and the user can choose to output/return 0 or more rows. For a streaming dataframe, we will repeatedly invoke the interface methods for new rows in each trigger and the user's state/state variables will be stored persistently across invocations.  

U
    
The type of the output objects. Must be encodable to Spark SQL types. 

statefulProcessor
    
Instance of statefulProcessor whose functions will be invoked by the operator. 

timeMode
    
The time mode semantics of the stateful processor for timers and TTL. 

outputMode
    
The output mode of the stateful processor. 

outputEncoder
    
Encoder for the output type. See [org.apache.spark.sql.Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder") for more details on what types are encodable to Spark SQL.
  44. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  45. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  46. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#wait\(\):Unit "Permalink") final  def wait(): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])


### Deprecated Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#finalize\(\):Unit "Permalink") def finalize(): Unit 

Attributes
    protected[lang]  

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.Throwable]) @Deprecated 

Deprecated
    
_(Since version 9)_


### Inherited from AnyRef
### Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html###:Int "Permalink") final  def ##: Int 

Definition Classes
    AnyRef → Any
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#clone\(\):Object "Permalink") def clone(): AnyRef 

Attributes
    protected[lang]  

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#equals\(x$1:Object\):Boolean "Permalink") def equals(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef → Any
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef] 

Definition Classes
    AnyRef → Any 

Annotations
     @IntrinsicCandidate() @native()
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#hashCode\(\):Int "Permalink") def hashCode(): Int 

Definition Classes
    AnyRef → Any 

Annotations
     @IntrinsicCandidate() @native()
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#notify\(\):Unit "Permalink") final  def notify(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0 

Definition Classes
    AnyRef
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#toString\(\):String "Permalink") def toString(): [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String") 

Definition Classes
    AnyRef → Any
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#wait\(\):Unit "Permalink") final  def wait(): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#finalize\(\):Unit "Permalink") def finalize(): Unit 

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
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0 

Definition Classes
    Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean 

Definition Classes
    Any


### Ungrouped
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#aggUntyped\(columns:org.apache.spark.sql.TypedColumn\[_,_\]*\):org.apache.spark.sql.Dataset\[_\] "Permalink") abstract  def aggUntyped(columns: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[_, _]*): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[_]
Internal helper function for building typed aggregations that return tuples.
Internal helper function for building typed aggregations that return tuples. For simplicity and code reuse, we do this without the help of the type system and then use helper functions that cast appropriately for the user facing interface.  

Attributes
    protected 
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#cogroupSorted\[U,R\]\(other:org.apache.spark.sql.KeyValueGroupedDataset\[K,U\]\)\(thisSortExprs:org.apache.spark.sql.Column*\)\(otherSortExprs:org.apache.spark.sql.Column*\)\(f:\(K,Iterator\[V\],Iterator\[U\]\)=>IterableOnce\[R\]\)\(implicitevidence$29:org.apache.spark.sql.Encoder\[R\]\):org.apache.spark.sql.Dataset\[R\] "Permalink") abstract  def cogroupSorted[U, R](other: [KeyValueGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html "org.apache.spark.sql.KeyValueGroupedDataset")[K, U])(thisSortExprs: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")*)(otherSortExprs: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")*)(f: (K, Iterator[V], Iterator[U]) => IterableOnce[R])(implicit arg0: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[R]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[R]
(Scala-specific) Applies the given function to each sorted cogrouped data.
(Scala-specific) Applies the given function to each sorted cogrouped data. For each unique group, the function will be passed the grouping key and 2 sorted iterators containing all elements in the group from [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") `this` and `other`. The function can return an iterator containing elements of an arbitrary type which will be returned as a new [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset").
This is equivalent to [KeyValueGroupedDataset#cogroup](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#cogroup\[U,R\]\(other:org.apache.spark.sql.KeyValueGroupedDataset\[K,U\],f:org.apache.spark.api.java.function.CoGroupFunction\[K,V,U,R\],encoder:org.apache.spark.sql.Encoder\[R\]\):org.apache.spark.sql.Dataset\[R\]), except for the iterators to be sorted according to the given sort expressions. That sorting does not add computational complexity.  

Since
    
3.4.0 

See also
    
`org.apache.spark.sql.api.KeyValueGroupedDataset#cogroup`
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#flatMapGroupsWithState\[S,U\]\(outputMode:org.apache.spark.sql.streaming.OutputMode,timeoutConf:org.apache.spark.sql.streaming.GroupStateTimeout,initialState:org.apache.spark.sql.KeyValueGroupedDataset\[K,S\]\)\(func:\(K,Iterator\[V\],org.apache.spark.sql.streaming.GroupState\[S\]\)=>Iterator\[U\]\)\(implicitevidence$14:org.apache.spark.sql.Encoder\[S\],implicitevidence$15:org.apache.spark.sql.Encoder\[U\]\):org.apache.spark.sql.Dataset\[U\] "Permalink") abstract  def flatMapGroupsWithState[S, U](outputMode: [OutputMode](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/OutputMode.html "org.apache.spark.sql.streaming.OutputMode"), timeoutConf: [GroupStateTimeout](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/GroupStateTimeout.html "org.apache.spark.sql.streaming.GroupStateTimeout"), initialState: [KeyValueGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html "org.apache.spark.sql.KeyValueGroupedDataset")[K, S])(func: (K, Iterator[V], [GroupState](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/GroupState.html "org.apache.spark.sql.streaming.GroupState")[S]) => Iterator[U])(implicit arg0: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[S], arg1: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[U]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[U]
(Scala-specific) Applies the given function to each group of data, while maintaining a user-defined per-group state.
(Scala-specific) Applies the given function to each group of data, while maintaining a user-defined per-group state. The result Dataset will represent the objects returned by the function. For a static batch Dataset, the function will be invoked once per group. For a streaming Dataset, the function will be invoked for each group repeatedly in every trigger, and updates to each group's state will be saved across invocations. See `GroupState` for more details.  

S
    
The type of the user-defined state. Must be encodable to Spark SQL types. 

U
    
The type of the output objects. Must be encodable to Spark SQL types. 

outputMode
    
The output mode of the function. 

timeoutConf
    
Timeout configuration for groups that do not receive data for a while. 

initialState
    
The user provided state that will be initialized when the first batch of data is processed in the streaming query. The user defined function will be called on the state data even if there are no other values in the group. To covert a Dataset `ds` of type of type `Dataset[(K, S)]` to a `KeyValueGroupedDataset[K, S]`, use

```
ds.groupByKey(x => x._1).mapValues(_._2)
```

See [org.apache.spark.sql.Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder") for more details on what types are encodable to Spark SQL. 

func
    
Function to be called on every group. 

Since
    
3.2.0
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#flatMapGroupsWithState\[S,U\]\(outputMode:org.apache.spark.sql.streaming.OutputMode,timeoutConf:org.apache.spark.sql.streaming.GroupStateTimeout\)\(func:\(K,Iterator\[V\],org.apache.spark.sql.streaming.GroupState\[S\]\)=>Iterator\[U\]\)\(implicitevidence$12:org.apache.spark.sql.Encoder\[S\],implicitevidence$13:org.apache.spark.sql.Encoder\[U\]\):org.apache.spark.sql.Dataset\[U\] "Permalink") abstract  def flatMapGroupsWithState[S, U](outputMode: [OutputMode](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/OutputMode.html "org.apache.spark.sql.streaming.OutputMode"), timeoutConf: [GroupStateTimeout](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/GroupStateTimeout.html "org.apache.spark.sql.streaming.GroupStateTimeout"))(func: (K, Iterator[V], [GroupState](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/GroupState.html "org.apache.spark.sql.streaming.GroupState")[S]) => Iterator[U])(implicit arg0: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[S], arg1: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[U]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[U]
(Scala-specific) Applies the given function to each group of data, while maintaining a user-defined per-group state.
(Scala-specific) Applies the given function to each group of data, while maintaining a user-defined per-group state. The result Dataset will represent the objects returned by the function. For a static batch Dataset, the function will be invoked once per group. For a streaming Dataset, the function will be invoked for each group repeatedly in every trigger, and updates to each group's state will be saved across invocations. See `GroupState` for more details.  

S
    
The type of the user-defined state. Must be encodable to Spark SQL types. 

U
    
The type of the output objects. Must be encodable to Spark SQL types. 

outputMode
    
The output mode of the function. 

timeoutConf
    
Timeout configuration for groups that do not receive data for a while. See [org.apache.spark.sql.Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder") for more details on what types are encodable to Spark SQL. 

func
    
Function to be called on every group. 

Since
    
2.2.0
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#flatMapSortedGroups\[U\]\(sortExprs:org.apache.spark.sql.Column*\)\(f:\(K,Iterator\[V\]\)=>IterableOnce\[U\]\)\(implicitevidence$4:org.apache.spark.sql.Encoder\[U\]\):org.apache.spark.sql.Dataset\[U\] "Permalink") abstract  def flatMapSortedGroups[U](sortExprs: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")*)(f: (K, Iterator[V]) => IterableOnce[U])(implicit arg0: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[U]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[U]
(Scala-specific) Applies the given function to each group of data.
(Scala-specific) Applies the given function to each group of data. For each unique group, the function will be passed the group key and a sorted iterator that contains all of the elements in the group. The function can return an iterator containing elements of an arbitrary type which will be returned as a new [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset").
This function does not support partial aggregation, and as a result requires shuffling all the data in the [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset"). If an application intends to perform an aggregation over each key, it is best to use the reduce function or an `org.apache.spark.sql.expressions#Aggregator`.
Internally, the implementation will spill to disk if any given group is too large to fit into memory. However, users must take care to avoid materializing the whole iterator for a group (for example, by calling `toList`) unless they are sure that this is possible given the memory constraints of their cluster.
This is equivalent to [KeyValueGroupedDataset#flatMapGroups](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#flatMapGroups\[U\]\(f:org.apache.spark.api.java.function.FlatMapGroupsFunction\[K,V,U\],encoder:org.apache.spark.sql.Encoder\[U\]\):org.apache.spark.sql.Dataset\[U\]), except for the iterator to be sorted according to the given sort expressions. That sorting does not add computational complexity.  

Since
    
3.4.0 

See also
    
`org.apache.spark.sql.api.KeyValueGroupedDataset#flatMapGroups`
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#keyAs\[L\]\(implicitevidence$1:org.apache.spark.sql.Encoder\[L\]\):org.apache.spark.sql.KeyValueGroupedDataset\[L,V\] "Permalink") abstract  def keyAs[L](implicit arg0: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[L]): [KeyValueGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html "org.apache.spark.sql.KeyValueGroupedDataset")[L, V]
Returns a new [KeyValueGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html "org.apache.spark.sql.KeyValueGroupedDataset") where the type of the key has been mapped to the specified type.
Returns a new [KeyValueGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html "org.apache.spark.sql.KeyValueGroupedDataset") where the type of the key has been mapped to the specified type. The mapping of key columns to the type follows the same rules as `as` on [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset").  

Since
    
1.6.0
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#keys:org.apache.spark.sql.Dataset\[K\] "Permalink") abstract  def keys: [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[K]
Returns a [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") that contains each unique key.
Returns a [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") that contains each unique key. This is equivalent to doing mapping over the Dataset to extract the keys and then running a distinct operation on those.  

Since
    
1.6.0
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#mapGroupsWithState\[S,U\]\(timeoutConf:org.apache.spark.sql.streaming.GroupStateTimeout,initialState:org.apache.spark.sql.KeyValueGroupedDataset\[K,S\]\)\(func:\(K,Iterator\[V\],org.apache.spark.sql.streaming.GroupState\[S\]\)=>U\)\(implicitevidence$10:org.apache.spark.sql.Encoder\[S\],implicitevidence$11:org.apache.spark.sql.Encoder\[U\]\):org.apache.spark.sql.Dataset\[U\] "Permalink") abstract  def mapGroupsWithState[S, U](timeoutConf: [GroupStateTimeout](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/GroupStateTimeout.html "org.apache.spark.sql.streaming.GroupStateTimeout"), initialState: [KeyValueGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html "org.apache.spark.sql.KeyValueGroupedDataset")[K, S])(func: (K, Iterator[V], [GroupState](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/GroupState.html "org.apache.spark.sql.streaming.GroupState")[S]) => U)(implicit arg0: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[S], arg1: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[U]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[U]
(Scala-specific) Applies the given function to each group of data, while maintaining a user-defined per-group state.
(Scala-specific) Applies the given function to each group of data, while maintaining a user-defined per-group state. The result Dataset will represent the objects returned by the function. For a static batch Dataset, the function will be invoked once per group. For a streaming Dataset, the function will be invoked for each group repeatedly in every trigger, and updates to each group's state will be saved across invocations. See [org.apache.spark.sql.streaming.GroupState](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/GroupState.html "org.apache.spark.sql.streaming.GroupState") for more details.  

S
    
The type of the user-defined state. Must be encodable to Spark SQL types. 

U
    
The type of the output objects. Must be encodable to Spark SQL types. 

timeoutConf
    
Timeout Conf, see GroupStateTimeout for more details 

initialState
    
The user provided state that will be initialized when the first batch of data is processed in the streaming query. The user defined function will be called on the state data even if there are no other values in the group. To convert a Dataset ds of type Dataset[(K, S)] to a KeyValueGroupedDataset[K, S] do 

```
ds.groupByKey(x => x._1).mapValues(_._2)
```

See [org.apache.spark.sql.Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder") for more details on what types are encodable to Spark SQL. 

func
    
Function to be called on every group. 

Since
    
3.2.0
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#mapGroupsWithState\[S,U\]\(timeoutConf:org.apache.spark.sql.streaming.GroupStateTimeout\)\(func:\(K,Iterator\[V\],org.apache.spark.sql.streaming.GroupState\[S\]\)=>U\)\(implicitevidence$8:org.apache.spark.sql.Encoder\[S\],implicitevidence$9:org.apache.spark.sql.Encoder\[U\]\):org.apache.spark.sql.Dataset\[U\] "Permalink") abstract  def mapGroupsWithState[S, U](timeoutConf: [GroupStateTimeout](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/GroupStateTimeout.html "org.apache.spark.sql.streaming.GroupStateTimeout"))(func: (K, Iterator[V], [GroupState](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/GroupState.html "org.apache.spark.sql.streaming.GroupState")[S]) => U)(implicit arg0: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[S], arg1: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[U]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[U]
(Scala-specific) Applies the given function to each group of data, while maintaining a user-defined per-group state.
(Scala-specific) Applies the given function to each group of data, while maintaining a user-defined per-group state. The result Dataset will represent the objects returned by the function. For a static batch Dataset, the function will be invoked once per group. For a streaming Dataset, the function will be invoked for each group repeatedly in every trigger, and updates to each group's state will be saved across invocations. See [org.apache.spark.sql.streaming.GroupState](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/GroupState.html "org.apache.spark.sql.streaming.GroupState") for more details.  

S
    
The type of the user-defined state. Must be encodable to Spark SQL types. 

U
    
The type of the output objects. Must be encodable to Spark SQL types. 

timeoutConf
    
Timeout configuration for groups that do not receive data for a while. See [org.apache.spark.sql.Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder") for more details on what types are encodable to Spark SQL. 

func
    
Function to be called on every group. 

Since
    
2.2.0
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#mapGroupsWithState\[S,U\]\(func:\(K,Iterator\[V\],org.apache.spark.sql.streaming.GroupState\[S\]\)=>U\)\(implicitevidence$6:org.apache.spark.sql.Encoder\[S\],implicitevidence$7:org.apache.spark.sql.Encoder\[U\]\):org.apache.spark.sql.Dataset\[U\] "Permalink") abstract  def mapGroupsWithState[S, U](func: (K, Iterator[V], [GroupState](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/GroupState.html "org.apache.spark.sql.streaming.GroupState")[S]) => U)(implicit arg0: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[S], arg1: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[U]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[U]
(Scala-specific) Applies the given function to each group of data, while maintaining a user-defined per-group state.
(Scala-specific) Applies the given function to each group of data, while maintaining a user-defined per-group state. The result Dataset will represent the objects returned by the function. For a static batch Dataset, the function will be invoked once per group. For a streaming Dataset, the function will be invoked for each group repeatedly in every trigger, and updates to each group's state will be saved across invocations. See [org.apache.spark.sql.streaming.GroupState](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/GroupState.html "org.apache.spark.sql.streaming.GroupState") for more details.  

S
    
The type of the user-defined state. Must be encodable to Spark SQL types. 

U
    
The type of the output objects. Must be encodable to Spark SQL types. 

func
    
Function to be called on every group. See [org.apache.spark.sql.Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder") for more details on what types are encodable to Spark SQL. 

Since
    
2.2.0
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#mapValues\[W\]\(func:V=>W\)\(implicitevidence$2:org.apache.spark.sql.Encoder\[W\]\):org.apache.spark.sql.KeyValueGroupedDataset\[K,W\] "Permalink") abstract  def mapValues[W](func: (V) => W)(implicit arg0: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[W]): [KeyValueGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html "org.apache.spark.sql.KeyValueGroupedDataset")[K, W]
Returns a new [KeyValueGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html "org.apache.spark.sql.KeyValueGroupedDataset") where the given function `func` has been applied to the data.
Returns a new [KeyValueGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html "org.apache.spark.sql.KeyValueGroupedDataset") where the given function `func` has been applied to the data. The grouping key is unchanged by this.

```
// Create values grouped by key from a Dataset[(K, V)]
ds.groupByKey(_._1).mapValues(_._2) // Scala
```


Since
    
2.1.0
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#reduceGroups\(f:\(V,V\)=>V\):org.apache.spark.sql.Dataset\[\(K,V\)\] "Permalink") abstract  def reduceGroups(f: (V, V) => V): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[(K, V)]
(Scala-specific) Reduces the elements of each group of data using the specified binary function.
(Scala-specific) Reduces the elements of each group of data using the specified binary function. The given function must be commutative and associative or the result may be non-deterministic.  

Since
    
1.6.0
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#transformWithState\[U,S\]\(statefulProcessor:org.apache.spark.sql.streaming.StatefulProcessorWithInitialState\[K,V,U,S\],eventTimeColumnName:String,outputMode:org.apache.spark.sql.streaming.OutputMode,initialState:org.apache.spark.sql.KeyValueGroupedDataset\[K,S\]\)\(implicitevidence$22:org.apache.spark.sql.Encoder\[U\],implicitevidence$23:org.apache.spark.sql.Encoder\[S\]\):org.apache.spark.sql.Dataset\[U\] "Permalink") abstract  def transformWithState[U, S](statefulProcessor: [StatefulProcessorWithInitialState](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StatefulProcessorWithInitialState.html "org.apache.spark.sql.streaming.StatefulProcessorWithInitialState")[K, V, U, S], eventTimeColumnName: String, outputMode: [OutputMode](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/OutputMode.html "org.apache.spark.sql.streaming.OutputMode"), initialState: [KeyValueGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html "org.apache.spark.sql.KeyValueGroupedDataset")[K, S])(implicit arg0: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[U], arg1: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[S]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[U]
(Scala-specific) Invokes methods defined in the stateful processor used in arbitrary state API v2.
(Scala-specific) Invokes methods defined in the stateful processor used in arbitrary state API v2. Functions as the function above, but with additional eventTimeColumnName for output.  

U
    
The type of the output objects. Must be encodable to Spark SQL types. 

S
    
The type of initial state objects. Must be encodable to Spark SQL types. Downstream operators would use specified eventTimeColumnName to calculate watermark. Note that TimeMode is set to EventTime to ensure correct flow of watermark. 

statefulProcessor
    
Instance of statefulProcessor whose functions will be invoked by the operator. 

eventTimeColumnName
    
eventTime column in the output dataset. Any operations after transformWithState will use the new eventTimeColumn. The user needs to ensure that the eventTime for emitted output adheres to the watermark boundary, otherwise streaming query will fail. 

outputMode
    
The output mode of the stateful processor. 

initialState
    
User provided initial state that will be used to initiate state for the query in the first batch. See [org.apache.spark.sql.Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder") for more details on what types are encodable to Spark SQL.
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#transformWithState\[U,S\]\(statefulProcessor:org.apache.spark.sql.streaming.StatefulProcessorWithInitialState\[K,V,U,S\],timeMode:org.apache.spark.sql.streaming.TimeMode,outputMode:org.apache.spark.sql.streaming.OutputMode,initialState:org.apache.spark.sql.KeyValueGroupedDataset\[K,S\]\)\(implicitevidence$20:org.apache.spark.sql.Encoder\[U\],implicitevidence$21:org.apache.spark.sql.Encoder\[S\]\):org.apache.spark.sql.Dataset\[U\] "Permalink") abstract  def transformWithState[U, S](statefulProcessor: [StatefulProcessorWithInitialState](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StatefulProcessorWithInitialState.html "org.apache.spark.sql.streaming.StatefulProcessorWithInitialState")[K, V, U, S], timeMode: [TimeMode](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/TimeMode.html "org.apache.spark.sql.streaming.TimeMode"), outputMode: [OutputMode](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/OutputMode.html "org.apache.spark.sql.streaming.OutputMode"), initialState: [KeyValueGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html "org.apache.spark.sql.KeyValueGroupedDataset")[K, S])(implicit arg0: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[U], arg1: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[S]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[U]
(Scala-specific) Invokes methods defined in the stateful processor used in arbitrary state API v2.
(Scala-specific) Invokes methods defined in the stateful processor used in arbitrary state API v2. Functions as the function above, but with additional initial state.  

U
    
The type of the output objects. Must be encodable to Spark SQL types. 

S
    
The type of initial state objects. Must be encodable to Spark SQL types. 

statefulProcessor
    
Instance of statefulProcessor whose functions will be invoked by the operator. 

timeMode
    
The time mode semantics of the stateful processor for timers and TTL. 

outputMode
    
The output mode of the stateful processor. 

initialState
    
User provided initial state that will be used to initiate state for the query in the first batch. See [org.apache.spark.sql.Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder") for more details on what types are encodable to Spark SQL.
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#transformWithState\[U\]\(statefulProcessor:org.apache.spark.sql.streaming.StatefulProcessor\[K,V,U\],eventTimeColumnName:String,outputMode:org.apache.spark.sql.streaming.OutputMode\)\(implicitevidence$17:org.apache.spark.sql.Encoder\[U\]\):org.apache.spark.sql.Dataset\[U\] "Permalink") abstract  def transformWithState[U](statefulProcessor: [StatefulProcessor](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StatefulProcessor.html "org.apache.spark.sql.streaming.StatefulProcessor")[K, V, U], eventTimeColumnName: String, outputMode: [OutputMode](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/OutputMode.html "org.apache.spark.sql.streaming.OutputMode"))(implicit arg0: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[U]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[U]
(Scala-specific) Invokes methods defined in the stateful processor used in arbitrary state API v2.
(Scala-specific) Invokes methods defined in the stateful processor used in arbitrary state API v2. We allow the user to act on per-group set of input rows along with keyed state and the user can choose to output/return 0 or more rows. For a streaming dataframe, we will repeatedly invoke the interface methods for new rows in each trigger and the user's state/state variables will be stored persistently across invocations.
Downstream operators would use specified eventTimeColumnName to calculate watermark. Note that TimeMode is set to EventTime to ensure correct flow of watermark.  

U
    
The type of the output objects. Must be encodable to Spark SQL types. 

statefulProcessor
    
Instance of statefulProcessor whose functions will be invoked by the operator. 

eventTimeColumnName
    
eventTime column in the output dataset. Any operations after transformWithState will use the new eventTimeColumn. The user needs to ensure that the eventTime for emitted output adheres to the watermark boundary, otherwise streaming query will fail. 

outputMode
    
The output mode of the stateful processor. See [org.apache.spark.sql.Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder") for more details on what types are encodable to Spark SQL.
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#transformWithState\[U\]\(statefulProcessor:org.apache.spark.sql.streaming.StatefulProcessor\[K,V,U\],timeMode:org.apache.spark.sql.streaming.TimeMode,outputMode:org.apache.spark.sql.streaming.OutputMode\)\(implicitevidence$16:org.apache.spark.sql.Encoder\[U\]\):org.apache.spark.sql.Dataset\[U\] "Permalink") abstract  def transformWithState[U](statefulProcessor: [StatefulProcessor](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StatefulProcessor.html "org.apache.spark.sql.streaming.StatefulProcessor")[K, V, U], timeMode: [TimeMode](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/TimeMode.html "org.apache.spark.sql.streaming.TimeMode"), outputMode: [OutputMode](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/OutputMode.html "org.apache.spark.sql.streaming.OutputMode"))(implicit arg0: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[U]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[U]
(Scala-specific) Invokes methods defined in the stateful processor used in arbitrary state API v2.
(Scala-specific) Invokes methods defined in the stateful processor used in arbitrary state API v2. We allow the user to act on per-group set of input rows along with keyed state and the user can choose to output/return 0 or more rows. For a streaming dataframe, we will repeatedly invoke the interface methods for new rows in each trigger and the user's state/state variables will be stored persistently across invocations.  

U
    
The type of the output objects. Must be encodable to Spark SQL types. 

statefulProcessor
    
Instance of statefulProcessor whose functions will be invoked by the operator. 

timeMode
    
The time mode semantics of the stateful processor for timers and TTL. 

outputMode
    
The output mode of the stateful processor. See [org.apache.spark.sql.Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder") for more details on what types are encodable to Spark SQL.
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html###:Int "Permalink") final  def ##: Int 

Definition Classes
    AnyRef → Any
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#agg\[U1,U2,U3,U4,U5,U6,U7,U8\]\(col1:org.apache.spark.sql.TypedColumn\[V,U1\],col2:org.apache.spark.sql.TypedColumn\[V,U2\],col3:org.apache.spark.sql.TypedColumn\[V,U3\],col4:org.apache.spark.sql.TypedColumn\[V,U4\],col5:org.apache.spark.sql.TypedColumn\[V,U5\],col6:org.apache.spark.sql.TypedColumn\[V,U6\],col7:org.apache.spark.sql.TypedColumn\[V,U7\],col8:org.apache.spark.sql.TypedColumn\[V,U8\]\):org.apache.spark.sql.Dataset\[\(K,U1,U2,U3,U4,U5,U6,U7,U8\)\] "Permalink") def agg[U1, U2, U3, U4, U5, U6, U7, U8](col1: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[V, U1], col2: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[V, U2], col3: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[V, U3], col4: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[V, U4], col5: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[V, U5], col6: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[V, U6], col7: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[V, U7], col8: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[V, U8]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[(K, U1, U2, U3, U4, U5, U6, U7, U8)]
Computes the given aggregations, returning a [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") of tuples for each unique key and the result of computing these aggregations over all elements in the group.
Computes the given aggregations, returning a [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") of tuples for each unique key and the result of computing these aggregations over all elements in the group.  

Since
    
3.0.0
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#agg\[U1,U2,U3,U4,U5,U6,U7\]\(col1:org.apache.spark.sql.TypedColumn\[V,U1\],col2:org.apache.spark.sql.TypedColumn\[V,U2\],col3:org.apache.spark.sql.TypedColumn\[V,U3\],col4:org.apache.spark.sql.TypedColumn\[V,U4\],col5:org.apache.spark.sql.TypedColumn\[V,U5\],col6:org.apache.spark.sql.TypedColumn\[V,U6\],col7:org.apache.spark.sql.TypedColumn\[V,U7\]\):org.apache.spark.sql.Dataset\[\(K,U1,U2,U3,U4,U5,U6,U7\)\] "Permalink") def agg[U1, U2, U3, U4, U5, U6, U7](col1: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[V, U1], col2: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[V, U2], col3: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[V, U3], col4: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[V, U4], col5: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[V, U5], col6: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[V, U6], col7: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[V, U7]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[(K, U1, U2, U3, U4, U5, U6, U7)]
Computes the given aggregations, returning a [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") of tuples for each unique key and the result of computing these aggregations over all elements in the group.
Computes the given aggregations, returning a [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") of tuples for each unique key and the result of computing these aggregations over all elements in the group.  

Since
    
3.0.0
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#agg\[U1,U2,U3,U4,U5,U6\]\(col1:org.apache.spark.sql.TypedColumn\[V,U1\],col2:org.apache.spark.sql.TypedColumn\[V,U2\],col3:org.apache.spark.sql.TypedColumn\[V,U3\],col4:org.apache.spark.sql.TypedColumn\[V,U4\],col5:org.apache.spark.sql.TypedColumn\[V,U5\],col6:org.apache.spark.sql.TypedColumn\[V,U6\]\):org.apache.spark.sql.Dataset\[\(K,U1,U2,U3,U4,U5,U6\)\] "Permalink") def agg[U1, U2, U3, U4, U5, U6](col1: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[V, U1], col2: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[V, U2], col3: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[V, U3], col4: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[V, U4], col5: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[V, U5], col6: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[V, U6]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[(K, U1, U2, U3, U4, U5, U6)]
Computes the given aggregations, returning a [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") of tuples for each unique key and the result of computing these aggregations over all elements in the group.
Computes the given aggregations, returning a [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") of tuples for each unique key and the result of computing these aggregations over all elements in the group.  

Since
    
3.0.0
  23. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#agg\[U1,U2,U3,U4,U5\]\(col1:org.apache.spark.sql.TypedColumn\[V,U1\],col2:org.apache.spark.sql.TypedColumn\[V,U2\],col3:org.apache.spark.sql.TypedColumn\[V,U3\],col4:org.apache.spark.sql.TypedColumn\[V,U4\],col5:org.apache.spark.sql.TypedColumn\[V,U5\]\):org.apache.spark.sql.Dataset\[\(K,U1,U2,U3,U4,U5\)\] "Permalink") def agg[U1, U2, U3, U4, U5](col1: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[V, U1], col2: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[V, U2], col3: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[V, U3], col4: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[V, U4], col5: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[V, U5]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[(K, U1, U2, U3, U4, U5)]
Computes the given aggregations, returning a [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") of tuples for each unique key and the result of computing these aggregations over all elements in the group.
Computes the given aggregations, returning a [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") of tuples for each unique key and the result of computing these aggregations over all elements in the group.  

Since
    
3.0.0
  24. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#agg\[U1,U2,U3,U4\]\(col1:org.apache.spark.sql.TypedColumn\[V,U1\],col2:org.apache.spark.sql.TypedColumn\[V,U2\],col3:org.apache.spark.sql.TypedColumn\[V,U3\],col4:org.apache.spark.sql.TypedColumn\[V,U4\]\):org.apache.spark.sql.Dataset\[\(K,U1,U2,U3,U4\)\] "Permalink") def agg[U1, U2, U3, U4](col1: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[V, U1], col2: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[V, U2], col3: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[V, U3], col4: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[V, U4]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[(K, U1, U2, U3, U4)]
Computes the given aggregations, returning a [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") of tuples for each unique key and the result of computing these aggregations over all elements in the group.
Computes the given aggregations, returning a [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") of tuples for each unique key and the result of computing these aggregations over all elements in the group.  

Since
    
1.6.0
  25. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#agg\[U1,U2,U3\]\(col1:org.apache.spark.sql.TypedColumn\[V,U1\],col2:org.apache.spark.sql.TypedColumn\[V,U2\],col3:org.apache.spark.sql.TypedColumn\[V,U3\]\):org.apache.spark.sql.Dataset\[\(K,U1,U2,U3\)\] "Permalink") def agg[U1, U2, U3](col1: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[V, U1], col2: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[V, U2], col3: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[V, U3]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[(K, U1, U2, U3)]
Computes the given aggregations, returning a [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") of tuples for each unique key and the result of computing these aggregations over all elements in the group.
Computes the given aggregations, returning a [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") of tuples for each unique key and the result of computing these aggregations over all elements in the group.  

Since
    
1.6.0
  26. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#agg\[U1,U2\]\(col1:org.apache.spark.sql.TypedColumn\[V,U1\],col2:org.apache.spark.sql.TypedColumn\[V,U2\]\):org.apache.spark.sql.Dataset\[\(K,U1,U2\)\] "Permalink") def agg[U1, U2](col1: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[V, U1], col2: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[V, U2]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[(K, U1, U2)]
Computes the given aggregations, returning a [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") of tuples for each unique key and the result of computing these aggregations over all elements in the group.
Computes the given aggregations, returning a [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") of tuples for each unique key and the result of computing these aggregations over all elements in the group.  

Since
    
1.6.0
  27. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#agg\[U1\]\(col1:org.apache.spark.sql.TypedColumn\[V,U1\]\):org.apache.spark.sql.Dataset\[\(K,U1\)\] "Permalink") def agg[U1](col1: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[V, U1]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[(K, U1)]
Computes the given aggregation, returning a [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") of tuples for each unique key and the result of computing this aggregation over all elements in the group.
Computes the given aggregation, returning a [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") of tuples for each unique key and the result of computing this aggregation over all elements in the group.  

Since
    
1.6.0
  28. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0 

Definition Classes
    Any
  29. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#clone\(\):Object "Permalink") def clone(): AnyRef 

Attributes
    protected[lang]  

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  30. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#cogroup\[U,R\]\(other:org.apache.spark.sql.KeyValueGroupedDataset\[K,U\],f:org.apache.spark.api.java.function.CoGroupFunction\[K,V,U,R\],encoder:org.apache.spark.sql.Encoder\[R\]\):org.apache.spark.sql.Dataset\[R\] "Permalink") def cogroup[U, R](other: [KeyValueGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html "org.apache.spark.sql.KeyValueGroupedDataset")[K, U], f: [CoGroupFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/CoGroupFunction.html "org.apache.spark.api.java.function.CoGroupFunction")[K, V, U, R], encoder: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[R]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[R]
(Java-specific) Applies the given function to each cogrouped data.
(Java-specific) Applies the given function to each cogrouped data. For each unique group, the function will be passed the grouping key and 2 iterators containing all elements in the group from [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") `this` and `other`. The function can return an iterator containing elements of an arbitrary type which will be returned as a new [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset").  

Since
    
1.6.0
  31. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#cogroup\[U,R\]\(other:org.apache.spark.sql.KeyValueGroupedDataset\[K,U\]\)\(f:\(K,Iterator\[V\],Iterator\[U\]\)=>IterableOnce\[R\]\)\(implicitevidence$28:org.apache.spark.sql.Encoder\[R\]\):org.apache.spark.sql.Dataset\[R\] "Permalink") def cogroup[U, R](other: [KeyValueGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html "org.apache.spark.sql.KeyValueGroupedDataset")[K, U])(f: (K, Iterator[V], Iterator[U]) => IterableOnce[R])(implicit arg0: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[R]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[R]
(Scala-specific) Applies the given function to each cogrouped data.
(Scala-specific) Applies the given function to each cogrouped data. For each unique group, the function will be passed the grouping key and 2 iterators containing all elements in the group from [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") `this` and `other`. The function can return an iterator containing elements of an arbitrary type which will be returned as a new [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset").  

Since
    
1.6.0
  32. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#cogroupSorted\[U,R\]\(other:org.apache.spark.sql.KeyValueGroupedDataset\[K,U\],thisSortExprs:Array\[org.apache.spark.sql.Column\],otherSortExprs:Array\[org.apache.spark.sql.Column\],f:org.apache.spark.api.java.function.CoGroupFunction\[K,V,U,R\],encoder:org.apache.spark.sql.Encoder\[R\]\):org.apache.spark.sql.Dataset\[R\] "Permalink") def cogroupSorted[U, R](other: [KeyValueGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html "org.apache.spark.sql.KeyValueGroupedDataset")[K, U], thisSortExprs: Array[[Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")], otherSortExprs: Array[[Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")], f: [CoGroupFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/CoGroupFunction.html "org.apache.spark.api.java.function.CoGroupFunction")[K, V, U, R], encoder: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[R]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[R]
(Java-specific) Applies the given function to each sorted cogrouped data.
(Java-specific) Applies the given function to each sorted cogrouped data. For each unique group, the function will be passed the grouping key and 2 sorted iterators containing all elements in the group from [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") `this` and `other`. The function can return an iterator containing elements of an arbitrary type which will be returned as a new [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset").
This is equivalent to [KeyValueGroupedDataset#cogroup](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#cogroup\[U,R\]\(other:org.apache.spark.sql.KeyValueGroupedDataset\[K,U\],f:org.apache.spark.api.java.function.CoGroupFunction\[K,V,U,R\],encoder:org.apache.spark.sql.Encoder\[R\]\):org.apache.spark.sql.Dataset\[R\]), except for the iterators to be sorted according to the given sort expressions. That sorting does not add computational complexity.  

Since
    
3.4.0 

See also
    
`org.apache.spark.sql.api.KeyValueGroupedDataset#cogroup`
  33. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#count\(\):org.apache.spark.sql.Dataset\[\(K,Long\)\] "Permalink") def count(): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[(K, Long)]
Returns a [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") that contains a tuple with each key and the number of items present for that key.
Returns a [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") that contains a tuple with each key and the number of items present for that key.  

Since
    
1.6.0
  34. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  35. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#equals\(x$1:Object\):Boolean "Permalink") def equals(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef → Any
  36. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#flatMapGroups\[U\]\(f:org.apache.spark.api.java.function.FlatMapGroupsFunction\[K,V,U\],encoder:org.apache.spark.sql.Encoder\[U\]\):org.apache.spark.sql.Dataset\[U\] "Permalink") def flatMapGroups[U](f: [FlatMapGroupsFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapGroupsFunction.html "org.apache.spark.api.java.function.FlatMapGroupsFunction")[K, V, U], encoder: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[U]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[U]
(Java-specific) Applies the given function to each group of data.
(Java-specific) Applies the given function to each group of data. For each unique group, the function will be passed the group key and an iterator that contains all of the elements in the group. The function can return an iterator containing elements of an arbitrary type which will be returned as a new [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset").
This function does not support partial aggregation, and as a result requires shuffling all the data in the [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset"). If an application intends to perform an aggregation over each key, it is best to use the reduce function or an `org.apache.spark.sql.expressions#Aggregator`.
Internally, the implementation will spill to disk if any given group is too large to fit into memory. However, users must take care to avoid materializing the whole iterator for a group (for example, by calling `toList`) unless they are sure that this is possible given the memory constraints of their cluster.  

Since
    
1.6.0
  37. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#flatMapGroups\[U\]\(f:\(K,Iterator\[V\]\)=>IterableOnce\[U\]\)\(implicitevidence$3:org.apache.spark.sql.Encoder\[U\]\):org.apache.spark.sql.Dataset\[U\] "Permalink") def flatMapGroups[U](f: (K, Iterator[V]) => IterableOnce[U])(implicit arg0: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[U]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[U]
(Scala-specific) Applies the given function to each group of data.
(Scala-specific) Applies the given function to each group of data. For each unique group, the function will be passed the group key and an iterator that contains all of the elements in the group. The function can return an iterator containing elements of an arbitrary type which will be returned as a new [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset").
This function does not support partial aggregation, and as a result requires shuffling all the data in the [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset"). If an application intends to perform an aggregation over each key, it is best to use the reduce function or an `org.apache.spark.sql.expressions#Aggregator`.
Internally, the implementation will spill to disk if any given group is too large to fit into memory. However, users must take care to avoid materializing the whole iterator for a group (for example, by calling `toList`) unless they are sure that this is possible given the memory constraints of their cluster.  

Since
    
1.6.0
  38. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#flatMapGroupsWithState\[S,U\]\(func:org.apache.spark.api.java.function.FlatMapGroupsWithStateFunction\[K,V,S,U\],outputMode:org.apache.spark.sql.streaming.OutputMode,stateEncoder:org.apache.spark.sql.Encoder\[S\],outputEncoder:org.apache.spark.sql.Encoder\[U\],timeoutConf:org.apache.spark.sql.streaming.GroupStateTimeout,initialState:org.apache.spark.sql.KeyValueGroupedDataset\[K,S\]\):org.apache.spark.sql.Dataset\[U\] "Permalink") def flatMapGroupsWithState[S, U](func: [FlatMapGroupsWithStateFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapGroupsWithStateFunction.html "org.apache.spark.api.java.function.FlatMapGroupsWithStateFunction")[K, V, S, U], outputMode: [OutputMode](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/OutputMode.html "org.apache.spark.sql.streaming.OutputMode"), stateEncoder: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[S], outputEncoder: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[U], timeoutConf: [GroupStateTimeout](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/GroupStateTimeout.html "org.apache.spark.sql.streaming.GroupStateTimeout"), initialState: [KeyValueGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html "org.apache.spark.sql.KeyValueGroupedDataset")[K, S]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[U]
(Java-specific) Applies the given function to each group of data, while maintaining a user-defined per-group state.
(Java-specific) Applies the given function to each group of data, while maintaining a user-defined per-group state. The result Dataset will represent the objects returned by the function. For a static batch Dataset, the function will be invoked once per group. For a streaming Dataset, the function will be invoked for each group repeatedly in every trigger, and updates to each group's state will be saved across invocations. See `GroupState` for more details.  

S
    
The type of the user-defined state. Must be encodable to Spark SQL types. 

U
    
The type of the output objects. Must be encodable to Spark SQL types. 

func
    
Function to be called on every group. 

outputMode
    
The output mode of the function. 

stateEncoder
    
Encoder for the state type. 

outputEncoder
    
Encoder for the output type. 

timeoutConf
    
Timeout configuration for groups that do not receive data for a while. 

initialState
    
The user provided state that will be initialized when the first batch of data is processed in the streaming query. The user defined function will be called on the state data even if there are no other values in the group. To covert a Dataset `ds` of type of type `Dataset[(K, S)]` to a `KeyValueGroupedDataset[K, S]`, use

```
ds.groupByKey(x => x._1).mapValues(_._2)
```

See [org.apache.spark.sql.Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder") for more details on what types are encodable to Spark SQL. 

Since
    
3.2.0
  39. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#flatMapGroupsWithState\[S,U\]\(func:org.apache.spark.api.java.function.FlatMapGroupsWithStateFunction\[K,V,S,U\],outputMode:org.apache.spark.sql.streaming.OutputMode,stateEncoder:org.apache.spark.sql.Encoder\[S\],outputEncoder:org.apache.spark.sql.Encoder\[U\],timeoutConf:org.apache.spark.sql.streaming.GroupStateTimeout\):org.apache.spark.sql.Dataset\[U\] "Permalink") def flatMapGroupsWithState[S, U](func: [FlatMapGroupsWithStateFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapGroupsWithStateFunction.html "org.apache.spark.api.java.function.FlatMapGroupsWithStateFunction")[K, V, S, U], outputMode: [OutputMode](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/OutputMode.html "org.apache.spark.sql.streaming.OutputMode"), stateEncoder: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[S], outputEncoder: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[U], timeoutConf: [GroupStateTimeout](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/GroupStateTimeout.html "org.apache.spark.sql.streaming.GroupStateTimeout")): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[U]
(Java-specific) Applies the given function to each group of data, while maintaining a user-defined per-group state.
(Java-specific) Applies the given function to each group of data, while maintaining a user-defined per-group state. The result Dataset will represent the objects returned by the function. For a static batch Dataset, the function will be invoked once per group. For a streaming Dataset, the function will be invoked for each group repeatedly in every trigger, and updates to each group's state will be saved across invocations. See `GroupState` for more details.  

S
    
The type of the user-defined state. Must be encodable to Spark SQL types. 

U
    
The type of the output objects. Must be encodable to Spark SQL types. 

func
    
Function to be called on every group. 

outputMode
    
The output mode of the function. 

stateEncoder
    
Encoder for the state type. 

outputEncoder
    
Encoder for the output type. 

timeoutConf
    
Timeout configuration for groups that do not receive data for a while. See [org.apache.spark.sql.Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder") for more details on what types are encodable to Spark SQL. 

Since
    
2.2.0
  40. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#flatMapSortedGroups\[U\]\(SortExprs:Array\[org.apache.spark.sql.Column\],f:org.apache.spark.api.java.function.FlatMapGroupsFunction\[K,V,U\],encoder:org.apache.spark.sql.Encoder\[U\]\):org.apache.spark.sql.Dataset\[U\] "Permalink") def flatMapSortedGroups[U](SortExprs: Array[[Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")], f: [FlatMapGroupsFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapGroupsFunction.html "org.apache.spark.api.java.function.FlatMapGroupsFunction")[K, V, U], encoder: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[U]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[U]
(Java-specific) Applies the given function to each group of data.
(Java-specific) Applies the given function to each group of data. For each unique group, the function will be passed the group key and a sorted iterator that contains all of the elements in the group. The function can return an iterator containing elements of an arbitrary type which will be returned as a new [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset").
This function does not support partial aggregation, and as a result requires shuffling all the data in the [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset"). If an application intends to perform an aggregation over each key, it is best to use the reduce function or an `org.apache.spark.sql.expressions#Aggregator`.
Internally, the implementation will spill to disk if any given group is too large to fit into memory. However, users must take care to avoid materializing the whole iterator for a group (for example, by calling `toList`) unless they are sure that this is possible given the memory constraints of their cluster.
This is equivalent to [KeyValueGroupedDataset#flatMapGroups](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#flatMapGroups\[U\]\(f:org.apache.spark.api.java.function.FlatMapGroupsFunction\[K,V,U\],encoder:org.apache.spark.sql.Encoder\[U\]\):org.apache.spark.sql.Dataset\[U\]), except for the iterator to be sorted according to the given sort expressions. That sorting does not add computational complexity.  

Since
    
3.4.0 

See also
    
`org.apache.spark.sql.api.KeyValueGroupedDataset#flatMapGroups`
  41. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef] 

Definition Classes
    AnyRef → Any 

Annotations
     @IntrinsicCandidate() @native()
  42. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#hashCode\(\):Int "Permalink") def hashCode(): Int 

Definition Classes
    AnyRef → Any 

Annotations
     @IntrinsicCandidate() @native()
  43. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean 

Definition Classes
    Any
  44. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#mapGroups\[U\]\(f:org.apache.spark.api.java.function.MapGroupsFunction\[K,V,U\],encoder:org.apache.spark.sql.Encoder\[U\]\):org.apache.spark.sql.Dataset\[U\] "Permalink") def mapGroups[U](f: [MapGroupsFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/MapGroupsFunction.html "org.apache.spark.api.java.function.MapGroupsFunction")[K, V, U], encoder: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[U]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[U]
(Java-specific) Applies the given function to each group of data.
(Java-specific) Applies the given function to each group of data. For each unique group, the function will be passed the group key and an iterator that contains all of the elements in the group. The function can return an element of arbitrary type which will be returned as a new [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset").
This function does not support partial aggregation, and as a result requires shuffling all the data in the [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset"). If an application intends to perform an aggregation over each key, it is best to use the reduce function or an `org.apache.spark.sql.expressions#Aggregator`.
Internally, the implementation will spill to disk if any given group is too large to fit into memory. However, users must take care to avoid materializing the whole iterator for a group (for example, by calling `toList`) unless they are sure that this is possible given the memory constraints of their cluster.  

Since
    
1.6.0
  45. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#mapGroups\[U\]\(f:\(K,Iterator\[V\]\)=>U\)\(implicitevidence$5:org.apache.spark.sql.Encoder\[U\]\):org.apache.spark.sql.Dataset\[U\] "Permalink") def mapGroups[U](f: (K, Iterator[V]) => U)(implicit arg0: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[U]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[U]
(Scala-specific) Applies the given function to each group of data.
(Scala-specific) Applies the given function to each group of data. For each unique group, the function will be passed the group key and an iterator that contains all of the elements in the group. The function can return an element of arbitrary type which will be returned as a new [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset").
This function does not support partial aggregation, and as a result requires shuffling all the data in the [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset"). If an application intends to perform an aggregation over each key, it is best to use the reduce function or an `org.apache.spark.sql.expressions#Aggregator`.
Internally, the implementation will spill to disk if any given group is too large to fit into memory. However, users must take care to avoid materializing the whole iterator for a group (for example, by calling `toList`) unless they are sure that this is possible given the memory constraints of their cluster.  

Since
    
1.6.0
  46. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#mapGroupsWithState\[S,U\]\(func:org.apache.spark.api.java.function.MapGroupsWithStateFunction\[K,V,S,U\],stateEncoder:org.apache.spark.sql.Encoder\[S\],outputEncoder:org.apache.spark.sql.Encoder\[U\],timeoutConf:org.apache.spark.sql.streaming.GroupStateTimeout,initialState:org.apache.spark.sql.KeyValueGroupedDataset\[K,S\]\):org.apache.spark.sql.Dataset\[U\] "Permalink") def mapGroupsWithState[S, U](func: [MapGroupsWithStateFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/MapGroupsWithStateFunction.html "org.apache.spark.api.java.function.MapGroupsWithStateFunction")[K, V, S, U], stateEncoder: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[S], outputEncoder: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[U], timeoutConf: [GroupStateTimeout](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/GroupStateTimeout.html "org.apache.spark.sql.streaming.GroupStateTimeout"), initialState: [KeyValueGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html "org.apache.spark.sql.KeyValueGroupedDataset")[K, S]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[U]
(Java-specific) Applies the given function to each group of data, while maintaining a user-defined per-group state.
(Java-specific) Applies the given function to each group of data, while maintaining a user-defined per-group state. The result Dataset will represent the objects returned by the function. For a static batch Dataset, the function will be invoked once per group. For a streaming Dataset, the function will be invoked for each group repeatedly in every trigger, and updates to each group's state will be saved across invocations. See `GroupState` for more details.  

S
    
The type of the user-defined state. Must be encodable to Spark SQL types. 

U
    
The type of the output objects. Must be encodable to Spark SQL types. 

func
    
Function to be called on every group. 

stateEncoder
    
Encoder for the state type. 

outputEncoder
    
Encoder for the output type. 

timeoutConf
    
Timeout configuration for groups that do not receive data for a while. 

initialState
    
The user provided state that will be initialized when the first batch of data is processed in the streaming query. The user defined function will be called on the state data even if there are no other values in the group. See [org.apache.spark.sql.Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder") for more details on what types are encodable to Spark SQL. 

Since
    
3.2.0
  47. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#mapGroupsWithState\[S,U\]\(func:org.apache.spark.api.java.function.MapGroupsWithStateFunction\[K,V,S,U\],stateEncoder:org.apache.spark.sql.Encoder\[S\],outputEncoder:org.apache.spark.sql.Encoder\[U\],timeoutConf:org.apache.spark.sql.streaming.GroupStateTimeout\):org.apache.spark.sql.Dataset\[U\] "Permalink") def mapGroupsWithState[S, U](func: [MapGroupsWithStateFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/MapGroupsWithStateFunction.html "org.apache.spark.api.java.function.MapGroupsWithStateFunction")[K, V, S, U], stateEncoder: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[S], outputEncoder: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[U], timeoutConf: [GroupStateTimeout](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/GroupStateTimeout.html "org.apache.spark.sql.streaming.GroupStateTimeout")): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[U]
(Java-specific) Applies the given function to each group of data, while maintaining a user-defined per-group state.
(Java-specific) Applies the given function to each group of data, while maintaining a user-defined per-group state. The result Dataset will represent the objects returned by the function. For a static batch Dataset, the function will be invoked once per group. For a streaming Dataset, the function will be invoked for each group repeatedly in every trigger, and updates to each group's state will be saved across invocations. See `GroupState` for more details.  

S
    
The type of the user-defined state. Must be encodable to Spark SQL types. 

U
    
The type of the output objects. Must be encodable to Spark SQL types. 

func
    
Function to be called on every group. 

stateEncoder
    
Encoder for the state type. 

outputEncoder
    
Encoder for the output type. 

timeoutConf
    
Timeout configuration for groups that do not receive data for a while. See [org.apache.spark.sql.Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder") for more details on what types are encodable to Spark SQL. 

Since
    
2.2.0
  48. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#mapGroupsWithState\[S,U\]\(func:org.apache.spark.api.java.function.MapGroupsWithStateFunction\[K,V,S,U\],stateEncoder:org.apache.spark.sql.Encoder\[S\],outputEncoder:org.apache.spark.sql.Encoder\[U\]\):org.apache.spark.sql.Dataset\[U\] "Permalink") def mapGroupsWithState[S, U](func: [MapGroupsWithStateFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/MapGroupsWithStateFunction.html "org.apache.spark.api.java.function.MapGroupsWithStateFunction")[K, V, S, U], stateEncoder: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[S], outputEncoder: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[U]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[U]
(Java-specific) Applies the given function to each group of data, while maintaining a user-defined per-group state.
(Java-specific) Applies the given function to each group of data, while maintaining a user-defined per-group state. The result Dataset will represent the objects returned by the function. For a static batch Dataset, the function will be invoked once per group. For a streaming Dataset, the function will be invoked for each group repeatedly in every trigger, and updates to each group's state will be saved across invocations. See `GroupState` for more details.  

S
    
The type of the user-defined state. Must be encodable to Spark SQL types. 

U
    
The type of the output objects. Must be encodable to Spark SQL types. 

func
    
Function to be called on every group. 

stateEncoder
    
Encoder for the state type. 

outputEncoder
    
Encoder for the output type. See [org.apache.spark.sql.Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder") for more details on what types are encodable to Spark SQL. 

Since
    
2.2.0
  49. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#mapValues\[W\]\(func:org.apache.spark.api.java.function.MapFunction\[V,W\],encoder:org.apache.spark.sql.Encoder\[W\]\):org.apache.spark.sql.KeyValueGroupedDataset\[K,W\] "Permalink") def mapValues[W](func: [MapFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/MapFunction.html "org.apache.spark.api.java.function.MapFunction")[V, W], encoder: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[W]): [KeyValueGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html "org.apache.spark.sql.KeyValueGroupedDataset")[K, W]
Returns a new [KeyValueGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html "org.apache.spark.sql.KeyValueGroupedDataset") where the given function `func` has been applied to the data.
Returns a new [KeyValueGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html "org.apache.spark.sql.KeyValueGroupedDataset") where the given function `func` has been applied to the data. The grouping key is unchanged by this.

```
// Create Integer values grouped by String key from a Dataset<Tuple2<String, Integer>>
Dataset<Tuple2<String, Integer>> ds = ...;
KeyValueGroupedDataset<String, Integer> grouped =
  ds.groupByKey(t -> t._1, Encoders.STRING()).mapValues(t -> t._2, Encoders.INT());
```


Since
    
2.1.0
  50. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  51. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#notify\(\):Unit "Permalink") final  def notify(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  52. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  53. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#reduceGroups\(f:org.apache.spark.api.java.function.ReduceFunction\[V\]\):org.apache.spark.sql.Dataset\[\(K,V\)\] "Permalink") def reduceGroups(f: [ReduceFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/ReduceFunction.html "org.apache.spark.api.java.function.ReduceFunction")[V]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[(K, V)]
(Java-specific) Reduces the elements of each group of data using the specified binary function.
(Java-specific) Reduces the elements of each group of data using the specified binary function. The given function must be commutative and associative or the result may be non-deterministic.  

Since
    
1.6.0
  54. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0 

Definition Classes
    AnyRef
  55. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#toString\(\):String "Permalink") def toString(): [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String") 

Definition Classes
    AnyRef → Any
  56. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#transformWithState\[U,S\]\(statefulProcessor:org.apache.spark.sql.streaming.StatefulProcessorWithInitialState\[K,V,U,S\],outputMode:org.apache.spark.sql.streaming.OutputMode,initialState:org.apache.spark.sql.KeyValueGroupedDataset\[K,S\],eventTimeColumnName:String,outputEncoder:org.apache.spark.sql.Encoder\[U\],initialStateEncoder:org.apache.spark.sql.Encoder\[S\]\)\(implicitevidence$26:org.apache.spark.sql.Encoder\[U\],implicitevidence$27:org.apache.spark.sql.Encoder\[S\]\):org.apache.spark.sql.Dataset\[U\] "Permalink") def transformWithState[U, S](statefulProcessor: [StatefulProcessorWithInitialState](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StatefulProcessorWithInitialState.html "org.apache.spark.sql.streaming.StatefulProcessorWithInitialState")[K, V, U, S], outputMode: [OutputMode](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/OutputMode.html "org.apache.spark.sql.streaming.OutputMode"), initialState: [KeyValueGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html "org.apache.spark.sql.KeyValueGroupedDataset")[K, S], eventTimeColumnName: String, outputEncoder: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[U], initialStateEncoder: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[S])(implicit arg0: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[U], arg1: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[S]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[U]
(Java-specific) Invokes methods defined in the stateful processor used in arbitrary state API v2.
(Java-specific) Invokes methods defined in the stateful processor used in arbitrary state API v2. Functions as the function above, but with additional eventTimeColumnName for output.
Downstream operators would use specified eventTimeColumnName to calculate watermark. Note that TimeMode is set to EventTime to ensure correct flow of watermark.  

U
    
The type of the output objects. Must be encodable to Spark SQL types. 

S
    
The type of initial state objects. Must be encodable to Spark SQL types. 

statefulProcessor
    
Instance of statefulProcessor whose functions will be invoked by the operator. 

outputMode
    
The output mode of the stateful processor. 

initialState
    
User provided initial state that will be used to initiate state for the query in the first batch. 

eventTimeColumnName
    
event column in the output dataset. Any operations after transformWithState will use the new eventTimeColumn. The user needs to ensure that the eventTime for emitted output adheres to the watermark boundary, otherwise streaming query will fail. 

outputEncoder
    
Encoder for the output type. 

initialStateEncoder
    
Encoder for the initial state type. See [org.apache.spark.sql.Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder") for more details on what types are encodable to Spark SQL.
  57. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#transformWithState\[U,S\]\(statefulProcessor:org.apache.spark.sql.streaming.StatefulProcessorWithInitialState\[K,V,U,S\],timeMode:org.apache.spark.sql.streaming.TimeMode,outputMode:org.apache.spark.sql.streaming.OutputMode,initialState:org.apache.spark.sql.KeyValueGroupedDataset\[K,S\],outputEncoder:org.apache.spark.sql.Encoder\[U\],initialStateEncoder:org.apache.spark.sql.Encoder\[S\]\)\(implicitevidence$24:org.apache.spark.sql.Encoder\[U\],implicitevidence$25:org.apache.spark.sql.Encoder\[S\]\):org.apache.spark.sql.Dataset\[U\] "Permalink") def transformWithState[U, S](statefulProcessor: [StatefulProcessorWithInitialState](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StatefulProcessorWithInitialState.html "org.apache.spark.sql.streaming.StatefulProcessorWithInitialState")[K, V, U, S], timeMode: [TimeMode](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/TimeMode.html "org.apache.spark.sql.streaming.TimeMode"), outputMode: [OutputMode](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/OutputMode.html "org.apache.spark.sql.streaming.OutputMode"), initialState: [KeyValueGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html "org.apache.spark.sql.KeyValueGroupedDataset")[K, S], outputEncoder: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[U], initialStateEncoder: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[S])(implicit arg0: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[U], arg1: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[S]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[U]
(Java-specific) Invokes methods defined in the stateful processor used in arbitrary state API v2.
(Java-specific) Invokes methods defined in the stateful processor used in arbitrary state API v2. Functions as the function above, but with additional initialStateEncoder for state encoding.  

U
    
The type of the output objects. Must be encodable to Spark SQL types. 

S
    
The type of initial state objects. Must be encodable to Spark SQL types. 

statefulProcessor
    
Instance of statefulProcessor whose functions will be invoked by the operator. 

timeMode
    
The time mode semantics of the stateful processor for timers and TTL. 

outputMode
    
The output mode of the stateful processor. 

initialState
    
User provided initial state that will be used to initiate state for the query in the first batch. 

outputEncoder
    
Encoder for the output type. 

initialStateEncoder
    
Encoder for the initial state type. See [org.apache.spark.sql.Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder") for more details on what types are encodable to Spark SQL.
  58. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#transformWithState\[U\]\(statefulProcessor:org.apache.spark.sql.streaming.StatefulProcessor\[K,V,U\],eventTimeColumnName:String,outputMode:org.apache.spark.sql.streaming.OutputMode,outputEncoder:org.apache.spark.sql.Encoder\[U\]\)\(implicitevidence$19:org.apache.spark.sql.Encoder\[U\]\):org.apache.spark.sql.Dataset\[U\] "Permalink") def transformWithState[U](statefulProcessor: [StatefulProcessor](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StatefulProcessor.html "org.apache.spark.sql.streaming.StatefulProcessor")[K, V, U], eventTimeColumnName: String, outputMode: [OutputMode](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/OutputMode.html "org.apache.spark.sql.streaming.OutputMode"), outputEncoder: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[U])(implicit arg0: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[U]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[U]
(Java-specific) Invokes methods defined in the stateful processor used in arbitrary state API v2.
(Java-specific) Invokes methods defined in the stateful processor used in arbitrary state API v2. We allow the user to act on per-group set of input rows along with keyed state and the user can choose to output/return 0 or more rows.
For a streaming dataframe, we will repeatedly invoke the interface methods for new rows in each trigger and the user's state/state variables will be stored persistently across invocations.
Downstream operators would use specified eventTimeColumnName to calculate watermark. Note that TimeMode is set to EventTime to ensure correct flow of watermark.  

U
    
The type of the output objects. Must be encodable to Spark SQL types. 

statefulProcessor
    
Instance of statefulProcessor whose functions will be invoked by the operator. 

eventTimeColumnName
    
eventTime column in the output dataset. Any operations after transformWithState will use the new eventTimeColumn. The user needs to ensure that the eventTime for emitted output adheres to the watermark boundary, otherwise streaming query will fail. 

outputMode
    
The output mode of the stateful processor. 

outputEncoder
    
Encoder for the output type. See [org.apache.spark.sql.Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder") for more details on what types are encodable to Spark SQL.
  59. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#transformWithState\[U\]\(statefulProcessor:org.apache.spark.sql.streaming.StatefulProcessor\[K,V,U\],timeMode:org.apache.spark.sql.streaming.TimeMode,outputMode:org.apache.spark.sql.streaming.OutputMode,outputEncoder:org.apache.spark.sql.Encoder\[U\]\)\(implicitevidence$18:org.apache.spark.sql.Encoder\[U\]\):org.apache.spark.sql.Dataset\[U\] "Permalink") def transformWithState[U](statefulProcessor: [StatefulProcessor](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/StatefulProcessor.html "org.apache.spark.sql.streaming.StatefulProcessor")[K, V, U], timeMode: [TimeMode](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/TimeMode.html "org.apache.spark.sql.streaming.TimeMode"), outputMode: [OutputMode](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/OutputMode.html "org.apache.spark.sql.streaming.OutputMode"), outputEncoder: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[U])(implicit arg0: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[U]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[U]
(Java-specific) Invokes methods defined in the stateful processor used in arbitrary state API v2.
(Java-specific) Invokes methods defined in the stateful processor used in arbitrary state API v2. We allow the user to act on per-group set of input rows along with keyed state and the user can choose to output/return 0 or more rows. For a streaming dataframe, we will repeatedly invoke the interface methods for new rows in each trigger and the user's state/state variables will be stored persistently across invocations.  

U
    
The type of the output objects. Must be encodable to Spark SQL types. 

statefulProcessor
    
Instance of statefulProcessor whose functions will be invoked by the operator. 

timeMode
    
The time mode semantics of the stateful processor for timers and TTL. 

outputMode
    
The output mode of the stateful processor. 

outputEncoder
    
Encoder for the output type. See [org.apache.spark.sql.Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder") for more details on what types are encodable to Spark SQL.
  60. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  61. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  62. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#wait\(\):Unit "Permalink") final  def wait(): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  63. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html#finalize\(\):Unit "Permalink") def finalize(): Unit 

Attributes
    protected[lang]  

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.Throwable]) @Deprecated 

Deprecated
    
_(Since version 9)_


