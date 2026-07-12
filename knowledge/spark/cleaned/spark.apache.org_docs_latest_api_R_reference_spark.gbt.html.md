[Skip to contents](https://spark.apache.org/docs/latest/api/R/reference/spark.gbt.html#main)
[ ![](https://spark.apache.org/images/spark-logo-rev.svg)](https://spark.apache.org/) [SparkR](https://spark.apache.org/docs/latest/api/R/index.html) 4.1.2
  * [Reference](https://spark.apache.org/docs/latest/api/R/reference/index.html)
  * [Articles](https://spark.apache.org/docs/latest/api/R/reference/spark.gbt.html)
[SparkR - Practical Guide](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html)

  *

![](https://spark.apache.org/docs/latest/api/R/reference/spark.gbt.html)
# Gradient Boosted Tree Model for Regression and Classification
`spark.gbt.Rd`
`spark.gbt` fits a Gradient Boosted Tree Regression model or Classification model on a SparkDataFrame. Users can call `summary` to get a summary of the fitted Gradient Boosted Tree model, `predict` to make predictions on new data, and `write.ml`/`read.ml` to save/load fitted models. For more details, see [ GBT Regression](https://spark.apache.org/docs/latest/ml-classification-regression.html#gradient-boosted-tree-regression) and [ GBT Classification](https://spark.apache.org/docs/latest/ml-classification-regression.html#gradient-boosted-tree-classifier)
## Usage[](https://spark.apache.org/docs/latest/api/R/reference/spark.gbt.html#ref-usage)

```
spark.gbt(data, formula, ...)

# S4 method for SparkDataFrame,formula
spark.gbt(
  data,
  formula,
  type = c[](https://rdrr.io/r/base/c.html)("regression", "classification"),
  maxDepth = 5,
  maxBins = 32,
  maxIter = 20,
  stepSize = 0.1,
  lossType = NULL,
  seed = NULL,
  subsamplingRate = 1,
  minInstancesPerNode = 1,
  minInfoGain = 0,
  checkpointInterval = 10,
  maxMemoryInMB = 256,
  cacheNodeIds = FALSE,
  handleInvalid = c[](https://rdrr.io/r/base/c.html)("error", "keep", "skip")
)

# S4 method for GBTRegressionModel
summary[](https://spark.apache.org/docs/latest/api/R/reference/summary.html)(object)

# S3 method for summary.GBTRegressionModel
print[](https://rdrr.io/r/base/print.html)(x, ...)

# S4 method for GBTClassificationModel
summary[](https://spark.apache.org/docs/latest/api/R/reference/summary.html)(object)

# S3 method for summary.GBTClassificationModel
print[](https://rdrr.io/r/base/print.html)(x, ...)

# S4 method for GBTRegressionModel
predict[](https://spark.apache.org/docs/latest/api/R/reference/predict.html)(object, newData)

# S4 method for GBTClassificationModel
predict[](https://spark.apache.org/docs/latest/api/R/reference/predict.html)(object, newData)

# S4 method for GBTRegressionModel,character
write.ml[](https://spark.apache.org/docs/latest/api/R/reference/write.ml.html)(object, path, overwrite = FALSE)

# S4 method for GBTClassificationModel,character
write.ml[](https://spark.apache.org/docs/latest/api/R/reference/write.ml.html)(object, path, overwrite = FALSE)
```

## Arguments[](https://spark.apache.org/docs/latest/api/R/reference/spark.gbt.html#arguments)

data

a SparkDataFrame for training.

formula

a symbolic description of the model to be fitted. Currently only a few formula operators are supported, including '~', ':', '+', '-', '*', and '^'.

...

additional arguments passed to the method.

type

type of model, one of "regression" or "classification", to fit

maxDepth

Maximum depth of the tree (>= 0).

maxBins

Maximum number of bins used for discretizing continuous features and for choosing how to split on features at each node. More bins give higher granularity. Must be >= 2 and >= number of categories in any categorical feature.

maxIter

Param for maximum number of iterations (>= 0).

stepSize

Param for Step size to be used for each iteration of optimization.

lossType

Loss function which GBT tries to minimize. For classification, must be "logistic". For regression, must be one of "squared" (L2) and "absolute" (L1), default is "squared".

seed

integer seed for random number generation.

subsamplingRate

Fraction of the training data used for learning each decision tree, in range (0, 1].

minInstancesPerNode

Minimum number of instances each child must have after split. If a split causes the left or right child to have fewer than minInstancesPerNode, the split will be discarded as invalid. Should be >= 1.

minInfoGain

Minimum information gain for a split to be considered at a tree node.

checkpointInterval

Param for set checkpoint interval (>= 1) or disable checkpoint (-1). Note: this setting will be ignored if the checkpoint directory is not set.

maxMemoryInMB

Maximum memory in MiB allocated to histogram aggregation.

cacheNodeIds

If FALSE, the algorithm will pass trees to executors to match instances with nodes. If TRUE, the algorithm will cache node IDs for each instance. Caching can speed up training of deeper trees. Users can set how often should the cache be checkpointed or disable it by setting checkpointInterval.

handleInvalid

How to handle invalid data (unseen labels or NULL values) in features and label column of string type in classification model. Supported options: "skip" (filter out rows with invalid data), "error" (throw an error), "keep" (put invalid data in a special additional bucket, at index numLabels). Default is "error".

object

A fitted Gradient Boosted Tree regression model or classification model.

x

summary object of Gradient Boosted Tree regression model or classification model returned by `summary`.

newData

a SparkDataFrame for testing.

path

The directory where the model is saved.

overwrite

Overwrites or not if the output path already exists. Default is FALSE which means throw exception if the output path exists.
## Value[](https://spark.apache.org/docs/latest/api/R/reference/spark.gbt.html#value)
`spark.gbt` returns a fitted Gradient Boosted Tree model. `summary` returns summary information of the fitted model, which is a list. The list of components includes `formula` (formula), `numFeatures` (number of features), `features` (list of features), `featureImportances` (feature importances), `maxDepth` (max depth of trees), `numTrees` (number of trees), and `treeWeights` (tree weights). `predict` returns a SparkDataFrame containing predicted labeled in a column named "prediction".
## Note[](https://spark.apache.org/docs/latest/api/R/reference/spark.gbt.html#note)
spark.gbt since 2.1.0
summary(GBTRegressionModel) since 2.1.0
print.summary.GBTRegressionModel since 2.1.0
summary(GBTClassificationModel) since 2.1.0
print.summary.GBTClassificationModel since 2.1.0
predict(GBTRegressionModel) since 2.1.0
predict(GBTClassificationModel) since 2.1.0
write.ml(GBTRegressionModel, character) since 2.1.0
write.ml(GBTClassificationModel, character) since 2.1.0
## Examples[](https://spark.apache.org/docs/latest/api/R/reference/spark.gbt.html#ref-examples)

```
if (FALSE) {
# fit a Gradient Boosted Tree Regression Model
df <- createDataFrame[](https://spark.apache.org/docs/latest/api/R/reference/createDataFrame.html)(longley)
model <- spark.gbt(df, Employed ~ ., type = "regression", maxDepth = 5, maxBins = 16)

# get the summary of the model
summary[](https://spark.apache.org/docs/latest/api/R/reference/summary.html)(model)

# make predictions
predictions <- predict[](https://spark.apache.org/docs/latest/api/R/reference/predict.html)(model, df)

# save and load the model
path <- "path/to/model"
write.ml[](https://spark.apache.org/docs/latest/api/R/reference/write.ml.html)(model, path)
savedModel <- read.ml[](https://spark.apache.org/docs/latest/api/R/reference/read.ml.html)(path)
summary[](https://spark.apache.org/docs/latest/api/R/reference/summary.html)(savedModel)

# fit a Gradient Boosted Tree Classification Model
# label must be binary - Only binary classification is supported for GBT.
t <- as.data.frame[](https://spark.apache.org/docs/latest/api/R/reference/as.data.frame.html)(Titanic)
df <- createDataFrame[](https://spark.apache.org/docs/latest/api/R/reference/createDataFrame.html)(t)
model <- spark.gbt(df, Survived ~ Age + Freq, "classification")

# numeric label is also supported
t2 <- as.data.frame[](https://spark.apache.org/docs/latest/api/R/reference/as.data.frame.html)(Titanic)
t2$NumericGender <- ifelse[](https://spark.apache.org/docs/latest/api/R/reference/column_nonaggregate_functions.html)(t2$Sex == "Male", 0, 1)
df <- createDataFrame[](https://spark.apache.org/docs/latest/api/R/reference/createDataFrame.html)(t2)
model <- spark.gbt(df, NumericGender ~ ., type = "classification")
}

```

## On this page
Developed by [ The Apache Software Foundation](https://www.apache.org/).
Site built with [pkgdown](https://pkgdown.r-lib.org/) 2.0.1.
Using [preferably](https://preferably.amirmasoudabdol.name/?source=footer) template.
