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
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/index.html "Permalink") package [api](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/api/index.html) 

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/broadcast/index.html "Permalink") package [broadcast](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/broadcast/index.html "Spark's broadcast variables, used to broadcast immutable datasets to all nodes.")
Spark's broadcast variables, used to broadcast immutable datasets to all nodes.
Spark's broadcast variables, used to broadcast immutable datasets to all nodes.  

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html "Permalink") package [graphx](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html "ALPHA COMPONENT GraphX is a graph processing framework built on top of Spark.")
ALPHA COMPONENT GraphX is a graph processing framework built on top of Spark.
ALPHA COMPONENT GraphX is a graph processing framework built on top of Spark.  

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/input/index.html "Permalink") package [input](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/input/index.html) 

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/index.html "Permalink") package [io](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/index.html "IO codecs used for compression.")
IO codecs used for compression.
IO codecs used for compression. See [org.apache.spark.io.CompressionCodec](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/io/CompressionCodec.html "org.apache.spark.io.CompressionCodec").  

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/launcher/index.html "Permalink") package [launcher](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/launcher/index.html) 

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/mapred/index.html "Permalink") package [mapred](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/mapred/index.html) 

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/metrics/index.html "Permalink") package [metrics](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/metrics/index.html) 

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/index.html "Permalink") package [ml](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/index.html "DataFrame-based machine learning APIs to let users quickly assemble and configure practical machine learning pipelines.")
DataFrame-based machine learning APIs to let users quickly assemble and configure practical machine learning pipelines.
DataFrame-based machine learning APIs to let users quickly assemble and configure practical machine learning pipelines.  

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/mllib/index.html "Permalink") package [mllib](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/mllib/index.html "RDD-based machine learning APIs \(in maintenance mode\).")
RDD-based machine learning APIs (in maintenance mode).
RDD-based machine learning APIs (in maintenance mode).
The `spark.mllib` package is in maintenance mode as of the Spark 2.0.0 release to encourage migration to the DataFrame-based APIs under the [org.apache.spark.ml](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/index.html "org.apache.spark.ml") package. While in maintenance mode,
    * no new features in the RDD-based `spark.mllib` package will be accepted, unless they block implementing new features in the DataFrame-based `spark.ml` package;
    * bug fixes in the RDD-based APIs will still be accepted.
The developers will continue adding more features to the DataFrame-based APIs in the 2.x series to reach feature parity with the RDD-based APIs. And once we reach feature parity, this package will be deprecated.  

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark") 

See also
    
[SPARK-4591](https://issues.apache.org/jira/browse/SPARK-4591) to track the progress of feature parity
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/partial/index.html "Permalink") package [partial](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/partial/index.html "Support for approximate results.")
Support for approximate results.
Support for approximate results. This provides convenient api and also implementation for approximate calculation.  

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark") 

See also
    
[org.apache.spark.rdd.RDD.countApprox](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html#countApprox\(timeout:Long,confidence:Double\):org.apache.spark.partial.PartialResult\[org.apache.spark.partial.BoundedDouble\])
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/paths/index.html "Permalink") package [paths](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/paths/index.html) 

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/index.html "Permalink") package [rdd](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/index.html "Provides several RDD implementations.")
Provides several RDD implementations.
Provides several RDD implementations. See [org.apache.spark.rdd.RDD](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/rdd/RDD.html "org.apache.spark.rdd.RDD").  

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/resource/index.html "Permalink") package [resource](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/resource/index.html) 

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/index.html "Permalink") package [scheduler](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/index.html "Spark's scheduling components.")
Spark's scheduling components.
Spark's scheduling components. This includes the `org.apache.spark.scheduler.DAGScheduler` and lower level `org.apache.spark.scheduler.TaskScheduler`.  

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/security/index.html "Permalink") package [security](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/security/index.html) 

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/index.html "Permalink") package [serializer](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/index.html "Pluggable serializers for RDD and shuffle data.")
Pluggable serializers for RDD and shuffle data.
Pluggable serializers for RDD and shuffle data.  

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark") 

See also
    
[org.apache.spark.serializer.Serializer](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/serializer/Serializer.html "org.apache.spark.serializer.Serializer")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/shuffle/index.html "Permalink") package [shuffle](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/shuffle/index.html) 

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html "Permalink") package sql
Allows the execution of relational queries, including those expressed in SQL using Spark.
Allows the execution of relational queries, including those expressed in SQL using Spark.  

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/api/index.html "Permalink") package [api](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/api/index.html "Contains API classes that are specific to a single language \(i.e.")
Contains API classes that are specific to a single language (i.e.
Contains API classes that are specific to a single language (i.e. Java). 
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/index.html "Permalink") package [catalog](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/index.html)
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalyst/index.html "Permalink") package [catalyst](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalyst/index.html)
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/columnar/index.html "Permalink") package [columnar](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/columnar/index.html)
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/connector/index.html "Permalink") package [connector](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/connector/index.html)
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/expressions/index.html "Permalink") package [expressions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/expressions/index.html)
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/jdbc/index.html "Permalink") package [jdbc](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/jdbc/index.html)
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/protobuf/index.html "Permalink") package [protobuf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/protobuf/index.html)
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/sources/index.html "Permalink") package [sources](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/sources/index.html "A set of APIs for adding data sources to Spark SQL.")
A set of APIs for adding data sources to Spark SQL.
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/index.html "Permalink") package [streaming](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/index.html)
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/types/index.html "Permalink") package [types](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/types/index.html "Contains a type system for attributes produced by relations, including complex types like structs, arrays and maps.")
Contains a type system for attributes produced by relations, including complex types like structs, arrays and maps.
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/util/index.html "Permalink") package [util](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/util/index.html)
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/vectorized/index.html "Permalink") package [vectorized](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/vectorized/index.html)
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
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/status/index.html "Permalink") package [status](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/status/index.html) 

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/index.html "Permalink") package [storage](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/storage/index.html) 

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/index.html "Permalink") package [streaming](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/index.html "Spark Streaming functionality.")
Spark Streaming functionality.
Spark Streaming functionality. [org.apache.spark.streaming.StreamingContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/StreamingContext.html "org.apache.spark.streaming.StreamingContext") serves as the main entry point to Spark Streaming, while [org.apache.spark.streaming.dstream.DStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/DStream.html "org.apache.spark.streaming.dstream.DStream") is the data type representing a continuous sequence of RDDs, representing a continuous stream of data.
In addition, [org.apache.spark.streaming.dstream.PairDStreamFunctions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/dstream/PairDStreamFunctions.html "org.apache.spark.streaming.dstream.PairDStreamFunctions") contains operations available only on DStreams of key-value pairs, such as `groupByKey` and `reduceByKey`. These operations are automatically available on any DStream of the right type (e.g. DStream[(Int, Int)] through implicit conversions.
For the Java API of Spark Streaming, take a look at the [org.apache.spark.streaming.api.java.JavaStreamingContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaStreamingContext.html "org.apache.spark.streaming.api.java.JavaStreamingContext") which serves as the entry point, and the [org.apache.spark.streaming.api.java.JavaDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaDStream.html "org.apache.spark.streaming.api.java.JavaDStream") and the [org.apache.spark.streaming.api.java.JavaPairDStream](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/api/java/JavaPairDStream.html "org.apache.spark.streaming.api.java.JavaPairDStream") which have the DStream functionality.  

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ui/index.html "Permalink") package [ui](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ui/index.html) 

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/unsafe/index.html "Permalink") package [unsafe](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/unsafe/index.html) 

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/index.html "Permalink") package [util](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/util/index.html "Spark utilities.")
Spark utilities.
Spark utilities.  

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")


