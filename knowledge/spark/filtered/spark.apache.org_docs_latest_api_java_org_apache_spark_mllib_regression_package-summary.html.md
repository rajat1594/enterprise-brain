[Skip navigation links](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/regression/package-summary.html#skip-navbar-top "Skip navigation links")
  * [Overview](https://spark.apache.org/docs/latest/api/java/index.html)
  * Package
  * Class
  * [Deprecated](https://spark.apache.org/docs/latest/api/java/deprecated-list.html)
  * [Index](https://spark.apache.org/docs/latest/api/java/index-all.html)
  * [Help](https://spark.apache.org/docs/latest/api/java/help-doc.html#package)


  * Package: 
  * Description | 
  * [Related Packages](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/regression/package-summary.html#related-package-summary) | 
  * [Classes and Interfaces](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/regression/package-summary.html#class-summary)


SEARCH:
# Package org.apache.spark.mllib.regression
* * *
package org.apache.spark.mllib.regression
  * Related Packages
Package
Description
[org.apache.spark.mllib](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/package-summary.html)
RDD-based machine learning APIs (in maintenance mode).
[org.apache.spark.mllib.regression.impl](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/regression/impl/package-summary.html)
  * All Classes and InterfacesInterfacesClasses
Class
Description
[GeneralizedLinearAlgorithm](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/regression/GeneralizedLinearAlgorithm.html "class in org.apache.spark.mllib.regression")<M extends [GeneralizedLinearModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/regression/GeneralizedLinearModel.html "class in org.apache.spark.mllib.regression")>
GeneralizedLinearAlgorithm implements methods to train a Generalized Linear Model (GLM).
[GeneralizedLinearModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/regression/GeneralizedLinearModel.html "class in org.apache.spark.mllib.regression")
GeneralizedLinearModel (GLM) represents a model trained using GeneralizedLinearAlgorithm.
[IsotonicRegression](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/regression/IsotonicRegression.html "class in org.apache.spark.mllib.regression")
Isotonic regression.
[IsotonicRegressionModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/regression/IsotonicRegressionModel.html "class in org.apache.spark.mllib.regression")
Regression model for isotonic regression.
[LabeledPoint](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/regression/LabeledPoint.html "class in org.apache.spark.mllib.regression")
Class that represents the features and labels of a data point.
[LassoModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/regression/LassoModel.html "class in org.apache.spark.mllib.regression")
Regression model trained using Lasso.
[LassoWithSGD](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/regression/LassoWithSGD.html "class in org.apache.spark.mllib.regression")
Train a regression model with L1-regularization using Stochastic Gradient Descent.
[LinearRegressionModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/regression/LinearRegressionModel.html "class in org.apache.spark.mllib.regression")
Regression model trained using LinearRegression.
[LinearRegressionWithSGD](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/regression/LinearRegressionWithSGD.html "class in org.apache.spark.mllib.regression")
Train a linear regression model with no regularization using Stochastic Gradient Descent.
[RegressionModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/regression/RegressionModel.html "interface in org.apache.spark.mllib.regression")
[RidgeRegressionModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/regression/RidgeRegressionModel.html "class in org.apache.spark.mllib.regression")
Regression model trained using RidgeRegression.
[RidgeRegressionWithSGD](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/regression/RidgeRegressionWithSGD.html "class in org.apache.spark.mllib.regression")
Train a regression model with L2-regularization using Stochastic Gradient Descent.
[StreamingLinearAlgorithm](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/regression/StreamingLinearAlgorithm.html "class in org.apache.spark.mllib.regression")<M extends [GeneralizedLinearModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/regression/GeneralizedLinearModel.html "class in org.apache.spark.mllib.regression"),A extends [GeneralizedLinearAlgorithm](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/regression/GeneralizedLinearAlgorithm.html "class in org.apache.spark.mllib.regression")<M>>
StreamingLinearAlgorithm implements methods for continuously training a generalized linear model on streaming data, and using it for prediction on (possibly different) streaming data.
[StreamingLinearRegressionWithSGD](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/regression/StreamingLinearRegressionWithSGD.html "class in org.apache.spark.mllib.regression")
Train or predict a linear regression model on streaming data.


