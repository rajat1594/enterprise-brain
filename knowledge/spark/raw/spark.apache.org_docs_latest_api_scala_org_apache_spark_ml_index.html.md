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
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/index.html "Permalink") package ml
DataFrame-based machine learning APIs to let users quickly assemble and configure practical machine learning pipelines.
DataFrame-based machine learning APIs to let users quickly assemble and configure practical machine learning pipelines.  

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/attribute/index.html "Permalink") package [attribute](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/attribute/index.html "The ML pipeline API uses DataFrames as ML datasets.")
The ML pipeline API uses `DataFrame`s as ML datasets.
#### ML attributes
The ML pipeline API uses `DataFrame`s as ML datasets. Each dataset consists of typed columns, e.g., string, double, vector, etc. However, knowing only the column type may not be sufficient to handle the data properly. For instance, a double column with values 0.0, 1.0, 2.0, ... may represent some label indices, which cannot be treated as numeric values in ML algorithms, and, for another instance, we may want to know the names and types of features stored in a vector column. ML attributes are used to provide additional information to describe columns in a dataset.
##### ML columns
A column with ML attributes attached is called an ML column. The data in ML columns are stored as double values, i.e., an ML column is either a scalar column of double values or a vector column. Columns of other types must be encoded into ML columns using transformers. We use [Attribute](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/attribute/Attribute.html "org.apache.spark.ml.attribute.Attribute") to describe a scalar ML column, and [AttributeGroup](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/attribute/AttributeGroup.html "org.apache.spark.ml.attribute.AttributeGroup") to describe a vector ML column. ML attributes are stored in the metadata field of the column schema. 
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/classification/index.html "Permalink") package [classification](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/classification/index.html)
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/clustering/index.html "Permalink") package [clustering](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/clustering/index.html)
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/evaluation/index.html "Permalink") package [evaluation](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/evaluation/index.html)
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/feature/index.html "Permalink") package [feature](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/feature/index.html "The ml.feature package provides common feature transformers that help convert raw data or features into more suitable forms for model fitting.")
The `ml.feature` package provides common feature transformers that help convert raw data or features into more suitable forms for model fitting.
####  Feature transformers 
The `ml.feature` package provides common feature transformers that help convert raw data or features into more suitable forms for model fitting. Most feature transformers are implemented as [Transformer](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Transformer.html "org.apache.spark.ml.Transformer")s, which transform one `DataFrame` into another, e.g., [HashingTF](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/feature/HashingTF.html "org.apache.spark.ml.feature.HashingTF"). Some feature transformers are implemented as [Estimator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Estimator.html "org.apache.spark.ml.Estimator")s, because the transformation requires some aggregated information of the dataset, e.g., document frequencies in [IDF](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/feature/IDF.html "org.apache.spark.ml.feature.IDF"). For those feature transformers, calling `Estimator.fit` is required to obtain the model first, e.g., [IDFModel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/feature/IDFModel.html "org.apache.spark.ml.feature.IDFModel"), in order to apply transformation. The transformation is usually done by appending new columns to the input `DataFrame`, so all input columns are carried over.
We try to make each transformer minimal, so it becomes flexible to assemble feature transformation pipelines. [Pipeline](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Pipeline.html "org.apache.spark.ml.Pipeline") can be used to chain feature transformers, and [VectorAssembler](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/feature/VectorAssembler.html "org.apache.spark.ml.feature.VectorAssembler") can be used to combine multiple feature transformations, for example:

```
import org.apache.spark.ml.feature._
import org.apache.spark.ml.Pipeline

// a DataFrame with three columns: id (integer), text (string), and rating (double).
val df = spark.createDataFrame(Seq(
  (0, "Hi I heard about Spark", 3.0),
  (1, "I wish Java could use case classes", 4.0),
  (2, "Logistic regression models are neat", 4.0)
)).toDF("id", "text", "rating")

// define feature transformers
val tok = new RegexTokenizer()
  .setInputCol("text")
  .setOutputCol("words")
val sw = new StopWordsRemover()
  .setInputCol("words")
  .setOutputCol("filtered_words")
val tf = new HashingTF()
  .setInputCol("filtered_words")
  .setOutputCol("tf")
  .setNumFeatures(10000)
val idf = new IDF()
  .setInputCol("tf")
  .setOutputCol("tf_idf")
val assembler = new VectorAssembler()
  .setInputCols(Array("tf_idf", "rating"))
  .setOutputCol("features")

// assemble and fit the feature transformation pipeline
val pipeline = new Pipeline()
  .setStages(Array(tok, sw, tf, idf, assembler))
val model = pipeline.fit(df)

// save transformed features with raw data
model.transform(df)
  .select("id", "text", "rating", "features")
  .write.format("parquet").save("/output/path")
```

