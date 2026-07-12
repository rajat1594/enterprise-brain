[Skip to contents](https://spark.apache.org/docs/latest/api/R/reference/spark.powerIterationClustering.html#main)
[ ![](https://spark.apache.org/images/spark-logo-rev.svg)](https://spark.apache.org/) [SparkR](https://spark.apache.org/docs/latest/api/R/index.html) 4.1.2
  * [Reference](https://spark.apache.org/docs/latest/api/R/reference/index.html)
  * [Articles](https://spark.apache.org/docs/latest/api/R/reference/spark.powerIterationClustering.html)
[SparkR - Practical Guide](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html)

  *

![](https://spark.apache.org/docs/latest/api/R/reference/spark.powerIterationClustering.html)
# PowerIterationClustering
`spark.powerIterationClustering.Rd`
A scalable graph clustering algorithm. Users can call `spark.assignClusters` to return a cluster assignment for each input vertex. Run the PIC algorithm and returns a cluster assignment for each input vertex.
## Usage[](https://spark.apache.org/docs/latest/api/R/reference/spark.powerIterationClustering.html#ref-usage)

```
spark.assignClusters(data, ...)

# S4 method for SparkDataFrame
spark.assignClusters(
  data,
  k = 2L,
  initMode = c[](https://rdrr.io/r/base/c.html)("random", "degree"),
  maxIter = 20L,
  sourceCol = "src",
  destinationCol = "dst",
  weightCol = NULL
)
```

## Arguments[](https://spark.apache.org/docs/latest/api/R/reference/spark.powerIterationClustering.html#arguments)

data

a SparkDataFrame.

...

additional argument(s) passed to the method.

k

the number of clusters to create.

initMode

the initialization algorithm; "random" or "degree"

maxIter

the maximum number of iterations.

sourceCol

the name of the input column for source vertex IDs.

destinationCol

the name of the input column for destination vertex IDs

weightCol

weight column name. If this is not set or `NULL`, we treat all instance weights as 1.0.
## Value[](https://spark.apache.org/docs/latest/api/R/reference/spark.powerIterationClustering.html#value)
A dataset that contains columns of vertex id and the corresponding cluster for the id. The schema of it will be: `id: integer`, `cluster: integer`
## Note[](https://spark.apache.org/docs/latest/api/R/reference/spark.powerIterationClustering.html#note)
spark.assignClusters(SparkDataFrame) since 3.0.0
## Examples[](https://spark.apache.org/docs/latest/api/R/reference/spark.powerIterationClustering.html#ref-examples)

```
if (FALSE) {
df <- createDataFrame[](https://spark.apache.org/docs/latest/api/R/reference/createDataFrame.html)(list[](https://rdrr.io/r/base/list.html)(list[](https://rdrr.io/r/base/list.html)(0L, 1L, 1.0), list[](https://rdrr.io/r/base/list.html)(0L, 2L, 1.0),
                           list[](https://rdrr.io/r/base/list.html)(1L, 2L, 1.0), list[](https://rdrr.io/r/base/list.html)(3L, 4L, 1.0),
                           list[](https://rdrr.io/r/base/list.html)(4L, 0L, 0.1)),
                      schema = c[](https://rdrr.io/r/base/c.html)("src", "dst", "weight"))
clusters <- spark.assignClusters(df, initMode = "degree", weightCol = "weight")
showDF[](https://spark.apache.org/docs/latest/api/R/reference/showDF.html)(clusters)
}

```

## On this page
Developed by [ The Apache Software Foundation](https://www.apache.org/).
Site built with [pkgdown](https://pkgdown.r-lib.org/) 2.0.1.
Using [preferably](https://preferably.amirmasoudabdol.name/?source=footer) template.