p
[org](https://spark.apache.org/docs/latest/api/scala/org/index.html "org").[apache](https://spark.apache.org/docs/latest/api/scala/org/apache/index.html "org.apache").[spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
# sql[ __](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html "Permalink")
####  package sql
Allows the execution of relational queries, including those expressed in SQL using Spark.  

Source
    [package.scala](https://github.com/apache/spark/tree/v4.1.2/sql/api/src/main/scala/org/apache/spark/sql/package.scala)
Linear Supertypes
AnyRef, Any
__ __
Ordering
  1. Alphabetic
  2. By Inheritance


Inherited  

  1. sql
  2. AnyRef
  3. Any


  1. Hide All
  2. Show All


Visibility
  1. Public
  2. Protected


### Package Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/api/index.html "Permalink") package [api](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/api/index.html "Contains API classes that are specific to a single language \(i.e.")
Contains API classes that are specific to a single language (i.e.
Contains API classes that are specific to a single language (i.e. Java). 
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/index.html "Permalink") package [catalog](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalog/index.html)
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalyst/index.html "Permalink") package [catalyst](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/catalyst/index.html)
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/columnar/index.html "Permalink") package [columnar](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/columnar/index.html)
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/connector/index.html "Permalink") package [connector](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/connector/index.html)
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/expressions/index.html "Permalink") package [expressions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/expressions/index.html)
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/jdbc/index.html "Permalink") package [jdbc](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/jdbc/index.html)
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/protobuf/index.html "Permalink") package [protobuf](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/protobuf/index.html)
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/sources/index.html "Permalink") package [sources](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/sources/index.html "A set of APIs for adding data sources to Spark SQL.")
A set of APIs for adding data sources to Spark SQL.
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/index.html "Permalink") package [streaming](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/streaming/index.html)
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/types/index.html "Permalink") package [types](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/types/index.html "Contains a type system for attributes produced by relations, including complex types like structs, arrays and maps.")
Contains a type system for attributes produced by relations, including complex types like structs, arrays and maps.
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/util/index.html "Permalink") package [util](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/util/index.html)
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/vectorized/index.html "Permalink") package [vectorized](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/vectorized/index.html)


### Type Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/AnalysisException.html "Permalink") class [AnalysisException](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/AnalysisException.html "Thrown when a query fails to analyze, usually because the query itself is invalid.") extends Exception with [SparkThrowable](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkThrowable.html "org.apache.spark.SparkThrowable") with Serializable with WithOrigin
Thrown when a query fails to analyze, usually because the query itself is invalid.
Thrown when a query fails to analyze, usually because the query itself is invalid.  

Annotations
     @Stable() 

Since
    
1.3.0
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "Permalink") class [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "A column that will be computed based on the data in a DataFrame.") extends Logging with TableValuedFunctionArgument
A column that will be computed based on the data in a `DataFrame`.
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

Since
    
1.3.0
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/ColumnName.html "Permalink") class [ColumnName](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/ColumnName.html "A convenient class used for constructing schema.") extends [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
A convenient class used for constructing schema.
A convenient class used for constructing schema.  

Annotations
     @Stable() 

Since
    
1.3.0
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/CreateTableWriter.html "Permalink") trait [CreateTableWriter](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/CreateTableWriter.html "Trait to restrict calls to create and replace operations.")[T] extends [WriteConfigMethods](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/WriteConfigMethods.html "org.apache.spark.sql.WriteConfigMethods")[[CreateTableWriter](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/CreateTableWriter.html "org.apache.spark.sql.CreateTableWriter")[T]]
Trait to restrict calls to create and replace operations.
Trait to restrict calls to create and replace operations.  

Since
    
3.0.0
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\] "Permalink") type DataFrame = [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[[Row](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Row.html "org.apache.spark.sql.Row")]
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/DataFrameNaFunctions.html "Permalink") abstract  class [DataFrameNaFunctions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/DataFrameNaFunctions.html "Functionality for working with missing data in DataFrames.") extends AnyRef
Functionality for working with missing data in `DataFrame`s.
Functionality for working with missing data in `DataFrame`s.  

Annotations
     @Stable() 

Since
    
1.3.1
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/DataFrameReader.html "Permalink") abstract  class [DataFrameReader](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/DataFrameReader.html "Interface used to load a Dataset from external storage systems \(e.g.") extends AnyRef
Interface used to load a [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") from external storage systems (e.g.
Interface used to load a [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") from external storage systems (e.g. file systems, key-value stores, etc). Use `SparkSession.read` to access this.  

Annotations
     @Stable() 

Since
    
1.4.0
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/DataFrameStatFunctions.html "Permalink") abstract  class [DataFrameStatFunctions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/DataFrameStatFunctions.html "Statistic functions for DataFrames.") extends AnyRef
Statistic functions for `DataFrame`s.
Statistic functions for `DataFrame`s.  

Annotations
     @Stable() 

Since
    
1.4.0
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/DataFrameWriter.html "Permalink") abstract  class [DataFrameWriter](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/DataFrameWriter.html "Interface used to write a org.apache.spark.sql.Dataset to external storage systems \(e.g.")[T] extends AnyRef
Interface used to write a [org.apache.spark.sql.Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") to external storage systems (e.g.
Interface used to write a [org.apache.spark.sql.Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") to external storage systems (e.g. file systems, key-value stores, etc). Use `Dataset.write` to access this.  

Annotations
     @Stable() 

Since
    
1.4.0
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/DataFrameWriterV2.html "Permalink") abstract  class [DataFrameWriterV2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/DataFrameWriterV2.html "Interface used to write a org.apache.spark.sql.Dataset to external storage using the v2 API.")[T] extends [CreateTableWriter](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/CreateTableWriter.html "org.apache.spark.sql.CreateTableWriter")[T]
Interface used to write a [org.apache.spark.sql.Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") to external storage using the v2 API.
Interface used to write a [org.apache.spark.sql.Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") to external storage using the v2 API.  

Annotations
     @Experimental() 

Since
    
3.0.0
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "Permalink") abstract  class [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "A Dataset is a strongly typed collection of domain-specific objects that can be transformed in parallel using functional or relational operations.")[T] extends Serializable
A Dataset is a strongly typed collection of domain-specific objects that can be transformed in parallel using functional or relational operations.
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

Since
    
1.6.0
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/DatasetHolder.html "Permalink") abstract  class [DatasetHolder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/DatasetHolder.html "A container for a org.apache.spark.sql.Dataset, used for implicit conversions in Scala.")[T] extends AnyRef
A container for a [org.apache.spark.sql.Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset"), used for implicit conversions in Scala.
A container for a [org.apache.spark.sql.Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset"), used for implicit conversions in Scala.
To use this, import implicit conversions in SQL:

```
val spark: SparkSession = ...
import spark.implicits._
```


Annotations
     @Stable() 

Since
    
1.6.0
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "Permalink") trait [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "Used to convert a JVM object of type T to and from the internal Spark SQL representation.")[T] extends Serializable
Used to convert a JVM object of type `T` to and from the internal Spark SQL representation.
Used to convert a JVM object of type `T` to and from the internal Spark SQL representation.
#### Scala
Encoders are generally created automatically through implicits from a `SparkSession`, or can be explicitly created by calling static methods on [Encoders](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoders$.html "org.apache.spark.sql.Encoders").

```
import spark.implicits._

val ds = Seq(1, 2, 3).toDS() // implicitly provided (spark.implicits.newIntEncoder)
```

#### Java
Encoders are specified by calling static methods on [Encoders](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoders$.html "org.apache.spark.sql.Encoders").

```
List<String> data = Arrays.asList("abc", "abc", "xyz");
Dataset<String> ds = context.createDataset(data, Encoders.STRING());
```

Encoders can be composed into tuples:

```
Encoder<Tuple2<Integer, String>> encoder2 = Encoders.tuple(Encoders.INT(), Encoders.STRING());
List<Tuple2<Integer, String>> data2 = Arrays.asList(new scala.Tuple2(1, "a");
Dataset<Tuple2<Integer, String>> ds2 = context.createDataset(data2, encoder2);
```

Or constructed from Java Beans:

```
Encoders.bean(MyClass.class);
```

#### Implementation
     * Encoders should be thread-safe.  

Annotations
     @implicitNotFound() 

Since
    
1.6.0
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/EncoderImplicits.html "Permalink") trait [EncoderImplicits](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/EncoderImplicits.html "EncoderImplicits used to implicitly generate SQL Encoders.") extends [LowPrioritySQLImplicits](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/LowPrioritySQLImplicits.html "org.apache.spark.sql.LowPrioritySQLImplicits") with Serializable
EncoderImplicits used to implicitly generate SQL Encoders.
EncoderImplicits used to implicitly generate SQL Encoders. Note that these functions don't rely on or expose `SparkSession`. 
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/ExperimentalMethods.html "Permalink") class [ExperimentalMethods](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/ExperimentalMethods.html ":: Experimental :: Holder for experimental methods for the bravest.") extends AnyRef
Holder for experimental methods for the bravest.
Holder for experimental methods for the bravest. We make NO guarantee about the stability regarding binary compatibility and source compatibility of methods here.

```
spark.experimental.extraStrategies += ...
```


Annotations
     @Experimental() @Unstable() 

Since
    
1.3.0
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/ExtendedExplainGenerator.html "Permalink") trait [ExtendedExplainGenerator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/ExtendedExplainGenerator.html "A trait for a session extension to implement that provides addition explain plan information.") extends AnyRef
A trait for a session extension to implement that provides addition explain plan information.
A trait for a session extension to implement that provides addition explain plan information.  

