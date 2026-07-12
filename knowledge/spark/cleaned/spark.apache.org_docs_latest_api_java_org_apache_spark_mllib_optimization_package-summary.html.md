[Skip navigation links](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/optimization/package-summary.html#skip-navbar-top "Skip navigation links")
  * [Overview](https://spark.apache.org/docs/latest/api/java/index.html)
  * Package
  * Class
  * [Deprecated](https://spark.apache.org/docs/latest/api/java/deprecated-list.html)
  * [Index](https://spark.apache.org/docs/latest/api/java/index-all.html)
  * [Help](https://spark.apache.org/docs/latest/api/java/help-doc.html#package)

  * Package:
  * Description |
  * [Related Packages](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/optimization/package-summary.html#related-package-summary) |
  * [Classes and Interfaces](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/optimization/package-summary.html#class-summary)

SEARCH:
# Package org.apache.spark.mllib.optimization
* * *
package org.apache.spark.mllib.optimization
  * Related Packages
Package
Description
[org.apache.spark.mllib](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/package-summary.html)
RDD-based machine learning APIs (in maintenance mode).
  * All Classes and InterfacesInterfacesClasses
Class
Description
[Gradient](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/optimization/Gradient.html "class in org.apache.spark.mllib.optimization")
Class used to compute the gradient for a loss function, given a single data point.
[GradientDescent](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/optimization/GradientDescent.html "class in org.apache.spark.mllib.optimization")
Class used to solve an optimization problem using Gradient Descent.
[HingeGradient](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/optimization/HingeGradient.html "class in org.apache.spark.mllib.optimization")
Compute gradient and loss for a Hinge loss function, as used in SVM binary classification.
[L1Updater](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/optimization/L1Updater.html "class in org.apache.spark.mllib.optimization")
Updater for L1 regularized problems.
[LBFGS](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/optimization/LBFGS.html "class in org.apache.spark.mllib.optimization")
Class used to solve an optimization problem using Limited-memory BFGS.
[LeastSquaresGradient](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/optimization/LeastSquaresGradient.html "class in org.apache.spark.mllib.optimization")
Compute gradient and loss for a Least-squared loss function, as used in linear regression.
[LogisticGradient](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/optimization/LogisticGradient.html "class in org.apache.spark.mllib.optimization")
Compute gradient and loss for a multinomial logistic loss function, as used in multi-class classification (it is also used in binary logistic regression).
[NNLS](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/optimization/NNLS.html "class in org.apache.spark.mllib.optimization")
Object used to solve nonnegative least squares problems using a modified projected gradient method.
[NNLS.Workspace](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/optimization/NNLS.Workspace.html "class in org.apache.spark.mllib.optimization")
[Optimizer](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/optimization/Optimizer.html "interface in org.apache.spark.mllib.optimization")
Trait for optimization problem solvers.
[SimpleUpdater](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/optimization/SimpleUpdater.html "class in org.apache.spark.mllib.optimization")
A simple updater for gradient descent *without* any regularization.
[SquaredL2Updater](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/optimization/SquaredL2Updater.html "class in org.apache.spark.mllib.optimization")
Updater for L2 regularized problems.
[Updater](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/optimization/Updater.html "class in org.apache.spark.mllib.optimization")
Class used to perform steps (weight update) using Gradient Descent methods.
