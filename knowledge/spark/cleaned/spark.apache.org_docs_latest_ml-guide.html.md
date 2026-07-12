[ ![](https://spark.apache.org/images/spark-logo-rev.svg)](https://spark.apache.org/docs/latest/index.html)4.1.2
  * [Overview](https://spark.apache.org/docs/latest/index.html)
  * [Programming Guides](https://spark.apache.org/docs/latest/ml-guide.html)
[Quick Start](https://spark.apache.org/docs/latest/quick-start.html) [RDDs, Accumulators, Broadcasts Vars](https://spark.apache.org/docs/latest/rdd-programming-guide.html) [SQL, DataFrames, and Datasets](https://spark.apache.org/docs/latest/sql-programming-guide.html) [Structured Streaming](https://spark.apache.org/docs/latest/streaming/index.html) [Spark Streaming (DStreams)](https://spark.apache.org/docs/latest/streaming-programming-guide.html) [MLlib (Machine Learning)](https://spark.apache.org/docs/latest/ml-guide.html) [GraphX (Graph Processing)](https://spark.apache.org/docs/latest/graphx-programming-guide.html) [SparkR (R on Spark)](https://spark.apache.org/docs/latest/sparkr.html) [PySpark (Python on Spark)](https://spark.apache.org/docs/latest/api/python/getting_started/index.html) [Declarative Pipelines](https://spark.apache.org/docs/latest/declarative-pipelines-programming-guide.html)
  * [API Docs](https://spark.apache.org/docs/latest/ml-guide.html)
[Python](https://spark.apache.org/docs/latest/api/python/index.html) [Scala](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html) [Java](https://spark.apache.org/docs/latest/api/java/index.html) [R](https://spark.apache.org/docs/latest/api/R/index.html) [SQL, Built-in Functions](https://spark.apache.org/docs/latest/api/sql/index.html)
  * [Deploying](https://spark.apache.org/docs/latest/ml-guide.html)
[Overview](https://spark.apache.org/docs/latest/cluster-overview.html) [Submitting Applications](https://spark.apache.org/docs/latest/submitting-applications.html) [Spark Standalone](https://spark.apache.org/docs/latest/spark-standalone.html) [YARN](https://spark.apache.org/docs/latest/running-on-yarn.html) [Kubernetes](https://spark.apache.org/docs/latest/running-on-kubernetes.html)
  * [More](https://spark.apache.org/docs/latest/ml-guide.html)
[Configuration](https://spark.apache.org/docs/latest/configuration.html) [Monitoring](https://spark.apache.org/docs/latest/monitoring.html) [Tuning Guide](https://spark.apache.org/docs/latest/tuning.html) [Job Scheduling](https://spark.apache.org/docs/latest/job-scheduling.html) [Security](https://spark.apache.org/docs/latest/security.html) [Hardware Provisioning](https://spark.apache.org/docs/latest/hardware-provisioning.html) [Migration Guide](https://spark.apache.org/docs/latest/migration-guide.html) [Building Spark](https://spark.apache.org/docs/latest/building-spark.html) [Contributing to Spark](https://spark.apache.org/contributing.html) [Third Party Projects](https://spark.apache.org/third-party-projects.html)
  *

###  [MLlib: Main Guide](https://spark.apache.org/docs/latest/ml-guide.html)[](https://spark.apache.org/docs/latest/ml-guide.html#mllib-main-guide)
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

###  [MLlib: RDD-based API Guide](https://spark.apache.org/docs/latest/mllib-guide.html)[](https://spark.apache.org/docs/latest/ml-guide.html#mllib-rdd-based-api-guide)
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

# Machine Learning Library (MLlib) Guide[](https://spark.apache.org/docs/latest/ml-guide.html#machine-learning-library-mllib-guide)
MLlib is Spark’s machine learning (ML) library. Its goal is to make practical machine learning scalable and easy. At a high level, it provides tools such as:
  * ML Algorithms: common learning algorithms such as classification, regression, clustering, and collaborative filtering
  * Featurization: feature extraction, transformation, dimensionality reduction, and selection
  * Pipelines: tools for constructing, evaluating, and tuning ML Pipelines
  * Persistence: saving and load algorithms, models, and Pipelines
  * Utilities: linear algebra, statistics, data handling, etc.

# Announcement: DataFrame-based API is primary API[](https://spark.apache.org/docs/latest/ml-guide.html#announcement-dataframe-based-api-is-primary-api)
**The MLlib RDD-based API is now in maintenance mode.**
As of Spark 2.0, the [RDD](https://spark.apache.org/docs/latest/rdd-programming-guide.html#resilient-distributed-datasets-rdds)-based APIs in the `spark.mllib` package have entered maintenance mode. The primary Machine Learning API for Spark is now the [DataFrame](https://spark.apache.org/docs/latest/sql-programming-guide.html)-based API in the `spark.ml` package.
_What are the implications?_
  * MLlib will still support the RDD-based API in `spark.mllib` with bug fixes.
  * MLlib will not add new features to the RDD-based API.
  * In the Spark 2.x releases, MLlib will add features to the DataFrames-based API to reach feature parity with the RDD-based API.

_Why is MLlib switching to the DataFrame-based API?_
  * DataFrames provide a more user-friendly API than RDDs. The many benefits of DataFrames include Spark Datasources, SQL/DataFrame queries, Tungsten and Catalyst optimizations, and uniform APIs across languages.
  * The DataFrame-based API for MLlib provides a uniform API across ML algorithms and across multiple languages.
  * DataFrames facilitate practical ML Pipelines, particularly feature transformations. See the [Pipelines guide](https://spark.apache.org/docs/latest/ml-pipeline.html) for details.

_What is “Spark ML”?_
  * “Spark ML” is not an official name but occasionally used to refer to the MLlib DataFrame-based API. This is majorly due to the `org.apache.spark.ml` Scala package name used by the DataFrame-based API, and the “Spark ML Pipelines” term we used initially to emphasize the pipeline concept.

_Is MLlib deprecated?_
  * No. MLlib includes both the RDD-based API and the DataFrame-based API. The RDD-based API is now in maintenance mode. But neither API is deprecated, nor MLlib as a whole.

# Dependencies[](https://spark.apache.org/docs/latest/ml-guide.html#dependencies)
MLlib uses linear algebra packages [Breeze](http://www.scalanlp.org/) and [dev.ludovic.netlib](https://github.com/luhenry/netlib) for optimised numerical processing[1](https://spark.apache.org/docs/latest/ml-guide.html#fn:1). Those packages may call native acceleration libraries such as [Intel MKL](https://software.intel.com/content/www/us/en/develop/tools/math-kernel-library.html) or [OpenBLAS](http://www.openblas.net) if they are available as system libraries or in runtime library paths.
However, native acceleration libraries can’t be distributed with Spark. See [MLlib Linear Algebra Acceleration Guide](https://spark.apache.org/docs/latest/ml-linalg-guide.html) for how to enable accelerated linear algebra processing. If accelerated native libraries are not enabled, you will see a warning message like below and a pure JVM implementation will be used instead:

```
WARNING: Failed to load implementation from:dev.ludovic.netlib.blas.JNIBLAS

```

To use MLlib in Python, you will need [NumPy](http://www.numpy.org) version 1.4 or newer.
# Highlights in 3.0[](https://spark.apache.org/docs/latest/ml-guide.html#highlights-in-30)
The list below highlights some of the new features and enhancements added to MLlib in the `3.0` release of Spark:
  * Multiple columns support was added to `Binarizer` ([SPARK-23578](https://issues.apache.org/jira/browse/SPARK-23578)), `StringIndexer` ([SPARK-11215](https://issues.apache.org/jira/browse/SPARK-11215)), `StopWordsRemover` ([SPARK-29808](https://issues.apache.org/jira/browse/SPARK-29808)) and PySpark `QuantileDiscretizer` ([SPARK-22796](https://issues.apache.org/jira/browse/SPARK-22796)).
  * Tree-Based Feature Transformation was added ([SPARK-13677](https://issues.apache.org/jira/browse/SPARK-13677)).
  * Two new evaluators `MultilabelClassificationEvaluator` ([SPARK-16692](https://issues.apache.org/jira/browse/SPARK-16692)) and `RankingEvaluator` ([SPARK-28045](https://issues.apache.org/jira/browse/SPARK-28045)) were added.
  * Sample weights support was added in `DecisionTreeClassifier/Regressor` ([SPARK-19591](https://issues.apache.org/jira/browse/SPARK-19591)), `RandomForestClassifier/Regressor` ([SPARK-9478](https://issues.apache.org/jira/browse/SPARK-9478)), `GBTClassifier/Regressor` ([SPARK-9612](https://issues.apache.org/jira/browse/SPARK-9612)), `MulticlassClassificationEvaluator` ([SPARK-24101](https://issues.apache.org/jira/browse/SPARK-24101)), `RegressionEvaluator` ([SPARK-24102](https://issues.apache.org/jira/browse/SPARK-24102)), `BinaryClassificationEvaluator` ([SPARK-24103](https://issues.apache.org/jira/browse/SPARK-24103)), `BisectingKMeans` ([SPARK-30351](https://issues.apache.org/jira/browse/SPARK-30351)), `KMeans` ([SPARK-29967](https://issues.apache.org/jira/browse/SPARK-29967)) and `GaussianMixture` ([SPARK-30102](https://issues.apache.org/jira/browse/SPARK-30102)).
  * R API for `PowerIterationClustering` was added ([SPARK-19827](https://issues.apache.org/jira/browse/SPARK-19827)).
  * Added Spark ML listener for tracking ML pipeline status ([SPARK-23674](https://issues.apache.org/jira/browse/SPARK-23674)).
  * Fit with validation set was added to Gradient Boosted Trees in Python ([SPARK-24333](https://issues.apache.org/jira/browse/SPARK-24333)).
  * [`RobustScaler`](https://spark.apache.org/docs/latest/ml-features.html#robustscaler) transformer was added ([SPARK-28399](https://issues.apache.org/jira/browse/SPARK-28399)).
  * [`Factorization Machines`](https://spark.apache.org/docs/latest/ml-classification-regression.html#factorization-machines) classifier and regressor were added ([SPARK-29224](https://issues.apache.org/jira/browse/SPARK-29224)).
  * Gaussian Naive Bayes Classifier ([SPARK-16872](https://issues.apache.org/jira/browse/SPARK-16872)) and Complement Naive Bayes Classifier ([SPARK-29942](https://issues.apache.org/jira/browse/SPARK-29942)) were added.
  * ML function parity between Scala and Python ([SPARK-28958](https://issues.apache.org/jira/browse/SPARK-28958)).
  * `predictRaw` is made public in all the Classification models. `predictProbability` is made public in all the Classification models except `LinearSVCModel` ([SPARK-30358](https://issues.apache.org/jira/browse/SPARK-30358)).

# Migration Guide[](https://spark.apache.org/docs/latest/ml-guide.html#migration-guide)
The migration guide is now archived [on this page](https://spark.apache.org/docs/latest/ml-migration-guide.html).
  1. To learn more about the benefits and background of system optimised natives, you may wish to watch Sam Halliday’s ScalaX talk on [High Performance Linear Algebra in Scala](http://fommil.github.io/scalax14/). [↩](https://spark.apache.org/docs/latest/ml-guide.html#fnref:1)