Some feature transformers implemented in MLlib are inspired by those implemented in scikit-learn. The major difference is that most scikit-learn feature transformers operate eagerly on the entire input dataset, while MLlib's feature transformers operate lazily on individual columns, which is more efficient and flexible to handle large and complex datasets.  

See also
    
[ scikit-learn.preprocessing](http://scikit-learn.org/stable/modules/preprocessing.html)
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/fpm/index.html "Permalink") package [fpm](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/fpm/index.html)
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/image/index.html "Permalink") package [image](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/image/index.html)
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/linalg/index.html "Permalink") package [linalg](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/linalg/index.html)
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/param/index.html "Permalink") package [param](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/param/index.html)
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/recommendation/index.html "Permalink") package [recommendation](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/recommendation/index.html)
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/regression/index.html "Permalink") package [regression](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/regression/index.html)
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/source/index.html "Permalink") package [source](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/source/index.html)
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/stat/index.html "Permalink") package [stat](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/stat/index.html)
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/tree/index.html "Permalink") package [tree](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/tree/index.html)
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/tuning/index.html "Permalink") package [tuning](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/tuning/index.html)
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/util/index.html "Permalink") package [util](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/util/index.html)
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Estimator.html "Abstract class for estimators that fit models to data.")[Estimator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Estimator.html "Abstract class for estimators that fit models to data.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/FitEnd.html "Event fired after Estimator.fit.")[FitEnd](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/FitEnd.html "Event fired after Estimator.fit.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/FitStart.html "Event fired before Estimator.fit.")[FitStart](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/FitStart.html "Event fired before Estimator.fit.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/LoadInstanceEnd.html "Event fired after MLReader.load.")[LoadInstanceEnd](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/LoadInstanceEnd.html "Event fired after MLReader.load.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/LoadInstanceStart.html "Event fired before MLReader.load.")[LoadInstanceStart](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/LoadInstanceStart.html "Event fired before MLReader.load.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/MLEvent.html "Event emitted by ML operations.")[MLEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/MLEvent.html "Event emitted by ML operations.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Model.html "A fitted model, i.e., a Transformer produced by an Estimator.")[Model](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Model.html "A fitted model, i.e., a Transformer produced by an Estimator.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Pipeline$.html) [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Pipeline.html "A simple pipeline, which acts as an estimator.")[Pipeline](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Pipeline.html "A simple pipeline, which acts as an estimator.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/PipelineModel$.html) [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/PipelineModel.html "Represents a fitted pipeline.")[PipelineModel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/PipelineModel.html "Represents a fitted pipeline.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/PipelineStage.html "A stage in a pipeline, either an Estimator or a Transformer.")[PipelineStage](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/PipelineStage.html "A stage in a pipeline, either an Estimator or a Transformer.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/PredictionModel.html "Abstraction for a model for prediction tasks \(regression and classification\).")[PredictionModel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/PredictionModel.html "Abstraction for a model for prediction tasks \(regression and classification\).")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Predictor.html "Abstraction for prediction problems \(regression and classification\).")[Predictor](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Predictor.html "Abstraction for prediction problems \(regression and classification\).")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/SaveInstanceEnd.html "Event fired after MLWriter.save.")[SaveInstanceEnd](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/SaveInstanceEnd.html "Event fired after MLWriter.save.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/SaveInstanceStart.html "Event fired before MLWriter.save.")[SaveInstanceStart](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/SaveInstanceStart.html "Event fired before MLWriter.save.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/TransformEnd.html "Event fired after Transformer.transform.")[TransformEnd](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/TransformEnd.html "Event fired after Transformer.transform.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/TransformStart.html "Event fired before Transformer.transform.")[TransformStart](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/TransformStart.html "Event fired before Transformer.transform.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Transformer.html "Abstract class for transformers that transform one dataset into another.")[Transformer](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Transformer.html "Abstract class for transformers that transform one dataset into another.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/UnaryTransformer.html "Abstract class for transformers that take one input column, apply transformation, and output the result as a new column.")[UnaryTransformer](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/UnaryTransformer.html "Abstract class for transformers that take one input column, apply transformation, and output the result as a new column.")
  * [](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/functions$.html)[functions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/functions$.html)
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
  * [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html "Permalink") package [sql](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html "Allows the execution of relational queries, including those expressed in SQL using Spark.")
Allows the execution of relational queries, including those expressed in SQL using Spark.
Allows the execution of relational queries, including those expressed in SQL using Spark.  

Definition Classes
    [spark](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html "org.apache.spark")
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
# ml[ __](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/index.html "Permalink")
####  package ml
DataFrame-based machine learning APIs to let users quickly assemble and configure practical machine learning pipelines.  

Source
    [package.scala](https://github.com/apache/spark/tree/v4.1.2/mllib/src/main/scala/org/apache/spark/ml/package.scala)
Linear Supertypes
AnyRef, Any
__ __
Ordering
  1. Alphabetic
  2. By Inheritance


Inherited  

  1. ml
  2. AnyRef
  3. Any


  1. Hide All
  2. Show All


Visibility
  1. Public
  2. Protected


### Package Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/attribute/index.html "Permalink") package [attribute](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/attribute/index.html "The ML pipeline API uses DataFrames as ML datasets.")
The ML pipeline API uses `DataFrame`s as ML datasets.
#### ML attributes
The ML pipeline API uses `DataFrame`s as ML datasets. Each dataset consists of typed columns, e.g., string, double, vector, etc. However, knowing only the column type may not be sufficient to handle the data properly. For instance, a double column with values 0.0, 1.0, 2.0, ... may represent some label indices, which cannot be treated as numeric values in ML algorithms, and, for another instance, we may want to know the names and types of features stored in a vector column. ML attributes are used to provide additional information to describe columns in a dataset.
##### ML columns
A column with ML attributes attached is called an ML column. The data in ML columns are stored as double values, i.e., an ML column is either a scalar column of double values or a vector column. Columns of other types must be encoded into ML columns using transformers. We use [Attribute](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/attribute/Attribute.html "org.apache.spark.ml.attribute.Attribute") to describe a scalar ML column, and [AttributeGroup](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/attribute/AttributeGroup.html "org.apache.spark.ml.attribute.AttributeGroup") to describe a vector ML column. ML attributes are stored in the metadata field of the column schema. 
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/classification/index.html "Permalink") package [classification](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/classification/index.html)
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/clustering/index.html "Permalink") package [clustering](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/clustering/index.html)
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/evaluation/index.html "Permalink") package [evaluation](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/evaluation/index.html)
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/feature/index.html "Permalink") package [feature](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/feature/index.html "The ml.feature package provides common feature transformers that help convert raw data or features into more suitable forms for model fitting.")
The `ml.feature` package provides common feature transformers that help convert raw data or features into more suitable forms for model fitting.
####  Feature transformers 
The `ml.feature` package provides common feature transformers that help convert raw data or features into more suitable forms for model fitting. Most feature transformers are implemented as [Transformer](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Transformer.html "org.apache.spark.ml.Transformer")s, which transform one `DataFrame` into another, e.g., [HashingTF](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/feature/HashingTF.html "org.apache.spark.ml.feature.HashingTF"). Some feature transformers are implemented as [Estimator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Estimator.html "org.apache.spark.ml.Estimator")s, because the transformation requires some aggregated information of the dataset, e.g., document frequencies in [IDF](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/feature/IDF.html "org.apache.spark.ml.feature.IDF"). For those feature transformers, calling `Estimator.fit` is required to obtain the model first, e.g., [IDFModel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/feature/IDFModel.html "org.apache.spark.ml.feature.IDFModel"), in order to apply transformation. The transformation is usually done by appending new columns to the input `DataFrame`, so all input columns are carried over.
We try to make each transformer minimal, so it becomes flexible to assemble feature transformation pipelines. [Pipeline](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Pipeline.html "org.apache.spark.ml.Pipeline") can be used to chain feature transformers, and [VectorAssembler](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/feature/VectorAssembler.html "org.apache.spark.ml.feature.VectorAssembler") can be used to combine multiple feature transformations, for example:

