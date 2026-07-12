[Skip to contents](https://spark.apache.org/docs/latest/api/R/reference/spark.lm.html#main)
[ ![](https://spark.apache.org/images/spark-logo-rev.svg)](https://spark.apache.org/) [SparkR](https://spark.apache.org/docs/latest/api/R/index.html) 4.1.2
  * [Reference](https://spark.apache.org/docs/latest/api/R/reference/index.html)
  * [Articles](https://spark.apache.org/docs/latest/api/R/reference/spark.lm.html)
[SparkR - Practical Guide](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html)


  * 

![](https://spark.apache.org/docs/latest/api/R/reference/spark.lm.html)
# Linear Regression Model
`spark.lm.Rd`
`spark.lm` fits a linear regression model against a SparkDataFrame. Users can call `summary` to print a summary of the fitted model, `predict` to make predictions on new data, and `write.ml`/`read.ml` to save/load fitted models.
## Usage[](https://spark.apache.org/docs/latest/api/R/reference/spark.lm.html#ref-usage)

```
spark.lm(data, formula, ...)

# S4 method for SparkDataFrame,formula
spark.lm(
  data,
  formula,
  maxIter = 100L,
  regParam = 0,
  elasticNetParam = 0,
  tol = 1e-06,
  standardization = TRUE,
  solver = c[](https://rdrr.io/r/base/c.html)("auto", "l-bfgs", "normal"),
  weightCol = NULL,
  aggregationDepth = 2L,
  loss = c[](https://rdrr.io/r/base/c.html)("squaredError", "huber"),
  epsilon = 1.35,
  stringIndexerOrderType = c[](https://rdrr.io/r/base/c.html)("frequencyDesc", "frequencyAsc", "alphabetDesc",
    "alphabetAsc")
)

# S4 method for LinearRegressionModel
summary[](https://spark.apache.org/docs/latest/api/R/reference/summary.html)(object)

# S4 method for LinearRegressionModel
predict[](https://spark.apache.org/docs/latest/api/R/reference/predict.html)(object, newData)

# S4 method for LinearRegressionModel,character
write.ml[](https://spark.apache.org/docs/latest/api/R/reference/write.ml.html)(object, path, overwrite = FALSE)
```

## Arguments[](https://spark.apache.org/docs/latest/api/R/reference/spark.lm.html#arguments) 

data
    
a `SparkDataFrame` of observations and labels for model fitting. 

formula
    
a symbolic description of the model to be fitted. Currently only a few formula operators are supported, including '~', '.', ':', '+', and '-'. 

...
    
additional arguments passed to the method. 

maxIter
    
maximum iteration number. 

regParam
    
the regularization parameter. 

elasticNetParam
    
the ElasticNet mixing parameter, in range [0, 1]. For alpha = 0, the penalty is an L2 penalty. For alpha = 1, it is an L1 penalty. 

tol
    
convergence tolerance of iterations. 

standardization
    
whether to standardize the training features before fitting the model. 

solver
    
The solver algorithm for optimization. Supported options: "l-bfgs", "normal" and "auto". 

weightCol
    
weight column name. 

aggregationDepth
    
suggested depth for treeAggregate (>= 2). 

loss
    
the loss function to be optimized. Supported options: "squaredError" and "huber". 

epsilon
    
the shape parameter to control the amount of robustness. 

stringIndexerOrderType
    
how to order categories of a string feature column. This is used to decide the base level of a string feature as the last category after ordering is dropped when encoding strings. Supported options are "frequencyDesc", "frequencyAsc", "alphabetDesc", and "alphabetAsc". The default value is "frequencyDesc". When the ordering is set to "alphabetDesc", this drops the same category as R when encoding strings. 

object
    
a Linear Regression Model model fitted by `spark.lm`. 

newData
    
a SparkDataFrame for testing. 

path
    
The directory where the model is saved. 

overwrite
    
Overwrites or not if the output path already exists. Default is FALSE which means throw exception if the output path exists.
## Value[](https://spark.apache.org/docs/latest/api/R/reference/spark.lm.html#value)
`spark.lm` returns a fitted Linear Regression Model. `summary` returns summary information of the fitted model, which is a list. `predict` returns the predicted values based on a LinearRegressionModel.
## Note[](https://spark.apache.org/docs/latest/api/R/reference/spark.lm.html#note)
spark.lm since 3.1.0
summary(LinearRegressionModel) since 3.1.0
predict(LinearRegressionModel) since 3.1.0
write.ml(LinearRegressionModel, character) since 3.1.0
## See also[](https://spark.apache.org/docs/latest/api/R/reference/spark.lm.html#see-also)
[read.ml](https://spark.apache.org/docs/latest/api/R/reference/read.ml.html)
## Examples[](https://spark.apache.org/docs/latest/api/R/reference/spark.lm.html#ref-examples)

```
if (FALSE) {
df <- read.df[](https://spark.apache.org/docs/latest/api/R/reference/read.df.html)("data/mllib/sample_linear_regression_data.txt", source = "libsvm")

# fit Linear Regression Model
model <- spark.lm(df, label ~ features, regParam = 0.01, maxIter = 1)

# get the summary of the model
summary[](https://spark.apache.org/docs/latest/api/R/reference/summary.html)(model)

# make predictions
predictions <- predict[](https://spark.apache.org/docs/latest/api/R/reference/predict.html)(model, df)

# save and load the model
path <- "path/to/model"
write.ml[](https://spark.apache.org/docs/latest/api/R/reference/write.ml.html)(model, path)
savedModel <- read.ml[](https://spark.apache.org/docs/latest/api/R/reference/read.ml.html)(path)
summary[](https://spark.apache.org/docs/latest/api/R/reference/summary.html)(savedModel)
}

```

## On this page
Developed by [ The Apache Software Foundation](https://www.apache.org/).
Site built with [pkgdown](https://pkgdown.r-lib.org/) 2.0.1.
Using [preferably](https://preferably.amirmasoudabdol.name/?source=footer) template.
