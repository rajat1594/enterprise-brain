[Skip to contents](https://spark.apache.org/docs/latest/api/R/reference/spark.prefixSpan.html#main)
[ ![](https://spark.apache.org/images/spark-logo-rev.svg)](https://spark.apache.org/) [SparkR](https://spark.apache.org/docs/latest/api/R/index.html) 4.1.2
  * [Reference](https://spark.apache.org/docs/latest/api/R/reference/index.html)
  * [Articles](https://spark.apache.org/docs/latest/api/R/reference/spark.prefixSpan.html)
[SparkR - Practical Guide](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html)

  *

![](https://spark.apache.org/docs/latest/api/R/reference/spark.prefixSpan.html)
# PrefixSpan
`spark.prefixSpan.Rd`
A parallel PrefixSpan algorithm to mine frequent sequential patterns. `spark.findFrequentSequentialPatterns` returns a complete set of frequent sequential patterns. For more details, see [ PrefixSpan](https://spark.apache.org/docs/latest/mllib-frequent-pattern-mining.html#prefixspan).
## Usage[](https://spark.apache.org/docs/latest/api/R/reference/spark.prefixSpan.html#ref-usage)

```
spark.findFrequentSequentialPatterns(data, ...)

# S4 method for SparkDataFrame
spark.findFrequentSequentialPatterns(
  data,
  minSupport = 0.1,
  maxPatternLength = 10L,
  maxLocalProjDBSize = 32000000L,
  sequenceCol = "sequence"
)
```

## Arguments[](https://spark.apache.org/docs/latest/api/R/reference/spark.prefixSpan.html#arguments)

data

A SparkDataFrame.

...

additional argument(s) passed to the method.

minSupport

Minimal support level.

maxPatternLength

Maximal pattern length.

maxLocalProjDBSize

Maximum number of items (including delimiters used in the internal storage format) allowed in a projected database before local processing.

sequenceCol

name of the sequence column in dataset.
## Value[](https://spark.apache.org/docs/latest/api/R/reference/spark.prefixSpan.html#value)
A complete set of frequent sequential patterns in the input sequences of itemsets. The returned `SparkDataFrame` contains columns of sequence and corresponding frequency. The schema of it will be: `sequence: ArrayType(ArrayType(T))`, `freq: integer` where T is the item type
## Note[](https://spark.apache.org/docs/latest/api/R/reference/spark.prefixSpan.html#note)
spark.findFrequentSequentialPatterns(SparkDataFrame) since 3.0.0
## Examples[](https://spark.apache.org/docs/latest/api/R/reference/spark.prefixSpan.html#ref-examples)

```
if (FALSE) {
df <- createDataFrame[](https://spark.apache.org/docs/latest/api/R/reference/createDataFrame.html)(list[](https://rdrr.io/r/base/list.html)(list[](https://rdrr.io/r/base/list.html)(list[](https://rdrr.io/r/base/list.html)(list[](https://rdrr.io/r/base/list.html)(1L, 2L), list[](https://rdrr.io/r/base/list.html)(3L))),
                           list[](https://rdrr.io/r/base/list.html)(list[](https://rdrr.io/r/base/list.html)(list[](https://rdrr.io/r/base/list.html)(1L), list[](https://rdrr.io/r/base/list.html)(3L, 2L), list[](https://rdrr.io/r/base/list.html)(1L, 2L))),
                           list[](https://rdrr.io/r/base/list.html)(list[](https://rdrr.io/r/base/list.html)(list[](https://rdrr.io/r/base/list.html)(1L, 2L), list[](https://rdrr.io/r/base/list.html)(5L))),
                           list[](https://rdrr.io/r/base/list.html)(list[](https://rdrr.io/r/base/list.html)(list[](https://rdrr.io/r/base/list.html)(6L)))),
                      schema = c[](https://rdrr.io/r/base/c.html)("sequence"))
frequency <- spark.findFrequentSequentialPatterns(df, minSupport = 0.5, maxPatternLength = 5L,
                                                  maxLocalProjDBSize = 32000000L)
showDF[](https://spark.apache.org/docs/latest/api/R/reference/showDF.html)(frequency)
}

```

## On this page
Developed by [ The Apache Software Foundation](https://www.apache.org/).
Site built with [pkgdown](https://pkgdown.r-lib.org/) 2.0.1.
Using [preferably](https://preferably.amirmasoudabdol.name/?source=footer) template.