```
import org.apache.spark.ml.feature._
import org.apache.spark.ml.Pipeline

// a DataFrame with three columns: id (integer), text (string), and rating (double).
val df = spark.createDataFrame(Seq(
  (0, "Hi I heard about Spark", 3.0),
  (1, "I wish Java could use case classes", 4.0),
  (2, "Logistic regression models are neat", 4.0)
)).toDF("id", "text", "rating")

// define feature transformers
val tok = new RegexTokenizer()
  .setInputCol("text")
  .setOutputCol("words")
val sw = new StopWordsRemover()
  .setInputCol("words")
  .setOutputCol("filtered_words")
val tf = new HashingTF()
  .setInputCol("filtered_words")
  .setOutputCol("tf")
  .setNumFeatures(10000)
val idf = new IDF()
  .setInputCol("tf")
  .setOutputCol("tf_idf")
val assembler = new VectorAssembler()
  .setInputCols(Array("tf_idf", "rating"))
  .setOutputCol("features")

// assemble and fit the feature transformation pipeline
val pipeline = new Pipeline()
  .setStages(Array(tok, sw, tf, idf, assembler))
val model = pipeline.fit(df)

// save transformed features with raw data
model.transform(df)
  .select("id", "text", "rating", "features")
  .write.format("parquet").save("/output/path")
```

