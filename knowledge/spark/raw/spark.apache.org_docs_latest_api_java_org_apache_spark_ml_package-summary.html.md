[Skip navigation links](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/package-summary.html#skip-navbar-top "Skip navigation links")
  * [Overview](https://spark.apache.org/docs/latest/api/java/index.html)
  * Package
  * Class
  * [Deprecated](https://spark.apache.org/docs/latest/api/java/deprecated-list.html)
  * [Index](https://spark.apache.org/docs/latest/api/java/index-all.html)
  * [Help](https://spark.apache.org/docs/latest/api/java/help-doc.html#package)


  * Package: 
  * [Description](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/package-summary.html#package-description) | 
  * [Related Packages](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/package-summary.html#related-package-summary) | 
  * [Classes and Interfaces](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/package-summary.html#class-summary)


SEARCH:
# Package org.apache.spark.ml
* * *
package org.apache.spark.ml
DataFrame-based machine learning APIs to let users quickly assemble and configure practical machine learning pipelines.
  * Related Packages
Package
Description
[org.apache.spark](https://spark.apache.org/docs/latest/api/java/org/apache/spark/package-summary.html)
Core Spark classes in Scala.
[org.apache.spark.ml.ann](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/ann/package-summary.html)
[org.apache.spark.ml.attribute](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/attribute/package-summary.html)
ML attributes
[org.apache.spark.ml.classification](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/package-summary.html)
[org.apache.spark.ml.clustering](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/clustering/package-summary.html)
[org.apache.spark.ml.evaluation](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/evaluation/package-summary.html)
[org.apache.spark.ml.feature](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/package-summary.html)
Feature transformers The `ml.feature` package provides common feature transformers that help convert raw data or features into more suitable forms for model fitting.
[org.apache.spark.ml.fpm](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/fpm/package-summary.html)
[org.apache.spark.ml.image](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/image/package-summary.html)
[org.apache.spark.ml.impl](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/impl/package-summary.html)
[org.apache.spark.ml.linalg](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/linalg/package-summary.html)
[org.apache.spark.ml.optim](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/optim/package-summary.html)
[org.apache.spark.ml.param](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/param/package-summary.html)
[org.apache.spark.ml.r](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/r/package-summary.html)
[org.apache.spark.ml.recommendation](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/recommendation/package-summary.html)
[org.apache.spark.ml.regression](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/regression/package-summary.html)
[org.apache.spark.ml.stat](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/stat/package-summary.html)
[org.apache.spark.ml.tree](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/tree/package-summary.html)
[org.apache.spark.ml.tuning](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/tuning/package-summary.html)
[org.apache.spark.ml.util](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/util/package-summary.html)
  * All Classes and InterfacesInterfacesClasses
Class
Description
[Estimator](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/Estimator.html "class in org.apache.spark.ml")<M extends [Model](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/Model.html "class in org.apache.spark.ml")<M>>
Abstract class for estimators that fit models to data.
[EstimatorUtils](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/EstimatorUtils.html "class in org.apache.spark.ml")
[FitEnd](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/FitEnd.html "class in org.apache.spark.ml")<M extends [Model](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/Model.html "class in org.apache.spark.ml")<M>>
Event fired after `Estimator.fit`.
[FitStart](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/FitStart.html "class in org.apache.spark.ml")<M extends [Model](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/Model.html "class in org.apache.spark.ml")<M>>
Event fired before `Estimator.fit`.
[functions](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/functions.html "class in org.apache.spark.ml")
[LoadInstanceEnd](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/LoadInstanceEnd.html "class in org.apache.spark.ml")<T>
Event fired after `MLReader.load`.
[LoadInstanceStart](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/LoadInstanceStart.html "class in org.apache.spark.ml")<T>
Event fired before `MLReader.load`.
[MLEvent](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/MLEvent.html "interface in org.apache.spark.ml")
Event emitted by ML operations.
[MLEvents](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/MLEvents.html "interface in org.apache.spark.ml")
A small trait that defines some methods to send [`MLEvent`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/MLEvent.html "interface in org.apache.spark.ml").
[Model](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/Model.html "class in org.apache.spark.ml")<M extends [Model](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/Model.html "class in org.apache.spark.ml")<M>>
A fitted model, i.e., a [`Transformer`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/Transformer.html "class in org.apache.spark.ml") produced by an [`Estimator`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/Estimator.html "class in org.apache.spark.ml").
[Pipeline](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/Pipeline.html "class in org.apache.spark.ml")
A simple pipeline, which acts as an estimator.
[Pipeline.SharedReadWrite$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/Pipeline.SharedReadWrite$.html "class in org.apache.spark.ml")
Methods for `MLReader` and `MLWriter` shared between [`Pipeline`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/Pipeline.html "class in org.apache.spark.ml") and [`PipelineModel`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/PipelineModel.html "class in org.apache.spark.ml")
[PipelineModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/PipelineModel.html "class in org.apache.spark.ml")
Represents a fitted pipeline.
[PipelineStage](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/PipelineStage.html "class in org.apache.spark.ml")
A stage in a pipeline, either an [`Estimator`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/Estimator.html "class in org.apache.spark.ml") or a [`Transformer`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/Transformer.html "class in org.apache.spark.ml").
[PredictionModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/PredictionModel.html "class in org.apache.spark.ml")<FeaturesType,M extends [PredictionModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/PredictionModel.html "class in org.apache.spark.ml")<FeaturesType,M>>
Abstraction for a model for prediction tasks (regression and classification).
[Predictor](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/Predictor.html "class in org.apache.spark.ml")<FeaturesType,Learner extends [Predictor](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/Predictor.html "class in org.apache.spark.ml")<FeaturesType,Learner,M>,M extends [PredictionModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/PredictionModel.html "class in org.apache.spark.ml")<FeaturesType,M>>
Abstraction for prediction problems (regression and classification).
[PredictorParams](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/PredictorParams.html "interface in org.apache.spark.ml")
(private[ml]) Trait for parameters for prediction (regression and classification).
[SaveInstanceEnd](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/SaveInstanceEnd.html "class in org.apache.spark.ml")
Event fired after `MLWriter.save`.
[SaveInstanceStart](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/SaveInstanceStart.html "class in org.apache.spark.ml")
Event fired before `MLWriter.save`.
[TransformEnd](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/TransformEnd.html "class in org.apache.spark.ml")
Event fired after `Transformer.transform`.
[Transformer](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/Transformer.html "class in org.apache.spark.ml")
Abstract class for transformers that transform one dataset into another.
[TransformStart](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/TransformStart.html "class in org.apache.spark.ml")
Event fired before `Transformer.transform`.
[UnaryTransformer](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/UnaryTransformer.html "class in org.apache.spark.ml")<IN,OUT,T extends [UnaryTransformer](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/UnaryTransformer.html "class in org.apache.spark.ml")<IN,OUT,T>>
Abstract class for transformers that take one input column, apply transformation, and output the result as a new column.


