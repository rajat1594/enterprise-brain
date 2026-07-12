[Skip navigation links](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/clustering/package-summary.html#skip-navbar-top "Skip navigation links")
  * [Overview](https://spark.apache.org/docs/latest/api/java/index.html)
  * Package
  * Class
  * [Deprecated](https://spark.apache.org/docs/latest/api/java/deprecated-list.html)
  * [Index](https://spark.apache.org/docs/latest/api/java/index-all.html)
  * [Help](https://spark.apache.org/docs/latest/api/java/help-doc.html#package)

  * Package:
  * Description |
  * [Related Packages](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/clustering/package-summary.html#related-package-summary) |
  * [Classes and Interfaces](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/clustering/package-summary.html#class-summary)

SEARCH:
# Package org.apache.spark.ml.clustering
* * *
package org.apache.spark.ml.clustering
  * Related Packages
Package
Description
[org.apache.spark.ml](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/package-summary.html)
DataFrame-based machine learning APIs to let users quickly assemble and configure practical machine learning pipelines.
  * All Classes and InterfacesInterfacesClasses
Class
Description
[BisectingKMeans](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/clustering/BisectingKMeans.html "class in org.apache.spark.ml.clustering")
A bisecting k-means algorithm based on the paper "A comparison of document clustering techniques" by Steinbach, Karypis, and Kumar, with modification to fit Spark.
[BisectingKMeansModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/clustering/BisectingKMeansModel.html "class in org.apache.spark.ml.clustering")
Model fitted by BisectingKMeans.
[BisectingKMeansParams](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/clustering/BisectingKMeansParams.html "interface in org.apache.spark.ml.clustering")
Common params for BisectingKMeans and BisectingKMeansModel
[BisectingKMeansSummary](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/clustering/BisectingKMeansSummary.html "class in org.apache.spark.ml.clustering")
Summary of BisectingKMeans.
[ClusteringSummary](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/clustering/ClusteringSummary.html "class in org.apache.spark.ml.clustering")
Summary of clustering algorithms.
[DistributedLDAModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/clustering/DistributedLDAModel.html "class in org.apache.spark.ml.clustering")
Distributed model fitted by [`LDA`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/clustering/LDA.html "class in org.apache.spark.ml.clustering").
[ExpectationAggregator](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/clustering/ExpectationAggregator.html "class in org.apache.spark.ml.clustering")
ExpectationAggregator computes the partial expectation results.
[GaussianMixture](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/clustering/GaussianMixture.html "class in org.apache.spark.ml.clustering")
Gaussian Mixture clustering.
[GaussianMixtureModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/clustering/GaussianMixtureModel.html "class in org.apache.spark.ml.clustering")
Multivariate Gaussian Mixture Model (GMM) consisting of k Gaussians, where points are drawn from each Gaussian i with probability weights(i).
[GaussianMixtureModel.Data$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/clustering/GaussianMixtureModel.Data$.html "class in org.apache.spark.ml.clustering")
[GaussianMixtureParams](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/clustering/GaussianMixtureParams.html "interface in org.apache.spark.ml.clustering")
Common params for GaussianMixture and GaussianMixtureModel
[GaussianMixtureSummary](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/clustering/GaussianMixtureSummary.html "class in org.apache.spark.ml.clustering")
Summary of GaussianMixture.
[InternalKMeansModelWriter](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/clustering/InternalKMeansModelWriter.html "class in org.apache.spark.ml.clustering")
A writer for KMeans that handles the "internal" (or default) format
[KMeans](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/clustering/KMeans.html "class in org.apache.spark.ml.clustering")
K-means clustering with support for k-means|| initialization proposed by Bahmani et al.
[KMeansAggregator](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/clustering/KMeansAggregator.html "class in org.apache.spark.ml.clustering")
KMeansAggregator computes the distances and updates the centers for blocks in sparse or dense matrix in an online fashion.
[KMeansModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/clustering/KMeansModel.html "class in org.apache.spark.ml.clustering")
Model fitted by KMeans.
[KMeansModel.OldData$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/clustering/KMeansModel.OldData$.html "class in org.apache.spark.ml.clustering")
[KMeansParams](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/clustering/KMeansParams.html "interface in org.apache.spark.ml.clustering")
Common params for KMeans and KMeansModel
[KMeansSummary](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/clustering/KMeansSummary.html "class in org.apache.spark.ml.clustering")
Summary of KMeans.
[LDA](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/clustering/LDA.html "class in org.apache.spark.ml.clustering")
Latent Dirichlet Allocation (LDA), a topic model designed for text documents.
[LDAModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/clustering/LDAModel.html "class in org.apache.spark.ml.clustering")
Model fitted by [`LDA`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/clustering/LDA.html "class in org.apache.spark.ml.clustering").
[LDAParams](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/clustering/LDAParams.html "interface in org.apache.spark.ml.clustering")
[LocalLDAModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/clustering/LocalLDAModel.html "class in org.apache.spark.ml.clustering")
Local (non-distributed) model fitted by [`LDA`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/clustering/LDA.html "class in org.apache.spark.ml.clustering").
[LocalLDAModel.LocalModelData$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/clustering/LocalLDAModel.LocalModelData$.html "class in org.apache.spark.ml.clustering")
[PMMLKMeansModelWriter](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/clustering/PMMLKMeansModelWriter.html "class in org.apache.spark.ml.clustering")
A writer for KMeans that handles the "pmml" format
[PowerIterationClustering](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/clustering/PowerIterationClustering.html "class in org.apache.spark.ml.clustering")
Power Iteration Clustering (PIC), a scalable graph clustering algorithm developed by [Lin and Cohen](http://www.cs.cmu.edu/~frank/papers/icml2010-pic-final.pdf).
[PowerIterationClusteringParams](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/clustering/PowerIterationClusteringParams.html "interface in org.apache.spark.ml.clustering")
Common params for PowerIterationClustering