Some feature transformers implemented in MLlib are inspired by those implemented in scikit-learn. The major difference is that most scikit-learn feature transformers operate eagerly on the entire input dataset, while MLlib's feature transformers operate lazily on individual columns, which is more efficient and flexible to handle large and complex datasets.  

See also
    
[ scikit-learn.preprocessing](http://scikit-learn.org/stable/modules/preprocessing.html)
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/fpm/index.html "Permalink") package [fpm](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/fpm/index.html)
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/image/index.html "Permalink") package [image](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/image/index.html)
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/linalg/index.html "Permalink") package [linalg](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/linalg/index.html)
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/param/index.html "Permalink") package [param](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/param/index.html)
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/recommendation/index.html "Permalink") package [recommendation](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/recommendation/index.html)
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/regression/index.html "Permalink") package [regression](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/regression/index.html)
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/source/index.html "Permalink") package [source](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/source/index.html)
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/stat/index.html "Permalink") package [stat](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/stat/index.html)
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/tree/index.html "Permalink") package [tree](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/tree/index.html)
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/tuning/index.html "Permalink") package [tuning](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/tuning/index.html)
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/util/index.html "Permalink") package [util](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/util/index.html)


### Type Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Estimator.html "Permalink") abstract  class [Estimator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Estimator.html "Abstract class for estimators that fit models to data.")[M <: [Model](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Model.html "org.apache.spark.ml.Model")[M]] extends [PipelineStage](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/PipelineStage.html "org.apache.spark.ml.PipelineStage")
Abstract class for estimators that fit models to data.
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/FitEnd.html "Permalink") case class [FitEnd](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/FitEnd.html "Event fired after Estimator.fit.")[M <: [Model](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Model.html "org.apache.spark.ml.Model")[M]]() extends [MLEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/MLEvent.html "org.apache.spark.ml.MLEvent") with Product with Serializable
Event fired after `Estimator.fit`.
Event fired after `Estimator.fit`.  

Annotations
     @Evolving()
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/FitStart.html "Permalink") case class [FitStart](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/FitStart.html "Event fired before Estimator.fit.")[M <: [Model](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Model.html "org.apache.spark.ml.Model")[M]]() extends [MLEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/MLEvent.html "org.apache.spark.ml.MLEvent") with Product with Serializable
Event fired before `Estimator.fit`.
Event fired before `Estimator.fit`.  

Annotations
     @Evolving()
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/LoadInstanceEnd.html "Permalink") case class [LoadInstanceEnd](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/LoadInstanceEnd.html "Event fired after MLReader.load.")[T]() extends [MLEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/MLEvent.html "org.apache.spark.ml.MLEvent") with Product with Serializable
Event fired after `MLReader.load`.
Event fired after `MLReader.load`.  

Annotations
     @Evolving()
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/LoadInstanceStart.html "Permalink") case class [LoadInstanceStart](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/LoadInstanceStart.html "Event fired before MLReader.load.")[T](path: String) extends [MLEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/MLEvent.html "org.apache.spark.ml.MLEvent") with Product with Serializable
Event fired before `MLReader.load`.
Event fired before `MLReader.load`.  

Annotations
     @Evolving()
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/MLEvent.html "Permalink") sealed  trait [MLEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/MLEvent.html "Event emitted by ML operations.") extends [SparkListenerEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html "org.apache.spark.scheduler.SparkListenerEvent")
Event emitted by ML operations.
Event emitted by ML operations. Events are either fired before and/or after each operation (the event should document this).  

Annotations
     @Evolving() 

Note
    
This is supported via [Pipeline](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Pipeline.html "org.apache.spark.ml.Pipeline") and [PipelineModel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/PipelineModel.html "org.apache.spark.ml.PipelineModel").
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Model.html "Permalink") abstract  class [Model](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Model.html "A fitted model, i.e., a Transformer produced by an Estimator.")[M <: [Model](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Model.html "org.apache.spark.ml.Model")[M]] extends [Transformer](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Transformer.html "org.apache.spark.ml.Transformer")
A fitted model, i.e., a [Transformer](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Transformer.html "org.apache.spark.ml.Transformer") produced by an [Estimator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Estimator.html "org.apache.spark.ml.Estimator").
A fitted model, i.e., a [Transformer](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Transformer.html "org.apache.spark.ml.Transformer") produced by an [Estimator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Estimator.html "org.apache.spark.ml.Estimator").  

M
    