Annotations
     @DeveloperApi() @Since("4.0.0")
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/ForeachWriter.html "Permalink") abstract  class [ForeachWriter](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/ForeachWriter.html "The abstract class for writing custom logic to process data generated by a query.")[T] extends Serializable
The abstract class for writing custom logic to process data generated by a query.
The abstract class for writing custom logic to process data generated by a query. This is often used to write the output of a streaming query to arbitrary storage systems. Any implementation of this base class will be used by Spark in the following way.
     * A single instance of this class is responsible of all the data generated by a single task in a query. In other words, one instance is responsible for processing one partition of the data generated in a distributed manner.
     * Any implementation of this class must be serializable because each task will get a fresh serialized-deserialized copy of the provided object. Hence, it is strongly recommended that any initialization for writing data (e.g. opening a connection or starting a transaction) is done after the `open(...)` method has been called, which signifies that the task is ready to generate data.
     * The lifecycle of the methods are as follows.

```
 For each partition with `partitionId`: For each batch/epoch of streaming data (if its
streaming query) with `epochId`: Method `open(partitionId, epochId)` is called. If `open`
returns true: For each row in the partition and batch/epoch, method `process(row)` is called.
Method `close(errorOrNull)` is called with error (if any) seen while processing rows. 

```

Important points to note:
     * Spark doesn't guarantee same output for (partitionId, epochId), so deduplication cannot be achieved with (partitionId, epochId). e.g. source provides different number of partitions for some reason, Spark optimization changes number of partitions, etc. Refer SPARK-28650 for more details. If you need deduplication on output, try out `foreachBatch` instead.
     * The `close()` method will be called if `open()` method returns successfully (irrespective of the return value), except if the JVM crashes in the middle.
Scala example:

```
datasetOfString.writeStream.foreach(new ForeachWriter[String] {

  def open(partitionId: Long, version: Long): Boolean = {
    // open connection
  }

  def process(record: String) = {
    // write string to connection
  }

  def close(errorOrNull: Throwable): Unit = {
    // close the connection
  }
})
```

Java example:

```
datasetOfString.writeStream().foreach(new ForeachWriter<String>() {

  @Override
  public boolean open(long partitionId, long version) {
    // open connection
  }

  @Override
  public void process(String value) {
    // write string to connection
  }

  @Override
  public void close(Throwable errorOrNull) {
    // close the connection
  }
});
```


Since
    
2.0.0
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html "Permalink") abstract  class [KeyValueGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html "A Dataset has been logically grouped by a user specified grouping key.")[K, V] extends Serializable
A [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") has been logically grouped by a user specified grouping key.
A [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") has been logically grouped by a user specified grouping key. Users should not construct a [KeyValueGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html "org.apache.spark.sql.KeyValueGroupedDataset") directly, but should instead call `groupByKey` on an existing [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset").  

Since
    
2.0.0
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/LowPrioritySQLImplicits.html "Permalink") trait [LowPrioritySQLImplicits](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/LowPrioritySQLImplicits.html "Lower priority implicit methods for converting Scala objects into org.apache.spark.sql.Datasets.") extends AnyRef
Lower priority implicit methods for converting Scala objects into [org.apache.spark.sql.Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")s.
Lower priority implicit methods for converting Scala objects into [org.apache.spark.sql.Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")s. Conflicting implicits are placed here to disambiguate resolution.
Reasons for including specific implicits: newProductEncoder - to disambiguate for `List`s which are both `Seq` and `Product`
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/MergeIntoWriter.html "Permalink") abstract  class [MergeIntoWriter](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/MergeIntoWriter.html "MergeIntoWriter provides methods to define and execute merge actions based on specified conditions.")[T] extends AnyRef
`MergeIntoWriter` provides methods to define and execute merge actions based on specified conditions.
`MergeIntoWriter` provides methods to define and execute merge actions based on specified conditions.
Please note that schema evolution is disabled by default.  

T
    
the type of data in the Dataset. 

Annotations
     @Experimental() 

Since
    
4.0.0
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Observation.html "Permalink") class [Observation](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Observation.html "Helper class to simplify usage of Dataset.observe\(String, Column, Column*\):") extends AnyRef
Helper class to simplify usage of `Dataset.observe(String, Column, Column*)`:
Helper class to simplify usage of `Dataset.observe(String, Column, Column*)`:

```
// Observe row count (rows) and highest id (maxid) in the Dataset while writing it
val observation = Observation("my metrics")
val observed_ds = ds.observe(observation, count(lit(1)).as("rows"), max($"id").as("maxid"))
observed_ds.write.parquet("ds.parquet")
val metrics = observation.get
```

This collects the metrics while the first action is executed on the observed dataset. Subsequent actions do not modify the metrics returned by [get](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Observation.html#get:Map\[String,Any\]). Retrieval of the metric via [get](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Observation.html#get:Map\[String,Any\]) blocks until the first action has finished and metrics become available.
This class does not support streaming datasets.  

Since
    
3.3.0
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/RelationalGroupedDataset.html "Permalink") abstract  class [RelationalGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/RelationalGroupedDataset.html "A set of methods for aggregations on a DataFrame, created by groupBy, cube or rollup \(and also pivot\).") extends AnyRef
A set of methods for aggregations on a `DataFrame`, created by [groupBy](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#groupBy\(col1:String,cols:String*\):org.apache.spark.sql.RelationalGroupedDataset), [cube](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#cube\(col1:String,cols:String*\):org.apache.spark.sql.RelationalGroupedDataset) or [rollup](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#rollup\(col1:String,cols:String*\):org.apache.spark.sql.RelationalGroupedDataset) (and also `pivot`).
A set of methods for aggregations on a `DataFrame`, created by [groupBy](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#groupBy\(col1:String,cols:String*\):org.apache.spark.sql.RelationalGroupedDataset), [cube](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#cube\(col1:String,cols:String*\):org.apache.spark.sql.RelationalGroupedDataset) or [rollup](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#rollup\(col1:String,cols:String*\):org.apache.spark.sql.RelationalGroupedDataset) (and also `pivot`).
The main method is the `agg` function, which has multiple variants. This class also contains some first-order statistics such as `mean`, `sum` for convenience.  

Annotations
     @Stable() 

Since
    
2.0.0 

Note
    
This class was named `GroupedData` in Spark 1.x.
  23. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Row.html "Permalink") trait [Row](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Row.html "Represents one row of output from a relational operator.") extends Serializable
Represents one row of output from a relational operator.
Represents one row of output from a relational operator. Allows both generic access by ordinal, which will incur boxing overhead for primitives, as well as native primitive access.
It is invalid to use the native primitive interface to retrieve a value that is null, instead a user must check `isNullAt` before attempting to retrieve a value that might be null.
To create a new Row, use `RowFactory.create()` in Java or `Row.apply()` in Scala.
A [Row](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Row.html "org.apache.spark.sql.Row") object can be constructed by providing field values. Example:

```
import org.apache.spark.sql._

// Create a Row from values.
Row(value1, value2, value3, ...)
// Create a Row from a Seq of values.
Row.fromSeq(Seq(value1, value2, ...))
```

A value of a row can be accessed through both generic access by ordinal, which will incur boxing overhead for primitives, as well as native primitive access. An example of generic access by ordinal:

```
import org.apache.spark.sql._

val row = Row(1, true, "a string", null)
// row: Row = [1,true,a string,null]
val firstValue = row(0)
// firstValue: Any = 1
val fourthValue = row(3)
// fourthValue: Any = null
```

For native primitive access, it is invalid to use the native primitive interface to retrieve a value that is null, instead a user must check `isNullAt` before attempting to retrieve a value that might be null. An example of native primitive access:

```
// using the row from the previous example.
val firstValue = row.getInt(0)
// firstValue: Int = 1
val isNull = row.isNullAt(3)
// isNull: Boolean = true
```

In Scala, fields in a [Row](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Row.html "org.apache.spark.sql.Row") object can be extracted in a pattern match. Example:

```
import org.apache.spark.sql._

val pairs = sql("SELECT key, value FROM src").rdd.map {
  case Row(key: Int, value: String) =>
    key -> value
}
```


Annotations
     @Stable() 

Since
    
1.3.0
  24. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/RowFactory.html "Permalink") class [RowFactory](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/RowFactory.html "A factory class used to construct Row objects.") extends AnyRef
A factory class used to construct `Row[](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Row.html "org.apache.spark.sql.Row")` objects.
A factory class used to construct `Row[](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Row.html "org.apache.spark.sql.Row")` objects.  

Annotations
     @Stable() 

Since
    
