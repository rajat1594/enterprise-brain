[Skip navigation links](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/regression/package-summary.html#skip-navbar-top "Skip navigation links")
  * [Overview](https://spark.apache.org/docs/latest/api/java/index.html)
  * Package
  * Class
  * [Deprecated](https://spark.apache.org/docs/latest/api/java/deprecated-list.html)
  * [Index](https://spark.apache.org/docs/latest/api/java/index-all.html)
  * [Help](https://spark.apache.org/docs/latest/api/java/help-doc.html#package)


  * Package: 
  * Description | 
  * [Related Packages](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/regression/package-summary.html#related-package-summary) | 
  * [Classes and Interfaces](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/regression/package-summary.html#class-summary)


SEARCH:
# Package org.apache.spark.ml.regression
* * *
package org.apache.spark.ml.regression
  * Related Packages
Package
Description
[org.apache.spark.ml](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/package-summary.html)
DataFrame-based machine learning APIs to let users quickly assemble and configure practical machine learning pipelines.
  * All Classes and InterfacesInterfacesClasses
Class
Description
[AFTSurvivalRegression](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/regression/AFTSurvivalRegression.html "class in org.apache.spark.ml.regression")
Fit a parametric survival regression model named accelerated failure time (AFT) model (see [ Accelerated failure time model (Wikipedia)](https://en.wikipedia.org/wiki/Accelerated_failure_time_model)) based on the Weibull distribution of the survival time.
[AFTSurvivalRegressionModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/regression/AFTSurvivalRegressionModel.html "class in org.apache.spark.ml.regression")
Model produced by [`AFTSurvivalRegression`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/regression/AFTSurvivalRegression.html "class in org.apache.spark.ml.regression").
[AFTSurvivalRegressionModel.Data$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/regression/AFTSurvivalRegressionModel.Data$.html "class in org.apache.spark.ml.regression")
[AFTSurvivalRegressionParams](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/regression/AFTSurvivalRegressionParams.html "interface in org.apache.spark.ml.regression")
Params for accelerated failure time (AFT) regression.
[DecisionTreeRegressionModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/regression/DecisionTreeRegressionModel.html "class in org.apache.spark.ml.regression")
[ Decision tree (Wikipedia)](http://en.wikipedia.org/wiki/Decision_tree_learning) model for regression.
[DecisionTreeRegressor](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/regression/DecisionTreeRegressor.html "class in org.apache.spark.ml.regression")
[Decision tree](http://en.wikipedia.org/wiki/Decision_tree_learning) learning algorithm for regression.
[FactorizationMachines](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/regression/FactorizationMachines.html "interface in org.apache.spark.ml.regression")
[FactorizationMachinesParams](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/regression/FactorizationMachinesParams.html "interface in org.apache.spark.ml.regression")
Params for Factorization Machines
[FMRegressionModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/regression/FMRegressionModel.html "class in org.apache.spark.ml.regression")
Model produced by [`FMRegressor`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/regression/FMRegressor.html "class in org.apache.spark.ml.regression").
[FMRegressionModel.Data$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/regression/FMRegressionModel.Data$.html "class in org.apache.spark.ml.regression")
[FMRegressor](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/regression/FMRegressor.html "class in org.apache.spark.ml.regression")
Factorization Machines learning algorithm for regression.
[FMRegressorParams](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/regression/FMRegressorParams.html "interface in org.apache.spark.ml.regression")
Params for FMRegressor
[GBTRegressionModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/regression/GBTRegressionModel.html "class in org.apache.spark.ml.regression")
[Gradient-Boosted Trees (GBTs)](http://en.wikipedia.org/wiki/Gradient_boosting) model for regression.
[GBTRegressor](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/regression/GBTRegressor.html "class in org.apache.spark.ml.regression")
[Gradient-Boosted Trees (GBTs)](http://en.wikipedia.org/wiki/Gradient_boosting) learning algorithm for regression.
[GeneralizedLinearRegression](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/regression/GeneralizedLinearRegression.html "class in org.apache.spark.ml.regression")
Fit a Generalized Linear Model (see [ Generalized linear model (Wikipedia)](https://en.wikipedia.org/wiki/Generalized_linear_model)) specified by giving a symbolic description of the linear predictor (link function) and a description of the error distribution (family).
[GeneralizedLinearRegression.Binomial$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/regression/GeneralizedLinearRegression.Binomial$.html "class in org.apache.spark.ml.regression")
Binomial exponential family distribution.
[GeneralizedLinearRegression.CLogLog$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/regression/GeneralizedLinearRegression.CLogLog$.html "class in org.apache.spark.ml.regression")
[GeneralizedLinearRegression.Family$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/regression/GeneralizedLinearRegression.Family$.html "class in org.apache.spark.ml.regression")
[GeneralizedLinearRegression.FamilyAndLink$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/regression/GeneralizedLinearRegression.FamilyAndLink$.html "class in org.apache.spark.ml.regression")
[GeneralizedLinearRegression.Gamma$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/regression/GeneralizedLinearRegression.Gamma$.html "class in org.apache.spark.ml.regression")
Gamma exponential family distribution.
[GeneralizedLinearRegression.Gaussian$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/regression/GeneralizedLinearRegression.Gaussian$.html "class in org.apache.spark.ml.regression")
Gaussian exponential family distribution.
[GeneralizedLinearRegression.Identity$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/regression/GeneralizedLinearRegression.Identity$.html "class in org.apache.spark.ml.regression")
[GeneralizedLinearRegression.Inverse$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/regression/GeneralizedLinearRegression.Inverse$.html "class in org.apache.spark.ml.regression")
[GeneralizedLinearRegression.Link$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/regression/GeneralizedLinearRegression.Link$.html "class in org.apache.spark.ml.regression")
[GeneralizedLinearRegression.Log$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/regression/GeneralizedLinearRegression.Log$.html "class in org.apache.spark.ml.regression")
[GeneralizedLinearRegression.Logit$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/regression/GeneralizedLinearRegression.Logit$.html "class in org.apache.spark.ml.regression")
[GeneralizedLinearRegression.Poisson$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/regression/GeneralizedLinearRegression.Poisson$.html "class in org.apache.spark.ml.regression")
Poisson exponential family distribution.
[GeneralizedLinearRegression.Probit$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/regression/GeneralizedLinearRegression.Probit$.html "class in org.apache.spark.ml.regression")
[GeneralizedLinearRegression.Sqrt$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/regression/GeneralizedLinearRegression.Sqrt$.html "class in org.apache.spark.ml.regression")
[GeneralizedLinearRegression.Tweedie$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/regression/GeneralizedLinearRegression.Tweedie$.html "class in org.apache.spark.ml.regression")
[GeneralizedLinearRegressionBase](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/regression/GeneralizedLinearRegressionBase.html "interface in org.apache.spark.ml.regression")
Params for Generalized Linear Regression.
[GeneralizedLinearRegressionModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/regression/GeneralizedLinearRegressionModel.html "class in org.apache.spark.ml.regression")
Model produced by [`GeneralizedLinearRegression`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/regression/GeneralizedLinearRegression.html "class in org.apache.spark.ml.regression").
[GeneralizedLinearRegressionModel.Data$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/regression/GeneralizedLinearRegressionModel.Data$.html "class in org.apache.spark.ml.regression")
[GeneralizedLinearRegressionSummary](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/regression/GeneralizedLinearRegressionSummary.html "class in org.apache.spark.ml.regression")
Summary of [`GeneralizedLinearRegression`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/regression/GeneralizedLinearRegression.html "class in org.apache.spark.ml.regression") model and predictions.
[GeneralizedLinearRegressionTrainingSummary](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/regression/GeneralizedLinearRegressionTrainingSummary.html "class in org.apache.spark.ml.regression")
Summary of [`GeneralizedLinearRegression`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/regression/GeneralizedLinearRegression.html "class in org.apache.spark.ml.regression") fitting and model.
[InternalLinearRegressionModelWriter](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/regression/InternalLinearRegressionModelWriter.html "class in org.apache.spark.ml.regression")
A writer for LinearRegression that handles the "internal" (or default) format
[IsotonicRegression](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/regression/IsotonicRegression.html "class in org.apache.spark.ml.regression")
Isotonic regression.
[IsotonicRegressionBase](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/regression/IsotonicRegressionBase.html "interface in org.apache.spark.ml.regression")
Params for isotonic regression.
[IsotonicRegressionModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/regression/IsotonicRegressionModel.html "class in org.apache.spark.ml.regression")
Model fitted by IsotonicRegression.
[IsotonicRegressionModel.Data$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/regression/IsotonicRegressionModel.Data$.html "class in org.apache.spark.ml.regression")
[LinearRegression](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/regression/LinearRegression.html "class in org.apache.spark.ml.regression")
Linear regression.
[LinearRegressionModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/regression/LinearRegressionModel.html "class in org.apache.spark.ml.regression")
Model produced by [`LinearRegression`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/regression/LinearRegression.html "class in org.apache.spark.ml.regression").
[LinearRegressionParams](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/regression/LinearRegressionParams.html "interface in org.apache.spark.ml.regression")
Params for linear regression.
[LinearRegressionSummary](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/regression/LinearRegressionSummary.html "class in org.apache.spark.ml.regression")
Linear regression results evaluated on a dataset.
[LinearRegressionTrainingSummary](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/regression/LinearRegressionTrainingSummary.html "class in org.apache.spark.ml.regression")
Linear regression training results.
[PMMLLinearRegressionModelWriter](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/regression/PMMLLinearRegressionModelWriter.html "class in org.apache.spark.ml.regression")
A writer for LinearRegression that handles the "pmml" format
[RandomForestRegressionModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/regression/RandomForestRegressionModel.html "class in org.apache.spark.ml.regression")
[Random Forest](http://en.wikipedia.org/wiki/Random_forest) model for regression.
[RandomForestRegressor](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/regression/RandomForestRegressor.html "class in org.apache.spark.ml.regression")
[Random Forest](http://en.wikipedia.org/wiki/Random_forest) learning algorithm for regression.
[RegressionModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/regression/RegressionModel.html "class in org.apache.spark.ml.regression")<FeaturesType,M extends [RegressionModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/regression/RegressionModel.html "class in org.apache.spark.ml.regression")<FeaturesType,M>>
Model produced by a `Regressor`.
[Regressor](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/regression/Regressor.html "class in org.apache.spark.ml.regression")<FeaturesType,Learner extends [Regressor](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/regression/Regressor.html "class in org.apache.spark.ml.regression")<FeaturesType,Learner,M>,M extends [RegressionModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/regression/RegressionModel.html "class in org.apache.spark.ml.regression")<FeaturesType,M>>
Single-label regression


