[Skip navigation links](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/tuning/package-summary.html#skip-navbar-top "Skip navigation links")
  * [Overview](https://spark.apache.org/docs/latest/api/java/index.html)
  * Package
  * Class
  * [Deprecated](https://spark.apache.org/docs/latest/api/java/deprecated-list.html)
  * [Index](https://spark.apache.org/docs/latest/api/java/index-all.html)
  * [Help](https://spark.apache.org/docs/latest/api/java/help-doc.html#package)

  * Package:
  * Description |
  * [Related Packages](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/tuning/package-summary.html#related-package-summary) |
  * [Classes and Interfaces](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/tuning/package-summary.html#class-summary)

SEARCH:
# Package org.apache.spark.ml.tuning
* * *
package org.apache.spark.ml.tuning
  * Related Packages
Package
Description
[org.apache.spark.ml](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/package-summary.html)
DataFrame-based machine learning APIs to let users quickly assemble and configure practical machine learning pipelines.
  * All Classes and InterfacesInterfacesClasses
Class
Description
[CrossValidator](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/tuning/CrossValidator.html "class in org.apache.spark.ml.tuning")
K-fold cross validation performs model selection by splitting the dataset into a set of non-overlapping randomly partitioned folds which are used as separate training and test datasets e.g., with k=3 folds, K-fold cross validation will generate 3 (training, test) dataset pairs, each of which uses 2/3 of the data for training and 1/3 for testing.
[CrossValidatorModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/tuning/CrossValidatorModel.html "class in org.apache.spark.ml.tuning")
CrossValidatorModel contains the model with the highest average cross-validation metric across folds and uses this model to transform input data.
[CrossValidatorModel.CrossValidatorModelWriter](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/tuning/CrossValidatorModel.CrossValidatorModelWriter.html "class in org.apache.spark.ml.tuning")
Writer for CrossValidatorModel.
[CrossValidatorParams](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/tuning/CrossValidatorParams.html "interface in org.apache.spark.ml.tuning")
Params for [`CrossValidator`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/tuning/CrossValidator.html "class in org.apache.spark.ml.tuning") and [`CrossValidatorModel`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/tuning/CrossValidatorModel.html "class in org.apache.spark.ml.tuning").
[ParamGridBuilder](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/tuning/ParamGridBuilder.html "class in org.apache.spark.ml.tuning")
Builder for a param grid used in grid search-based model selection.
[TrainValidationSplit](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/tuning/TrainValidationSplit.html "class in org.apache.spark.ml.tuning")
Validation for hyper-parameter tuning.
[TrainValidationSplitModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/tuning/TrainValidationSplitModel.html "class in org.apache.spark.ml.tuning")
Model from train validation split.
[TrainValidationSplitModel.TrainValidationSplitModelWriter](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/tuning/TrainValidationSplitModel.TrainValidationSplitModelWriter.html "class in org.apache.spark.ml.tuning")
Writer for TrainValidationSplitModel.
[TrainValidationSplitParams](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/tuning/TrainValidationSplitParams.html "interface in org.apache.spark.ml.tuning")
Params for [`TrainValidationSplit`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/tuning/TrainValidationSplit.html "class in org.apache.spark.ml.tuning") and [`TrainValidationSplitModel`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/tuning/TrainValidationSplitModel.html "class in org.apache.spark.ml.tuning").
[ValidatorParams](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/tuning/ValidatorParams.html "interface in org.apache.spark.ml.tuning")
Common params for [`TrainValidationSplitParams`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/tuning/TrainValidationSplitParams.html "interface in org.apache.spark.ml.tuning") and [`CrossValidatorParams`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/tuning/CrossValidatorParams.html "interface in org.apache.spark.ml.tuning").
