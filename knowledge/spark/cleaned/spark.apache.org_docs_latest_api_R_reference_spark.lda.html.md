[Skip to contents](https://spark.apache.org/docs/latest/api/R/reference/spark.lda.html#main)
[ ![](https://spark.apache.org/images/spark-logo-rev.svg)](https://spark.apache.org/) [SparkR](https://spark.apache.org/docs/latest/api/R/index.html) 4.1.2
  * [Reference](https://spark.apache.org/docs/latest/api/R/reference/index.html)
  * [Articles](https://spark.apache.org/docs/latest/api/R/reference/spark.lda.html)
[SparkR - Practical Guide](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html)

  *

![](https://spark.apache.org/docs/latest/api/R/reference/spark.lda.html)
# Latent Dirichlet Allocation
`spark.lda.Rd`
`spark.lda` fits a Latent Dirichlet Allocation model on a SparkDataFrame. Users can call `summary` to get a summary of the fitted LDA model, `spark.posterior` to compute posterior probabilities on new data, `spark.perplexity` to compute log perplexity on new data and `write.ml`/`read.ml` to save/load fitted models.
## Usage[](https://spark.apache.org/docs/latest/api/R/reference/spark.lda.html#ref-usage)

```
spark.lda(data, ...)

spark.posterior(object, newData)

spark.perplexity(object, data)

# S4 method for SparkDataFrame
spark.lda(
  data,
  features = "features",
  k = 10,
  maxIter = 20,
  optimizer = c[](https://rdrr.io/r/base/c.html)("online", "em"),
  subsamplingRate = 0.05,
  topicConcentration = -1,
  docConcentration = -1,
  customizedStopWords = "",
  maxVocabSize = bitwShiftL[](https://rdrr.io/r/base/bitwise.html)(1, 18)
)

# S4 method for LDAModel
summary[](https://spark.apache.org/docs/latest/api/R/reference/summary.html)(object, maxTermsPerTopic)

# S4 method for LDAModel,SparkDataFrame
spark.perplexity(object, data)

# S4 method for LDAModel,SparkDataFrame
spark.posterior(object, newData)

# S4 method for LDAModel,character
write.ml[](https://spark.apache.org/docs/latest/api/R/reference/write.ml.html)(object, path, overwrite = FALSE)
```

## Arguments[](https://spark.apache.org/docs/latest/api/R/reference/spark.lda.html#arguments)

data

A SparkDataFrame for training.

...

additional argument(s) passed to the method.

object

A Latent Dirichlet Allocation model fitted by `spark.lda`.

newData

A SparkDataFrame for testing.

features

Features column name. Either libSVM-format column or character-format column is valid.

k

Number of topics.

maxIter

Maximum iterations.

optimizer

Optimizer to train an LDA model, "online" or "em", default is "online".

subsamplingRate

(For online optimizer) Fraction of the corpus to be sampled and used in each iteration of mini-batch gradient descent, in range (0, 1].

topicConcentration

concentration parameter (commonly named `beta` or `eta`) for the prior placed on topic distributions over terms, default -1 to set automatically on the Spark side. Use `summary` to retrieve the effective topicConcentration. Only 1-size numeric is accepted.

docConcentration

concentration parameter (commonly named `alpha`) for the prior placed on documents distributions over topics (`theta`), default -1 to set automatically on the Spark side. Use `summary` to retrieve the effective docConcentration. Only 1-size or `k`-size numeric is accepted.

customizedStopWords

stopwords that need to be removed from the given corpus. Ignore the parameter if libSVM-format column is used as the features column.

maxVocabSize

maximum vocabulary size, default 1 << 18

maxTermsPerTopic

Maximum number of terms to collect for each topic. Default value of 10.

path

The directory where the model is saved.

overwrite

Overwrites or not if the output path already exists. Default is FALSE which means throw exception if the output path exists.
## Value[](https://spark.apache.org/docs/latest/api/R/reference/spark.lda.html#value)
`spark.lda` returns a fitted Latent Dirichlet Allocation model. `summary` returns summary information of the fitted model, which is a list. The list includes

`docConcentration`

concentration parameter commonly named `alpha` for the prior placed on documents distributions over topics `theta`

`topicConcentration`

concentration parameter commonly named `beta` or `eta` for the prior placed on topic distributions over terms

`logLikelihood`

log likelihood of the entire corpus

`logPerplexity`

log perplexity

`isDistributed`

TRUE for distributed model while FALSE for local model

`vocabSize`

number of terms in the corpus

`topics`

top 10 terms and their weights of all topics

`vocabulary`

whole terms of the training corpus, NULL if libsvm format file used as training set

`trainingLogLikelihood`

Log likelihood of the observed tokens in the training set, given the current parameter estimates: log P(docs | topics, topic distributions for docs, Dirichlet hyperparameters) It is only for distributed LDA model (i.e., optimizer = "em")

`logPrior`

Log probability of the current parameter estimate: log P(topics, topic distributions for docs | Dirichlet hyperparameters) It is only for distributed LDA model (i.e., optimizer = "em")
`spark.perplexity` returns the log perplexity of given SparkDataFrame, or the log perplexity of the training data if missing argument "data". `spark.posterior` returns a SparkDataFrame containing posterior probabilities vectors named "topicDistribution".
## Note[](https://spark.apache.org/docs/latest/api/R/reference/spark.lda.html#note)
spark.lda since 2.1.0
summary(LDAModel) since 2.1.0
spark.perplexity(LDAModel) since 2.1.0
spark.posterior(LDAModel) since 2.1.0
write.ml(LDAModel, character) since 2.1.0
## See also[](https://spark.apache.org/docs/latest/api/R/reference/spark.lda.html#see-also)
topicmodels: <https://cran.r-project.org/package=topicmodels>
[read.ml](https://spark.apache.org/docs/latest/api/R/reference/read.ml.html)
## Examples[](https://spark.apache.org/docs/latest/api/R/reference/spark.lda.html#ref-examples)

```
if (FALSE) {
text <- read.df[](https://spark.apache.org/docs/latest/api/R/reference/read.df.html)("data/mllib/sample_lda_libsvm_data.txt", source = "libsvm")
model <- spark.lda(data = text, optimizer = "em")

# get a summary of the model
summary[](https://spark.apache.org/docs/latest/api/R/reference/summary.html)(model)

# compute posterior probabilities
posterior <- spark.posterior(model, text)
showDF[](https://spark.apache.org/docs/latest/api/R/reference/showDF.html)(posterior)

# compute perplexity
perplexity <- spark.perplexity(model, text)

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