1.3.0
  25. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/RuntimeConfig.html "Permalink") abstract  class [RuntimeConfig](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/RuntimeConfig.html "Runtime configuration interface for Spark.") extends AnyRef
Runtime configuration interface for Spark.
Runtime configuration interface for Spark. To access this, use `SparkSession.conf`.
Options set here are automatically propagated to the Hadoop configuration during I/O.  

Annotations
     @Stable() 

Since
    
2.0.0
  26. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/SQLContext.html "Permalink") abstract  class [SQLContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/SQLContext.html "The entry point for working with structured data \(rows and columns\) in Spark 1.x.") extends Logging with Serializable
The entry point for working with structured data (rows and columns) in Spark 1.x.
The entry point for working with structured data (rows and columns) in Spark 1.x.
As of Spark 2.0, this is replaced by [SparkSession](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/SparkSession.html "org.apache.spark.sql.SparkSession"). However, we are keeping the class here for backward compatibility.  

Annotations
     @Stable() 

Since
    
1.0.0
  27. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/SQLImplicits.html "Permalink") abstract  class [SQLImplicits](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/SQLImplicits.html "A collection of implicit methods for converting common Scala objects into org.apache.spark.sql.Datasets.") extends [EncoderImplicits](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/EncoderImplicits.html "org.apache.spark.sql.EncoderImplicits") with Serializable
A collection of implicit methods for converting common Scala objects into [org.apache.spark.sql.Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")s.
A collection of implicit methods for converting common Scala objects into [org.apache.spark.sql.Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")s.  

Since
    
1.6.0
  28. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/SaveMode.html "Permalink") sealed final  class [SaveMode](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/SaveMode.html "SaveMode is used to specify the expected behavior of saving a DataFrame to a data source.") extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#java.lang.Enum "java.lang.Enum")[[SaveMode](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/SaveMode.html "org.apache.spark.sql.SaveMode")]
SaveMode is used to specify the expected behavior of saving a DataFrame to a data source.
SaveMode is used to specify the expected behavior of saving a DataFrame to a data source.  

Annotations
     @Stable() 

Since
    
1.3.0
  29. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/SparkSession.html "Permalink") abstract  class [SparkSession](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/SparkSession.html "The entry point to programming Spark with the Dataset and DataFrame API.") extends Serializable with [Closeable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Closeable.html#java.io.Closeable "java.io.Closeable")
The entry point to programming Spark with the Dataset and DataFrame API.
The entry point to programming Spark with the Dataset and DataFrame API.
In environments that this has been created upfront (e.g. REPL, notebooks), use the builder to get an existing session:

```
SparkSession.builder().getOrCreate()
```

The builder can also be used to create a new session:

```
SparkSession.builder
  .master("local")
  .appName("Word Count")
  .config("spark.some.config.option", "some-value")
  .getOrCreate()
```

  30. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/SparkSessionExtensions.html "Permalink") class [SparkSessionExtensions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/SparkSessionExtensions.html ":: Experimental :: Holder for injection points to the SparkSession.") extends AnyRef
Holder for injection points to the [SparkSession](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/SparkSession.html "org.apache.spark.sql.SparkSession").
Holder for injection points to the [SparkSession](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/SparkSession.html "org.apache.spark.sql.SparkSession"). We make NO guarantee about the stability regarding binary compatibility and source compatibility of methods here.
This current provides the following extension points:
     * Analyzer Rules.
     * Check Analysis Rules.
     * Cache Plan Normalization Rules.
     * Optimizer Rules.
     * Pre CBO Rules.
     * Planning Strategies.
     * Customized Parser.
     * (External) Catalog listeners.
     * Columnar Rules.
     * Adaptive Query Post Planner Strategy Rules.
     * Adaptive Query Stage Preparation Rules.
     * Adaptive Query Execution Runtime Optimizer Rules.
     * Adaptive Query Stage Optimizer Rules.
The extensions can be used by calling `withExtensions` on the [SparkSession.Builder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/SparkSession$$Builder.html "org.apache.spark.sql.SparkSession.Builder"), for example:

```
SparkSession.builder()
  .master("...")
  .config("...", true)
  .withExtensions { extensions =>
    extensions.injectResolutionRule { session =>
      ...
    }
    extensions.injectParser { (session, parser) =>
      ...
    }
  }
  .getOrCreate()
```

The extensions can also be used by setting the Spark SQL configuration property `spark.sql.extensions`. Multiple extensions can be set using a comma-separated list. For example:

```
SparkSession.builder()
  .master("...")
  .config("spark.sql.extensions", "org.example.MyExtensions,org.example.YourExtensions")
  .getOrCreate()

class MyExtensions extends Function1[SparkSessionExtensions, Unit] {
  override def apply(extensions: SparkSessionExtensions): Unit = {
    extensions.injectResolutionRule { session =>
      ...
    }
    extensions.injectParser { (session, parser) =>
      ...
    }
  }
}

class YourExtensions extends SparkSessionExtensionsProvider {
  override def apply(extensions: SparkSessionExtensions): Unit = {
    extensions.injectResolutionRule { session =>
      ...
    }
    extensions.injectFunction(...)
  }
}
```

Note that none of the injected builders should assume that the [SparkSession](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/SparkSession.html "org.apache.spark.sql.SparkSession") is fully initialized and should not touch the session's internals (e.g. the SessionState).  

Annotations
     @DeveloperApi() @Experimental() @Unstable()
  31. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/SparkSessionExtensionsProvider.html "Permalink") trait [SparkSessionExtensionsProvider](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/SparkSessionExtensionsProvider.html "Base trait for implementations used by SparkSessionExtensions") extends ([SparkSessionExtensions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/SparkSessionExtensions.html "org.apache.spark.sql.SparkSessionExtensions")) => Unit
Base trait for implementations used by [SparkSessionExtensions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/SparkSessionExtensions.html "org.apache.spark.sql.SparkSessionExtensions")
Base trait for implementations used by [SparkSessionExtensions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/SparkSessionExtensions.html "org.apache.spark.sql.SparkSessionExtensions")
For example, now we have an external function named `Age` to register as an extension for SparkSession:

```
package org.apache.spark.examples.extensions

import org.apache.spark.sql.catalyst.expressions.{CurrentDate, Expression, RuntimeReplaceable, SubtractDates}

case class Age(birthday: Expression, child: Expression) extends RuntimeReplaceable {

  def this(birthday: Expression) = this(birthday, SubtractDates(CurrentDate(), birthday))
  override def exprsReplaced: Seq[Expression] = Seq(birthday)
  override protected def withNewChildInternal(newChild: Expression): Expression = copy(newChild)
}
```

We need to create our extension which inherits [SparkSessionExtensionsProvider](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/SparkSessionExtensionsProvider.html "org.apache.spark.sql.SparkSessionExtensionsProvider") Example:

```
package org.apache.spark.examples.extensions

import org.apache.spark.sql.{SparkSessionExtensions, SparkSessionExtensionsProvider}
import org.apache.spark.sql.catalyst.FunctionIdentifier
import org.apache.spark.sql.catalyst.expressions.{Expression, ExpressionInfo}

class MyExtensions extends SparkSessionExtensionsProvider {
  override def apply(v1: SparkSessionExtensions): Unit = {
    v1.injectFunction(
      (new FunctionIdentifier("age"),
        new ExpressionInfo(classOf[Age].getName, "age"),
        (children: Seq[Expression]) => new Age(children.head)))
  }
}
```

Then, we can inject `MyExtensions` in three ways,
     * withExtensions of [SparkSession.Builder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/SparkSession$$Builder.html "org.apache.spark.sql.SparkSession.Builder")
     * Config - spark.sql.extensions
     * [java.util.ServiceLoader](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/ServiceLoader.html "java.util.ServiceLoader") - Add to src/main/resources/META-INF/services/org.apache.spark.sql.SparkSessionExtensionsProvider 

Annotations
     @DeveloperApi() @Since("3.2.0") 

Since
    
3.2.0 

See also
    
[SparkSessionExtensions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/SparkSessionExtensions.html "org.apache.spark.sql.SparkSessionExtensions")
[SparkSession.Builder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/SparkSession$$Builder.html "org.apache.spark.sql.SparkSession.Builder")
[java.util.ServiceLoader](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/ServiceLoader.html "java.util.ServiceLoader")
  32. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TableValuedFunction.html "Permalink") abstract  class [TableValuedFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TableValuedFunction.html "Interface for invoking table-valued functions in Spark SQL.") extends AnyRef
Interface for invoking table-valued functions in Spark SQL.
Interface for invoking table-valued functions in Spark SQL.  