model type
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Pipeline.html "Permalink") class [Pipeline](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Pipeline.html "A simple pipeline, which acts as an estimator.") extends [Estimator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Estimator.html "org.apache.spark.ml.Estimator")[[PipelineModel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/PipelineModel.html "org.apache.spark.ml.PipelineModel")] with [MLWritable](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/util/MLWritable.html "org.apache.spark.ml.util.MLWritable")
A simple pipeline, which acts as an estimator.
A simple pipeline, which acts as an estimator. A Pipeline consists of a sequence of stages, each of which is either an [Estimator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Estimator.html "org.apache.spark.ml.Estimator") or a [Transformer](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Transformer.html "org.apache.spark.ml.Transformer"). When `Pipeline.fit` is called, the stages are executed in order. If a stage is an [Estimator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Estimator.html "org.apache.spark.ml.Estimator"), its `Estimator.fit` method will be called on the input dataset to fit a model. Then the model, which is a transformer, will be used to transform the dataset as the input to the next stage. If a stage is a [Transformer](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Transformer.html "org.apache.spark.ml.Transformer"), its `Transformer.transform` method will be called to produce the dataset for the next stage. The fitted model from a [Pipeline](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Pipeline.html "org.apache.spark.ml.Pipeline") is a [PipelineModel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/PipelineModel.html "org.apache.spark.ml.PipelineModel"), which consists of fitted models and transformers, corresponding to the pipeline stages. If there are no stages, the pipeline acts as an identity transformer.  

Annotations
     @Since("1.2.0")
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/PipelineModel.html "Permalink") class [PipelineModel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/PipelineModel.html "Represents a fitted pipeline.") extends [Model](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Model.html "org.apache.spark.ml.Model")[[PipelineModel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/PipelineModel.html "org.apache.spark.ml.PipelineModel")] with [MLWritable](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/util/MLWritable.html "org.apache.spark.ml.util.MLWritable") with Logging
Represents a fitted pipeline.
Represents a fitted pipeline.  

Annotations
     @Since("1.2.0")
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/PipelineStage.html "Permalink") abstract  class [PipelineStage](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/PipelineStage.html "A stage in a pipeline, either an Estimator or a Transformer.") extends [Params](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/param/Params.html "org.apache.spark.ml.param.Params") with Logging
A stage in a pipeline, either an [Estimator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Estimator.html "org.apache.spark.ml.Estimator") or a [Transformer](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Transformer.html "org.apache.spark.ml.Transformer").
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/PredictionModel.html "Permalink") abstract  class [PredictionModel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/PredictionModel.html "Abstraction for a model for prediction tasks \(regression and classification\).")[FeaturesType, M <: [PredictionModel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/PredictionModel.html "org.apache.spark.ml.PredictionModel")[FeaturesType, M]] extends [Model](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Model.html "org.apache.spark.ml.Model")[M] with PredictorParams
Abstraction for a model for prediction tasks (regression and classification).
Abstraction for a model for prediction tasks (regression and classification).  

FeaturesType
    
Type of features. E.g., `VectorUDT` for vector features. 

M
    
Specialization of [PredictionModel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/PredictionModel.html "org.apache.spark.ml.PredictionModel"). If you subclass this type, use this type parameter to specify the concrete type for the corresponding model.
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Predictor.html "Permalink") abstract  class [Predictor](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Predictor.html "Abstraction for prediction problems \(regression and classification\).")[FeaturesType, Learner <: [Predictor](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Predictor.html "org.apache.spark.ml.Predictor")[FeaturesType, Learner, M], M <: [PredictionModel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/PredictionModel.html "org.apache.spark.ml.PredictionModel")[FeaturesType, M]] extends [Estimator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Estimator.html "org.apache.spark.ml.Estimator")[M] with PredictorParams
Abstraction for prediction problems (regression and classification).
Abstraction for prediction problems (regression and classification). It accepts all NumericType labels and will automatically cast it to DoubleType in `fit()`. If this predictor supports weights, it accepts all NumericType weights, which will be automatically casted to DoubleType in `fit()`.  

FeaturesType
    
Type of features. E.g., `VectorUDT` for vector features. 

Learner
    
Specialization of this class. If you subclass this type, use this type parameter to specify the concrete type. 

M
    
Specialization of [PredictionModel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/PredictionModel.html "org.apache.spark.ml.PredictionModel"). If you subclass this type, use this type parameter to specify the concrete type for the corresponding model.
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/SaveInstanceEnd.html "Permalink") case class [SaveInstanceEnd](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/SaveInstanceEnd.html "Event fired after MLWriter.save.")(path: String) extends [MLEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/MLEvent.html "org.apache.spark.ml.MLEvent") with Product with Serializable
Event fired after `MLWriter.save`.
Event fired after `MLWriter.save`.  

