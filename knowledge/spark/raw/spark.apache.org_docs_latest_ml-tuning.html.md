[ ![](https://spark.apache.org/images/spark-logo-rev.svg)](https://spark.apache.org/docs/latest/index.html)4.1.2
  * [Overview](https://spark.apache.org/docs/latest/index.html)
  * [Programming Guides](https://spark.apache.org/docs/latest/ml-tuning.html)
[Quick Start](https://spark.apache.org/docs/latest/quick-start.html) [RDDs, Accumulators, Broadcasts Vars](https://spark.apache.org/docs/latest/rdd-programming-guide.html) [SQL, DataFrames, and Datasets](https://spark.apache.org/docs/latest/sql-programming-guide.html) [Structured Streaming](https://spark.apache.org/docs/latest/streaming/index.html) [Spark Streaming (DStreams)](https://spark.apache.org/docs/latest/streaming-programming-guide.html) [MLlib (Machine Learning)](https://spark.apache.org/docs/latest/ml-guide.html) [GraphX (Graph Processing)](https://spark.apache.org/docs/latest/graphx-programming-guide.html) [SparkR (R on Spark)](https://spark.apache.org/docs/latest/sparkr.html) [PySpark (Python on Spark)](https://spark.apache.org/docs/latest/api/python/getting_started/index.html) [Declarative Pipelines](https://spark.apache.org/docs/latest/declarative-pipelines-programming-guide.html)
  * [API Docs](https://spark.apache.org/docs/latest/ml-tuning.html)
[Python](https://spark.apache.org/docs/latest/api/python/index.html) [Scala](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html) [Java](https://spark.apache.org/docs/latest/api/java/index.html) [R](https://spark.apache.org/docs/latest/api/R/index.html) [SQL, Built-in Functions](https://spark.apache.org/docs/latest/api/sql/index.html)
  * [Deploying](https://spark.apache.org/docs/latest/ml-tuning.html)
[Overview](https://spark.apache.org/docs/latest/cluster-overview.html) [Submitting Applications](https://spark.apache.org/docs/latest/submitting-applications.html) [Spark Standalone](https://spark.apache.org/docs/latest/spark-standalone.html) [YARN](https://spark.apache.org/docs/latest/running-on-yarn.html) [Kubernetes](https://spark.apache.org/docs/latest/running-on-kubernetes.html)
  * [More](https://spark.apache.org/docs/latest/ml-tuning.html)
[Configuration](https://spark.apache.org/docs/latest/configuration.html) [Monitoring](https://spark.apache.org/docs/latest/monitoring.html) [Tuning Guide](https://spark.apache.org/docs/latest/tuning.html) [Job Scheduling](https://spark.apache.org/docs/latest/job-scheduling.html) [Security](https://spark.apache.org/docs/latest/security.html) [Hardware Provisioning](https://spark.apache.org/docs/latest/hardware-provisioning.html) [Migration Guide](https://spark.apache.org/docs/latest/migration-guide.html) [Building Spark](https://spark.apache.org/docs/latest/building-spark.html) [Contributing to Spark](https://spark.apache.org/contributing.html) [Third Party Projects](https://spark.apache.org/third-party-projects.html)
  * 

###  [MLlib: Main Guide](https://spark.apache.org/docs/latest/ml-guide.html)[](https://spark.apache.org/docs/latest/ml-tuning.html#mllib-main-guide)
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


###  [MLlib: RDD-based API Guide](https://spark.apache.org/docs/latest/mllib-guide.html)[](https://spark.apache.org/docs/latest/ml-tuning.html#mllib-rdd-based-api-guide)
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


# ML Tuning: model selection and hyperparameter tuning[](https://spark.apache.org/docs/latest/ml-tuning.html#ml-tuning-model-selection-and-hyperparameter-tuning)
`\[ \newcommand{\R}{\mathbb{R}} \newcommand{\E}{\mathbb{E}} \newcommand{\x}{\mathbf{x}} \newcommand{\y}{\mathbf{y}} \newcommand{\wv}{\mathbf{w}} \newcommand{\av}{\mathbf{\alpha}} \newcommand{\bv}{\mathbf{b}} \newcommand{\N}{\mathbb{N}} \newcommand{\id}{\mathbf{I}} \newcommand{\ind}{\mathbf{1}} \newcommand{\0}{\mathbf{0}} \newcommand{\unit}{\mathbf{e}} \newcommand{\one}{\mathbf{1}} \newcommand{\zero}{\mathbf{0}} \]`
This section describes how to use MLlib’s tooling for tuning ML algorithms and Pipelines. Built-in Cross-Validation and other tooling allow users to optimize hyperparameters in algorithms and Pipelines.
**Table of contents**
  * [Model selection (a.k.a. hyperparameter tuning)](https://spark.apache.org/docs/latest/ml-tuning.html#model-selection-aka-hyperparameter-tuning)
  * [Cross-Validation](https://spark.apache.org/docs/latest/ml-tuning.html#cross-validation)
  * [Train-Validation Split](https://spark.apache.org/docs/latest/ml-tuning.html#train-validation-split)


# Model selection (a.k.a. hyperparameter tuning)[](https://spark.apache.org/docs/latest/ml-tuning.html#model-selection-aka-hyperparameter-tuning)
An important task in ML is _model selection_ , or using data to find the best model or parameters for a given task. This is also called _tuning_. Tuning may be done for individual `Estimator`s such as `LogisticRegression`, or for entire `Pipeline`s which include multiple algorithms, featurization, and other steps. Users can tune an entire `Pipeline` at once, rather than tuning each element in the `Pipeline` separately.
MLlib supports model selection using tools such as [`CrossValidator`](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/tuning/CrossValidator.html) and [`TrainValidationSplit`](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/tuning/TrainValidationSplit.html). These tools require the following items:
  * [`Estimator`](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/Estimator.html): algorithm or `Pipeline` to tune
  * Set of `ParamMap`s: parameters to choose from, sometimes called a “parameter grid” to search over
  * [`Evaluator`](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/evaluation/Evaluator.html): metric to measure how well a fitted `Model` does on held-out test data


At a high level, these model selection tools work as follows:
  * They split the input data into separate training and test datasets.
  * For each (training, test) pair, they iterate through the set of `ParamMap`s: 
    * For each `ParamMap`, they fit the `Estimator` using those parameters, get the fitted `Model`, and evaluate the `Model`’s performance using the `Evaluator`.
  * They select the `Model` produced by the best-performing set of parameters.


The `Evaluator` can be a [`RegressionEvaluator`](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/evaluation/RegressionEvaluator.html) for regression problems, a [`BinaryClassificationEvaluator`](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/evaluation/BinaryClassificationEvaluator.html) for binary data, a [`MulticlassClassificationEvaluator`](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/evaluation/MulticlassClassificationEvaluator.html) for multiclass problems, a [`MultilabelClassificationEvaluator`](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/evaluation/MultilabelClassificationEvaluator.html) for multi-label classifications, or a [`RankingEvaluator`](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/evaluation/RankingEvaluator.html) for ranking problems. The default metric used to choose the best `ParamMap` can be overridden by the `setMetricName` method in each of these evaluators.
To help construct the parameter grid, users can use the [`ParamGridBuilder`](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/tuning/ParamGridBuilder.html) utility. By default, sets of parameters from the parameter grid are evaluated in serial. Parameter evaluation can be done in parallel by setting `parallelism` with a value of 2 or more (a value of 1 will be serial) before running model selection with `CrossValidator` or `TrainValidationSplit`. The value of `parallelism` should be chosen carefully to maximize parallelism without exceeding cluster resources, and larger values may not always lead to improved performance. Generally speaking, a value up to 10 should be sufficient for most clusters.
# Cross-Validation[](https://spark.apache.org/docs/latest/ml-tuning.html#cross-validation)
`CrossValidator` begins by splitting the dataset into a set of _folds_ which are used as separate training and test datasets. E.g., with `$k=3$` folds, `CrossValidator` will generate 3 (training, test) dataset pairs, each of which uses 2/3 of the data for training and 1/3 for testing. To evaluate a particular `ParamMap`, `CrossValidator` computes the average evaluation metric for the 3 `Model`s produced by fitting the `Estimator` on the 3 different (training, test) dataset pairs.
After identifying the best `ParamMap`, `CrossValidator` finally re-fits the `Estimator` using the best `ParamMap` and the entire dataset.
**Examples: model selection via cross-validation**
The following example demonstrates using `CrossValidator` to select from a grid of parameters.
Note that cross-validation over a grid of parameters is expensive. E.g., in the example below, the parameter grid has 3 values for `hashingTF.numFeatures` and 2 values for `lr.regParam`, and `CrossValidator` uses 2 folds. This multiplies out to `$(3 \times 2) \times 2 = 12$` different models being trained. In realistic settings, it can be common to try many more parameters and use more folds (`$k=3$` and `$k=10$` are common). In other words, using `CrossValidator` can be very expensive. However, it is also a well-established method for choosing parameters which is more statistically sound than heuristic hand-tuning.
  * **Python**
  * **Scala**
  * **Java**


Refer to the [`CrossValidator` Python docs](https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.ml.tuning.CrossValidator.html) for more details on the API.

```
from pyspark.ml import Pipeline
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.evaluation import BinaryClassificationEvaluator
from pyspark.ml.feature import HashingTF, Tokenizer
from pyspark.ml.tuning import CrossValidator, ParamGridBuilder

# Prepare training documents, which are labeled.
training = spark.createDataFrame([
    (0, "a b c d e spark", 1.0),
    (1, "b d", 0.0),
    (2, "spark f g h", 1.0),
    (3, "hadoop mapreduce", 0.0),
    (4, "b spark who", 1.0),
    (5, "g d a y", 0.0),
    (6, "spark fly", 1.0),
    (7, "was mapreduce", 0.0),
    (8, "e spark program", 1.0),
    (9, "a e c l", 0.0),
    (10, "spark compile", 1.0),
    (11, "hadoop software", 0.0)
], ["id", "text", "label"])

# Configure an ML pipeline, which consists of tree stages: tokenizer, hashingTF, and lr.
tokenizer = Tokenizer(inputCol="text", outputCol="words")
hashingTF = HashingTF(inputCol=tokenizer.getOutputCol(), outputCol="features")
lr = LogisticRegression(maxIter=10)
pipeline = Pipeline(stages=[tokenizer, hashingTF, lr])

# We now treat the Pipeline as an Estimator, wrapping it in a CrossValidator instance.
# This will allow us to jointly choose parameters for all Pipeline stages.
# A CrossValidator requires an Estimator, a set of Estimator ParamMaps, and an Evaluator.
# We use a ParamGridBuilder to construct a grid of parameters to search over.
# With 3 values for hashingTF.numFeatures and 2 values for lr.regParam,
# this grid will have 3 x 2 = 6 parameter settings for CrossValidator to choose from.
paramGrid = ParamGridBuilder() \
    .addGrid(hashingTF.numFeatures, [10, 100, 1000]) \
    .addGrid(lr.regParam, [0.1, 0.01]) \
    .build()

crossval = CrossValidator(estimator=pipeline,
                          estimatorParamMaps=paramGrid,
                          evaluator=BinaryClassificationEvaluator(),
                          numFolds=2)  # use 3+ folds in practice

# Run cross-validation, and choose the best set of parameters.
cvModel = crossval.fit(training)

# Prepare test documents, which are unlabeled.
test = spark.createDataFrame([
    (4, "spark i j k"),
    (5, "l m n"),
    (6, "mapreduce spark"),
    (7, "apache hadoop")
], ["id", "text"])

# Make predictions on test documents. cvModel uses the best model found (lrModel).
prediction = cvModel.transform(test)
selected = prediction.select("id", "text", "probability", "prediction")
for row in selected.collect():
    print(row)
```

Find full example code at "examples/src/main/python/ml/cross_validator.py" in the Spark repo.
Refer to the [`CrossValidator` Scala docs](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/tuning/CrossValidator.html) for details on the API.

```
import org.apache.spark.ml.Pipeline
import org.apache.spark.ml.classification.LogisticRegression
import org.apache.spark.ml.evaluation.BinaryClassificationEvaluator
import org.apache.spark.ml.feature.{HashingTF, Tokenizer}
import org.apache.spark.ml.linalg.Vector
import org.apache.spark.ml.tuning.{CrossValidator, ParamGridBuilder}
import org.apache.spark.sql.Row

// Prepare training data from a list of (id, text, label) tuples.
val training = spark.createDataFrame(Seq(
  (0L, "a b c d e spark", 1.0),
  (1L, "b d", 0.0),
  (2L, "spark f g h", 1.0),
  (3L, "hadoop mapreduce", 0.0),
  (4L, "b spark who", 1.0),
  (5L, "g d a y", 0.0),
  (6L, "spark fly", 1.0),
  (7L, "was mapreduce", 0.0),
  (8L, "e spark program", 1.0),
  (9L, "a e c l", 0.0),
  (10L, "spark compile", 1.0),
  (11L, "hadoop software", 0.0)
)).toDF("id", "text", "label")

// Configure an ML pipeline, which consists of three stages: tokenizer, hashingTF, and lr.
val tokenizer = new Tokenizer()
  .setInputCol("text")
  .setOutputCol("words")
val hashingTF = new HashingTF()
  .setInputCol(tokenizer.getOutputCol)
  .setOutputCol("features")
val lr = new LogisticRegression()
  .setMaxIter(10)
val pipeline = new Pipeline()
  .setStages(Array(tokenizer, hashingTF, lr))

// We use a ParamGridBuilder to construct a grid of parameters to search over.
// With 3 values for hashingTF.numFeatures and 2 values for lr.regParam,
// this grid will have 3 x 2 = 6 parameter settings for CrossValidator to choose from.
val paramGrid = new ParamGridBuilder()
  .addGrid(hashingTF.numFeatures, Array(10, 100, 1000))
  .addGrid(lr.regParam, Array(0.1, 0.01))
  .build()

// We now treat the Pipeline as an Estimator, wrapping it in a CrossValidator instance.
// This will allow us to jointly choose parameters for all Pipeline stages.
// A CrossValidator requires an Estimator, a set of Estimator ParamMaps, and an Evaluator.
// Note that the evaluator here is a BinaryClassificationEvaluator and its default metric
// is areaUnderROC.
val cv = new CrossValidator()
  .setEstimator(pipeline)
  .setEvaluator(new BinaryClassificationEvaluator)
  .setEstimatorParamMaps(paramGrid)
  .setNumFolds(2)  // Use 3+ in practice
  .setParallelism(2)  // Evaluate up to 2 parameter settings in parallel

// Run cross-validation, and choose the best set of parameters.
val cvModel = cv.fit(training)

// Prepare test documents, which are unlabeled (id, text) tuples.
val test = spark.createDataFrame(Seq(
  (4L, "spark i j k"),
  (5L, "l m n"),
  (6L, "mapreduce spark"),
  (7L, "apache hadoop")
)).toDF("id", "text")

// Make predictions on test documents. cvModel uses the best model found (lrModel).
cvModel.transform(test)
  .select("id", "text", "probability", "prediction")
  .collect()
  .foreach { case Row(id: Long, text: String, prob: Vector, prediction: Double) =>
    println(s"($id, $text) --> prob=$prob, prediction=$prediction")
  }
```

Find full example code at "examples/src/main/scala/org/apache/spark/examples/ml/ModelSelectionViaCrossValidationExample.scala" in the Spark repo.
Refer to the [`CrossValidator` Java docs](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/tuning/CrossValidator.html) for details on the API.

```
import java.util.Arrays;

import org.apache.spark.ml.Pipeline;
import org.apache.spark.ml.PipelineStage;
import org.apache.spark.ml.classification.LogisticRegression;
import org.apache.spark.ml.evaluation.BinaryClassificationEvaluator;
import org.apache.spark.ml.feature.HashingTF;
import org.apache.spark.ml.feature.Tokenizer;
import org.apache.spark.ml.param.ParamMap;
import org.apache.spark.ml.tuning.CrossValidator;
import org.apache.spark.ml.tuning.CrossValidatorModel;
import org.apache.spark.ml.tuning.ParamGridBuilder;
import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;

// Prepare training documents, which are labeled.
Dataset<Row> training = spark.createDataFrame(Arrays.asList(
  new JavaLabeledDocument(0L, "a b c d e spark", 1.0),
  new JavaLabeledDocument(1L, "b d", 0.0),
  new JavaLabeledDocument(2L,"spark f g h", 1.0),
  new JavaLabeledDocument(3L, "hadoop mapreduce", 0.0),
  new JavaLabeledDocument(4L, "b spark who", 1.0),
  new JavaLabeledDocument(5L, "g d a y", 0.0),
  new JavaLabeledDocument(6L, "spark fly", 1.0),
  new JavaLabeledDocument(7L, "was mapreduce", 0.0),
  new JavaLabeledDocument(8L, "e spark program", 1.0),
  new JavaLabeledDocument(9L, "a e c l", 0.0),
  new JavaLabeledDocument(10L, "spark compile", 1.0),
  new JavaLabeledDocument(11L, "hadoop software", 0.0)
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
  .setRegParam(0.01);
Pipeline pipeline = new Pipeline()
  .setStages(new PipelineStage[] {tokenizer, hashingTF, lr});

// We use a ParamGridBuilder to construct a grid of parameters to search over.
// With 3 values for hashingTF.numFeatures and 2 values for lr.regParam,
// this grid will have 3 x 2 = 6 parameter settings for CrossValidator to choose from.
ParamMap[] paramGrid = new ParamGridBuilder()
  .addGrid(hashingTF.numFeatures(), new int[] {10, 100, 1000})
  .addGrid(lr.regParam(), new double[] {0.1, 0.01})
  .build();

// We now treat the Pipeline as an Estimator, wrapping it in a CrossValidator instance.
// This will allow us to jointly choose parameters for all Pipeline stages.
// A CrossValidator requires an Estimator, a set of Estimator ParamMaps, and an Evaluator.
// Note that the evaluator here is a BinaryClassificationEvaluator and its default metric
// is areaUnderROC.
CrossValidator cv = new CrossValidator()
  .setEstimator(pipeline)
  .setEvaluator(new BinaryClassificationEvaluator())
  .setEstimatorParamMaps(paramGrid)
  .setNumFolds(2)  // Use 3+ in practice
  .setParallelism(2);  // Evaluate up to 2 parameter settings in parallel

// Run cross-validation, and choose the best set of parameters.
CrossValidatorModel cvModel = cv.fit(training);

// Prepare test documents, which are unlabeled.
Dataset<Row> test = spark.createDataFrame(Arrays.asList(
  new JavaDocument(4L, "spark i j k"),
  new JavaDocument(5L, "l m n"),
  new JavaDocument(6L, "mapreduce spark"),
  new JavaDocument(7L, "apache hadoop")
), JavaDocument.class);

// Make predictions on test documents. cvModel uses the best model found (lrModel).
Dataset<Row> predictions = cvModel.transform(test);
for (Row r : predictions.select("id", "text", "probability", "prediction").collectAsList()) {
  System.out.println("(" + r.get(0) + ", " + r.get(1) + ") --> prob=" + r.get(2)
    + ", prediction=" + r.get(3));
}
```

Find full example code at "examples/src/main/java/org/apache/spark/examples/ml/JavaModelSelectionViaCrossValidationExample.java" in the Spark repo.
# Train-Validation Split[](https://spark.apache.org/docs/latest/ml-tuning.html#train-validation-split)
In addition to `CrossValidator` Spark also offers `TrainValidationSplit` for hyper-parameter tuning. `TrainValidationSplit` only evaluates each combination of parameters once, as opposed to k times in the case of `CrossValidator`. It is, therefore, less expensive, but will not produce as reliable results when the training dataset is not sufficiently large.
Unlike `CrossValidator`, `TrainValidationSplit` creates a single (training, test) dataset pair. It splits the dataset into these two parts using the `trainRatio` parameter. For example with `$trainRatio=0.75$`, `TrainValidationSplit` will generate a training and test dataset pair where 75% of the data is used for training and 25% for validation.
Like `CrossValidator`, `TrainValidationSplit` finally fits the `Estimator` using the best `ParamMap` and the entire dataset.
**Examples: model selection via train validation split**
  * **Python**
  * **Scala**
  * **Java**


Refer to the [`TrainValidationSplit` Python docs](https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.ml.tuning.TrainValidationSplit.html) for more details on the API.

```
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.regression import LinearRegression
from pyspark.ml.tuning import ParamGridBuilder, TrainValidationSplit

# Prepare training and test data.
data = spark.read.format("libsvm")\
    .load("data/mllib/sample_linear_regression_data.txt")
train, test = data.randomSplit([0.9, 0.1], seed=12345)

lr = LinearRegression(maxIter=10)

# We use a ParamGridBuilder to construct a grid of parameters to search over.
# TrainValidationSplit will try all combinations of values and determine best model using
# the evaluator.
paramGrid = ParamGridBuilder()\
    .addGrid(lr.regParam, [0.1, 0.01]) \
    .addGrid(lr.fitIntercept, [False, True])\
    .addGrid(lr.elasticNetParam, [0.0, 0.5, 1.0])\
    .build()

# In this case the estimator is simply the linear regression.
# A TrainValidationSplit requires an Estimator, a set of Estimator ParamMaps, and an Evaluator.
tvs = TrainValidationSplit(estimator=lr,
                           estimatorParamMaps=paramGrid,
                           evaluator=RegressionEvaluator(),
                           # 80% of the data will be used for training, 20% for validation.
                           trainRatio=0.8)

# Run TrainValidationSplit, and choose the best set of parameters.
model = tvs.fit(train)

# Make predictions on test data. model is the model with combination of parameters
# that performed best.
model.transform(test)\
    .select("features", "label", "prediction")\
    .show()
```

Find full example code at "examples/src/main/python/ml/train_validation_split.py" in the Spark repo.
Refer to the [`TrainValidationSplit` Scala docs](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/tuning/TrainValidationSplit.html) for details on the API.

```
import org.apache.spark.ml.evaluation.RegressionEvaluator
import org.apache.spark.ml.regression.LinearRegression
import org.apache.spark.ml.tuning.{ParamGridBuilder, TrainValidationSplit}

// Prepare training and test data.
val data = spark.read.format("libsvm").load("data/mllib/sample_linear_regression_data.txt")
val Array(training, test) = data.randomSplit(Array(0.9, 0.1), seed = 12345)

val lr = new LinearRegression()
    .setMaxIter(10)

// We use a ParamGridBuilder to construct a grid of parameters to search over.
// TrainValidationSplit will try all combinations of values and determine best model using
// the evaluator.
val paramGrid = new ParamGridBuilder()
  .addGrid(lr.regParam, Array(0.1, 0.01))
  .addGrid(lr.fitIntercept)
  .addGrid(lr.elasticNetParam, Array(0.0, 0.5, 1.0))
  .build()

// In this case the estimator is simply the linear regression.
// A TrainValidationSplit requires an Estimator, a set of Estimator ParamMaps, and an Evaluator.
val trainValidationSplit = new TrainValidationSplit()
  .setEstimator(lr)
  .setEvaluator(new RegressionEvaluator)
  .setEstimatorParamMaps(paramGrid)
  // 80% of the data will be used for training and the remaining 20% for validation.
  .setTrainRatio(0.8)
  // Evaluate up to 2 parameter settings in parallel
  .setParallelism(2)

// Run train validation split, and choose the best set of parameters.
val model = trainValidationSplit.fit(training)

// Make predictions on test data. model is the model with combination of parameters
// that performed best.
model.transform(test)
  .select("features", "label", "prediction")
  .show()
```

Find full example code at "examples/src/main/scala/org/apache/spark/examples/ml/ModelSelectionViaTrainValidationSplitExample.scala" in the Spark repo.
Refer to the [`TrainValidationSplit` Java docs](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/tuning/TrainValidationSplit.html) for details on the API.

```
import org.apache.spark.ml.evaluation.RegressionEvaluator;
import org.apache.spark.ml.param.ParamMap;
import org.apache.spark.ml.regression.LinearRegression;
import org.apache.spark.ml.tuning.ParamGridBuilder;
import org.apache.spark.ml.tuning.TrainValidationSplit;
import org.apache.spark.ml.tuning.TrainValidationSplitModel;
import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;

Dataset<Row> data = spark.read().format("libsvm")
  .load("data/mllib/sample_linear_regression_data.txt");

// Prepare training and test data.
Dataset<Row>[] splits = data.randomSplit(new double[] {0.9, 0.1}, 12345);
Dataset<Row> training = splits[0];
Dataset<Row> test = splits[1];

LinearRegression lr = new LinearRegression();

// We use a ParamGridBuilder to construct a grid of parameters to search over.
// TrainValidationSplit will try all combinations of values and determine best model using
// the evaluator.
ParamMap[] paramGrid = new ParamGridBuilder()
  .addGrid(lr.regParam(), new double[] {0.1, 0.01})
  .addGrid(lr.fitIntercept())
  .addGrid(lr.elasticNetParam(), new double[] {0.0, 0.5, 1.0})
  .build();

// In this case the estimator is simply the linear regression.
// A TrainValidationSplit requires an Estimator, a set of Estimator ParamMaps, and an Evaluator.
TrainValidationSplit trainValidationSplit = new TrainValidationSplit()
  .setEstimator(lr)
  .setEvaluator(new RegressionEvaluator())
  .setEstimatorParamMaps(paramGrid)
  .setTrainRatio(0.8)  // 80% for training and the remaining 20% for validation
  .setParallelism(2);  // Evaluate up to 2 parameter settings in parallel

// Run train validation split, and choose the best set of parameters.
TrainValidationSplitModel model = trainValidationSplit.fit(training);

// Make predictions on test data. model is the model with combination of parameters
// that performed best.
model.transform(test)
  .select("features", "label", "prediction")
  .show();
```

Find full example code at "examples/src/main/java/org/apache/spark/examples/ml/JavaModelSelectionViaTrainValidationSplitExample.java" in the Spark repo.
