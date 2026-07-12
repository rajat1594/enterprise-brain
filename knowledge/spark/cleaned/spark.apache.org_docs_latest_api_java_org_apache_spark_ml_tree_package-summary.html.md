[Skip navigation links](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/tree/package-summary.html#skip-navbar-top "Skip navigation links")
  * [Overview](https://spark.apache.org/docs/latest/api/java/index.html)
  * Package
  * Class
  * [Deprecated](https://spark.apache.org/docs/latest/api/java/deprecated-list.html)
  * [Index](https://spark.apache.org/docs/latest/api/java/index-all.html)
  * [Help](https://spark.apache.org/docs/latest/api/java/help-doc.html#package)

  * Package:
  * Description |
  * [Related Packages](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/tree/package-summary.html#related-package-summary) |
  * [Classes and Interfaces](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/tree/package-summary.html#class-summary)

SEARCH:
# Package org.apache.spark.ml.tree
* * *
package org.apache.spark.ml.tree
  * Related Packages
Package
Description
[org.apache.spark.ml](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/package-summary.html)
DataFrame-based machine learning APIs to let users quickly assemble and configure practical machine learning pipelines.
[org.apache.spark.ml.tree.impl](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/tree/impl/package-summary.html)
  * All Classes and InterfacesInterfacesClasses
Class
Description
[CategoricalSplit](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/tree/CategoricalSplit.html "class in org.apache.spark.ml.tree")
Split which tests a categorical feature.
[ContinuousSplit](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/tree/ContinuousSplit.html "class in org.apache.spark.ml.tree")
Split which tests a continuous feature.
[DecisionTreeClassifierParams](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/tree/DecisionTreeClassifierParams.html "interface in org.apache.spark.ml.tree")
[DecisionTreeModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/tree/DecisionTreeModel.html "interface in org.apache.spark.ml.tree")
Abstraction for Decision Tree models.
[DecisionTreeModelReadWrite](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/tree/DecisionTreeModelReadWrite.html "class in org.apache.spark.ml.tree")
Helper classes for tree model persistence
[DecisionTreeModelReadWrite.NodeData](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/tree/DecisionTreeModelReadWrite.NodeData.html "class in org.apache.spark.ml.tree")
Info for a [`Node`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/tree/Node.html "class in org.apache.spark.ml.tree")
[DecisionTreeModelReadWrite.NodeData$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/tree/DecisionTreeModelReadWrite.NodeData$.html "class in org.apache.spark.ml.tree")
[DecisionTreeModelReadWrite.SplitData](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/tree/DecisionTreeModelReadWrite.SplitData.html "class in org.apache.spark.ml.tree")
Info for a [`Split`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/tree/Split.html "interface in org.apache.spark.ml.tree")
[DecisionTreeModelReadWrite.SplitData$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/tree/DecisionTreeModelReadWrite.SplitData$.html "class in org.apache.spark.ml.tree")
[DecisionTreeParams](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/tree/DecisionTreeParams.html "interface in org.apache.spark.ml.tree")
Parameters for Decision Tree-based algorithms.
[DecisionTreeRegressorParams](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/tree/DecisionTreeRegressorParams.html "interface in org.apache.spark.ml.tree")
[EnsembleModelReadWrite](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/tree/EnsembleModelReadWrite.html "class in org.apache.spark.ml.tree")
[EnsembleModelReadWrite.EnsembleNodeData](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/tree/EnsembleModelReadWrite.EnsembleNodeData.html "class in org.apache.spark.ml.tree")
Info for one [`Node`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/tree/Node.html "class in org.apache.spark.ml.tree") in a tree ensemble
[EnsembleModelReadWrite.EnsembleNodeData$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/tree/EnsembleModelReadWrite.EnsembleNodeData$.html "class in org.apache.spark.ml.tree")
[GBTClassifierParams](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/tree/GBTClassifierParams.html "interface in org.apache.spark.ml.tree")
[GBTParams](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/tree/GBTParams.html "interface in org.apache.spark.ml.tree")
Parameters for Gradient-Boosted Tree algorithms.
[GBTRegressorParams](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/tree/GBTRegressorParams.html "interface in org.apache.spark.ml.tree")
[HasVarianceImpurity](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/tree/HasVarianceImpurity.html "interface in org.apache.spark.ml.tree")
[InternalNode](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/tree/InternalNode.html "class in org.apache.spark.ml.tree")
Internal Decision Tree node.
[LeafNode](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/tree/LeafNode.html "class in org.apache.spark.ml.tree")
Decision tree leaf node.
[Node](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/tree/Node.html "class in org.apache.spark.ml.tree")
Decision tree node interface.
[RandomForestClassifierParams](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/tree/RandomForestClassifierParams.html "interface in org.apache.spark.ml.tree")
[RandomForestParams](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/tree/RandomForestParams.html "interface in org.apache.spark.ml.tree")
Parameters for Random Forest algorithms.
[RandomForestRegressorParams](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/tree/RandomForestRegressorParams.html "interface in org.apache.spark.ml.tree")
[Split](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/tree/Split.html "interface in org.apache.spark.ml.tree")
Interface for a "Split," which specifies a test made at a decision tree node to choose the left or right path.
[TreeClassifierParams](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/tree/TreeClassifierParams.html "interface in org.apache.spark.ml.tree")
Parameters for Decision Tree-based classification algorithms.
[TreeConfig](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/tree/TreeConfig.html "class in org.apache.spark.ml.tree")
[TreeEnsembleClassifierParams](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/tree/TreeEnsembleClassifierParams.html "interface in org.apache.spark.ml.tree")
Parameters for Decision Tree-based ensemble classification algorithms.
[TreeEnsembleModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/tree/TreeEnsembleModel.html "interface in org.apache.spark.ml.tree")<M extends [DecisionTreeModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/tree/DecisionTreeModel.html "interface in org.apache.spark.ml.tree")>
Abstraction for models which are ensembles of decision trees
[TreeEnsembleParams](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/tree/TreeEnsembleParams.html "interface in org.apache.spark.ml.tree")
Parameters for Decision Tree-based ensemble algorithms.
[TreeEnsembleRegressorParams](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/tree/TreeEnsembleRegressorParams.html "interface in org.apache.spark.ml.tree")
Parameters for Decision Tree-based ensemble regression algorithms.
[TreeRegressorParams](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/tree/TreeRegressorParams.html "interface in org.apache.spark.ml.tree")
Parameters for Decision Tree-based regression algorithms.
