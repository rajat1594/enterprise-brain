[Skip to contents](https://spark.apache.org/docs/latest/api/R/reference/spark.logit.html#main)
[ ![](https://spark.apache.org/images/spark-logo-rev.svg)](https://spark.apache.org/) [SparkR](https://spark.apache.org/docs/latest/api/R/index.html) 4.1.2
  * [Reference](https://spark.apache.org/docs/latest/api/R/reference/index.html)
  * [Articles](https://spark.apache.org/docs/latest/api/R/reference/spark.logit.html)
[SparkR - Practical Guide](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html)


  * 

![](https://spark.apache.org/docs/latest/api/R/reference/spark.logit.html)
# Logistic Regression Model
`spark.logit.Rd`
Fits an logistic regression model against a SparkDataFrame. It supports "binomial": Binary logistic regression with pivoting; "multinomial": Multinomial logistic (softmax) regression without pivoting, similar to glmnet. Users can print, make predictions on the produced model and save the model to the input path.
## Usage[](https://spark.apache.org/docs/latest/api/R/reference/spark.logit.html#ref-usage)

```
spark.logit(data, formula, ...)

# S4 method for SparkDataFrame,formula
spark.logit(
  data,
  formula,
  regParam = 0,
  elasticNetParam = 0,
  maxIter = 100,
  tol = 1e-06,
  family = "auto",
  standardization = TRUE,
  thresholds = 0.5,
  weightCol = NULL,
  aggregationDepth = 2,
  lowerBoundsOnCoefficients = NULL,
  upperBoundsOnCoefficients = NULL,
  lowerBoundsOnIntercepts = NULL,
  upperBoundsOnIntercepts = NULL,
  handleInvalid = c[](https://rdrr.io/r/base/c.html)("error", "keep", "skip")
)

# S4 method for LogisticRegressionModel
summary[](https://spark.apache.org/docs/latest/api/R/reference/summary.html)(object)

# S4 method for LogisticRegressionModel
predict[](https://spark.apache.org/docs/latest/api/R/reference/predict.html)(object, newData)

# S4 method for LogisticRegressionModel,character
write.ml[](https://spark.apache.org/docs/latest/api/R/reference/write.ml.html)(object, path, overwrite = FALSE)
```

## Arguments[](https://spark.apache.org/docs/latest/api/R/reference/spark.logit.html#arguments) 

data
    
SparkDataFrame for training. 

formula
    
A symbolic description of the model to be fitted. Currently only a few formula operators are supported, including '~', '.', ':', '+', and '-'. 

...
    
additional arguments passed to the method. 

regParam
    
the regularization parameter. 

elasticNetParam
    
the ElasticNet mixing parameter. For alpha = 0.0, the penalty is an L2 penalty. For alpha = 1.0, it is an L1 penalty. For 0.0 < alpha < 1.0, the penalty is a combination of L1 and L2. Default is 0.0 which is an L2 penalty. 

maxIter
    
maximum iteration number. 

tol
    
convergence tolerance of iterations. 

family
    
the name of family which is a description of the label distribution to be used in the model. Supported options:
  * "auto": Automatically select the family based on the number of classes: If number of classes == 1 || number of classes == 2, set to "binomial". Else, set to "multinomial".
  * "binomial": Binary logistic regression with pivoting.
  * "multinomial": Multinomial logistic (softmax) regression without pivoting.



standardization
    
whether to standardize the training features before fitting the model. The coefficients of models will be always returned on the original scale, so it will be transparent for users. Note that with/without standardization, the models should be always converged to the same solution when no regularization is applied. Default is TRUE, same as glmnet. 

thresholds
    
in binary classification, in range [0, 1]. If the estimated probability of class label 1 is > threshold, then predict 1, else 0. A high threshold encourages the model to predict 0 more often; a low threshold encourages the model to predict 1 more often. Note: Setting this with threshold p is equivalent to setting thresholds c(1-p, p). In multiclass (or binary) classification to adjust the probability of predicting each class. Array must have length equal to the number of classes, with values > 0, excepting that at most one value may be 0. The class with largest value p/t is predicted, where p is the original probability of that class and t is the class's threshold. 

weightCol
    
The weight column name. 

aggregationDepth
    
The depth for treeAggregate (greater than or equal to 2). If the dimensions of features or the number of partitions are large, this param could be adjusted to a larger size. This is an expert parameter. Default value should be good for most cases. 

lowerBoundsOnCoefficients
    
The lower bounds on coefficients if fitting under bound constrained optimization. The bound matrix must be compatible with the shape (1, number of features) for binomial regression, or (number of classes, number of features) for multinomial regression. It is a R matrix. 

upperBoundsOnCoefficients
    
The upper bounds on coefficients if fitting under bound constrained optimization. The bound matrix must be compatible with the shape (1, number of features) for binomial regression, or (number of classes, number of features) for multinomial regression. It is a R matrix. 

lowerBoundsOnIntercepts
    
The lower bounds on intercepts if fitting under bound constrained optimization. The bounds vector size must be equal to 1 for binomial regression, or the number of classes for multinomial regression. 

upperBoundsOnIntercepts
    
The upper bounds on intercepts if fitting under bound constrained optimization. The bound vector size must be equal to 1 for binomial regression, or the number of classes for multinomial regression. 

handleInvalid
    
How to handle invalid data (unseen labels or NULL values) in features and label column of string type. Supported options: "skip" (filter out rows with invalid data), "error" (throw an error), "keep" (put invalid data in a special additional bucket, at index numLabels). Default is "error". 

object
    
an LogisticRegressionModel fitted by `spark.logit`. 

newData
    
a SparkDataFrame for testing. 

path
    
The directory where the model is saved. 

overwrite
    
Overwrites or not if the output path already exists. Default is FALSE which means throw exception if the output path exists.
## Value[](https://spark.apache.org/docs/latest/api/R/reference/spark.logit.html#value)
`spark.logit` returns a fitted logistic regression model. `summary` returns summary information of the fitted model, which is a list. The list includes `coefficients` (coefficients matrix of the fitted model). `predict` returns the predicted values based on an LogisticRegressionModel.
## Note[](https://spark.apache.org/docs/latest/api/R/reference/spark.logit.html#note)
spark.logit since 2.1.0
summary(LogisticRegressionModel) since 2.1.0
predict(LogisticRegressionModel) since 2.1.0
write.ml(LogisticRegression, character) since 2.1.0
## Examples[](https://spark.apache.org/docs/latest/api/R/reference/spark.logit.html#ref-examples)

```
if (FALSE) {
sparkR.session[](https://spark.apache.org/docs/latest/api/R/reference/sparkR.session.html)()
# binary logistic regression
t <- as.data.frame[](https://spark.apache.org/docs/latest/api/R/reference/as.data.frame.html)(Titanic)
training <- createDataFrame[](https://spark.apache.org/docs/latest/api/R/reference/createDataFrame.html)(t)
model <- spark.logit(training, Survived ~ ., regParam = 0.5)
summary <- summary[](https://spark.apache.org/docs/latest/api/R/reference/summary.html)(model)

# fitted values on training data
fitted <- predict[](https://spark.apache.org/docs/latest/api/R/reference/predict.html)(model, training)

# save fitted model to input path
path <- "path/to/model"
write.ml[](https://spark.apache.org/docs/latest/api/R/reference/write.ml.html)(model, path)

# can also read back the saved model and predict
# Note that summary deos not work on loaded model
savedModel <- read.ml[](https://spark.apache.org/docs/latest/api/R/reference/read.ml.html)(path)
summary[](https://spark.apache.org/docs/latest/api/R/reference/summary.html)(savedModel)

# binary logistic regression against two classes with
# upperBoundsOnCoefficients and upperBoundsOnIntercepts
ubc <- matrix[](https://rdrr.io/r/base/matrix.html)(c[](https://rdrr.io/r/base/c.html)(1.0, 0.0, 1.0, 0.0), nrow = 1, ncol = 4)
model <- spark.logit(training, Species ~ .,
                      upperBoundsOnCoefficients = ubc,
                      upperBoundsOnIntercepts = 1.0)

# multinomial logistic regression
model <- spark.logit(training, Class ~ ., regParam = 0.5)
summary <- summary[](https://spark.apache.org/docs/latest/api/R/reference/summary.html)(model)

# multinomial logistic regression with
# lowerBoundsOnCoefficients and lowerBoundsOnIntercepts
lbc <- matrix[](https://rdrr.io/r/base/matrix.html)(c[](https://rdrr.io/r/base/c.html)(0.0, -1.0, 0.0, -1.0, 0.0, -1.0, 0.0, -1.0), nrow = 2, ncol = 4)
lbi <- as.array[](https://rdrr.io/r/base/array.html)(c[](https://rdrr.io/r/base/c.html)(0.0, 0.0))
model <- spark.logit(training, Species ~ ., family = "multinomial",
                     lowerBoundsOnCoefficients = lbc,
                     lowerBoundsOnIntercepts = lbi)
}

```

## On this page
Developed by [ The Apache Software Foundation](https://www.apache.org/).
Site built with [pkgdown](https://pkgdown.r-lib.org/) 2.0.1.
Using [preferably](https://preferably.amirmasoudabdol.name/?source=footer) template.
