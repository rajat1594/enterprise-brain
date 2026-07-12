[Skip to contents](https://spark.apache.org/docs/latest/api/R/reference/read.ml.html#main)
[ ![](https://spark.apache.org/images/spark-logo-rev.svg)](https://spark.apache.org/) [SparkR](https://spark.apache.org/docs/latest/api/R/index.html) 4.1.2
  * [Reference](https://spark.apache.org/docs/latest/api/R/reference/index.html)
  * [Articles](https://spark.apache.org/docs/latest/api/R/reference/read.ml.html)
[SparkR - Practical Guide](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html)


  * 

![](https://spark.apache.org/docs/latest/api/R/reference/read.ml.html)
# Load a fitted MLlib model from the input path.
`read.ml.Rd`
Load a fitted MLlib model from the input path.
## Usage[](https://spark.apache.org/docs/latest/api/R/reference/read.ml.html#ref-usage)

```
read.ml(path)
```

## Arguments[](https://spark.apache.org/docs/latest/api/R/reference/read.ml.html#arguments) 

path
    
path of the model to read.
## Value[](https://spark.apache.org/docs/latest/api/R/reference/read.ml.html#value)
A fitted MLlib model.
## Note[](https://spark.apache.org/docs/latest/api/R/reference/read.ml.html#note)
read.ml since 2.0.0
## See also[](https://spark.apache.org/docs/latest/api/R/reference/read.ml.html#see-also)
[write.ml](https://spark.apache.org/docs/latest/api/R/reference/write.ml.html)
## Examples[](https://spark.apache.org/docs/latest/api/R/reference/read.ml.html#ref-examples)

```
if (FALSE) {
path <- "path/to/model"
model <- read.ml(path)
}

```

## On this page
Developed by [ The Apache Software Foundation](https://www.apache.org/).
Site built with [pkgdown](https://pkgdown.r-lib.org/) 2.0.1.
Using [preferably](https://preferably.amirmasoudabdol.name/?source=footer) template.
