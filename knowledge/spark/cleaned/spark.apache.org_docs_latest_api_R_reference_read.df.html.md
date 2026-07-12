[Skip to contents](https://spark.apache.org/docs/latest/api/R/reference/read.df.html#main)
[ ![](https://spark.apache.org/images/spark-logo-rev.svg)](https://spark.apache.org/) [SparkR](https://spark.apache.org/docs/latest/api/R/index.html) 4.1.2
  * [Reference](https://spark.apache.org/docs/latest/api/R/reference/index.html)
  * [Articles](https://spark.apache.org/docs/latest/api/R/reference/read.df.html)
[SparkR - Practical Guide](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html)

  *

![](https://spark.apache.org/docs/latest/api/R/reference/read.df.html)
# Load a SparkDataFrame
`read.df.Rd`
Returns the dataset in a data source as a SparkDataFrame
## Usage[](https://spark.apache.org/docs/latest/api/R/reference/read.df.html#ref-usage)

```
read.df(path = NULL, source = NULL, schema = NULL, na.strings = "NA", ...)

loadDF(path = NULL, source = NULL, schema = NULL, ...)
```

## Arguments[](https://spark.apache.org/docs/latest/api/R/reference/read.df.html#arguments)

path

The path of files to load

source

The name of external data source

schema

The data schema defined in structType or a DDL-formatted string.

na.strings

Default string value for NA when source is "csv"

...

additional external data source specific named properties.
## Value[](https://spark.apache.org/docs/latest/api/R/reference/read.df.html#value)
SparkDataFrame
## Details[](https://spark.apache.org/docs/latest/api/R/reference/read.df.html#details)
The data source is specified by the `source` and a set of options(...). If `source` is not specified, the default data source configured by "spark.sql.sources.default" will be used.
Similar to R read.csv, when `source` is "csv", by default, a value of "NA" will be interpreted as NA.
## Note[](https://spark.apache.org/docs/latest/api/R/reference/read.df.html#note)
read.df since 1.4.0
loadDF since 1.6.0
## See also[](https://spark.apache.org/docs/latest/api/R/reference/read.df.html#see-also)
[read.json](https://spark.apache.org/docs/latest/api/R/reference/read.json.html)
## Examples[](https://spark.apache.org/docs/latest/api/R/reference/read.df.html#ref-examples)

```
if (FALSE) {
sparkR.session[](https://spark.apache.org/docs/latest/api/R/reference/sparkR.session.html)()
df1 <- read.df("path/to/file.json", source = "json")
schema <- structType[](https://spark.apache.org/docs/latest/api/R/reference/structType.html)(structField[](https://spark.apache.org/docs/latest/api/R/reference/structField.html)("name", "string"),
                     structField[](https://spark.apache.org/docs/latest/api/R/reference/structField.html)("info", "map<string,double>"))
df2 <- read.df(mapTypeJsonPath, "json", schema, multiLine = TRUE)
df3 <- loadDF("data/test_table", "parquet", mergeSchema = "true")
stringSchema <- "name STRING, info MAP<STRING, DOUBLE>"
df4 <- read.df(mapTypeJsonPath, "json", stringSchema, multiLine = TRUE)
}

```

## On this page
Developed by [ The Apache Software Foundation](https://www.apache.org/).
Site built with [pkgdown](https://pkgdown.r-lib.org/) 2.0.1.
Using [preferably](https://preferably.amirmasoudabdol.name/?source=footer) template.