Annotations
     @Evolving()
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/SaveInstanceStart.html "Permalink") case class [SaveInstanceStart](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/SaveInstanceStart.html "Event fired before MLWriter.save.")(path: String) extends [MLEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/MLEvent.html "org.apache.spark.ml.MLEvent") with Product with Serializable
Event fired before `MLWriter.save`.
Event fired before `MLWriter.save`.  

Annotations
     @Evolving()
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/TransformEnd.html "Permalink") case class [TransformEnd](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/TransformEnd.html "Event fired after Transformer.transform.")() extends [MLEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/MLEvent.html "org.apache.spark.ml.MLEvent") with Product with Serializable
Event fired after `Transformer.transform`.
Event fired after `Transformer.transform`.  

Annotations
     @Evolving()
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/TransformStart.html "Permalink") case class [TransformStart](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/TransformStart.html "Event fired before Transformer.transform.")() extends [MLEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/MLEvent.html "org.apache.spark.ml.MLEvent") with Product with Serializable
Event fired before `Transformer.transform`.
Event fired before `Transformer.transform`.  

Annotations
     @Evolving()
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Transformer.html "Permalink") abstract  class [Transformer](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Transformer.html "Abstract class for transformers that transform one dataset into another.") extends [PipelineStage](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/PipelineStage.html "org.apache.spark.ml.PipelineStage")
Abstract class for transformers that transform one dataset into another.
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/UnaryTransformer.html "Permalink") abstract  class [UnaryTransformer](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/UnaryTransformer.html "Abstract class for transformers that take one input column, apply transformation, and output the result as a new column.")[IN, OUT, T <: [UnaryTransformer](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/UnaryTransformer.html "org.apache.spark.ml.UnaryTransformer")[IN, OUT, T]] extends [Transformer](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Transformer.html "org.apache.spark.ml.Transformer") with [HasInputCol](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/param/shared/HasInputCol.html "org.apache.spark.ml.param.shared.HasInputCol") with [HasOutputCol](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/param/shared/HasOutputCol.html "org.apache.spark.ml.param.shared.HasOutputCol") with Logging
Abstract class for transformers that take one input column, apply transformation, and output the result as a new column.


### Value Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Pipeline$.html "Permalink") object [Pipeline](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Pipeline$.html) extends [MLReadable](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/util/MLReadable.html "org.apache.spark.ml.util.MLReadable")[[Pipeline](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Pipeline.html "org.apache.spark.ml.Pipeline")] with [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable") 

Annotations
     @Since("1.6.0")
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/PipelineModel$.html "Permalink") object [PipelineModel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/PipelineModel$.html) extends [MLReadable](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/util/MLReadable.html "org.apache.spark.ml.util.MLReadable")[[PipelineModel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/PipelineModel.html "org.apache.spark.ml.PipelineModel")] with [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable") 

Annotations
     @Since("1.6.0")
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/functions$.html "Permalink") object [functions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/functions$.html) 

Annotations
     @Since("3.0.0")


### Members
  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Estimator.html "Permalink") abstract  class [Estimator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Estimator.html "Abstract class for estimators that fit models to data.")[M <: [Model](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Model.html "org.apache.spark.ml.Model")[M]] extends [PipelineStage](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/PipelineStage.html "org.apache.spark.ml.PipelineStage")
Abstract class for estimators that fit models to data.
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/FitEnd.html "Permalink") case class [FitEnd](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/FitEnd.html "Event fired after Estimator.fit.")[M <: [Model](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Model.html "org.apache.spark.ml.Model")[M]]() extends [MLEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/MLEvent.html "org.apache.spark.ml.MLEvent") with Product with Serializable
Event fired after `Estimator.fit`.
Event fired after `Estimator.fit`.  

Annotations
     @Evolving()
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/FitStart.html "Permalink") case class [FitStart](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/FitStart.html "Event fired before Estimator.fit.")[M <: [Model](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Model.html "org.apache.spark.ml.Model")[M]]() extends [MLEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/MLEvent.html "org.apache.spark.ml.MLEvent") with Product with Serializable
Event fired before `Estimator.fit`.
Event fired before `Estimator.fit`.  

Annotations
     @Evolving()
  4. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/LoadInstanceEnd.html "Permalink") case class [LoadInstanceEnd](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/LoadInstanceEnd.html "Event fired after MLReader.load.")[T]() extends [MLEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/MLEvent.html "org.apache.spark.ml.MLEvent") with Product with Serializable
Event fired after `MLReader.load`.
Event fired after `MLReader.load`.  

Annotations
     @Evolving()
  5. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/LoadInstanceStart.html "Permalink") case class [LoadInstanceStart](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/LoadInstanceStart.html "Event fired before MLReader.load.")[T](path: String) extends [MLEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/MLEvent.html "org.apache.spark.ml.MLEvent") with Product with Serializable
