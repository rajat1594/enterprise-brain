[Skip navigation links](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/evaluation/package-summary.html#skip-navbar-top "Skip navigation links")
  * [Overview](https://spark.apache.org/docs/latest/api/java/index.html)
  * Package
  * Class
  * [Deprecated](https://spark.apache.org/docs/latest/api/java/deprecated-list.html)
  * [Index](https://spark.apache.org/docs/latest/api/java/index-all.html)
  * [Help](https://spark.apache.org/docs/latest/api/java/help-doc.html#package)


  * Package: 
  * Description | 
  * [Related Packages](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/evaluation/package-summary.html#related-package-summary) | 
  * [Classes and Interfaces](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/evaluation/package-summary.html#class-summary)


SEARCH:
# Package org.apache.spark.ml.evaluation
* * *
package org.apache.spark.ml.evaluation
  * Related Packages
Package
Description
[org.apache.spark.ml](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/package-summary.html)
DataFrame-based machine learning APIs to let users quickly assemble and configure practical machine learning pipelines.
  * Classes
Class
Description
[BinaryClassificationEvaluator](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/evaluation/BinaryClassificationEvaluator.html "class in org.apache.spark.ml.evaluation")
Evaluator for binary classification, which expects input columns rawPrediction, label and an optional weight column.
[ClusteringEvaluator](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/evaluation/ClusteringEvaluator.html "class in org.apache.spark.ml.evaluation")
Evaluator for clustering results.
[ClusteringMetrics](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/evaluation/ClusteringMetrics.html "class in org.apache.spark.ml.evaluation")
Metrics for clustering, which expects two input columns: prediction and label.
[CosineSilhouette](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/evaluation/CosineSilhouette.html "class in org.apache.spark.ml.evaluation")
The algorithm which is implemented in this object, instead, is an efficient and parallel implementation of the Silhouette using the cosine distance measure.
[Evaluator](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/evaluation/Evaluator.html "class in org.apache.spark.ml.evaluation")
Abstract class for evaluators that compute metrics from predictions.
[MulticlassClassificationEvaluator](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/evaluation/MulticlassClassificationEvaluator.html "class in org.apache.spark.ml.evaluation")
Evaluator for multiclass classification, which expects input columns: prediction, label, weight (optional) and probability (only for logLoss).
[MultilabelClassificationEvaluator](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/evaluation/MultilabelClassificationEvaluator.html "class in org.apache.spark.ml.evaluation")
Experimental Evaluator for multi-label classification, which expects two input columns: prediction and label.
[RankingEvaluator](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/evaluation/RankingEvaluator.html "class in org.apache.spark.ml.evaluation")
Experimental Evaluator for ranking, which expects two input columns: prediction and label.
[RegressionEvaluator](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/evaluation/RegressionEvaluator.html "class in org.apache.spark.ml.evaluation")
Evaluator for regression, which expects input columns prediction, label and an optional weight column.
[SquaredEuclideanSilhouette](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/evaluation/SquaredEuclideanSilhouette.html "class in org.apache.spark.ml.evaluation")
SquaredEuclideanSilhouette computes the average of the Silhouette over all the data of the dataset, which is a measure of how appropriately the data have been clustered.
[SquaredEuclideanSilhouette.ClusterStats](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/evaluation/SquaredEuclideanSilhouette.ClusterStats.html "class in org.apache.spark.ml.evaluation")
[SquaredEuclideanSilhouette.ClusterStats$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/evaluation/SquaredEuclideanSilhouette.ClusterStats$.html "class in org.apache.spark.ml.evaluation")


