[ ![](https://spark.apache.org/images/spark-logo-rev.svg)](https://spark.apache.org/docs/latest/index.html)4.1.2
  * [Overview](https://spark.apache.org/docs/latest/index.html)
  * [Programming Guides](https://spark.apache.org/docs/latest/ml-pipeline.html)
[Quick Start](https://spark.apache.org/docs/latest/quick-start.html) [RDDs, Accumulators, Broadcasts Vars](https://spark.apache.org/docs/latest/rdd-programming-guide.html) [SQL, DataFrames, and Datasets](https://spark.apache.org/docs/latest/sql-programming-guide.html) [Structured Streaming](https://spark.apache.org/docs/latest/streaming/index.html) [Spark Streaming (DStreams)](https://spark.apache.org/docs/latest/streaming-programming-guide.html) [MLlib (Machine Learning)](https://spark.apache.org/docs/latest/ml-guide.html) [GraphX (Graph Processing)](https://spark.apache.org/docs/latest/graphx-programming-guide.html) [SparkR (R on Spark)](https://spark.apache.org/docs/latest/sparkr.html) [PySpark (Python on Spark)](https://spark.apache.org/docs/latest/api/python/getting_started/index.html) [Declarative Pipelines](https://spark.apache.org/docs/latest/declarative-pipelines-programming-guide.html)
  * [API Docs](https://spark.apache.org/docs/latest/ml-pipeline.html)
[Python](https://spark.apache.org/docs/latest/api/python/index.html) [Scala](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html) [Java](https://spark.apache.org/docs/latest/api/java/index.html) [R](https://spark.apache.org/docs/latest/api/R/index.html) [SQL, Built-in Functions](https://spark.apache.org/docs/latest/api/sql/index.html)
  * [Deploying](https://spark.apache.org/docs/latest/ml-pipeline.html)
[Overview](https://spark.apache.org/docs/latest/cluster-overview.html) [Submitting Applications](https://spark.apache.org/docs/latest/submitting-applications.html) [Spark Standalone](https://spark.apache.org/docs/latest/spark-standalone.html) [YARN](https://spark.apache.org/docs/latest/running-on-yarn.html) [Kubernetes](https://spark.apache.org/docs/latest/running-on-kubernetes.html)
  * [More](https://spark.apache.org/docs/latest/ml-pipeline.html)
[Configuration](https://spark.apache.org/docs/latest/configuration.html) [Monitoring](https://spark.apache.org/docs/latest/monitoring.html) [Tuning Guide](https://spark.apache.org/docs/latest/tuning.html) [Job Scheduling](https://spark.apache.org/docs/latest/job-scheduling.html) [Security](https://spark.apache.org/docs/latest/security.html) [Hardware Provisioning](https://spark.apache.org/docs/latest/hardware-provisioning.html) [Migration Guide](https://spark.apache.org/docs/latest/migration-guide.html) [Building Spark](https://spark.apache.org/docs/latest/building-spark.html) [Contributing to Spark](https://spark.apache.org/contributing.html) [Third Party Projects](https://spark.apache.org/third-party-projects.html)
  *

###  [MLlib: Main Guide](https://spark.apache.org/docs/latest/ml-guide.html)[](https://spark.apache.org/docs/latest/ml-pipeline.html#mllib-main-guide)
  * [ Basic statistics ](https://spark.apache.org/docs/latest/ml-statistics.html)
  * [ Data sources ](https://spark.apache.org/docs/latest/ml-datasource.html)
  * [ Pipelines ](https://spark.apache.org/docs/latest/ml-pipeline.html)
  * [ Extracting, transforming and selecting features ](https://spark.apache.org/docs/latest/ml-features.html)
  * [ Classification and Regression ](https://spark.apache.org/docs/latest/ml-classification-regression.html)
  * [ Clustering ](https://spark.apache.org/docs/latest/ml-clustering.html)
  * [ Collaborative filtering ](https://spark.apache.org/docs/latest/ml-collaborative-filtering.html)
  * [ Frequent Pattern Mining ](https://spark.apache.org/docs/latest/ml-frequent-pattern-mining.html)
  * [ Model selection and tuning ](https://spark.apache.org/docs/latest/ml-tuning.html)
  * [ Advanced topics ](https://spark.apache.org/docs/latest/ml-advanced.html)

###  [MLlib: RDD-based API Guide](https://spark.apache.org/docs/latest/mllib-guide.html)[](https://spark.apache.org/docs/latest/ml-pipeline.html#mllib-rdd-based-api-guide)
  * [ Data types ](https://spark.apache.org/docs/latest/mllib-data-types.html)
  * [ Basic statistics ](https://spark.apache.org/docs/latest/mllib-statistics.html)
  * [ Classification and regression ](https://spark.apache.org/docs/latest/mllib-classification-regression.html)
  * [ Collaborative filtering ](https://spark.apache.org/docs/latest/mllib-collaborative-filtering.html)
  * [ Clustering ](https://spark.apache.org/docs/latest/mllib-clustering.html)
  * [ Dimensionality reduction ](https://spark.apache.org/docs/latest/mllib-dimensionality-reduction.html)
  * [ Feature extraction and transformation ](https://spark.apache.org/docs/latest/mllib-feature-extraction.html)
  * [ Frequent pattern mining ](https://spark.apache.org/docs/latest/mllib-frequent-pattern-mining.html)
  * [ Evaluation metrics ](https://spark.apache.org/docs/latest/mllib-evaluation-metrics.html)
  * [ PMML model export ](https://spark.apache.org/docs/latest/mllib-pmml-model-export.html)
  * [ Optimization (developer) ](https://spark.apache.org/docs/latest/mllib-optimization.html)

# ML Pipelines[](https://spark.apache.org/docs/latest/ml-pipeline.html#ml-pipelines)
`\[ \newcommand{\R}{\mathbb{R}} \newcommand{\E}{\mathbb{E}} \newcommand{\x}{\mathbf{x}} \newcommand{\y}{\mathbf{y}} \newcommand{\wv}{\mathbf{w}} \newcommand{\av}{\mathbf{\alpha}} \newcommand{\bv}{\mathbf{b}} \newcommand{\N}{\mathbb{N}} \newcommand{\id}{\mathbf{I}} \newcommand{\ind}{\mathbf{1}} \newcommand{\0}{\mathbf{0}} \newcommand{\unit}{\mathbf{e}} \newcommand{\one}{\mathbf{1}} \newcommand{\zero}{\mathbf{0}} \]`
In this section, we introduce the concept of **_ML Pipelines_**. ML Pipelines provide a uniform set of high-level APIs built on top of [DataFrames](https://spark.apache.org/docs/latest/sql-programming-guide.html) that help users create and tune practical machine learning pipelines.
**Table of Contents**
  * [Main concepts in Pipelines](https://spark.apache.org/docs/latest/ml-pipeline.html#main-concepts-in-pipelines)
    * [DataFrame](https://spark.apache.org/docs/latest/ml-pipeline.html#dataframe)
    * [Pipeline components](https://spark.apache.org/docs/latest/ml-pipeline.html#pipeline-components)
      * [Transformers](https://spark.apache.org/docs/latest/ml-pipeline.html#transformers)
      * [Estimators](https://spark.apache.org/docs/latest/ml-pipeline.html#estimators)
      * [Properties of pipeline components](https://spark.apache.org/docs/latest/ml-pipeline.html#properties-of-pipeline-components)
    * [Pipeline](https://spark.apache.org/docs/latest/ml-pipeline.html#pipeline)
      * [How it works](https://spark.apache.org/docs/latest/ml-pipeline.html#how-it-works)
      * [Details](https://spark.apache.org/docs/latest/ml-pipeline.html#details)
    * [Parameters](https://spark.apache.org/docs/latest/ml-pipeline.html#parameters)
    * [ML persistence: Saving and Loading Pipelines](https://spark.apache.org/docs/latest/ml-pipeline.html#ml-persistence-saving-and-loading-pipelines)
      * [Backwards compatibility for ML persistence](https://spark.apache.org/docs/latest/ml-pipeline.html#backwards-compatibility-for-ml-persistence)
  * [Code examples](https://spark.apache.org/docs/latest/ml-pipeline.html#code-examples)
    * [Example: Estimator, Transformer, and Param](https://spark.apache.org/docs/latest/ml-pipeline.html#example-estimator-transformer-and-param)
    * [Example: Pipeline](https://spark.apache.org/docs/latest/ml-pipeline.html#example-pipeline)
    * [Model selection (hyperparameter tuning)](https://spark.apache.org/docs/latest/ml-pipeline.html#model-selection-hyperparameter-tuning)

# Main concepts in Pipelines[](https://spark.apache.org/docs/latest/ml-pipeline.html#main-concepts-in-pipelines)
MLlib standardizes APIs for machine learning algorithms to make it easier to combine multiple algorithms into a single pipeline, or workflow. This section covers the key concepts introduced by the Pipelines API, where the pipeline concept is mostly inspired by the [scikit-learn](http://scikit-learn.org/) project.
  * **[`DataFrame`](https://spark.apache.org/docs/latest/ml-pipeline.html#dataframe)**: This ML API uses`DataFrame` from Spark SQL as an ML dataset, which can hold a variety of data types. E.g., a `DataFrame` could have different columns storing text, feature vectors, true labels, and predictions.
  * **[`Transformer`](https://spark.apache.org/docs/latest/ml-pipeline.html#transformers)**: A`Transformer` is an algorithm which can transform one `DataFrame` into another `DataFrame`. E.g., an ML model is a `Transformer` which transforms a `DataFrame` with features into a `DataFrame` with predictions.
  * **[`Estimator`](https://spark.apache.org/docs/latest/ml-pipeline.html#estimators)**: An`Estimator` is an algorithm which can be fit on a `DataFrame` to produce a `Transformer`. E.g., a learning algorithm is an `Estimator` which trains on a `DataFrame` and produces a model.
  * **[`Pipeline`](https://spark.apache.org/docs/latest/ml-pipeline.html#pipeline)**: A`Pipeline` chains multiple `Transformer`s and `Estimator`s together to specify an ML workflow.
  * **[`Parameter`](https://spark.apache.org/docs/latest/ml-pipeline.html#parameters)**: All`Transformer` s and `Estimator`s now share a common API for specifying parameters.

## DataFrame[](https://spark.apache.org/docs/latest/ml-pipeline.html#dataframe)
Machine learning can be applied to a wide variety of data types, such as vectors, text, images, and structured data. This API adopts the `DataFrame` from Spark SQL in order to support a variety of data types.
`DataFrame` supports many basic and structured types; see the [Spark SQL datatype reference](https://spark.apache.org/docs/latest/sql-ref-datatypes.html) for a list of supported types. In addition to the types listed in the Spark SQL guide, `DataFrame` can use ML [`Vector`](https://spark.apache.org/docs/latest/mllib-data-types.html#local-vector) types.
A `DataFrame` can be created either implicitly or explicitly from a regular `RDD`. See the code examples below and the [Spark SQL programming guide](https://spark.apache.org/docs/latest/sql-programming-guide.html) for examples.
Columns in a `DataFrame` are named. The code examples below use names such as “text”, “features”, and “label”.
## Pipeline components[](https://spark.apache.org/docs/latest/ml-pipeline.html#pipeline-components)
### Transformers[](https://spark.apache.org/docs/latest/ml-pipeline.html#transformers)
A `Transformer` is an abstraction that includes feature transformers and learned models. Technically, a `Transformer` implements a method `transform()`, which converts one `DataFrame` into another, generally by appending one or more columns. For example:
  * A feature transformer might take a `DataFrame`, read a column (e.g., text), map it into a new column (e.g., feature vectors), and output a new `DataFrame` with the mapped column appended.
  * A learning model might take a `DataFrame`, read the column containing feature vectors, predict the label for each feature vector, and output a new `DataFrame` with predicted labels appended as a column.

### Estimators[](https://spark.apache.org/docs/latest/ml-pipeline.html#estimators)
An `Estimator` abstracts the concept of a learning algorithm or any algorithm that fits or trains on data. Technically, an `Estimator` implements a method `fit()`, which accepts a `DataFrame` and produces a `Model`, which is a `Transformer`. For example, a learning algorithm such as `LogisticRegression` is an `Estimator`, and calling `fit()` trains a `LogisticRegressionModel`, which is a `Model` and hence a `Transformer`.
### Properties of pipeline components[](https://spark.apache.org/docs/latest/ml-pipeline.html#properties-of-pipeline-components)
`Transformer.transform()`s and `Estimator.fit()`s are both stateless. In the future, stateful algorithms may be supported via alternative concepts.
Each instance of a `Transformer` or `Estimator` has a unique ID, which is useful in specifying parameters (discussed below).
## Pipeline[](https://spark.apache.org/docs/latest/ml-pipeline.html#pipeline)
In machine learning, it is common to run a sequence of algorithms to process and learn from data. E.g., a simple text document processing workflow might include several stages:
  * Split each document’s text into words.
  * Convert each document’s words into a numerical feature vector.
  * Learn a prediction model using the feature vectors and labels.

MLlib represents such a workflow as a `Pipeline`, which consists of a sequence of `PipelineStage`s (`Transformer`s and `Estimator`s) to be run in a specific order. We will use this simple workflow as a running example in this section.
### How it works[](https://spark.apache.org/docs/latest/ml-pipeline.html#how-it-works)
A `Pipeline` is specified as a sequence of stages, and each stage is either a `Transformer` or an `Estimator`. These stages are run in order, and the input `DataFrame` is transformed as it passes through each stage. For `Transformer` stages, the `transform()` method is called on the `DataFrame`. For `Estimator` stages, the `fit()` method is called to produce a `Transformer` (which becomes part of the `PipelineModel`, or fitted `Pipeline`), and that `Transformer`’s `transform()` method is called on the `DataFrame`.
We illustrate this for the simple text document workflow. The figure below is for the _training time_ usage of a `Pipeline`.
![ML Pipeline Example](https://spark.apache.org/docs/latest/img/ml-Pipeline.png)
Above, the top row represents a `Pipeline` with three stages. The first two (`Tokenizer` and `HashingTF`) are `Transformer`s (blue), and the third (`LogisticRegression`) is an `Estimator` (red). The bottom row represents data flowing through the pipeline, where cylinders indicate `DataFrame`s. The `Pipeline.fit()` method is called on the original `DataFrame`, which has raw text documents and labels. The `Tokenizer.transform()` method splits the raw text documents into words, adding a new column with words to the `DataFrame`. The `HashingTF.transform()` method converts the words column into feature vectors, adding a new column with those vectors to the `DataFrame`. Now, since `LogisticRegression` is an `Estimator`, the `Pipeline` first calls `LogisticRegression.fit()` to produce a `LogisticRegressionModel`. If the `Pipeline` had more `Estimator`s, it would call the `LogisticRegressionModel`’s `transform()` method on the `DataFrame` before passing the `DataFrame` to the next stage.
A `Pipeline` is an `Estimator`. Thus, after a `Pipeline`’s `fit()` method runs, it produces a `PipelineModel`, which is a `Transformer`. This `PipelineModel` is used at _test time_ ; the figure below illustrates this usage.
![ML PipelineModel Example](https://spark.apache.org/docs/latest/img/ml-PipelineModel.png)
In the figure above, the `PipelineModel` has the same number of stages as the original `Pipeline`, but all `Estimator`s in the original `Pipeline` have become `Transformer`s. When the `PipelineModel`’s `transform()` method is called on a test dataset, the data are passed through the fitted pipeline in order. Each stage’s `transform()` method updates the dataset and passes it to the next stage.
`Pipeline`s and `PipelineModel`s help to ensure that training and test data go through identical feature processing steps.
### Details[](https://spark.apache.org/docs/latest/ml-pipeline.html#details)
_DAG`Pipeline` s_: A `Pipeline`’s stages are specified as an ordered array. The examples given here are all for linear `Pipeline`s, i.e., `Pipeline`s in which each stage uses data produced by the previous stage. It is possible to create non-linear `Pipeline`s as long as the data flow graph forms a Directed Acyclic Graph (DAG). This graph is currently specified implicitly based on the input and output column names of each stage (generally specified as parameters). If the `Pipeline` forms a DAG, then the stages must be specified in topological order.
_Runtime checking_ : Since `Pipeline`s can operate on `DataFrame`s with varied types, they cannot use compile-time type checking. `Pipeline`s and `PipelineModel`s instead do runtime checking before actually running the `Pipeline`. This type checking is done using the `DataFrame` _schema_ , a description of the data types of columns in the `DataFrame`.
_Unique Pipeline stages_ : A `Pipeline`’s stages should be unique instances. E.g., the same instance `myHashingTF` should not be inserted into the `Pipeline` twice since `Pipeline` stages must have unique IDs. However, different instances `myHashingTF1` and `myHashingTF2` (both of type `HashingTF`) can be put into the same `Pipeline` since different instances will be created with different IDs.
## Parameters[](https://spark.apache.org/docs/latest/ml-pipeline.html#parameters)
MLlib `Estimator`s and `Transformer`s use a uniform API for specifying parameters.
A `Param` is a named parameter with self-contained documentation. A `ParamMap` is a set of (parameter, value) pairs.
There are two main ways to pass parameters to an algorithm:
  1. Set parameters for an instance. E.g., if `lr` is an instance of `LogisticRegression`, one could call `lr.setMaxIter(10)` to make `lr.fit()` use at most 10 iterations. This API resembles the API used in `spark.mllib` package.
  2. Pass a `ParamMap` to `fit()` or `transform()`. Any parameters in the `ParamMap` will override parameters previously specified via setter methods.

Parameters belong to specific instances of `Estimator`s and `Transformer`s. For example, if we have two `LogisticRegression` instances `lr1` and `lr2`, then we can build a `ParamMap` with both `maxIter` parameters specified: `ParamMap(lr1.maxIter -> 10, lr2.maxIter -> 20)`. This is useful if there are two algorithms with the `maxIter` parameter in a `Pipeline`.
## ML persistence: Saving and Loading Pipelines[](https://spark.apache.org/docs/latest/ml-pipeline.html#ml-persistence-saving-and-loading-pipelines)
Often times it is worth it to save a model or a pipeline to disk for later use. In Spark 1.6, a model import/export functionality was added to the Pipeline API. As of Spark 2.3, the DataFrame-based API in `spark.ml` and `pyspark.ml` has complete coverage.
ML persistence works across Scala, Java and Python. However, R currently uses a modified format, so models saved in R can only be loaded back in R; this should be fixed in the future and is tracked in [SPARK-15572](https://issues.apache.org/jira/browse/SPARK-15572).
### Backwards compatibility for ML persistence[](https://spark.apache.org/docs/latest/ml-pipeline.html#backwards-compatibility-for-ml-persistence)
In general, MLlib maintains backwards compatibility for ML persistence. I.e., if you save an ML model or Pipeline in one version of Spark, then you should be able to load it back and use it in a future version of Spark. However, there are rare exceptions, described below.
Model persistence: Is a model or Pipeline saved using Apache Spark ML persistence in Spark version X loadable by Spark version Y?
  * Major versions: No guarantees, but best-effort.
  * Minor and patch versions: Yes; these are backwards compatible.
  * Note about the format: There are no guarantees for a stable persistence format, but model loading itself is designed to be backwards compatible.

Model behavior: Does a model or Pipeline in Spark version X behave identically in Spark version Y?
  * Major versions: No guarantees, but best-effort.
  * Minor and patch versions: Identical behavior, except for bug fixes.

For both model persistence and model behavior, any breaking changes across a minor version or patch version are reported in the Spark version release notes. If a breakage is not reported in release notes, then it should be treated as a bug to be fixed.
# Code examples[](https://spark.apache.org/docs/latest/ml-pipeline.html#code-examples)
This section gives code examples illustrating the functionality discussed above. For more info, please refer to the API documentation ([Python](https://spark.apache.org/docs/latest/api/python/reference/pyspark.ml.html), [Scala](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/package.html), and [Java](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/package-summary.html)).
## Example: Estimator, Transformer, and Param[](https://spark.apache.org/docs/latest/ml-pipeline.html#example-estimator-transformer-and-param)
This example covers the concepts of `Estimator`, `Transformer`, and `Param`.
  * **Python**
  * **Scala**
  * **Java**

Refer to the [`Estimator` Python docs](https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.ml.Estimator.html), the [`Transformer` Python docs](https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.ml.Transformer.html) and the [`Params` Python docs](https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.ml.param.Params.html) for more details on the API.

```
from pyspark.ml.linalg import Vectors
from pyspark.ml.classification import LogisticRegression

# Prepare training data from a list of (label, features) tuples.
training = spark.createDataFrame([
    (1.0, Vectors.dense([0.0, 1.1, 0.1])),
    (0.0, Vectors.dense([2.0, 1.0, -1.0])),
    (0.0, Vectors.dense([2.0, 1.3, 1.0])),
    (1.0, Vectors.dense([0.0, 1.2, -0.5]))], ["label", "features"])

# Create a LogisticRegression instance. This instance is an Estimator.
lr = LogisticRegression(maxIter=10, regParam=0.01)
# Print out the parameters, documentation, and any default values.
print("LogisticRegression parameters:\n" + lr.explainParams() + "\n")

# Learn a LogisticRegression model. This uses the parameters stored in lr.
model1 = lr.fit(training)

# Since model1 is a Model (i.e., a transformer produced by an Estimator),
# we can view the parameters it used during fit().
# This prints the parameter (name: value) pairs, where names are unique IDs for this
# LogisticRegression instance.
print("Model 1 was fit using parameters: ")
print(model1.extractParamMap())

# We may alternatively specify parameters using a Python dictionary as a paramMap
paramMap = {lr.maxIter: 20}
paramMap[lr.maxIter] = 30  # Specify 1 Param, overwriting the original maxIter.
# Specify multiple Params.
paramMap.update({lr.regParam: 0.1, lr.threshold: 0.55})  # type: ignore

# You can combine paramMaps, which are python dictionaries.
# Change output column name
paramMap2 = {lr.probabilityCol: "myProbability"}
paramMapCombined = paramMap.copy()
paramMapCombined.update(paramMap2)  # type: ignore

# Now learn a new model using the paramMapCombined parameters.
# paramMapCombined overrides all parameters set earlier via lr.set* methods.
model2 = lr.fit(training, paramMapCombined)
print("Model 2 was fit using parameters: ")
print(model2.extractParamMap())

# Prepare test data
test = spark.createDataFrame([
    (1.0, Vectors.dense([-1.0, 1.5, 1.3])),
    (0.0, Vectors.dense([3.0, 2.0, -0.1])),
    (1.0, Vectors.dense([0.0, 2.2, -1.5]))], ["label", "features"])

# Make predictions on test data using the Transformer.transform() method.
# LogisticRegression.transform will only use the 'features' column.
# Note that model2.transform() outputs a "myProbability" column instead of the usual
# 'probability' column since we renamed the lr.probabilityCol parameter previously.
prediction = model2.transform(test)
result = prediction.select("features", "label", "myProbability", "prediction") \
    .collect()

for row in result:
    print("features=%s, label=%s -> prob=%s, prediction=%s"
          % (row.features, row.label, row.myProbability, row.prediction))
```

Find full example code at "examples/src/main/python/ml/estimator_transformer_param_example.py" in the Spark repo.
Refer to the [`Estimator` Scala docs](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Estimator.html), the [`Transformer` Scala docs](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Transformer.html) and the [`Params` Scala docs](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/param/Params.html) for details on the API.

```
import org.apache.spark.ml.classification.LogisticRegression
import org.apache.spark.ml.linalg.{Vector, Vectors}
import org.apache.spark.ml.param.ParamMap
import org.apache.spark.sql.Row

// Prepare training data from a list of (label, features) tuples.
val training = spark.createDataFrame(Seq(
  (1.0, Vectors.dense(0.0, 1.1, 0.1)),
  (0.0, Vectors.dense(2.0, 1.0, -1.0)),
  (0.0, Vectors.dense(2.0, 1.3, 1.0)),
  (1.0, Vectors.dense(0.0, 1.2, -0.5))
)).toDF("label", "features")

// Create a LogisticRegression instance. This instance is an Estimator.
val lr = new LogisticRegression()
// Print out the parameters, documentation, and any default values.
println(s"LogisticRegression parameters:\n ${lr.explainParams()}\n")

// We may set parameters using setter methods.
lr.setMaxIter(10)
  .setRegParam(0.01)

// Learn a LogisticRegression model. This uses the parameters stored in lr.
val model1 = lr.fit(training)
// Since model1 is a Model (i.e., a Transformer produced by an Estimator),
// we can view the parameters it used during fit().
// This prints the parameter (name: value) pairs, where names are unique IDs for this
// LogisticRegression instance.
println(s"Model 1 was fit using parameters: ${model1.parent.extractParamMap()}")

// We may alternatively specify parameters using a ParamMap,
// which supports several methods for specifying parameters.
val paramMap = ParamMap(lr.maxIter -> 20)
  .put(lr.maxIter, 30)  // Specify 1 Param. This overwrites the original maxIter.
  .put(lr.regParam -> 0.1, lr.threshold -> 0.55)  // Specify multiple Params.

// One can also combine ParamMaps.
val paramMap2 = ParamMap(lr.probabilityCol -> "myProbability")  // Change output column name.
val paramMapCombined = paramMap ++ paramMap2

// Now learn a new model using the paramMapCombined parameters.
// paramMapCombined overrides all parameters set earlier via lr.set* methods.
val model2 = lr.fit(training, paramMapCombined)
println(s"Model 2 was fit using parameters: ${model2.parent.extractParamMap()}")

// Prepare test data.
val test = spark.createDataFrame(Seq(
  (1.0, Vectors.dense(-1.0, 1.5, 1.3)),
  (0.0, Vectors.dense(3.0, 2.0, -0.1)),
  (1.0, Vectors.dense(0.0, 2.2, -1.5))
)).toDF("label", "features")

// Make predictions on test data using the Transformer.transform() method.
// LogisticRegression.transform will only use the 'features' column.
// Note that model2.transform() outputs a 'myProbability' column instead of the usual
// 'probability' column since we renamed the lr.probabilityCol parameter previously.
model2.transform(test)
  .select("features", "label", "myProbability", "prediction")
  .collect()
  .foreach { case Row(features: Vector, label: Double, prob: Vector, prediction: Double) =>
    println(s"($features, $label) -> prob=$prob, prediction=$prediction")
  }
```

Find full example code at "examples/src/main/scala/org/apache/spark/examples/ml/EstimatorTransformerParamExample.scala" in the Spark repo.
Refer to the [`Estimator` Java docs](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/Estimator.html), the [`Transformer` Java docs](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/Transformer.html) and the [`Params` Java docs](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/param/Params.html) for details on the API.

```
import java.util.Arrays;
import java.util.List;

import org.apache.spark.ml.classification.LogisticRegression;
import org.apache.spark.ml.classification.LogisticRegressionModel;
import org.apache.spark.ml.linalg.VectorUDT;
import org.apache.spark.ml.linalg.Vectors;
import org.apache.spark.ml.param.ParamMap;
import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;
import org.apache.spark.sql.RowFactory;
import org.apache.spark.sql.types.DataTypes;
import org.apache.spark.sql.types.Metadata;
import org.apache.spark.sql.types.StructField;
import org.apache.spark.sql.types.StructType;

// Prepare training data.
List<Row> dataTraining = Arrays.asList(
    RowFactory.create(1.0, Vectors.dense(0.0, 1.1, 0.1)),
    RowFactory.create(0.0, Vectors.dense(2.0, 1.0, -1.0)),
    RowFactory.create(0.0, Vectors.dense(2.0, 1.3, 1.0)),
    RowFactory.create(1.0, Vectors.dense(0.0, 1.2, -0.5))
);
StructType schema = new StructType(new StructField[]{
    new StructField("label", DataTypes.DoubleType, false, Metadata.empty()),
    new StructField("features", new VectorUDT(), false, Metadata.empty())
});
Dataset<Row> training = spark.createDataFrame(dataTraining, schema);

// Create a LogisticRegression instance. This instance is an Estimator.
LogisticRegression lr = new LogisticRegression();
// Print out the parameters, documentation, and any default values.
System.out.println("LogisticRegression parameters:\n" + lr.explainParams() + "\n");

// We may set parameters using setter methods.
lr.setMaxIter(10).setRegParam(0.01);

// Learn a LogisticRegression model. This uses the parameters stored in lr.
LogisticRegressionModel model1 = lr.fit(training);
// Since model1 is a Model (i.e., a Transformer produced by an Estimator),
// we can view the parameters it used during fit().
// This prints the parameter (name: value) pairs, where names are unique IDs for this
// LogisticRegression instance.
System.out.println("Model 1 was fit using parameters: " + model1.parent().extractParamMap());

// We may alternatively specify parameters using a ParamMap.
ParamMap paramMap = new ParamMap()
  .put(lr.maxIter().w(20))  // Specify 1 Param.
  .put(lr.maxIter(), 30)  // This overwrites the original maxIter.
  .put(lr.regParam().w(0.1), lr.threshold().w(0.55));  // Specify multiple Params.

// One can also combine ParamMaps.
ParamMap paramMap2 = new ParamMap()
  .put(lr.probabilityCol().w("myProbability"));  // Change output column name
ParamMap paramMapCombined = paramMap.$plus$plus(paramMap2);

// Now learn a new model using the paramMapCombined parameters.
// paramMapCombined overrides all parameters set earlier via lr.set* methods.
LogisticRegressionModel model2 = lr.fit(training, paramMapCombined);
System.out.println("Model 2 was fit using parameters: " + model2.parent().extractParamMap());

// Prepare test documents.
List<Row> dataTest = Arrays.asList(
    RowFactory.create(1.0, Vectors.dense(-1.0, 1.5, 1.3)),
    RowFactory.create(0.0, Vectors.dense(3.0, 2.0, -0.1)),
    RowFactory.create(1.0, Vectors.dense(0.0, 2.2, -1.5))
);
Dataset<Row> test = spark.createDataFrame(dataTest, schema);

// Make predictions on test documents using the Transformer.transform() method.
// LogisticRegression.transform will only use the 'features' column.
// Note that model2.transform() outputs a 'myProbability' column instead of the usual
// 'probability' column since we renamed the lr.probabilityCol parameter previously.
Dataset<Row> results = model2.transform(test);
Dataset<Row> rows = results.select("features", "label", "myProbability", "prediction");
for (Row r: rows.collectAsList()) {
  System.out.println("(" + r.get(0) + ", " + r.get(1) + ") -> prob=" + r.get(2)
    + ", prediction=" + r.get(3));
}
```

Find full example code at "examples/src/main/java/org/apache/spark/examples/ml/JavaEstimatorTransformerParamExample.java" in the Spark repo.
## Example: Pipeline[](https://spark.apache.org/docs/latest/ml-pipeline.html#example-pipeline)
This example follows the simple text document `Pipeline` illustrated in the figures above.
  * **Python**
  * **Scala**
  * **Java**

Refer to the [`Pipeline` Python docs](https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.ml.Pipeline.html) for more details on the API.

```
from pyspark.ml import Pipeline
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.feature import HashingTF, Tokenizer

# Prepare training documents from a list of (id, text, label) tuples.
training = spark.createDataFrame([
    (0, "a b c d e spark", 1.0),
    (1, "b d", 0.0),
    (2, "spark f g h", 1.0),
    (3, "hadoop mapreduce", 0.0)
], ["id", "text", "label"])

# Configure an ML pipeline, which consists of three stages: tokenizer, hashingTF, and lr.
tokenizer = Tokenizer(inputCol="text", outputCol="words")
hashingTF = HashingTF(inputCol=tokenizer.getOutputCol(), outputCol="features")
lr = LogisticRegression(maxIter=10, regParam=0.001)
pipeline = Pipeline(stages=[tokenizer, hashingTF, lr])

# Fit the pipeline to training documents.
model = pipeline.fit(training)

# Prepare test documents, which are unlabeled (id, text) tuples.
test = spark.createDataFrame([
    (4, "spark i j k"),
    (5, "l m n"),
    (6, "spark hadoop spark"),
    (7, "apache hadoop")
], ["id", "text"])

# Make predictions on test documents and print columns of interest.
prediction = model.transform(test)
selected = prediction.select("id", "text", "probability", "prediction")
for row in selected.collect():
    rid, text, prob, prediction = row
    print(
        "(%d, %s) --> prob=%s, prediction=%f" % (
            rid, text, str(prob), prediction   # type: ignore
        )
    )
```

Find full example code at "examples/src/main/python/ml/pipeline_example.py" in the Spark repo.
Refer to the [`Pipeline` Scala docs](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Pipeline.html) for details on the API.

```
import org.apache.spark.ml.{Pipeline, PipelineModel}
import org.apache.spark.ml.classification.LogisticRegression
import org.apache.spark.ml.feature.{HashingTF, Tokenizer}
import org.apache.spark.ml.linalg.Vector
import org.apache.spark.sql.Row

// Prepare training documents from a list of (id, text, label) tuples.
val training = spark.createDataFrame(Seq(
  (0L, "a b c d e spark", 1.0),
  (1L, "b d", 0.0),
  (2L, "spark f g h", 1.0),
  (3L, "hadoop mapreduce", 0.0)
)).toDF("id", "text", "label")

// Configure an ML pipeline, which consists of three stages: tokenizer, hashingTF, and lr.
val tokenizer = new Tokenizer()
  .setInputCol("text")
  .setOutputCol("words")
val hashingTF = new HashingTF()
  .setNumFeatures(1000)
  .setInputCol(tokenizer.getOutputCol)
  .setOutputCol("features")
val lr = new LogisticRegression()
  .setMaxIter(10)
  .setRegParam(0.001)
val pipeline = new Pipeline()
  .setStages(Array(tokenizer, hashingTF, lr))

// Fit the pipeline to training documents.
val model = pipeline.fit(training)

// Now we can optionally save the fitted pipeline to disk
model.write.overwrite().save("/tmp/spark-logistic-regression-model")

// We can also save this unfit pipeline to disk
pipeline.write.overwrite().save("/tmp/unfit-lr-model")

// And load it back in during production
val sameModel = PipelineModel.load("/tmp/spark-logistic-regression-model")

// Prepare test documents, which are unlabeled (id, text) tuples.
val test = spark.createDataFrame(Seq(
  (4L, "spark i j k"),
  (5L, "l m n"),
  (6L, "spark hadoop spark"),
  (7L, "apache hadoop")
)).toDF("id", "text")

// Make predictions on test documents.
model.transform(test)
  .select("id", "text", "probability", "prediction")
  .collect()
  .foreach { case Row(id: Long, text: String, prob: Vector, prediction: Double) =>
    println(s"($id, $text) --> prob=$prob, prediction=$prediction")
  }
```

Find full example code at "examples/src/main/scala/org/apache/spark/examples/ml/PipelineExample.scala" in the Spark repo.
Refer to the [`Pipeline` Java docs](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/Pipeline.html) for details on the API.

```
import java.util.Arrays;

import org.apache.spark.ml.Pipeline;
import org.apache.spark.ml.PipelineModel;
import org.apache.spark.ml.PipelineStage;
import org.apache.spark.ml.classification.LogisticRegression;
import org.apache.spark.ml.feature.HashingTF;
import org.apache.spark.ml.feature.Tokenizer;
import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;

// Prepare training documents, which are labeled.
Dataset<Row> training = spark.createDataFrame(Arrays.asList(
  new JavaLabeledDocument(0L, "a b c d e spark", 1.0),
  new JavaLabeledDocument(1L, "b d", 0.0),
  new JavaLabeledDocument(2L, "spark f g h", 1.0),
  new JavaLabeledDocument(3L, "hadoop mapreduce", 0.0)
), JavaLabeledDocument.class);

// Configure an ML pipeline, which consists of three stages: tokenizer, hashingTF, and lr.
Tokenizer tokenizer = new Tokenizer()
  .setInputCol("text")
  .setOutputCol("words");
HashingTF hashingTF = new HashingTF()
  .setNumFeatures(1000)
  .setInputCol(tokenizer.getOutputCol())
  .setOutputCol("features");
LogisticRegression lr = new LogisticRegression()
  .setMaxIter(10)
  .setRegParam(0.001);
Pipeline pipeline = new Pipeline()
  .setStages(new PipelineStage[] {tokenizer, hashingTF, lr});

// Fit the pipeline to training documents.
PipelineModel model = pipeline.fit(training);

// Prepare test documents, which are unlabeled.
Dataset<Row> test = spark.createDataFrame(Arrays.asList(
  new JavaDocument(4L, "spark i j k"),
  new JavaDocument(5L, "l m n"),
  new JavaDocument(6L, "spark hadoop spark"),
  new JavaDocument(7L, "apache hadoop")
), JavaDocument.class);

// Make predictions on test documents.
Dataset<Row> predictions = model.transform(test);
for (Row r : predictions.select("id", "text", "probability", "prediction").collectAsList()) {
  System.out.println("(" + r.get(0) + ", " + r.get(1) + ") --> prob=" + r.get(2)
    + ", prediction=" + r.get(3));
}
```

Find full example code at "examples/src/main/java/org/apache/spark/examples/ml/JavaPipelineExample.java" in the Spark repo.
## Model selection (hyperparameter tuning)[](https://spark.apache.org/docs/latest/ml-pipeline.html#model-selection-hyperparameter-tuning)
A big benefit of using ML Pipelines is hyperparameter optimization. See the [ML Tuning Guide](https://spark.apache.org/docs/latest/ml-tuning.html) for more information on automatic model selection.
