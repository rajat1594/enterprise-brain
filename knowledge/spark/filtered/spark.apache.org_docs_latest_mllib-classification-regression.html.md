[ ![](https://spark.apache.org/images/spark-logo-rev.svg)](https://spark.apache.org/docs/latest/index.html)4.1.2
  * [Overview](https://spark.apache.org/docs/latest/index.html)
  * [Programming Guides](https://spark.apache.org/docs/latest/mllib-classification-regression.html)
[Quick Start](https://spark.apache.org/docs/latest/quick-start.html) [RDDs, Accumulators, Broadcasts Vars](https://spark.apache.org/docs/latest/rdd-programming-guide.html) [SQL, DataFrames, and Datasets](https://spark.apache.org/docs/latest/sql-programming-guide.html) [Structured Streaming](https://spark.apache.org/docs/latest/streaming/index.html) [Spark Streaming (DStreams)](https://spark.apache.org/docs/latest/streaming-programming-guide.html) [MLlib (Machine Learning)](https://spark.apache.org/docs/latest/ml-guide.html) [GraphX (Graph Processing)](https://spark.apache.org/docs/latest/graphx-programming-guide.html) [SparkR (R on Spark)](https://spark.apache.org/docs/latest/sparkr.html) [PySpark (Python on Spark)](https://spark.apache.org/docs/latest/api/python/getting_started/index.html) [Declarative Pipelines](https://spark.apache.org/docs/latest/declarative-pipelines-programming-guide.html)
  * [API Docs](https://spark.apache.org/docs/latest/mllib-classification-regression.html)
[Python](https://spark.apache.org/docs/latest/api/python/index.html) [Scala](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html) [Java](https://spark.apache.org/docs/latest/api/java/index.html) [R](https://spark.apache.org/docs/latest/api/R/index.html) [SQL, Built-in Functions](https://spark.apache.org/docs/latest/api/sql/index.html)
  * [Deploying](https://spark.apache.org/docs/latest/mllib-classification-regression.html)
[Overview](https://spark.apache.org/docs/latest/cluster-overview.html) [Submitting Applications](https://spark.apache.org/docs/latest/submitting-applications.html) [Spark Standalone](https://spark.apache.org/docs/latest/spark-standalone.html) [YARN](https://spark.apache.org/docs/latest/running-on-yarn.html) [Kubernetes](https://spark.apache.org/docs/latest/running-on-kubernetes.html)
  * [More](https://spark.apache.org/docs/latest/mllib-classification-regression.html)
[Configuration](https://spark.apache.org/docs/latest/configuration.html) [Monitoring](https://spark.apache.org/docs/latest/monitoring.html) [Tuning Guide](https://spark.apache.org/docs/latest/tuning.html) [Job Scheduling](https://spark.apache.org/docs/latest/job-scheduling.html) [Security](https://spark.apache.org/docs/latest/security.html) [Hardware Provisioning](https://spark.apache.org/docs/latest/hardware-provisioning.html) [Migration Guide](https://spark.apache.org/docs/latest/migration-guide.html) [Building Spark](https://spark.apache.org/docs/latest/building-spark.html) [Contributing to Spark](https://spark.apache.org/contributing.html) [Third Party Projects](https://spark.apache.org/third-party-projects.html)
  * 

###  [MLlib: Main Guide](https://spark.apache.org/docs/latest/ml-guide.html)[](https://spark.apache.org/docs/latest/mllib-classification-regression.html#mllib-main-guide)
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


###  [MLlib: RDD-based API Guide](https://spark.apache.org/docs/latest/mllib-guide.html)[](https://spark.apache.org/docs/latest/mllib-classification-regression.html#mllib-rdd-based-api-guide)
  * [ Data types ](https://spark.apache.org/docs/latest/mllib-data-types.html)
  * [ Basic statistics ](https://spark.apache.org/docs/latest/mllib-statistics.html)
  * [ Classification and regression ](https://spark.apache.org/docs/latest/mllib-classification-regression.html)
    * [ Linear models (SVMs, logistic regression, linear regression) ](https://spark.apache.org/docs/latest/mllib-linear-methods.html)
    * [ Naive Bayes ](https://spark.apache.org/docs/latest/mllib-naive-bayes.html)
    * [ decision trees ](https://spark.apache.org/docs/latest/mllib-decision-tree.html)
    * [ ensembles of trees (Random Forests and Gradient-Boosted Trees) ](https://spark.apache.org/docs/latest/mllib-ensembles.html)
    * [ isotonic regression ](https://spark.apache.org/docs/latest/mllib-isotonic-regression.html)
  * [ Collaborative filtering ](https://spark.apache.org/docs/latest/mllib-collaborative-filtering.html)
  * [ Clustering ](https://spark.apache.org/docs/latest/mllib-clustering.html)
  * [ Dimensionality reduction ](https://spark.apache.org/docs/latest/mllib-dimensionality-reduction.html)
  * [ Feature extraction and transformation ](https://spark.apache.org/docs/latest/mllib-feature-extraction.html)
  * [ Frequent pattern mining ](https://spark.apache.org/docs/latest/mllib-frequent-pattern-mining.html)
  * [ Evaluation metrics ](https://spark.apache.org/docs/latest/mllib-evaluation-metrics.html)
  * [ PMML model export ](https://spark.apache.org/docs/latest/mllib-pmml-model-export.html)
  * [ Optimization (developer) ](https://spark.apache.org/docs/latest/mllib-optimization.html)


# Classification and Regression - RDD-based API[](https://spark.apache.org/docs/latest/mllib-classification-regression.html#classification-and-regression-rdd-based-api)
The `spark.mllib` package supports various methods for [binary classification](http://en.wikipedia.org/wiki/Binary_classification), [multiclass classification](http://en.wikipedia.org/wiki/Multiclass_classification), and [regression analysis](http://en.wikipedia.org/wiki/Regression_analysis). The table below outlines the supported algorithms for each type of problem.  
| Problem Type  | Supported Methods  |  
| --- | --- |  
| Binary Classification  | linear SVMs, logistic regression, decision trees, random forests, gradient-boosted trees, naive Bayes  |  
| Multiclass Classification  | logistic regression, decision trees, random forests, naive Bayes  |  
| Regression  | linear least squares, Lasso, ridge regression, decision trees, random forests, gradient-boosted trees, isotonic regression  |  
More details for these methods can be found here:
  * [Linear models](https://spark.apache.org/docs/latest/mllib-linear-methods.html)
    * [classification (SVMs, logistic regression)](https://spark.apache.org/docs/latest/mllib-linear-methods.html#classification)
    * [linear regression (least squares, Lasso, ridge)](https://spark.apache.org/docs/latest/mllib-linear-methods.html#linear-least-squares-lasso-and-ridge-regression)
  * [Decision trees](https://spark.apache.org/docs/latest/mllib-decision-tree.html)
  * [Ensembles of decision trees](https://spark.apache.org/docs/latest/mllib-ensembles.html)
    * [random forests](https://spark.apache.org/docs/latest/mllib-ensembles.html#random-forests)
    * [gradient-boosted trees](https://spark.apache.org/docs/latest/mllib-ensembles.html#gradient-boosted-trees-gbts)
  * [Naive Bayes](https://spark.apache.org/docs/latest/mllib-naive-bayes.html)
  * [Isotonic regression](https://spark.apache.org/docs/latest/mllib-isotonic-regression.html)


