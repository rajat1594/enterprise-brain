[ ![](https://spark.apache.org/images/spark-logo-rev.svg)](https://spark.apache.org/docs/latest/index.html)4.1.2
  * [Overview](https://spark.apache.org/docs/latest/index.html)
  * [Programming Guides](https://spark.apache.org/docs/latest/mllib-pmml-model-export.html)
[Quick Start](https://spark.apache.org/docs/latest/quick-start.html) [RDDs, Accumulators, Broadcasts Vars](https://spark.apache.org/docs/latest/rdd-programming-guide.html) [SQL, DataFrames, and Datasets](https://spark.apache.org/docs/latest/sql-programming-guide.html) [Structured Streaming](https://spark.apache.org/docs/latest/streaming/index.html) [Spark Streaming (DStreams)](https://spark.apache.org/docs/latest/streaming-programming-guide.html) [MLlib (Machine Learning)](https://spark.apache.org/docs/latest/ml-guide.html) [GraphX (Graph Processing)](https://spark.apache.org/docs/latest/graphx-programming-guide.html) [SparkR (R on Spark)](https://spark.apache.org/docs/latest/sparkr.html) [PySpark (Python on Spark)](https://spark.apache.org/docs/latest/api/python/getting_started/index.html) [Declarative Pipelines](https://spark.apache.org/docs/latest/declarative-pipelines-programming-guide.html)
  * [API Docs](https://spark.apache.org/docs/latest/mllib-pmml-model-export.html)
[Python](https://spark.apache.org/docs/latest/api/python/index.html) [Scala](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html) [Java](https://spark.apache.org/docs/latest/api/java/index.html) [R](https://spark.apache.org/docs/latest/api/R/index.html) [SQL, Built-in Functions](https://spark.apache.org/docs/latest/api/sql/index.html)
  * [Deploying](https://spark.apache.org/docs/latest/mllib-pmml-model-export.html)
[Overview](https://spark.apache.org/docs/latest/cluster-overview.html) [Submitting Applications](https://spark.apache.org/docs/latest/submitting-applications.html) [Spark Standalone](https://spark.apache.org/docs/latest/spark-standalone.html) [YARN](https://spark.apache.org/docs/latest/running-on-yarn.html) [Kubernetes](https://spark.apache.org/docs/latest/running-on-kubernetes.html)
  * [More](https://spark.apache.org/docs/latest/mllib-pmml-model-export.html)
[Configuration](https://spark.apache.org/docs/latest/configuration.html) [Monitoring](https://spark.apache.org/docs/latest/monitoring.html) [Tuning Guide](https://spark.apache.org/docs/latest/tuning.html) [Job Scheduling](https://spark.apache.org/docs/latest/job-scheduling.html) [Security](https://spark.apache.org/docs/latest/security.html) [Hardware Provisioning](https://spark.apache.org/docs/latest/hardware-provisioning.html) [Migration Guide](https://spark.apache.org/docs/latest/migration-guide.html) [Building Spark](https://spark.apache.org/docs/latest/building-spark.html) [Contributing to Spark](https://spark.apache.org/contributing.html) [Third Party Projects](https://spark.apache.org/third-party-projects.html)
  *

###  [MLlib: Main Guide](https://spark.apache.org/docs/latest/ml-guide.html)[](https://spark.apache.org/docs/latest/mllib-pmml-model-export.html#mllib-main-guide)
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

###  [MLlib: RDD-based API Guide](https://spark.apache.org/docs/latest/mllib-guide.html)[](https://spark.apache.org/docs/latest/mllib-pmml-model-export.html#mllib-rdd-based-api-guide)
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

# PMML model export - RDD-based API[](https://spark.apache.org/docs/latest/mllib-pmml-model-export.html#pmml-model-export-rdd-based-api)
  * [spark.mllib supported models](https://spark.apache.org/docs/latest/mllib-pmml-model-export.html#sparkmllib-supported-models)
  * [Examples](https://spark.apache.org/docs/latest/mllib-pmml-model-export.html#examples)

## spark.mllib supported models[](https://spark.apache.org/docs/latest/mllib-pmml-model-export.html#sparkmllib-supported-models)
`spark.mllib` supports model export to Predictive Model Markup Language ([PMML](http://en.wikipedia.org/wiki/Predictive_Model_Markup_Language)).
The table below outlines the `spark.mllib` models that can be exported to PMML and their equivalent PMML model.
| spark.mllib model  | PMML model  |
| --- | --- |
| KMeansModel  | ClusteringModel  |
| LinearRegressionModel  | RegressionModel (functionName="regression")  |
| RidgeRegressionModel  | RegressionModel (functionName="regression")  |
| LassoModel  | RegressionModel (functionName="regression")  |
| SVMModel  | RegressionModel (functionName="classification" normalizationMethod="none")  |
| Binary LogisticRegressionModel  | RegressionModel (functionName="classification" normalizationMethod="logit")  |
## Examples[](https://spark.apache.org/docs/latest/mllib-pmml-model-export.html#examples)
  * **Scala**

To export a supported `model` (see table above) to PMML, simply call `model.toPMML`.
As well as exporting the PMML model to a String (`model.toPMML` as in the example above), you can export the PMML model to other formats.
Refer to the [`KMeans` Scala docs](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/mllib/clustering/KMeans.html) and [`Vectors` Scala docs](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/mllib/linalg/Vectors$.html) for details on the API.
Here a complete example of building a KMeansModel and print it out in PMML format:

```
import org.apache.spark.mllib.clustering.KMeans
import org.apache.spark.mllib.linalg.Vectors

// Load and parse the data
val data = sc.textFile("data/mllib/kmeans_data.txt")
val parsedData = data.map(s => Vectors.dense(s.split(' ').map(_.toDouble))).cache()

// Cluster the data into two classes using KMeans
val numClusters = 2
val numIterations = 20
val clusters = KMeans.train(parsedData, numClusters, numIterations)

// Export to PMML to a String in PMML format
println(s"PMML Model:\n ${clusters.toPMML()}")

// Export the model to a local file in PMML format
clusters.toPMML("/tmp/kmeans.xml")

// Export the model to a directory on a distributed file system in PMML format
clusters.toPMML(sc, "/tmp/kmeans")

// Export the model to the OutputStream in PMML format
clusters.toPMML(System.out)
```

Find full example code at "examples/src/main/scala/org/apache/spark/examples/mllib/PMMLModelExportExample.scala" in the Spark repo.
For unsupported models, either you will not find a `.toPMML` method or an `IllegalArgumentException` will be thrown.
