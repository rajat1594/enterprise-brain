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
# Dataset[ __](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "Permalink")
####  abstract  class Dataset[T] extends Serializable
A Dataset is a strongly typed collection of domain-specific objects that can be transformed in parallel using functional or relational operations. Each Dataset also has an untyped view called a `DataFrame`, which is a Dataset of [org.apache.spark.sql.Row](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Row.html "org.apache.spark.sql.Row").
Operations available on Datasets are divided into transformations and actions. Transformations are the ones that produce new Datasets, and actions are the ones that trigger computation and return results. Example transformations include map, filter, select, and aggregate (`groupBy`). Example actions count, show, or writing data out to file systems.
Datasets are "lazy", i.e. computations are only triggered when an action is invoked. Internally, a Dataset represents a logical plan that describes the computation required to produce the data. When an action is invoked, Spark's query optimizer optimizes the logical plan and generates a physical plan for efficient execution in a parallel and distributed manner. To explore the logical plan as well as optimized physical plan, use the `explain` function.
To efficiently support domain-specific objects, an [org.apache.spark.sql.Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder") is required. The encoder maps the domain specific type `T` to Spark's internal type system. For example, given a class `Person` with two fields, `name` (string) and `age` (int), an encoder is used to tell Spark to generate code at runtime to serialize the `Person` object into a binary structure. This binary structure often has much lower memory footprint as well as are optimized for efficiency in data processing (e.g. in a columnar format). To understand the internal binary representation for data, use the `schema` function.
There are typically two ways to create a Dataset. The most common way is by pointing Spark to some files on storage systems, using the `read` function available on a `SparkSession`.

```
val people = spark.read.parquet("...").as[Person]  // Scala
Dataset<Person> people = spark.read().parquet("...").as(Encoders.bean(Person.class)); // Java
```

Datasets can also be created through transformations available on existing Datasets. For example, the following creates a new Dataset by applying a filter on the existing one:

```
val names = people.map(_.name)  // in Scala; names is a Dataset[String]
Dataset<String> names = people.map(
  (MapFunction<Person, String>) p -> p.name, Encoders.STRING()); // Java
```

Dataset operations can also be untyped, through various domain-specific-language (DSL) functions defined in: Dataset (this class), [org.apache.spark.sql.Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column"), and [org.apache.spark.sql.functions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/functions$.html "org.apache.spark.sql.functions"). These operations are very similar to the operations available in the data frame abstraction in R or Python.
To select a column from the Dataset, use `apply` method in Scala and `col` in Java.

```
val ageCol = people("age")  // in Scala
Column ageCol = people.col("age"); // in Java
```

Note that the [org.apache.spark.sql.Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column") type can also be manipulated through its various functions.

```
// The following creates a new column that increases everybody's age by 10.
people("age") + 10  // in Scala
people.col("age").plus(10);  // in Java
```

A more concrete example in Scala:

```
// To create Dataset[Row] using SparkSession
val people = spark.read.parquet("...")
val department = spark.read.parquet("...")

people.filter("age > 30")
  .join(department, people("deptId") === department("id"))
  .groupBy(department("name"), people("gender"))
  .agg(avg(people("salary")), max(people("age")))
```

and in Java:

```
// To create Dataset<Row> using SparkSession
Dataset<Row> people = spark.read().parquet("...");
Dataset<Row> department = spark.read().parquet("...");

people.filter(people.col("age").gt(30))
  .join(department, people.col("deptId").equalTo(department.col("id")))
  .groupBy(department.col("name"), people.col("gender"))
  .agg(avg(people.col("salary")), max(people.col("age")));
```


Annotations
     @Stable() 

Source
    [Dataset.scala](https://github.com/apache/spark/tree/v4.1.2/sql/api/src/main/scala/org/apache/spark/sql/Dataset.scala) 

Since
    
1.6.0
Linear Supertypes
[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable"), AnyRef, Any
__ __
Ordering
  1. Grouped
  2. Alphabetic
  3. By Inheritance


Inherited  

  1. Dataset
  2. Serializable
  3. AnyRef
  4. Any


  1. Hide All
  2. Show All


Visibility
  1. Public
  2. Protected


### Instance Constructors
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#<init>\(\):org.apache.spark.sql.Dataset\[T\] "Permalink") new Dataset()


### Abstract Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#as\(alias:String\):org.apache.spark.sql.Dataset\[T\] "Permalink") abstract  def as(alias: String): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Returns a new Dataset with an alias set.
Returns a new Dataset with an alias set.  

Since
    
1.6.0
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#as\[U\]\(implicitevidence$1:org.apache.spark.sql.Encoder\[U\]\):org.apache.spark.sql.Dataset\[U\] "Permalink") abstract  def as[U](implicit arg0: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[U]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[U]
Returns a new Dataset where each record has been mapped on to the specified type.
Returns a new Dataset where each record has been mapped on to the specified type. The method used to map columns depend on the type of `U`:
     * When `U` is a class, fields for the class will be mapped to columns of the same name (case sensitivity is determined by `spark.sql.caseSensitive`).
     * When `U` is a tuple, the columns will be mapped by ordinal (i.e. the first column will be assigned to `_1`).
     * When `U` is a primitive type (i.e. String, Int, etc), then the first column of the `DataFrame` will be used.
If the schema of the Dataset does not match the desired `U` type, you can use `select` along with `alias` or `as` to rearrange or rename as required.
Note that `as[]` only changes the view of the data that is passed into typed operations, such as `map()`, and does not eagerly project away any columns that are not present in the specified class.  

Since
    
1.6.0
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#cache\(\):org.apache.spark.sql.Dataset\[T\] "Permalink") abstract  def cache(): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Persist this Dataset with the default storage level (`MEMORY_AND_DISK`).
Persist this Dataset with the default storage level (`MEMORY_AND_DISK`).  

Since
    
1.6.0
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#checkpoint\(eager:Boolean,reliableCheckpoint:Boolean,storageLevel:Option\[org.apache.spark.storage.StorageLevel\]\):org.apache.spark.sql.Dataset\[T\] "Permalink") abstract  def checkpoint(eager: Boolean, reliableCheckpoint: Boolean, storageLevel: Option[[StorageLevel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StorageLevel.html "org.apache.spark.storage.StorageLevel")]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Returns a checkpointed version of this Dataset.
Returns a checkpointed version of this Dataset.  

eager
    
Whether to checkpoint this dataframe immediately 

reliableCheckpoint
    
Whether to create a reliable checkpoint saved to files inside the checkpoint directory. If false creates a local checkpoint using the caching subsystem 

storageLevel
    
Option. If defined, StorageLevel with which to checkpoint the data. Only with reliableCheckpoint = false. 

Attributes
    protected 
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#coalesce\(numPartitions:Int\):org.apache.spark.sql.Dataset\[T\] "Permalink") abstract  def coalesce(numPartitions: Int): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Returns a new Dataset that has exactly `numPartitions` partitions, when the fewer partitions are requested.
Returns a new Dataset that has exactly `numPartitions` partitions, when the fewer partitions are requested. If a larger number of partitions is requested, it will stay at the current number of partitions. Similar to coalesce defined on an `RDD`, this operation results in a narrow dependency, e.g. if you go from 1000 partitions to 100 partitions, there will not be a shuffle, instead each of the 100 new partitions will claim 10 of the current partitions.
However, if you're doing a drastic coalesce, e.g. to numPartitions = 1, this may result in your computation taking place on fewer nodes than you like (e.g. one node in the case of numPartitions = 1). To avoid this, you can call repartition. This will add a shuffle step, but means the current upstream partitions will be executed in parallel (per whatever the current partitioning is).  

Since
    
1.6.0
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#col\(colName:String\):org.apache.spark.sql.Column "Permalink") abstract  def col(colName: String): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Selects column based on the column name and returns it as a [org.apache.spark.sql.Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column").
Selects column based on the column name and returns it as a [org.apache.spark.sql.Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column").  

Since
    
2.0.0 

Note
    
The column name can also reference to a nested column like `a.b`.
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#colRegex\(colName:String\):org.apache.spark.sql.Column "Permalink") abstract  def colRegex(colName: String): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Selects column based on the column name specified as a regex and returns it as [org.apache.spark.sql.Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column").
Selects column based on the column name specified as a regex and returns it as [org.apache.spark.sql.Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column").  

Since
    
2.3.0
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#collect\(\):Array\[T\] "Permalink") abstract  def collect(): Array[T]
Returns an array that contains all rows in this Dataset.
Returns an array that contains all rows in this Dataset.
Running collect requires moving all the data into the application's driver process, and doing so on a very large dataset can crash the driver process with OutOfMemoryError.
For Java API, use [collectAsList](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#collectAsList\(\):java.util.List\[T\]).  

Since
    
1.6.0
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#collectAsList\(\):java.util.List\[T\] "Permalink") abstract  def collectAsList(): [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#java.util.List "java.util.List")[T]
Returns a Java list that contains all rows in this Dataset.
Returns a Java list that contains all rows in this Dataset.
Running collect requires moving all the data into the application's driver process, and doing so on a very large dataset can crash the driver process with OutOfMemoryError.  

Since
    
1.6.0
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#count\(\):Long "Permalink") abstract  def count(): Long
Returns the number of rows in the Dataset.
Returns the number of rows in the Dataset.  

Since
    
1.6.0
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#createTempView\(viewName:String,replace:Boolean,global:Boolean\):Unit "Permalink") abstract  def createTempView(viewName: String, replace: Boolean, global: Boolean): Unit 

Attributes
    protected 
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#crossJoin\(right:org.apache.spark.sql.Dataset\[_\]\):org.apache.spark.sql.DataFrame "Permalink") abstract  def crossJoin(right: [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[_]): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Explicit cartesian join with another `DataFrame`.
Explicit cartesian join with another `DataFrame`.  

right
    
Right side of the join operation. 

Since
    
2.1.0 

Note
    
Cartesian joins are very expensive without an extra filter that can be pushed down.
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#cube\(cols:org.apache.spark.sql.Column*\):org.apache.spark.sql.RelationalGroupedDataset "Permalink") abstract  def cube(cols: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")*): [RelationalGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/RelationalGroupedDataset.html "org.apache.spark.sql.RelationalGroupedDataset")
Create a multi-dimensional cube for the current Dataset using the specified columns, so we can run aggregation on them.
Create a multi-dimensional cube for the current Dataset using the specified columns, so we can run aggregation on them. See [RelationalGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/RelationalGroupedDataset.html "org.apache.spark.sql.RelationalGroupedDataset") for all the available aggregate functions.

```
// Compute the average for all numeric columns cubed by department and group.
ds.cube($"department", $"group").avg()

// Compute the max age and average salary, cubed by department and gender.
ds.cube($"department", $"gender").agg(Map(
  "salary" -> "avg",
  "age" -> "max"
))
```


Annotations
     @varargs() 

Since
    
2.0.0
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#describe\(cols:String*\):org.apache.spark.sql.DataFrame "Permalink") abstract  def describe(cols: String*): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Computes basic statistics for numeric and string columns, including count, mean, stddev, min, and max.
Computes basic statistics for numeric and string columns, including count, mean, stddev, min, and max. If no columns are given, this function computes statistics for all numerical or string columns.
This function is meant for exploratory data analysis, as we make no guarantee about the backward compatibility of the schema of the resulting Dataset. If you want to programmatically compute summary statistics, use the `agg` function instead.

```
ds.describe("age", "height").show()

// output:
// summary age   height
// count   10.0  10.0
// mean    53.3  178.05
// stddev  11.6  15.7
// min     18.0  163.0
// max     92.0  192.0
```

Use [summary](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#summary\(statistics:String*\):org.apache.spark.sql.DataFrame) for expanded statistics and control over which statistics to compute.  

cols
    
Columns to compute statistics on. 

Annotations
     @varargs() 

Since
    
1.6.0
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#drop\(col:org.apache.spark.sql.Column,cols:org.apache.spark.sql.Column*\):org.apache.spark.sql.DataFrame "Permalink") abstract  def drop(col: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column"), cols: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")*): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Returns a new Dataset with columns dropped.
Returns a new Dataset with columns dropped.
This method can only be used to drop top level columns. This is a no-op if the Dataset doesn't have a columns with an equivalent expression.  

Annotations
     @varargs() 

Since
    
3.4.0
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#drop\(colNames:String*\):org.apache.spark.sql.DataFrame "Permalink") abstract  def drop(colNames: String*): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Returns a new Dataset with columns dropped.
Returns a new Dataset with columns dropped. This is a no-op if schema doesn't contain column name(s).
This method can only be used to drop top level columns. the colName string is treated literally without further interpretation.  

Annotations
     @varargs() 

Since
    
2.0.0
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#dropDuplicates\(colNames:Seq\[String\]\):org.apache.spark.sql.Dataset\[T\] "Permalink") abstract  def dropDuplicates(colNames: Seq[String]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
(Scala-specific) Returns a new Dataset with duplicate rows removed, considering only the subset of columns.
(Scala-specific) Returns a new Dataset with duplicate rows removed, considering only the subset of columns.
For a static batch [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset"), it just drops duplicate rows. For a streaming [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset"), it will keep all data across triggers as intermediate state to drop duplicates rows. You can use [withWatermark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#withWatermark\(eventTime:String,delayThreshold:String\):org.apache.spark.sql.Dataset\[T\]) to limit how late the duplicate data can be and system will accordingly limit the state. In addition, too late data older than watermark will be dropped to avoid any possibility of duplicates.  

Since
    
2.0.0
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#dropDuplicates\(\):org.apache.spark.sql.Dataset\[T\] "Permalink") abstract  def dropDuplicates(): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Returns a new Dataset that contains only the unique rows from this Dataset.
Returns a new Dataset that contains only the unique rows from this Dataset. This is an alias for `distinct`.
For a static batch [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset"), it just drops duplicate rows. For a streaming [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset"), it will keep all data across triggers as intermediate state to drop duplicates rows. You can use [withWatermark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#withWatermark\(eventTime:String,delayThreshold:String\):org.apache.spark.sql.Dataset\[T\]) to limit how late the duplicate data can be and system will accordingly limit the state. In addition, too late data older than watermark will be dropped to avoid any possibility of duplicates.  

Since
    
2.0.0
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#dropDuplicatesWithinWatermark\(colNames:Seq\[String\]\):org.apache.spark.sql.Dataset\[T\] "Permalink") abstract  def dropDuplicatesWithinWatermark(colNames: Seq[String]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Returns a new Dataset with duplicates rows removed, considering only the subset of columns, within watermark.
Returns a new Dataset with duplicates rows removed, considering only the subset of columns, within watermark.
This only works with streaming [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset"), and watermark for the input [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") must be set via [withWatermark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#withWatermark\(eventTime:String,delayThreshold:String\):org.apache.spark.sql.Dataset\[T\]).
For a streaming [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset"), this will keep all data across triggers as intermediate state to drop duplicated rows. The state will be kept to guarantee the semantic, "Events are deduplicated as long as the time distance of earliest and latest events are smaller than the delay threshold of watermark." Users are encouraged to set the delay threshold of watermark longer than max timestamp differences among duplicated events.
Note: too late data older than watermark will be dropped.  

Since
    
3.5.0
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#dropDuplicatesWithinWatermark\(\):org.apache.spark.sql.Dataset\[T\] "Permalink") abstract  def dropDuplicatesWithinWatermark(): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Returns a new Dataset with duplicates rows removed, within watermark.
Returns a new Dataset with duplicates rows removed, within watermark.
This only works with streaming [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset"), and watermark for the input [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") must be set via [withWatermark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#withWatermark\(eventTime:String,delayThreshold:String\):org.apache.spark.sql.Dataset\[T\]).
For a streaming [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset"), this will keep all data across triggers as intermediate state to drop duplicated rows. The state will be kept to guarantee the semantic, "Events are deduplicated as long as the time distance of earliest and latest events are smaller than the delay threshold of watermark." Users are encouraged to set the delay threshold of watermark longer than max timestamp differences among duplicated events.
Note: too late data older than watermark will be dropped.  

Since
    
3.5.0
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#encoder:org.apache.spark.sql.Encoder\[T\] "Permalink") abstract  val encoder: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[T]
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#except\(other:org.apache.spark.sql.Dataset\[T\]\):org.apache.spark.sql.Dataset\[T\] "Permalink") abstract  def except(other: [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Returns a new Dataset containing rows in this Dataset but not in another Dataset.
Returns a new Dataset containing rows in this Dataset but not in another Dataset. This is equivalent to `EXCEPT DISTINCT` in SQL.  

Since
    
2.0.0 

Note
    
Equality checking is performed directly on the encoded representation of the data and thus is not affected by a custom `equals` function defined on `T`.
  23. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#exceptAll\(other:org.apache.spark.sql.Dataset\[T\]\):org.apache.spark.sql.Dataset\[T\] "Permalink") abstract  def exceptAll(other: [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Returns a new Dataset containing rows in this Dataset but not in another Dataset while preserving the duplicates.
Returns a new Dataset containing rows in this Dataset but not in another Dataset while preserving the duplicates. This is equivalent to `EXCEPT ALL` in SQL.  

Since
    
2.4.0 

Note
    
Equality checking is performed directly on the encoded representation of the data and thus is not affected by a custom `equals` function defined on `T`. Also as standard in SQL, this function resolves columns by position (not by name).
  24. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#explain\(mode:String\):Unit "Permalink") abstract  def explain(mode: String): Unit
Prints the plans (logical and physical) with a format specified by a given explain mode.
Prints the plans (logical and physical) with a format specified by a given explain mode.  

mode
    
specifies the expected output format of plans.
     * `simple` Print only a physical plan.
     * `extended`: Print both logical and physical plans.
     * `codegen`: Print a physical plan and generated codes if they are available.
     * `cost`: Print a logical plan and statistics if they are available.
     * `formatted`: Split explain output into two sections: a physical plan outline and node details. 

Since
    
3.0.0
  25. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#filter\(func:org.apache.spark.api.java.function.FilterFunction\[T\]\):org.apache.spark.sql.Dataset\[T\] "Permalink") abstract  def filter(func: [FilterFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FilterFunction.html "org.apache.spark.api.java.function.FilterFunction")[T]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
(Java-specific) Returns a new Dataset that only contains elements where `func` returns `true`.
(Java-specific) Returns a new Dataset that only contains elements where `func` returns `true`.  

Since
    
1.6.0
  26. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#filter\(func:T=>Boolean\):org.apache.spark.sql.Dataset\[T\] "Permalink") abstract  def filter(func: (T) => Boolean): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
(Scala-specific) Returns a new Dataset that only contains elements where `func` returns `true`.
(Scala-specific) Returns a new Dataset that only contains elements where `func` returns `true`.  

Since
    
1.6.0
  27. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#filter\(condition:org.apache.spark.sql.Column\):org.apache.spark.sql.Dataset\[T\] "Permalink") abstract  def filter(condition: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Filters rows using the given condition.
Filters rows using the given condition.

```
// The following are equivalent:
peopleDs.filter($"age" > 15)
peopleDs.where($"age" > 15)
```


Since
    
1.6.0
  28. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#foreachPartition\(f:Iterator\[T\]=>Unit\):Unit "Permalink") abstract  def foreachPartition(f: (Iterator[T]) => Unit): Unit
Applies a function `f` to each partition of this Dataset.
Applies a function `f` to each partition of this Dataset.  

Since
    
1.6.0
  29. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#groupBy\(cols:org.apache.spark.sql.Column*\):org.apache.spark.sql.RelationalGroupedDataset "Permalink") abstract  def groupBy(cols: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")*): [RelationalGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/RelationalGroupedDataset.html "org.apache.spark.sql.RelationalGroupedDataset")
Groups the Dataset using the specified columns, so we can run aggregation on them.
Groups the Dataset using the specified columns, so we can run aggregation on them. See [RelationalGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/RelationalGroupedDataset.html "org.apache.spark.sql.RelationalGroupedDataset") for all the available aggregate functions.

```
// Compute the average for all numeric columns grouped by department.
ds.groupBy($"department").avg()

// Compute the max age and average salary, grouped by department and gender.
ds.groupBy($"department", $"gender").agg(Map(
  "salary" -> "avg",
  "age" -> "max"
))
```


Annotations
     @varargs() 

Since
    
2.0.0
  30. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#groupByKey\[K\]\(func:T=>K\)\(implicitevidence$2:org.apache.spark.sql.Encoder\[K\]\):org.apache.spark.sql.KeyValueGroupedDataset\[K,T\] "Permalink") abstract  def groupByKey[K](func: (T) => K)(implicit arg0: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[K]): [KeyValueGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html "org.apache.spark.sql.KeyValueGroupedDataset")[K, T]
(Scala-specific) Returns a [KeyValueGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html "org.apache.spark.sql.KeyValueGroupedDataset") where the data is grouped by the given key `func`.
(Scala-specific) Returns a [KeyValueGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html "org.apache.spark.sql.KeyValueGroupedDataset") where the data is grouped by the given key `func`.  

Since
    
2.0.0
  31. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#groupingSets\(groupingSets:Seq\[Seq\[org.apache.spark.sql.Column\]\],cols:org.apache.spark.sql.Column*\):org.apache.spark.sql.RelationalGroupedDataset "Permalink") abstract  def groupingSets(groupingSets: Seq[Seq[[Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")]], cols: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")*): [RelationalGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/RelationalGroupedDataset.html "org.apache.spark.sql.RelationalGroupedDataset")
Create multi-dimensional aggregation for the current Dataset using the specified grouping sets, so we can run aggregation on them.
Create multi-dimensional aggregation for the current Dataset using the specified grouping sets, so we can run aggregation on them. See [RelationalGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/RelationalGroupedDataset.html "org.apache.spark.sql.RelationalGroupedDataset") for all the available aggregate functions.

```
// Compute the average for all numeric columns group by specific grouping sets.
ds.groupingSets(Seq(Seq($"department", $"group"), Seq()), $"department", $"group").avg()

// Compute the max age and average salary, group by specific grouping sets.
ds.groupingSets(Seq($"department", $"gender"), Seq()), $"department", $"group").agg(Map(
  "salary" -> "avg",
  "age" -> "max"
))
```


Annotations
     @varargs() 

Since
    
4.0.0
  32. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#head\(n:Int\):Array\[T\] "Permalink") abstract  def head(n: Int): Array[T]
Returns the first `n` rows.
Returns the first `n` rows.  

Since
    
1.6.0 

Note
    
this method should only be used if the resulting array is expected to be small, as all the data is loaded into the driver's memory.
  33. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#hint\(name:String,parameters:Any*\):org.apache.spark.sql.Dataset\[T\] "Permalink") abstract  def hint(name: String, parameters: Any*): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Specifies some hint on the current Dataset.
Specifies some hint on the current Dataset. As an example, the following code specifies that one of the plan can be broadcasted:

```
df1.join(df2.hint("broadcast"))
```

the following code specifies that this dataset could be rebalanced with given number of partitions:

```
df1.hint("rebalance", 10)
```


name
    
the name of the hint 

parameters
    
the parameters of the hint, all the parameters should be a `Column` or `Expression` or `Symbol` or could be converted into a `Literal` 

Annotations
     @varargs() 

Since
    
2.2.0
  34. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#inputFiles:Array\[String\] "Permalink") abstract  def inputFiles: Array[String]
Returns a best-effort snapshot of the files that compose this Dataset.
Returns a best-effort snapshot of the files that compose this Dataset. This method simply asks each constituent BaseRelation for its respective files and takes the union of all results. Depending on the source relations, this may not find all input files. Duplicates are removed.  

Since
    
2.0.0
  35. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#intersect\(other:org.apache.spark.sql.Dataset\[T\]\):org.apache.spark.sql.Dataset\[T\] "Permalink") abstract  def intersect(other: [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Returns a new Dataset containing rows only in both this Dataset and another Dataset.
Returns a new Dataset containing rows only in both this Dataset and another Dataset. This is equivalent to `INTERSECT` in SQL.  

Since
    
1.6.0 

Note
    
Equality checking is performed directly on the encoded representation of the data and thus is not affected by a custom `equals` function defined on `T`.
  36. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#intersectAll\(other:org.apache.spark.sql.Dataset\[T\]\):org.apache.spark.sql.Dataset\[T\] "Permalink") abstract  def intersectAll(other: [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Returns a new Dataset containing rows only in both this Dataset and another Dataset while preserving the duplicates.
Returns a new Dataset containing rows only in both this Dataset and another Dataset while preserving the duplicates. This is equivalent to `INTERSECT ALL` in SQL.  

Since
    
2.4.0 

Note
    
Equality checking is performed directly on the encoded representation of the data and thus is not affected by a custom `equals` function defined on `T`. Also as standard in SQL, this function resolves columns by position (not by name).
  37. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#isEmpty:Boolean "Permalink") abstract  def isEmpty: Boolean
Returns true if the `Dataset` is empty.
Returns true if the `Dataset` is empty.  

Since
    
2.4.0
  38. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#isLocal:Boolean "Permalink") abstract  def isLocal: Boolean
Returns true if the `collect` and `take` methods can be run locally (without any Spark executors).
Returns true if the `collect` and `take` methods can be run locally (without any Spark executors).  

Since
    
1.6.0
  39. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#isStreaming:Boolean "Permalink") abstract  def isStreaming: Boolean
Returns true if this Dataset contains one or more sources that continuously return data as it arrives.
Returns true if this Dataset contains one or more sources that continuously return data as it arrives. A Dataset that reads data from a streaming source must be executed as a `StreamingQuery` using the `start()` method in `DataStreamWriter`. Methods that return a single answer, e.g. `count()` or `collect()`, will throw an [org.apache.spark.sql.AnalysisException](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/AnalysisException.html "org.apache.spark.sql.AnalysisException") when there is a streaming source present.  

Since
    
2.0.0
  40. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#join\(right:org.apache.spark.sql.Dataset\[_\],joinExprs:org.apache.spark.sql.Column,joinType:String\):org.apache.spark.sql.DataFrame "Permalink") abstract  def join(right: [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[_], joinExprs: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column"), joinType: String): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Join with another `DataFrame`, using the given join expression.
Join with another `DataFrame`, using the given join expression. The following performs a full outer join between `df1` and `df2`.

```
// Scala:
import org.apache.spark.sql.functions._
df1.join(df2, $"df1Key" === $"df2Key", "outer")

// Java:
import static org.apache.spark.sql.functions.*;
df1.join(df2, col("df1Key").equalTo(col("df2Key")), "outer");
```


right
    
Right side of the join. 

joinExprs
    
Join expression. 

joinType
    
Type of join to perform. Default `inner`. Must be one of: `inner`, `cross`, `outer`, `full`, `fullouter`, `full_outer`, `left`, `leftouter`, `left_outer`, `right`, `rightouter`, `right_outer`, `semi`, `leftsemi`, `left_semi`, `anti`, `leftanti`, `left_anti`. 

Since
    
2.0.0
  41. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#join\(right:org.apache.spark.sql.Dataset\[_\],usingColumns:Seq\[String\],joinType:String\):org.apache.spark.sql.DataFrame "Permalink") abstract  def join(right: [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[_], usingColumns: Seq[String], joinType: String): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
(Scala-specific) Equi-join with another `DataFrame` using the given columns.
(Scala-specific) Equi-join with another `DataFrame` using the given columns. A cross join with a predicate is specified as an inner join. If you would explicitly like to perform a cross join use the `crossJoin` method.
Different from other join functions, the join columns will only appear once in the output, i.e. similar to SQL's `JOIN USING` syntax.  

right
    
Right side of the join operation. 

usingColumns
    
Names of the columns to join on. This columns must exist on both sides. 

joinType
    
Type of join to perform. Default `inner`. Must be one of: `inner`, `cross`, `outer`, `full`, `fullouter`, `full_outer`, `left`, `leftouter`, `left_outer`, `right`, `rightouter`, `right_outer`, `semi`, `leftsemi`, `left_semi`, `anti`, `leftanti`, `left_anti`. 

Since
    
2.0.0 

Note
    
If you perform a self-join using this function without aliasing the input `DataFrame`s, you will NOT be able to reference any columns after the join, since there is no way to disambiguate which side of the join you would like to reference.
  42. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#join\(right:org.apache.spark.sql.Dataset\[_\]\):org.apache.spark.sql.DataFrame "Permalink") abstract  def join(right: [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[_]): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Join with another `DataFrame`.
Join with another `DataFrame`.
Behaves as an INNER JOIN and requires a subsequent join predicate.  

right
    
Right side of the join operation. 

Since
    
2.0.0
  43. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#joinWith\[U\]\(other:org.apache.spark.sql.Dataset\[U\],condition:org.apache.spark.sql.Column,joinType:String\):org.apache.spark.sql.Dataset\[\(T,U\)\] "Permalink") abstract  def joinWith[U](other: [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[U], condition: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column"), joinType: String): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[(T, U)]
Joins this Dataset returning a `Tuple2` for each pair where `condition` evaluates to true.
Joins this Dataset returning a `Tuple2` for each pair where `condition` evaluates to true.
This is similar to the relation `join` function with one important difference in the result schema. Since `joinWith` preserves objects present on either side of the join, the result schema is similarly nested into a tuple under the column names `_1` and `_2`.
This type of join can be useful both for preserving type-safety with the original object types as well as working with relational data where either side of the join has column names in common.  

other
    
Right side of the join. 

condition
    
Join expression. 

joinType
    
Type of join to perform. Default `inner`. Must be one of: `inner`, `cross`, `outer`, `full`, `fullouter`,`full_outer`, `left`, `leftouter`, `left_outer`, `right`, `rightouter`, `right_outer`. 

Since
    
1.6.0
  44. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#lateralJoin\(right:org.apache.spark.sql.Dataset\[_\],joinExprs:org.apache.spark.sql.Column,joinType:String\):org.apache.spark.sql.DataFrame "Permalink") abstract  def lateralJoin(right: [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[_], joinExprs: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column"), joinType: String): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Lateral join with another `DataFrame`.
Lateral join with another `DataFrame`.  

right
    
Right side of the join operation. 

joinExprs
    
Join expression. 

joinType
    
Type of join to perform. Default `inner`. Must be one of: `inner`, `cross`, `left`, `leftouter`, `left_outer`. 

Since
    
4.0.0
  45. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#lateralJoin\(right:org.apache.spark.sql.Dataset\[_\],joinType:String\):org.apache.spark.sql.DataFrame "Permalink") abstract  def lateralJoin(right: [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[_], joinType: String): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Lateral join with another `DataFrame`.
Lateral join with another `DataFrame`.  

right
    
Right side of the join operation. 

joinType
    
Type of join to perform. Default `inner`. Must be one of: `inner`, `cross`, `left`, `leftouter`, `left_outer`. 

Since
    
4.0.0
  46. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#lateralJoin\(right:org.apache.spark.sql.Dataset\[_\],joinExprs:org.apache.spark.sql.Column\):org.apache.spark.sql.DataFrame "Permalink") abstract  def lateralJoin(right: [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[_], joinExprs: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Lateral join with another `DataFrame`.
Lateral join with another `DataFrame`.
Behaves as an JOIN LATERAL.  

right
    
Right side of the join operation. 

joinExprs
    
Join expression. 

Since
    
4.0.0
  47. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#lateralJoin\(right:org.apache.spark.sql.Dataset\[_\]\):org.apache.spark.sql.DataFrame "Permalink") abstract  def lateralJoin(right: [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[_]): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Lateral join with another `DataFrame`.
Lateral join with another `DataFrame`.
Behaves as an JOIN LATERAL.  

right
    
Right side of the join operation. 

Since
    
4.0.0
  48. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#limit\(n:Int\):org.apache.spark.sql.Dataset\[T\] "Permalink") abstract  def limit(n: Int): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Returns a new Dataset by taking the first `n` rows.
Returns a new Dataset by taking the first `n` rows. The difference between this function and `head` is that `head` is an action and returns an array (by triggering query execution) while `limit` returns a new Dataset.  

Since
    
2.0.0
  49. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#map\[U\]\(func:org.apache.spark.api.java.function.MapFunction\[T,U\],encoder:org.apache.spark.sql.Encoder\[U\]\):org.apache.spark.sql.Dataset\[U\] "Permalink") abstract  def map[U](func: [MapFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/MapFunction.html "org.apache.spark.api.java.function.MapFunction")[T, U], encoder: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[U]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[U]
(Java-specific) Returns a new Dataset that contains the result of applying `func` to each element.
(Java-specific) Returns a new Dataset that contains the result of applying `func` to each element.  

Since
    
1.6.0
  50. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#map\[U\]\(func:T=>U\)\(implicitevidence$5:org.apache.spark.sql.Encoder\[U\]\):org.apache.spark.sql.Dataset\[U\] "Permalink") abstract  def map[U](func: (T) => U)(implicit arg0: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[U]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[U]
(Scala-specific) Returns a new Dataset that contains the result of applying `func` to each element.
(Scala-specific) Returns a new Dataset that contains the result of applying `func` to each element.  

Since
    
1.6.0
  51. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#mapPartitions\[U\]\(func:Iterator\[T\]=>Iterator\[U\]\)\(implicitevidence$6:org.apache.spark.sql.Encoder\[U\]\):org.apache.spark.sql.Dataset\[U\] "Permalink") abstract  def mapPartitions[U](func: (Iterator[T]) => Iterator[U])(implicit arg0: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[U]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[U]
(Scala-specific) Returns a new Dataset that contains the result of applying `func` to each partition.
(Scala-specific) Returns a new Dataset that contains the result of applying `func` to each partition.  

Since
    
1.6.0
  52. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#mergeInto\(table:String,condition:org.apache.spark.sql.Column\):org.apache.spark.sql.MergeIntoWriter\[T\] "Permalink") abstract  def mergeInto(table: String, condition: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")): [MergeIntoWriter](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/MergeIntoWriter.html "org.apache.spark.sql.MergeIntoWriter")[T]
Merges a set of updates, insertions, and deletions based on a source table into a target table.
Merges a set of updates, insertions, and deletions based on a source table into a target table.
Scala Examples:

```
spark.table("source")
  .mergeInto("target", $"source.id" === $"target.id")
  .whenMatched($"salary" === 100)
  .delete()
  .whenNotMatched()
  .insertAll()
  .whenNotMatchedBySource($"salary" === 100)
  .update(Map(
    "salary" -> lit(200)
  ))
  .merge()
```


Since
    
4.0.0
  53. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#metadataColumn\(colName:String\):org.apache.spark.sql.Column "Permalink") abstract  def metadataColumn(colName: String): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Selects a metadata column based on its logical column name, and returns it as a [org.apache.spark.sql.Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column").
Selects a metadata column based on its logical column name, and returns it as a [org.apache.spark.sql.Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column").
A metadata column can be accessed this way even if the underlying data source defines a data column with a conflicting name.  

Since
    
3.5.0
  54. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#na:org.apache.spark.sql.DataFrameNaFunctions "Permalink") abstract  def na: [DataFrameNaFunctions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/DataFrameNaFunctions.html "org.apache.spark.sql.DataFrameNaFunctions")
Returns a [DataFrameNaFunctions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/DataFrameNaFunctions.html "org.apache.spark.sql.DataFrameNaFunctions") for working with missing data.
Returns a [DataFrameNaFunctions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/DataFrameNaFunctions.html "org.apache.spark.sql.DataFrameNaFunctions") for working with missing data.

```
// Dropping rows containing any null values.
ds.na.drop()
```


Since
    
1.6.0
  55. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#observe\(observation:org.apache.spark.sql.Observation,expr:org.apache.spark.sql.Column,exprs:org.apache.spark.sql.Column*\):org.apache.spark.sql.Dataset\[T\] "Permalink") abstract  def observe(observation: [Observation](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Observation.html "org.apache.spark.sql.Observation"), expr: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column"), exprs: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")*): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Observe (named) metrics through an `org.apache.spark.sql.Observation` instance.
Observe (named) metrics through an `org.apache.spark.sql.Observation` instance. This method does not support streaming datasets.
A user can retrieve the metrics by accessing `org.apache.spark.sql.Observation.get`.

```
// Observe row count (rows) and highest id (maxid) in the Dataset while writing it
val observation = Observation("my_metrics")
val observed_ds = ds.observe(observation, count(lit(1)).as("rows"), max($"id").as("maxid"))
observed_ds.write.parquet("ds.parquet")
val metrics = observation.get
```


Annotations
     @varargs() 

Since
    
3.3.0 

Exceptions thrown
    
`IllegalArgumentException` If this is a streaming Dataset (this.isStreaming == true)
  56. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#observe\(name:String,expr:org.apache.spark.sql.Column,exprs:org.apache.spark.sql.Column*\):org.apache.spark.sql.Dataset\[T\] "Permalink") abstract  def observe(name: String, expr: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column"), exprs: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")*): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Define (named) metrics to observe on the Dataset.
Define (named) metrics to observe on the Dataset. This method returns an 'observed' Dataset that returns the same result as the input, with the following guarantees:
     * It will compute the defined aggregates (metrics) on all the data that is flowing through the Dataset at that point.
     * It will report the value of the defined aggregate columns as soon as we reach a completion point. A completion point is either the end of a query (batch mode) or the end of a streaming epoch. The value of the aggregates only reflects the data processed since the previous completion point. Please note that continuous execution is currently not supported.
The metrics columns must either contain a literal (e.g. lit(42)), or should contain one or more aggregate functions (e.g. sum(a) or sum(a + b) + avg(c) - lit(1)). Expressions that contain references to the input Dataset's columns must always be wrapped in an aggregate function.  

Annotations
     @varargs() 

Since
    
3.0.0
  57. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#offset\(n:Int\):org.apache.spark.sql.Dataset\[T\] "Permalink") abstract  def offset(n: Int): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Returns a new Dataset by skipping the first `n` rows.
Returns a new Dataset by skipping the first `n` rows.  

Since
    
3.4.0
  58. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#persist\(newLevel:org.apache.spark.storage.StorageLevel\):org.apache.spark.sql.Dataset\[T\] "Permalink") abstract  def persist(newLevel: [StorageLevel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StorageLevel.html "org.apache.spark.storage.StorageLevel")): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Persist this Dataset with the given storage level.
Persist this Dataset with the given storage level.  

newLevel
    
One of: `MEMORY_ONLY`, `MEMORY_AND_DISK`, `MEMORY_ONLY_SER`, `MEMORY_AND_DISK_SER`, `DISK_ONLY`, `MEMORY_ONLY_2`, `MEMORY_AND_DISK_2`, etc. 

Since
    
1.6.0
  59. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#persist\(\):org.apache.spark.sql.Dataset\[T\] "Permalink") abstract  def persist(): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Persist this Dataset with the default storage level (`MEMORY_AND_DISK`).
Persist this Dataset with the default storage level (`MEMORY_AND_DISK`).  

Since
    
1.6.0
  60. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#queryExecution:org.apache.spark.sql.execution.QueryExecution "Permalink") abstract  def queryExecution: QueryExecution 

Annotations
     @ClassicOnly() @DeveloperApi() @Unstable()
  61. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#randomSplit\(weights:Array\[Double\]\):Array\[org.apache.spark.sql.Dataset\[T\]\] "Permalink") abstract  def randomSplit(weights: Array[Double]): Array[[Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]]
Randomly splits this Dataset with the provided weights.
Randomly splits this Dataset with the provided weights.  

weights
    
weights for splits, will be normalized if they don't sum to 1. 

Since
    
2.0.0
  62. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#randomSplit\(weights:Array\[Double\],seed:Long\):Array\[org.apache.spark.sql.Dataset\[T\]\] "Permalink") abstract  def randomSplit(weights: Array[Double], seed: Long): Array[[Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]]
Randomly splits this Dataset with the provided weights.
Randomly splits this Dataset with the provided weights.  

weights
    
weights for splits, will be normalized if they don't sum to 1. 

seed
    
Seed for sampling. For Java API, use [randomSplitAsList](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#randomSplitAsList\(weights:Array\[Double\],seed:Long\):java.util.List\[org.apache.spark.sql.Dataset\[T\]\]). 

Since
    
2.0.0
  63. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#randomSplitAsList\(weights:Array\[Double\],seed:Long\):java.util.List\[org.apache.spark.sql.Dataset\[T\]\] "Permalink") abstract  def randomSplitAsList(weights: Array[Double], seed: Long): [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#java.util.List "java.util.List")[[Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]]
Returns a Java list that contains randomly split Dataset with the provided weights.
Returns a Java list that contains randomly split Dataset with the provided weights.  

weights
    
weights for splits, will be normalized if they don't sum to 1. 

seed
    
Seed for sampling. 

Since
    
2.0.0
  64. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#rdd:org.apache.spark.rdd.RDD\[T\] "Permalink") abstract  def rdd: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[T]
Represents the content of the Dataset as an `RDD` of `T`.
Represents the content of the Dataset as an `RDD` of `T`.  

Annotations
     @ClassicOnly() 

Since
    
1.6.0 

Note
    
this is only supported in Classic.
  65. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#reduce\(func:\(T,T\)=>T\):T "Permalink") abstract  def reduce(func: (T, T) => T): T
(Scala-specific) Reduces the elements of this Dataset using the specified binary function.
(Scala-specific) Reduces the elements of this Dataset using the specified binary function. The given `func` must be commutative and associative or the result may be non-deterministic.  

Since
    
1.6.0
  66. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#repartition\(numPartitions:Int\):org.apache.spark.sql.Dataset\[T\] "Permalink") abstract  def repartition(numPartitions: Int): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Returns a new Dataset that has exactly `numPartitions` partitions.
Returns a new Dataset that has exactly `numPartitions` partitions.  

Since
    
1.6.0
  67. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#repartitionByExpression\(numPartitions:Option\[Int\],partitionExprs:Seq\[org.apache.spark.sql.Column\]\):org.apache.spark.sql.Dataset\[T\] "Permalink") abstract  def repartitionByExpression(numPartitions: Option[Int], partitionExprs: Seq[[Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T] 

Attributes
    protected 
  68. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#repartitionById\(numPartitions:Int,partitionIdExpr:org.apache.spark.sql.Column\):org.apache.spark.sql.Dataset\[T\] "Permalink") abstract  def repartitionById(numPartitions: Int, partitionIdExpr: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Repartition the Dataset into the given number of partitions using the specified partition ID expression.
Repartition the Dataset into the given number of partitions using the specified partition ID expression.  

numPartitions
    
the number of partitions to use. 

partitionIdExpr
    
the expression to be used as the partition ID. Must be an integer type. 

Since
    
4.1.0
  69. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#repartitionByRange\(numPartitions:Option\[Int\],partitionExprs:Seq\[org.apache.spark.sql.Column\]\):org.apache.spark.sql.Dataset\[T\] "Permalink") abstract  def repartitionByRange(numPartitions: Option[Int], partitionExprs: Seq[[Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T] 

Attributes
    protected 
  70. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#rollup\(cols:org.apache.spark.sql.Column*\):org.apache.spark.sql.RelationalGroupedDataset "Permalink") abstract  def rollup(cols: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")*): [RelationalGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/RelationalGroupedDataset.html "org.apache.spark.sql.RelationalGroupedDataset")
Create a multi-dimensional rollup for the current Dataset using the specified columns, so we can run aggregation on them.
Create a multi-dimensional rollup for the current Dataset using the specified columns, so we can run aggregation on them. See [RelationalGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/RelationalGroupedDataset.html "org.apache.spark.sql.RelationalGroupedDataset") for all the available aggregate functions.

```
// Compute the average for all numeric columns rolled up by department and group.
ds.rollup($"department", $"group").avg()

// Compute the max age and average salary, rolled up by department and gender.
ds.rollup($"department", $"gender").agg(Map(
  "salary" -> "avg",
  "age" -> "max"
))
```


Annotations
     @varargs() 

Since
    
2.0.0
  71. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#sameSemantics\(other:org.apache.spark.sql.Dataset\[T\]\):Boolean "Permalink") abstract  def sameSemantics(other: [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]): Boolean
Returns `true` when the logical query plans inside both [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")s are equal and therefore return same results.
Returns `true` when the logical query plans inside both [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")s are equal and therefore return same results.  

Annotations
     @DeveloperApi() 

Since
    
3.1.0 

Note
    
The equality comparison here is simplified by tolerating the cosmetic differences such as attribute names.
, 
This API can compare both [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")s very fast but can still return `false` on the [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") that return the same results, for instance, from different plans. Such false negative semantic can be useful when caching as an example.
  72. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#sample\(withReplacement:Boolean,fraction:Double,seed:Long\):org.apache.spark.sql.Dataset\[T\] "Permalink") abstract  def sample(withReplacement: Boolean, fraction: Double, seed: Long): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Returns a new [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") by sampling a fraction of rows, using a user-supplied seed.
Returns a new [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") by sampling a fraction of rows, using a user-supplied seed.  

withReplacement
    
Sample with replacement or not. 

fraction
    
Fraction of rows to generate, range [0.0, 1.0]. 

seed
    
Seed for sampling. 

Since
    
1.6.0 

Note
    
This is NOT guaranteed to provide exactly the fraction of the count of the given [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset").
  73. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#schema:org.apache.spark.sql.types.StructType "Permalink") abstract  def schema: [StructType](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/types/StructType.html "org.apache.spark.sql.types.StructType")
Returns the schema of this Dataset.
Returns the schema of this Dataset.  

Since
    
1.6.0
  74. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#select\[U1\]\(c1:org.apache.spark.sql.TypedColumn\[T,U1\]\):org.apache.spark.sql.Dataset\[U1\] "Permalink") abstract  def select[U1](c1: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[T, U1]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[U1]
Returns a new Dataset by computing the given [org.apache.spark.sql.Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column") expression for each element.
Returns a new Dataset by computing the given [org.apache.spark.sql.Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column") expression for each element.

```
val ds = Seq(1, 2, 3).toDS()
val newDS = ds.select(expr("value + 1").as[Int])
```


Since
    
1.6.0
  75. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#select\(cols:org.apache.spark.sql.Column*\):org.apache.spark.sql.DataFrame "Permalink") abstract  def select(cols: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")*): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Selects a set of column based expressions.
Selects a set of column based expressions.

```
ds.select($"colA", $"colB" + 1)
```


Annotations
     @varargs() 

Since
    
2.0.0
  76. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#selectUntyped\(columns:org.apache.spark.sql.TypedColumn\[_,_\]*\):org.apache.spark.sql.Dataset\[_\] "Permalink") abstract  def selectUntyped(columns: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[_, _]*): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[_]
Internal helper function for building typed selects that return tuples.
Internal helper function for building typed selects that return tuples. For simplicity and code reuse, we do this without the help of the type system and then use helper functions that cast appropriately for the user facing interface.  

Attributes
    protected 
  77. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#semanticHash\(\):Int "Permalink") abstract  def semanticHash(): Int
Returns a `hashCode` of the logical query plan against this [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset").
Returns a `hashCode` of the logical query plan against this [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset").  

Annotations
     @DeveloperApi() 

Since
    
3.1.0 

Note
    
Unlike the standard `hashCode`, the hash is calculated against the query plan simplified by tolerating the cosmetic differences such as attribute names.
  78. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#show\(numRows:Int,truncate:Int,vertical:Boolean\):Unit "Permalink") abstract  def show(numRows: Int, truncate: Int, vertical: Boolean): Unit
Displays the Dataset in a tabular form.
Displays the Dataset in a tabular form. For example:

```
year  month AVG('Adj Close) MAX('Adj Close)
1980  12    0.503218        0.595103
1981  01    0.523289        0.570307
1982  02    0.436504        0.475256
1983  03    0.410516        0.442194
1984  04    0.450090        0.483521
```

If `vertical` enabled, this command prints output rows vertically (one line per column value)?

```
-RECORD 0-------------------
 year            | 1980
 month           | 12
 AVG('Adj Close) | 0.503218
 AVG('Adj Close) | 0.595103
-RECORD 1-------------------
 year            | 1981
 month           | 01
 AVG('Adj Close) | 0.523289
 AVG('Adj Close) | 0.570307
-RECORD 2-------------------
 year            | 1982
 month           | 02
 AVG('Adj Close) | 0.436504
 AVG('Adj Close) | 0.475256
-RECORD 3-------------------
 year            | 1983
 month           | 03
 AVG('Adj Close) | 0.410516
 AVG('Adj Close) | 0.442194
-RECORD 4-------------------
 year            | 1984
 month           | 04
 AVG('Adj Close) | 0.450090
 AVG('Adj Close) | 0.483521
```


numRows
    
Number of rows to show 

truncate
    
If set to more than 0, truncates strings to `truncate` characters and all cells will be aligned right. 

vertical
    
If set to true, prints output rows vertically (one line per column value). 

Since
    
2.3.0
  79. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#show\(numRows:Int,truncate:Boolean\):Unit "Permalink") abstract  def show(numRows: Int, truncate: Boolean): Unit
Displays the Dataset in a tabular form.
Displays the Dataset in a tabular form. For example:

```
year  month AVG('Adj Close) MAX('Adj Close)
1980  12    0.503218        0.595103
1981  01    0.523289        0.570307
1982  02    0.436504        0.475256
1983  03    0.410516        0.442194
1984  04    0.450090        0.483521
```


numRows
    
Number of rows to show 

truncate
    
Whether truncate long strings. If true, strings more than 20 characters will be truncated and all cells will be aligned right 

Since
    
1.6.0
  80. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#sortInternal\(global:Boolean,sortExprs:Seq\[org.apache.spark.sql.Column\]\):org.apache.spark.sql.Dataset\[T\] "Permalink") abstract  def sortInternal(global: Boolean, sortExprs: Seq[[Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T] 

Attributes
    protected 
  81. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#sparkSession:org.apache.spark.sql.SparkSession "Permalink") abstract  val sparkSession: [SparkSession](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/SparkSession.html "org.apache.spark.sql.SparkSession")
  82. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#stat:org.apache.spark.sql.DataFrameStatFunctions "Permalink") abstract  def stat: [DataFrameStatFunctions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/DataFrameStatFunctions.html "org.apache.spark.sql.DataFrameStatFunctions")
Returns a [DataFrameStatFunctions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/DataFrameStatFunctions.html "org.apache.spark.sql.DataFrameStatFunctions") for working statistic functions support.
Returns a [DataFrameStatFunctions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/DataFrameStatFunctions.html "org.apache.spark.sql.DataFrameStatFunctions") for working statistic functions support.

```
// Finding frequent items in column with name 'a'.
ds.stat.freqItems(Seq("a"))
```


Since
    
1.6.0
  83. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#storageLevel:org.apache.spark.storage.StorageLevel "Permalink") abstract  def storageLevel: [StorageLevel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StorageLevel.html "org.apache.spark.storage.StorageLevel")
Get the Dataset's current storage level, or StorageLevel.NONE if not persisted.
Get the Dataset's current storage level, or StorageLevel.NONE if not persisted.  

Since
    
2.1.0
  84. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#summary\(statistics:String*\):org.apache.spark.sql.DataFrame "Permalink") abstract  def summary(statistics: String*): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Computes specified statistics for numeric and string columns.
Computes specified statistics for numeric and string columns. Available statistics are:
     * count
     * mean
     * stddev
     * min
     * max
     * arbitrary approximate percentiles specified as a percentage (e.g. 75%)
     * count_distinct
     * approx_count_distinct
If no statistics are given, this function computes count, mean, stddev, min, approximate quartiles (percentiles at 25%, 50%, and 75%), and max.
This function is meant for exploratory data analysis, as we make no guarantee about the backward compatibility of the schema of the resulting Dataset. If you want to programmatically compute summary statistics, use the `agg` function instead.

```
ds.summary().show()

// output:
// summary age   height
// count   10.0  10.0
// mean    53.3  178.05
// stddev  11.6  15.7
// min     18.0  163.0
// 25%     24.0  176.0
// 50%     24.0  176.0
// 75%     32.0  180.0
// max     92.0  192.0
```

```
ds.summary("count", "min", "25%", "75%", "max").show()

// output:
// summary age   height
// count   10.0  10.0
// min     18.0  163.0
// 25%     24.0  176.0
// 75%     32.0  180.0
// max     92.0  192.0
```

To do a summary for specific columns first select them:

```
ds.select("age", "height").summary().show()
```

Specify statistics to output custom summaries:

```
ds.summary("count", "count_distinct").show()
```

The distinct count isn't included by default.
You can also run approximate distinct counts which are faster:

```
ds.summary("count", "approx_count_distinct").show()
```

See also [describe](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#describe\(cols:String*\):org.apache.spark.sql.DataFrame) for basic statistics.  

statistics
    
Statistics from above list to be computed. 

Annotations
     @varargs() 

Since
    
2.3.0
  85. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#tail\(n:Int\):Array\[T\] "Permalink") abstract  def tail(n: Int): Array[T]
Returns the last `n` rows in the Dataset.
Returns the last `n` rows in the Dataset.
Running tail requires moving data into the application's driver process, and doing so with a very large `n` can crash the driver process with OutOfMemoryError.  

Since
    
3.0.0
  86. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#to\(schema:org.apache.spark.sql.types.StructType\):org.apache.spark.sql.DataFrame "Permalink") abstract  def to(schema: [StructType](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/types/StructType.html "org.apache.spark.sql.types.StructType")): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Returns a new DataFrame where each row is reconciled to match the specified schema.
Returns a new DataFrame where each row is reconciled to match the specified schema. Spark will:
     * Reorder columns and/or inner fields by name to match the specified schema.
     * Project away columns and/or inner fields that are not needed by the specified schema. Missing columns and/or inner fields (present in the specified schema but not input DataFrame) lead to failures.
     * Cast the columns and/or inner fields to match the data types in the specified schema, if the types are compatible, e.g., numeric to numeric (error if overflows), but not string to int.
     * Carry over the metadata from the specified schema, while the columns and/or inner fields still keep their own metadata if not overwritten by the specified schema.
     * Fail if the nullability is not compatible. For example, the column and/or inner field is nullable but the specified schema requires them to be not nullable.  

Since
    
3.4.0
  87. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#toDF\(colNames:String*\):org.apache.spark.sql.DataFrame "Permalink") abstract  def toDF(colNames: String*): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Converts this strongly typed collection of data to generic `DataFrame` with columns renamed.
Converts this strongly typed collection of data to generic `DataFrame` with columns renamed. This can be quite convenient in conversion from an RDD of tuples into a `DataFrame` with meaningful names. For example:

```
val rdd: RDD[(Int, String)] = ...
rdd.toDF()  // this implicit conversion creates a DataFrame with column name `_1` and `_2`
rdd.toDF("id", "name")  // this creates a DataFrame with column name "id" and "name"
```


Annotations
     @varargs() 

Since
    
2.0.0
  88. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#toDF\(\):org.apache.spark.sql.DataFrame "Permalink") abstract  def toDF(): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Converts this strongly typed collection of data to generic Dataframe.
Converts this strongly typed collection of data to generic Dataframe. In contrast to the strongly typed objects that Dataset operations work on, a Dataframe returns generic [org.apache.spark.sql.Row](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Row.html "org.apache.spark.sql.Row") objects that allow fields to be accessed by ordinal or name.  

Since
    
1.6.0
  89. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#toJSON:org.apache.spark.sql.Dataset\[String\] "Permalink") abstract  def toJSON: [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[String]
Returns the content of the Dataset as a Dataset of JSON strings.
Returns the content of the Dataset as a Dataset of JSON strings.  

Since
    
2.0.0
  90. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#toJavaRDD:org.apache.spark.api.java.JavaRDD\[T\] "Permalink") abstract  def toJavaRDD: [JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[T]
Returns the content of the Dataset as a `JavaRDD` of `T`s.
Returns the content of the Dataset as a `JavaRDD` of `T`s.  

Annotations
     @ClassicOnly() 

Since
    
1.6.0 

Note
    
this is only supported in Classic.
  91. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#toLocalIterator\(\):java.util.Iterator\[T\] "Permalink") abstract  def toLocalIterator(): [Iterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html#java.util.Iterator "java.util.Iterator")[T]
Returns an iterator that contains all rows in this Dataset.
Returns an iterator that contains all rows in this Dataset.
The iterator will consume as much memory as the largest partition in this Dataset.  

Since
    
2.0.0 

Note
    
this results in multiple Spark jobs, and if the input Dataset is the result of a wide transformation (e.g. join with different partitioners), to avoid recomputing the input Dataset should be cached first.
  92. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#transpose\(\):org.apache.spark.sql.DataFrame "Permalink") abstract  def transpose(): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Transposes a DataFrame, switching rows to columns.
Transposes a DataFrame, switching rows to columns. This function transforms the DataFrame such that the values in the first column become the new columns of the DataFrame.
This is equivalent to calling `Dataset#transpose(Column)` where `indexColumn` is set to the first column.
Please note:
     * All columns except the index column must share a least common data type. Unless they are the same data type, all columns are cast to the nearest common data type.
     * The name of the column into which the original column names are transposed defaults to "key".
     * Non-"key" column names for the transposed table are ordered in ascending order.  

Since
    
4.0.0
  93. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#transpose\(indexColumn:org.apache.spark.sql.Column\):org.apache.spark.sql.DataFrame "Permalink") abstract  def transpose(indexColumn: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Transposes a DataFrame such that the values in the specified index column become the new columns of the DataFrame.
Transposes a DataFrame such that the values in the specified index column become the new columns of the DataFrame.
Please note:
     * All columns except the index column must share a least common data type. Unless they are the same data type, all columns are cast to the nearest common data type.
     * The name of the column into which the original column names are transposed defaults to "key".
     * null values in the index column are excluded from the column names for the transposed table, which are ordered in ascending order.

```
val df = Seq(("A", 1, 2), ("B", 3, 4)).toDF("id", "val1", "val2")
df.show()
// output:
// +---+----+----+
// | id|val1|val2|
// +---+----+----+
// |  A|   1|   2|
// |  B|   3|   4|
// +---+----+----+

df.transpose($"id").show()
// output:
// +----+---+---+
// | key|  A|  B|
// +----+---+---+
// |val1|  1|  3|
// |val2|  2|  4|
// +----+---+---+
// schema:
// root
//  |-- key: string (nullable = false)
//  |-- A: integer (nullable = true)
//  |-- B: integer (nullable = true)

df.transpose().show()
// output:
// +----+---+---+
// | key|  A|  B|
// +----+---+---+
// |val1|  1|  3|
// |val2|  2|  4|
// +----+---+---+
// schema:
// root
//  |-- key: string (nullable = false)
//  |-- A: integer (nullable = true)
//  |-- B: integer (nullable = true)
```


indexColumn
    
The single column that will be treated as the index for the transpose operation. This column will be used to pivot the data, transforming the DataFrame such that the values of the indexColumn become the new columns in the transposed DataFrame. 

Since
    
4.0.0
  94. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#union\(other:org.apache.spark.sql.Dataset\[T\]\):org.apache.spark.sql.Dataset\[T\] "Permalink") abstract  def union(other: [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Returns a new Dataset containing union of rows in this Dataset and another Dataset.
Returns a new Dataset containing union of rows in this Dataset and another Dataset.
This is equivalent to `UNION ALL` in SQL. To do a SQL-style set union (that does deduplication of elements), use this function followed by a [distinct](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#distinct\(\):org.apache.spark.sql.Dataset\[T\]).
Also as standard in SQL, this function resolves columns by position (not by name):

```
val df1 = Seq((1, 2, 3)).toDF("col0", "col1", "col2")
val df2 = Seq((4, 5, 6)).toDF("col1", "col2", "col0")
df1.union(df2).show

// output:
// +----+----+----+
// |col0|col1|col2|
// +----+----+----+
// |   1|   2|   3|
// |   4|   5|   6|
// +----+----+----+
```

Notice that the column positions in the schema aren't necessarily matched with the fields in the strongly typed objects in a Dataset. This function resolves columns by their positions in the schema, not the fields in the strongly typed objects. Use [unionByName](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#unionByName\(other:org.apache.spark.sql.Dataset\[T\]\):org.apache.spark.sql.Dataset\[T\]) to resolve columns by field name in the typed objects.  

Since
    
2.0.0
  95. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#unionByName\(other:org.apache.spark.sql.Dataset\[T\],allowMissingColumns:Boolean\):org.apache.spark.sql.Dataset\[T\] "Permalink") abstract  def unionByName(other: [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T], allowMissingColumns: Boolean): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Returns a new Dataset containing union of rows in this Dataset and another Dataset.
Returns a new Dataset containing union of rows in this Dataset and another Dataset.
The difference between this function and [union](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#union\(other:org.apache.spark.sql.Dataset\[T\]\):org.apache.spark.sql.Dataset\[T\]) is that this function resolves columns by name (not by position).
When the parameter `allowMissingColumns` is `true`, the set of column names in this and other `Dataset` can differ; missing columns will be filled with null. Further, the missing columns of this `Dataset` will be added at the end in the schema of the union result:

```
val df1 = Seq((1, 2, 3)).toDF("col0", "col1", "col2")
val df2 = Seq((4, 5, 6)).toDF("col1", "col0", "col3")
df1.unionByName(df2, true).show

// output: "col3" is missing at left df1 and added at the end of schema.
// +----+----+----+----+
// |col0|col1|col2|col3|
// +----+----+----+----+
// |   1|   2|   3|NULL|
// |   5|   4|NULL|   6|
// +----+----+----+----+

df2.unionByName(df1, true).show

// output: "col2" is missing at left df2 and added at the end of schema.
// +----+----+----+----+
// |col1|col0|col3|col2|
// +----+----+----+----+
// |   4|   5|   6|NULL|
// |   2|   1|NULL|   3|
// +----+----+----+----+
```

Note that this supports nested columns in struct and array types. With `allowMissingColumns`, missing nested columns of struct columns with the same name will also be filled with null values and added to the end of struct. Nested columns in map types are not currently supported.  

Since
    
3.1.0
  96. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#unpersist\(\):org.apache.spark.sql.Dataset\[T\] "Permalink") abstract  def unpersist(): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Mark the Dataset as non-persistent, and remove all blocks for it from memory and disk.
Mark the Dataset as non-persistent, and remove all blocks for it from memory and disk. This will not un-persist any cached data that is built upon this Dataset.  

Since
    
1.6.0
  97. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#unpersist\(blocking:Boolean\):org.apache.spark.sql.Dataset\[T\] "Permalink") abstract  def unpersist(blocking: Boolean): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Mark the Dataset as non-persistent, and remove all blocks for it from memory and disk.
Mark the Dataset as non-persistent, and remove all blocks for it from memory and disk. This will not un-persist any cached data that is built upon this Dataset.  

blocking
    
Whether to block until all blocks are deleted. 

Since
    
1.6.0
  98. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#unpivot\(ids:Array\[org.apache.spark.sql.Column\],variableColumnName:String,valueColumnName:String\):org.apache.spark.sql.DataFrame "Permalink") abstract  def unpivot(ids: Array[[Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")], variableColumnName: String, valueColumnName: String): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Unpivot a DataFrame from wide format to long format, optionally leaving identifier columns set.
Unpivot a DataFrame from wide format to long format, optionally leaving identifier columns set. This is the reverse to `groupBy(...).pivot(...).agg(...)`, except for the aggregation, which cannot be reversed.  

ids
    
Id columns 

variableColumnName
    
Name of the variable column 

valueColumnName
    
Name of the value column 

Since
    
3.4.0 

See also
    
`org.apache.spark.sql.Dataset.unpivot(Array, Array, String, String)` This is equivalent to calling `Dataset#unpivot(Array, Array, String, String)` where `values` is set to all non-id columns that exist in the DataFrame.
  99. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#unpivot\(ids:Array\[org.apache.spark.sql.Column\],values:Array\[org.apache.spark.sql.Column\],variableColumnName:String,valueColumnName:String\):org.apache.spark.sql.DataFrame "Permalink") abstract  def unpivot(ids: Array[[Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")], values: Array[[Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")], variableColumnName: String, valueColumnName: String): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Unpivot a DataFrame from wide format to long format, optionally leaving identifier columns set.
Unpivot a DataFrame from wide format to long format, optionally leaving identifier columns set. This is the reverse to `groupBy(...).pivot(...).agg(...)`, except for the aggregation, which cannot be reversed.
This function is useful to massage a DataFrame into a format where some columns are identifier columns ("ids"), while all other columns ("values") are "unpivoted" to the rows, leaving just two non-id columns, named as given by `variableColumnName` and `valueColumnName`.

```
val df = Seq((1, 11, 12L), (2, 21, 22L)).toDF("id", "int", "long")
df.show()
// output:
// +---+---+----+
// | id|int|long|
// +---+---+----+
// |  1| 11|  12|
// |  2| 21|  22|
// +---+---+----+

df.unpivot(Array($"id"), Array($"int", $"long"), "variable", "value").show()
// output:
// +---+--------+-----+
// | id|variable|value|
// +---+--------+-----+
// |  1|     int|   11|
// |  1|    long|   12|
// |  2|     int|   21|
// |  2|    long|   22|
// +---+--------+-----+
// schema:
//root
// |-- id: integer (nullable = false)
// |-- variable: string (nullable = false)
// |-- value: long (nullable = true)
```

When no "id" columns are given, the unpivoted DataFrame consists of only the "variable" and "value" columns.
All "value" columns must share a least common data type. Unless they are the same data type, all "value" columns are cast to the nearest common data type. For instance, types `IntegerType` and `LongType` are cast to `LongType`, while `IntegerType` and `StringType` do not have a common data type and `unpivot` fails with an `AnalysisException`.  

ids
    
Id columns 

values
    
Value columns to unpivot 

variableColumnName
    
Name of the variable column 

valueColumnName
    
Name of the value column 

Since
    
3.4.0
  100. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#withColumnsRenamed\(colNames:Seq\[String\],newColNames:Seq\[String\]\):org.apache.spark.sql.DataFrame "Permalink") abstract  def withColumnsRenamed(colNames: Seq[String], newColNames: Seq[String]): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\]) 

Attributes
    protected 
  101. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#withMetadata\(columnName:String,metadata:org.apache.spark.sql.types.Metadata\):org.apache.spark.sql.DataFrame "Permalink") abstract  def withMetadata(columnName: String, metadata: [Metadata](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/types/Metadata.html "org.apache.spark.sql.types.Metadata")): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Returns a new Dataset by updating an existing column with metadata.
Returns a new Dataset by updating an existing column with metadata.  

Since
    
3.3.0
  102. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#withWatermark\(eventTime:String,delayThreshold:String\):org.apache.spark.sql.Dataset\[T\] "Permalink") abstract  def withWatermark(eventTime: String, delayThreshold: String): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Defines an event time watermark for this [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset").
Defines an event time watermark for this [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset"). A watermark tracks a point in time before which we assume no more late data is going to arrive.
Spark will use this watermark for several purposes:
     * To know when a given time window aggregation can be finalized and thus can be emitted when using output modes that do not allow updates.
     * To minimize the amount of state that we need to keep for on-going aggregations, `mapGroupsWithState` and `dropDuplicates` operators. The current watermark is computed by looking at the `MAX(eventTime)` seen across all of the partitions in the query minus a user specified `delayThreshold`. Due to the cost of coordinating this value across partitions, the actual watermark used is only guaranteed to be at least `delayThreshold` behind the actual event time. In some cases we may still process records that arrive more than `delayThreshold` late.  

eventTime
    
the name of the column that contains the event time of the row. 

delayThreshold
    
the minimum delay to wait to data to arrive late, relative to the latest record that has been processed in the form of an interval (e.g. "1 minute" or "5 hours"). NOTE: This should not be negative. 

Since
    
2.1.0
  103. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#write:org.apache.spark.sql.DataFrameWriter\[T\] "Permalink") abstract  def write: [DataFrameWriter](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/DataFrameWriter.html "org.apache.spark.sql.DataFrameWriter")[T]
Interface for saving the content of the non-streaming Dataset out into external storage.
Interface for saving the content of the non-streaming Dataset out into external storage.  

Since
    
1.6.0
  104. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#writeStream:org.apache.spark.sql.streaming.DataStreamWriter\[T\] "Permalink") abstract  def writeStream: [DataStreamWriter](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamWriter.html "org.apache.spark.sql.streaming.DataStreamWriter")[T]
Interface for saving the content of the streaming Dataset out into external storage.
Interface for saving the content of the streaming Dataset out into external storage.  

Since
    
2.0.0
  105. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#writeTo\(table:String\):org.apache.spark.sql.DataFrameWriterV2\[T\] "Permalink") abstract  def writeTo(table: String): [DataFrameWriterV2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/DataFrameWriterV2.html "org.apache.spark.sql.DataFrameWriterV2")[T]
Create a write configuration builder for v2 sources.
Create a write configuration builder for v2 sources.
This builder is used to configure and execute write operations. For example, to append to an existing table, run:

```
df.writeTo("catalog.db.table").append()
```

This can also be used to create or replace existing tables:

```
df.writeTo("catalog.db.table").partitionedBy($"col").createOrReplace()
```


Since
    
3.0.0
  106. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#explode\[A,B\]\(inputColumn:String,outputColumn:String\)\(f:A=>IterableOnce\[B\]\)\(implicitevidence$4:reflect.runtime.universe.TypeTag\[B\]\):org.apache.spark.sql.DataFrame "Permalink") abstract  def explode[A, B](inputColumn: String, outputColumn: String)(f: (A) => IterableOnce[B])(implicit arg0: scala.reflect.api.JavaUniverse.TypeTag[B]): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
(Scala-specific) Returns a new Dataset where a single column has been expanded to zero or more rows by the provided function.
(Scala-specific) Returns a new Dataset where a single column has been expanded to zero or more rows by the provided function. This is similar to a `LATERAL VIEW` in HiveQL. All columns of the input row are implicitly joined with each value that is output by the function.
Given that this is deprecated, as an alternative, you can explode columns either using `functions.explode()`:

```
ds.select(explode(split($"words", " ")).as("word"))
```

or `flatMap()`:

```
ds.flatMap(_.words.split(" "))
```


Annotations
     @deprecated 

Deprecated
    
_(Since version 2.0.0)_ use flatMap() or select() with functions.explode() instead 

Since
    
2.0.0
  107. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#explode\[A<:Product\]\(input:org.apache.spark.sql.Column*\)\(f:org.apache.spark.sql.Row=>IterableOnce\[A\]\)\(implicitevidence$3:reflect.runtime.universe.TypeTag\[A\]\):org.apache.spark.sql.DataFrame "Permalink") abstract  def explode[A <: Product](input: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")*)(f: ([Row](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Row.html "org.apache.spark.sql.Row")) => IterableOnce[A])(implicit arg0: scala.reflect.api.JavaUniverse.TypeTag[A]): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
(Scala-specific) Returns a new Dataset where each row has been expanded to zero or more rows by the provided function.
(Scala-specific) Returns a new Dataset where each row has been expanded to zero or more rows by the provided function. This is similar to a `LATERAL VIEW` in HiveQL. The columns of the input row are implicitly joined with each row that is output by the function.
Given that this is deprecated, as an alternative, you can explode columns either using `functions.explode()` or `flatMap()`. The following example uses these alternatives to count the number of books that contain a given word:

```
case class Book(title: String, words: String)
val ds: Dataset[Book]

val allWords = ds.select($"title", explode(split($"words", " ")).as("word"))

val bookCountPerWord = allWords.groupBy("word").agg(count_distinct("title"))
```

Using `flatMap()` this can similarly be exploded as:

```
ds.flatMap(_.words.split(" "))
```


Annotations
     @deprecated 

Deprecated
    
_(Since version 2.0.0)_ use flatMap() or select() with functions.explode() instead 

Since
    
2.0.0


### Concrete Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html###:Int "Permalink") final  def ##: Int 

Definition Classes
    AnyRef → Any
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#agg\(expr:org.apache.spark.sql.Column,exprs:org.apache.spark.sql.Column*\):org.apache.spark.sql.DataFrame "Permalink") def agg(expr: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column"), exprs: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")*): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Aggregates on the entire Dataset without groups.
Aggregates on the entire Dataset without groups.

```
// ds.agg(...) is a shorthand for ds.groupBy().agg(...)
ds.agg(max($"age"), avg($"salary"))
ds.groupBy().agg(max($"age"), avg($"salary"))
```


Annotations
     @varargs() 

Since
    
2.0.0
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#agg\(exprs:java.util.Map\[String,String\]\):org.apache.spark.sql.DataFrame "Permalink") def agg(exprs: [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#java.util.Map "java.util.Map")[String, String]): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
(Java-specific) Aggregates on the entire Dataset without groups.
(Java-specific) Aggregates on the entire Dataset without groups.

```
// ds.agg(...) is a shorthand for ds.groupBy().agg(...)
ds.agg(Map("age" -> "max", "salary" -> "avg"))
ds.groupBy().agg(Map("age" -> "max", "salary" -> "avg"))
```


Since
    
2.0.0
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#agg\(exprs:Map\[String,String\]\):org.apache.spark.sql.DataFrame "Permalink") def agg(exprs: Map[String, String]): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
(Scala-specific) Aggregates on the entire Dataset without groups.
(Scala-specific) Aggregates on the entire Dataset without groups.

```
// ds.agg(...) is a shorthand for ds.groupBy().agg(...)
ds.agg(Map("age" -> "max", "salary" -> "avg"))
ds.groupBy().agg(Map("age" -> "max", "salary" -> "avg"))
```


Since
    
2.0.0
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#agg\(aggExpr:\(String,String\),aggExprs:\(String,String\)*\):org.apache.spark.sql.DataFrame "Permalink") def agg(aggExpr: (String, String), aggExprs: (String, String)*): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
(Scala-specific) Aggregates on the entire Dataset without groups.
(Scala-specific) Aggregates on the entire Dataset without groups.

```
// ds.agg(...) is a shorthand for ds.groupBy().agg(...)
ds.agg("age" -> "max", "salary" -> "avg")
ds.groupBy().agg("age" -> "max", "salary" -> "avg")
```


Since
    
2.0.0
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#alias\(alias:Symbol\):org.apache.spark.sql.Dataset\[T\] "Permalink") def alias(alias: Symbol): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
(Scala-specific) Returns a new Dataset with an alias set.
(Scala-specific) Returns a new Dataset with an alias set. Same as `as`.  

Since
    
2.0.0
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#alias\(alias:String\):org.apache.spark.sql.Dataset\[T\] "Permalink") def alias(alias: String): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Returns a new Dataset with an alias set.
Returns a new Dataset with an alias set. Same as `as`.  

Since
    
2.0.0
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#apply\(colName:String\):org.apache.spark.sql.Column "Permalink") def apply(colName: String): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Selects column based on the column name and returns it as a [org.apache.spark.sql.Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column").
Selects column based on the column name and returns it as a [org.apache.spark.sql.Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column").  

Since
    
2.0.0 

Note
    
The column name can also reference to a nested column like `a.b`.
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#as\(alias:Symbol\):org.apache.spark.sql.Dataset\[T\] "Permalink") def as(alias: Symbol): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
(Scala-specific) Returns a new Dataset with an alias set.
(Scala-specific) Returns a new Dataset with an alias set.  

Since
    
2.0.0
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0 

Definition Classes
    Any
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#checkpoint\(eager:Boolean\):org.apache.spark.sql.Dataset\[T\] "Permalink") def checkpoint(eager: Boolean): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Returns a checkpointed version of this Dataset.
Returns a checkpointed version of this Dataset. Checkpointing can be used to truncate the logical plan of this Dataset, which is especially useful in iterative algorithms where the plan may grow exponentially. It will be saved to files inside the checkpoint directory set with `SparkContext#setCheckpointDir`.  

eager
    
Whether to checkpoint this dataframe immediately 

Since
    
2.1.0 

Note
    
When checkpoint is used with eager = false, the final data that is checkpointed after the first action may be different from the data that was used during the job due to non-determinism of the underlying operation and retries. If checkpoint is used to achieve saving a deterministic snapshot of the data, eager = true should be used. Otherwise, it is only deterministic after the first execution, after the checkpoint was finalized.
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#checkpoint\(\):org.apache.spark.sql.Dataset\[T\] "Permalink") def checkpoint(): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Eagerly checkpoint a Dataset and return the new Dataset.
Eagerly checkpoint a Dataset and return the new Dataset. Checkpointing can be used to truncate the logical plan of this Dataset, which is especially useful in iterative algorithms where the plan may grow exponentially. It will be saved to files inside the checkpoint directory set with `SparkContext#setCheckpointDir`.  

Since
    
2.1.0
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#clone\(\):Object "Permalink") def clone(): AnyRef 

Attributes
    protected[lang]  

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#columns:Array\[String\] "Permalink") def columns: Array[String]
Returns all column names as an array.
Returns all column names as an array.  

Since
    
1.6.0
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#createGlobalTempView\(viewName:String\):Unit "Permalink") def createGlobalTempView(viewName: String): Unit
Creates a global temporary view using the given name.
Creates a global temporary view using the given name. The lifetime of this temporary view is tied to this Spark application.
Global temporary view is cross-session. Its lifetime is the lifetime of the Spark application, i.e. it will be automatically dropped when the application terminates. It's tied to a system preserved database `global_temp`, and we must use the qualified name to refer a global temp view, e.g. `SELECT * FROM global_temp.view1`.  

Annotations
     @throws("") 

Since
    
2.1.0 

Exceptions thrown
    
[`org.apache.spark.sql.AnalysisException`](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/AnalysisException.html "org.apache.spark.sql.AnalysisException") if the view name is invalid or already exists
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#createOrReplaceGlobalTempView\(viewName:String\):Unit "Permalink") def createOrReplaceGlobalTempView(viewName: String): Unit
Creates or replaces a global temporary view using the given name.
Creates or replaces a global temporary view using the given name. The lifetime of this temporary view is tied to this Spark application.
Global temporary view is cross-session. Its lifetime is the lifetime of the Spark application, i.e. it will be automatically dropped when the application terminates. It's tied to a system preserved database `global_temp`, and we must use the qualified name to refer a global temp view, e.g. `SELECT * FROM global_temp.view1`.  

Since
    
2.2.0
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#createOrReplaceTempView\(viewName:String\):Unit "Permalink") def createOrReplaceTempView(viewName: String): Unit
Creates a local temporary view using the given name.
Creates a local temporary view using the given name. The lifetime of this temporary view is tied to the `SparkSession` that was used to create this Dataset.  

Since
    
2.0.0
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#createTempView\(viewName:String\):Unit "Permalink") def createTempView(viewName: String): Unit
Creates a local temporary view using the given name.
Creates a local temporary view using the given name. The lifetime of this temporary view is tied to the `SparkSession` that was used to create this Dataset.
Local temporary view is session-scoped. Its lifetime is the lifetime of the session that created it, i.e. it will be automatically dropped when the session terminates. It's not tied to any databases, i.e. we can't use `db1.view1` to reference a local temporary view.  

Annotations
     @throws("") 

Since
    
2.0.0 

Exceptions thrown
    
[`org.apache.spark.sql.AnalysisException`](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/AnalysisException.html "org.apache.spark.sql.AnalysisException") if the view name is invalid or already exists
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#cube\(col1:String,cols:String*\):org.apache.spark.sql.RelationalGroupedDataset "Permalink") def cube(col1: String, cols: String*): [RelationalGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/RelationalGroupedDataset.html "org.apache.spark.sql.RelationalGroupedDataset")
Create a multi-dimensional cube for the current Dataset using the specified columns, so we can run aggregation on them.
Create a multi-dimensional cube for the current Dataset using the specified columns, so we can run aggregation on them. See [RelationalGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/RelationalGroupedDataset.html "org.apache.spark.sql.RelationalGroupedDataset") for all the available aggregate functions.
This is a variant of cube that can only group by existing columns using column names (i.e. cannot construct expressions).

```
// Compute the average for all numeric columns cubed by department and group.
ds.cube("department", "group").avg()

// Compute the max age and average salary, cubed by department and gender.
ds.cube($"department", $"gender").agg(Map(
  "salary" -> "avg",
  "age" -> "max"
))
```


Annotations
     @varargs() 

Since
    
2.0.0
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#distinct\(\):org.apache.spark.sql.Dataset\[T\] "Permalink") def distinct(): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Returns a new Dataset that contains only the unique rows from this Dataset.
Returns a new Dataset that contains only the unique rows from this Dataset. This is an alias for `dropDuplicates`.
Note that for a streaming [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset"), this method returns distinct rows only once regardless of the output mode, which the behavior may not be same with `DISTINCT` in SQL against streaming [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset").  

Since
    
2.0.0 

Note
    
Equality checking is performed directly on the encoded representation of the data and thus is not affected by a custom `equals` function defined on `T`.
  23. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#drop\(col:org.apache.spark.sql.Column\):org.apache.spark.sql.DataFrame "Permalink") def drop(col: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Returns a new Dataset with column dropped.
Returns a new Dataset with column dropped.
This method can only be used to drop top level column. This version of drop accepts a [org.apache.spark.sql.Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column") rather than a name. This is a no-op if the Dataset doesn't have a column with an equivalent expression.
Note: `drop(col(colName))` has different semantic with `drop(colName)`, please refer to `Dataset#drop(colName: String)`.  

Since
    
2.0.0
  24. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#drop\(colName:String\):org.apache.spark.sql.DataFrame "Permalink") def drop(colName: String): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Returns a new Dataset with a column dropped.
Returns a new Dataset with a column dropped. This is a no-op if schema doesn't contain column name.
This method can only be used to drop top level columns. the colName string is treated literally without further interpretation.
Note: `drop(colName)` has different semantic with `drop(col(colName))`, for example: 1, multi column have the same colName:

```
val df1 = spark.range(0, 2).withColumn("key1", lit(1))
val df2 = spark.range(0, 2).withColumn("key2", lit(2))
val df3 = df1.join(df2)

df3.show
// +---+----+---+----+
// | id|key1| id|key2|
// +---+----+---+----+
// |  0|   1|  0|   2|
// |  0|   1|  1|   2|
// |  1|   1|  0|   2|
// |  1|   1|  1|   2|
// +---+----+---+----+

df3.drop("id").show()
// output: the two 'id' columns are both dropped.
// |key1|key2|
// +----+----+
// |   1|   2|
// |   1|   2|
// |   1|   2|
// |   1|   2|
// +----+----+

df3.drop(col("id")).show()
// ...AnalysisException: [AMBIGUOUS_REFERENCE] Reference `id` is ambiguous...
```

2, colName contains special characters, like dot.

```
val df = spark.range(0, 2).withColumn("a.b.c", lit(1))

df.show()
// +---+-----+
// | id|a.b.c|
// +---+-----+
// |  0|    1|
// |  1|    1|
// +---+-----+

df.drop("a.b.c").show()
// +---+
// | id|
// +---+
// |  0|
// |  1|
// +---+

df.drop(col("a.b.c")).show()
// no column match the expression 'a.b.c'
// +---+-----+
// | id|a.b.c|
// +---+-----+
// |  0|    1|
// |  1|    1|
// +---+-----+
```


Since
    
2.0.0
  25. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#dropDuplicates\(col1:String,cols:String*\):org.apache.spark.sql.Dataset\[T\] "Permalink") def dropDuplicates(col1: String, cols: String*): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Returns a new [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") with duplicate rows removed, considering only the subset of columns.
Returns a new [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") with duplicate rows removed, considering only the subset of columns.
For a static batch [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset"), it just drops duplicate rows. For a streaming [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset"), it will keep all data across triggers as intermediate state to drop duplicates rows. You can use [withWatermark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#withWatermark\(eventTime:String,delayThreshold:String\):org.apache.spark.sql.Dataset\[T\]) to limit how late the duplicate data can be and system will accordingly limit the state. In addition, too late data older than watermark will be dropped to avoid any possibility of duplicates.  

Annotations
     @varargs() 

Since
    
2.0.0
  26. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#dropDuplicates\(colNames:Array\[String\]\):org.apache.spark.sql.Dataset\[T\] "Permalink") def dropDuplicates(colNames: Array[String]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Returns a new Dataset with duplicate rows removed, considering only the subset of columns.
Returns a new Dataset with duplicate rows removed, considering only the subset of columns.
For a static batch [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset"), it just drops duplicate rows. For a streaming [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset"), it will keep all data across triggers as intermediate state to drop duplicates rows. You can use [withWatermark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#withWatermark\(eventTime:String,delayThreshold:String\):org.apache.spark.sql.Dataset\[T\]) to limit how late the duplicate data can be and system will accordingly limit the state. In addition, too late data older than watermark will be dropped to avoid any possibility of duplicates.  

Since
    
2.0.0
  27. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#dropDuplicatesWithinWatermark\(col1:String,cols:String*\):org.apache.spark.sql.Dataset\[T\] "Permalink") def dropDuplicatesWithinWatermark(col1: String, cols: String*): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Returns a new Dataset with duplicates rows removed, considering only the subset of columns, within watermark.
Returns a new Dataset with duplicates rows removed, considering only the subset of columns, within watermark.
This only works with streaming [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset"), and watermark for the input [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") must be set via [withWatermark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#withWatermark\(eventTime:String,delayThreshold:String\):org.apache.spark.sql.Dataset\[T\]).
For a streaming [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset"), this will keep all data across triggers as intermediate state to drop duplicated rows. The state will be kept to guarantee the semantic, "Events are deduplicated as long as the time distance of earliest and latest events are smaller than the delay threshold of watermark." Users are encouraged to set the delay threshold of watermark longer than max timestamp differences among duplicated events.
Note: too late data older than watermark will be dropped.  

Annotations
     @varargs() 

Since
    
3.5.0
  28. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#dropDuplicatesWithinWatermark\(colNames:Array\[String\]\):org.apache.spark.sql.Dataset\[T\] "Permalink") def dropDuplicatesWithinWatermark(colNames: Array[String]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Returns a new Dataset with duplicates rows removed, considering only the subset of columns, within watermark.
Returns a new Dataset with duplicates rows removed, considering only the subset of columns, within watermark.
This only works with streaming [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset"), and watermark for the input [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") must be set via [withWatermark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#withWatermark\(eventTime:String,delayThreshold:String\):org.apache.spark.sql.Dataset\[T\]).
For a streaming [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset"), this will keep all data across triggers as intermediate state to drop duplicated rows. The state will be kept to guarantee the semantic, "Events are deduplicated as long as the time distance of earliest and latest events are smaller than the delay threshold of watermark." Users are encouraged to set the delay threshold of watermark longer than max timestamp differences among duplicated events.
Note: too late data older than watermark will be dropped.  

Since
    
3.5.0
  29. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#dtypes:Array\[\(String,String\)\] "Permalink") def dtypes: Array[(String, String)]
Returns all column names and their data types as an array.
Returns all column names and their data types as an array.  

Since
    
1.6.0
  30. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  31. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#equals\(x$1:Object\):Boolean "Permalink") def equals(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef → Any
  32. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#exists\(\):org.apache.spark.sql.Column "Permalink") def exists(): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Return a `Column` object for an EXISTS Subquery.
Return a `Column` object for an EXISTS Subquery.
The `exists` method provides a way to create a boolean column that checks for the presence of related records in a subquery. When applied within a `DataFrame`, this method allows you to filter rows based on whether matching records exist in the related dataset. The resulting `Column` object can be used directly in filtering conditions or as a computed column.  

Since
    
4.0.0
  33. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#explain\(\):Unit "Permalink") def explain(): Unit
Prints the physical plan to the console for debugging purposes.
Prints the physical plan to the console for debugging purposes.  

Since
    
1.6.0
  34. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#explain\(extended:Boolean\):Unit "Permalink") def explain(extended: Boolean): Unit
Prints the plans (logical and physical) to the console for debugging purposes.
Prints the plans (logical and physical) to the console for debugging purposes.  

extended
    
default `false`. If `false`, prints only the physical plan. 

Since
    
1.6.0
  35. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#filter\(conditionExpr:String\):org.apache.spark.sql.Dataset\[T\] "Permalink") def filter(conditionExpr: String): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Filters rows using the given SQL expression.
Filters rows using the given SQL expression.

```
peopleDs.filter("age > 15")
```


Since
    
1.6.0
  36. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#first\(\):T "Permalink") def first(): T
Returns the first row.
Returns the first row. Alias for head().  

Since
    
1.6.0
  37. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#flatMap\[U\]\(f:org.apache.spark.api.java.function.FlatMapFunction\[T,U\],encoder:org.apache.spark.sql.Encoder\[U\]\):org.apache.spark.sql.Dataset\[U\] "Permalink") def flatMap[U](f: [FlatMapFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction.html "org.apache.spark.api.java.function.FlatMapFunction")[T, U], encoder: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[U]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[U]
(Java-specific) Returns a new Dataset by first applying a function to all elements of this Dataset, and then flattening the results.
(Java-specific) Returns a new Dataset by first applying a function to all elements of this Dataset, and then flattening the results.  

Since
    
1.6.0
  38. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#flatMap\[U\]\(func:T=>IterableOnce\[U\]\)\(implicitevidence$7:org.apache.spark.sql.Encoder\[U\]\):org.apache.spark.sql.Dataset\[U\] "Permalink") def flatMap[U](func: (T) => IterableOnce[U])(implicit arg0: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[U]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[U]
(Scala-specific) Returns a new Dataset by first applying a function to all elements of this Dataset, and then flattening the results.
(Scala-specific) Returns a new Dataset by first applying a function to all elements of this Dataset, and then flattening the results.  

Since
    
1.6.0
  39. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#foreach\(func:org.apache.spark.api.java.function.ForeachFunction\[T\]\):Unit "Permalink") def foreach(func: [ForeachFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/ForeachFunction.html "org.apache.spark.api.java.function.ForeachFunction")[T]): Unit
(Java-specific) Runs `func` on each element of this Dataset.
(Java-specific) Runs `func` on each element of this Dataset.  

Since
    
1.6.0
  40. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#foreach\(f:T=>Unit\):Unit "Permalink") def foreach(f: (T) => Unit): Unit
Applies a function `f` to all rows.
Applies a function `f` to all rows.  

Since
    
1.6.0
  41. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#foreachPartition\(func:org.apache.spark.api.java.function.ForeachPartitionFunction\[T\]\):Unit "Permalink") def foreachPartition(func: [ForeachPartitionFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/ForeachPartitionFunction.html "org.apache.spark.api.java.function.ForeachPartitionFunction")[T]): Unit
(Java-specific) Runs `func` on each partition of this Dataset.
(Java-specific) Runs `func` on each partition of this Dataset.  

Since
    
1.6.0
  42. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef] 

Definition Classes
    AnyRef → Any 

Annotations
     @IntrinsicCandidate() @native()
  43. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#groupBy\(col1:String,cols:String*\):org.apache.spark.sql.RelationalGroupedDataset "Permalink") def groupBy(col1: String, cols: String*): [RelationalGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/RelationalGroupedDataset.html "org.apache.spark.sql.RelationalGroupedDataset")
Groups the Dataset using the specified columns, so that we can run aggregation on them.
Groups the Dataset using the specified columns, so that we can run aggregation on them. See [RelationalGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/RelationalGroupedDataset.html "org.apache.spark.sql.RelationalGroupedDataset") for all the available aggregate functions.
This is a variant of groupBy that can only group by existing columns using column names (i.e. cannot construct expressions).

```
// Compute the average for all numeric columns grouped by department.
ds.groupBy("department").avg()

// Compute the max age and average salary, grouped by department and gender.
ds.groupBy($"department", $"gender").agg(Map(
  "salary" -> "avg",
  "age" -> "max"
))
```


Annotations
     @varargs() 

Since
    
2.0.0
  44. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#groupByKey\[K\]\(func:org.apache.spark.api.java.function.MapFunction\[T,K\],encoder:org.apache.spark.sql.Encoder\[K\]\):org.apache.spark.sql.KeyValueGroupedDataset\[K,T\] "Permalink") def groupByKey[K](func: [MapFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/MapFunction.html "org.apache.spark.api.java.function.MapFunction")[T, K], encoder: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[K]): [KeyValueGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html "org.apache.spark.sql.KeyValueGroupedDataset")[K, T]
(Java-specific) Returns a [KeyValueGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html "org.apache.spark.sql.KeyValueGroupedDataset") where the data is grouped by the given key `func`.
(Java-specific) Returns a [KeyValueGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html "org.apache.spark.sql.KeyValueGroupedDataset") where the data is grouped by the given key `func`.  

Since
    
2.0.0
  45. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#hashCode\(\):Int "Permalink") def hashCode(): Int 

Definition Classes
    AnyRef → Any 

Annotations
     @IntrinsicCandidate() @native()
  46. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#head\(\):T "Permalink") def head(): T
Returns the first row.
Returns the first row.  

Since
    
1.6.0
  47. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean 

Definition Classes
    Any
  48. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#javaRDD:org.apache.spark.api.java.JavaRDD\[T\] "Permalink") def javaRDD: [JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[T]
Returns the content of the Dataset as a `JavaRDD` of `T`s.
Returns the content of the Dataset as a `JavaRDD` of `T`s.  

Annotations
     @ClassicOnly() 

Since
    
1.6.0 

Note
    
this is only supported in Classic.
  49. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#join\(right:org.apache.spark.sql.Dataset\[_\],joinExprs:org.apache.spark.sql.Column\):org.apache.spark.sql.DataFrame "Permalink") def join(right: [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[_], joinExprs: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Inner join with another `DataFrame`, using the given join expression.
Inner join with another `DataFrame`, using the given join expression.

```
// The following two are equivalent:
df1.join(df2, $"df1Key" === $"df2Key")
df1.join(df2).where($"df1Key" === $"df2Key")
```


Since
    
2.0.0
  50. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#join\(right:org.apache.spark.sql.Dataset\[_\],usingColumns:Array\[String\],joinType:String\):org.apache.spark.sql.DataFrame "Permalink") def join(right: [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[_], usingColumns: Array[String], joinType: String): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
(Java-specific) Equi-join with another `DataFrame` using the given columns.
(Java-specific) Equi-join with another `DataFrame` using the given columns. See the Scala-specific overload for more details.  

right
    
Right side of the join operation. 

usingColumns
    
Names of the columns to join on. This columns must exist on both sides. 

joinType
    
Type of join to perform. Default `inner`. Must be one of: `inner`, `cross`, `outer`, `full`, `fullouter`, `full_outer`, `left`, `leftouter`, `left_outer`, `right`, `rightouter`, `right_outer`, `semi`, `leftsemi`, `left_semi`, `anti`, `leftanti`, `left_anti`. 

Since
    
3.4.0
  51. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#join\(right:org.apache.spark.sql.Dataset\[_\],usingColumn:String,joinType:String\):org.apache.spark.sql.DataFrame "Permalink") def join(right: [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[_], usingColumn: String, joinType: String): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Equi-join with another `DataFrame` using the given column.
Equi-join with another `DataFrame` using the given column. A cross join with a predicate is specified as an inner join. If you would explicitly like to perform a cross join use the `crossJoin` method.
Different from other join functions, the join column will only appear once in the output, i.e. similar to SQL's `JOIN USING` syntax.  

right
    
Right side of the join operation. 

usingColumn
    
Name of the column to join on. This column must exist on both sides. 

joinType
    
Type of join to perform. Default `inner`. Must be one of: `inner`, `cross`, `outer`, `full`, `fullouter`, `full_outer`, `left`, `leftouter`, `left_outer`, `right`, `rightouter`, `right_outer`, `semi`, `leftsemi`, `left_semi`, `anti`, `leftanti`, `left_anti`. 

Since
    
3.4.0 

Note
    
If you perform a self-join using this function without aliasing the input `DataFrame`s, you will NOT be able to reference any columns after the join, since there is no way to disambiguate which side of the join you would like to reference.
  52. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#join\(right:org.apache.spark.sql.Dataset\[_\],usingColumns:Seq\[String\]\):org.apache.spark.sql.DataFrame "Permalink") def join(right: [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[_], usingColumns: Seq[String]): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
(Scala-specific) Inner equi-join with another `DataFrame` using the given columns.
(Scala-specific) Inner equi-join with another `DataFrame` using the given columns.
Different from other join functions, the join columns will only appear once in the output, i.e. similar to SQL's `JOIN USING` syntax.

```
// Joining df1 and df2 using the columns "user_id" and "user_name"
df1.join(df2, Seq("user_id", "user_name"))
```


right
    
Right side of the join operation. 

usingColumns
    
Names of the columns to join on. This columns must exist on both sides. 

Since
    
2.0.0 

Note
    
If you perform a self-join using this function without aliasing the input `DataFrame`s, you will NOT be able to reference any columns after the join, since there is no way to disambiguate which side of the join you would like to reference.
  53. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#join\(right:org.apache.spark.sql.Dataset\[_\],usingColumns:Array\[String\]\):org.apache.spark.sql.DataFrame "Permalink") def join(right: [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[_], usingColumns: Array[String]): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
(Java-specific) Inner equi-join with another `DataFrame` using the given columns.
(Java-specific) Inner equi-join with another `DataFrame` using the given columns. See the Scala-specific overload for more details.  

right
    
Right side of the join operation. 

usingColumns
    
Names of the columns to join on. This columns must exist on both sides. 

Since
    
3.4.0
  54. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#join\(right:org.apache.spark.sql.Dataset\[_\],usingColumn:String\):org.apache.spark.sql.DataFrame "Permalink") def join(right: [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[_], usingColumn: String): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Inner equi-join with another `DataFrame` using the given column.
Inner equi-join with another `DataFrame` using the given column.
Different from other join functions, the join column will only appear once in the output, i.e. similar to SQL's `JOIN USING` syntax.

```
// Joining df1 and df2 using the column "user_id"
df1.join(df2, "user_id")
```


right
    
Right side of the join operation. 

usingColumn
    
Name of the column to join on. This column must exist on both sides. 

Since
    
2.0.0 

Note
    
If you perform a self-join using this function without aliasing the input `DataFrame`s, you will NOT be able to reference any columns after the join, since there is no way to disambiguate which side of the join you would like to reference.
  55. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#joinWith\[U\]\(other:org.apache.spark.sql.Dataset\[U\],condition:org.apache.spark.sql.Column\):org.apache.spark.sql.Dataset\[\(T,U\)\] "Permalink") def joinWith[U](other: [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[U], condition: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[(T, U)]
Using inner equi-join to join this Dataset returning a `Tuple2` for each pair where `condition` evaluates to true.
Using inner equi-join to join this Dataset returning a `Tuple2` for each pair where `condition` evaluates to true.  

other
    
Right side of the join. 

condition
    
Join expression. 

Since
    
1.6.0
  56. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#localCheckpoint\(eager:Boolean,storageLevel:org.apache.spark.storage.StorageLevel\):org.apache.spark.sql.Dataset\[T\] "Permalink") def localCheckpoint(eager: Boolean, storageLevel: [StorageLevel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StorageLevel.html "org.apache.spark.storage.StorageLevel")): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Locally checkpoints a Dataset and return the new Dataset.
Locally checkpoints a Dataset and return the new Dataset. Checkpointing can be used to truncate the logical plan of this Dataset, which is especially useful in iterative algorithms where the plan may grow exponentially. Local checkpoints are written to executor storage and despite potentially faster they are unreliable and may compromise job completion.  

eager
    
Whether to checkpoint this dataframe immediately 

storageLevel
    
StorageLevel with which to checkpoint the data. 

Since
    
4.0.0 

Note
    
When checkpoint is used with eager = false, the final data that is checkpointed after the first action may be different from the data that was used during the job due to non-determinism of the underlying operation and retries. If checkpoint is used to achieve saving a deterministic snapshot of the data, eager = true should be used. Otherwise, it is only deterministic after the first execution, after the checkpoint was finalized.
  57. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#localCheckpoint\(eager:Boolean\):org.apache.spark.sql.Dataset\[T\] "Permalink") def localCheckpoint(eager: Boolean): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Locally checkpoints a Dataset and return the new Dataset.
Locally checkpoints a Dataset and return the new Dataset. Checkpointing can be used to truncate the logical plan of this Dataset, which is especially useful in iterative algorithms where the plan may grow exponentially. Local checkpoints are written to executor storage and despite potentially faster they are unreliable and may compromise job completion.  

eager
    
Whether to checkpoint this dataframe immediately 

Since
    
2.3.0 

Note
    
When checkpoint is used with eager = false, the final data that is checkpointed after the first action may be different from the data that was used during the job due to non-determinism of the underlying operation and retries. If checkpoint is used to achieve saving a deterministic snapshot of the data, eager = true should be used. Otherwise, it is only deterministic after the first execution, after the checkpoint was finalized.
  58. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#localCheckpoint\(\):org.apache.spark.sql.Dataset\[T\] "Permalink") def localCheckpoint(): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Eagerly locally checkpoints a Dataset and return the new Dataset.
Eagerly locally checkpoints a Dataset and return the new Dataset. Checkpointing can be used to truncate the logical plan of this Dataset, which is especially useful in iterative algorithms where the plan may grow exponentially. Local checkpoints are written to executor storage and despite potentially faster they are unreliable and may compromise job completion.  

Since
    
2.3.0
  59. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#mapPartitions\[U\]\(f:org.apache.spark.api.java.function.MapPartitionsFunction\[T,U\],encoder:org.apache.spark.sql.Encoder\[U\]\):org.apache.spark.sql.Dataset\[U\] "Permalink") def mapPartitions[U](f: [MapPartitionsFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/MapPartitionsFunction.html "org.apache.spark.api.java.function.MapPartitionsFunction")[T, U], encoder: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[U]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[U]
(Java-specific) Returns a new Dataset that contains the result of applying `f` to each partition.
(Java-specific) Returns a new Dataset that contains the result of applying `f` to each partition.  

Since
    
1.6.0
  60. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#melt\(ids:Array\[org.apache.spark.sql.Column\],variableColumnName:String,valueColumnName:String\):org.apache.spark.sql.DataFrame "Permalink") def melt(ids: Array[[Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")], variableColumnName: String, valueColumnName: String): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Unpivot a DataFrame from wide format to long format, optionally leaving identifier columns set.
Unpivot a DataFrame from wide format to long format, optionally leaving identifier columns set. This is the reverse to `groupBy(...).pivot(...).agg(...)`, except for the aggregation, which cannot be reversed. This is an alias for `unpivot`.  

ids
    
Id columns 

variableColumnName
    
Name of the variable column 

valueColumnName
    
Name of the value column 

Since
    
3.4.0 

See also
    
`org.apache.spark.sql.Dataset.unpivot(Array, Array, String, String)` This is equivalent to calling `Dataset#unpivot(Array, Array, String, String)` where `values` is set to all non-id columns that exist in the DataFrame.
  61. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#melt\(ids:Array\[org.apache.spark.sql.Column\],values:Array\[org.apache.spark.sql.Column\],variableColumnName:String,valueColumnName:String\):org.apache.spark.sql.DataFrame "Permalink") def melt(ids: Array[[Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")], values: Array[[Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")], variableColumnName: String, valueColumnName: String): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Unpivot a DataFrame from wide format to long format, optionally leaving identifier columns set.
Unpivot a DataFrame from wide format to long format, optionally leaving identifier columns set. This is the reverse to `groupBy(...).pivot(...).agg(...)`, except for the aggregation, which cannot be reversed. This is an alias for `unpivot`.  

ids
    
Id columns 

values
    
Value columns to unpivot 

variableColumnName
    
Name of the variable column 

valueColumnName
    
Name of the value column 

Since
    
3.4.0 

See also
    
`org.apache.spark.sql.Dataset.unpivot(Array, Array, String, String)`
  62. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  63. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#notify\(\):Unit "Permalink") final  def notify(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  64. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  65. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#orderBy\(sortExprs:org.apache.spark.sql.Column*\):org.apache.spark.sql.Dataset\[T\] "Permalink") def orderBy(sortExprs: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")*): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Returns a new Dataset sorted by the given expressions.
Returns a new Dataset sorted by the given expressions. This is an alias of the `sort` function.  

Annotations
     @varargs() 

Since
    
2.0.0
  66. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#orderBy\(sortCol:String,sortCols:String*\):org.apache.spark.sql.Dataset\[T\] "Permalink") def orderBy(sortCol: String, sortCols: String*): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Returns a new Dataset sorted by the given expressions.
Returns a new Dataset sorted by the given expressions. This is an alias of the `sort` function.  

Annotations
     @varargs() 

Since
    
2.0.0
  67. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#printSchema\(level:Int\):Unit "Permalink") def printSchema(level: Int): Unit
Prints the schema up to the given level to the console in a nice tree format.
Prints the schema up to the given level to the console in a nice tree format.  

Since
    
3.0.0
  68. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#printSchema\(\):Unit "Permalink") def printSchema(): Unit
Prints the schema to the console in a nice tree format.
Prints the schema to the console in a nice tree format.  

Since
    
1.6.0
  69. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#reduce\(func:org.apache.spark.api.java.function.ReduceFunction\[T\]\):T "Permalink") def reduce(func: [ReduceFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/ReduceFunction.html "org.apache.spark.api.java.function.ReduceFunction")[T]): T
(Java-specific) Reduces the elements of this Dataset using the specified binary function.
(Java-specific) Reduces the elements of this Dataset using the specified binary function. The given `func` must be commutative and associative or the result may be non-deterministic.  

Since
    
1.6.0
  70. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#repartition\(partitionExprs:org.apache.spark.sql.Column*\):org.apache.spark.sql.Dataset\[T\] "Permalink") def repartition(partitionExprs: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")*): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Returns a new Dataset partitioned by the given partitioning expressions, using `spark.sql.shuffle.partitions` as number of partitions.
Returns a new Dataset partitioned by the given partitioning expressions, using `spark.sql.shuffle.partitions` as number of partitions. The resulting Dataset is hash partitioned.
This is the same operation as "DISTRIBUTE BY" in SQL (Hive QL).  

Annotations
     @varargs() 

Since
    
2.0.0
  71. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#repartition\(numPartitions:Int,partitionExprs:org.apache.spark.sql.Column*\):org.apache.spark.sql.Dataset\[T\] "Permalink") def repartition(numPartitions: Int, partitionExprs: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")*): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Returns a new Dataset partitioned by the given partitioning expressions into `numPartitions`.
Returns a new Dataset partitioned by the given partitioning expressions into `numPartitions`. The resulting Dataset is hash partitioned.
This is the same operation as "DISTRIBUTE BY" in SQL (Hive QL).  

Annotations
     @varargs() 

Since
    
2.0.0
  72. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#repartitionByRange\(partitionExprs:org.apache.spark.sql.Column*\):org.apache.spark.sql.Dataset\[T\] "Permalink") def repartitionByRange(partitionExprs: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")*): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Returns a new Dataset partitioned by the given partitioning expressions, using `spark.sql.shuffle.partitions` as number of partitions.
Returns a new Dataset partitioned by the given partitioning expressions, using `spark.sql.shuffle.partitions` as number of partitions. The resulting Dataset is range partitioned.
At least one partition-by expression must be specified. When no explicit sort order is specified, "ascending nulls first" is assumed. Note, the rows are not sorted in each partition of the resulting Dataset.
Note that due to performance reasons this method uses sampling to estimate the ranges. Hence, the output may not be consistent, since sampling can return different values. The sample size can be controlled by the config `spark.sql.execution.rangeExchange.sampleSizePerPartition`.  

Annotations
     @varargs() 

Since
    
2.3.0
  73. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#repartitionByRange\(numPartitions:Int,partitionExprs:org.apache.spark.sql.Column*\):org.apache.spark.sql.Dataset\[T\] "Permalink") def repartitionByRange(numPartitions: Int, partitionExprs: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")*): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Returns a new Dataset partitioned by the given partitioning expressions into `numPartitions`.
Returns a new Dataset partitioned by the given partitioning expressions into `numPartitions`. The resulting Dataset is range partitioned.
At least one partition-by expression must be specified. When no explicit sort order is specified, "ascending nulls first" is assumed. Note, the rows are not sorted in each partition of the resulting Dataset.
Note that due to performance reasons this method uses sampling to estimate the ranges. Hence, the output may not be consistent, since sampling can return different values. The sample size can be controlled by the config `spark.sql.execution.rangeExchange.sampleSizePerPartition`.  

Annotations
     @varargs() 

Since
    
2.3.0
  74. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#rollup\(col1:String,cols:String*\):org.apache.spark.sql.RelationalGroupedDataset "Permalink") def rollup(col1: String, cols: String*): [RelationalGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/RelationalGroupedDataset.html "org.apache.spark.sql.RelationalGroupedDataset")
Create a multi-dimensional rollup for the current Dataset using the specified columns, so we can run aggregation on them.
Create a multi-dimensional rollup for the current Dataset using the specified columns, so we can run aggregation on them. See [RelationalGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/RelationalGroupedDataset.html "org.apache.spark.sql.RelationalGroupedDataset") for all the available aggregate functions.
This is a variant of rollup that can only group by existing columns using column names (i.e. cannot construct expressions).

```
// Compute the average for all numeric columns rolled up by department and group.
ds.rollup("department", "group").avg()

// Compute the max age and average salary, rolled up by department and gender.
ds.rollup($"department", $"gender").agg(Map(
  "salary" -> "avg",
  "age" -> "max"
))
```


Annotations
     @varargs() 

Since
    
2.0.0
  75. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#sample\(withReplacement:Boolean,fraction:Double\):org.apache.spark.sql.Dataset\[T\] "Permalink") def sample(withReplacement: Boolean, fraction: Double): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Returns a new [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") by sampling a fraction of rows, using a random seed.
Returns a new [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") by sampling a fraction of rows, using a random seed.  

withReplacement
    
Sample with replacement or not. 

fraction
    
Fraction of rows to generate, range [0.0, 1.0]. 

Since
    
1.6.0 

Note
    
This is NOT guaranteed to provide exactly the fraction of the total count of the given [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset").
  76. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#sample\(fraction:Double\):org.apache.spark.sql.Dataset\[T\] "Permalink") def sample(fraction: Double): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Returns a new [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") by sampling a fraction of rows (without replacement), using a random seed.
Returns a new [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") by sampling a fraction of rows (without replacement), using a random seed.  

fraction
    
Fraction of rows to generate, range [0.0, 1.0]. 

Since
    
2.3.0 

Note
    
This is NOT guaranteed to provide exactly the fraction of the count of the given [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset").
  77. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#sample\(fraction:Double,seed:Long\):org.apache.spark.sql.Dataset\[T\] "Permalink") def sample(fraction: Double, seed: Long): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Returns a new [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") by sampling a fraction of rows (without replacement), using a user-supplied seed.
Returns a new [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") by sampling a fraction of rows (without replacement), using a user-supplied seed.  

fraction
    
Fraction of rows to generate, range [0.0, 1.0]. 

seed
    
Seed for sampling. 

Since
    
2.3.0 

Note
    
This is NOT guaranteed to provide exactly the fraction of the count of the given [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset").
  78. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#scalar\(\):org.apache.spark.sql.Column "Permalink") def scalar(): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Return a `Column` object for a SCALAR Subquery containing exactly one row and one column.
Return a `Column` object for a SCALAR Subquery containing exactly one row and one column.
The `scalar()` method is useful for extracting a `Column` object that represents a scalar value from a DataFrame, especially when the DataFrame results from an aggregation or single-value computation. This returned `Column` can then be used directly in `select` clauses or as predicates in filters on the outer DataFrame, enabling dynamic data filtering and calculations based on scalar values.  

Since
    
4.0.0
  79. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#select\[U1,U2,U3,U4,U5\]\(c1:org.apache.spark.sql.TypedColumn\[T,U1\],c2:org.apache.spark.sql.TypedColumn\[T,U2\],c3:org.apache.spark.sql.TypedColumn\[T,U3\],c4:org.apache.spark.sql.TypedColumn\[T,U4\],c5:org.apache.spark.sql.TypedColumn\[T,U5\]\):org.apache.spark.sql.Dataset\[\(U1,U2,U3,U4,U5\)\] "Permalink") def select[U1, U2, U3, U4, U5](c1: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[T, U1], c2: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[T, U2], c3: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[T, U3], c4: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[T, U4], c5: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[T, U5]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[(U1, U2, U3, U4, U5)]
Returns a new Dataset by computing the given [org.apache.spark.sql.Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column") expressions for each element.
Returns a new Dataset by computing the given [org.apache.spark.sql.Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column") expressions for each element.  

Since
    
1.6.0
  80. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#select\[U1,U2,U3,U4\]\(c1:org.apache.spark.sql.TypedColumn\[T,U1\],c2:org.apache.spark.sql.TypedColumn\[T,U2\],c3:org.apache.spark.sql.TypedColumn\[T,U3\],c4:org.apache.spark.sql.TypedColumn\[T,U4\]\):org.apache.spark.sql.Dataset\[\(U1,U2,U3,U4\)\] "Permalink") def select[U1, U2, U3, U4](c1: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[T, U1], c2: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[T, U2], c3: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[T, U3], c4: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[T, U4]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[(U1, U2, U3, U4)]
Returns a new Dataset by computing the given [org.apache.spark.sql.Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column") expressions for each element.
Returns a new Dataset by computing the given [org.apache.spark.sql.Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column") expressions for each element.  

Since
    
1.6.0
  81. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#select\[U1,U2,U3\]\(c1:org.apache.spark.sql.TypedColumn\[T,U1\],c2:org.apache.spark.sql.TypedColumn\[T,U2\],c3:org.apache.spark.sql.TypedColumn\[T,U3\]\):org.apache.spark.sql.Dataset\[\(U1,U2,U3\)\] "Permalink") def select[U1, U2, U3](c1: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[T, U1], c2: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[T, U2], c3: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[T, U3]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[(U1, U2, U3)]
Returns a new Dataset by computing the given [org.apache.spark.sql.Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column") expressions for each element.
Returns a new Dataset by computing the given [org.apache.spark.sql.Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column") expressions for each element.  

Since
    
1.6.0
  82. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#select\[U1,U2\]\(c1:org.apache.spark.sql.TypedColumn\[T,U1\],c2:org.apache.spark.sql.TypedColumn\[T,U2\]\):org.apache.spark.sql.Dataset\[\(U1,U2\)\] "Permalink") def select[U1, U2](c1: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[T, U1], c2: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[T, U2]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[(U1, U2)]
Returns a new Dataset by computing the given [org.apache.spark.sql.Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column") expressions for each element.
Returns a new Dataset by computing the given [org.apache.spark.sql.Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column") expressions for each element.  

Since
    
1.6.0
  83. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#select\(col:String,cols:String*\):org.apache.spark.sql.DataFrame "Permalink") def select(col: String, cols: String*): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Selects a set of columns.
Selects a set of columns. This is a variant of `select` that can only select existing columns using column names (i.e. cannot construct expressions).

```
// The following two are equivalent:
ds.select("colA", "colB")
ds.select($"colA", $"colB")
```


Annotations
     @varargs() 

Since
    
2.0.0
  84. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#selectExpr\(exprs:String*\):org.apache.spark.sql.DataFrame "Permalink") def selectExpr(exprs: String*): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Selects a set of SQL expressions.
Selects a set of SQL expressions. This is a variant of `select` that accepts SQL expressions.

```
// The following are equivalent:
ds.selectExpr("colA", "colB as newName", "abs(colC)")
ds.select(expr("colA"), expr("colB as newName"), expr("abs(colC)"))
```


Annotations
     @varargs() 

Since
    
2.0.0
  85. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#show\(numRows:Int,truncate:Int\):Unit "Permalink") def show(numRows: Int, truncate: Int): Unit
Displays the Dataset in a tabular form.
Displays the Dataset in a tabular form. For example:

```
year  month AVG('Adj Close) MAX('Adj Close)
1980  12    0.503218        0.595103
1981  01    0.523289        0.570307
1982  02    0.436504        0.475256
1983  03    0.410516        0.442194
1984  04    0.450090        0.483521
```


numRows
    
Number of rows to show 

truncate
    
If set to more than 0, truncates strings to `truncate` characters and all cells will be aligned right. 

Since
    
1.6.0
  86. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#show\(truncate:Boolean\):Unit "Permalink") def show(truncate: Boolean): Unit
Displays the top 20 rows of Dataset in a tabular form.
Displays the top 20 rows of Dataset in a tabular form.  

truncate
    
Whether truncate long strings. If true, strings more than 20 characters will be truncated and all cells will be aligned right 

Since
    
1.6.0
  87. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#show\(\):Unit "Permalink") def show(): Unit
Displays the top 20 rows of Dataset in a tabular form.
Displays the top 20 rows of Dataset in a tabular form. Strings more than 20 characters will be truncated, and all cells will be aligned right.  

Since
    
1.6.0
  88. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#show\(numRows:Int\):Unit "Permalink") def show(numRows: Int): Unit
Displays the Dataset in a tabular form.
Displays the Dataset in a tabular form. Strings more than 20 characters will be truncated, and all cells will be aligned right. For example:

```
year  month AVG('Adj Close) MAX('Adj Close)
1980  12    0.503218        0.595103
1981  01    0.523289        0.570307
1982  02    0.436504        0.475256
1983  03    0.410516        0.442194
1984  04    0.450090        0.483521
```


numRows
    
Number of rows to show 

Since
    
1.6.0
  89. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#sort\(sortExprs:org.apache.spark.sql.Column*\):org.apache.spark.sql.Dataset\[T\] "Permalink") def sort(sortExprs: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")*): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Returns a new Dataset sorted by the given expressions.
Returns a new Dataset sorted by the given expressions. For example:

```
ds.sort($"col1", $"col2".desc)
```


Annotations
     @varargs() 

Since
    
2.0.0
  90. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#sort\(sortCol:String,sortCols:String*\):org.apache.spark.sql.Dataset\[T\] "Permalink") def sort(sortCol: String, sortCols: String*): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Returns a new Dataset sorted by the specified column, all in ascending order.
Returns a new Dataset sorted by the specified column, all in ascending order.

```
// The following 3 are equivalent
ds.sort("sortcol")
ds.sort($"sortcol")
ds.sort($"sortcol".asc)
```


Annotations
     @varargs() 

Since
    
2.0.0
  91. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#sortWithinPartitions\(sortExprs:org.apache.spark.sql.Column*\):org.apache.spark.sql.Dataset\[T\] "Permalink") def sortWithinPartitions(sortExprs: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")*): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Returns a new Dataset with each partition sorted by the given expressions.
Returns a new Dataset with each partition sorted by the given expressions.
This is the same operation as "SORT BY" in SQL (Hive QL).  

Annotations
     @varargs() 

Since
    
2.0.0
  92. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#sortWithinPartitions\(sortCol:String,sortCols:String*\):org.apache.spark.sql.Dataset\[T\] "Permalink") def sortWithinPartitions(sortCol: String, sortCols: String*): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Returns a new Dataset with each partition sorted by the given expressions.
Returns a new Dataset with each partition sorted by the given expressions.
This is the same operation as "SORT BY" in SQL (Hive QL).  

Annotations
     @varargs() 

Since
    
2.0.0
  93. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0 

Definition Classes
    AnyRef
  94. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#take\(n:Int\):Array\[T\] "Permalink") def take(n: Int): Array[T]
Returns the first `n` rows in the Dataset.
Returns the first `n` rows in the Dataset.
Running take requires moving data into the application's driver process, and doing so with a very large `n` can crash the driver process with OutOfMemoryError.  

Since
    
1.6.0
  95. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#takeAsList\(n:Int\):java.util.List\[T\] "Permalink") def takeAsList(n: Int): [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#java.util.List "java.util.List")[T]
Returns the first `n` rows in the Dataset as a list.
Returns the first `n` rows in the Dataset as a list.
Running take requires moving data into the application's driver process, and doing so with a very large `n` can crash the driver process with OutOfMemoryError.  

Since
    
1.6.0
  96. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#toString\(\):String "Permalink") def toString(): [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String") 

Definition Classes
    AnyRef → Any
  97. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#transform\[U,DSO\[_\]<:org.apache.spark.sql.Dataset\[_\]\]\(t:Dataset.this.type=>DSO\[U\]\):DSO\[U\] "Permalink") def transform[U, DSO[_] <: [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[_]](t: ([Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset").this.type) => DSO[U]): DSO[U]
Concise syntax for chaining custom transformations.
Concise syntax for chaining custom transformations.

```
def featurize(ds: Dataset[T]): Dataset[U] = ...

ds
  .transform(featurize)
  .transform(...)
```


Since
    
1.6.0
  98. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#unionAll\(other:org.apache.spark.sql.Dataset\[T\]\):org.apache.spark.sql.Dataset\[T\] "Permalink") def unionAll(other: [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Returns a new Dataset containing union of rows in this Dataset and another Dataset.
Returns a new Dataset containing union of rows in this Dataset and another Dataset. This is an alias for `union`.
This is equivalent to `UNION ALL` in SQL. To do a SQL-style set union (that does deduplication of elements), use this function followed by a [distinct](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#distinct\(\):org.apache.spark.sql.Dataset\[T\]).
Also as standard in SQL, this function resolves columns by position (not by name).  

Since
    
2.0.0
  99. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#unionByName\(other:org.apache.spark.sql.Dataset\[T\]\):org.apache.spark.sql.Dataset\[T\] "Permalink") def unionByName(other: [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Returns a new Dataset containing union of rows in this Dataset and another Dataset.
Returns a new Dataset containing union of rows in this Dataset and another Dataset.
This is different from both `UNION ALL` and `UNION DISTINCT` in SQL. To do a SQL-style set union (that does deduplication of elements), use this function followed by a [distinct](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#distinct\(\):org.apache.spark.sql.Dataset\[T\]).
The difference between this function and [union](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#union\(other:org.apache.spark.sql.Dataset\[T\]\):org.apache.spark.sql.Dataset\[T\]) is that this function resolves columns by name (not by position):

```
val df1 = Seq((1, 2, 3)).toDF("col0", "col1", "col2")
val df2 = Seq((4, 5, 6)).toDF("col1", "col2", "col0")
df1.unionByName(df2).show

// output:
// +----+----+----+
// |col0|col1|col2|
// +----+----+----+
// |   1|   2|   3|
// |   6|   4|   5|
// +----+----+----+
```

Note that this supports nested columns in struct and array types. Nested columns in map types are not currently supported.  

Since
    
2.3.0
  100. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  101. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  102. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#wait\(\):Unit "Permalink") final  def wait(): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  103. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#where\(conditionExpr:String\):org.apache.spark.sql.Dataset\[T\] "Permalink") def where(conditionExpr: String): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Filters rows using the given SQL expression.
Filters rows using the given SQL expression.

```
peopleDs.where("age > 15")
```


Since
    
1.6.0
  104. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#where\(condition:org.apache.spark.sql.Column\):org.apache.spark.sql.Dataset\[T\] "Permalink") def where(condition: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Filters rows using the given condition.
Filters rows using the given condition. This is an alias for `filter`.

```
// The following are equivalent:
peopleDs.filter($"age" > 15)
peopleDs.where($"age" > 15)
```


Since
    
1.6.0
  105. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#withColumn\(colName:String,col:org.apache.spark.sql.Column\):org.apache.spark.sql.DataFrame "Permalink") def withColumn(colName: String, col: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Returns a new Dataset by adding a column or replacing the existing column that has the same name.
Returns a new Dataset by adding a column or replacing the existing column that has the same name.
`column`'s expression must only refer to attributes supplied by this Dataset. It is an error to add a column that refers to some other Dataset.  

Since
    
2.0.0 

Note
    
this method introduces a projection internally. Therefore, calling it multiple times, for instance, via loops in order to add multiple columns can generate big plans which can cause performance issues and even `StackOverflowException`. To avoid this, use `select` with the multiple columns at once.
  106. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#withColumnRenamed\(existingName:String,newName:String\):org.apache.spark.sql.DataFrame "Permalink") def withColumnRenamed(existingName: String, newName: String): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Returns a new Dataset with a column renamed.
Returns a new Dataset with a column renamed. This is a no-op if schema doesn't contain existingName.  

Since
    
2.0.0
  107. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#withColumns\(colsMap:java.util.Map\[String,org.apache.spark.sql.Column\]\):org.apache.spark.sql.DataFrame "Permalink") def withColumns(colsMap: [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#java.util.Map "java.util.Map")[String, [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")]): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
(Java-specific) Returns a new Dataset by adding columns or replacing the existing columns that has the same names.
(Java-specific) Returns a new Dataset by adding columns or replacing the existing columns that has the same names.
`colsMap` is a map of column name and column, the column must only refer to attribute supplied by this Dataset. It is an error to add columns that refers to some other Dataset.  

Since
    
3.3.0
  108. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#withColumns\(colsMap:Map\[String,org.apache.spark.sql.Column\]\):org.apache.spark.sql.DataFrame "Permalink") def withColumns(colsMap: Map[String, [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")]): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
(Scala-specific) Returns a new Dataset by adding columns or replacing the existing columns that has the same names.
(Scala-specific) Returns a new Dataset by adding columns or replacing the existing columns that has the same names.
`colsMap` is a map of column name and column, the column must only refer to attributes supplied by this Dataset. It is an error to add columns that refers to some other Dataset.  

Since
    
3.3.0
  109. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#withColumnsRenamed\(colsMap:java.util.Map\[String,String\]\):org.apache.spark.sql.DataFrame "Permalink") def withColumnsRenamed(colsMap: [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#java.util.Map "java.util.Map")[String, String]): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
(Java-specific) Returns a new Dataset with a columns renamed.
(Java-specific) Returns a new Dataset with a columns renamed. This is a no-op if schema doesn't contain existingName.
`colsMap` is a map of existing column name and new column name.  

Since
    
3.4.0
  110. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#withColumnsRenamed\(colsMap:Map\[String,String\]\):org.apache.spark.sql.DataFrame "Permalink") def withColumnsRenamed(colsMap: Map[String, String]): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
(Scala-specific) Returns a new Dataset with a columns renamed.
(Scala-specific) Returns a new Dataset with a columns renamed. This is a no-op if schema doesn't contain existingName.
`colsMap` is a map of existing column name and new column name.  

Annotations
     @throws("") 

Since
    
3.4.0 

Exceptions thrown
    
[`org.apache.spark.sql.AnalysisException`](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/AnalysisException.html "org.apache.spark.sql.AnalysisException") if there are duplicate names in resulting projection


### Deprecated Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#finalize\(\):Unit "Permalink") def finalize(): Unit 

Attributes
    protected[lang]  

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.Throwable]) @Deprecated 

Deprecated
    
_(Since version 9)_
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#registerTempTable\(tableName:String\):Unit "Permalink") def registerTempTable(tableName: String): Unit
Registers this Dataset as a temporary table using the given name.
Registers this Dataset as a temporary table using the given name. The lifetime of this temporary table is tied to the `SparkSession` that was used to create this Dataset.  

Annotations
     @deprecated 

Deprecated
    
_(Since version 2.0.0)_ Use createOrReplaceTempView(viewName) instead. 

Since
    
1.6.0


### Inherited from AnyRef
### Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html###:Int "Permalink") final  def ##: Int 

Definition Classes
    AnyRef → Any
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#clone\(\):Object "Permalink") def clone(): AnyRef 

Attributes
    protected[lang]  

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#equals\(x$1:Object\):Boolean "Permalink") def equals(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef → Any
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef] 

Definition Classes
    AnyRef → Any 

Annotations
     @IntrinsicCandidate() @native()
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#hashCode\(\):Int "Permalink") def hashCode(): Int 

Definition Classes
    AnyRef → Any 

Annotations
     @IntrinsicCandidate() @native()
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#notify\(\):Unit "Permalink") final  def notify(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0 

Definition Classes
    AnyRef
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#toString\(\):String "Permalink") def toString(): [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String") 

Definition Classes
    AnyRef → Any
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#wait\(\):Unit "Permalink") final  def wait(): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#finalize\(\):Unit "Permalink") def finalize(): Unit 

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
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0 

Definition Classes
    Any
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean 

Definition Classes
    Any


### Actions
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#collect\(\):Array\[T\] "Permalink") abstract  def collect(): Array[T]
Returns an array that contains all rows in this Dataset.
Returns an array that contains all rows in this Dataset.
Running collect requires moving all the data into the application's driver process, and doing so on a very large dataset can crash the driver process with OutOfMemoryError.
For Java API, use [collectAsList](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#collectAsList\(\):java.util.List\[T\]).  

Since
    
1.6.0
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#collectAsList\(\):java.util.List\[T\] "Permalink") abstract  def collectAsList(): [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#java.util.List "java.util.List")[T]
Returns a Java list that contains all rows in this Dataset.
Returns a Java list that contains all rows in this Dataset.
Running collect requires moving all the data into the application's driver process, and doing so on a very large dataset can crash the driver process with OutOfMemoryError.  

Since
    
1.6.0
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#count\(\):Long "Permalink") abstract  def count(): Long
Returns the number of rows in the Dataset.
Returns the number of rows in the Dataset.  

Since
    
1.6.0
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#describe\(cols:String*\):org.apache.spark.sql.DataFrame "Permalink") abstract  def describe(cols: String*): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Computes basic statistics for numeric and string columns, including count, mean, stddev, min, and max.
Computes basic statistics for numeric and string columns, including count, mean, stddev, min, and max. If no columns are given, this function computes statistics for all numerical or string columns.
This function is meant for exploratory data analysis, as we make no guarantee about the backward compatibility of the schema of the resulting Dataset. If you want to programmatically compute summary statistics, use the `agg` function instead.

```
ds.describe("age", "height").show()

// output:
// summary age   height
// count   10.0  10.0
// mean    53.3  178.05
// stddev  11.6  15.7
// min     18.0  163.0
// max     92.0  192.0
```

Use [summary](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#summary\(statistics:String*\):org.apache.spark.sql.DataFrame) for expanded statistics and control over which statistics to compute.  

cols
    
Columns to compute statistics on. 

Annotations
     @varargs() 

Since
    
1.6.0
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#foreachPartition\(f:Iterator\[T\]=>Unit\):Unit "Permalink") abstract  def foreachPartition(f: (Iterator[T]) => Unit): Unit
Applies a function `f` to each partition of this Dataset.
Applies a function `f` to each partition of this Dataset.  

Since
    
1.6.0
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#head\(n:Int\):Array\[T\] "Permalink") abstract  def head(n: Int): Array[T]
Returns the first `n` rows.
Returns the first `n` rows.  

Since
    
1.6.0 

Note
    
this method should only be used if the resulting array is expected to be small, as all the data is loaded into the driver's memory.
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#reduce\(func:\(T,T\)=>T\):T "Permalink") abstract  def reduce(func: (T, T) => T): T
(Scala-specific) Reduces the elements of this Dataset using the specified binary function.
(Scala-specific) Reduces the elements of this Dataset using the specified binary function. The given `func` must be commutative and associative or the result may be non-deterministic.  

Since
    
1.6.0
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#show\(numRows:Int,truncate:Int,vertical:Boolean\):Unit "Permalink") abstract  def show(numRows: Int, truncate: Int, vertical: Boolean): Unit
Displays the Dataset in a tabular form.
Displays the Dataset in a tabular form. For example:

```
year  month AVG('Adj Close) MAX('Adj Close)
1980  12    0.503218        0.595103
1981  01    0.523289        0.570307
1982  02    0.436504        0.475256
1983  03    0.410516        0.442194
1984  04    0.450090        0.483521
```

If `vertical` enabled, this command prints output rows vertically (one line per column value)?

```
-RECORD 0-------------------
 year            | 1980
 month           | 12
 AVG('Adj Close) | 0.503218
 AVG('Adj Close) | 0.595103
-RECORD 1-------------------
 year            | 1981
 month           | 01
 AVG('Adj Close) | 0.523289
 AVG('Adj Close) | 0.570307
-RECORD 2-------------------
 year            | 1982
 month           | 02
 AVG('Adj Close) | 0.436504
 AVG('Adj Close) | 0.475256
-RECORD 3-------------------
 year            | 1983
 month           | 03
 AVG('Adj Close) | 0.410516
 AVG('Adj Close) | 0.442194
-RECORD 4-------------------
 year            | 1984
 month           | 04
 AVG('Adj Close) | 0.450090
 AVG('Adj Close) | 0.483521
```


numRows
    
Number of rows to show 

truncate
    
If set to more than 0, truncates strings to `truncate` characters and all cells will be aligned right. 

vertical
    
If set to true, prints output rows vertically (one line per column value). 

Since
    
2.3.0
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#show\(numRows:Int,truncate:Boolean\):Unit "Permalink") abstract  def show(numRows: Int, truncate: Boolean): Unit
Displays the Dataset in a tabular form.
Displays the Dataset in a tabular form. For example:

```
year  month AVG('Adj Close) MAX('Adj Close)
1980  12    0.503218        0.595103
1981  01    0.523289        0.570307
1982  02    0.436504        0.475256
1983  03    0.410516        0.442194
1984  04    0.450090        0.483521
```


numRows
    
Number of rows to show 

truncate
    
Whether truncate long strings. If true, strings more than 20 characters will be truncated and all cells will be aligned right 

Since
    
1.6.0
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#summary\(statistics:String*\):org.apache.spark.sql.DataFrame "Permalink") abstract  def summary(statistics: String*): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Computes specified statistics for numeric and string columns.
Computes specified statistics for numeric and string columns. Available statistics are:
     * count
     * mean
     * stddev
     * min
     * max
     * arbitrary approximate percentiles specified as a percentage (e.g. 75%)
     * count_distinct
     * approx_count_distinct
If no statistics are given, this function computes count, mean, stddev, min, approximate quartiles (percentiles at 25%, 50%, and 75%), and max.
This function is meant for exploratory data analysis, as we make no guarantee about the backward compatibility of the schema of the resulting Dataset. If you want to programmatically compute summary statistics, use the `agg` function instead.

```
ds.summary().show()

// output:
// summary age   height
// count   10.0  10.0
// mean    53.3  178.05
// stddev  11.6  15.7
// min     18.0  163.0
// 25%     24.0  176.0
// 50%     24.0  176.0
// 75%     32.0  180.0
// max     92.0  192.0
```

```
ds.summary("count", "min", "25%", "75%", "max").show()

// output:
// summary age   height
// count   10.0  10.0
// min     18.0  163.0
// 25%     24.0  176.0
// 75%     32.0  180.0
// max     92.0  192.0
```

To do a summary for specific columns first select them:

```
ds.select("age", "height").summary().show()
```

Specify statistics to output custom summaries:

```
ds.summary("count", "count_distinct").show()
```

The distinct count isn't included by default.
You can also run approximate distinct counts which are faster:

```
ds.summary("count", "approx_count_distinct").show()
```

See also [describe](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#describe\(cols:String*\):org.apache.spark.sql.DataFrame) for basic statistics.  

statistics
    
Statistics from above list to be computed. 

Annotations
     @varargs() 

Since
    
2.3.0
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#tail\(n:Int\):Array\[T\] "Permalink") abstract  def tail(n: Int): Array[T]
Returns the last `n` rows in the Dataset.
Returns the last `n` rows in the Dataset.
Running tail requires moving data into the application's driver process, and doing so with a very large `n` can crash the driver process with OutOfMemoryError.  

Since
    
3.0.0
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#toLocalIterator\(\):java.util.Iterator\[T\] "Permalink") abstract  def toLocalIterator(): [Iterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html#java.util.Iterator "java.util.Iterator")[T]
Returns an iterator that contains all rows in this Dataset.
Returns an iterator that contains all rows in this Dataset.
The iterator will consume as much memory as the largest partition in this Dataset.  

Since
    
2.0.0 

Note
    
this results in multiple Spark jobs, and if the input Dataset is the result of a wide transformation (e.g. join with different partitioners), to avoid recomputing the input Dataset should be cached first.
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#first\(\):T "Permalink") def first(): T
Returns the first row.
Returns the first row. Alias for head().  

Since
    
1.6.0
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#foreach\(func:org.apache.spark.api.java.function.ForeachFunction\[T\]\):Unit "Permalink") def foreach(func: [ForeachFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/ForeachFunction.html "org.apache.spark.api.java.function.ForeachFunction")[T]): Unit
(Java-specific) Runs `func` on each element of this Dataset.
(Java-specific) Runs `func` on each element of this Dataset.  

Since
    
1.6.0
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#foreach\(f:T=>Unit\):Unit "Permalink") def foreach(f: (T) => Unit): Unit
Applies a function `f` to all rows.
Applies a function `f` to all rows.  

Since
    
1.6.0
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#foreachPartition\(func:org.apache.spark.api.java.function.ForeachPartitionFunction\[T\]\):Unit "Permalink") def foreachPartition(func: [ForeachPartitionFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/ForeachPartitionFunction.html "org.apache.spark.api.java.function.ForeachPartitionFunction")[T]): Unit
(Java-specific) Runs `func` on each partition of this Dataset.
(Java-specific) Runs `func` on each partition of this Dataset.  

Since
    
1.6.0
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#head\(\):T "Permalink") def head(): T
Returns the first row.
Returns the first row.  

Since
    
1.6.0
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#reduce\(func:org.apache.spark.api.java.function.ReduceFunction\[T\]\):T "Permalink") def reduce(func: [ReduceFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/ReduceFunction.html "org.apache.spark.api.java.function.ReduceFunction")[T]): T
(Java-specific) Reduces the elements of this Dataset using the specified binary function.
(Java-specific) Reduces the elements of this Dataset using the specified binary function. The given `func` must be commutative and associative or the result may be non-deterministic.  

Since
    
1.6.0
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#show\(numRows:Int,truncate:Int\):Unit "Permalink") def show(numRows: Int, truncate: Int): Unit
Displays the Dataset in a tabular form.
Displays the Dataset in a tabular form. For example:

```
year  month AVG('Adj Close) MAX('Adj Close)
1980  12    0.503218        0.595103
1981  01    0.523289        0.570307
1982  02    0.436504        0.475256
1983  03    0.410516        0.442194
1984  04    0.450090        0.483521
```


numRows
    
Number of rows to show 

truncate
    
If set to more than 0, truncates strings to `truncate` characters and all cells will be aligned right. 

Since
    
1.6.0
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#show\(truncate:Boolean\):Unit "Permalink") def show(truncate: Boolean): Unit
Displays the top 20 rows of Dataset in a tabular form.
Displays the top 20 rows of Dataset in a tabular form.  

truncate
    
Whether truncate long strings. If true, strings more than 20 characters will be truncated and all cells will be aligned right 

Since
    
1.6.0
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#show\(\):Unit "Permalink") def show(): Unit
Displays the top 20 rows of Dataset in a tabular form.
Displays the top 20 rows of Dataset in a tabular form. Strings more than 20 characters will be truncated, and all cells will be aligned right.  

Since
    
1.6.0
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#show\(numRows:Int\):Unit "Permalink") def show(numRows: Int): Unit
Displays the Dataset in a tabular form.
Displays the Dataset in a tabular form. Strings more than 20 characters will be truncated, and all cells will be aligned right. For example:

```
year  month AVG('Adj Close) MAX('Adj Close)
1980  12    0.503218        0.595103
1981  01    0.523289        0.570307
1982  02    0.436504        0.475256
1983  03    0.410516        0.442194
1984  04    0.450090        0.483521
```


numRows
    
Number of rows to show 

Since
    
1.6.0
  23. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#take\(n:Int\):Array\[T\] "Permalink") def take(n: Int): Array[T]
Returns the first `n` rows in the Dataset.
Returns the first `n` rows in the Dataset.
Running take requires moving data into the application's driver process, and doing so with a very large `n` can crash the driver process with OutOfMemoryError.  

Since
    
1.6.0
  24. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#takeAsList\(n:Int\):java.util.List\[T\] "Permalink") def takeAsList(n: Int): [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#java.util.List "java.util.List")[T]
Returns the first `n` rows in the Dataset as a list.
Returns the first `n` rows in the Dataset as a list.
Running take requires moving data into the application's driver process, and doing so with a very large `n` can crash the driver process with OutOfMemoryError.  

Since
    
1.6.0


### Basic Dataset functions
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#as\[U\]\(implicitevidence$1:org.apache.spark.sql.Encoder\[U\]\):org.apache.spark.sql.Dataset\[U\] "Permalink") abstract  def as[U](implicit arg0: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[U]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[U]
Returns a new Dataset where each record has been mapped on to the specified type.
Returns a new Dataset where each record has been mapped on to the specified type. The method used to map columns depend on the type of `U`:
     * When `U` is a class, fields for the class will be mapped to columns of the same name (case sensitivity is determined by `spark.sql.caseSensitive`).
     * When `U` is a tuple, the columns will be mapped by ordinal (i.e. the first column will be assigned to `_1`).
     * When `U` is a primitive type (i.e. String, Int, etc), then the first column of the `DataFrame` will be used.
If the schema of the Dataset does not match the desired `U` type, you can use `select` along with `alias` or `as` to rearrange or rename as required.
Note that `as[]` only changes the view of the data that is passed into typed operations, such as `map()`, and does not eagerly project away any columns that are not present in the specified class.  

Since
    
1.6.0
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#cache\(\):org.apache.spark.sql.Dataset\[T\] "Permalink") abstract  def cache(): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Persist this Dataset with the default storage level (`MEMORY_AND_DISK`).
Persist this Dataset with the default storage level (`MEMORY_AND_DISK`).  

Since
    
1.6.0
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#explain\(mode:String\):Unit "Permalink") abstract  def explain(mode: String): Unit
Prints the plans (logical and physical) with a format specified by a given explain mode.
Prints the plans (logical and physical) with a format specified by a given explain mode.  

mode
    
specifies the expected output format of plans.
     * `simple` Print only a physical plan.
     * `extended`: Print both logical and physical plans.
     * `codegen`: Print a physical plan and generated codes if they are available.
     * `cost`: Print a logical plan and statistics if they are available.
     * `formatted`: Split explain output into two sections: a physical plan outline and node details. 

Since
    
3.0.0
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#hint\(name:String,parameters:Any*\):org.apache.spark.sql.Dataset\[T\] "Permalink") abstract  def hint(name: String, parameters: Any*): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Specifies some hint on the current Dataset.
Specifies some hint on the current Dataset. As an example, the following code specifies that one of the plan can be broadcasted:

```
df1.join(df2.hint("broadcast"))
```

the following code specifies that this dataset could be rebalanced with given number of partitions:

```
df1.hint("rebalance", 10)
```


name
    
the name of the hint 

parameters
    
the parameters of the hint, all the parameters should be a `Column` or `Expression` or `Symbol` or could be converted into a `Literal` 

Annotations
     @varargs() 

Since
    
2.2.0
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#inputFiles:Array\[String\] "Permalink") abstract  def inputFiles: Array[String]
Returns a best-effort snapshot of the files that compose this Dataset.
Returns a best-effort snapshot of the files that compose this Dataset. This method simply asks each constituent BaseRelation for its respective files and takes the union of all results. Depending on the source relations, this may not find all input files. Duplicates are removed.  

Since
    
2.0.0
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#isEmpty:Boolean "Permalink") abstract  def isEmpty: Boolean
Returns true if the `Dataset` is empty.
Returns true if the `Dataset` is empty.  

Since
    
2.4.0
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#isLocal:Boolean "Permalink") abstract  def isLocal: Boolean
Returns true if the `collect` and `take` methods can be run locally (without any Spark executors).
Returns true if the `collect` and `take` methods can be run locally (without any Spark executors).  

Since
    
1.6.0
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#mergeInto\(table:String,condition:org.apache.spark.sql.Column\):org.apache.spark.sql.MergeIntoWriter\[T\] "Permalink") abstract  def mergeInto(table: String, condition: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")): [MergeIntoWriter](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/MergeIntoWriter.html "org.apache.spark.sql.MergeIntoWriter")[T]
Merges a set of updates, insertions, and deletions based on a source table into a target table.
Merges a set of updates, insertions, and deletions based on a source table into a target table.
Scala Examples:

```
spark.table("source")
  .mergeInto("target", $"source.id" === $"target.id")
  .whenMatched($"salary" === 100)
  .delete()
  .whenNotMatched()
  .insertAll()
  .whenNotMatchedBySource($"salary" === 100)
  .update(Map(
    "salary" -> lit(200)
  ))
  .merge()
```


Since
    
4.0.0
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#persist\(newLevel:org.apache.spark.storage.StorageLevel\):org.apache.spark.sql.Dataset\[T\] "Permalink") abstract  def persist(newLevel: [StorageLevel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StorageLevel.html "org.apache.spark.storage.StorageLevel")): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Persist this Dataset with the given storage level.
Persist this Dataset with the given storage level.  

newLevel
    
One of: `MEMORY_ONLY`, `MEMORY_AND_DISK`, `MEMORY_ONLY_SER`, `MEMORY_AND_DISK_SER`, `DISK_ONLY`, `MEMORY_ONLY_2`, `MEMORY_AND_DISK_2`, etc. 

Since
    
1.6.0
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#persist\(\):org.apache.spark.sql.Dataset\[T\] "Permalink") abstract  def persist(): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Persist this Dataset with the default storage level (`MEMORY_AND_DISK`).
Persist this Dataset with the default storage level (`MEMORY_AND_DISK`).  

Since
    
1.6.0
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#rdd:org.apache.spark.rdd.RDD\[T\] "Permalink") abstract  def rdd: [RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD")[T]
Represents the content of the Dataset as an `RDD` of `T`.
Represents the content of the Dataset as an `RDD` of `T`.  

Annotations
     @ClassicOnly() 

Since
    
1.6.0 

Note
    
this is only supported in Classic.
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#schema:org.apache.spark.sql.types.StructType "Permalink") abstract  def schema: [StructType](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/types/StructType.html "org.apache.spark.sql.types.StructType")
Returns the schema of this Dataset.
Returns the schema of this Dataset.  

Since
    
1.6.0
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#storageLevel:org.apache.spark.storage.StorageLevel "Permalink") abstract  def storageLevel: [StorageLevel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StorageLevel.html "org.apache.spark.storage.StorageLevel")
Get the Dataset's current storage level, or StorageLevel.NONE if not persisted.
Get the Dataset's current storage level, or StorageLevel.NONE if not persisted.  

Since
    
2.1.0
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#to\(schema:org.apache.spark.sql.types.StructType\):org.apache.spark.sql.DataFrame "Permalink") abstract  def to(schema: [StructType](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/types/StructType.html "org.apache.spark.sql.types.StructType")): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Returns a new DataFrame where each row is reconciled to match the specified schema.
Returns a new DataFrame where each row is reconciled to match the specified schema. Spark will:
     * Reorder columns and/or inner fields by name to match the specified schema.
     * Project away columns and/or inner fields that are not needed by the specified schema. Missing columns and/or inner fields (present in the specified schema but not input DataFrame) lead to failures.
     * Cast the columns and/or inner fields to match the data types in the specified schema, if the types are compatible, e.g., numeric to numeric (error if overflows), but not string to int.
     * Carry over the metadata from the specified schema, while the columns and/or inner fields still keep their own metadata if not overwritten by the specified schema.
     * Fail if the nullability is not compatible. For example, the column and/or inner field is nullable but the specified schema requires them to be not nullable.  

Since
    
3.4.0
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#toDF\(colNames:String*\):org.apache.spark.sql.DataFrame "Permalink") abstract  def toDF(colNames: String*): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Converts this strongly typed collection of data to generic `DataFrame` with columns renamed.
Converts this strongly typed collection of data to generic `DataFrame` with columns renamed. This can be quite convenient in conversion from an RDD of tuples into a `DataFrame` with meaningful names. For example:

```
val rdd: RDD[(Int, String)] = ...
rdd.toDF()  // this implicit conversion creates a DataFrame with column name `_1` and `_2`
rdd.toDF("id", "name")  // this creates a DataFrame with column name "id" and "name"
```


Annotations
     @varargs() 

Since
    
2.0.0
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#toDF\(\):org.apache.spark.sql.DataFrame "Permalink") abstract  def toDF(): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Converts this strongly typed collection of data to generic Dataframe.
Converts this strongly typed collection of data to generic Dataframe. In contrast to the strongly typed objects that Dataset operations work on, a Dataframe returns generic [org.apache.spark.sql.Row](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Row.html "org.apache.spark.sql.Row") objects that allow fields to be accessed by ordinal or name.  

Since
    
1.6.0
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#toJavaRDD:org.apache.spark.api.java.JavaRDD\[T\] "Permalink") abstract  def toJavaRDD: [JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[T]
Returns the content of the Dataset as a `JavaRDD` of `T`s.
Returns the content of the Dataset as a `JavaRDD` of `T`s.  

Annotations
     @ClassicOnly() 

Since
    
1.6.0 

Note
    
this is only supported in Classic.
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#unpersist\(\):org.apache.spark.sql.Dataset\[T\] "Permalink") abstract  def unpersist(): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Mark the Dataset as non-persistent, and remove all blocks for it from memory and disk.
Mark the Dataset as non-persistent, and remove all blocks for it from memory and disk. This will not un-persist any cached data that is built upon this Dataset.  

Since
    
1.6.0
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#unpersist\(blocking:Boolean\):org.apache.spark.sql.Dataset\[T\] "Permalink") abstract  def unpersist(blocking: Boolean): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Mark the Dataset as non-persistent, and remove all blocks for it from memory and disk.
Mark the Dataset as non-persistent, and remove all blocks for it from memory and disk. This will not un-persist any cached data that is built upon this Dataset.  

blocking
    
Whether to block until all blocks are deleted. 

Since
    
1.6.0
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#write:org.apache.spark.sql.DataFrameWriter\[T\] "Permalink") abstract  def write: [DataFrameWriter](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/DataFrameWriter.html "org.apache.spark.sql.DataFrameWriter")[T]
Interface for saving the content of the non-streaming Dataset out into external storage.
Interface for saving the content of the non-streaming Dataset out into external storage.  

Since
    
1.6.0
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#writeStream:org.apache.spark.sql.streaming.DataStreamWriter\[T\] "Permalink") abstract  def writeStream: [DataStreamWriter](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/DataStreamWriter.html "org.apache.spark.sql.streaming.DataStreamWriter")[T]
Interface for saving the content of the streaming Dataset out into external storage.
Interface for saving the content of the streaming Dataset out into external storage.  

Since
    
2.0.0
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#writeTo\(table:String\):org.apache.spark.sql.DataFrameWriterV2\[T\] "Permalink") abstract  def writeTo(table: String): [DataFrameWriterV2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/DataFrameWriterV2.html "org.apache.spark.sql.DataFrameWriterV2")[T]
Create a write configuration builder for v2 sources.
Create a write configuration builder for v2 sources.
This builder is used to configure and execute write operations. For example, to append to an existing table, run:

```
df.writeTo("catalog.db.table").append()
```

This can also be used to create or replace existing tables:

```
df.writeTo("catalog.db.table").partitionedBy($"col").createOrReplace()
```


Since
    
3.0.0
  23. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#checkpoint\(eager:Boolean\):org.apache.spark.sql.Dataset\[T\] "Permalink") def checkpoint(eager: Boolean): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Returns a checkpointed version of this Dataset.
Returns a checkpointed version of this Dataset. Checkpointing can be used to truncate the logical plan of this Dataset, which is especially useful in iterative algorithms where the plan may grow exponentially. It will be saved to files inside the checkpoint directory set with `SparkContext#setCheckpointDir`.  

eager
    
Whether to checkpoint this dataframe immediately 

Since
    
2.1.0 

Note
    
When checkpoint is used with eager = false, the final data that is checkpointed after the first action may be different from the data that was used during the job due to non-determinism of the underlying operation and retries. If checkpoint is used to achieve saving a deterministic snapshot of the data, eager = true should be used. Otherwise, it is only deterministic after the first execution, after the checkpoint was finalized.
  24. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#checkpoint\(\):org.apache.spark.sql.Dataset\[T\] "Permalink") def checkpoint(): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Eagerly checkpoint a Dataset and return the new Dataset.
Eagerly checkpoint a Dataset and return the new Dataset. Checkpointing can be used to truncate the logical plan of this Dataset, which is especially useful in iterative algorithms where the plan may grow exponentially. It will be saved to files inside the checkpoint directory set with `SparkContext#setCheckpointDir`.  

Since
    
2.1.0
  25. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#columns:Array\[String\] "Permalink") def columns: Array[String]
Returns all column names as an array.
Returns all column names as an array.  

Since
    
1.6.0
  26. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#createGlobalTempView\(viewName:String\):Unit "Permalink") def createGlobalTempView(viewName: String): Unit
Creates a global temporary view using the given name.
Creates a global temporary view using the given name. The lifetime of this temporary view is tied to this Spark application.
Global temporary view is cross-session. Its lifetime is the lifetime of the Spark application, i.e. it will be automatically dropped when the application terminates. It's tied to a system preserved database `global_temp`, and we must use the qualified name to refer a global temp view, e.g. `SELECT * FROM global_temp.view1`.  

Annotations
     @throws("") 

Since
    
2.1.0 

Exceptions thrown
    
[`org.apache.spark.sql.AnalysisException`](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/AnalysisException.html "org.apache.spark.sql.AnalysisException") if the view name is invalid or already exists
  27. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#createOrReplaceGlobalTempView\(viewName:String\):Unit "Permalink") def createOrReplaceGlobalTempView(viewName: String): Unit
Creates or replaces a global temporary view using the given name.
Creates or replaces a global temporary view using the given name. The lifetime of this temporary view is tied to this Spark application.
Global temporary view is cross-session. Its lifetime is the lifetime of the Spark application, i.e. it will be automatically dropped when the application terminates. It's tied to a system preserved database `global_temp`, and we must use the qualified name to refer a global temp view, e.g. `SELECT * FROM global_temp.view1`.  

Since
    
2.2.0
  28. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#createOrReplaceTempView\(viewName:String\):Unit "Permalink") def createOrReplaceTempView(viewName: String): Unit
Creates a local temporary view using the given name.
Creates a local temporary view using the given name. The lifetime of this temporary view is tied to the `SparkSession` that was used to create this Dataset.  

Since
    
2.0.0
  29. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#createTempView\(viewName:String\):Unit "Permalink") def createTempView(viewName: String): Unit
Creates a local temporary view using the given name.
Creates a local temporary view using the given name. The lifetime of this temporary view is tied to the `SparkSession` that was used to create this Dataset.
Local temporary view is session-scoped. Its lifetime is the lifetime of the session that created it, i.e. it will be automatically dropped when the session terminates. It's not tied to any databases, i.e. we can't use `db1.view1` to reference a local temporary view.  

Annotations
     @throws("") 

Since
    
2.0.0 

Exceptions thrown
    
[`org.apache.spark.sql.AnalysisException`](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/AnalysisException.html "org.apache.spark.sql.AnalysisException") if the view name is invalid or already exists
  30. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#dtypes:Array\[\(String,String\)\] "Permalink") def dtypes: Array[(String, String)]
Returns all column names and their data types as an array.
Returns all column names and their data types as an array.  

Since
    
1.6.0
  31. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#explain\(\):Unit "Permalink") def explain(): Unit
Prints the physical plan to the console for debugging purposes.
Prints the physical plan to the console for debugging purposes.  

Since
    
1.6.0
  32. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#explain\(extended:Boolean\):Unit "Permalink") def explain(extended: Boolean): Unit
Prints the plans (logical and physical) to the console for debugging purposes.
Prints the plans (logical and physical) to the console for debugging purposes.  

extended
    
default `false`. If `false`, prints only the physical plan. 

Since
    
1.6.0
  33. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#javaRDD:org.apache.spark.api.java.JavaRDD\[T\] "Permalink") def javaRDD: [JavaRDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/JavaRDD.html "org.apache.spark.api.java.JavaRDD")[T]
Returns the content of the Dataset as a `JavaRDD` of `T`s.
Returns the content of the Dataset as a `JavaRDD` of `T`s.  

Annotations
     @ClassicOnly() 

Since
    
1.6.0 

Note
    
this is only supported in Classic.
  34. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#localCheckpoint\(eager:Boolean,storageLevel:org.apache.spark.storage.StorageLevel\):org.apache.spark.sql.Dataset\[T\] "Permalink") def localCheckpoint(eager: Boolean, storageLevel: [StorageLevel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StorageLevel.html "org.apache.spark.storage.StorageLevel")): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Locally checkpoints a Dataset and return the new Dataset.
Locally checkpoints a Dataset and return the new Dataset. Checkpointing can be used to truncate the logical plan of this Dataset, which is especially useful in iterative algorithms where the plan may grow exponentially. Local checkpoints are written to executor storage and despite potentially faster they are unreliable and may compromise job completion.  

eager
    
Whether to checkpoint this dataframe immediately 

storageLevel
    
StorageLevel with which to checkpoint the data. 

Since
    
4.0.0 

Note
    
When checkpoint is used with eager = false, the final data that is checkpointed after the first action may be different from the data that was used during the job due to non-determinism of the underlying operation and retries. If checkpoint is used to achieve saving a deterministic snapshot of the data, eager = true should be used. Otherwise, it is only deterministic after the first execution, after the checkpoint was finalized.
  35. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#localCheckpoint\(eager:Boolean\):org.apache.spark.sql.Dataset\[T\] "Permalink") def localCheckpoint(eager: Boolean): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Locally checkpoints a Dataset and return the new Dataset.
Locally checkpoints a Dataset and return the new Dataset. Checkpointing can be used to truncate the logical plan of this Dataset, which is especially useful in iterative algorithms where the plan may grow exponentially. Local checkpoints are written to executor storage and despite potentially faster they are unreliable and may compromise job completion.  

eager
    
Whether to checkpoint this dataframe immediately 

Since
    
2.3.0 

Note
    
When checkpoint is used with eager = false, the final data that is checkpointed after the first action may be different from the data that was used during the job due to non-determinism of the underlying operation and retries. If checkpoint is used to achieve saving a deterministic snapshot of the data, eager = true should be used. Otherwise, it is only deterministic after the first execution, after the checkpoint was finalized.
  36. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#localCheckpoint\(\):org.apache.spark.sql.Dataset\[T\] "Permalink") def localCheckpoint(): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Eagerly locally checkpoints a Dataset and return the new Dataset.
Eagerly locally checkpoints a Dataset and return the new Dataset. Checkpointing can be used to truncate the logical plan of this Dataset, which is especially useful in iterative algorithms where the plan may grow exponentially. Local checkpoints are written to executor storage and despite potentially faster they are unreliable and may compromise job completion.  

Since
    
2.3.0
  37. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#printSchema\(level:Int\):Unit "Permalink") def printSchema(level: Int): Unit
Prints the schema up to the given level to the console in a nice tree format.
Prints the schema up to the given level to the console in a nice tree format.  

Since
    
3.0.0
  38. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#printSchema\(\):Unit "Permalink") def printSchema(): Unit
Prints the schema to the console in a nice tree format.
Prints the schema to the console in a nice tree format.  

Since
    
1.6.0
  39. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#registerTempTable\(tableName:String\):Unit "Permalink") def registerTempTable(tableName: String): Unit
Registers this Dataset as a temporary table using the given name.
Registers this Dataset as a temporary table using the given name. The lifetime of this temporary table is tied to the `SparkSession` that was used to create this Dataset.  

Annotations
     @deprecated 

Deprecated
    
_(Since version 2.0.0)_ Use createOrReplaceTempView(viewName) instead. 

Since
    
1.6.0


### streaming
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#isStreaming:Boolean "Permalink") abstract  def isStreaming: Boolean
Returns true if this Dataset contains one or more sources that continuously return data as it arrives.
Returns true if this Dataset contains one or more sources that continuously return data as it arrives. A Dataset that reads data from a streaming source must be executed as a `StreamingQuery` using the `start()` method in `DataStreamWriter`. Methods that return a single answer, e.g. `count()` or `collect()`, will throw an [org.apache.spark.sql.AnalysisException](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/AnalysisException.html "org.apache.spark.sql.AnalysisException") when there is a streaming source present.  

Since
    
2.0.0
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#withWatermark\(eventTime:String,delayThreshold:String\):org.apache.spark.sql.Dataset\[T\] "Permalink") abstract  def withWatermark(eventTime: String, delayThreshold: String): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Defines an event time watermark for this [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset").
Defines an event time watermark for this [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset"). A watermark tracks a point in time before which we assume no more late data is going to arrive.
Spark will use this watermark for several purposes:
     * To know when a given time window aggregation can be finalized and thus can be emitted when using output modes that do not allow updates.
     * To minimize the amount of state that we need to keep for on-going aggregations, `mapGroupsWithState` and `dropDuplicates` operators. The current watermark is computed by looking at the `MAX(eventTime)` seen across all of the partitions in the query minus a user specified `delayThreshold`. Due to the cost of coordinating this value across partitions, the actual watermark used is only guaranteed to be at least `delayThreshold` behind the actual event time. In some cases we may still process records that arrive more than `delayThreshold` late.  

eventTime
    
the name of the column that contains the event time of the row. 

delayThreshold
    
the minimum delay to wait to data to arrive late, relative to the latest record that has been processed in the form of an interval (e.g. "1 minute" or "5 hours"). NOTE: This should not be negative. 

Since
    
2.1.0


### subquery
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#exists\(\):org.apache.spark.sql.Column "Permalink") def exists(): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Return a `Column` object for an EXISTS Subquery.
Return a `Column` object for an EXISTS Subquery.
The `exists` method provides a way to create a boolean column that checks for the presence of related records in a subquery. When applied within a `DataFrame`, this method allows you to filter rows based on whether matching records exist in the related dataset. The resulting `Column` object can be used directly in filtering conditions or as a computed column.  

Since
    
4.0.0
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#scalar\(\):org.apache.spark.sql.Column "Permalink") def scalar(): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Return a `Column` object for a SCALAR Subquery containing exactly one row and one column.
Return a `Column` object for a SCALAR Subquery containing exactly one row and one column.
The `scalar()` method is useful for extracting a `Column` object that represents a scalar value from a DataFrame, especially when the DataFrame results from an aggregation or single-value computation. This returned `Column` can then be used directly in `select` clauses or as predicates in filters on the outer DataFrame, enabling dynamic data filtering and calculations based on scalar values.  

Since
    
4.0.0


### Typed transformations
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#as\(alias:String\):org.apache.spark.sql.Dataset\[T\] "Permalink") abstract  def as(alias: String): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Returns a new Dataset with an alias set.
Returns a new Dataset with an alias set.  

Since
    
1.6.0
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#coalesce\(numPartitions:Int\):org.apache.spark.sql.Dataset\[T\] "Permalink") abstract  def coalesce(numPartitions: Int): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Returns a new Dataset that has exactly `numPartitions` partitions, when the fewer partitions are requested.
Returns a new Dataset that has exactly `numPartitions` partitions, when the fewer partitions are requested. If a larger number of partitions is requested, it will stay at the current number of partitions. Similar to coalesce defined on an `RDD`, this operation results in a narrow dependency, e.g. if you go from 1000 partitions to 100 partitions, there will not be a shuffle, instead each of the 100 new partitions will claim 10 of the current partitions.
However, if you're doing a drastic coalesce, e.g. to numPartitions = 1, this may result in your computation taking place on fewer nodes than you like (e.g. one node in the case of numPartitions = 1). To avoid this, you can call repartition. This will add a shuffle step, but means the current upstream partitions will be executed in parallel (per whatever the current partitioning is).  

Since
    
1.6.0
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#dropDuplicates\(colNames:Seq\[String\]\):org.apache.spark.sql.Dataset\[T\] "Permalink") abstract  def dropDuplicates(colNames: Seq[String]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
(Scala-specific) Returns a new Dataset with duplicate rows removed, considering only the subset of columns.
(Scala-specific) Returns a new Dataset with duplicate rows removed, considering only the subset of columns.
For a static batch [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset"), it just drops duplicate rows. For a streaming [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset"), it will keep all data across triggers as intermediate state to drop duplicates rows. You can use [withWatermark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#withWatermark\(eventTime:String,delayThreshold:String\):org.apache.spark.sql.Dataset\[T\]) to limit how late the duplicate data can be and system will accordingly limit the state. In addition, too late data older than watermark will be dropped to avoid any possibility of duplicates.  

Since
    
2.0.0
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#dropDuplicates\(\):org.apache.spark.sql.Dataset\[T\] "Permalink") abstract  def dropDuplicates(): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Returns a new Dataset that contains only the unique rows from this Dataset.
Returns a new Dataset that contains only the unique rows from this Dataset. This is an alias for `distinct`.
For a static batch [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset"), it just drops duplicate rows. For a streaming [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset"), it will keep all data across triggers as intermediate state to drop duplicates rows. You can use [withWatermark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#withWatermark\(eventTime:String,delayThreshold:String\):org.apache.spark.sql.Dataset\[T\]) to limit how late the duplicate data can be and system will accordingly limit the state. In addition, too late data older than watermark will be dropped to avoid any possibility of duplicates.  

Since
    
2.0.0
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#dropDuplicatesWithinWatermark\(colNames:Seq\[String\]\):org.apache.spark.sql.Dataset\[T\] "Permalink") abstract  def dropDuplicatesWithinWatermark(colNames: Seq[String]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Returns a new Dataset with duplicates rows removed, considering only the subset of columns, within watermark.
Returns a new Dataset with duplicates rows removed, considering only the subset of columns, within watermark.
This only works with streaming [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset"), and watermark for the input [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") must be set via [withWatermark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#withWatermark\(eventTime:String,delayThreshold:String\):org.apache.spark.sql.Dataset\[T\]).
For a streaming [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset"), this will keep all data across triggers as intermediate state to drop duplicated rows. The state will be kept to guarantee the semantic, "Events are deduplicated as long as the time distance of earliest and latest events are smaller than the delay threshold of watermark." Users are encouraged to set the delay threshold of watermark longer than max timestamp differences among duplicated events.
Note: too late data older than watermark will be dropped.  

Since
    
3.5.0
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#dropDuplicatesWithinWatermark\(\):org.apache.spark.sql.Dataset\[T\] "Permalink") abstract  def dropDuplicatesWithinWatermark(): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Returns a new Dataset with duplicates rows removed, within watermark.
Returns a new Dataset with duplicates rows removed, within watermark.
This only works with streaming [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset"), and watermark for the input [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") must be set via [withWatermark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#withWatermark\(eventTime:String,delayThreshold:String\):org.apache.spark.sql.Dataset\[T\]).
For a streaming [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset"), this will keep all data across triggers as intermediate state to drop duplicated rows. The state will be kept to guarantee the semantic, "Events are deduplicated as long as the time distance of earliest and latest events are smaller than the delay threshold of watermark." Users are encouraged to set the delay threshold of watermark longer than max timestamp differences among duplicated events.
Note: too late data older than watermark will be dropped.  

Since
    
3.5.0
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#except\(other:org.apache.spark.sql.Dataset\[T\]\):org.apache.spark.sql.Dataset\[T\] "Permalink") abstract  def except(other: [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Returns a new Dataset containing rows in this Dataset but not in another Dataset.
Returns a new Dataset containing rows in this Dataset but not in another Dataset. This is equivalent to `EXCEPT DISTINCT` in SQL.  

Since
    
2.0.0 

Note
    
Equality checking is performed directly on the encoded representation of the data and thus is not affected by a custom `equals` function defined on `T`.
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#exceptAll\(other:org.apache.spark.sql.Dataset\[T\]\):org.apache.spark.sql.Dataset\[T\] "Permalink") abstract  def exceptAll(other: [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Returns a new Dataset containing rows in this Dataset but not in another Dataset while preserving the duplicates.
Returns a new Dataset containing rows in this Dataset but not in another Dataset while preserving the duplicates. This is equivalent to `EXCEPT ALL` in SQL.  

Since
    
2.4.0 

Note
    
Equality checking is performed directly on the encoded representation of the data and thus is not affected by a custom `equals` function defined on `T`. Also as standard in SQL, this function resolves columns by position (not by name).
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#filter\(func:org.apache.spark.api.java.function.FilterFunction\[T\]\):org.apache.spark.sql.Dataset\[T\] "Permalink") abstract  def filter(func: [FilterFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FilterFunction.html "org.apache.spark.api.java.function.FilterFunction")[T]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
(Java-specific) Returns a new Dataset that only contains elements where `func` returns `true`.
(Java-specific) Returns a new Dataset that only contains elements where `func` returns `true`.  

Since
    
1.6.0
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#filter\(func:T=>Boolean\):org.apache.spark.sql.Dataset\[T\] "Permalink") abstract  def filter(func: (T) => Boolean): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
(Scala-specific) Returns a new Dataset that only contains elements where `func` returns `true`.
(Scala-specific) Returns a new Dataset that only contains elements where `func` returns `true`.  

Since
    
1.6.0
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#filter\(condition:org.apache.spark.sql.Column\):org.apache.spark.sql.Dataset\[T\] "Permalink") abstract  def filter(condition: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Filters rows using the given condition.
Filters rows using the given condition.

```
// The following are equivalent:
peopleDs.filter($"age" > 15)
peopleDs.where($"age" > 15)
```


Since
    
1.6.0
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#groupByKey\[K\]\(func:T=>K\)\(implicitevidence$2:org.apache.spark.sql.Encoder\[K\]\):org.apache.spark.sql.KeyValueGroupedDataset\[K,T\] "Permalink") abstract  def groupByKey[K](func: (T) => K)(implicit arg0: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[K]): [KeyValueGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html "org.apache.spark.sql.KeyValueGroupedDataset")[K, T]
(Scala-specific) Returns a [KeyValueGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html "org.apache.spark.sql.KeyValueGroupedDataset") where the data is grouped by the given key `func`.
(Scala-specific) Returns a [KeyValueGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html "org.apache.spark.sql.KeyValueGroupedDataset") where the data is grouped by the given key `func`.  

Since
    
2.0.0
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#intersect\(other:org.apache.spark.sql.Dataset\[T\]\):org.apache.spark.sql.Dataset\[T\] "Permalink") abstract  def intersect(other: [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Returns a new Dataset containing rows only in both this Dataset and another Dataset.
Returns a new Dataset containing rows only in both this Dataset and another Dataset. This is equivalent to `INTERSECT` in SQL.  

Since
    
1.6.0 

Note
    
Equality checking is performed directly on the encoded representation of the data and thus is not affected by a custom `equals` function defined on `T`.
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#intersectAll\(other:org.apache.spark.sql.Dataset\[T\]\):org.apache.spark.sql.Dataset\[T\] "Permalink") abstract  def intersectAll(other: [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Returns a new Dataset containing rows only in both this Dataset and another Dataset while preserving the duplicates.
Returns a new Dataset containing rows only in both this Dataset and another Dataset while preserving the duplicates. This is equivalent to `INTERSECT ALL` in SQL.  

Since
    
2.4.0 

Note
    
Equality checking is performed directly on the encoded representation of the data and thus is not affected by a custom `equals` function defined on `T`. Also as standard in SQL, this function resolves columns by position (not by name).
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#joinWith\[U\]\(other:org.apache.spark.sql.Dataset\[U\],condition:org.apache.spark.sql.Column,joinType:String\):org.apache.spark.sql.Dataset\[\(T,U\)\] "Permalink") abstract  def joinWith[U](other: [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[U], condition: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column"), joinType: String): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[(T, U)]
Joins this Dataset returning a `Tuple2` for each pair where `condition` evaluates to true.
Joins this Dataset returning a `Tuple2` for each pair where `condition` evaluates to true.
This is similar to the relation `join` function with one important difference in the result schema. Since `joinWith` preserves objects present on either side of the join, the result schema is similarly nested into a tuple under the column names `_1` and `_2`.
This type of join can be useful both for preserving type-safety with the original object types as well as working with relational data where either side of the join has column names in common.  

other
    
Right side of the join. 

condition
    
Join expression. 

joinType
    
Type of join to perform. Default `inner`. Must be one of: `inner`, `cross`, `outer`, `full`, `fullouter`,`full_outer`, `left`, `leftouter`, `left_outer`, `right`, `rightouter`, `right_outer`. 

Since
    
1.6.0
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#limit\(n:Int\):org.apache.spark.sql.Dataset\[T\] "Permalink") abstract  def limit(n: Int): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Returns a new Dataset by taking the first `n` rows.
Returns a new Dataset by taking the first `n` rows. The difference between this function and `head` is that `head` is an action and returns an array (by triggering query execution) while `limit` returns a new Dataset.  

Since
    
2.0.0
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#map\[U\]\(func:org.apache.spark.api.java.function.MapFunction\[T,U\],encoder:org.apache.spark.sql.Encoder\[U\]\):org.apache.spark.sql.Dataset\[U\] "Permalink") abstract  def map[U](func: [MapFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/MapFunction.html "org.apache.spark.api.java.function.MapFunction")[T, U], encoder: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[U]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[U]
(Java-specific) Returns a new Dataset that contains the result of applying `func` to each element.
(Java-specific) Returns a new Dataset that contains the result of applying `func` to each element.  

Since
    
1.6.0
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#map\[U\]\(func:T=>U\)\(implicitevidence$5:org.apache.spark.sql.Encoder\[U\]\):org.apache.spark.sql.Dataset\[U\] "Permalink") abstract  def map[U](func: (T) => U)(implicit arg0: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[U]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[U]
(Scala-specific) Returns a new Dataset that contains the result of applying `func` to each element.
(Scala-specific) Returns a new Dataset that contains the result of applying `func` to each element.  

Since
    
1.6.0
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#mapPartitions\[U\]\(func:Iterator\[T\]=>Iterator\[U\]\)\(implicitevidence$6:org.apache.spark.sql.Encoder\[U\]\):org.apache.spark.sql.Dataset\[U\] "Permalink") abstract  def mapPartitions[U](func: (Iterator[T]) => Iterator[U])(implicit arg0: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[U]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[U]
(Scala-specific) Returns a new Dataset that contains the result of applying `func` to each partition.
(Scala-specific) Returns a new Dataset that contains the result of applying `func` to each partition.  

Since
    
1.6.0
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#observe\(observation:org.apache.spark.sql.Observation,expr:org.apache.spark.sql.Column,exprs:org.apache.spark.sql.Column*\):org.apache.spark.sql.Dataset\[T\] "Permalink") abstract  def observe(observation: [Observation](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Observation.html "org.apache.spark.sql.Observation"), expr: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column"), exprs: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")*): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Observe (named) metrics through an `org.apache.spark.sql.Observation` instance.
Observe (named) metrics through an `org.apache.spark.sql.Observation` instance. This method does not support streaming datasets.
A user can retrieve the metrics by accessing `org.apache.spark.sql.Observation.get`.

```
// Observe row count (rows) and highest id (maxid) in the Dataset while writing it
val observation = Observation("my_metrics")
val observed_ds = ds.observe(observation, count(lit(1)).as("rows"), max($"id").as("maxid"))
observed_ds.write.parquet("ds.parquet")
val metrics = observation.get
```


Annotations
     @varargs() 

Since
    
3.3.0 

Exceptions thrown
    
`IllegalArgumentException` If this is a streaming Dataset (this.isStreaming == true)
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#observe\(name:String,expr:org.apache.spark.sql.Column,exprs:org.apache.spark.sql.Column*\):org.apache.spark.sql.Dataset\[T\] "Permalink") abstract  def observe(name: String, expr: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column"), exprs: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")*): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Define (named) metrics to observe on the Dataset.
Define (named) metrics to observe on the Dataset. This method returns an 'observed' Dataset that returns the same result as the input, with the following guarantees:
     * It will compute the defined aggregates (metrics) on all the data that is flowing through the Dataset at that point.
     * It will report the value of the defined aggregate columns as soon as we reach a completion point. A completion point is either the end of a query (batch mode) or the end of a streaming epoch. The value of the aggregates only reflects the data processed since the previous completion point. Please note that continuous execution is currently not supported.
The metrics columns must either contain a literal (e.g. lit(42)), or should contain one or more aggregate functions (e.g. sum(a) or sum(a + b) + avg(c) - lit(1)). Expressions that contain references to the input Dataset's columns must always be wrapped in an aggregate function.  

Annotations
     @varargs() 

Since
    
3.0.0
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#offset\(n:Int\):org.apache.spark.sql.Dataset\[T\] "Permalink") abstract  def offset(n: Int): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Returns a new Dataset by skipping the first `n` rows.
Returns a new Dataset by skipping the first `n` rows.  

Since
    
3.4.0
  23. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#randomSplit\(weights:Array\[Double\]\):Array\[org.apache.spark.sql.Dataset\[T\]\] "Permalink") abstract  def randomSplit(weights: Array[Double]): Array[[Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]]
Randomly splits this Dataset with the provided weights.
Randomly splits this Dataset with the provided weights.  

weights
    
weights for splits, will be normalized if they don't sum to 1. 

Since
    
2.0.0
  24. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#randomSplit\(weights:Array\[Double\],seed:Long\):Array\[org.apache.spark.sql.Dataset\[T\]\] "Permalink") abstract  def randomSplit(weights: Array[Double], seed: Long): Array[[Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]]
Randomly splits this Dataset with the provided weights.
Randomly splits this Dataset with the provided weights.  

weights
    
weights for splits, will be normalized if they don't sum to 1. 

seed
    
Seed for sampling. For Java API, use [randomSplitAsList](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#randomSplitAsList\(weights:Array\[Double\],seed:Long\):java.util.List\[org.apache.spark.sql.Dataset\[T\]\]). 

Since
    
2.0.0
  25. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#randomSplitAsList\(weights:Array\[Double\],seed:Long\):java.util.List\[org.apache.spark.sql.Dataset\[T\]\] "Permalink") abstract  def randomSplitAsList(weights: Array[Double], seed: Long): [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html#java.util.List "java.util.List")[[Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]]
Returns a Java list that contains randomly split Dataset with the provided weights.
Returns a Java list that contains randomly split Dataset with the provided weights.  

weights
    
weights for splits, will be normalized if they don't sum to 1. 

seed
    
Seed for sampling. 

Since
    
2.0.0
  26. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#repartition\(numPartitions:Int\):org.apache.spark.sql.Dataset\[T\] "Permalink") abstract  def repartition(numPartitions: Int): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Returns a new Dataset that has exactly `numPartitions` partitions.
Returns a new Dataset that has exactly `numPartitions` partitions.  

Since
    
1.6.0
  27. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#repartitionById\(numPartitions:Int,partitionIdExpr:org.apache.spark.sql.Column\):org.apache.spark.sql.Dataset\[T\] "Permalink") abstract  def repartitionById(numPartitions: Int, partitionIdExpr: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Repartition the Dataset into the given number of partitions using the specified partition ID expression.
Repartition the Dataset into the given number of partitions using the specified partition ID expression.  

numPartitions
    
the number of partitions to use. 

partitionIdExpr
    
the expression to be used as the partition ID. Must be an integer type. 

Since
    
4.1.0
  28. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#sample\(withReplacement:Boolean,fraction:Double,seed:Long\):org.apache.spark.sql.Dataset\[T\] "Permalink") abstract  def sample(withReplacement: Boolean, fraction: Double, seed: Long): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Returns a new [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") by sampling a fraction of rows, using a user-supplied seed.
Returns a new [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") by sampling a fraction of rows, using a user-supplied seed.  

withReplacement
    
Sample with replacement or not. 

fraction
    
Fraction of rows to generate, range [0.0, 1.0]. 

seed
    
Seed for sampling. 

Since
    
1.6.0 

Note
    
This is NOT guaranteed to provide exactly the fraction of the count of the given [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset").
  29. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#select\[U1\]\(c1:org.apache.spark.sql.TypedColumn\[T,U1\]\):org.apache.spark.sql.Dataset\[U1\] "Permalink") abstract  def select[U1](c1: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[T, U1]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[U1]
Returns a new Dataset by computing the given [org.apache.spark.sql.Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column") expression for each element.
Returns a new Dataset by computing the given [org.apache.spark.sql.Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column") expression for each element.

```
val ds = Seq(1, 2, 3).toDS()
val newDS = ds.select(expr("value + 1").as[Int])
```


Since
    
1.6.0
  30. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#union\(other:org.apache.spark.sql.Dataset\[T\]\):org.apache.spark.sql.Dataset\[T\] "Permalink") abstract  def union(other: [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Returns a new Dataset containing union of rows in this Dataset and another Dataset.
Returns a new Dataset containing union of rows in this Dataset and another Dataset.
This is equivalent to `UNION ALL` in SQL. To do a SQL-style set union (that does deduplication of elements), use this function followed by a [distinct](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#distinct\(\):org.apache.spark.sql.Dataset\[T\]).
Also as standard in SQL, this function resolves columns by position (not by name):

```
val df1 = Seq((1, 2, 3)).toDF("col0", "col1", "col2")
val df2 = Seq((4, 5, 6)).toDF("col1", "col2", "col0")
df1.union(df2).show

// output:
// +----+----+----+
// |col0|col1|col2|
// +----+----+----+
// |   1|   2|   3|
// |   4|   5|   6|
// +----+----+----+
```

Notice that the column positions in the schema aren't necessarily matched with the fields in the strongly typed objects in a Dataset. This function resolves columns by their positions in the schema, not the fields in the strongly typed objects. Use [unionByName](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#unionByName\(other:org.apache.spark.sql.Dataset\[T\]\):org.apache.spark.sql.Dataset\[T\]) to resolve columns by field name in the typed objects.  

Since
    
2.0.0
  31. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#unionByName\(other:org.apache.spark.sql.Dataset\[T\],allowMissingColumns:Boolean\):org.apache.spark.sql.Dataset\[T\] "Permalink") abstract  def unionByName(other: [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T], allowMissingColumns: Boolean): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Returns a new Dataset containing union of rows in this Dataset and another Dataset.
Returns a new Dataset containing union of rows in this Dataset and another Dataset.
The difference between this function and [union](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#union\(other:org.apache.spark.sql.Dataset\[T\]\):org.apache.spark.sql.Dataset\[T\]) is that this function resolves columns by name (not by position).
When the parameter `allowMissingColumns` is `true`, the set of column names in this and other `Dataset` can differ; missing columns will be filled with null. Further, the missing columns of this `Dataset` will be added at the end in the schema of the union result:

```
val df1 = Seq((1, 2, 3)).toDF("col0", "col1", "col2")
val df2 = Seq((4, 5, 6)).toDF("col1", "col0", "col3")
df1.unionByName(df2, true).show

// output: "col3" is missing at left df1 and added at the end of schema.
// +----+----+----+----+
// |col0|col1|col2|col3|
// +----+----+----+----+
// |   1|   2|   3|NULL|
// |   5|   4|NULL|   6|
// +----+----+----+----+

df2.unionByName(df1, true).show

// output: "col2" is missing at left df2 and added at the end of schema.
// +----+----+----+----+
// |col1|col0|col3|col2|
// +----+----+----+----+
// |   4|   5|   6|NULL|
// |   2|   1|NULL|   3|
// +----+----+----+----+
```

Note that this supports nested columns in struct and array types. With `allowMissingColumns`, missing nested columns of struct columns with the same name will also be filled with null values and added to the end of struct. Nested columns in map types are not currently supported.  

Since
    
3.1.0
  32. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#alias\(alias:Symbol\):org.apache.spark.sql.Dataset\[T\] "Permalink") def alias(alias: Symbol): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
(Scala-specific) Returns a new Dataset with an alias set.
(Scala-specific) Returns a new Dataset with an alias set. Same as `as`.  

Since
    
2.0.0
  33. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#alias\(alias:String\):org.apache.spark.sql.Dataset\[T\] "Permalink") def alias(alias: String): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Returns a new Dataset with an alias set.
Returns a new Dataset with an alias set. Same as `as`.  

Since
    
2.0.0
  34. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#as\(alias:Symbol\):org.apache.spark.sql.Dataset\[T\] "Permalink") def as(alias: Symbol): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
(Scala-specific) Returns a new Dataset with an alias set.
(Scala-specific) Returns a new Dataset with an alias set.  

Since
    
2.0.0
  35. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#distinct\(\):org.apache.spark.sql.Dataset\[T\] "Permalink") def distinct(): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Returns a new Dataset that contains only the unique rows from this Dataset.
Returns a new Dataset that contains only the unique rows from this Dataset. This is an alias for `dropDuplicates`.
Note that for a streaming [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset"), this method returns distinct rows only once regardless of the output mode, which the behavior may not be same with `DISTINCT` in SQL against streaming [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset").  

Since
    
2.0.0 

Note
    
Equality checking is performed directly on the encoded representation of the data and thus is not affected by a custom `equals` function defined on `T`.
  36. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#dropDuplicates\(col1:String,cols:String*\):org.apache.spark.sql.Dataset\[T\] "Permalink") def dropDuplicates(col1: String, cols: String*): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Returns a new [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") with duplicate rows removed, considering only the subset of columns.
Returns a new [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") with duplicate rows removed, considering only the subset of columns.
For a static batch [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset"), it just drops duplicate rows. For a streaming [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset"), it will keep all data across triggers as intermediate state to drop duplicates rows. You can use [withWatermark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#withWatermark\(eventTime:String,delayThreshold:String\):org.apache.spark.sql.Dataset\[T\]) to limit how late the duplicate data can be and system will accordingly limit the state. In addition, too late data older than watermark will be dropped to avoid any possibility of duplicates.  

Annotations
     @varargs() 

Since
    
2.0.0
  37. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#dropDuplicates\(colNames:Array\[String\]\):org.apache.spark.sql.Dataset\[T\] "Permalink") def dropDuplicates(colNames: Array[String]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Returns a new Dataset with duplicate rows removed, considering only the subset of columns.
Returns a new Dataset with duplicate rows removed, considering only the subset of columns.
For a static batch [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset"), it just drops duplicate rows. For a streaming [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset"), it will keep all data across triggers as intermediate state to drop duplicates rows. You can use [withWatermark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#withWatermark\(eventTime:String,delayThreshold:String\):org.apache.spark.sql.Dataset\[T\]) to limit how late the duplicate data can be and system will accordingly limit the state. In addition, too late data older than watermark will be dropped to avoid any possibility of duplicates.  

Since
    
2.0.0
  38. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#dropDuplicatesWithinWatermark\(col1:String,cols:String*\):org.apache.spark.sql.Dataset\[T\] "Permalink") def dropDuplicatesWithinWatermark(col1: String, cols: String*): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Returns a new Dataset with duplicates rows removed, considering only the subset of columns, within watermark.
Returns a new Dataset with duplicates rows removed, considering only the subset of columns, within watermark.
This only works with streaming [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset"), and watermark for the input [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") must be set via [withWatermark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#withWatermark\(eventTime:String,delayThreshold:String\):org.apache.spark.sql.Dataset\[T\]).
For a streaming [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset"), this will keep all data across triggers as intermediate state to drop duplicated rows. The state will be kept to guarantee the semantic, "Events are deduplicated as long as the time distance of earliest and latest events are smaller than the delay threshold of watermark." Users are encouraged to set the delay threshold of watermark longer than max timestamp differences among duplicated events.
Note: too late data older than watermark will be dropped.  

Annotations
     @varargs() 

Since
    
3.5.0
  39. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#dropDuplicatesWithinWatermark\(colNames:Array\[String\]\):org.apache.spark.sql.Dataset\[T\] "Permalink") def dropDuplicatesWithinWatermark(colNames: Array[String]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Returns a new Dataset with duplicates rows removed, considering only the subset of columns, within watermark.
Returns a new Dataset with duplicates rows removed, considering only the subset of columns, within watermark.
This only works with streaming [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset"), and watermark for the input [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") must be set via [withWatermark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#withWatermark\(eventTime:String,delayThreshold:String\):org.apache.spark.sql.Dataset\[T\]).
For a streaming [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset"), this will keep all data across triggers as intermediate state to drop duplicated rows. The state will be kept to guarantee the semantic, "Events are deduplicated as long as the time distance of earliest and latest events are smaller than the delay threshold of watermark." Users are encouraged to set the delay threshold of watermark longer than max timestamp differences among duplicated events.
Note: too late data older than watermark will be dropped.  

Since
    
3.5.0
  40. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#filter\(conditionExpr:String\):org.apache.spark.sql.Dataset\[T\] "Permalink") def filter(conditionExpr: String): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Filters rows using the given SQL expression.
Filters rows using the given SQL expression.

```
peopleDs.filter("age > 15")
```


Since
    
1.6.0
  41. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#flatMap\[U\]\(f:org.apache.spark.api.java.function.FlatMapFunction\[T,U\],encoder:org.apache.spark.sql.Encoder\[U\]\):org.apache.spark.sql.Dataset\[U\] "Permalink") def flatMap[U](f: [FlatMapFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/FlatMapFunction.html "org.apache.spark.api.java.function.FlatMapFunction")[T, U], encoder: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[U]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[U]
(Java-specific) Returns a new Dataset by first applying a function to all elements of this Dataset, and then flattening the results.
(Java-specific) Returns a new Dataset by first applying a function to all elements of this Dataset, and then flattening the results.  

Since
    
1.6.0
  42. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#flatMap\[U\]\(func:T=>IterableOnce\[U\]\)\(implicitevidence$7:org.apache.spark.sql.Encoder\[U\]\):org.apache.spark.sql.Dataset\[U\] "Permalink") def flatMap[U](func: (T) => IterableOnce[U])(implicit arg0: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[U]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[U]
(Scala-specific) Returns a new Dataset by first applying a function to all elements of this Dataset, and then flattening the results.
(Scala-specific) Returns a new Dataset by first applying a function to all elements of this Dataset, and then flattening the results.  

Since
    
1.6.0
  43. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#groupByKey\[K\]\(func:org.apache.spark.api.java.function.MapFunction\[T,K\],encoder:org.apache.spark.sql.Encoder\[K\]\):org.apache.spark.sql.KeyValueGroupedDataset\[K,T\] "Permalink") def groupByKey[K](func: [MapFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/MapFunction.html "org.apache.spark.api.java.function.MapFunction")[T, K], encoder: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[K]): [KeyValueGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html "org.apache.spark.sql.KeyValueGroupedDataset")[K, T]
(Java-specific) Returns a [KeyValueGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html "org.apache.spark.sql.KeyValueGroupedDataset") where the data is grouped by the given key `func`.
(Java-specific) Returns a [KeyValueGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html "org.apache.spark.sql.KeyValueGroupedDataset") where the data is grouped by the given key `func`.  

Since
    
2.0.0
  44. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#joinWith\[U\]\(other:org.apache.spark.sql.Dataset\[U\],condition:org.apache.spark.sql.Column\):org.apache.spark.sql.Dataset\[\(T,U\)\] "Permalink") def joinWith[U](other: [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[U], condition: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[(T, U)]
Using inner equi-join to join this Dataset returning a `Tuple2` for each pair where `condition` evaluates to true.
Using inner equi-join to join this Dataset returning a `Tuple2` for each pair where `condition` evaluates to true.  

other
    
Right side of the join. 

condition
    
Join expression. 

Since
    
1.6.0
  45. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#mapPartitions\[U\]\(f:org.apache.spark.api.java.function.MapPartitionsFunction\[T,U\],encoder:org.apache.spark.sql.Encoder\[U\]\):org.apache.spark.sql.Dataset\[U\] "Permalink") def mapPartitions[U](f: [MapPartitionsFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/java/function/MapPartitionsFunction.html "org.apache.spark.api.java.function.MapPartitionsFunction")[T, U], encoder: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[U]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[U]
(Java-specific) Returns a new Dataset that contains the result of applying `f` to each partition.
(Java-specific) Returns a new Dataset that contains the result of applying `f` to each partition.  

Since
    
1.6.0
  46. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#orderBy\(sortExprs:org.apache.spark.sql.Column*\):org.apache.spark.sql.Dataset\[T\] "Permalink") def orderBy(sortExprs: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")*): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Returns a new Dataset sorted by the given expressions.
Returns a new Dataset sorted by the given expressions. This is an alias of the `sort` function.  

Annotations
     @varargs() 

Since
    
2.0.0
  47. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#orderBy\(sortCol:String,sortCols:String*\):org.apache.spark.sql.Dataset\[T\] "Permalink") def orderBy(sortCol: String, sortCols: String*): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Returns a new Dataset sorted by the given expressions.
Returns a new Dataset sorted by the given expressions. This is an alias of the `sort` function.  

Annotations
     @varargs() 

Since
    
2.0.0
  48. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#repartition\(partitionExprs:org.apache.spark.sql.Column*\):org.apache.spark.sql.Dataset\[T\] "Permalink") def repartition(partitionExprs: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")*): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Returns a new Dataset partitioned by the given partitioning expressions, using `spark.sql.shuffle.partitions` as number of partitions.
Returns a new Dataset partitioned by the given partitioning expressions, using `spark.sql.shuffle.partitions` as number of partitions. The resulting Dataset is hash partitioned.
This is the same operation as "DISTRIBUTE BY" in SQL (Hive QL).  

Annotations
     @varargs() 

Since
    
2.0.0
  49. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#repartition\(numPartitions:Int,partitionExprs:org.apache.spark.sql.Column*\):org.apache.spark.sql.Dataset\[T\] "Permalink") def repartition(numPartitions: Int, partitionExprs: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")*): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Returns a new Dataset partitioned by the given partitioning expressions into `numPartitions`.
Returns a new Dataset partitioned by the given partitioning expressions into `numPartitions`. The resulting Dataset is hash partitioned.
This is the same operation as "DISTRIBUTE BY" in SQL (Hive QL).  

Annotations
     @varargs() 

Since
    
2.0.0
  50. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#repartitionByRange\(partitionExprs:org.apache.spark.sql.Column*\):org.apache.spark.sql.Dataset\[T\] "Permalink") def repartitionByRange(partitionExprs: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")*): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Returns a new Dataset partitioned by the given partitioning expressions, using `spark.sql.shuffle.partitions` as number of partitions.
Returns a new Dataset partitioned by the given partitioning expressions, using `spark.sql.shuffle.partitions` as number of partitions. The resulting Dataset is range partitioned.
At least one partition-by expression must be specified. When no explicit sort order is specified, "ascending nulls first" is assumed. Note, the rows are not sorted in each partition of the resulting Dataset.
Note that due to performance reasons this method uses sampling to estimate the ranges. Hence, the output may not be consistent, since sampling can return different values. The sample size can be controlled by the config `spark.sql.execution.rangeExchange.sampleSizePerPartition`.  

Annotations
     @varargs() 

Since
    
2.3.0
  51. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#repartitionByRange\(numPartitions:Int,partitionExprs:org.apache.spark.sql.Column*\):org.apache.spark.sql.Dataset\[T\] "Permalink") def repartitionByRange(numPartitions: Int, partitionExprs: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")*): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Returns a new Dataset partitioned by the given partitioning expressions into `numPartitions`.
Returns a new Dataset partitioned by the given partitioning expressions into `numPartitions`. The resulting Dataset is range partitioned.
At least one partition-by expression must be specified. When no explicit sort order is specified, "ascending nulls first" is assumed. Note, the rows are not sorted in each partition of the resulting Dataset.
Note that due to performance reasons this method uses sampling to estimate the ranges. Hence, the output may not be consistent, since sampling can return different values. The sample size can be controlled by the config `spark.sql.execution.rangeExchange.sampleSizePerPartition`.  

Annotations
     @varargs() 

Since
    
2.3.0
  52. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#sample\(withReplacement:Boolean,fraction:Double\):org.apache.spark.sql.Dataset\[T\] "Permalink") def sample(withReplacement: Boolean, fraction: Double): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Returns a new [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") by sampling a fraction of rows, using a random seed.
Returns a new [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") by sampling a fraction of rows, using a random seed.  

withReplacement
    
Sample with replacement or not. 

fraction
    
Fraction of rows to generate, range [0.0, 1.0]. 

Since
    
1.6.0 

Note
    
This is NOT guaranteed to provide exactly the fraction of the total count of the given [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset").
  53. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#sample\(fraction:Double\):org.apache.spark.sql.Dataset\[T\] "Permalink") def sample(fraction: Double): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Returns a new [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") by sampling a fraction of rows (without replacement), using a random seed.
Returns a new [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") by sampling a fraction of rows (without replacement), using a random seed.  

fraction
    
Fraction of rows to generate, range [0.0, 1.0]. 

Since
    
2.3.0 

Note
    
This is NOT guaranteed to provide exactly the fraction of the count of the given [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset").
  54. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#sample\(fraction:Double,seed:Long\):org.apache.spark.sql.Dataset\[T\] "Permalink") def sample(fraction: Double, seed: Long): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Returns a new [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") by sampling a fraction of rows (without replacement), using a user-supplied seed.
Returns a new [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") by sampling a fraction of rows (without replacement), using a user-supplied seed.  

fraction
    
Fraction of rows to generate, range [0.0, 1.0]. 

seed
    
Seed for sampling. 

Since
    
2.3.0 

Note
    
This is NOT guaranteed to provide exactly the fraction of the count of the given [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset").
  55. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#select\[U1,U2,U3,U4,U5\]\(c1:org.apache.spark.sql.TypedColumn\[T,U1\],c2:org.apache.spark.sql.TypedColumn\[T,U2\],c3:org.apache.spark.sql.TypedColumn\[T,U3\],c4:org.apache.spark.sql.TypedColumn\[T,U4\],c5:org.apache.spark.sql.TypedColumn\[T,U5\]\):org.apache.spark.sql.Dataset\[\(U1,U2,U3,U4,U5\)\] "Permalink") def select[U1, U2, U3, U4, U5](c1: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[T, U1], c2: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[T, U2], c3: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[T, U3], c4: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[T, U4], c5: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[T, U5]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[(U1, U2, U3, U4, U5)]
Returns a new Dataset by computing the given [org.apache.spark.sql.Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column") expressions for each element.
Returns a new Dataset by computing the given [org.apache.spark.sql.Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column") expressions for each element.  

Since
    
1.6.0
  56. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#select\[U1,U2,U3,U4\]\(c1:org.apache.spark.sql.TypedColumn\[T,U1\],c2:org.apache.spark.sql.TypedColumn\[T,U2\],c3:org.apache.spark.sql.TypedColumn\[T,U3\],c4:org.apache.spark.sql.TypedColumn\[T,U4\]\):org.apache.spark.sql.Dataset\[\(U1,U2,U3,U4\)\] "Permalink") def select[U1, U2, U3, U4](c1: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[T, U1], c2: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[T, U2], c3: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[T, U3], c4: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[T, U4]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[(U1, U2, U3, U4)]
Returns a new Dataset by computing the given [org.apache.spark.sql.Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column") expressions for each element.
Returns a new Dataset by computing the given [org.apache.spark.sql.Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column") expressions for each element.  

Since
    
1.6.0
  57. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#select\[U1,U2,U3\]\(c1:org.apache.spark.sql.TypedColumn\[T,U1\],c2:org.apache.spark.sql.TypedColumn\[T,U2\],c3:org.apache.spark.sql.TypedColumn\[T,U3\]\):org.apache.spark.sql.Dataset\[\(U1,U2,U3\)\] "Permalink") def select[U1, U2, U3](c1: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[T, U1], c2: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[T, U2], c3: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[T, U3]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[(U1, U2, U3)]
Returns a new Dataset by computing the given [org.apache.spark.sql.Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column") expressions for each element.
Returns a new Dataset by computing the given [org.apache.spark.sql.Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column") expressions for each element.  

Since
    
1.6.0
  58. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#select\[U1,U2\]\(c1:org.apache.spark.sql.TypedColumn\[T,U1\],c2:org.apache.spark.sql.TypedColumn\[T,U2\]\):org.apache.spark.sql.Dataset\[\(U1,U2\)\] "Permalink") def select[U1, U2](c1: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[T, U1], c2: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[T, U2]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[(U1, U2)]
Returns a new Dataset by computing the given [org.apache.spark.sql.Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column") expressions for each element.
Returns a new Dataset by computing the given [org.apache.spark.sql.Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column") expressions for each element.  

Since
    
1.6.0
  59. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#sort\(sortExprs:org.apache.spark.sql.Column*\):org.apache.spark.sql.Dataset\[T\] "Permalink") def sort(sortExprs: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")*): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Returns a new Dataset sorted by the given expressions.
Returns a new Dataset sorted by the given expressions. For example:

```
ds.sort($"col1", $"col2".desc)
```


Annotations
     @varargs() 

Since
    
2.0.0
  60. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#sort\(sortCol:String,sortCols:String*\):org.apache.spark.sql.Dataset\[T\] "Permalink") def sort(sortCol: String, sortCols: String*): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Returns a new Dataset sorted by the specified column, all in ascending order.
Returns a new Dataset sorted by the specified column, all in ascending order.

```
// The following 3 are equivalent
ds.sort("sortcol")
ds.sort($"sortcol")
ds.sort($"sortcol".asc)
```


Annotations
     @varargs() 

Since
    
2.0.0
  61. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#sortWithinPartitions\(sortExprs:org.apache.spark.sql.Column*\):org.apache.spark.sql.Dataset\[T\] "Permalink") def sortWithinPartitions(sortExprs: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")*): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Returns a new Dataset with each partition sorted by the given expressions.
Returns a new Dataset with each partition sorted by the given expressions.
This is the same operation as "SORT BY" in SQL (Hive QL).  

Annotations
     @varargs() 

Since
    
2.0.0
  62. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#sortWithinPartitions\(sortCol:String,sortCols:String*\):org.apache.spark.sql.Dataset\[T\] "Permalink") def sortWithinPartitions(sortCol: String, sortCols: String*): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Returns a new Dataset with each partition sorted by the given expressions.
Returns a new Dataset with each partition sorted by the given expressions.
This is the same operation as "SORT BY" in SQL (Hive QL).  

Annotations
     @varargs() 

Since
    
2.0.0
  63. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#transform\[U,DSO\[_\]<:org.apache.spark.sql.Dataset\[_\]\]\(t:Dataset.this.type=>DSO\[U\]\):DSO\[U\] "Permalink") def transform[U, DSO[_] <: [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[_]](t: ([Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset").this.type) => DSO[U]): DSO[U]
Concise syntax for chaining custom transformations.
Concise syntax for chaining custom transformations.

```
def featurize(ds: Dataset[T]): Dataset[U] = ...

ds
  .transform(featurize)
  .transform(...)
```


Since
    
1.6.0
  64. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#unionAll\(other:org.apache.spark.sql.Dataset\[T\]\):org.apache.spark.sql.Dataset\[T\] "Permalink") def unionAll(other: [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Returns a new Dataset containing union of rows in this Dataset and another Dataset.
Returns a new Dataset containing union of rows in this Dataset and another Dataset. This is an alias for `union`.
This is equivalent to `UNION ALL` in SQL. To do a SQL-style set union (that does deduplication of elements), use this function followed by a [distinct](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#distinct\(\):org.apache.spark.sql.Dataset\[T\]).
Also as standard in SQL, this function resolves columns by position (not by name).  

Since
    
2.0.0
  65. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#unionByName\(other:org.apache.spark.sql.Dataset\[T\]\):org.apache.spark.sql.Dataset\[T\] "Permalink") def unionByName(other: [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Returns a new Dataset containing union of rows in this Dataset and another Dataset.
Returns a new Dataset containing union of rows in this Dataset and another Dataset.
This is different from both `UNION ALL` and `UNION DISTINCT` in SQL. To do a SQL-style set union (that does deduplication of elements), use this function followed by a [distinct](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#distinct\(\):org.apache.spark.sql.Dataset\[T\]).
The difference between this function and [union](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#union\(other:org.apache.spark.sql.Dataset\[T\]\):org.apache.spark.sql.Dataset\[T\]) is that this function resolves columns by name (not by position):

```
val df1 = Seq((1, 2, 3)).toDF("col0", "col1", "col2")
val df2 = Seq((4, 5, 6)).toDF("col1", "col2", "col0")
df1.unionByName(df2).show

// output:
// +----+----+----+
// |col0|col1|col2|
// +----+----+----+
// |   1|   2|   3|
// |   6|   4|   5|
// +----+----+----+
```

Note that this supports nested columns in struct and array types. Nested columns in map types are not currently supported.  

Since
    
2.3.0
  66. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#where\(conditionExpr:String\):org.apache.spark.sql.Dataset\[T\] "Permalink") def where(conditionExpr: String): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Filters rows using the given SQL expression.
Filters rows using the given SQL expression.

```
peopleDs.where("age > 15")
```


Since
    
1.6.0
  67. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#where\(condition:org.apache.spark.sql.Column\):org.apache.spark.sql.Dataset\[T\] "Permalink") def where(condition: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Filters rows using the given condition.
Filters rows using the given condition. This is an alias for `filter`.

```
// The following are equivalent:
peopleDs.filter($"age" > 15)
peopleDs.where($"age" > 15)
```


Since
    
1.6.0


### Untyped transformations
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#col\(colName:String\):org.apache.spark.sql.Column "Permalink") abstract  def col(colName: String): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Selects column based on the column name and returns it as a [org.apache.spark.sql.Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column").
Selects column based on the column name and returns it as a [org.apache.spark.sql.Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column").  

Since
    
2.0.0 

Note
    
The column name can also reference to a nested column like `a.b`.
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#colRegex\(colName:String\):org.apache.spark.sql.Column "Permalink") abstract  def colRegex(colName: String): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Selects column based on the column name specified as a regex and returns it as [org.apache.spark.sql.Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column").
Selects column based on the column name specified as a regex and returns it as [org.apache.spark.sql.Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column").  

Since
    
2.3.0
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#crossJoin\(right:org.apache.spark.sql.Dataset\[_\]\):org.apache.spark.sql.DataFrame "Permalink") abstract  def crossJoin(right: [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[_]): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Explicit cartesian join with another `DataFrame`.
Explicit cartesian join with another `DataFrame`.  

right
    
Right side of the join operation. 

Since
    
2.1.0 

Note
    
Cartesian joins are very expensive without an extra filter that can be pushed down.
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#cube\(cols:org.apache.spark.sql.Column*\):org.apache.spark.sql.RelationalGroupedDataset "Permalink") abstract  def cube(cols: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")*): [RelationalGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/RelationalGroupedDataset.html "org.apache.spark.sql.RelationalGroupedDataset")
Create a multi-dimensional cube for the current Dataset using the specified columns, so we can run aggregation on them.
Create a multi-dimensional cube for the current Dataset using the specified columns, so we can run aggregation on them. See [RelationalGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/RelationalGroupedDataset.html "org.apache.spark.sql.RelationalGroupedDataset") for all the available aggregate functions.

```
// Compute the average for all numeric columns cubed by department and group.
ds.cube($"department", $"group").avg()

// Compute the max age and average salary, cubed by department and gender.
ds.cube($"department", $"gender").agg(Map(
  "salary" -> "avg",
  "age" -> "max"
))
```


Annotations
     @varargs() 

Since
    
2.0.0
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#drop\(col:org.apache.spark.sql.Column,cols:org.apache.spark.sql.Column*\):org.apache.spark.sql.DataFrame "Permalink") abstract  def drop(col: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column"), cols: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")*): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Returns a new Dataset with columns dropped.
Returns a new Dataset with columns dropped.
This method can only be used to drop top level columns. This is a no-op if the Dataset doesn't have a columns with an equivalent expression.  

Annotations
     @varargs() 

Since
    
3.4.0
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#drop\(colNames:String*\):org.apache.spark.sql.DataFrame "Permalink") abstract  def drop(colNames: String*): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Returns a new Dataset with columns dropped.
Returns a new Dataset with columns dropped. This is a no-op if schema doesn't contain column name(s).
This method can only be used to drop top level columns. the colName string is treated literally without further interpretation.  

Annotations
     @varargs() 

Since
    
2.0.0
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#groupBy\(cols:org.apache.spark.sql.Column*\):org.apache.spark.sql.RelationalGroupedDataset "Permalink") abstract  def groupBy(cols: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")*): [RelationalGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/RelationalGroupedDataset.html "org.apache.spark.sql.RelationalGroupedDataset")
Groups the Dataset using the specified columns, so we can run aggregation on them.
Groups the Dataset using the specified columns, so we can run aggregation on them. See [RelationalGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/RelationalGroupedDataset.html "org.apache.spark.sql.RelationalGroupedDataset") for all the available aggregate functions.

```
// Compute the average for all numeric columns grouped by department.
ds.groupBy($"department").avg()

// Compute the max age and average salary, grouped by department and gender.
ds.groupBy($"department", $"gender").agg(Map(
  "salary" -> "avg",
  "age" -> "max"
))
```


Annotations
     @varargs() 

Since
    
2.0.0
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#groupingSets\(groupingSets:Seq\[Seq\[org.apache.spark.sql.Column\]\],cols:org.apache.spark.sql.Column*\):org.apache.spark.sql.RelationalGroupedDataset "Permalink") abstract  def groupingSets(groupingSets: Seq[Seq[[Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")]], cols: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")*): [RelationalGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/RelationalGroupedDataset.html "org.apache.spark.sql.RelationalGroupedDataset")
Create multi-dimensional aggregation for the current Dataset using the specified grouping sets, so we can run aggregation on them.
Create multi-dimensional aggregation for the current Dataset using the specified grouping sets, so we can run aggregation on them. See [RelationalGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/RelationalGroupedDataset.html "org.apache.spark.sql.RelationalGroupedDataset") for all the available aggregate functions.

```
// Compute the average for all numeric columns group by specific grouping sets.
ds.groupingSets(Seq(Seq($"department", $"group"), Seq()), $"department", $"group").avg()

// Compute the max age and average salary, group by specific grouping sets.
ds.groupingSets(Seq($"department", $"gender"), Seq()), $"department", $"group").agg(Map(
  "salary" -> "avg",
  "age" -> "max"
))
```


Annotations
     @varargs() 

Since
    
4.0.0
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#join\(right:org.apache.spark.sql.Dataset\[_\],joinExprs:org.apache.spark.sql.Column,joinType:String\):org.apache.spark.sql.DataFrame "Permalink") abstract  def join(right: [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[_], joinExprs: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column"), joinType: String): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Join with another `DataFrame`, using the given join expression.
Join with another `DataFrame`, using the given join expression. The following performs a full outer join between `df1` and `df2`.

```
// Scala:
import org.apache.spark.sql.functions._
df1.join(df2, $"df1Key" === $"df2Key", "outer")

// Java:
import static org.apache.spark.sql.functions.*;
df1.join(df2, col("df1Key").equalTo(col("df2Key")), "outer");
```


right
    
Right side of the join. 

joinExprs
    
Join expression. 

joinType
    
Type of join to perform. Default `inner`. Must be one of: `inner`, `cross`, `outer`, `full`, `fullouter`, `full_outer`, `left`, `leftouter`, `left_outer`, `right`, `rightouter`, `right_outer`, `semi`, `leftsemi`, `left_semi`, `anti`, `leftanti`, `left_anti`. 

Since
    
2.0.0
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#join\(right:org.apache.spark.sql.Dataset\[_\],usingColumns:Seq\[String\],joinType:String\):org.apache.spark.sql.DataFrame "Permalink") abstract  def join(right: [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[_], usingColumns: Seq[String], joinType: String): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
(Scala-specific) Equi-join with another `DataFrame` using the given columns.
(Scala-specific) Equi-join with another `DataFrame` using the given columns. A cross join with a predicate is specified as an inner join. If you would explicitly like to perform a cross join use the `crossJoin` method.
Different from other join functions, the join columns will only appear once in the output, i.e. similar to SQL's `JOIN USING` syntax.  

right
    
Right side of the join operation. 

usingColumns
    
Names of the columns to join on. This columns must exist on both sides. 

joinType
    
Type of join to perform. Default `inner`. Must be one of: `inner`, `cross`, `outer`, `full`, `fullouter`, `full_outer`, `left`, `leftouter`, `left_outer`, `right`, `rightouter`, `right_outer`, `semi`, `leftsemi`, `left_semi`, `anti`, `leftanti`, `left_anti`. 

Since
    
2.0.0 

Note
    
If you perform a self-join using this function without aliasing the input `DataFrame`s, you will NOT be able to reference any columns after the join, since there is no way to disambiguate which side of the join you would like to reference.
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#join\(right:org.apache.spark.sql.Dataset\[_\]\):org.apache.spark.sql.DataFrame "Permalink") abstract  def join(right: [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[_]): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Join with another `DataFrame`.
Join with another `DataFrame`.
Behaves as an INNER JOIN and requires a subsequent join predicate.  

right
    
Right side of the join operation. 

Since
    
2.0.0
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#lateralJoin\(right:org.apache.spark.sql.Dataset\[_\],joinExprs:org.apache.spark.sql.Column,joinType:String\):org.apache.spark.sql.DataFrame "Permalink") abstract  def lateralJoin(right: [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[_], joinExprs: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column"), joinType: String): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Lateral join with another `DataFrame`.
Lateral join with another `DataFrame`.  

right
    
Right side of the join operation. 

joinExprs
    
Join expression. 

joinType
    
Type of join to perform. Default `inner`. Must be one of: `inner`, `cross`, `left`, `leftouter`, `left_outer`. 

Since
    
4.0.0
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#lateralJoin\(right:org.apache.spark.sql.Dataset\[_\],joinType:String\):org.apache.spark.sql.DataFrame "Permalink") abstract  def lateralJoin(right: [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[_], joinType: String): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Lateral join with another `DataFrame`.
Lateral join with another `DataFrame`.  

right
    
Right side of the join operation. 

joinType
    
Type of join to perform. Default `inner`. Must be one of: `inner`, `cross`, `left`, `leftouter`, `left_outer`. 

Since
    
4.0.0
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#lateralJoin\(right:org.apache.spark.sql.Dataset\[_\],joinExprs:org.apache.spark.sql.Column\):org.apache.spark.sql.DataFrame "Permalink") abstract  def lateralJoin(right: [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[_], joinExprs: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Lateral join with another `DataFrame`.
Lateral join with another `DataFrame`.
Behaves as an JOIN LATERAL.  

right
    
Right side of the join operation. 

joinExprs
    
Join expression. 

Since
    
4.0.0
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#lateralJoin\(right:org.apache.spark.sql.Dataset\[_\]\):org.apache.spark.sql.DataFrame "Permalink") abstract  def lateralJoin(right: [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[_]): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Lateral join with another `DataFrame`.
Lateral join with another `DataFrame`.
Behaves as an JOIN LATERAL.  

right
    
Right side of the join operation. 

Since
    
4.0.0
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#metadataColumn\(colName:String\):org.apache.spark.sql.Column "Permalink") abstract  def metadataColumn(colName: String): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Selects a metadata column based on its logical column name, and returns it as a [org.apache.spark.sql.Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column").
Selects a metadata column based on its logical column name, and returns it as a [org.apache.spark.sql.Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column").
A metadata column can be accessed this way even if the underlying data source defines a data column with a conflicting name.  

Since
    
3.5.0
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#na:org.apache.spark.sql.DataFrameNaFunctions "Permalink") abstract  def na: [DataFrameNaFunctions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/DataFrameNaFunctions.html "org.apache.spark.sql.DataFrameNaFunctions")
Returns a [DataFrameNaFunctions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/DataFrameNaFunctions.html "org.apache.spark.sql.DataFrameNaFunctions") for working with missing data.
Returns a [DataFrameNaFunctions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/DataFrameNaFunctions.html "org.apache.spark.sql.DataFrameNaFunctions") for working with missing data.

```
// Dropping rows containing any null values.
ds.na.drop()
```


Since
    
1.6.0
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#rollup\(cols:org.apache.spark.sql.Column*\):org.apache.spark.sql.RelationalGroupedDataset "Permalink") abstract  def rollup(cols: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")*): [RelationalGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/RelationalGroupedDataset.html "org.apache.spark.sql.RelationalGroupedDataset")
Create a multi-dimensional rollup for the current Dataset using the specified columns, so we can run aggregation on them.
Create a multi-dimensional rollup for the current Dataset using the specified columns, so we can run aggregation on them. See [RelationalGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/RelationalGroupedDataset.html "org.apache.spark.sql.RelationalGroupedDataset") for all the available aggregate functions.

```
// Compute the average for all numeric columns rolled up by department and group.
ds.rollup($"department", $"group").avg()

// Compute the max age and average salary, rolled up by department and gender.
ds.rollup($"department", $"gender").agg(Map(
  "salary" -> "avg",
  "age" -> "max"
))
```


Annotations
     @varargs() 

Since
    
2.0.0
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#select\(cols:org.apache.spark.sql.Column*\):org.apache.spark.sql.DataFrame "Permalink") abstract  def select(cols: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")*): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Selects a set of column based expressions.
Selects a set of column based expressions.

```
ds.select($"colA", $"colB" + 1)
```


Annotations
     @varargs() 

Since
    
2.0.0
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#stat:org.apache.spark.sql.DataFrameStatFunctions "Permalink") abstract  def stat: [DataFrameStatFunctions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/DataFrameStatFunctions.html "org.apache.spark.sql.DataFrameStatFunctions")
Returns a [DataFrameStatFunctions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/DataFrameStatFunctions.html "org.apache.spark.sql.DataFrameStatFunctions") for working statistic functions support.
Returns a [DataFrameStatFunctions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/DataFrameStatFunctions.html "org.apache.spark.sql.DataFrameStatFunctions") for working statistic functions support.

```
// Finding frequent items in column with name 'a'.
ds.stat.freqItems(Seq("a"))
```


Since
    
1.6.0
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#transpose\(\):org.apache.spark.sql.DataFrame "Permalink") abstract  def transpose(): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Transposes a DataFrame, switching rows to columns.
Transposes a DataFrame, switching rows to columns. This function transforms the DataFrame such that the values in the first column become the new columns of the DataFrame.
This is equivalent to calling `Dataset#transpose(Column)` where `indexColumn` is set to the first column.
Please note:
     * All columns except the index column must share a least common data type. Unless they are the same data type, all columns are cast to the nearest common data type.
     * The name of the column into which the original column names are transposed defaults to "key".
     * Non-"key" column names for the transposed table are ordered in ascending order.  

Since
    
4.0.0
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#transpose\(indexColumn:org.apache.spark.sql.Column\):org.apache.spark.sql.DataFrame "Permalink") abstract  def transpose(indexColumn: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Transposes a DataFrame such that the values in the specified index column become the new columns of the DataFrame.
Transposes a DataFrame such that the values in the specified index column become the new columns of the DataFrame.
Please note:
     * All columns except the index column must share a least common data type. Unless they are the same data type, all columns are cast to the nearest common data type.
     * The name of the column into which the original column names are transposed defaults to "key".
     * null values in the index column are excluded from the column names for the transposed table, which are ordered in ascending order.

```
val df = Seq(("A", 1, 2), ("B", 3, 4)).toDF("id", "val1", "val2")
df.show()
// output:
// +---+----+----+
// | id|val1|val2|
// +---+----+----+
// |  A|   1|   2|
// |  B|   3|   4|
// +---+----+----+

df.transpose($"id").show()
// output:
// +----+---+---+
// | key|  A|  B|
// +----+---+---+
// |val1|  1|  3|
// |val2|  2|  4|
// +----+---+---+
// schema:
// root
//  |-- key: string (nullable = false)
//  |-- A: integer (nullable = true)
//  |-- B: integer (nullable = true)

df.transpose().show()
// output:
// +----+---+---+
// | key|  A|  B|
// +----+---+---+
// |val1|  1|  3|
// |val2|  2|  4|
// +----+---+---+
// schema:
// root
//  |-- key: string (nullable = false)
//  |-- A: integer (nullable = true)
//  |-- B: integer (nullable = true)
```


indexColumn
    
The single column that will be treated as the index for the transpose operation. This column will be used to pivot the data, transforming the DataFrame such that the values of the indexColumn become the new columns in the transposed DataFrame. 

Since
    
4.0.0
  23. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#unpivot\(ids:Array\[org.apache.spark.sql.Column\],variableColumnName:String,valueColumnName:String\):org.apache.spark.sql.DataFrame "Permalink") abstract  def unpivot(ids: Array[[Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")], variableColumnName: String, valueColumnName: String): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Unpivot a DataFrame from wide format to long format, optionally leaving identifier columns set.
Unpivot a DataFrame from wide format to long format, optionally leaving identifier columns set. This is the reverse to `groupBy(...).pivot(...).agg(...)`, except for the aggregation, which cannot be reversed.  

ids
    
Id columns 

variableColumnName
    
Name of the variable column 

valueColumnName
    
Name of the value column 

Since
    
3.4.0 

See also
    
`org.apache.spark.sql.Dataset.unpivot(Array, Array, String, String)` This is equivalent to calling `Dataset#unpivot(Array, Array, String, String)` where `values` is set to all non-id columns that exist in the DataFrame.
  24. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#unpivot\(ids:Array\[org.apache.spark.sql.Column\],values:Array\[org.apache.spark.sql.Column\],variableColumnName:String,valueColumnName:String\):org.apache.spark.sql.DataFrame "Permalink") abstract  def unpivot(ids: Array[[Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")], values: Array[[Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")], variableColumnName: String, valueColumnName: String): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Unpivot a DataFrame from wide format to long format, optionally leaving identifier columns set.
Unpivot a DataFrame from wide format to long format, optionally leaving identifier columns set. This is the reverse to `groupBy(...).pivot(...).agg(...)`, except for the aggregation, which cannot be reversed.
This function is useful to massage a DataFrame into a format where some columns are identifier columns ("ids"), while all other columns ("values") are "unpivoted" to the rows, leaving just two non-id columns, named as given by `variableColumnName` and `valueColumnName`.

```
val df = Seq((1, 11, 12L), (2, 21, 22L)).toDF("id", "int", "long")
df.show()
// output:
// +---+---+----+
// | id|int|long|
// +---+---+----+
// |  1| 11|  12|
// |  2| 21|  22|
// +---+---+----+

df.unpivot(Array($"id"), Array($"int", $"long"), "variable", "value").show()
// output:
// +---+--------+-----+
// | id|variable|value|
// +---+--------+-----+
// |  1|     int|   11|
// |  1|    long|   12|
// |  2|     int|   21|
// |  2|    long|   22|
// +---+--------+-----+
// schema:
//root
// |-- id: integer (nullable = false)
// |-- variable: string (nullable = false)
// |-- value: long (nullable = true)
```

When no "id" columns are given, the unpivoted DataFrame consists of only the "variable" and "value" columns.
All "value" columns must share a least common data type. Unless they are the same data type, all "value" columns are cast to the nearest common data type. For instance, types `IntegerType` and `LongType` are cast to `LongType`, while `IntegerType` and `StringType` do not have a common data type and `unpivot` fails with an `AnalysisException`.  

ids
    
Id columns 

values
    
Value columns to unpivot 

variableColumnName
    
Name of the variable column 

valueColumnName
    
Name of the value column 

Since
    
3.4.0
  25. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#withMetadata\(columnName:String,metadata:org.apache.spark.sql.types.Metadata\):org.apache.spark.sql.DataFrame "Permalink") abstract  def withMetadata(columnName: String, metadata: [Metadata](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/types/Metadata.html "org.apache.spark.sql.types.Metadata")): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Returns a new Dataset by updating an existing column with metadata.
Returns a new Dataset by updating an existing column with metadata.  

Since
    
3.3.0
  26. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#explode\[A,B\]\(inputColumn:String,outputColumn:String\)\(f:A=>IterableOnce\[B\]\)\(implicitevidence$4:reflect.runtime.universe.TypeTag\[B\]\):org.apache.spark.sql.DataFrame "Permalink") abstract  def explode[A, B](inputColumn: String, outputColumn: String)(f: (A) => IterableOnce[B])(implicit arg0: scala.reflect.api.JavaUniverse.TypeTag[B]): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
(Scala-specific) Returns a new Dataset where a single column has been expanded to zero or more rows by the provided function.
(Scala-specific) Returns a new Dataset where a single column has been expanded to zero or more rows by the provided function. This is similar to a `LATERAL VIEW` in HiveQL. All columns of the input row are implicitly joined with each value that is output by the function.
Given that this is deprecated, as an alternative, you can explode columns either using `functions.explode()`:

```
ds.select(explode(split($"words", " ")).as("word"))
```

or `flatMap()`:

```
ds.flatMap(_.words.split(" "))
```


Annotations
     @deprecated 

Deprecated
    
_(Since version 2.0.0)_ use flatMap() or select() with functions.explode() instead 

Since
    
2.0.0
  27. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#explode\[A<:Product\]\(input:org.apache.spark.sql.Column*\)\(f:org.apache.spark.sql.Row=>IterableOnce\[A\]\)\(implicitevidence$3:reflect.runtime.universe.TypeTag\[A\]\):org.apache.spark.sql.DataFrame "Permalink") abstract  def explode[A <: Product](input: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")*)(f: ([Row](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Row.html "org.apache.spark.sql.Row")) => IterableOnce[A])(implicit arg0: scala.reflect.api.JavaUniverse.TypeTag[A]): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
(Scala-specific) Returns a new Dataset where each row has been expanded to zero or more rows by the provided function.
(Scala-specific) Returns a new Dataset where each row has been expanded to zero or more rows by the provided function. This is similar to a `LATERAL VIEW` in HiveQL. The columns of the input row are implicitly joined with each row that is output by the function.
Given that this is deprecated, as an alternative, you can explode columns either using `functions.explode()` or `flatMap()`. The following example uses these alternatives to count the number of books that contain a given word:

```
case class Book(title: String, words: String)
val ds: Dataset[Book]

val allWords = ds.select($"title", explode(split($"words", " ")).as("word"))

val bookCountPerWord = allWords.groupBy("word").agg(count_distinct("title"))
```

Using `flatMap()` this can similarly be exploded as:

```
ds.flatMap(_.words.split(" "))
```


Annotations
     @deprecated 

Deprecated
    
_(Since version 2.0.0)_ use flatMap() or select() with functions.explode() instead 

Since
    
2.0.0
  28. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#agg\(expr:org.apache.spark.sql.Column,exprs:org.apache.spark.sql.Column*\):org.apache.spark.sql.DataFrame "Permalink") def agg(expr: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column"), exprs: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")*): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Aggregates on the entire Dataset without groups.
Aggregates on the entire Dataset without groups.

```
// ds.agg(...) is a shorthand for ds.groupBy().agg(...)
ds.agg(max($"age"), avg($"salary"))
ds.groupBy().agg(max($"age"), avg($"salary"))
```


Annotations
     @varargs() 

Since
    
2.0.0
  29. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#agg\(exprs:java.util.Map\[String,String\]\):org.apache.spark.sql.DataFrame "Permalink") def agg(exprs: [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#java.util.Map "java.util.Map")[String, String]): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
(Java-specific) Aggregates on the entire Dataset without groups.
(Java-specific) Aggregates on the entire Dataset without groups.

```
// ds.agg(...) is a shorthand for ds.groupBy().agg(...)
ds.agg(Map("age" -> "max", "salary" -> "avg"))
ds.groupBy().agg(Map("age" -> "max", "salary" -> "avg"))
```


Since
    
2.0.0
  30. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#agg\(exprs:Map\[String,String\]\):org.apache.spark.sql.DataFrame "Permalink") def agg(exprs: Map[String, String]): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
(Scala-specific) Aggregates on the entire Dataset without groups.
(Scala-specific) Aggregates on the entire Dataset without groups.

```
// ds.agg(...) is a shorthand for ds.groupBy().agg(...)
ds.agg(Map("age" -> "max", "salary" -> "avg"))
ds.groupBy().agg(Map("age" -> "max", "salary" -> "avg"))
```


Since
    
2.0.0
  31. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#agg\(aggExpr:\(String,String\),aggExprs:\(String,String\)*\):org.apache.spark.sql.DataFrame "Permalink") def agg(aggExpr: (String, String), aggExprs: (String, String)*): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
(Scala-specific) Aggregates on the entire Dataset without groups.
(Scala-specific) Aggregates on the entire Dataset without groups.

```
// ds.agg(...) is a shorthand for ds.groupBy().agg(...)
ds.agg("age" -> "max", "salary" -> "avg")
ds.groupBy().agg("age" -> "max", "salary" -> "avg")
```


Since
    
2.0.0
  32. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#apply\(colName:String\):org.apache.spark.sql.Column "Permalink") def apply(colName: String): [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
Selects column based on the column name and returns it as a [org.apache.spark.sql.Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column").
Selects column based on the column name and returns it as a [org.apache.spark.sql.Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column").  

Since
    
2.0.0 

Note
    
The column name can also reference to a nested column like `a.b`.
  33. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#cube\(col1:String,cols:String*\):org.apache.spark.sql.RelationalGroupedDataset "Permalink") def cube(col1: String, cols: String*): [RelationalGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/RelationalGroupedDataset.html "org.apache.spark.sql.RelationalGroupedDataset")
Create a multi-dimensional cube for the current Dataset using the specified columns, so we can run aggregation on them.
Create a multi-dimensional cube for the current Dataset using the specified columns, so we can run aggregation on them. See [RelationalGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/RelationalGroupedDataset.html "org.apache.spark.sql.RelationalGroupedDataset") for all the available aggregate functions.
This is a variant of cube that can only group by existing columns using column names (i.e. cannot construct expressions).

```
// Compute the average for all numeric columns cubed by department and group.
ds.cube("department", "group").avg()

// Compute the max age and average salary, cubed by department and gender.
ds.cube($"department", $"gender").agg(Map(
  "salary" -> "avg",
  "age" -> "max"
))
```


Annotations
     @varargs() 

Since
    
2.0.0
  34. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#drop\(col:org.apache.spark.sql.Column\):org.apache.spark.sql.DataFrame "Permalink") def drop(col: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Returns a new Dataset with column dropped.
Returns a new Dataset with column dropped.
This method can only be used to drop top level column. This version of drop accepts a [org.apache.spark.sql.Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column") rather than a name. This is a no-op if the Dataset doesn't have a column with an equivalent expression.
Note: `drop(col(colName))` has different semantic with `drop(colName)`, please refer to `Dataset#drop(colName: String)`.  

Since
    
2.0.0
  35. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#drop\(colName:String\):org.apache.spark.sql.DataFrame "Permalink") def drop(colName: String): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Returns a new Dataset with a column dropped.
Returns a new Dataset with a column dropped. This is a no-op if schema doesn't contain column name.
This method can only be used to drop top level columns. the colName string is treated literally without further interpretation.
Note: `drop(colName)` has different semantic with `drop(col(colName))`, for example: 1, multi column have the same colName:

```
val df1 = spark.range(0, 2).withColumn("key1", lit(1))
val df2 = spark.range(0, 2).withColumn("key2", lit(2))
val df3 = df1.join(df2)

df3.show
// +---+----+---+----+
// | id|key1| id|key2|
// +---+----+---+----+
// |  0|   1|  0|   2|
// |  0|   1|  1|   2|
// |  1|   1|  0|   2|
// |  1|   1|  1|   2|
// +---+----+---+----+

df3.drop("id").show()
// output: the two 'id' columns are both dropped.
// |key1|key2|
// +----+----+
// |   1|   2|
// |   1|   2|
// |   1|   2|
// |   1|   2|
// +----+----+

df3.drop(col("id")).show()
// ...AnalysisException: [AMBIGUOUS_REFERENCE] Reference `id` is ambiguous...
```

2, colName contains special characters, like dot.

```
val df = spark.range(0, 2).withColumn("a.b.c", lit(1))

df.show()
// +---+-----+
// | id|a.b.c|
// +---+-----+
// |  0|    1|
// |  1|    1|
// +---+-----+

df.drop("a.b.c").show()
// +---+
// | id|
// +---+
// |  0|
// |  1|
// +---+

df.drop(col("a.b.c")).show()
// no column match the expression 'a.b.c'
// +---+-----+
// | id|a.b.c|
// +---+-----+
// |  0|    1|
// |  1|    1|
// +---+-----+
```


Since
    
2.0.0
  36. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#groupBy\(col1:String,cols:String*\):org.apache.spark.sql.RelationalGroupedDataset "Permalink") def groupBy(col1: String, cols: String*): [RelationalGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/RelationalGroupedDataset.html "org.apache.spark.sql.RelationalGroupedDataset")
Groups the Dataset using the specified columns, so that we can run aggregation on them.
Groups the Dataset using the specified columns, so that we can run aggregation on them. See [RelationalGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/RelationalGroupedDataset.html "org.apache.spark.sql.RelationalGroupedDataset") for all the available aggregate functions.
This is a variant of groupBy that can only group by existing columns using column names (i.e. cannot construct expressions).

```
// Compute the average for all numeric columns grouped by department.
ds.groupBy("department").avg()

// Compute the max age and average salary, grouped by department and gender.
ds.groupBy($"department", $"gender").agg(Map(
  "salary" -> "avg",
  "age" -> "max"
))
```


Annotations
     @varargs() 

Since
    
2.0.0
  37. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#join\(right:org.apache.spark.sql.Dataset\[_\],joinExprs:org.apache.spark.sql.Column\):org.apache.spark.sql.DataFrame "Permalink") def join(right: [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[_], joinExprs: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Inner join with another `DataFrame`, using the given join expression.
Inner join with another `DataFrame`, using the given join expression.

```
// The following two are equivalent:
df1.join(df2, $"df1Key" === $"df2Key")
df1.join(df2).where($"df1Key" === $"df2Key")
```


Since
    
2.0.0
  38. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#join\(right:org.apache.spark.sql.Dataset\[_\],usingColumns:Array\[String\],joinType:String\):org.apache.spark.sql.DataFrame "Permalink") def join(right: [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[_], usingColumns: Array[String], joinType: String): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
(Java-specific) Equi-join with another `DataFrame` using the given columns.
(Java-specific) Equi-join with another `DataFrame` using the given columns. See the Scala-specific overload for more details.  

right
    
Right side of the join operation. 

usingColumns
    
Names of the columns to join on. This columns must exist on both sides. 

joinType
    
Type of join to perform. Default `inner`. Must be one of: `inner`, `cross`, `outer`, `full`, `fullouter`, `full_outer`, `left`, `leftouter`, `left_outer`, `right`, `rightouter`, `right_outer`, `semi`, `leftsemi`, `left_semi`, `anti`, `leftanti`, `left_anti`. 

Since
    
3.4.0
  39. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#join\(right:org.apache.spark.sql.Dataset\[_\],usingColumn:String,joinType:String\):org.apache.spark.sql.DataFrame "Permalink") def join(right: [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[_], usingColumn: String, joinType: String): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Equi-join with another `DataFrame` using the given column.
Equi-join with another `DataFrame` using the given column. A cross join with a predicate is specified as an inner join. If you would explicitly like to perform a cross join use the `crossJoin` method.
Different from other join functions, the join column will only appear once in the output, i.e. similar to SQL's `JOIN USING` syntax.  

right
    
Right side of the join operation. 

usingColumn
    
Name of the column to join on. This column must exist on both sides. 

joinType
    
Type of join to perform. Default `inner`. Must be one of: `inner`, `cross`, `outer`, `full`, `fullouter`, `full_outer`, `left`, `leftouter`, `left_outer`, `right`, `rightouter`, `right_outer`, `semi`, `leftsemi`, `left_semi`, `anti`, `leftanti`, `left_anti`. 

Since
    
3.4.0 

Note
    
If you perform a self-join using this function without aliasing the input `DataFrame`s, you will NOT be able to reference any columns after the join, since there is no way to disambiguate which side of the join you would like to reference.
  40. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#join\(right:org.apache.spark.sql.Dataset\[_\],usingColumns:Seq\[String\]\):org.apache.spark.sql.DataFrame "Permalink") def join(right: [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[_], usingColumns: Seq[String]): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
(Scala-specific) Inner equi-join with another `DataFrame` using the given columns.
(Scala-specific) Inner equi-join with another `DataFrame` using the given columns.
Different from other join functions, the join columns will only appear once in the output, i.e. similar to SQL's `JOIN USING` syntax.

```
// Joining df1 and df2 using the columns "user_id" and "user_name"
df1.join(df2, Seq("user_id", "user_name"))
```


right
    
Right side of the join operation. 

usingColumns
    
Names of the columns to join on. This columns must exist on both sides. 

Since
    
2.0.0 

Note
    
If you perform a self-join using this function without aliasing the input `DataFrame`s, you will NOT be able to reference any columns after the join, since there is no way to disambiguate which side of the join you would like to reference.
  41. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#join\(right:org.apache.spark.sql.Dataset\[_\],usingColumns:Array\[String\]\):org.apache.spark.sql.DataFrame "Permalink") def join(right: [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[_], usingColumns: Array[String]): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
(Java-specific) Inner equi-join with another `DataFrame` using the given columns.
(Java-specific) Inner equi-join with another `DataFrame` using the given columns. See the Scala-specific overload for more details.  

right
    
Right side of the join operation. 

usingColumns
    
Names of the columns to join on. This columns must exist on both sides. 

Since
    
3.4.0
  42. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#join\(right:org.apache.spark.sql.Dataset\[_\],usingColumn:String\):org.apache.spark.sql.DataFrame "Permalink") def join(right: [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[_], usingColumn: String): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Inner equi-join with another `DataFrame` using the given column.
Inner equi-join with another `DataFrame` using the given column.
Different from other join functions, the join column will only appear once in the output, i.e. similar to SQL's `JOIN USING` syntax.

```
// Joining df1 and df2 using the column "user_id"
df1.join(df2, "user_id")
```


right
    
Right side of the join operation. 

usingColumn
    
Name of the column to join on. This column must exist on both sides. 

Since
    
2.0.0 

Note
    
If you perform a self-join using this function without aliasing the input `DataFrame`s, you will NOT be able to reference any columns after the join, since there is no way to disambiguate which side of the join you would like to reference.
  43. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#melt\(ids:Array\[org.apache.spark.sql.Column\],variableColumnName:String,valueColumnName:String\):org.apache.spark.sql.DataFrame "Permalink") def melt(ids: Array[[Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")], variableColumnName: String, valueColumnName: String): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Unpivot a DataFrame from wide format to long format, optionally leaving identifier columns set.
Unpivot a DataFrame from wide format to long format, optionally leaving identifier columns set. This is the reverse to `groupBy(...).pivot(...).agg(...)`, except for the aggregation, which cannot be reversed. This is an alias for `unpivot`.  

ids
    
Id columns 

variableColumnName
    
Name of the variable column 

valueColumnName
    
Name of the value column 

Since
    
3.4.0 

See also
    
`org.apache.spark.sql.Dataset.unpivot(Array, Array, String, String)` This is equivalent to calling `Dataset#unpivot(Array, Array, String, String)` where `values` is set to all non-id columns that exist in the DataFrame.
  44. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#melt\(ids:Array\[org.apache.spark.sql.Column\],values:Array\[org.apache.spark.sql.Column\],variableColumnName:String,valueColumnName:String\):org.apache.spark.sql.DataFrame "Permalink") def melt(ids: Array[[Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")], values: Array[[Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")], variableColumnName: String, valueColumnName: String): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Unpivot a DataFrame from wide format to long format, optionally leaving identifier columns set.
Unpivot a DataFrame from wide format to long format, optionally leaving identifier columns set. This is the reverse to `groupBy(...).pivot(...).agg(...)`, except for the aggregation, which cannot be reversed. This is an alias for `unpivot`.  

ids
    
Id columns 

values
    
Value columns to unpivot 

variableColumnName
    
Name of the variable column 

valueColumnName
    
Name of the value column 

Since
    
3.4.0 

See also
    
`org.apache.spark.sql.Dataset.unpivot(Array, Array, String, String)`
  45. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#rollup\(col1:String,cols:String*\):org.apache.spark.sql.RelationalGroupedDataset "Permalink") def rollup(col1: String, cols: String*): [RelationalGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/RelationalGroupedDataset.html "org.apache.spark.sql.RelationalGroupedDataset")
Create a multi-dimensional rollup for the current Dataset using the specified columns, so we can run aggregation on them.
Create a multi-dimensional rollup for the current Dataset using the specified columns, so we can run aggregation on them. See [RelationalGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/RelationalGroupedDataset.html "org.apache.spark.sql.RelationalGroupedDataset") for all the available aggregate functions.
This is a variant of rollup that can only group by existing columns using column names (i.e. cannot construct expressions).

```
// Compute the average for all numeric columns rolled up by department and group.
ds.rollup("department", "group").avg()

// Compute the max age and average salary, rolled up by department and gender.
ds.rollup($"department", $"gender").agg(Map(
  "salary" -> "avg",
  "age" -> "max"
))
```


Annotations
     @varargs() 

Since
    
2.0.0
  46. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#select\(col:String,cols:String*\):org.apache.spark.sql.DataFrame "Permalink") def select(col: String, cols: String*): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Selects a set of columns.
Selects a set of columns. This is a variant of `select` that can only select existing columns using column names (i.e. cannot construct expressions).

```
// The following two are equivalent:
ds.select("colA", "colB")
ds.select($"colA", $"colB")
```


Annotations
     @varargs() 

Since
    
2.0.0
  47. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#selectExpr\(exprs:String*\):org.apache.spark.sql.DataFrame "Permalink") def selectExpr(exprs: String*): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Selects a set of SQL expressions.
Selects a set of SQL expressions. This is a variant of `select` that accepts SQL expressions.

```
// The following are equivalent:
ds.selectExpr("colA", "colB as newName", "abs(colC)")
ds.select(expr("colA"), expr("colB as newName"), expr("abs(colC)"))
```


Annotations
     @varargs() 

Since
    
2.0.0
  48. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#withColumn\(colName:String,col:org.apache.spark.sql.Column\):org.apache.spark.sql.DataFrame "Permalink") def withColumn(colName: String, col: [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Returns a new Dataset by adding a column or replacing the existing column that has the same name.
Returns a new Dataset by adding a column or replacing the existing column that has the same name.
`column`'s expression must only refer to attributes supplied by this Dataset. It is an error to add a column that refers to some other Dataset.  

Since
    
2.0.0 

Note
    
this method introduces a projection internally. Therefore, calling it multiple times, for instance, via loops in order to add multiple columns can generate big plans which can cause performance issues and even `StackOverflowException`. To avoid this, use `select` with the multiple columns at once.
  49. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#withColumnRenamed\(existingName:String,newName:String\):org.apache.spark.sql.DataFrame "Permalink") def withColumnRenamed(existingName: String, newName: String): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
Returns a new Dataset with a column renamed.
Returns a new Dataset with a column renamed. This is a no-op if schema doesn't contain existingName.  

Since
    
2.0.0
  50. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#withColumns\(colsMap:java.util.Map\[String,org.apache.spark.sql.Column\]\):org.apache.spark.sql.DataFrame "Permalink") def withColumns(colsMap: [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#java.util.Map "java.util.Map")[String, [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")]): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
(Java-specific) Returns a new Dataset by adding columns or replacing the existing columns that has the same names.
(Java-specific) Returns a new Dataset by adding columns or replacing the existing columns that has the same names.
`colsMap` is a map of column name and column, the column must only refer to attribute supplied by this Dataset. It is an error to add columns that refers to some other Dataset.  

Since
    
3.3.0
  51. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#withColumns\(colsMap:Map\[String,org.apache.spark.sql.Column\]\):org.apache.spark.sql.DataFrame "Permalink") def withColumns(colsMap: Map[String, [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")]): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
(Scala-specific) Returns a new Dataset by adding columns or replacing the existing columns that has the same names.
(Scala-specific) Returns a new Dataset by adding columns or replacing the existing columns that has the same names.
`colsMap` is a map of column name and column, the column must only refer to attributes supplied by this Dataset. It is an error to add columns that refers to some other Dataset.  

Since
    
3.3.0
  52. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#withColumnsRenamed\(colsMap:java.util.Map\[String,String\]\):org.apache.spark.sql.DataFrame "Permalink") def withColumnsRenamed(colsMap: [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html#java.util.Map "java.util.Map")[String, String]): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
(Java-specific) Returns a new Dataset with a columns renamed.
(Java-specific) Returns a new Dataset with a columns renamed. This is a no-op if schema doesn't contain existingName.
`colsMap` is a map of existing column name and new column name.  

Since
    
3.4.0
  53. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#withColumnsRenamed\(colsMap:Map\[String,String\]\):org.apache.spark.sql.DataFrame "Permalink") def withColumnsRenamed(colsMap: Map[String, String]): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\])
(Scala-specific) Returns a new Dataset with a columns renamed.
(Scala-specific) Returns a new Dataset with a columns renamed. This is a no-op if schema doesn't contain existingName.
`colsMap` is a map of existing column name and new column name.  

Annotations
     @throws("") 

Since
    
3.4.0 

Exceptions thrown
    
[`org.apache.spark.sql.AnalysisException`](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/AnalysisException.html "org.apache.spark.sql.AnalysisException") if there are duplicate names in resulting projection


### Ungrouped
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#checkpoint\(eager:Boolean,reliableCheckpoint:Boolean,storageLevel:Option\[org.apache.spark.storage.StorageLevel\]\):org.apache.spark.sql.Dataset\[T\] "Permalink") abstract  def checkpoint(eager: Boolean, reliableCheckpoint: Boolean, storageLevel: Option[[StorageLevel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/StorageLevel.html "org.apache.spark.storage.StorageLevel")]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]
Returns a checkpointed version of this Dataset.
Returns a checkpointed version of this Dataset.  

eager
    
Whether to checkpoint this dataframe immediately 

reliableCheckpoint
    
Whether to create a reliable checkpoint saved to files inside the checkpoint directory. If false creates a local checkpoint using the caching subsystem 

storageLevel
    
Option. If defined, StorageLevel with which to checkpoint the data. Only with reliableCheckpoint = false. 

Attributes
    protected 
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#createTempView\(viewName:String,replace:Boolean,global:Boolean\):Unit "Permalink") abstract  def createTempView(viewName: String, replace: Boolean, global: Boolean): Unit 

Attributes
    protected 
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#encoder:org.apache.spark.sql.Encoder\[T\] "Permalink") abstract  val encoder: [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder")[T]
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#queryExecution:org.apache.spark.sql.execution.QueryExecution "Permalink") abstract  def queryExecution: QueryExecution 

Annotations
     @ClassicOnly() @DeveloperApi() @Unstable()
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#repartitionByExpression\(numPartitions:Option\[Int\],partitionExprs:Seq\[org.apache.spark.sql.Column\]\):org.apache.spark.sql.Dataset\[T\] "Permalink") abstract  def repartitionByExpression(numPartitions: Option[Int], partitionExprs: Seq[[Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T] 

Attributes
    protected 
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#repartitionByRange\(numPartitions:Option\[Int\],partitionExprs:Seq\[org.apache.spark.sql.Column\]\):org.apache.spark.sql.Dataset\[T\] "Permalink") abstract  def repartitionByRange(numPartitions: Option[Int], partitionExprs: Seq[[Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T] 

Attributes
    protected 
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#sameSemantics\(other:org.apache.spark.sql.Dataset\[T\]\):Boolean "Permalink") abstract  def sameSemantics(other: [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T]): Boolean
Returns `true` when the logical query plans inside both [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")s are equal and therefore return same results.
Returns `true` when the logical query plans inside both [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")s are equal and therefore return same results.  

Annotations
     @DeveloperApi() 

Since
    
3.1.0 

Note
    
The equality comparison here is simplified by tolerating the cosmetic differences such as attribute names.
, 
This API can compare both [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")s very fast but can still return `false` on the [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") that return the same results, for instance, from different plans. Such false negative semantic can be useful when caching as an example.
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#selectUntyped\(columns:org.apache.spark.sql.TypedColumn\[_,_\]*\):org.apache.spark.sql.Dataset\[_\] "Permalink") abstract  def selectUntyped(columns: [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn")[_, _]*): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[_]
Internal helper function for building typed selects that return tuples.
Internal helper function for building typed selects that return tuples. For simplicity and code reuse, we do this without the help of the type system and then use helper functions that cast appropriately for the user facing interface.  

Attributes
    protected 
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#semanticHash\(\):Int "Permalink") abstract  def semanticHash(): Int
Returns a `hashCode` of the logical query plan against this [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset").
Returns a `hashCode` of the logical query plan against this [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset").  

Annotations
     @DeveloperApi() 

Since
    
3.1.0 

Note
    
Unlike the standard `hashCode`, the hash is calculated against the query plan simplified by tolerating the cosmetic differences such as attribute names.
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#sortInternal\(global:Boolean,sortExprs:Seq\[org.apache.spark.sql.Column\]\):org.apache.spark.sql.Dataset\[T\] "Permalink") abstract  def sortInternal(global: Boolean, sortExprs: Seq[[Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")]): [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[T] 

Attributes
    protected 
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#sparkSession:org.apache.spark.sql.SparkSession "Permalink") abstract  val sparkSession: [SparkSession](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/SparkSession.html "org.apache.spark.sql.SparkSession")
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#toJSON:org.apache.spark.sql.Dataset\[String\] "Permalink") abstract  def toJSON: [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[String]
Returns the content of the Dataset as a Dataset of JSON strings.
Returns the content of the Dataset as a Dataset of JSON strings.  

Since
    
2.0.0
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#withColumnsRenamed\(colNames:Seq\[String\],newColNames:Seq\[String\]\):org.apache.spark.sql.DataFrame "Permalink") abstract  def withColumnsRenamed(colNames: Seq[String], newColNames: Seq[String]): [DataFrame](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\]) 

Attributes
    protected 
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#!=\(x$1:Any\):Boolean "Permalink") final  def !=(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html###:Int "Permalink") final  def ##: Int 

Definition Classes
    AnyRef → Any
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#==\(x$1:Any\):Boolean "Permalink") final  def ==(arg0: Any): Boolean 

Definition Classes
    AnyRef → Any
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#asInstanceOf\[T0\]:T0 "Permalink") final  def asInstanceOf[T0]: T0 

Definition Classes
    Any
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#clone\(\):Object "Permalink") def clone(): AnyRef 

Attributes
    protected[lang]  

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.CloneNotSupportedException]) @IntrinsicCandidate() @native()
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#eq\(x$1:AnyRef\):Boolean "Permalink") final  def eq(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#equals\(x$1:Object\):Boolean "Permalink") def equals(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef → Any
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#getClass\(\):Class\[_\] "Permalink") final  def getClass(): [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html#java.lang.Class "java.lang.Class")[_ <: AnyRef] 

Definition Classes
    AnyRef → Any 

Annotations
     @IntrinsicCandidate() @native()
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#hashCode\(\):Int "Permalink") def hashCode(): Int 

Definition Classes
    AnyRef → Any 

Annotations
     @IntrinsicCandidate() @native()
  23. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#isInstanceOf\[T0\]:Boolean "Permalink") final  def isInstanceOf[T0]: Boolean 

Definition Classes
    Any
  24. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#ne\(x$1:AnyRef\):Boolean "Permalink") final  def ne(arg0: AnyRef): Boolean 

Definition Classes
    AnyRef
  25. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#notify\(\):Unit "Permalink") final  def notify(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  26. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#notifyAll\(\):Unit "Permalink") final  def notifyAll(): Unit 

Definition Classes
    AnyRef 

Annotations
     @IntrinsicCandidate() @native()
  27. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#synchronized\[T0\]\(x$1:=>T0\):T0 "Permalink") final  def synchronized[T0](arg0: => T0): T0 

Definition Classes
    AnyRef
  28. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#toString\(\):String "Permalink") def toString(): [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#java.lang.String "java.lang.String") 

Definition Classes
    AnyRef → Any
  29. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#wait\(x$1:Long,x$2:Int\):Unit "Permalink") final  def wait(arg0: Long, arg1: Int): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  30. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#wait\(x$1:Long\):Unit "Permalink") final  def wait(arg0: Long): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException]) @native()
  31. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#wait\(\):Unit "Permalink") final  def wait(): Unit 

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.InterruptedException])
  32. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#finalize\(\):Unit "Permalink") def finalize(): Unit 

Attributes
    protected[lang]  

Definition Classes
    AnyRef 

Annotations
     @throws(classOf[java.lang.Throwable]) @Deprecated 

Deprecated
    
_(Since version 9)_