Event fired before `MLReader.load`.
Event fired before `MLReader.load`.  

Annotations
     @Evolving()
  6. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/MLEvent.html "Permalink") sealed  trait [MLEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/MLEvent.html "Event emitted by ML operations.") extends [SparkListenerEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/scheduler/SparkListenerEvent.html "org.apache.spark.scheduler.SparkListenerEvent")
Event emitted by ML operations.
Event emitted by ML operations. Events are either fired before and/or after each operation (the event should document this).  

Annotations
     @Evolving() 

Note
    
This is supported via [Pipeline](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Pipeline.html "org.apache.spark.ml.Pipeline") and [PipelineModel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/PipelineModel.html "org.apache.spark.ml.PipelineModel").
  7. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Model.html "Permalink") abstract  class [Model](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Model.html "A fitted model, i.e., a Transformer produced by an Estimator.")[M <: [Model](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Model.html "org.apache.spark.ml.Model")[M]] extends [Transformer](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Transformer.html "org.apache.spark.ml.Transformer")
A fitted model, i.e., a [Transformer](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Transformer.html "org.apache.spark.ml.Transformer") produced by an [Estimator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Estimator.html "org.apache.spark.ml.Estimator").
A fitted model, i.e., a [Transformer](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Transformer.html "org.apache.spark.ml.Transformer") produced by an [Estimator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Estimator.html "org.apache.spark.ml.Estimator").  

M
    
model type
  8. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Pipeline.html "Permalink") class [Pipeline](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Pipeline.html "A simple pipeline, which acts as an estimator.") extends [Estimator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Estimator.html "org.apache.spark.ml.Estimator")[[PipelineModel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/PipelineModel.html "org.apache.spark.ml.PipelineModel")] with [MLWritable](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/util/MLWritable.html "org.apache.spark.ml.util.MLWritable")
A simple pipeline, which acts as an estimator.
A simple pipeline, which acts as an estimator. A Pipeline consists of a sequence of stages, each of which is either an [Estimator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Estimator.html "org.apache.spark.ml.Estimator") or a [Transformer](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Transformer.html "org.apache.spark.ml.Transformer"). When `Pipeline.fit` is called, the stages are executed in order. If a stage is an [Estimator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Estimator.html "org.apache.spark.ml.Estimator"), its `Estimator.fit` method will be called on the input dataset to fit a model. Then the model, which is a transformer, will be used to transform the dataset as the input to the next stage. If a stage is a [Transformer](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Transformer.html "org.apache.spark.ml.Transformer"), its `Transformer.transform` method will be called to produce the dataset for the next stage. The fitted model from a [Pipeline](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Pipeline.html "org.apache.spark.ml.Pipeline") is a [PipelineModel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/PipelineModel.html "org.apache.spark.ml.PipelineModel"), which consists of fitted models and transformers, corresponding to the pipeline stages. If there are no stages, the pipeline acts as an identity transformer.  

Annotations
     @Since("1.2.0")
  9. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/PipelineModel.html "Permalink") class [PipelineModel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/PipelineModel.html "Represents a fitted pipeline.") extends [Model](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Model.html "org.apache.spark.ml.Model")[[PipelineModel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/PipelineModel.html "org.apache.spark.ml.PipelineModel")] with [MLWritable](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/util/MLWritable.html "org.apache.spark.ml.util.MLWritable") with Logging
Represents a fitted pipeline.
Represents a fitted pipeline.  

Annotations
     @Since("1.2.0")
  10. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/PipelineStage.html "Permalink") abstract  class [PipelineStage](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/PipelineStage.html "A stage in a pipeline, either an Estimator or a Transformer.") extends [Params](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/param/Params.html "org.apache.spark.ml.param.Params") with Logging
A stage in a pipeline, either an [Estimator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Estimator.html "org.apache.spark.ml.Estimator") or a [Transformer](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Transformer.html "org.apache.spark.ml.Transformer").
  11. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/PredictionModel.html "Permalink") abstract  class [PredictionModel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/PredictionModel.html "Abstraction for a model for prediction tasks \(regression and classification\).")[FeaturesType, M <: [PredictionModel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/PredictionModel.html "org.apache.spark.ml.PredictionModel")[FeaturesType, M]] extends [Model](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Model.html "org.apache.spark.ml.Model")[M] with PredictorParams
Abstraction for a model for prediction tasks (regression and classification).
Abstraction for a model for prediction tasks (regression and classification).  

FeaturesType
    
Type of features. E.g., `VectorUDT` for vector features. 

M
    
