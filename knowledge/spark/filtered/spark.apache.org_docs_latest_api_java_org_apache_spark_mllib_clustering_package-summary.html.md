[Skip navigation links](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/clustering/package-summary.html#skip-navbar-top "Skip navigation links")
  * [Overview](https://spark.apache.org/docs/latest/api/java/index.html)
  * Package
  * Class
  * [Deprecated](https://spark.apache.org/docs/latest/api/java/deprecated-list.html)
  * [Index](https://spark.apache.org/docs/latest/api/java/index-all.html)
  * [Help](https://spark.apache.org/docs/latest/api/java/help-doc.html#package)


  * Package: 
  * Description | 
  * [Related Packages](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/clustering/package-summary.html#related-package-summary) | 
  * [Classes and Interfaces](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/clustering/package-summary.html#class-summary)


SEARCH:
# Package org.apache.spark.mllib.clustering
* * *
package org.apache.spark.mllib.clustering
  * Related Packages
Package
Description
[org.apache.spark.mllib](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/package-summary.html)
RDD-based machine learning APIs (in maintenance mode).
  * All Classes and InterfacesInterfacesClasses
Class
Description
[BisectingKMeans](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/clustering/BisectingKMeans.html "class in org.apache.spark.mllib.clustering")
A bisecting k-means algorithm based on the paper "A comparison of document clustering techniques" by Steinbach, Karypis, and Kumar, with modification to fit Spark.
[BisectingKMeansModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/clustering/BisectingKMeansModel.html "class in org.apache.spark.mllib.clustering")
Clustering model produced by [`BisectingKMeans`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/clustering/BisectingKMeans.html "class in org.apache.spark.mllib.clustering").
[BisectingKMeansModel.SaveLoadV1_0$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/clustering/BisectingKMeansModel.SaveLoadV1_0$.html "class in org.apache.spark.mllib.clustering")
[BisectingKMeansModel.SaveLoadV2_0$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/clustering/BisectingKMeansModel.SaveLoadV2_0$.html "class in org.apache.spark.mllib.clustering")
[BisectingKMeansModel.SaveLoadV3_0$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/clustering/BisectingKMeansModel.SaveLoadV3_0$.html "class in org.apache.spark.mllib.clustering")
[DistributedLDAModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/clustering/DistributedLDAModel.html "class in org.apache.spark.mllib.clustering")
Distributed LDA model.
[EMLDAOptimizer](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/clustering/EMLDAOptimizer.html "class in org.apache.spark.mllib.clustering")
Optimizer for EM algorithm which stores data + parameter graph, plus algorithm parameters.
[ExpectationSum](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/clustering/ExpectationSum.html "class in org.apache.spark.mllib.clustering")
[GaussianMixture](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/clustering/GaussianMixture.html "class in org.apache.spark.mllib.clustering")
This class performs expectation maximization for multivariate Gaussian Mixture Models (GMMs).
[GaussianMixtureModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/clustering/GaussianMixtureModel.html "class in org.apache.spark.mllib.clustering")
Multivariate Gaussian Mixture Model (GMM) consisting of k Gaussians, where points are drawn from each Gaussian i=1..k with probability w(i); mu(i) and sigma(i) are the respective mean and covariance for each Gaussian distribution i=1..k.
[KMeans](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/clustering/KMeans.html "class in org.apache.spark.mllib.clustering")
K-means clustering with a k-means++ like initialization mode (the k-means|| algorithm by Bahmani et al).
[KMeansModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/clustering/KMeansModel.html "class in org.apache.spark.mllib.clustering")
A clustering model for K-means.
[KMeansModel.Cluster$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/clustering/KMeansModel.Cluster$.html "class in org.apache.spark.mllib.clustering")
[KMeansModel.SaveLoadV1_0$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/clustering/KMeansModel.SaveLoadV1_0$.html "class in org.apache.spark.mllib.clustering")
[KMeansModel.SaveLoadV2_0$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/clustering/KMeansModel.SaveLoadV2_0$.html "class in org.apache.spark.mllib.clustering")
[LDA](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/clustering/LDA.html "class in org.apache.spark.mllib.clustering")
Latent Dirichlet Allocation (LDA), a topic model designed for text documents.
[LDAModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/clustering/LDAModel.html "class in org.apache.spark.mllib.clustering")
Latent Dirichlet Allocation (LDA) model.
[LDAOptimizer](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/clustering/LDAOptimizer.html "interface in org.apache.spark.mllib.clustering")
An LDAOptimizer specifies which optimization/learning/inference algorithm to use, and it can hold optimizer-specific parameters for users to set.
[LDAUtils](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/clustering/LDAUtils.html "class in org.apache.spark.mllib.clustering")
Utility methods for LDA.
[LocalKMeans](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/clustering/LocalKMeans.html "class in org.apache.spark.mllib.clustering")
An utility object to run K-means locally.
[LocalLDAModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/clustering/LocalLDAModel.html "class in org.apache.spark.mllib.clustering")
Local LDA model.
[OnlineLDAOptimizer](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/clustering/OnlineLDAOptimizer.html "class in org.apache.spark.mllib.clustering")
An online optimizer for LDA.
[PowerIterationClustering](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/clustering/PowerIterationClustering.html "class in org.apache.spark.mllib.clustering")
Power Iteration Clustering (PIC), a scalable graph clustering algorithm developed by [Lin and Cohen](http://www.cs.cmu.edu/~frank/papers/icml2010-pic-final.pdf).
[PowerIterationClustering.Assignment](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/clustering/PowerIterationClustering.Assignment.html "class in org.apache.spark.mllib.clustering")
Cluster assignment.
[PowerIterationClustering.Assignment$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/clustering/PowerIterationClustering.Assignment$.html "class in org.apache.spark.mllib.clustering")
[PowerIterationClusteringModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/clustering/PowerIterationClusteringModel.html "class in org.apache.spark.mllib.clustering")
Model produced by [`PowerIterationClustering`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/clustering/PowerIterationClustering.html "class in org.apache.spark.mllib.clustering").
[PowerIterationClusteringModel.SaveLoadV1_0$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/clustering/PowerIterationClusteringModel.SaveLoadV1_0$.html "class in org.apache.spark.mllib.clustering")
[StreamingKMeans](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/clustering/StreamingKMeans.html "class in org.apache.spark.mllib.clustering")
StreamingKMeans provides methods for configuring a streaming k-means analysis, training the model on streaming, and using the model to make predictions on streaming data.
[StreamingKMeansModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/clustering/StreamingKMeansModel.html "class in org.apache.spark.mllib.clustering")
StreamingKMeansModel extends MLlib's KMeansModel for streaming algorithms, so it can keep track of a continuously updated weight associated with each cluster, and also update the model by doing a single iteration of the standard k-means algorithm.