Since
    
4.0.0
  33. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "Permalink") class [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "A Column where an Encoder has been given for the expected input and return type.")[-T, U] extends [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
A [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column") where an [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder") has been given for the expected input and return type.
A [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column") where an [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder") has been given for the expected input and return type. To create a [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn"), use the `as` function on a [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column").  

T
    
The input type expected for this expression. Can be `Any` if the expression is type checked by the analyzer instead of the compiler (i.e. `expr("sum(...)")`). 

U
    
The output type of this column. 

Annotations
     @Stable() 

Since
    
1.6.0
  34. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/UDFRegistration.html "Permalink") abstract  class [UDFRegistration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/UDFRegistration.html "Functions for registering user-defined functions.") extends AnyRef
Functions for registering user-defined functions.
Functions for registering user-defined functions. Use `SparkSession.udf` to access this:

```
spark.udf
```


Since
    
4.0.0
  35. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/WhenMatched.html "Permalink") case class [WhenMatched](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/WhenMatched.html "A class for defining actions to be taken when matching rows in a DataFrame during a merge operation.")[T] extends Product with Serializable
A class for defining actions to be taken when matching rows in a DataFrame during a merge operation.
A class for defining actions to be taken when matching rows in a DataFrame during a merge operation.  

T
    
The type of data in the MergeIntoWriter.
  36. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/WhenNotMatched.html "Permalink") case class [WhenNotMatched](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/WhenNotMatched.html "A class for defining actions to be taken when no matching rows are found in a DataFrame during a merge operation.")[T] extends Product with Serializable
A class for defining actions to be taken when no matching rows are found in a DataFrame during a merge operation.
A class for defining actions to be taken when no matching rows are found in a DataFrame during a merge operation.  

T
    
The type of data in the MergeIntoWriter.
  37. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/WhenNotMatchedBySource.html "Permalink") case class [WhenNotMatchedBySource](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/WhenNotMatchedBySource.html "A class for defining actions to be performed when there is no match by source during a merge operation in a MergeIntoWriter.")[T] extends Product with Serializable
A class for defining actions to be performed when there is no match by source during a merge operation in a MergeIntoWriter.
A class for defining actions to be performed when there is no match by source during a merge operation in a MergeIntoWriter.  

T
    
the type parameter for the MergeIntoWriter.
  38. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/WriteConfigMethods.html "Permalink") trait [WriteConfigMethods](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/WriteConfigMethods.html "Configuration methods common to create/replace operations and insert/overwrite operations.")[R] extends AnyRef
Configuration methods common to create/replace operations and insert/overwrite operations.
Configuration methods common to create/replace operations and insert/overwrite operations. 

R
    
builder type to return 

Since
    
3.0.0


### Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoders$.html "Permalink") object [Encoders](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoders$.html "Methods for creating an Encoder.")
Methods for creating an [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder").
Methods for creating an [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder").  

Since
    
1.6.0
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Observation$.html "Permalink") object [Observation](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Observation$.html "\(Scala-specific\) Create instances of Observation via Scala apply.")
(Scala-specific) Create instances of Observation via Scala `apply`.
(Scala-specific) Create instances of Observation via Scala `apply`. 

Since
    
3.3.0
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Row$.html "Permalink") object [Row](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Row$.html) extends [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable") 

Annotations
     @Stable() 

Since
    
1.3.0
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/SQLContext$.html "Permalink") object [SQLContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/SQLContext$.html) extends SQLContextCompanion with [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable")
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/SparkSession$.html "Permalink") object [SparkSession](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/SparkSession$.html) extends SparkSessionCompanion with [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable")
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/functions$.html "Permalink") object [functions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/functions$.html "Commonly used functions available for DataFrame operations.")
Commonly used functions available for DataFrame operations.
Commonly used functions available for DataFrame operations. Using functions defined here provides a little bit more compile-time safety to make sure the function exists.
You can call the functions defined here by two ways: `_FUNC_(...)` and `functions.expr("_FUNC_(...)")`.
As an example, `regr_count` is a function that is defined here. You can use `regr_count(col("yCol", col("xCol")))` to invoke the `regr_count` function. This way the programming language's compiler ensures `regr_count` exists and is of the proper form. You can also use `expr("regr_count(yCol, xCol)")` function to invoke the same function. In this case, Spark itself will ensure `regr_count` exists when it analyzes the query.
You can find the entire list of functions at SQL API documentation of your Spark version, see also [the latest list](https://spark.apache.org/docs/latest/api/sql/index.html)
This function APIs usually have methods with `Column` signature only because it can support not only `Column` but also other types such as a native string. The other variants currently exist for historical reasons.  

Annotations
     @Stable() 

Since
    
1.3.0


### Ungrouped
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/AnalysisException.html "Permalink") class [AnalysisException](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/AnalysisException.html "Thrown when a query fails to analyze, usually because the query itself is invalid.") extends Exception with [SparkThrowable](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/SparkThrowable.html "org.apache.spark.SparkThrowable") with Serializable with WithOrigin
Thrown when a query fails to analyze, usually because the query itself is invalid.
Thrown when a query fails to analyze, usually because the query itself is invalid.  

Annotations
     @Stable() 

Since
    
1.3.0
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "Permalink") class [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "A column that will be computed based on the data in a DataFrame.") extends Logging with TableValuedFunctionArgument
A column that will be computed based on the data in a `DataFrame`.
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

Since
    
1.3.0
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/ColumnName.html "Permalink") class [ColumnName](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/ColumnName.html "A convenient class used for constructing schema.") extends [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
A convenient class used for constructing schema.
A convenient class used for constructing schema.  

Annotations
     @Stable() 

Since
    
1.3.0
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/CreateTableWriter.html "Permalink") trait [CreateTableWriter](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/CreateTableWriter.html "Trait to restrict calls to create and replace operations.")[T] extends [WriteConfigMethods](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/WriteConfigMethods.html "org.apache.spark.sql.WriteConfigMethods")[[CreateTableWriter](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/CreateTableWriter.html "org.apache.spark.sql.CreateTableWriter")[T]]
Trait to restrict calls to create and replace operations.
Trait to restrict calls to create and replace operations.  

Since
    
3.0.0
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html#DataFrame=org.apache.spark.sql.Dataset\[org.apache.spark.sql.Row\] "Permalink") type DataFrame = [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")[[Row](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Row.html "org.apache.spark.sql.Row")]
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/DataFrameNaFunctions.html "Permalink") abstract  class [DataFrameNaFunctions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/DataFrameNaFunctions.html "Functionality for working with missing data in DataFrames.") extends AnyRef
Functionality for working with missing data in `DataFrame`s.
Functionality for working with missing data in `DataFrame`s.  

Annotations
     @Stable() 

Since
    
