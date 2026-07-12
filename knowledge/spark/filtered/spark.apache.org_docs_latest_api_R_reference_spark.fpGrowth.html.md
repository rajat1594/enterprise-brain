[Skip to contents](https://spark.apache.org/docs/latest/api/R/reference/spark.fpGrowth.html#main)
[ ![](https://spark.apache.org/images/spark-logo-rev.svg)](https://spark.apache.org/) [SparkR](https://spark.apache.org/docs/latest/api/R/index.html) 4.1.2
  * [Reference](https://spark.apache.org/docs/latest/api/R/reference/index.html)
  * [Articles](https://spark.apache.org/docs/latest/api/R/reference/spark.fpGrowth.html)
[SparkR - Practical Guide](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html)


  * 

![](https://spark.apache.org/docs/latest/api/R/reference/spark.fpGrowth.html)
# FP-growth
`spark.fpGrowth.Rd`
A parallel FP-growth algorithm to mine frequent itemsets. `spark.fpGrowth` fits a FP-growth model on a SparkDataFrame. Users can `spark.freqItemsets` to get frequent itemsets, `spark.associationRules` to get association rules, `predict` to make predictions on new data based on generated association rules, and `write.ml`/`read.ml` to save/load fitted models. For more details, see [ FP-growth](https://spark.apache.org/docs/latest/mllib-frequent-pattern-mining.html#fp-growth).
## Usage[](https://spark.apache.org/docs/latest/api/R/reference/spark.fpGrowth.html#ref-usage)

```
spark.fpGrowth(data, ...)

spark.freqItemsets(object)

spark.associationRules(object)

# S4 method for SparkDataFrame
spark.fpGrowth(
  data,
  minSupport = 0.3,
  minConfidence = 0.8,
  itemsCol = "items",
  numPartitions = NULL
)

# S4 method for FPGrowthModel
spark.freqItemsets(object)

# S4 method for FPGrowthModel
spark.associationRules(object)

# S4 method for FPGrowthModel
predict[](https://spark.apache.org/docs/latest/api/R/reference/predict.html)(object, newData)

# S4 method for FPGrowthModel,character
write.ml[](https://spark.apache.org/docs/latest/api/R/reference/write.ml.html)(object, path, overwrite = FALSE)
```

## Arguments[](https://spark.apache.org/docs/latest/api/R/reference/spark.fpGrowth.html#arguments) 

data
    
A SparkDataFrame for training. 

...
    
additional argument(s) passed to the method. 

object
    
a fitted FPGrowth model. 

minSupport
    
Minimal support level. 

minConfidence
    
Minimal confidence level. 

itemsCol
    
Features column name. 

numPartitions
    
Number of partitions used for fitting. 

newData
    
a SparkDataFrame for testing. 

path
    
the directory where the model is saved. 

overwrite
    
logical value indicating whether to overwrite if the output path already exists. Default is FALSE which means throw exception if the output path exists.
## Value[](https://spark.apache.org/docs/latest/api/R/reference/spark.fpGrowth.html#value)
`spark.fpGrowth` returns a fitted FPGrowth model. A `SparkDataFrame` with frequent itemsets. The `SparkDataFrame` contains two columns: `items` (an array of the same type as the input column) and `freq` (frequency of the itemset). A `SparkDataFrame` with association rules. The `SparkDataFrame` contains five columns: `antecedent` (an array of the same type as the input column), `consequent` (an array of the same type as the input column), `confidence` (confidence for the rule) `lift` (lift for the rule) and `support` (support for the rule) `predict` returns a SparkDataFrame containing predicted values.
## Note[](https://spark.apache.org/docs/latest/api/R/reference/spark.fpGrowth.html#note)
spark.fpGrowth since 2.2.0
spark.freqItemsets(FPGrowthModel) since 2.2.0
spark.associationRules(FPGrowthModel) since 2.2.0
predict(FPGrowthModel) since 2.2.0
write.ml(FPGrowthModel, character) since 2.2.0
## See also[](https://spark.apache.org/docs/latest/api/R/reference/spark.fpGrowth.html#see-also)
[read.ml](https://spark.apache.org/docs/latest/api/R/reference/read.ml.html)
## Examples[](https://spark.apache.org/docs/latest/api/R/reference/spark.fpGrowth.html#ref-examples)

```
if (FALSE) {
raw_data <- read.df[](https://spark.apache.org/docs/latest/api/R/reference/read.df.html)(
  "data/mllib/sample_fpgrowth.txt",
  source = "csv",
  schema = structType[](https://spark.apache.org/docs/latest/api/R/reference/structType.html)(structField[](https://spark.apache.org/docs/latest/api/R/reference/structField.html)("raw_items", "string")))

data <- selectExpr[](https://spark.apache.org/docs/latest/api/R/reference/selectExpr.html)(raw_data, "split(raw_items, ' ') as items")
model <- spark.fpGrowth(data)

# Show frequent itemsets
frequent_itemsets <- spark.freqItemsets(model)
showDF[](https://spark.apache.org/docs/latest/api/R/reference/showDF.html)(frequent_itemsets)

# Show association rules
association_rules <- spark.associationRules(model)
showDF[](https://spark.apache.org/docs/latest/api/R/reference/showDF.html)(association_rules)

# Predict on new data
new_itemsets <- data.frame[](https://rdrr.io/r/base/data.frame.html)(items = c[](https://rdrr.io/r/base/c.html)("t", "t,s"))
new_data <- selectExpr[](https://spark.apache.org/docs/latest/api/R/reference/selectExpr.html)(createDataFrame[](https://spark.apache.org/docs/latest/api/R/reference/createDataFrame.html)(new_itemsets), "split(items, ',') as items")
predict[](https://spark.apache.org/docs/latest/api/R/reference/predict.html)(model, new_data)

# Save and load model
path <- "/path/to/model"
write.ml[](https://spark.apache.org/docs/latest/api/R/reference/write.ml.html)(model, path)
read.ml[](https://spark.apache.org/docs/latest/api/R/reference/read.ml.html)(path)

# Optional arguments
baskets_data <- selectExpr[](https://spark.apache.org/docs/latest/api/R/reference/selectExpr.html)(createDataFrame[](https://spark.apache.org/docs/latest/api/R/reference/createDataFrame.html)(itemsets), "split(items, ',') as baskets")
another_model <- spark.fpGrowth(data, minSupport = 0.1, minConfidence = 0.5,
                                itemsCol = "baskets", numPartitions = 10)
}

```

## On this page
Developed by [ The Apache Software Foundation](https://www.apache.org/).
Site built with [pkgdown](https://pkgdown.r-lib.org/) 2.0.1.
Using [preferably](https://preferably.amirmasoudabdol.name/?source=footer) template.
