[Skip navigation links](https://spark.apache.org/docs/latest/api/java/deprecated-list.html#skip-navbar-top "Skip navigation links")
  * [Overview](https://spark.apache.org/docs/latest/api/java/index.html)
  * Package
  * Class
  * Deprecated
  * [Index](https://spark.apache.org/docs/latest/api/java/index-all.html)
  * [Help](https://spark.apache.org/docs/latest/api/java/help-doc.html#deprecated)

SEARCH:
# Deprecated API
## Contents
  * [Classes](https://spark.apache.org/docs/latest/api/java/deprecated-list.html#class)
  * [Fields](https://spark.apache.org/docs/latest/api/java/deprecated-list.html#field)
  * [Methods](https://spark.apache.org/docs/latest/api/java/deprecated-list.html#method)
  * [Constructors](https://spark.apache.org/docs/latest/api/java/deprecated-list.html#constructor)

  * Deprecated Classes
Class
Description
[org.apache.spark.ContextAwareIterator](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ContextAwareIterator.html "class in org.apache.spark")
since 4.0.0 as its only usage for Python evaluation is now extinct
[org.apache.spark.ml.feature.ChiSqSelector](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/ChiSqSelector.html "class in org.apache.spark.ml.feature")
use UnivariateFeatureSelector instead. Since 3.1.1.
[org.apache.spark.rdd.JdbcRDD](https://spark.apache.org/docs/latest/api/java/org/apache/spark/rdd/JdbcRDD.html "class in org.apache.spark.rdd")
Jdbc RDD is deprecated, consider using JDBC data source instead.
[org.apache.spark.scheduler.SparkListenerExecutorBlacklisted](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/SparkListenerExecutorBlacklisted.html "class in org.apache.spark.scheduler")
use SparkListenerExecutorExcluded instead. Since 3.1.0.
[org.apache.spark.scheduler.SparkListenerExecutorBlacklistedForStage](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/SparkListenerExecutorBlacklistedForStage.html "class in org.apache.spark.scheduler")
use SparkListenerExecutorExcludedForStage instead. Since 3.1.0.
[org.apache.spark.scheduler.SparkListenerExecutorUnblacklisted](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/SparkListenerExecutorUnblacklisted.html "class in org.apache.spark.scheduler")
use SparkListenerExecutorUnexcluded instead. Since 3.1.0.
[org.apache.spark.scheduler.SparkListenerNodeBlacklisted](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/SparkListenerNodeBlacklisted.html "class in org.apache.spark.scheduler")
use SparkListenerNodeExcluded instead. Since 3.1.0.
[org.apache.spark.scheduler.SparkListenerNodeBlacklistedForStage](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/SparkListenerNodeBlacklistedForStage.html "class in org.apache.spark.scheduler")
use SparkListenerNodeExcludedForStage instead. Since 3.1.0.
[org.apache.spark.scheduler.SparkListenerNodeUnblacklisted](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/SparkListenerNodeUnblacklisted.html "class in org.apache.spark.scheduler")
use SparkListenerNodeUnexcluded instead. Since 3.1.0.
[org.apache.spark.sql.expressions.javalang.typed](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/expressions/javalang/typed.html "class in org.apache.spark.sql.expressions.javalang")
As of release 3.0.0, please use the untyped builtin aggregate functions.
[org.apache.spark.sql.expressions.scalalang.typed](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/expressions/scalalang/typed.html "class in org.apache.spark.sql.expressions.scalalang")
please use untyped builtin aggregate functions. Since 3.0.0.
[org.apache.spark.sql.expressions.UserDefinedAggregateFunction](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/expressions/UserDefinedAggregateFunction.html "class in org.apache.spark.sql.expressions")
UserDefinedAggregateFunction is deprecated. Aggregator[IN, BUF, OUT] should now be registered as a UDF via the functions.udaf(agg) method.
[org.apache.spark.streaming.api.java.JavaStreamingContext](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/api/java/JavaStreamingContext.html "class in org.apache.spark.streaming.api.java")
This is deprecated as of Spark 3.4.0. There are no longer updates to DStream and it's a legacy project. There is a newer and easier to use streaming engine in Spark called Structured Streaming. You should use Spark Structured Streaming for your streaming applications.
[org.apache.spark.streaming.StreamingContext](https://spark.apache.org/docs/latest/api/java/org/apache/spark/streaming/StreamingContext.html "class in org.apache.spark.streaming")
This is deprecated as of Spark 3.4.0. There are no longer updates to DStream and it's a legacy project. There is a newer and easier to use streaming engine in Spark called Structured Streaming. You should use Spark Structured Streaming for your streaming applications.

  * Deprecated Fields
Field
Description
[org.apache.spark.launcher.SparkLauncher.DEPRECATED_CHILD_CONNECTION_TIMEOUT](https://spark.apache.org/docs/latest/api/java/org/apache/spark/launcher/SparkLauncher.html#DEPRECATED_CHILD_CONNECTION_TIMEOUT)
use `CHILD_CONNECTION_TIMEOUT`

  * Deprecated Methods
Method
Description
[org.apache.spark.ml.clustering.BisectingKMeansModel.computeCost(Dataset<?>)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/clustering/BisectingKMeansModel.html#computeCost\(org.apache.spark.sql.Dataset\))
This method is deprecated and will be removed in future versions. Use ClusteringEvaluator instead. You can also get the cost on the training dataset in the summary.
[org.apache.spark.ml.feature.StringIndexerModel.labels()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/StringIndexerModel.html#labels\(\))
`labels` is deprecated and will be removed in 3.1.0. Use `labelsArray` instead. Since 3.0.0.
[org.apache.spark.ml.Pipeline.SharedReadWrite$.load(String, SparkContext, String)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/Pipeline.SharedReadWrite$.html#load\(java.lang.String,org.apache.spark.SparkContext,java.lang.String\))
use load with SparkSession. Since 4.0.0.
[org.apache.spark.ml.Pipeline.SharedReadWrite$.saveImpl(Params, PipelineStage[], SparkContext, String)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/Pipeline.SharedReadWrite$.html#saveImpl\(org.apache.spark.ml.param.Params,org.apache.spark.ml.PipelineStage%5B%5D,org.apache.spark.SparkContext,java.lang.String\))
use saveImpl with SparkSession. Since 4.0.0.
[org.apache.spark.scheduler.SparkListenerInterface.onExecutorBlacklisted(SparkListenerExecutorBlacklisted)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/SparkListenerInterface.html#onExecutorBlacklisted\(org.apache.spark.scheduler.SparkListenerExecutorBlacklisted\))
use onExecutorExcluded instead. Since 3.1.0.
[org.apache.spark.scheduler.SparkListenerInterface.onExecutorBlacklistedForStage(SparkListenerExecutorBlacklistedForStage)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/SparkListenerInterface.html#onExecutorBlacklistedForStage\(org.apache.spark.scheduler.SparkListenerExecutorBlacklistedForStage\))
use onExecutorExcludedForStage instead. Since 3.1.0.
[org.apache.spark.scheduler.SparkListenerInterface.onExecutorUnblacklisted(SparkListenerExecutorUnblacklisted)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/SparkListenerInterface.html#onExecutorUnblacklisted\(org.apache.spark.scheduler.SparkListenerExecutorUnblacklisted\))
use onExecutorUnexcluded instead. Since 3.1.0.
[org.apache.spark.scheduler.SparkListenerInterface.onNodeBlacklisted(SparkListenerNodeBlacklisted)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/SparkListenerInterface.html#onNodeBlacklisted\(org.apache.spark.scheduler.SparkListenerNodeBlacklisted\))
use onNodeExcluded instead. Since 3.1.0.
[org.apache.spark.scheduler.SparkListenerInterface.onNodeBlacklistedForStage(SparkListenerNodeBlacklistedForStage)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/SparkListenerInterface.html#onNodeBlacklistedForStage\(org.apache.spark.scheduler.SparkListenerNodeBlacklistedForStage\))
use onNodeExcludedForStage instead. Since 3.1.0.
[org.apache.spark.scheduler.SparkListenerInterface.onNodeUnblacklisted(SparkListenerNodeUnblacklisted)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/scheduler/SparkListenerInterface.html#onNodeUnblacklisted\(org.apache.spark.scheduler.SparkListenerNodeUnblacklisted\))
use onNodeUnexcluded instead. Since 3.1.0.
[org.apache.spark.SparkThrowable.getErrorClass()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/SparkThrowable.html#getErrorClass\(\))
Use [`SparkThrowable.getCondition()`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/SparkThrowable.html#getCondition\(\)) instead.
[org.apache.spark.sql.catalog.Catalog.createExternalTable(String, String)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/catalog/Catalog.html#createExternalTable\(java.lang.String,java.lang.String\))
use createTable instead. Since 2.2.0.
[org.apache.spark.sql.catalog.Catalog.createExternalTable(String, String, String)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/catalog/Catalog.html#createExternalTable\(java.lang.String,java.lang.String,java.lang.String\))
use createTable instead. Since 2.2.0.
[org.apache.spark.sql.catalog.Catalog.createExternalTable(String, String, Map<String, String>)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/catalog/Catalog.html#createExternalTable\(java.lang.String,java.lang.String,java.util.Map\))
use createTable instead. Since 2.2.0.
[org.apache.spark.sql.catalog.Catalog.createExternalTable(String, String, StructType, Map<String, String>)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/catalog/Catalog.html#createExternalTable\(java.lang.String,java.lang.String,org.apache.spark.sql.types.StructType,java.util.Map\))
use createTable instead. Since 2.2.0.
[org.apache.spark.sql.catalog.Catalog.createExternalTable(String, String, StructType, Map<String, String>)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/catalog/Catalog.html#createExternalTable\(java.lang.String,java.lang.String,org.apache.spark.sql.types.StructType,scala.collection.immutable.Map\))
use createTable instead. Since 2.2.0.
[org.apache.spark.sql.catalog.Catalog.createExternalTable(String, String, Map<String, String>)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/catalog/Catalog.html#createExternalTable\(java.lang.String,java.lang.String,scala.collection.immutable.Map\))
use createTable instead. Since 2.2.0.
[org.apache.spark.sql.catalog.Catalog.functionExists(String, String)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/catalog/Catalog.html#functionExists\(java.lang.String,java.lang.String\))
use functionExists(functionName: String) instead. Since 4.0.0.
[org.apache.spark.sql.catalog.Catalog.getFunction(String, String)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/catalog/Catalog.html#getFunction\(java.lang.String,java.lang.String\))
use getFunction(functionName: String) instead. Since 4.0.0.
[org.apache.spark.sql.catalog.Catalog.getTable(String, String)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/catalog/Catalog.html#getTable\(java.lang.String,java.lang.String\))
use getTable(tableName: String) instead. Since 4.0.0.
[org.apache.spark.sql.catalog.Catalog.listColumns(String, String)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/catalog/Catalog.html#listColumns\(java.lang.String,java.lang.String\))
use listColumns(tableName: String) instead. Since 4.0.0.
[org.apache.spark.sql.catalog.Catalog.tableExists(String, String)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/catalog/Catalog.html#tableExists\(java.lang.String,java.lang.String\))
use tableExists(tableName: String) instead. Since 4.0.0.
[org.apache.spark.sql.connector.catalog.StagingTableCatalog.stageCreate(Identifier, Column[], Transform[], Map<String, String>)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/StagingTableCatalog.html#stageCreate\(org.apache.spark.sql.connector.catalog.Identifier,org.apache.spark.sql.connector.catalog.Column%5B%5D,org.apache.spark.sql.connector.expressions.Transform%5B%5D,java.util.Map\))
This is deprecated. Please override [`StagingTableCatalog.stageCreate(Identifier, TableInfo)`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/StagingTableCatalog.html#stageCreate\(org.apache.spark.sql.connector.catalog.Identifier,org.apache.spark.sql.connector.catalog.TableInfo\)) instead.
[org.apache.spark.sql.connector.catalog.StagingTableCatalog.stageCreate(Identifier, StructType, Transform[], Map<String, String>)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/StagingTableCatalog.html#stageCreate\(org.apache.spark.sql.connector.catalog.Identifier,org.apache.spark.sql.types.StructType,org.apache.spark.sql.connector.expressions.Transform%5B%5D,java.util.Map\))
This is deprecated. Please override [`StagingTableCatalog.stageCreate(Identifier, Column[], Transform[], Map)`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/StagingTableCatalog.html#stageCreate\(org.apache.spark.sql.connector.catalog.Identifier,org.apache.spark.sql.connector.catalog.Column%5B%5D,org.apache.spark.sql.connector.expressions.Transform%5B%5D,java.util.Map\)) instead.
[org.apache.spark.sql.connector.catalog.StagingTableCatalog.stageCreateOrReplace(Identifier, Column[], Transform[], Map<String, String>)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/StagingTableCatalog.html#stageCreateOrReplace\(org.apache.spark.sql.connector.catalog.Identifier,org.apache.spark.sql.connector.catalog.Column%5B%5D,org.apache.spark.sql.connector.expressions.Transform%5B%5D,java.util.Map\))
[org.apache.spark.sql.connector.catalog.StagingTableCatalog.stageCreateOrReplace(Identifier, StructType, Transform[], Map<String, String>)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/StagingTableCatalog.html#stageCreateOrReplace\(org.apache.spark.sql.connector.catalog.Identifier,org.apache.spark.sql.types.StructType,org.apache.spark.sql.connector.expressions.Transform%5B%5D,java.util.Map\))
[org.apache.spark.sql.connector.catalog.StagingTableCatalog.stageReplace(Identifier, Column[], Transform[], Map<String, String>)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/StagingTableCatalog.html#stageReplace\(org.apache.spark.sql.connector.catalog.Identifier,org.apache.spark.sql.connector.catalog.Column%5B%5D,org.apache.spark.sql.connector.expressions.Transform%5B%5D,java.util.Map\))
[org.apache.spark.sql.connector.catalog.StagingTableCatalog.stageReplace(Identifier, StructType, Transform[], Map<String, String>)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/StagingTableCatalog.html#stageReplace\(org.apache.spark.sql.connector.catalog.Identifier,org.apache.spark.sql.types.StructType,org.apache.spark.sql.connector.expressions.Transform%5B%5D,java.util.Map\))
[org.apache.spark.sql.connector.catalog.Table.schema()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/Table.html#schema\(\))
This is deprecated. Please override [`Table.columns()`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/Table.html#columns\(\)) instead.
[org.apache.spark.sql.connector.catalog.TableCatalog.createTable(Identifier, Column[], Transform[], Map<String, String>)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/TableCatalog.html#createTable\(org.apache.spark.sql.connector.catalog.Identifier,org.apache.spark.sql.connector.catalog.Column%5B%5D,org.apache.spark.sql.connector.expressions.Transform%5B%5D,java.util.Map\))
This is deprecated. Please override [`TableCatalog.createTable(Identifier, TableInfo)`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/TableCatalog.html#createTable\(org.apache.spark.sql.connector.catalog.Identifier,org.apache.spark.sql.connector.catalog.TableInfo\)) instead.
[org.apache.spark.sql.connector.catalog.TableCatalog.createTable(Identifier, StructType, Transform[], Map<String, String>)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/TableCatalog.html#createTable\(org.apache.spark.sql.connector.catalog.Identifier,org.apache.spark.sql.types.StructType,org.apache.spark.sql.connector.expressions.Transform%5B%5D,java.util.Map\))
This is deprecated. Please override [`TableCatalog.createTable(Identifier, Column[], Transform[], Map)`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/TableCatalog.html#createTable\(org.apache.spark.sql.connector.catalog.Identifier,org.apache.spark.sql.connector.catalog.Column%5B%5D,org.apache.spark.sql.connector.expressions.Transform%5B%5D,java.util.Map\)) instead.
[org.apache.spark.sql.connector.catalog.TableChange.updateColumnDefaultValue(String[], String)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/TableChange.html#updateColumnDefaultValue\(java.lang.String%5B%5D,java.lang.String\))
Please use [`TableChange.updateColumnDefaultValue(String[], DefaultValue)`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/TableChange.html#updateColumnDefaultValue\(java.lang.String%5B%5D,org.apache.spark.sql.connector.catalog.DefaultValue\)) instead.
[org.apache.spark.sql.connector.catalog.TableChange.UpdateColumnDefaultValue.newDefaultValue()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/TableChange.UpdateColumnDefaultValue.html#newDefaultValue\(\))
Use [`TableChange.UpdateColumnDefaultValue.newCurrentDefault()`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/catalog/TableChange.UpdateColumnDefaultValue.html#newCurrentDefault\(\)) instead.
[org.apache.spark.sql.connector.write.WriteBuilder.buildForBatch()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/write/WriteBuilder.html#buildForBatch\(\))
use [`WriteBuilder.build()`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/write/WriteBuilder.html#build\(\)) instead.
[org.apache.spark.sql.connector.write.WriteBuilder.buildForStreaming()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/write/WriteBuilder.html#buildForStreaming\(\))
use [`WriteBuilder.build()`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/write/WriteBuilder.html#build\(\)) instead.
[org.apache.spark.sql.DataFrameReader.json(JavaRDD<String>)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/DataFrameReader.html#json\(org.apache.spark.api.java.JavaRDD\))
Use json(Dataset[String]) instead. Since 2.2.0.
[org.apache.spark.sql.DataFrameReader.json(RDD<String>)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/DataFrameReader.html#json\(org.apache.spark.rdd.RDD\))
Use json(Dataset[String]) instead. Since 2.2.0.
[org.apache.spark.sql.Dataset.explode(String, String, Function1<A, IterableOnce<B>>, TypeTags.TypeTag<B>)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/Dataset.html#explode\(java.lang.String,java.lang.String,scala.Function1,scala.reflect.api.TypeTags.TypeTag\))
use flatMap() or select() with functions.explode() instead. Since 2.0.0.
[org.apache.spark.sql.Dataset.explode(Seq<Column>, Function1<Row, IterableOnce<A>>, TypeTags.TypeTag<A>)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/Dataset.html#explode\(scala.collection.immutable.Seq,scala.Function1,scala.reflect.api.TypeTags.TypeTag\))
use flatMap() or select() with functions.explode() instead. Since 2.0.0.
[org.apache.spark.sql.Dataset.registerTempTable(String)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/Dataset.html#registerTempTable\(java.lang.String\))
Use createOrReplaceTempView(viewName) instead. Since 2.0.0.
[org.apache.spark.sql.EncoderImplicits.newBooleanSeqEncoder()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/EncoderImplicits.html#newBooleanSeqEncoder\(\))
use [`EncoderImplicits.<T>newSequenceEncoder(scala.reflect.api.TypeTags.TypeTag<T>)`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/EncoderImplicits.html#newSequenceEncoder\(scala.reflect.api.TypeTags.TypeTag\))
[org.apache.spark.sql.EncoderImplicits.newByteSeqEncoder()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/EncoderImplicits.html#newByteSeqEncoder\(\))
use [`EncoderImplicits.<T>newSequenceEncoder(scala.reflect.api.TypeTags.TypeTag<T>)`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/EncoderImplicits.html#newSequenceEncoder\(scala.reflect.api.TypeTags.TypeTag\))
[org.apache.spark.sql.EncoderImplicits.newDoubleSeqEncoder()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/EncoderImplicits.html#newDoubleSeqEncoder\(\))
use [`EncoderImplicits.<T>newSequenceEncoder(scala.reflect.api.TypeTags.TypeTag<T>)`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/EncoderImplicits.html#newSequenceEncoder\(scala.reflect.api.TypeTags.TypeTag\))
[org.apache.spark.sql.EncoderImplicits.newFloatSeqEncoder()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/EncoderImplicits.html#newFloatSeqEncoder\(\))
use [`EncoderImplicits.<T>newSequenceEncoder(scala.reflect.api.TypeTags.TypeTag<T>)`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/EncoderImplicits.html#newSequenceEncoder\(scala.reflect.api.TypeTags.TypeTag\))
[org.apache.spark.sql.EncoderImplicits.newIntSeqEncoder()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/EncoderImplicits.html#newIntSeqEncoder\(\))
use [`EncoderImplicits.<T>newSequenceEncoder(scala.reflect.api.TypeTags.TypeTag<T>)`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/EncoderImplicits.html#newSequenceEncoder\(scala.reflect.api.TypeTags.TypeTag\))
[org.apache.spark.sql.EncoderImplicits.newLongSeqEncoder()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/EncoderImplicits.html#newLongSeqEncoder\(\))
use [`EncoderImplicits.<T>newSequenceEncoder(scala.reflect.api.TypeTags.TypeTag<T>)`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/EncoderImplicits.html#newSequenceEncoder\(scala.reflect.api.TypeTags.TypeTag\))
[org.apache.spark.sql.EncoderImplicits.newProductSeqEncoder(TypeTags.TypeTag<A>)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/EncoderImplicits.html#newProductSeqEncoder\(scala.reflect.api.TypeTags.TypeTag\))
use [`EncoderImplicits.<T>newSequenceEncoder(scala.reflect.api.TypeTags.TypeTag<T>)`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/EncoderImplicits.html#newSequenceEncoder\(scala.reflect.api.TypeTags.TypeTag\))
[org.apache.spark.sql.EncoderImplicits.newShortSeqEncoder()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/EncoderImplicits.html#newShortSeqEncoder\(\))
use [`EncoderImplicits.<T>newSequenceEncoder(scala.reflect.api.TypeTags.TypeTag<T>)`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/EncoderImplicits.html#newSequenceEncoder\(scala.reflect.api.TypeTags.TypeTag\))
[org.apache.spark.sql.EncoderImplicits.newStringSeqEncoder()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/EncoderImplicits.html#newStringSeqEncoder\(\))
use [`EncoderImplicits.<T>newSequenceEncoder(scala.reflect.api.TypeTags.TypeTag<T>)`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/EncoderImplicits.html#newSequenceEncoder\(scala.reflect.api.TypeTags.TypeTag\))
[org.apache.spark.sql.functions.approxCountDistinct(String)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/functions.html#approxCountDistinct\(java.lang.String\))
Use approx_count_distinct. Since 2.1.0.
[org.apache.spark.sql.functions.approxCountDistinct(String, double)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/functions.html#approxCountDistinct\(java.lang.String,double\))
Use approx_count_distinct. Since 2.1.0.
[org.apache.spark.sql.functions.approxCountDistinct(Column)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/functions.html#approxCountDistinct\(org.apache.spark.sql.Column\))
Use approx_count_distinct. Since 2.1.0.
[org.apache.spark.sql.functions.approxCountDistinct(Column, double)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/functions.html#approxCountDistinct\(org.apache.spark.sql.Column,double\))
Use approx_count_distinct. Since 2.1.0.
[org.apache.spark.sql.functions.bitwiseNOT(Column)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/functions.html#bitwiseNOT\(org.apache.spark.sql.Column\))
Use bitwise_not. Since 3.2.0.
[org.apache.spark.sql.functions.callUDF(String, Seq<Column>)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/functions.html#callUDF\(java.lang.String,scala.collection.immutable.Seq\))
Use call_udf.
[org.apache.spark.sql.functions.monotonicallyIncreasingId()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/functions.html#monotonicallyIncreasingId\(\))
Use monotonically_increasing_id(). Since 2.0.0.
[org.apache.spark.sql.functions.shiftLeft(Column, int)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/functions.html#shiftLeft\(org.apache.spark.sql.Column,int\))
Use shiftleft. Since 3.2.0.
[org.apache.spark.sql.functions.shiftRight(Column, int)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/functions.html#shiftRight\(org.apache.spark.sql.Column,int\))
Use shiftright. Since 3.2.0.
[org.apache.spark.sql.functions.shiftRightUnsigned(Column, int)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/functions.html#shiftRightUnsigned\(org.apache.spark.sql.Column,int\))
Use shiftrightunsigned. Since 3.2.0.
[org.apache.spark.sql.functions.sumDistinct(String)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/functions.html#sumDistinct\(java.lang.String\))
Use sum_distinct. Since 3.2.0.
[org.apache.spark.sql.functions.sumDistinct(Column)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/functions.html#sumDistinct\(org.apache.spark.sql.Column\))
Use sum_distinct. Since 3.2.0.
[org.apache.spark.sql.functions.toDegrees(String)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/functions.html#toDegrees\(java.lang.String\))
Use degrees. Since 2.1.0.
[org.apache.spark.sql.functions.toDegrees(Column)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/functions.html#toDegrees\(org.apache.spark.sql.Column\))
Use degrees. Since 2.1.0.
[org.apache.spark.sql.functions.toRadians(String)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/functions.html#toRadians\(java.lang.String\))
Use radians. Since 2.1.0.
[org.apache.spark.sql.functions.toRadians(Column)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/functions.html#toRadians\(org.apache.spark.sql.Column\))
Use radians. Since 2.1.0.
[org.apache.spark.sql.functions.udf(Object, DataType)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/functions.html#udf\(java.lang.Object,org.apache.spark.sql.types.DataType\))
Scala `udf` method with return type parameter is deprecated. Please use Scala `udf` method without return type parameter. Since 3.0.0.
[org.apache.spark.sql.jdbc.JdbcDialect.classifyException(String, Throwable)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/jdbc/JdbcDialect.html#classifyException\(java.lang.String,java.lang.Throwable\))
Please override the classifyException method with an error condition. Since 4.0.0.
[org.apache.spark.sql.jdbc.JdbcDialect.compileAggregate(AggregateFunc)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/jdbc/JdbcDialect.html#compileAggregate\(org.apache.spark.sql.connector.expressions.aggregate.AggregateFunc\))
use org.apache.spark.sql.jdbc.JdbcDialect.compileExpression instead. Since 3.4.0.
[org.apache.spark.sql.jdbc.JdbcDialect.renameTable(String, String)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/jdbc/JdbcDialect.html#renameTable\(java.lang.String,java.lang.String\))
Please override renameTable method with identifiers. Since 3.5.0.
[org.apache.spark.sql.SQLContext.applySchema(JavaRDD<?>, Class<?>)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/SQLContext.html#applySchema\(org.apache.spark.api.java.JavaRDD,java.lang.Class\))
As of 1.3.0, replaced by `createDataFrame()`.
[org.apache.spark.sql.SQLContext.applySchema(JavaRDD<Row>, StructType)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/SQLContext.html#applySchema\(org.apache.spark.api.java.JavaRDD,org.apache.spark.sql.types.StructType\))
As of 1.3.0, replaced by `createDataFrame()`.
[org.apache.spark.sql.SQLContext.applySchema(RDD<?>, Class<?>)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/SQLContext.html#applySchema\(org.apache.spark.rdd.RDD,java.lang.Class\))
As of 1.3.0, replaced by `createDataFrame()`.
[org.apache.spark.sql.SQLContext.applySchema(RDD<Row>, StructType)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/SQLContext.html#applySchema\(org.apache.spark.rdd.RDD,org.apache.spark.sql.types.StructType\))
As of 1.3.0, replaced by `createDataFrame()`.
[org.apache.spark.sql.SQLContext.createExternalTable(String, String)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/SQLContext.html#createExternalTable\(java.lang.String,java.lang.String\))
use sparkSession.catalog.createTable instead. Since 2.2.0.
[org.apache.spark.sql.SQLContext.createExternalTable(String, String, String)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/SQLContext.html#createExternalTable\(java.lang.String,java.lang.String,java.lang.String\))
use sparkSession.catalog.createTable instead. Since 2.2.0.
[org.apache.spark.sql.SQLContext.createExternalTable(String, String, Map<String, String>)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/SQLContext.html#createExternalTable\(java.lang.String,java.lang.String,java.util.Map\))
use sparkSession.catalog.createTable instead. Since 2.2.0.
[org.apache.spark.sql.SQLContext.createExternalTable(String, String, StructType, Map<String, String>)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/SQLContext.html#createExternalTable\(java.lang.String,java.lang.String,org.apache.spark.sql.types.StructType,java.util.Map\))
use sparkSession.catalog.createTable instead. Since 2.2.0.
[org.apache.spark.sql.SQLContext.createExternalTable(String, String, StructType, Map<String, String>)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/SQLContext.html#createExternalTable\(java.lang.String,java.lang.String,org.apache.spark.sql.types.StructType,scala.collection.immutable.Map\))
use sparkSession.catalog.createTable instead. Since 2.2.0.
[org.apache.spark.sql.SQLContext.createExternalTable(String, String, Map<String, String>)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/SQLContext.html#createExternalTable\(java.lang.String,java.lang.String,scala.collection.immutable.Map\))
use sparkSession.catalog.createTable instead. Since 2.2.0.
[org.apache.spark.sql.SQLContext.getOrCreate(SparkContext)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/SQLContext.html#getOrCreate\(org.apache.spark.SparkContext\))
Use SparkSession.builder instead. Since 2.0.0.
[org.apache.spark.sql.SQLContext.jdbc(String, String)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/SQLContext.html#jdbc\(java.lang.String,java.lang.String\))
As of 1.4.0, replaced by `read().jdbc()`.
[org.apache.spark.sql.SQLContext.jdbc(String, String, String[])](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/SQLContext.html#jdbc\(java.lang.String,java.lang.String,java.lang.String%5B%5D\))
As of 1.4.0, replaced by `read().jdbc()`.
[org.apache.spark.sql.SQLContext.jdbc(String, String, String, long, long, int)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/SQLContext.html#jdbc\(java.lang.String,java.lang.String,java.lang.String,long,long,int\))
As of 1.4.0, replaced by `read().jdbc()`.
[org.apache.spark.sql.SQLContext.jsonFile(String)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/SQLContext.html#jsonFile\(java.lang.String\))
As of 1.4.0, replaced by `read().json()`.
[org.apache.spark.sql.SQLContext.jsonFile(String, double)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/SQLContext.html#jsonFile\(java.lang.String,double\))
As of 1.4.0, replaced by `read().json()`.
[org.apache.spark.sql.SQLContext.jsonFile(String, StructType)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/SQLContext.html#jsonFile\(java.lang.String,org.apache.spark.sql.types.StructType\))
As of 1.4.0, replaced by `read().json()`.
[org.apache.spark.sql.SQLContext.jsonRDD(JavaRDD<String>)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/SQLContext.html#jsonRDD\(org.apache.spark.api.java.JavaRDD\))
As of 1.4.0, replaced by `read().json()`.
[org.apache.spark.sql.SQLContext.jsonRDD(JavaRDD<String>, double)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/SQLContext.html#jsonRDD\(org.apache.spark.api.java.JavaRDD,double\))
As of 1.4.0, replaced by `read().json()`.
[org.apache.spark.sql.SQLContext.jsonRDD(JavaRDD<String>, StructType)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/SQLContext.html#jsonRDD\(org.apache.spark.api.java.JavaRDD,org.apache.spark.sql.types.StructType\))
As of 1.4.0, replaced by `read().json()`.
[org.apache.spark.sql.SQLContext.jsonRDD(RDD<String>)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/SQLContext.html#jsonRDD\(org.apache.spark.rdd.RDD\))
As of 1.4.0, replaced by `read().json()`.
[org.apache.spark.sql.SQLContext.jsonRDD(RDD<String>, double)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/SQLContext.html#jsonRDD\(org.apache.spark.rdd.RDD,double\))
As of 1.4.0, replaced by `read().json()`.
[org.apache.spark.sql.SQLContext.jsonRDD(RDD<String>, StructType)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/SQLContext.html#jsonRDD\(org.apache.spark.rdd.RDD,org.apache.spark.sql.types.StructType\))
As of 1.4.0, replaced by `read().json()`.
[org.apache.spark.sql.SQLContext.load(String)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/SQLContext.html#load\(java.lang.String\))
As of 1.4.0, replaced by `read().load(path)`.
[org.apache.spark.sql.SQLContext.load(String, String)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/SQLContext.html#load\(java.lang.String,java.lang.String\))
As of 1.4.0, replaced by `read().format(source).load(path)`.
[org.apache.spark.sql.SQLContext.load(String, Map<String, String>)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/SQLContext.html#load\(java.lang.String,java.util.Map\))
As of 1.4.0, replaced by `read().format(source).options(options).load()`.
[org.apache.spark.sql.SQLContext.load(String, StructType, Map<String, String>)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/SQLContext.html#load\(java.lang.String,org.apache.spark.sql.types.StructType,java.util.Map\))
As of 1.4.0, replaced by `read().format(source).schema(schema).options(options).load()`.
[org.apache.spark.sql.SQLContext.load(String, StructType, Map<String, String>)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/SQLContext.html#load\(java.lang.String,org.apache.spark.sql.types.StructType,scala.collection.immutable.Map\))
As of 1.4.0, replaced by `read().format(source).schema(schema).options(options).load()`.
[org.apache.spark.sql.SQLContext.load(String, Map<String, String>)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/SQLContext.html#load\(java.lang.String,scala.collection.immutable.Map\))
As of 1.4.0, replaced by `read().format(source).options(options).load()`.
[org.apache.spark.sql.SQLContext.parquetFile(String...)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/SQLContext.html#parquetFile\(java.lang.String...\))
As of 1.4.0, replaced by `read().parquet()`.
[org.apache.spark.sql.SQLContext.parquetFile(Seq<String>)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/SQLContext.html#parquetFile\(scala.collection.immutable.Seq\))
As of 1.4.0, replaced by `read().parquet()`.
[org.apache.spark.sql.SQLContextCompanion.clearActive()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/SQLContextCompanion.html#clearActive\(\))
Use SparkSession.clearActiveSession instead. Since 2.0.0.
[org.apache.spark.sql.SQLContextCompanion.getOrCreate(SparkContext)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/SQLContextCompanion.html#getOrCreate\(org.apache.spark.SparkContext\))
Use SparkSession.builder instead. Since 2.0.0.
[org.apache.spark.sql.SQLContextCompanion.setActive(SQLContextCompanion)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/SQLContextCompanion.html#setActive\(org.apache.spark.sql.SQLContextCompanion\))
Use SparkSession.setActiveSession instead. Since 2.0.0.
[org.apache.spark.sql.SQLImplicits.newBooleanSeqEncoder()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/SQLImplicits.html#newBooleanSeqEncoder\(\))
Use newSequenceEncoder instead. Since 2.2.0.
[org.apache.spark.sql.SQLImplicits.newByteSeqEncoder()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/SQLImplicits.html#newByteSeqEncoder\(\))
Use newSequenceEncoder instead. Since 2.2.0.
[org.apache.spark.sql.SQLImplicits.newDoubleSeqEncoder()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/SQLImplicits.html#newDoubleSeqEncoder\(\))
Use newSequenceEncoder instead. Since 2.2.0.
[org.apache.spark.sql.SQLImplicits.newFloatSeqEncoder()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/SQLImplicits.html#newFloatSeqEncoder\(\))
Use newSequenceEncoder instead. Since 2.2.0.
[org.apache.spark.sql.SQLImplicits.newIntSeqEncoder()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/SQLImplicits.html#newIntSeqEncoder\(\))
Use newSequenceEncoder instead. Since 2.2.0.
[org.apache.spark.sql.SQLImplicits.newLongSeqEncoder()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/SQLImplicits.html#newLongSeqEncoder\(\))
Use newSequenceEncoder instead. Since 2.2.0.
[org.apache.spark.sql.SQLImplicits.newShortSeqEncoder()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/SQLImplicits.html#newShortSeqEncoder\(\))
Use newSequenceEncoder instead. Since 2.2.0.
[org.apache.spark.sql.SQLImplicits.newStringSeqEncoder()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/SQLImplicits.html#newStringSeqEncoder\(\))
Use newSequenceEncoder instead. Since 2.2.0.
[org.apache.spark.sql.streaming.StatefulProcessor.implicits.newBooleanSeqEncoder()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/streaming/StatefulProcessor.implicits.html#newBooleanSeqEncoder\(\))
Use newSequenceEncoder instead. Since 2.2.0.
[org.apache.spark.sql.streaming.StatefulProcessor.implicits.newByteSeqEncoder()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/streaming/StatefulProcessor.implicits.html#newByteSeqEncoder\(\))
Use newSequenceEncoder instead. Since 2.2.0.
[org.apache.spark.sql.streaming.StatefulProcessor.implicits.newDoubleSeqEncoder()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/streaming/StatefulProcessor.implicits.html#newDoubleSeqEncoder\(\))
Use newSequenceEncoder instead. Since 2.2.0.
[org.apache.spark.sql.streaming.StatefulProcessor.implicits.newFloatSeqEncoder()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/streaming/StatefulProcessor.implicits.html#newFloatSeqEncoder\(\))
Use newSequenceEncoder instead. Since 2.2.0.
[org.apache.spark.sql.streaming.StatefulProcessor.implicits.newIntSeqEncoder()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/streaming/StatefulProcessor.implicits.html#newIntSeqEncoder\(\))
Use newSequenceEncoder instead. Since 2.2.0.
[org.apache.spark.sql.streaming.StatefulProcessor.implicits.newLongSeqEncoder()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/streaming/StatefulProcessor.implicits.html#newLongSeqEncoder\(\))
Use newSequenceEncoder instead. Since 2.2.0.
[org.apache.spark.sql.streaming.StatefulProcessor.implicits.newShortSeqEncoder()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/streaming/StatefulProcessor.implicits.html#newShortSeqEncoder\(\))
Use newSequenceEncoder instead. Since 2.2.0.
[org.apache.spark.sql.streaming.StatefulProcessor.implicits.newStringSeqEncoder()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/streaming/StatefulProcessor.implicits.html#newStringSeqEncoder\(\))
Use newSequenceEncoder instead. Since 2.2.0.
[org.apache.spark.sql.streaming.StatefulProcessor.implicits$.newBooleanSeqEncoder()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/streaming/StatefulProcessor.implicits$.html#newBooleanSeqEncoder\(\))
Use newSequenceEncoder instead. Since 2.2.0.
[org.apache.spark.sql.streaming.StatefulProcessor.implicits$.newByteSeqEncoder()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/streaming/StatefulProcessor.implicits$.html#newByteSeqEncoder\(\))
Use newSequenceEncoder instead. Since 2.2.0.
[org.apache.spark.sql.streaming.StatefulProcessor.implicits$.newDoubleSeqEncoder()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/streaming/StatefulProcessor.implicits$.html#newDoubleSeqEncoder\(\))
Use newSequenceEncoder instead. Since 2.2.0.
[org.apache.spark.sql.streaming.StatefulProcessor.implicits$.newFloatSeqEncoder()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/streaming/StatefulProcessor.implicits$.html#newFloatSeqEncoder\(\))
Use newSequenceEncoder instead. Since 2.2.0.
[org.apache.spark.sql.streaming.StatefulProcessor.implicits$.newIntSeqEncoder()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/streaming/StatefulProcessor.implicits$.html#newIntSeqEncoder\(\))
Use newSequenceEncoder instead. Since 2.2.0.
[org.apache.spark.sql.streaming.StatefulProcessor.implicits$.newLongSeqEncoder()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/streaming/StatefulProcessor.implicits$.html#newLongSeqEncoder\(\))
Use newSequenceEncoder instead. Since 2.2.0.
[org.apache.spark.sql.streaming.StatefulProcessor.implicits$.newShortSeqEncoder()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/streaming/StatefulProcessor.implicits$.html#newShortSeqEncoder\(\))
Use newSequenceEncoder instead. Since 2.2.0.
[org.apache.spark.sql.streaming.StatefulProcessor.implicits$.newStringSeqEncoder()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/streaming/StatefulProcessor.implicits$.html#newStringSeqEncoder\(\))
Use newSequenceEncoder instead. Since 2.2.0.
[org.apache.spark.sql.streaming.Trigger.Once()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/streaming/Trigger.html#Once\(\))
This is deprecated as of Spark 3.4.0. Use [`Trigger.AvailableNow()`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/streaming/Trigger.html#AvailableNow\(\)) to leverage better guarantee of processing, fine-grained scale of batches, and better gradual processing of watermark advancement including no-data batch. See the NOTES in [`Trigger.AvailableNow()`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/streaming/Trigger.html#AvailableNow\(\)) for details.
[org.apache.spark.sql.UDFRegistration.register(String, UserDefinedAggregateFunction)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/UDFRegistration.html#register\(java.lang.String,org.apache.spark.sql.expressions.UserDefinedAggregateFunction\))
this method and the use of UserDefinedAggregateFunction are deprecated. Aggregator[IN, BUF, OUT] should now be registered as a UDF via the functions.udaf(agg) method.
[org.apache.spark.status.api.v1.ExecutorStageSummary.isBlacklistedForStage()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/api/v1/ExecutorStageSummary.html#isBlacklistedForStage\(\))
use isExcludedForStage instead. Since 3.1.0.
[org.apache.spark.status.api.v1.ExecutorSummary.blacklistedInStages()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/api/v1/ExecutorSummary.html#blacklistedInStages\(\))
use excludedInStages instead. Since 3.1.0.
[org.apache.spark.status.api.v1.ExecutorSummary.isBlacklisted()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/api/v1/ExecutorSummary.html#isBlacklisted\(\))
use isExcluded instead. Since 3.1.0.
[org.apache.spark.status.api.v1.ThreadStackTrace.holdingLocks()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/api/v1/ThreadStackTrace.html#holdingLocks\(\))
using synchronizers and monitors instead. Since 4.0.0.
[org.apache.spark.status.protobuf.StoreTypes.DeterministicLevel.valueOf(int)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.DeterministicLevel.html#valueOf\(int\))
[org.apache.spark.status.protobuf.StoreTypes.ExecutorMetrics.Builder.getMetrics()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.ExecutorMetrics.Builder.html#getMetrics\(\))
[org.apache.spark.status.protobuf.StoreTypes.ExecutorMetrics.Builder.getMutableMetrics()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.ExecutorMetrics.Builder.html#getMutableMetrics\(\))
[org.apache.spark.status.protobuf.StoreTypes.ExecutorMetrics.getMetrics()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.ExecutorMetrics.html#getMetrics\(\))
[org.apache.spark.status.protobuf.StoreTypes.ExecutorMetricsOrBuilder.getMetrics()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.ExecutorMetricsOrBuilder.html#getMetrics\(\))
[org.apache.spark.status.protobuf.StoreTypes.ExecutorSummary.Builder.getAttributes()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.ExecutorSummary.Builder.html#getAttributes\(\))
[org.apache.spark.status.protobuf.StoreTypes.ExecutorSummary.Builder.getExecutorLogs()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.ExecutorSummary.Builder.html#getExecutorLogs\(\))
[org.apache.spark.status.protobuf.StoreTypes.ExecutorSummary.Builder.getMutableAttributes()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.ExecutorSummary.Builder.html#getMutableAttributes\(\))
[org.apache.spark.status.protobuf.StoreTypes.ExecutorSummary.Builder.getMutableExecutorLogs()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.ExecutorSummary.Builder.html#getMutableExecutorLogs\(\))
[org.apache.spark.status.protobuf.StoreTypes.ExecutorSummary.Builder.getMutableResources()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.ExecutorSummary.Builder.html#getMutableResources\(\))
[org.apache.spark.status.protobuf.StoreTypes.ExecutorSummary.Builder.getResources()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.ExecutorSummary.Builder.html#getResources\(\))
[org.apache.spark.status.protobuf.StoreTypes.ExecutorSummary.getAttributes()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.ExecutorSummary.html#getAttributes\(\))
[org.apache.spark.status.protobuf.StoreTypes.ExecutorSummary.getExecutorLogs()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.ExecutorSummary.html#getExecutorLogs\(\))
[org.apache.spark.status.protobuf.StoreTypes.ExecutorSummary.getResources()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.ExecutorSummary.html#getResources\(\))
[org.apache.spark.status.protobuf.StoreTypes.ExecutorSummaryOrBuilder.getAttributes()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.ExecutorSummaryOrBuilder.html#getAttributes\(\))
[org.apache.spark.status.protobuf.StoreTypes.ExecutorSummaryOrBuilder.getExecutorLogs()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.ExecutorSummaryOrBuilder.html#getExecutorLogs\(\))
[org.apache.spark.status.protobuf.StoreTypes.ExecutorSummaryOrBuilder.getResources()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.ExecutorSummaryOrBuilder.html#getResources\(\))
[org.apache.spark.status.protobuf.StoreTypes.JobData.Builder.getKillTasksSummary()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.JobData.Builder.html#getKillTasksSummary\(\))
[org.apache.spark.status.protobuf.StoreTypes.JobData.Builder.getMutableKillTasksSummary()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.JobData.Builder.html#getMutableKillTasksSummary\(\))
[org.apache.spark.status.protobuf.StoreTypes.JobData.getKillTasksSummary()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.JobData.html#getKillTasksSummary\(\))
[org.apache.spark.status.protobuf.StoreTypes.JobDataOrBuilder.getKillTasksSummary()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.JobDataOrBuilder.html#getKillTasksSummary\(\))
[org.apache.spark.status.protobuf.StoreTypes.JobExecutionStatus.valueOf(int)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.JobExecutionStatus.html#valueOf\(int\))
[org.apache.spark.status.protobuf.StoreTypes.ProcessSummary.Builder.getMutableProcessLogs()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.ProcessSummary.Builder.html#getMutableProcessLogs\(\))
[org.apache.spark.status.protobuf.StoreTypes.ProcessSummary.Builder.getProcessLogs()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.ProcessSummary.Builder.html#getProcessLogs\(\))
[org.apache.spark.status.protobuf.StoreTypes.ProcessSummary.getProcessLogs()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.ProcessSummary.html#getProcessLogs\(\))
[org.apache.spark.status.protobuf.StoreTypes.ProcessSummaryOrBuilder.getProcessLogs()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.ProcessSummaryOrBuilder.html#getProcessLogs\(\))
[org.apache.spark.status.protobuf.StoreTypes.ResourceProfileInfo.Builder.getExecutorResources()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.ResourceProfileInfo.Builder.html#getExecutorResources\(\))
[org.apache.spark.status.protobuf.StoreTypes.ResourceProfileInfo.Builder.getMutableExecutorResources()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.ResourceProfileInfo.Builder.html#getMutableExecutorResources\(\))
[org.apache.spark.status.protobuf.StoreTypes.ResourceProfileInfo.Builder.getMutableTaskResources()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.ResourceProfileInfo.Builder.html#getMutableTaskResources\(\))
[org.apache.spark.status.protobuf.StoreTypes.ResourceProfileInfo.Builder.getTaskResources()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.ResourceProfileInfo.Builder.html#getTaskResources\(\))
[org.apache.spark.status.protobuf.StoreTypes.ResourceProfileInfo.getExecutorResources()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.ResourceProfileInfo.html#getExecutorResources\(\))
[org.apache.spark.status.protobuf.StoreTypes.ResourceProfileInfo.getTaskResources()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.ResourceProfileInfo.html#getTaskResources\(\))
[org.apache.spark.status.protobuf.StoreTypes.ResourceProfileInfoOrBuilder.getExecutorResources()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.ResourceProfileInfoOrBuilder.html#getExecutorResources\(\))
[org.apache.spark.status.protobuf.StoreTypes.ResourceProfileInfoOrBuilder.getTaskResources()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.ResourceProfileInfoOrBuilder.html#getTaskResources\(\))
[org.apache.spark.status.protobuf.StoreTypes.SinkProgress.Builder.getMetrics()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.SinkProgress.Builder.html#getMetrics\(\))
[org.apache.spark.status.protobuf.StoreTypes.SinkProgress.Builder.getMutableMetrics()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.SinkProgress.Builder.html#getMutableMetrics\(\))
[org.apache.spark.status.protobuf.StoreTypes.SinkProgress.getMetrics()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.SinkProgress.html#getMetrics\(\))
[org.apache.spark.status.protobuf.StoreTypes.SinkProgressOrBuilder.getMetrics()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.SinkProgressOrBuilder.html#getMetrics\(\))
[org.apache.spark.status.protobuf.StoreTypes.SourceProgress.Builder.getMetrics()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.SourceProgress.Builder.html#getMetrics\(\))
[org.apache.spark.status.protobuf.StoreTypes.SourceProgress.Builder.getMutableMetrics()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.SourceProgress.Builder.html#getMutableMetrics\(\))
[org.apache.spark.status.protobuf.StoreTypes.SourceProgress.getMetrics()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.SourceProgress.html#getMetrics\(\))
[org.apache.spark.status.protobuf.StoreTypes.SourceProgressOrBuilder.getMetrics()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.SourceProgressOrBuilder.html#getMetrics\(\))
[org.apache.spark.status.protobuf.StoreTypes.SparkPlanGraphNodeWrapper.WrapperCase.valueOf(int)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.SparkPlanGraphNodeWrapper.WrapperCase.html#valueOf\(int\))
[org.apache.spark.status.protobuf.StoreTypes.SQLExecutionUIData.Builder.getJobs()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.SQLExecutionUIData.Builder.html#getJobs\(\))
[org.apache.spark.status.protobuf.StoreTypes.SQLExecutionUIData.Builder.getJobsValue()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.SQLExecutionUIData.Builder.html#getJobsValue\(\))
[org.apache.spark.status.protobuf.StoreTypes.SQLExecutionUIData.Builder.getMetricValues()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.SQLExecutionUIData.Builder.html#getMetricValues\(\))
[org.apache.spark.status.protobuf.StoreTypes.SQLExecutionUIData.Builder.getModifiedConfigs()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.SQLExecutionUIData.Builder.html#getModifiedConfigs\(\))
[org.apache.spark.status.protobuf.StoreTypes.SQLExecutionUIData.Builder.getMutableJobs()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.SQLExecutionUIData.Builder.html#getMutableJobs\(\))
[org.apache.spark.status.protobuf.StoreTypes.SQLExecutionUIData.Builder.getMutableJobsValue()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.SQLExecutionUIData.Builder.html#getMutableJobsValue\(\))
[org.apache.spark.status.protobuf.StoreTypes.SQLExecutionUIData.Builder.getMutableMetricValues()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.SQLExecutionUIData.Builder.html#getMutableMetricValues\(\))
[org.apache.spark.status.protobuf.StoreTypes.SQLExecutionUIData.Builder.getMutableModifiedConfigs()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.SQLExecutionUIData.Builder.html#getMutableModifiedConfigs\(\))
[org.apache.spark.status.protobuf.StoreTypes.SQLExecutionUIData.getJobs()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.SQLExecutionUIData.html#getJobs\(\))
[org.apache.spark.status.protobuf.StoreTypes.SQLExecutionUIData.getJobsValue()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.SQLExecutionUIData.html#getJobsValue\(\))
[org.apache.spark.status.protobuf.StoreTypes.SQLExecutionUIData.getMetricValues()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.SQLExecutionUIData.html#getMetricValues\(\))
[org.apache.spark.status.protobuf.StoreTypes.SQLExecutionUIData.getModifiedConfigs()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.SQLExecutionUIData.html#getModifiedConfigs\(\))
[org.apache.spark.status.protobuf.StoreTypes.SQLExecutionUIDataOrBuilder.getJobs()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.SQLExecutionUIDataOrBuilder.html#getJobs\(\))
[org.apache.spark.status.protobuf.StoreTypes.SQLExecutionUIDataOrBuilder.getJobsValue()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.SQLExecutionUIDataOrBuilder.html#getJobsValue\(\))
[org.apache.spark.status.protobuf.StoreTypes.SQLExecutionUIDataOrBuilder.getMetricValues()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.SQLExecutionUIDataOrBuilder.html#getMetricValues\(\))
[org.apache.spark.status.protobuf.StoreTypes.SQLExecutionUIDataOrBuilder.getModifiedConfigs()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.SQLExecutionUIDataOrBuilder.html#getModifiedConfigs\(\))
[org.apache.spark.status.protobuf.StoreTypes.StageData.Builder.getExecutorSummary()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.StageData.Builder.html#getExecutorSummary\(\))
[org.apache.spark.status.protobuf.StoreTypes.StageData.Builder.getKilledTasksSummary()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.StageData.Builder.html#getKilledTasksSummary\(\))
[org.apache.spark.status.protobuf.StoreTypes.StageData.Builder.getMutableExecutorSummary()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.StageData.Builder.html#getMutableExecutorSummary\(\))
[org.apache.spark.status.protobuf.StoreTypes.StageData.Builder.getMutableKilledTasksSummary()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.StageData.Builder.html#getMutableKilledTasksSummary\(\))
[org.apache.spark.status.protobuf.StoreTypes.StageData.Builder.getMutableTasks()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.StageData.Builder.html#getMutableTasks\(\))
[org.apache.spark.status.protobuf.StoreTypes.StageData.Builder.getTasks()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.StageData.Builder.html#getTasks\(\))
[org.apache.spark.status.protobuf.StoreTypes.StageData.getExecutorSummary()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.StageData.html#getExecutorSummary\(\))
[org.apache.spark.status.protobuf.StoreTypes.StageData.getKilledTasksSummary()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.StageData.html#getKilledTasksSummary\(\))
[org.apache.spark.status.protobuf.StoreTypes.StageData.getTasks()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.StageData.html#getTasks\(\))
[org.apache.spark.status.protobuf.StoreTypes.StageDataOrBuilder.getExecutorSummary()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.StageDataOrBuilder.html#getExecutorSummary\(\))
[org.apache.spark.status.protobuf.StoreTypes.StageDataOrBuilder.getKilledTasksSummary()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.StageDataOrBuilder.html#getKilledTasksSummary\(\))
[org.apache.spark.status.protobuf.StoreTypes.StageDataOrBuilder.getTasks()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.StageDataOrBuilder.html#getTasks\(\))
[org.apache.spark.status.protobuf.StoreTypes.StageDataWrapper.Builder.getLocality()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.StageDataWrapper.Builder.html#getLocality\(\))
[org.apache.spark.status.protobuf.StoreTypes.StageDataWrapper.Builder.getMutableLocality()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.StageDataWrapper.Builder.html#getMutableLocality\(\))
[org.apache.spark.status.protobuf.StoreTypes.StageDataWrapper.getLocality()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.StageDataWrapper.html#getLocality\(\))
[org.apache.spark.status.protobuf.StoreTypes.StageDataWrapperOrBuilder.getLocality()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.StageDataWrapperOrBuilder.html#getLocality\(\))
[org.apache.spark.status.protobuf.StoreTypes.StageStatus.valueOf(int)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.StageStatus.html#valueOf\(int\))
[org.apache.spark.status.protobuf.StoreTypes.StateOperatorProgress.Builder.getCustomMetrics()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.StateOperatorProgress.Builder.html#getCustomMetrics\(\))
[org.apache.spark.status.protobuf.StoreTypes.StateOperatorProgress.Builder.getMutableCustomMetrics()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.StateOperatorProgress.Builder.html#getMutableCustomMetrics\(\))
[org.apache.spark.status.protobuf.StoreTypes.StateOperatorProgress.getCustomMetrics()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.StateOperatorProgress.html#getCustomMetrics\(\))
[org.apache.spark.status.protobuf.StoreTypes.StateOperatorProgressOrBuilder.getCustomMetrics()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.StateOperatorProgressOrBuilder.html#getCustomMetrics\(\))
[org.apache.spark.status.protobuf.StoreTypes.StreamingQueryProgress.Builder.getDurationMs()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.StreamingQueryProgress.Builder.html#getDurationMs\(\))
[org.apache.spark.status.protobuf.StoreTypes.StreamingQueryProgress.Builder.getEventTime()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.StreamingQueryProgress.Builder.html#getEventTime\(\))
[org.apache.spark.status.protobuf.StoreTypes.StreamingQueryProgress.Builder.getMutableDurationMs()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.StreamingQueryProgress.Builder.html#getMutableDurationMs\(\))
[org.apache.spark.status.protobuf.StoreTypes.StreamingQueryProgress.Builder.getMutableEventTime()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.StreamingQueryProgress.Builder.html#getMutableEventTime\(\))
[org.apache.spark.status.protobuf.StoreTypes.StreamingQueryProgress.Builder.getMutableObservedMetrics()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.StreamingQueryProgress.Builder.html#getMutableObservedMetrics\(\))
[org.apache.spark.status.protobuf.StoreTypes.StreamingQueryProgress.Builder.getObservedMetrics()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.StreamingQueryProgress.Builder.html#getObservedMetrics\(\))
[org.apache.spark.status.protobuf.StoreTypes.StreamingQueryProgress.getDurationMs()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.StreamingQueryProgress.html#getDurationMs\(\))
[org.apache.spark.status.protobuf.StoreTypes.StreamingQueryProgress.getEventTime()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.StreamingQueryProgress.html#getEventTime\(\))
[org.apache.spark.status.protobuf.StoreTypes.StreamingQueryProgress.getObservedMetrics()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.StreamingQueryProgress.html#getObservedMetrics\(\))
[org.apache.spark.status.protobuf.StoreTypes.StreamingQueryProgressOrBuilder.getDurationMs()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.StreamingQueryProgressOrBuilder.html#getDurationMs\(\))
[org.apache.spark.status.protobuf.StoreTypes.StreamingQueryProgressOrBuilder.getEventTime()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.StreamingQueryProgressOrBuilder.html#getEventTime\(\))
[org.apache.spark.status.protobuf.StoreTypes.StreamingQueryProgressOrBuilder.getObservedMetrics()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.StreamingQueryProgressOrBuilder.html#getObservedMetrics\(\))
[org.apache.spark.status.protobuf.StoreTypes.TaskData.Builder.getExecutorLogs()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.TaskData.Builder.html#getExecutorLogs\(\))
[org.apache.spark.status.protobuf.StoreTypes.TaskData.Builder.getMutableExecutorLogs()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.TaskData.Builder.html#getMutableExecutorLogs\(\))
[org.apache.spark.status.protobuf.StoreTypes.TaskData.getExecutorLogs()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.TaskData.html#getExecutorLogs\(\))
[org.apache.spark.status.protobuf.StoreTypes.TaskDataOrBuilder.getExecutorLogs()](https://spark.apache.org/docs/latest/api/java/org/apache/spark/status/protobuf/StoreTypes.TaskDataOrBuilder.html#getExecutorLogs\(\))

  * Deprecated Constructors
Constructor
Description
[org.apache.spark.sql.connector.expressions.Cast(Expression, DataType)](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/connector/expressions/Cast.html#%3Cinit%3E\(org.apache.spark.sql.connector.expressions.Expression,org.apache.spark.sql.types.DataType\))