1.3.1
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/DataFrameReader.html "Permalink") abstract  class [DataFrameReader](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/DataFrameReader.html "Interface used to load a Dataset from external storage systems \(e.g.") extends AnyRef
Interface used to load a [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") from external storage systems (e.g.
Interface used to load a [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") from external storage systems (e.g. file systems, key-value stores, etc). Use `SparkSession.read` to access this.  

Annotations
     @Stable() 

Since
    
1.4.0
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/DataFrameStatFunctions.html "Permalink") abstract  class [DataFrameStatFunctions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/DataFrameStatFunctions.html "Statistic functions for DataFrames.") extends AnyRef
Statistic functions for `DataFrame`s.
Statistic functions for `DataFrame`s.  

Annotations
     @Stable() 

Since
    
1.4.0
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/DataFrameWriter.html "Permalink") abstract  class [DataFrameWriter](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/DataFrameWriter.html "Interface used to write a org.apache.spark.sql.Dataset to external storage systems \(e.g.")[T] extends AnyRef
Interface used to write a [org.apache.spark.sql.Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") to external storage systems (e.g.
Interface used to write a [org.apache.spark.sql.Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") to external storage systems (e.g. file systems, key-value stores, etc). Use `Dataset.write` to access this.  

Annotations
     @Stable() 

Since
    
1.4.0
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/DataFrameWriterV2.html "Permalink") abstract  class [DataFrameWriterV2](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/DataFrameWriterV2.html "Interface used to write a org.apache.spark.sql.Dataset to external storage using the v2 API.")[T] extends [CreateTableWriter](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/CreateTableWriter.html "org.apache.spark.sql.CreateTableWriter")[T]
Interface used to write a [org.apache.spark.sql.Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") to external storage using the v2 API.
Interface used to write a [org.apache.spark.sql.Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") to external storage using the v2 API.  

Annotations
     @Experimental() 

Since
    
3.0.0
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "Permalink") abstract  class [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "A Dataset is a strongly typed collection of domain-specific objects that can be transformed in parallel using functional or relational operations.")[T] extends Serializable
A Dataset is a strongly typed collection of domain-specific objects that can be transformed in parallel using functional or relational operations.
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

Since
    
1.6.0
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/DatasetHolder.html "Permalink") abstract  class [DatasetHolder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/DatasetHolder.html "A container for a org.apache.spark.sql.Dataset, used for implicit conversions in Scala.")[T] extends AnyRef
A container for a [org.apache.spark.sql.Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset"), used for implicit conversions in Scala.
A container for a [org.apache.spark.sql.Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset"), used for implicit conversions in Scala.
To use this, import implicit conversions in SQL:

```
val spark: SparkSession = ...
import spark.implicits._
```


Annotations
     @Stable() 

Since
    
1.6.0
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "Permalink") trait [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "Used to convert a JVM object of type T to and from the internal Spark SQL representation.")[T] extends Serializable
Used to convert a JVM object of type `T` to and from the internal Spark SQL representation.
Used to convert a JVM object of type `T` to and from the internal Spark SQL representation.
#### Scala
Encoders are generally created automatically through implicits from a `SparkSession`, or can be explicitly created by calling static methods on [Encoders](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoders$.html "org.apache.spark.sql.Encoders").

```
import spark.implicits._

val ds = Seq(1, 2, 3).toDS() // implicitly provided (spark.implicits.newIntEncoder)
```

#### Java
Encoders are specified by calling static methods on [Encoders](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoders$.html "org.apache.spark.sql.Encoders").

```
List<String> data = Arrays.asList("abc", "abc", "xyz");
Dataset<String> ds = context.createDataset(data, Encoders.STRING());
```

Encoders can be composed into tuples:

```
Encoder<Tuple2<Integer, String>> encoder2 = Encoders.tuple(Encoders.INT(), Encoders.STRING());
List<Tuple2<Integer, String>> data2 = Arrays.asList(new scala.Tuple2(1, "a");
Dataset<Tuple2<Integer, String>> ds2 = context.createDataset(data2, encoder2);
```

Or constructed from Java Beans:

```
Encoders.bean(MyClass.class);
```

#### Implementation
     * Encoders should be thread-safe.  

Annotations
     @implicitNotFound() 

Since
    
1.6.0
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/EncoderImplicits.html "Permalink") trait [EncoderImplicits](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/EncoderImplicits.html "EncoderImplicits used to implicitly generate SQL Encoders.") extends [LowPrioritySQLImplicits](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/LowPrioritySQLImplicits.html "org.apache.spark.sql.LowPrioritySQLImplicits") with Serializable
EncoderImplicits used to implicitly generate SQL Encoders.
EncoderImplicits used to implicitly generate SQL Encoders. Note that these functions don't rely on or expose `SparkSession`. 
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/ExperimentalMethods.html "Permalink") class [ExperimentalMethods](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/ExperimentalMethods.html ":: Experimental :: Holder for experimental methods for the bravest.") extends AnyRef
Holder for experimental methods for the bravest.
Holder for experimental methods for the bravest. We make NO guarantee about the stability regarding binary compatibility and source compatibility of methods here.

```
spark.experimental.extraStrategies += ...
```


Annotations
     @Experimental() @Unstable() 

Since
    
1.3.0
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/ExtendedExplainGenerator.html "Permalink") trait [ExtendedExplainGenerator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/ExtendedExplainGenerator.html "A trait for a session extension to implement that provides addition explain plan information.") extends AnyRef
A trait for a session extension to implement that provides addition explain plan information.
A trait for a session extension to implement that provides addition explain plan information.  

Annotations
     @DeveloperApi() @Since("4.0.0")
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/ForeachWriter.html "Permalink") abstract  class [ForeachWriter](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/ForeachWriter.html "The abstract class for writing custom logic to process data generated by a query.")[T] extends Serializable
The abstract class for writing custom logic to process data generated by a query.
The abstract class for writing custom logic to process data generated by a query. This is often used to write the output of a streaming query to arbitrary storage systems. Any implementation of this base class will be used by Spark in the following way.
     * A single instance of this class is responsible of all the data generated by a single task in a query. In other words, one instance is responsible for processing one partition of the data generated in a distributed manner.
     * Any implementation of this class must be serializable because each task will get a fresh serialized-deserialized copy of the provided object. Hence, it is strongly recommended that any initialization for writing data (e.g. opening a connection or starting a transaction) is done after the `open(...)` method has been called, which signifies that the task is ready to generate data.
     * The lifecycle of the methods are as follows.

```
 For each partition with `partitionId`: For each batch/epoch of streaming data (if its
streaming query) with `epochId`: Method `open(partitionId, epochId)` is called. If `open`
returns true: For each row in the partition and batch/epoch, method `process(row)` is called.
Method `close(errorOrNull)` is called with error (if any) seen while processing rows. 

```

Important points to note:
     * Spark doesn't guarantee same output for (partitionId, epochId), so deduplication cannot be achieved with (partitionId, epochId). e.g. source provides different number of partitions for some reason, Spark optimization changes number of partitions, etc. Refer SPARK-28650 for more details. If you need deduplication on output, try out `foreachBatch` instead.
     * The `close()` method will be called if `open()` method returns successfully (irrespective of the return value), except if the JVM crashes in the middle.
Scala example:

```
datasetOfString.writeStream.foreach(new ForeachWriter[String] {

  def open(partitionId: Long, version: Long): Boolean = {
    // open connection
  }

  def process(record: String) = {
    // write string to connection
  }

  def close(errorOrNull: Throwable): Unit = {
    // close the connection
  }
})
```

Java example:

```
datasetOfString.writeStream().foreach(new ForeachWriter<String>() {

  @Override
  public boolean open(long partitionId, long version) {
    // open connection
  }

  @Override
  public void process(String value) {
    // write string to connection
  }

  @Override
  public void close(Throwable errorOrNull) {
    // close the connection
  }
});
```


Since
    
2.0.0
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html "Permalink") abstract  class [KeyValueGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html "A Dataset has been logically grouped by a user specified grouping key.")[K, V] extends Serializable
A [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") has been logically grouped by a user specified grouping key.
A [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset") has been logically grouped by a user specified grouping key. Users should not construct a [KeyValueGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/KeyValueGroupedDataset.html "org.apache.spark.sql.KeyValueGroupedDataset") directly, but should instead call `groupByKey` on an existing [Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset").  

Since
    
2.0.0
  19. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/LowPrioritySQLImplicits.html "Permalink") trait [LowPrioritySQLImplicits](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/LowPrioritySQLImplicits.html "Lower priority implicit methods for converting Scala objects into org.apache.spark.sql.Datasets.") extends AnyRef
Lower priority implicit methods for converting Scala objects into [org.apache.spark.sql.Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")s.
Lower priority implicit methods for converting Scala objects into [org.apache.spark.sql.Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")s. Conflicting implicits are placed here to disambiguate resolution.
Reasons for including specific implicits: newProductEncoder - to disambiguate for `List`s which are both `Seq` and `Product`
  20. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/MergeIntoWriter.html "Permalink") abstract  class [MergeIntoWriter](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/MergeIntoWriter.html "MergeIntoWriter provides methods to define and execute merge actions based on specified conditions.")[T] extends AnyRef
`MergeIntoWriter` provides methods to define and execute merge actions based on specified conditions.
`MergeIntoWriter` provides methods to define and execute merge actions based on specified conditions.
Please note that schema evolution is disabled by default.  

T
    
the type of data in the Dataset. 

Annotations
     @Experimental() 

Since
    
4.0.0
  21. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Observation.html "Permalink") class [Observation](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Observation.html "Helper class to simplify usage of Dataset.observe\(String, Column, Column*\):") extends AnyRef
Helper class to simplify usage of `Dataset.observe(String, Column, Column*)`:
Helper class to simplify usage of `Dataset.observe(String, Column, Column*)`:

```
// Observe row count (rows) and highest id (maxid) in the Dataset while writing it
val observation = Observation("my metrics")
val observed_ds = ds.observe(observation, count(lit(1)).as("rows"), max($"id").as("maxid"))
observed_ds.write.parquet("ds.parquet")
val metrics = observation.get
```

This collects the metrics while the first action is executed on the observed dataset. Subsequent actions do not modify the metrics returned by [get](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Observation.html#get:Map\[String,Any\]). Retrieval of the metric via [get](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Observation.html#get:Map\[String,Any\]) blocks until the first action has finished and metrics become available.
This class does not support streaming datasets.  

Since
    
3.3.0
  22. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/RelationalGroupedDataset.html "Permalink") abstract  class [RelationalGroupedDataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/RelationalGroupedDataset.html "A set of methods for aggregations on a DataFrame, created by groupBy, cube or rollup \(and also pivot\).") extends AnyRef