Specialization of [PredictionModel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/PredictionModel.html "org.apache.spark.ml.PredictionModel"). If you subclass this type, use this type parameter to specify the concrete type for the corresponding model.
  12. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Predictor.html "Permalink") abstract  class [Predictor](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Predictor.html "Abstraction for prediction problems \(regression and classification\).")[FeaturesType, Learner <: [Predictor](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Predictor.html "org.apache.spark.ml.Predictor")[FeaturesType, Learner, M], M <: [PredictionModel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/PredictionModel.html "org.apache.spark.ml.PredictionModel")[FeaturesType, M]] extends [Estimator](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Estimator.html "org.apache.spark.ml.Estimator")[M] with PredictorParams
Abstraction for prediction problems (regression and classification).
Abstraction for prediction problems (regression and classification). It accepts all NumericType labels and will automatically cast it to DoubleType in `fit()`. If this predictor supports weights, it accepts all NumericType weights, which will be automatically casted to DoubleType in `fit()`.  

FeaturesType
    
Type of features. E.g., `VectorUDT` for vector features. 

Learner
    
Specialization of this class. If you subclass this type, use this type parameter to specify the concrete type. 

M
    
Specialization of [PredictionModel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/PredictionModel.html "org.apache.spark.ml.PredictionModel"). If you subclass this type, use this type parameter to specify the concrete type for the corresponding model.
  13. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/SaveInstanceEnd.html "Permalink") case class [SaveInstanceEnd](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/SaveInstanceEnd.html "Event fired after MLWriter.save.")(path: String) extends [MLEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/MLEvent.html "org.apache.spark.ml.MLEvent") with Product with Serializable
Event fired after `MLWriter.save`.
Event fired after `MLWriter.save`.  

Annotations
     @Evolving()
  14. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/SaveInstanceStart.html "Permalink") case class [SaveInstanceStart](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/SaveInstanceStart.html "Event fired before MLWriter.save.")(path: String) extends [MLEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/MLEvent.html "org.apache.spark.ml.MLEvent") with Product with Serializable
Event fired before `MLWriter.save`.
Event fired before `MLWriter.save`.  

Annotations
     @Evolving()
  15. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/TransformEnd.html "Permalink") case class [TransformEnd](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/TransformEnd.html "Event fired after Transformer.transform.")() extends [MLEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/MLEvent.html "org.apache.spark.ml.MLEvent") with Product with Serializable
Event fired after `Transformer.transform`.
Event fired after `Transformer.transform`.  

Annotations
     @Evolving()
  16. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/TransformStart.html "Permalink") case class [TransformStart](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/TransformStart.html "Event fired before Transformer.transform.")() extends [MLEvent](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/MLEvent.html "org.apache.spark.ml.MLEvent") with Product with Serializable
Event fired before `Transformer.transform`.
Event fired before `Transformer.transform`.  

Annotations
     @Evolving()
  17. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Transformer.html "Permalink") abstract  class [Transformer](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Transformer.html "Abstract class for transformers that transform one dataset into another.") extends [PipelineStage](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/PipelineStage.html "org.apache.spark.ml.PipelineStage")
Abstract class for transformers that transform one dataset into another.
  18. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/UnaryTransformer.html "Permalink") abstract  class [UnaryTransformer](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/UnaryTransformer.html "Abstract class for transformers that take one input column, apply transformation, and output the result as a new column.")[IN, OUT, T <: [UnaryTransformer](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/UnaryTransformer.html "org.apache.spark.ml.UnaryTransformer")[IN, OUT, T]] extends [Transformer](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Transformer.html "org.apache.spark.ml.Transformer") with [HasInputCol](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/param/shared/HasInputCol.html "org.apache.spark.ml.param.shared.HasInputCol") with [HasOutputCol](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/param/shared/HasOutputCol.html "org.apache.spark.ml.param.shared.HasOutputCol") with Logging
Abstract class for transformers that take one input column, apply transformation, and output the result as a new column.


  1. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Pipeline$.html "Permalink") object [Pipeline](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Pipeline$.html) extends [MLReadable](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/util/MLReadable.html "org.apache.spark.ml.util.MLReadable")[[Pipeline](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Pipeline.html "org.apache.spark.ml.Pipeline")] with [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable") 

Annotations
     @Since("1.6.0")
  2. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/PipelineModel$.html "Permalink") object [PipelineModel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/PipelineModel$.html) extends [MLReadable](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/util/MLReadable.html "org.apache.spark.ml.util.MLReadable")[[PipelineModel](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/PipelineModel.html "org.apache.spark.ml.PipelineModel")] with [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html#java.io.Serializable "java.io.Serializable") 

Annotations
     @Since("1.6.0")
  3. [__](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/functions$.html "Permalink") object [functions](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/functions$.html) 

Annotations
     @Since("3.0.0")


