[Skip to contents](https://spark.apache.org/docs/latest/api/R/reference/spark.mlp.html#main)
[ ![](https://spark.apache.org/images/spark-logo-rev.svg)](https://spark.apache.org/) [SparkR](https://spark.apache.org/docs/latest/api/R/index.html) 4.1.2
  * [Reference](https://spark.apache.org/docs/latest/api/R/reference/index.html)
  * [Articles](https://spark.apache.org/docs/latest/api/R/reference/spark.mlp.html)
[SparkR - Practical Guide](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html)


  * 

![](https://spark.apache.org/docs/latest/api/R/reference/spark.mlp.html)
# Multilayer Perceptron Classification Model
`spark.mlp.Rd`
`spark.mlp` fits a multi-layer perceptron neural network model against a SparkDataFrame. Users can call `summary` to print a summary of the fitted model, `predict` to make predictions on new data, and `write.ml`/`read.ml` to save/load fitted models. Only categorical data is supported. For more details, see [ Multilayer Perceptron](https://spark.apache.org/docs/latest/ml-classification-regression.html)
## Usage[](https://spark.apache.org/docs/latest/api/R/reference/spark.mlp.html#ref-usage)

```
spark.mlp(data, formula, ...)

# S4 method for SparkDataFrame,formula
spark.mlp(
  data,
  formula,
  layers,
  blockSize = 128,
  solver = "l-bfgs",
  maxIter = 100,
  tol = 1e-06,
  stepSize = 0.03,
  seed = NULL,
  initialWeights = NULL,
  handleInvalid = c[](https://rdrr.io/r/base/c.html)("error", "keep", "skip")
)

# S4 method for MultilayerPerceptronClassificationModel
summary[](https://spark.apache.org/docs/latest/api/R/reference/summary.html)(object)

# S4 method for MultilayerPerceptronClassificationModel
predict[](https://spark.apache.org/docs/latest/api/R/reference/predict.html)(object, newData)

# S4 method for MultilayerPerceptronClassificationModel,character
write.ml[](https://spark.apache.org/docs/latest/api/R/reference/write.ml.html)(object, path, overwrite = FALSE)
```

## Arguments[](https://spark.apache.org/docs/latest/api/R/reference/spark.mlp.html#arguments) 

data
    
a `SparkDataFrame` of observations and labels for model fitting. 

formula
    
a symbolic description of the model to be fitted. Currently only a few formula operators are supported, including '~', '.', ':', '+', and '-'. 

...
    
additional arguments passed to the method. 

layers
    
integer vector containing the number of nodes for each layer. 

blockSize
    
blockSize parameter. 

solver
    
solver parameter, supported options: "gd" (minibatch gradient descent) or "l-bfgs". 

maxIter
    
maximum iteration number. 

tol
    
convergence tolerance of iterations. 

stepSize
    
stepSize parameter. 

seed
    
seed parameter for weights initialization. 

initialWeights
    
initialWeights parameter for weights initialization, it should be a numeric vector. 

handleInvalid
    
How to handle invalid data (unseen labels or NULL values) in features and label column of string type. Supported options: "skip" (filter out rows with invalid data), "error" (throw an error), "keep" (put invalid data in a special additional bucket, at index numLabels). Default is "error". 

object
    
a Multilayer Perceptron Classification Model fitted by `spark.mlp` 

newData
    
a SparkDataFrame for testing. 

path
    
the directory where the model is saved. 

overwrite
    
overwrites or not if the output path already exists. Default is FALSE which means throw exception if the output path exists.
## Value[](https://spark.apache.org/docs/latest/api/R/reference/spark.mlp.html#value)
`spark.mlp` returns a fitted Multilayer Perceptron Classification Model. `summary` returns summary information of the fitted model, which is a list. The list includes `numOfInputs` (number of inputs), `numOfOutputs` (number of outputs), `layers` (array of layer sizes including input and output layers), and `weights` (the weights of layers). For `weights`, it is a numeric vector with length equal to the expected given the architecture (i.e., for 8-10-2 network, 112 connection weights). `predict` returns a SparkDataFrame containing predicted labeled in a column named "prediction".
## Note[](https://spark.apache.org/docs/latest/api/R/reference/spark.mlp.html#note)
spark.mlp since 2.1.0
summary(MultilayerPerceptronClassificationModel) since 2.1.0
predict(MultilayerPerceptronClassificationModel) since 2.1.0
write.ml(MultilayerPerceptronClassificationModel, character) since 2.1.0
## See also[](https://spark.apache.org/docs/latest/api/R/reference/spark.mlp.html#see-also)
[read.ml](https://spark.apache.org/docs/latest/api/R/reference/read.ml.html)
[write.ml](https://spark.apache.org/docs/latest/api/R/reference/write.ml.html)
## Examples[](https://spark.apache.org/docs/latest/api/R/reference/spark.mlp.html#ref-examples)

```
if (FALSE) {
df <- read.df[](https://spark.apache.org/docs/latest/api/R/reference/read.df.html)("data/mllib/sample_multiclass_classification_data.txt", source = "libsvm")

# fit a Multilayer Perceptron Classification Model
model <- spark.mlp(df, label ~ features, blockSize = 128, layers = c[](https://rdrr.io/r/base/c.html)(4, 3), solver = "l-bfgs",
                   maxIter = 100, tol = 0.5, stepSize = 1, seed = 1,
                   initialWeights = c[](https://rdrr.io/r/base/c.html)(0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 9, 9, 9, 9, 9))

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