A set of methods for aggregations on a `DataFrame`, created by [groupBy](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#groupBy\(col1:String,cols:String*\):org.apache.spark.sql.RelationalGroupedDataset), [cube](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#cube\(col1:String,cols:String*\):org.apache.spark.sql.RelationalGroupedDataset) or [rollup](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#rollup\(col1:String,cols:String*\):org.apache.spark.sql.RelationalGroupedDataset) (and also `pivot`).
A set of methods for aggregations on a `DataFrame`, created by [groupBy](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#groupBy\(col1:String,cols:String*\):org.apache.spark.sql.RelationalGroupedDataset), [cube](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#cube\(col1:String,cols:String*\):org.apache.spark.sql.RelationalGroupedDataset) or [rollup](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html#rollup\(col1:String,cols:String*\):org.apache.spark.sql.RelationalGroupedDataset) (and also `pivot`).
The main method is the `agg` function, which has multiple variants. This class also contains some first-order statistics such as `mean`, `sum` for convenience.  

Annotations
     @Stable() 

Since
    
2.0.0 

Note
    
This class was named `GroupedData` in Spark 1.x.
  23. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Row.html "Permalink") trait [Row](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Row.html "Represents one row of output from a relational operator.") extends Serializable
Represents one row of output from a relational operator.
Represents one row of output from a relational operator. Allows both generic access by ordinal, which will incur boxing overhead for primitives, as well as native primitive access.
It is invalid to use the native primitive interface to retrieve a value that is null, instead a user must check `isNullAt` before attempting to retrieve a value that might be null.
To create a new Row, use `RowFactory.create()` in Java or `Row.apply()` in Scala.
A [Row](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Row.html "org.apache.spark.sql.Row") object can be constructed by providing field values. Example:

```
import org.apache.spark.sql._

// Create a Row from values.
Row(value1, value2, value3, ...)
// Create a Row from a Seq of values.
Row.fromSeq(Seq(value1, value2, ...))
```

A value of a row can be accessed through both generic access by ordinal, which will incur boxing overhead for primitives, as well as native primitive access. An example of generic access by ordinal:

```
import org.apache.spark.sql._

val row = Row(1, true, "a string", null)
// row: Row = [1,true,a string,null]
val firstValue = row(0)
// firstValue: Any = 1
val fourthValue = row(3)
// fourthValue: Any = null
```

For native primitive access, it is invalid to use the native primitive interface to retrieve a value that is null, instead a user must check `isNullAt` before attempting to retrieve a value that might be null. An example of native primitive access:

```
// using the row from the previous example.
val firstValue = row.getInt(0)
// firstValue: Int = 1
val isNull = row.isNullAt(3)
// isNull: Boolean = true
```

In Scala, fields in a [Row](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Row.html "org.apache.spark.sql.Row") object can be extracted in a pattern match. Example:

```
import org.apache.spark.sql._

val pairs = sql("SELECT key, value FROM src").rdd.map {
  case Row(key: Int, value: String) =>
    key -> value
}
```


Annotations
     @Stable() 

Since
    
1.3.0
  24. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/RowFactory.html "Permalink") class [RowFactory](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/RowFactory.html "A factory class used to construct Row objects.") extends AnyRef
A factory class used to construct `Row[](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Row.html "org.apache.spark.sql.Row")` objects.
A factory class used to construct `Row[](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Row.html "org.apache.spark.sql.Row")` objects.  

Annotations
     @Stable() 

Since
    
1.3.0
  25. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/RuntimeConfig.html "Permalink") abstract  class [RuntimeConfig](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/RuntimeConfig.html "Runtime configuration interface for Spark.") extends AnyRef
Runtime configuration interface for Spark.
Runtime configuration interface for Spark. To access this, use `SparkSession.conf`.
Options set here are automatically propagated to the Hadoop configuration during I/O.  

Annotations
     @Stable() 

Since
    
2.0.0
  26. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/SQLContext.html "Permalink") abstract  class [SQLContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/SQLContext.html "The entry point for working with structured data \(rows and columns\) in Spark 1.x.") extends Logging with Serializable
The entry point for working with structured data (rows and columns) in Spark 1.x.
The entry point for working with structured data (rows and columns) in Spark 1.x.
As of Spark 2.0, this is replaced by [SparkSession](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/SparkSession.html "org.apache.spark.sql.SparkSession"). However, we are keeping the class here for backward compatibility.  

Annotations
     @Stable() 

Since
    
1.0.0
  27. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/SQLImplicits.html "Permalink") abstract  class [SQLImplicits](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/SQLImplicits.html "A collection of implicit methods for converting common Scala objects into org.apache.spark.sql.Datasets.") extends [EncoderImplicits](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/EncoderImplicits.html "org.apache.spark.sql.EncoderImplicits") with Serializable
A collection of implicit methods for converting common Scala objects into [org.apache.spark.sql.Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")s.
A collection of implicit methods for converting common Scala objects into [org.apache.spark.sql.Dataset](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Dataset.html "org.apache.spark.sql.Dataset")s.  

Since
    
1.6.0
  28. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/SaveMode.html "Permalink") sealed final  class [SaveMode](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/SaveMode.html "SaveMode is used to specify the expected behavior of saving a DataFrame to a data source.") extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#java.lang.Enum "java.lang.Enum")[[SaveMode](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/SaveMode.html "org.apache.spark.sql.SaveMode")]
SaveMode is used to specify the expected behavior of saving a DataFrame to a data source.
SaveMode is used to specify the expected behavior of saving a DataFrame to a data source.  

Annotations
     @Stable() 

Since
    
1.3.0
  29. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/SparkSession.html "Permalink") abstract  class [SparkSession](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/SparkSession.html "The entry point to programming Spark with the Dataset and DataFrame API.") extends Serializable with [Closeable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Closeable.html#java.io.Closeable "java.io.Closeable")
The entry point to programming Spark with the Dataset and DataFrame API.
The entry point to programming Spark with the Dataset and DataFrame API.
In environments that this has been created upfront (e.g. REPL, notebooks), use the builder to get an existing session:

```
SparkSession.builder().getOrCreate()
```

The builder can also be used to create a new session:

```
SparkSession.builder
  .master("local")
  .appName("Word Count")
  .config("spark.some.config.option", "some-value")
  .getOrCreate()
```

  30. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/SparkSessionExtensions.html "Permalink") class [SparkSessionExtensions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/SparkSessionExtensions.html ":: Experimental :: Holder for injection points to the SparkSession.") extends AnyRef
Holder for injection points to the [SparkSession](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/SparkSession.html "org.apache.spark.sql.SparkSession").
Holder for injection points to the [SparkSession](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/SparkSession.html "org.apache.spark.sql.SparkSession"). We make NO guarantee about the stability regarding binary compatibility and source compatibility of methods here.
This current provides the following extension points:
     * Analyzer Rules.
     * Check Analysis Rules.
     * Cache Plan Normalization Rules.
     * Optimizer Rules.
     * Pre CBO Rules.
     * Planning Strategies.
     * Customized Parser.
     * (External) Catalog listeners.
     * Columnar Rules.
     * Adaptive Query Post Planner Strategy Rules.
     * Adaptive Query Stage Preparation Rules.
     * Adaptive Query Execution Runtime Optimizer Rules.
     * Adaptive Query Stage Optimizer Rules.
The extensions can be used by calling `withExtensions` on the [SparkSession.Builder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/SparkSession$$Builder.html "org.apache.spark.sql.SparkSession.Builder"), for example:

```
SparkSession.builder()
  .master("...")
  .config("...", true)
  .withExtensions { extensions =>
    extensions.injectResolutionRule { session =>
      ...
    }
    extensions.injectParser { (session, parser) =>
      ...
    }
  }
  .getOrCreate()
```

The extensions can also be used by setting the Spark SQL configuration property `spark.sql.extensions`. Multiple extensions can be set using a comma-separated list. For example:

```
SparkSession.builder()
  .master("...")
  .config("spark.sql.extensions", "org.example.MyExtensions,org.example.YourExtensions")
  .getOrCreate()

class MyExtensions extends Function1[SparkSessionExtensions, Unit] {
  override def apply(extensions: SparkSessionExtensions): Unit = {
    extensions.injectResolutionRule { session =>
      ...
    }
    extensions.injectParser { (session, parser) =>
      ...
    }
  }
}

class YourExtensions extends SparkSessionExtensionsProvider {
  override def apply(extensions: SparkSessionExtensions): Unit = {
    extensions.injectResolutionRule { session =>
      ...
    }
    extensions.injectFunction(...)
  }
}
```

