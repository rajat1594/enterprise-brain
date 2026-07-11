[ ![](https://spark.apache.org/images/spark-logo-rev.svg)](https://spark.apache.org/docs/latest/index.html)4.1.2
  * [Overview](https://spark.apache.org/docs/latest/index.html)
  * [Programming Guides](https://spark.apache.org/docs/latest/ml-clustering.html)
[Quick Start](https://spark.apache.org/docs/latest/quick-start.html) [RDDs, Accumulators, Broadcasts Vars](https://spark.apache.org/docs/latest/rdd-programming-guide.html) [SQL, DataFrames, and Datasets](https://spark.apache.org/docs/latest/sql-programming-guide.html) [Structured Streaming](https://spark.apache.org/docs/latest/streaming/index.html) [Spark Streaming (DStreams)](https://spark.apache.org/docs/latest/streaming-programming-guide.html) [MLlib (Machine Learning)](https://spark.apache.org/docs/latest/ml-guide.html) [GraphX (Graph Processing)](https://spark.apache.org/docs/latest/graphx-programming-guide.html) [SparkR (R on Spark)](https://spark.apache.org/docs/latest/sparkr.html) [PySpark (Python on Spark)](https://spark.apache.org/docs/latest/api/python/getting_started/index.html) [Declarative Pipelines](https://spark.apache.org/docs/latest/declarative-pipelines-programming-guide.html)
  * [API Docs](https://spark.apache.org/docs/latest/ml-clustering.html)
[Python](https://spark.apache.org/docs/latest/api/python/index.html) [Scala](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html) [Java](https://spark.apache.org/docs/latest/api/java/index.html) [R](https://spark.apache.org/docs/latest/api/R/index.html) [SQL, Built-in Functions](https://spark.apache.org/docs/latest/api/sql/index.html)
  * [Deploying](https://spark.apache.org/docs/latest/ml-clustering.html)
[Overview](https://spark.apache.org/docs/latest/cluster-overview.html) [Submitting Applications](https://spark.apache.org/docs/latest/submitting-applications.html) [Spark Standalone](https://spark.apache.org/docs/latest/spark-standalone.html) [YARN](https://spark.apache.org/docs/latest/running-on-yarn.html) [Kubernetes](https://spark.apache.org/docs/latest/running-on-kubernetes.html)
  * [More](https://spark.apache.org/docs/latest/ml-clustering.html)
[Configuration](https://spark.apache.org/docs/latest/configuration.html) [Monitoring](https://spark.apache.org/docs/latest/monitoring.html) [Tuning Guide](https://spark.apache.org/docs/latest/tuning.html) [Job Scheduling](https://spark.apache.org/docs/latest/job-scheduling.html) [Security](https://spark.apache.org/docs/latest/security.html) [Hardware Provisioning](https://spark.apache.org/docs/latest/hardware-provisioning.html) [Migration Guide](https://spark.apache.org/docs/latest/migration-guide.html) [Building Spark](https://spark.apache.org/docs/latest/building-spark.html) [Contributing to Spark](https://spark.apache.org/contributing.html) [Third Party Projects](https://spark.apache.org/third-party-projects.html)
  * 

###  [MLlib: Main Guide](https://spark.apache.org/docs/latest/ml-guide.html)[](https://spark.apache.org/docs/latest/ml-clustering.html#mllib-main-guide)
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


###  [MLlib: RDD-based API Guide](https://spark.apache.org/docs/latest/mllib-guide.html)[](https://spark.apache.org/docs/latest/ml-clustering.html#mllib-rdd-based-api-guide)
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


# Clustering[](https://spark.apache.org/docs/latest/ml-clustering.html#clustering)
This page describes clustering algorithms in MLlib. The [guide for clustering in the RDD-based API](https://spark.apache.org/docs/latest/mllib-clustering.html) also has relevant information about these algorithms.
**Table of Contents**
  * [K-means](https://spark.apache.org/docs/latest/ml-clustering.html#k-means)
    * [Input Columns](https://spark.apache.org/docs/latest/ml-clustering.html#input-columns)
    * [Output Columns](https://spark.apache.org/docs/latest/ml-clustering.html#output-columns)
  * [Latent Dirichlet allocation (LDA)](https://spark.apache.org/docs/latest/ml-clustering.html#latent-dirichlet-allocation-lda)
  * [Bisecting k-means](https://spark.apache.org/docs/latest/ml-clustering.html#bisecting-k-means)
  * [Gaussian Mixture Model (GMM)](https://spark.apache.org/docs/latest/ml-clustering.html#gaussian-mixture-model-gmm)
    * [Input Columns](https://spark.apache.org/docs/latest/ml-clustering.html#input-columns-1)
    * [Output Columns](https://spark.apache.org/docs/latest/ml-clustering.html#output-columns-1)
  * [Power Iteration Clustering (PIC)](https://spark.apache.org/docs/latest/ml-clustering.html#power-iteration-clustering-pic)


## K-means[](https://spark.apache.org/docs/latest/ml-clustering.html#k-means)
[k-means](http://en.wikipedia.org/wiki/K-means_clustering) is one of the most commonly used clustering algorithms that clusters the data points into a predefined number of clusters. The MLlib implementation includes a parallelized variant of the [k-means++](http://en.wikipedia.org/wiki/K-means%2B%2B) method called [kmeans||](http://theory.stanford.edu/~sergei/papers/vldb12-kmpar.pdf).
`KMeans` is implemented as an `Estimator` and generates a `KMeansModel` as the base model.
### Input Columns[](https://spark.apache.org/docs/latest/ml-clustering.html#input-columns)  
| Param name  | Type(s)  | Default  | Description  |  
| --- | --- | --- | --- |  
| featuresCol  | Vector  | "features"  | Feature vector  |  
### Output Columns[](https://spark.apache.org/docs/latest/ml-clustering.html#output-columns)  
| Param name  | Type(s)  | Default  | Description  |  
| --- | --- | --- | --- |  
| predictionCol  | Int  | "prediction"  | Predicted cluster center  |  
**Examples**
  * **Python**
  * **Scala**
  * **Java**
  * **R**


Refer to the [Python API docs](https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.ml.clustering.KMeans.html) for more details.

```
from pyspark.ml.clustering import KMeans
from pyspark.ml.evaluation import ClusteringEvaluator

# Loads data.
dataset = spark.read.format("libsvm").load("data/mllib/sample_kmeans_data.txt")

# Trains a k-means model.
kmeans = KMeans().setK(2).setSeed(1)
model = kmeans.fit(dataset)

# Make predictions
predictions = model.transform(dataset)

# Evaluate clustering by computing Silhouette score
evaluator = ClusteringEvaluator()

silhouette = evaluator.evaluate(predictions)
print("Silhouette with squared euclidean distance = " + str(silhouette))

# Shows the result.
centers = model.clusterCenters()
print("Cluster Centers: ")
for center in centers:
    print(center)
```

Find full example code at "examples/src/main/python/ml/kmeans_example.py" in the Spark repo.
Refer to the [Scala API docs](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/clustering/KMeans.html) for more details.

```
import org.apache.spark.ml.clustering.KMeans
import org.apache.spark.ml.evaluation.ClusteringEvaluator

// Loads data.
val dataset = spark.read.format("libsvm").load("data/mllib/sample_kmeans_data.txt")

// Trains a k-means model.
val kmeans = new KMeans().setK(2).setSeed(1L)
val model = kmeans.fit(dataset)

// Make predictions
val predictions = model.transform(dataset)

// Evaluate clustering by computing Silhouette score
val evaluator = new ClusteringEvaluator()

val silhouette = evaluator.evaluate(predictions)
println(s"Silhouette with squared euclidean distance = $silhouette")

// Shows the result.
println("Cluster Centers: ")
model.clusterCenters.foreach(println)
```

Find full example code at "examples/src/main/scala/org/apache/spark/examples/ml/KMeansExample.scala" in the Spark repo.
Refer to the [Java API docs](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/clustering/KMeans.html) for more details.

```
import org.apache.spark.ml.clustering.KMeansModel;
import org.apache.spark.ml.clustering.KMeans;
import org.apache.spark.ml.evaluation.ClusteringEvaluator;
import org.apache.spark.ml.linalg.Vector;
import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;

// Loads data.
Dataset<Row> dataset = spark.read().format("libsvm").load("data/mllib/sample_kmeans_data.txt");

// Trains a k-means model.
KMeans kmeans = new KMeans().setK(2).setSeed(1L);
KMeansModel model = kmeans.fit(dataset);

// Make predictions
Dataset<Row> predictions = model.transform(dataset);

// Evaluate clustering by computing Silhouette score
ClusteringEvaluator evaluator = new ClusteringEvaluator();

double silhouette = evaluator.evaluate(predictions);
System.out.println("Silhouette with squared euclidean distance = " + silhouette);

// Shows the result.
Vector[] centers = model.clusterCenters();
System.out.println("Cluster Centers: ");
for (Vector center: centers) {
  System.out.println(center);
}
```

Find full example code at "examples/src/main/java/org/apache/spark/examples/ml/JavaKMeansExample.java" in the Spark repo.
Refer to the [R API docs](https://spark.apache.org/docs/latest/api/R/reference/spark.kmeans.html) for more details.

```
# Fit a k-means model with spark.kmeans
t <- as.data.frame(Titanic)
training <- createDataFrame(t)
df_list <- randomSplit(training, c(7,3), 2)
kmeansDF <- df_list[[1]]
kmeansTestDF <- df_list[[2]]
kmeansModel <- spark.kmeans(kmeansDF, ~ Class + Sex + Age + Freq,
                            k = 3)

# Model summary
summary(kmeansModel)

# Get fitted result from the k-means model
head(fitted(kmeansModel))

# Prediction
kmeansPredictions <- predict(kmeansModel, kmeansTestDF)
head(kmeansPredictions)
```

Find full example code at "examples/src/main/r/ml/kmeans.R" in the Spark repo.
## Latent Dirichlet allocation (LDA)[](https://spark.apache.org/docs/latest/ml-clustering.html#latent-dirichlet-allocation-lda)
`LDA` is implemented as an `Estimator` that supports both `EMLDAOptimizer` and `OnlineLDAOptimizer`, and generates a `LDAModel` as the base model. Expert users may cast a `LDAModel` generated by `EMLDAOptimizer` to a `DistributedLDAModel` if needed.
**Examples**
  * **Python**
  * **Scala**
  * **Java**
  * **R**


Refer to the [Python API docs](https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.ml.clustering.LDA.html) for more details.

```
from pyspark.ml.clustering import LDA

# Loads data.
dataset = spark.read.format("libsvm").load("data/mllib/sample_lda_libsvm_data.txt")

# Trains a LDA model.
lda = LDA(k=10, maxIter=10)
model = lda.fit(dataset)

ll = model.logLikelihood(dataset)
lp = model.logPerplexity(dataset)
print("The lower bound on the log likelihood of the entire corpus: " + str(ll))
print("The upper bound on perplexity: " + str(lp))

# Describe topics.
topics = model.describeTopics(3)
print("The topics described by their top-weighted terms:")
topics.show(truncate=False)

# Shows the result
transformed = model.transform(dataset)
transformed.show(truncate=False)
```

Find full example code at "examples/src/main/python/ml/lda_example.py" in the Spark repo.
Refer to the [Scala API docs](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/clustering/LDA.html) for more details.

```
import org.apache.spark.ml.clustering.LDA

// Loads data.
val dataset = spark.read.format("libsvm")
  .load("data/mllib/sample_lda_libsvm_data.txt")

// Trains a LDA model.
val lda = new LDA().setK(10).setMaxIter(10)
val model = lda.fit(dataset)

val ll = model.logLikelihood(dataset)
val lp = model.logPerplexity(dataset)
println(s"The lower bound on the log likelihood of the entire corpus: $ll")
println(s"The upper bound on perplexity: $lp")

// Describe topics.
val topics = model.describeTopics(3)
println("The topics described by their top-weighted terms:")
topics.show(false)

// Shows the result.
val transformed = model.transform(dataset)
transformed.show(false)
```

Find full example code at "examples/src/main/scala/org/apache/spark/examples/ml/LDAExample.scala" in the Spark repo.
Refer to the [Java API docs](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/clustering/LDA.html) for more details.

```
import org.apache.spark.ml.clustering.LDA;
import org.apache.spark.ml.clustering.LDAModel;
import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;
import org.apache.spark.sql.SparkSession;

// Loads data.
Dataset<Row> dataset = spark.read().format("libsvm")
  .load("data/mllib/sample_lda_libsvm_data.txt");

// Trains a LDA model.
LDA lda = new LDA().setK(10).setMaxIter(10);
LDAModel model = lda.fit(dataset);

double ll = model.logLikelihood(dataset);
double lp = model.logPerplexity(dataset);
System.out.println("The lower bound on the log likelihood of the entire corpus: " + ll);
System.out.println("The upper bound on perplexity: " + lp);

// Describe topics.
Dataset<Row> topics = model.describeTopics(3);
System.out.println("The topics described by their top-weighted terms:");
topics.show(false);

// Shows the result.
Dataset<Row> transformed = model.transform(dataset);
transformed.show(false);
```

Find full example code at "examples/src/main/java/org/apache/spark/examples/ml/JavaLDAExample.java" in the Spark repo.
Refer to the [R API docs](https://spark.apache.org/docs/latest/api/R/reference/spark.lda.html) for more details.

```
# Load training data
df <- read.df("data/mllib/sample_lda_libsvm_data.txt", source = "libsvm")
training <- df
test <- df

# Fit a latent dirichlet allocation model with spark.lda
model <- spark.lda(training, k = 10, maxIter = 10)

# Model summary
summary(model)

# Posterior probabilities
posterior <- spark.posterior(model, test)
head(posterior)

# The log perplexity of the LDA model
logPerplexity <- spark.perplexity(model, test)
print(paste0("The upper bound bound on perplexity: ", logPerplexity))
```

Find full example code at "examples/src/main/r/ml/lda.R" in the Spark repo.
## Bisecting k-means[](https://spark.apache.org/docs/latest/ml-clustering.html#bisecting-k-means)
Bisecting k-means is a kind of [hierarchical clustering](https://en.wikipedia.org/wiki/Hierarchical_clustering) using a divisive (or “top-down”) approach: all observations start in one cluster, and splits are performed recursively as one moves down the hierarchy.
Bisecting K-means can often be much faster than regular K-means, but it will generally produce a different clustering.
`BisectingKMeans` is implemented as an `Estimator` and generates a `BisectingKMeansModel` as the base model.
**Examples**
  * **Python**
  * **Scala**
  * **Java**
  * **R**


Refer to the [Python API docs](https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.ml.clustering.BisectingKMeans.html) for more details.

```
from pyspark.ml.clustering import BisectingKMeans
from pyspark.ml.evaluation import ClusteringEvaluator

# Loads data.
dataset = spark.read.format("libsvm").load("data/mllib/sample_kmeans_data.txt")

# Trains a bisecting k-means model.
bkm = BisectingKMeans().setK(2).setSeed(1)
model = bkm.fit(dataset)

# Make predictions
predictions = model.transform(dataset)

# Evaluate clustering by computing Silhouette score
evaluator = ClusteringEvaluator()

silhouette = evaluator.evaluate(predictions)
print("Silhouette with squared euclidean distance = " + str(silhouette))

# Shows the result.
print("Cluster Centers: ")
centers = model.clusterCenters()
for center in centers:
    print(center)
```

Find full example code at "examples/src/main/python/ml/bisecting_k_means_example.py" in the Spark repo.
Refer to the [Scala API docs](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/clustering/BisectingKMeans.html) for more details.

```
import org.apache.spark.ml.clustering.BisectingKMeans
import org.apache.spark.ml.evaluation.ClusteringEvaluator

// Loads data.
val dataset = spark.read.format("libsvm").load("data/mllib/sample_kmeans_data.txt")

// Trains a bisecting k-means model.
val bkm = new BisectingKMeans().setK(2).setSeed(1)
val model = bkm.fit(dataset)

// Make predictions
val predictions = model.transform(dataset)

// Evaluate clustering by computing Silhouette score
val evaluator = new ClusteringEvaluator()

val silhouette = evaluator.evaluate(predictions)
println(s"Silhouette with squared euclidean distance = $silhouette")

// Shows the result.
println("Cluster Centers: ")
val centers = model.clusterCenters
centers.foreach(println)
```

Find full example code at "examples/src/main/scala/org/apache/spark/examples/ml/BisectingKMeansExample.scala" in the Spark repo.
Refer to the [Java API docs](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/clustering/BisectingKMeans.html) for more details.

```
import org.apache.spark.ml.clustering.BisectingKMeans;
import org.apache.spark.ml.clustering.BisectingKMeansModel;
import org.apache.spark.ml.evaluation.ClusteringEvaluator;
import org.apache.spark.ml.linalg.Vector;
import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;

// Loads data.
Dataset<Row> dataset = spark.read().format("libsvm").load("data/mllib/sample_kmeans_data.txt");

// Trains a bisecting k-means model.
BisectingKMeans bkm = new BisectingKMeans().setK(2).setSeed(1);
BisectingKMeansModel model = bkm.fit(dataset);

// Make predictions
Dataset<Row> predictions = model.transform(dataset);

// Evaluate clustering by computing Silhouette score
ClusteringEvaluator evaluator = new ClusteringEvaluator();

double silhouette = evaluator.evaluate(predictions);
System.out.println("Silhouette with squared euclidean distance = " + silhouette);

// Shows the result.
System.out.println("Cluster Centers: ");
Vector[] centers = model.clusterCenters();
for (Vector center : centers) {
  System.out.println(center);
}
```

Find full example code at "examples/src/main/java/org/apache/spark/examples/ml/JavaBisectingKMeansExample.java" in the Spark repo.
Refer to the [R API docs](https://spark.apache.org/docs/latest/api/R/reference/spark.bisectingKmeans.html) for more details.

```
t <- as.data.frame(Titanic)
training <- createDataFrame(t)

# Fit bisecting k-means model with four centers
model <- spark.bisectingKmeans(training, Class ~ Survived, k = 4)

# get fitted result from a bisecting k-means model
fitted.model <- fitted(model, "centers")

# Model summary
head(summary(fitted.model))

# fitted values on training data
fitted <- predict(model, training)
head(select(fitted, "Class", "prediction"))
```

Find full example code at "examples/src/main/r/ml/bisectingKmeans.R" in the Spark repo.
## Gaussian Mixture Model (GMM)[](https://spark.apache.org/docs/latest/ml-clustering.html#gaussian-mixture-model-gmm)
A [Gaussian Mixture Model](http://en.wikipedia.org/wiki/Mixture_model#Multivariate_Gaussian_mixture_model) represents a composite distribution whereby points are drawn from one of _k_ Gaussian sub-distributions, each with its own probability. The `spark.ml` implementation uses the [expectation-maximization](http://en.wikipedia.org/wiki/Expectation%E2%80%93maximization_algorithm) algorithm to induce the maximum-likelihood model given a set of samples.
`GaussianMixture` is implemented as an `Estimator` and generates a `GaussianMixtureModel` as the base model.
### Input Columns[](https://spark.apache.org/docs/latest/ml-clustering.html#input-columns-1)  
| Param name  | Type(s)  | Default  | Description  |  
| --- | --- | --- | --- |  
| featuresCol  | Vector  | "features"  | Feature vector  |  
### Output Columns[](https://spark.apache.org/docs/latest/ml-clustering.html#output-columns-1)  
| Param name  | Type(s)  | Default  | Description  |  
| --- | --- | --- | --- |  
| predictionCol  | Int  | "prediction"  | Predicted cluster center  |  
| probabilityCol  | Vector  | "probability"  | Probability of each cluster  |  
**Examples**
  * **Python**
  * **Scala**
  * **Java**
  * **R**


Refer to the [Python API docs](https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.ml.clustering.GaussianMixture.html) for more details.

```
from pyspark.ml.clustering import GaussianMixture

# loads data
dataset = spark.read.format("libsvm").load("data/mllib/sample_kmeans_data.txt")

gmm = GaussianMixture().setK(2).setSeed(538009335)
model = gmm.fit(dataset)

print("Gaussians shown as a DataFrame: ")
model.gaussiansDF.show(truncate=False)
```

Find full example code at "examples/src/main/python/ml/gaussian_mixture_example.py" in the Spark repo.
Refer to the [Scala API docs](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/clustering/GaussianMixture.html) for more details.

```
import org.apache.spark.ml.clustering.GaussianMixture

// Loads data
val dataset = spark.read.format("libsvm").load("data/mllib/sample_kmeans_data.txt")

// Trains Gaussian Mixture Model
val gmm = new GaussianMixture()
  .setK(2)
val model = gmm.fit(dataset)

// output parameters of mixture model model
for (i <- 0 until model.getK) {
  println(s"Gaussian $i:\nweight=${model.weights(i)}\n" +
      s"mu=${model.gaussians(i).mean}\nsigma=\n${model.gaussians(i).cov}\n")
}
```

Find full example code at "examples/src/main/scala/org/apache/spark/examples/ml/GaussianMixtureExample.scala" in the Spark repo.
Refer to the [Java API docs](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/clustering/GaussianMixture.html) for more details.

```
import org.apache.spark.ml.clustering.GaussianMixture;
import org.apache.spark.ml.clustering.GaussianMixtureModel;
import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;

// Loads data
Dataset<Row> dataset = spark.read().format("libsvm").load("data/mllib/sample_kmeans_data.txt");

// Trains a GaussianMixture model
GaussianMixture gmm = new GaussianMixture()
  .setK(2);
GaussianMixtureModel model = gmm.fit(dataset);

// Output the parameters of the mixture model
for (int i = 0; i < model.getK(); i++) {
  System.out.printf("Gaussian %d:\nweight=%f\nmu=%s\nsigma=\n%s\n\n",
          i, model.weights()[i], model.gaussians()[i].mean(), model.gaussians()[i].cov());
}
```

Find full example code at "examples/src/main/java/org/apache/spark/examples/ml/JavaGaussianMixtureExample.java" in the Spark repo.
Refer to the [R API docs](https://spark.apache.org/docs/latest/api/R/reference/spark.gaussianMixture.html) for more details.

```
# Load training data
df <- read.df("data/mllib/sample_kmeans_data.txt", source = "libsvm")
training <- df
test <- df

# Fit a gaussian mixture clustering model with spark.gaussianMixture
model <- spark.gaussianMixture(training, ~ features, k = 2)

# Model summary
summary(model)

# Prediction
predictions <- predict(model, test)
head(predictions)
```

Find full example code at "examples/src/main/r/ml/gaussianMixture.R" in the Spark repo.
## Power Iteration Clustering (PIC)[](https://spark.apache.org/docs/latest/ml-clustering.html#power-iteration-clustering-pic)
Power Iteration Clustering (PIC) is a scalable graph clustering algorithm developed by [Lin and Cohen](http://www.cs.cmu.edu/~frank/papers/icml2010-pic-final.pdf). From the abstract: PIC finds a very low-dimensional embedding of a dataset using truncated power iteration on a normalized pair-wise similarity matrix of the data.
`spark.ml`’s PowerIterationClustering implementation takes the following parameters:
  * `k`: the number of clusters to create
  * `initMode`: param for the initialization algorithm
  * `maxIter`: param for maximum number of iterations
  * `srcCol`: param for the name of the input column for source vertex IDs
  * `dstCol`: name of the input column for destination vertex IDs
  * `weightCol`: Param for weight column name


**Examples**
  * **Python**
  * **Scala**
  * **Java**
  * **R**


Refer to the [Python API docs](https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.ml.clustering.PowerIterationClustering.html) for more details.

```
from pyspark.ml.clustering import PowerIterationClustering

df = spark.createDataFrame([
    (0, 1, 1.0),
    (0, 2, 1.0),
    (1, 2, 1.0),
    (3, 4, 1.0),
    (4, 0, 0.1)
], ["src", "dst", "weight"])

pic = PowerIterationClustering(k=2, maxIter=20, initMode="degree", weightCol="weight")

# Shows the cluster assignment
pic.assignClusters(df).show()
```

Find full example code at "examples/src/main/python/ml/power_iteration_clustering_example.py" in the Spark repo.
Refer to the [Scala API docs](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/clustering/PowerIterationClustering.html) for more details.

```
import org.apache.spark.ml.clustering.PowerIterationClustering

val dataset = spark.createDataFrame(Seq(
  (0L, 1L, 1.0),
  (0L, 2L, 1.0),
  (1L, 2L, 1.0),
  (3L, 4L, 1.0),
  (4L, 0L, 0.1)
)).toDF("src", "dst", "weight")

val model = new PowerIterationClustering().
  setK(2).
  setMaxIter(20).
  setInitMode("degree").
  setWeightCol("weight")

val prediction = model.assignClusters(dataset).select("id", "cluster")

//  Shows the cluster assignment
prediction.show(false)
```

Find full example code at "examples/src/main/scala/org/apache/spark/examples/ml/PowerIterationClusteringExample.scala" in the Spark repo.
Refer to the [Java API docs](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/clustering/PowerIterationClustering.html) for more details.

```
import java.util.Arrays;
import java.util.List;

import org.apache.spark.ml.clustering.PowerIterationClustering;
import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;
import org.apache.spark.sql.RowFactory;
import org.apache.spark.sql.SparkSession;
import org.apache.spark.sql.types.DataTypes;
import org.apache.spark.sql.types.Metadata;
import org.apache.spark.sql.types.StructField;
import org.apache.spark.sql.types.StructType;

List<Row> data = Arrays.asList(
  RowFactory.create(0L, 1L, 1.0),
  RowFactory.create(0L, 2L, 1.0),
  RowFactory.create(1L, 2L, 1.0),
  RowFactory.create(3L, 4L, 1.0),
  RowFactory.create(4L, 0L, 0.1)
);

StructType schema = new StructType(new StructField[]{
  new StructField("src", DataTypes.LongType, false, Metadata.empty()),
  new StructField("dst", DataTypes.LongType, false, Metadata.empty()),
  new StructField("weight", DataTypes.DoubleType, false, Metadata.empty())
});

Dataset<Row> df = spark.createDataFrame(data, schema);

PowerIterationClustering model = new PowerIterationClustering()
  .setK(2)
  .setMaxIter(10)
  .setInitMode("degree")
  .setWeightCol("weight");

Dataset<Row> result = model.assignClusters(df);
result.show(false);
```

Find full example code at "examples/src/main/java/org/apache/spark/examples/ml/JavaPowerIterationClusteringExample.java" in the Spark repo.
Refer to the [R API docs](https://spark.apache.org/docs/latest/api/R/reference/spark.powerIterationClustering.html) for more details.

```
df <- createDataFrame(list(list(0L, 1L, 1.0), list(0L, 2L, 1.0),
                           list(1L, 2L, 1.0), list(3L, 4L, 1.0),
                           list(4L, 0L, 0.1)),
                      schema = c("src", "dst", "weight"))
# assign clusters
clusters <- spark.assignClusters(df, k = 2L, maxIter = 20L,
                                 initMode = "degree", weightCol = "weight")

showDF(arrange(clusters, clusters$id))
```

Find full example code at "examples/src/main/r/ml/powerIterationClustering.R" in the Spark repo.
