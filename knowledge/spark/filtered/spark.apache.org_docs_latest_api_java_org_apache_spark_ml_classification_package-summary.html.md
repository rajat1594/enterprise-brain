[Skip navigation links](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/package-summary.html#skip-navbar-top "Skip navigation links")
  * [Overview](https://spark.apache.org/docs/latest/api/java/index.html)
  * Package
  * Class
  * [Deprecated](https://spark.apache.org/docs/latest/api/java/deprecated-list.html)
  * [Index](https://spark.apache.org/docs/latest/api/java/index-all.html)
  * [Help](https://spark.apache.org/docs/latest/api/java/help-doc.html#package)


  * Package: 
  * Description | 
  * [Related Packages](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/package-summary.html#related-package-summary) | 
  * [Classes and Interfaces](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/package-summary.html#class-summary)


SEARCH:
# Package org.apache.spark.ml.classification
* * *
package org.apache.spark.ml.classification
  * Related Packages
Package
Description
[org.apache.spark.ml](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/package-summary.html)
DataFrame-based machine learning APIs to let users quickly assemble and configure practical machine learning pipelines.
  * All Classes and InterfacesInterfacesClasses
Class
Description
[BinaryClassificationSummary](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/BinaryClassificationSummary.html "interface in org.apache.spark.ml.classification")
Abstraction for binary classification results for a given model.
[BinaryLogisticRegressionSummary](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/BinaryLogisticRegressionSummary.html "interface in org.apache.spark.ml.classification")
Abstraction for binary logistic regression results for a given model.
[BinaryLogisticRegressionSummaryImpl](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/BinaryLogisticRegressionSummaryImpl.html "class in org.apache.spark.ml.classification")
Binary logistic regression results for a given model.
[BinaryLogisticRegressionTrainingSummary](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/BinaryLogisticRegressionTrainingSummary.html "interface in org.apache.spark.ml.classification")
Abstraction for binary logistic regression training results.
[BinaryLogisticRegressionTrainingSummaryImpl](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/BinaryLogisticRegressionTrainingSummaryImpl.html "class in org.apache.spark.ml.classification")
Binary logistic regression training results.
[BinaryRandomForestClassificationSummary](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/BinaryRandomForestClassificationSummary.html "interface in org.apache.spark.ml.classification")
Abstraction for BinaryRandomForestClassification results for a given model.
[BinaryRandomForestClassificationSummaryImpl](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/BinaryRandomForestClassificationSummaryImpl.html "class in org.apache.spark.ml.classification")
Binary RandomForestClassification for a given model.
[BinaryRandomForestClassificationTrainingSummary](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/BinaryRandomForestClassificationTrainingSummary.html "interface in org.apache.spark.ml.classification")
Abstraction for BinaryRandomForestClassification training results.
[BinaryRandomForestClassificationTrainingSummaryImpl](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/BinaryRandomForestClassificationTrainingSummaryImpl.html "class in org.apache.spark.ml.classification")
Binary RandomForestClassification training results.
[ClassificationModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/ClassificationModel.html "class in org.apache.spark.ml.classification")<FeaturesType,M extends [ClassificationModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/ClassificationModel.html "class in org.apache.spark.ml.classification")<FeaturesType,M>>
Model produced by a [`Classifier`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/Classifier.html "class in org.apache.spark.ml.classification").
[ClassificationSummary](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/ClassificationSummary.html "interface in org.apache.spark.ml.classification")
Abstraction for multiclass classification results for a given model.
[Classifier](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/Classifier.html "class in org.apache.spark.ml.classification")<FeaturesType,E extends [Classifier](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/Classifier.html "class in org.apache.spark.ml.classification")<FeaturesType,E,M>,M extends [ClassificationModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/ClassificationModel.html "class in org.apache.spark.ml.classification")<FeaturesType,M>>
Single-label binary or multiclass classification.
[ClassifierParams](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/ClassifierParams.html "interface in org.apache.spark.ml.classification")
(private[spark]) Params for classification.
[ClassifierTypeTrait](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/ClassifierTypeTrait.html "interface in org.apache.spark.ml.classification")
[DecisionTreeClassificationModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/DecisionTreeClassificationModel.html "class in org.apache.spark.ml.classification")
Decision tree model (http://en.wikipedia.org/wiki/Decision_tree_learning) for classification.
[DecisionTreeClassifier](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/DecisionTreeClassifier.html "class in org.apache.spark.ml.classification")
Decision tree learning algorithm (http://en.wikipedia.org/wiki/Decision_tree_learning) for classification.
[FMClassificationModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/FMClassificationModel.html "class in org.apache.spark.ml.classification")
Model produced by [`FMClassifier`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/FMClassifier.html "class in org.apache.spark.ml.classification")
[FMClassificationModel.Data$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/FMClassificationModel.Data$.html "class in org.apache.spark.ml.classification")
[FMClassificationSummary](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/FMClassificationSummary.html "interface in org.apache.spark.ml.classification")
Abstraction for FMClassifier results for a given model.
[FMClassificationSummaryImpl](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/FMClassificationSummaryImpl.html "class in org.apache.spark.ml.classification")
FMClassifier results for a given model.
[FMClassificationTrainingSummary](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/FMClassificationTrainingSummary.html "interface in org.apache.spark.ml.classification")
Abstraction for FMClassifier training results.
[FMClassificationTrainingSummaryImpl](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/FMClassificationTrainingSummaryImpl.html "class in org.apache.spark.ml.classification")
FMClassifier training results.
[FMClassifier](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/FMClassifier.html "class in org.apache.spark.ml.classification")
Factorization Machines learning algorithm for classification.
[FMClassifierParams](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/FMClassifierParams.html "interface in org.apache.spark.ml.classification")
Params for FMClassifier.
[GBTClassificationModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/GBTClassificationModel.html "class in org.apache.spark.ml.classification")
Gradient-Boosted Trees (GBTs) (http://en.wikipedia.org/wiki/Gradient_boosting) model for classification.
[GBTClassifier](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/GBTClassifier.html "class in org.apache.spark.ml.classification")
Gradient-Boosted Trees (GBTs) (http://en.wikipedia.org/wiki/Gradient_boosting) learning algorithm for classification.
[LinearSVC](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/LinearSVC.html "class in org.apache.spark.ml.classification")
[ Linear SVM Classifier](https://en.wikipedia.org/wiki/Support_vector_machine#Linear_SVM)
[LinearSVCModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/LinearSVCModel.html "class in org.apache.spark.ml.classification")
Linear SVM Model trained by [`LinearSVC`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/LinearSVC.html "class in org.apache.spark.ml.classification")
[LinearSVCModel.Data$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/LinearSVCModel.Data$.html "class in org.apache.spark.ml.classification")
[LinearSVCParams](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/LinearSVCParams.html "interface in org.apache.spark.ml.classification")
Params for linear SVM Classifier.
[LinearSVCSummary](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/LinearSVCSummary.html "interface in org.apache.spark.ml.classification")
Abstraction for LinearSVC results for a given model.
[LinearSVCSummaryImpl](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/LinearSVCSummaryImpl.html "class in org.apache.spark.ml.classification")
LinearSVC results for a given model.
[LinearSVCTrainingSummary](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/LinearSVCTrainingSummary.html "interface in org.apache.spark.ml.classification")
Abstraction for LinearSVC training results.
[LinearSVCTrainingSummaryImpl](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/LinearSVCTrainingSummaryImpl.html "class in org.apache.spark.ml.classification")
LinearSVC training results.
[LogisticRegression](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/LogisticRegression.html "class in org.apache.spark.ml.classification")
Logistic regression.
[LogisticRegressionModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/LogisticRegressionModel.html "class in org.apache.spark.ml.classification")
Model produced by [`LogisticRegression`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/LogisticRegression.html "class in org.apache.spark.ml.classification").
[LogisticRegressionModel.Data$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/LogisticRegressionModel.Data$.html "class in org.apache.spark.ml.classification")
[LogisticRegressionParams](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/LogisticRegressionParams.html "interface in org.apache.spark.ml.classification")
Params for logistic regression.
[LogisticRegressionSummary](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/LogisticRegressionSummary.html "interface in org.apache.spark.ml.classification")
Abstraction for logistic regression results for a given model.
[LogisticRegressionSummaryImpl](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/LogisticRegressionSummaryImpl.html "class in org.apache.spark.ml.classification")
Multiclass logistic regression results for a given model.
[LogisticRegressionTrainingSummary](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/LogisticRegressionTrainingSummary.html "interface in org.apache.spark.ml.classification")
Abstraction for multiclass logistic regression training results.
[LogisticRegressionTrainingSummaryImpl](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/LogisticRegressionTrainingSummaryImpl.html "class in org.apache.spark.ml.classification")
Multiclass logistic regression training results.
[MultilayerPerceptronClassificationModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/MultilayerPerceptronClassificationModel.html "class in org.apache.spark.ml.classification")
Classification model based on the Multilayer Perceptron.
[MultilayerPerceptronClassificationModel.Data$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/MultilayerPerceptronClassificationModel.Data$.html "class in org.apache.spark.ml.classification")
[MultilayerPerceptronClassificationSummary](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/MultilayerPerceptronClassificationSummary.html "interface in org.apache.spark.ml.classification")
Abstraction for MultilayerPerceptronClassification results for a given model.
[MultilayerPerceptronClassificationSummaryImpl](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/MultilayerPerceptronClassificationSummaryImpl.html "class in org.apache.spark.ml.classification")
MultilayerPerceptronClassification results for a given model.
[MultilayerPerceptronClassificationTrainingSummary](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/MultilayerPerceptronClassificationTrainingSummary.html "interface in org.apache.spark.ml.classification")
Abstraction for MultilayerPerceptronClassification training results.
[MultilayerPerceptronClassificationTrainingSummaryImpl](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/MultilayerPerceptronClassificationTrainingSummaryImpl.html "class in org.apache.spark.ml.classification")
MultilayerPerceptronClassification training results.
[MultilayerPerceptronClassifier](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/MultilayerPerceptronClassifier.html "class in org.apache.spark.ml.classification")
Classifier trainer based on the Multilayer Perceptron.
[MultilayerPerceptronParams](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/MultilayerPerceptronParams.html "interface in org.apache.spark.ml.classification")
Params for Multilayer Perceptron.
[NaiveBayes](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/NaiveBayes.html "class in org.apache.spark.ml.classification")
Naive Bayes Classifiers.
[NaiveBayesModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/NaiveBayesModel.html "class in org.apache.spark.ml.classification")
Model produced by [`NaiveBayes`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/NaiveBayes.html "class in org.apache.spark.ml.classification")
[NaiveBayesModel.Data$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/NaiveBayesModel.Data$.html "class in org.apache.spark.ml.classification")
[NaiveBayesParams](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/NaiveBayesParams.html "interface in org.apache.spark.ml.classification")
Params for Naive Bayes Classifiers.
[OneVsRest](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/OneVsRest.html "class in org.apache.spark.ml.classification")
Reduction of Multiclass Classification to Binary Classification.
[OneVsRestModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/OneVsRestModel.html "class in org.apache.spark.ml.classification")
Model produced by [`OneVsRest`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/OneVsRest.html "class in org.apache.spark.ml.classification").
[OneVsRestParams](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/OneVsRestParams.html "interface in org.apache.spark.ml.classification")
Params for [`OneVsRest`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/OneVsRest.html "class in org.apache.spark.ml.classification").
[ProbabilisticClassificationModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/ProbabilisticClassificationModel.html "class in org.apache.spark.ml.classification")<FeaturesType,M extends [ProbabilisticClassificationModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/ProbabilisticClassificationModel.html "class in org.apache.spark.ml.classification")<FeaturesType,M>>
Model produced by a [`ProbabilisticClassifier`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/ProbabilisticClassifier.html "class in org.apache.spark.ml.classification").
[ProbabilisticClassifier](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/ProbabilisticClassifier.html "class in org.apache.spark.ml.classification")<FeaturesType,E extends [ProbabilisticClassifier](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/ProbabilisticClassifier.html "class in org.apache.spark.ml.classification")<FeaturesType,E,M>,M extends [ProbabilisticClassificationModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/ProbabilisticClassificationModel.html "class in org.apache.spark.ml.classification")<FeaturesType,M>>
Single-label binary or multiclass classifier which can output class conditional probabilities.
[ProbabilisticClassifierParams](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/ProbabilisticClassifierParams.html "interface in org.apache.spark.ml.classification")
(private[classification]) Params for probabilistic classification.
[RandomForestClassificationModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/RandomForestClassificationModel.html "class in org.apache.spark.ml.classification")
[Random Forest](http://en.wikipedia.org/wiki/Random_forest) model for classification.
[RandomForestClassificationSummary](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/RandomForestClassificationSummary.html "interface in org.apache.spark.ml.classification")
Abstraction for multiclass RandomForestClassification results for a given model.
[RandomForestClassificationSummaryImpl](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/RandomForestClassificationSummaryImpl.html "class in org.apache.spark.ml.classification")
Multiclass RandomForestClassification results for a given model.
[RandomForestClassificationTrainingSummary](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/RandomForestClassificationTrainingSummary.html "interface in org.apache.spark.ml.classification")
Abstraction for multiclass RandomForestClassification training results.
[RandomForestClassificationTrainingSummaryImpl](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/RandomForestClassificationTrainingSummaryImpl.html "class in org.apache.spark.ml.classification")
Multiclass RandomForestClassification training results.
[RandomForestClassifier](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/RandomForestClassifier.html "class in org.apache.spark.ml.classification")
[Random Forest](http://en.wikipedia.org/wiki/Random_forest) learning algorithm for classification.
[TrainingSummary](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/classification/TrainingSummary.html "interface in org.apache.spark.ml.classification")
Abstraction for training results.