Note that none of the injected builders should assume that the [SparkSession](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/SparkSession.html "org.apache.spark.sql.SparkSession") is fully initialized and should not touch the session's internals (e.g. the SessionState).  

Annotations
     @DeveloperApi() @Experimental() @Unstable()
  31. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/SparkSessionExtensionsProvider.html "Permalink") trait [SparkSessionExtensionsProvider](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/SparkSessionExtensionsProvider.html "Base trait for implementations used by SparkSessionExtensions") extends ([SparkSessionExtensions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/SparkSessionExtensions.html "org.apache.spark.sql.SparkSessionExtensions")) => Unit
Base trait for implementations used by [SparkSessionExtensions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/SparkSessionExtensions.html "org.apache.spark.sql.SparkSessionExtensions")
Base trait for implementations used by [SparkSessionExtensions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/SparkSessionExtensions.html "org.apache.spark.sql.SparkSessionExtensions")
For example, now we have an external function named `Age` to register as an extension for SparkSession:

```
package org.apache.spark.examples.extensions

import org.apache.spark.sql.catalyst.expressions.{CurrentDate, Expression, RuntimeReplaceable, SubtractDates}

case class Age(birthday: Expression, child: Expression) extends RuntimeReplaceable {

  def this(birthday: Expression) = this(birthday, SubtractDates(CurrentDate(), birthday))
  override def exprsReplaced: Seq[Expression] = Seq(birthday)
  override protected def withNewChildInternal(newChild: Expression): Expression = copy(newChild)
}
```

We need to create our extension which inherits [SparkSessionExtensionsProvider](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/SparkSessionExtensionsProvider.html "org.apache.spark.sql.SparkSessionExtensionsProvider") Example:

```
package org.apache.spark.examples.extensions

import org.apache.spark.sql.{SparkSessionExtensions, SparkSessionExtensionsProvider}
import org.apache.spark.sql.catalyst.FunctionIdentifier
import org.apache.spark.sql.catalyst.expressions.{Expression, ExpressionInfo}

class MyExtensions extends SparkSessionExtensionsProvider {
  override def apply(v1: SparkSessionExtensions): Unit = {
    v1.injectFunction(
      (new FunctionIdentifier("age"),
        new ExpressionInfo(classOf[Age].getName, "age"),
        (children: Seq[Expression]) => new Age(children.head)))
  }
}
```

Then, we can inject `MyExtensions` in three ways,
     * withExtensions of [SparkSession.Builder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/SparkSession$$Builder.html "org.apache.spark.sql.SparkSession.Builder")
     * Config - spark.sql.extensions
     * [java.util.ServiceLoader](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/ServiceLoader.html "java.util.ServiceLoader") - Add to src/main/resources/META-INF/services/org.apache.spark.sql.SparkSessionExtensionsProvider 

Annotations
     @DeveloperApi() @Since("3.2.0") 

Since
    
3.2.0 

See also
    
[SparkSessionExtensions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/SparkSessionExtensions.html "org.apache.spark.sql.SparkSessionExtensions")
[SparkSession.Builder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/SparkSession$$Builder.html "org.apache.spark.sql.SparkSession.Builder")
[java.util.ServiceLoader](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/ServiceLoader.html "java.util.ServiceLoader")
  32. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TableValuedFunction.html "Permalink") abstract  class [TableValuedFunction](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TableValuedFunction.html "Interface for invoking table-valued functions in Spark SQL.") extends AnyRef
Interface for invoking table-valued functions in Spark SQL.
Interface for invoking table-valued functions in Spark SQL.  

Since
    
4.0.0
  33. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "Permalink") class [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "A Column where an Encoder has been given for the expected input and return type.")[-T, U] extends [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column")
A [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column") where an [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder") has been given for the expected input and return type.
A [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column") where an [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder") has been given for the expected input and return type. To create a [TypedColumn](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/TypedColumn.html "org.apache.spark.sql.TypedColumn"), use the `as` function on a [Column](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html "org.apache.spark.sql.Column").  

T
    
The input type expected for this expression. Can be `Any` if the expression is type checked by the analyzer instead of the compiler (i.e. `expr("sum(...)")`). 

U
    
The output type of this column. 

Annotations
     @Stable() 

Since
    
1.6.0
  34. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/UDFRegistration.html "Permalink") abstract  class [UDFRegistration](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/UDFRegistration.html "Functions for registering user-defined functions.") extends AnyRef
Functions for registering user-defined functions.
Functions for registering user-defined functions. Use `SparkSession.udf` to access this:

```
spark.udf
```


Since
    
4.0.0
  35. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/WhenMatched.html "Permalink") case class [WhenMatched](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/WhenMatched.html "A class for defining actions to be taken when matching rows in a DataFrame during a merge operation.")[T] extends Product with Serializable
A class for defining actions to be taken when matching rows in a DataFrame during a merge operation.
A class for defining actions to be taken when matching rows in a DataFrame during a merge operation.  

T
    
The type of data in the MergeIntoWriter.
  36. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/WhenNotMatched.html "Permalink") case class [WhenNotMatched](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/WhenNotMatched.html "A class for defining actions to be taken when no matching rows are found in a DataFrame during a merge operation.")[T] extends Product with Serializable
A class for defining actions to be taken when no matching rows are found in a DataFrame during a merge operation.
A class for defining actions to be taken when no matching rows are found in a DataFrame during a merge operation.  

T
    
The type of data in the MergeIntoWriter.
  37. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/WhenNotMatchedBySource.html "Permalink") case class [WhenNotMatchedBySource](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/WhenNotMatchedBySource.html "A class for defining actions to be performed when there is no match by source during a merge operation in a MergeIntoWriter.")[T] extends Product with Serializable
A class for defining actions to be performed when there is no match by source during a merge operation in a MergeIntoWriter.
A class for defining actions to be performed when there is no match by source during a merge operation in a MergeIntoWriter.  

T
    
the type parameter for the MergeIntoWriter.
  38. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/WriteConfigMethods.html "Permalink") trait [WriteConfigMethods](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/WriteConfigMethods.html "Configuration methods common to create/replace operations and insert/overwrite operations.")[R] extends AnyRef
Configuration methods common to create/replace operations and insert/overwrite operations.
Configuration methods common to create/replace operations and insert/overwrite operations. 

R
    
builder type to return 

Since
    
3.0.0


  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoders$.html "Permalink") object [Encoders](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoders$.html "Methods for creating an Encoder.")
Methods for creating an [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder").
Methods for creating an [Encoder](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Encoder.html "org.apache.spark.sql.Encoder").  

Since
    
1.6.0
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Observation$.html "Permalink") object [Observation](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Observation$.html "\(Scala-specific\) Create instances of Observation via Scala apply.")
(Scala-specific) Create instances of Observation via Scala `apply`.
(Scala-specific) Create instances of Observation via Scala `apply`. 

Since
    
3.3.0
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Row$.html "Permalink") object [Row](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Row$.html) extends [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable") 

Annotations
     @Stable() 

Since
    
1.3.0
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/SQLContext$.html "Permalink") object [SQLContext](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/SQLContext$.html) extends SQLContextCompanion with [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable")
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/SparkSession$.html "Permalink") object [SparkSession](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/SparkSession$.html) extends SparkSessionCompanion with [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable")
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/functions$.html "Permalink") object [functions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/functions$.html "Commonly used functions available for DataFrame operations.")
Commonly used functions available for DataFrame operations.
Commonly used functions available for DataFrame operations. Using functions defined here provides a little bit more compile-time safety to make sure the function exists.
You can call the functions defined here by two ways: `_FUNC_(...)` and `functions.expr("_FUNC_(...)")`.
As an example, `regr_count` is a function that is defined here. You can use `regr_count(col("yCol", col("xCol")))` to invoke the `regr_count` function. This way the programming language's compiler ensures `regr_count` exists and is of the proper form. You can also use `expr("regr_count(yCol, xCol)")` function to invoke the same function. In this case, Spark itself will ensure `regr_count` exists when it analyzes the query.
You can find the entire list of functions at SQL API documentation of your Spark version, see also [the latest list](https://spark.apache.org/docs/latest/api/sql/index.html)
This function APIs usually have methods with `Column` signature only because it can support not only `Column` but also other types such as a native string. The other variants currently exist for historical reasons.  

Annotations
     @Stable() 

Since
    
1.3.0


