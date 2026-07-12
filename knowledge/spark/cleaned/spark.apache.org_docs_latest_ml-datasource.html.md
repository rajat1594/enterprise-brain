[ ![](https://spark.apache.org/images/spark-logo-rev.svg)](https://spark.apache.org/docs/latest/index.html)4.1.2
  * [Overview](https://spark.apache.org/docs/latest/index.html)
  * [Programming Guides](https://spark.apache.org/docs/latest/ml-datasource.html)
[Quick Start](https://spark.apache.org/docs/latest/quick-start.html) [RDDs, Accumulators, Broadcasts Vars](https://spark.apache.org/docs/latest/rdd-programming-guide.html) [SQL, DataFrames, and Datasets](https://spark.apache.org/docs/latest/sql-programming-guide.html) [Structured Streaming](https://spark.apache.org/docs/latest/streaming/index.html) [Spark Streaming (DStreams)](https://spark.apache.org/docs/latest/streaming-programming-guide.html) [MLlib (Machine Learning)](https://spark.apache.org/docs/latest/ml-guide.html) [GraphX (Graph Processing)](https://spark.apache.org/docs/latest/graphx-programming-guide.html) [SparkR (R on Spark)](https://spark.apache.org/docs/latest/sparkr.html) [PySpark (Python on Spark)](https://spark.apache.org/docs/latest/api/python/getting_started/index.html) [Declarative Pipelines](https://spark.apache.org/docs/latest/declarative-pipelines-programming-guide.html)
  * [API Docs](https://spark.apache.org/docs/latest/ml-datasource.html)
[Python](https://spark.apache.org/docs/latest/api/python/index.html) [Scala](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html) [Java](https://spark.apache.org/docs/latest/api/java/index.html) [R](https://spark.apache.org/docs/latest/api/R/index.html) [SQL, Built-in Functions](https://spark.apache.org/docs/latest/api/sql/index.html)
  * [Deploying](https://spark.apache.org/docs/latest/ml-datasource.html)
[Overview](https://spark.apache.org/docs/latest/cluster-overview.html) [Submitting Applications](https://spark.apache.org/docs/latest/submitting-applications.html) [Spark Standalone](https://spark.apache.org/docs/latest/spark-standalone.html) [YARN](https://spark.apache.org/docs/latest/running-on-yarn.html) [Kubernetes](https://spark.apache.org/docs/latest/running-on-kubernetes.html)
  * [More](https://spark.apache.org/docs/latest/ml-datasource.html)
[Configuration](https://spark.apache.org/docs/latest/configuration.html) [Monitoring](https://spark.apache.org/docs/latest/monitoring.html) [Tuning Guide](https://spark.apache.org/docs/latest/tuning.html) [Job Scheduling](https://spark.apache.org/docs/latest/job-scheduling.html) [Security](https://spark.apache.org/docs/latest/security.html) [Hardware Provisioning](https://spark.apache.org/docs/latest/hardware-provisioning.html) [Migration Guide](https://spark.apache.org/docs/latest/migration-guide.html) [Building Spark](https://spark.apache.org/docs/latest/building-spark.html) [Contributing to Spark](https://spark.apache.org/contributing.html) [Third Party Projects](https://spark.apache.org/third-party-projects.html)
  *

###  [MLlib: Main Guide](https://spark.apache.org/docs/latest/ml-guide.html)[](https://spark.apache.org/docs/latest/ml-datasource.html#mllib-main-guide)
  * [ Basic statistics ](https://spark.apache.org/docs/latest/ml-statistics.html)
  * [ Data sources ](https://spark.apache.org/docs/latest/ml-datasource.html)
  * [ Pipelines ](https://spark.apache.org/docs/latest/ml-pipeline.html)
  * [ Extracting, transforming and selecting features ](https://spark.apache.org/docs/latest/ml-features.html)
  * [ Classification and Regression ](https://spark.apache.org/docs/latest/ml-classification-regression.html)
  * [ Clustering ](https://spark.apache.org/docs/latest/ml-clustering.html)
  * [ Collaborative filtering ](https://spark.apache.org/docs/latest/ml-collaborative-filtering.html)
  * [ Frequent Pattern Mining ](https://spark.apache.org/docs/latest/ml-frequent-pattern-mining.html)
  * [ Model selection and tuning ](https://spark.apache.org/docs/latest/ml-tuning.html)
  * [ Advanced topics ](https://spark.apache.org/docs/latest/ml-advanced.html)

###  [MLlib: RDD-based API Guide](https://spark.apache.org/docs/latest/mllib-guide.html)[](https://spark.apache.org/docs/latest/ml-datasource.html#mllib-rdd-based-api-guide)
  * [ Data types ](https://spark.apache.org/docs/latest/mllib-data-types.html)
  * [ Basic statistics ](https://spark.apache.org/docs/latest/mllib-statistics.html)
  * [ Classification and regression ](https://spark.apache.org/docs/latest/mllib-classification-regression.html)
  * [ Collaborative filtering ](https://spark.apache.org/docs/latest/mllib-collaborative-filtering.html)
  * [ Clustering ](https://spark.apache.org/docs/latest/mllib-clustering.html)
  * [ Dimensionality reduction ](https://spark.apache.org/docs/latest/mllib-dimensionality-reduction.html)
  * [ Feature extraction and transformation ](https://spark.apache.org/docs/latest/mllib-feature-extraction.html)
  * [ Frequent pattern mining ](https://spark.apache.org/docs/latest/mllib-frequent-pattern-mining.html)
  * [ Evaluation metrics ](https://spark.apache.org/docs/latest/mllib-evaluation-metrics.html)
  * [ PMML model export ](https://spark.apache.org/docs/latest/mllib-pmml-model-export.html)
  * [ Optimization (developer) ](https://spark.apache.org/docs/latest/mllib-optimization.html)

# Data sources[](https://spark.apache.org/docs/latest/ml-datasource.html#data-sources)
In this section, we introduce how to use data source in ML to load data. Besides some general data sources such as Parquet, CSV, JSON and JDBC, we also provide some specific data sources for ML.
**Table of Contents**
  * [Image data source](https://spark.apache.org/docs/latest/ml-datasource.html#image-data-source)
  * [LIBSVM data source](https://spark.apache.org/docs/latest/ml-datasource.html#libsvm-data-source)

## Image data source[](https://spark.apache.org/docs/latest/ml-datasource.html#image-data-source)
This image data source is used to load image files from a directory, it can load compressed image (jpeg, png, etc.) into raw image representation via `ImageIO` in Java library. The loaded DataFrame has one `StructType` column: “image”, containing image data stored as image schema. The schema of the `image` column is:
  * origin: `StringType` (represents the file path of the image)
  * height: `IntegerType` (height of the image)
  * width: `IntegerType` (width of the image)
  * nChannels: `IntegerType` (number of image channels)
  * mode: `IntegerType` (OpenCV-compatible type)
  * data: `BinaryType` (Image bytes in OpenCV-compatible order: row-wise BGR in most cases)

  * **Python**
  * **Scala**
  * **Java**
  * **R**

In PySpark we provide Spark SQL data source API for loading image data as a DataFrame.

```
>>> df = spark.read.format("image").option("dropInvalid", True).load("data/mllib/images/origin/kittens")
>>> df.select("image.origin", "image.width", "image.height").show(truncate=False)
+-----------------------------------------------------------------------+-----+------+
|origin                                                                 |width|height|
+-----------------------------------------------------------------------+-----+------+
|file:///spark/data/mllib/images/origin/kittens/54893.jpg               |300  |311   |
|file:///spark/data/mllib/images/origin/kittens/DP802813.jpg            |199  |313   |
|file:///spark/data/mllib/images/origin/kittens/29.5.a_b_EGDP022204.jpg |300  |200   |
|file:///spark/data/mllib/images/origin/kittens/DP153539.jpg            |300  |296   |
+-----------------------------------------------------------------------+-----+------+
```

[`ImageDataSource`](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/source/image/ImageDataSource.html) implements a Spark SQL data source API for loading image data as a DataFrame.

```
scala> val df = spark.read.format("image").option("dropInvalid", true).load("data/mllib/images/origin/kittens")
df: org.apache.spark.sql.DataFrame = [image: struct<origin: string, height: int ... 4 more fields>]

scala> df.select("image.origin", "image.width", "image.height").show(truncate=false)
+-----------------------------------------------------------------------+-----+------+
|origin                                                                 |width|height|
+-----------------------------------------------------------------------+-----+------+
|file:///spark/data/mllib/images/origin/kittens/54893.jpg               |300  |311   |
|file:///spark/data/mllib/images/origin/kittens/DP802813.jpg            |199  |313   |
|file:///spark/data/mllib/images/origin/kittens/29.5.a_b_EGDP022204.jpg |300  |200   |
|file:///spark/data/mllib/images/origin/kittens/DP153539.jpg            |300  |296   |
+-----------------------------------------------------------------------+-----+------+
```

[`ImageDataSource`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/source/image/ImageDataSource.html) implements Spark SQL data source API for loading image data as a DataFrame.

```
Dataset<Row> imagesDF = spark.read().format("image").option("dropInvalid", true).load("data/mllib/images/origin/kittens");
imageDF.select("image.origin", "image.width", "image.height").show(false);
/*
Will output:
+-----------------------------------------------------------------------+-----+------+
|origin                                                                 |width|height|
+-----------------------------------------------------------------------+-----+------+
|file:///spark/data/mllib/images/origin/kittens/54893.jpg               |300  |311   |
|file:///spark/data/mllib/images/origin/kittens/DP802813.jpg            |199  |313   |
|file:///spark/data/mllib/images/origin/kittens/29.5.a_b_EGDP022204.jpg |300  |200   |
|file:///spark/data/mllib/images/origin/kittens/DP153539.jpg            |300  |296   |
+-----------------------------------------------------------------------+-----+------+
*/
```

In SparkR we provide Spark SQL data source API for loading image data as a DataFrame.

```
> df = read.df("data/mllib/images/origin/kittens", "image")
> head(select(df, df$image.origin, df$image.width, df$image.height))

1               file:///spark/data/mllib/images/origin/kittens/54893.jpg
2            file:///spark/data/mllib/images/origin/kittens/DP802813.jpg
3 file:///spark/data/mllib/images/origin/kittens/29.5.a_b_EGDP022204.jpg
4            file:///spark/data/mllib/images/origin/kittens/DP153539.jpg
  width height
1   300    311
2   199    313
3   300    200
4   300    296
```

## LIBSVM data source[](https://spark.apache.org/docs/latest/ml-datasource.html#libsvm-data-source)
This `LIBSVM` data source is used to load ‘libsvm’ type files from a directory. The loaded DataFrame has two columns: label containing labels stored as doubles and features containing feature vectors stored as Vectors. The schemas of the columns are:
  * label: `DoubleType` (represents the instance label)
  * features: `VectorUDT` (represents the feature vector)

  * **Python**
  * **Scala**
  * **Java**
  * **R**

In PySpark we provide Spark SQL data source API for loading `LIBSVM` data as a DataFrame.

```
>>> df = spark.read.format("libsvm").option("numFeatures", "780").load("data/mllib/sample_libsvm_data.txt")
>>> df.show(10)
+-----+--------------------+
|label|            features|
+-----+--------------------+
|  0.0|(780,[127,128,129...|
|  1.0|(780,[158,159,160...|
|  1.0|(780,[124,125,126...|
|  1.0|(780,[152,153,154...|
|  1.0|(780,[151,152,153...|
|  0.0|(780,[129,130,131...|
|  1.0|(780,[158,159,160...|
|  1.0|(780,[99,100,101,...|
|  0.0|(780,[154,155,156...|
|  0.0|(780,[127,128,129...|
+-----+--------------------+
only showing top 10 rows
```

[`LibSVMDataSource`](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/source/libsvm/LibSVMDataSource.html) implements a Spark SQL data source API for loading `LIBSVM` data as a DataFrame.

```
scala> val df = spark.read.format("libsvm").option("numFeatures", "780").load("data/mllib/sample_libsvm_data.txt")
df: org.apache.spark.sql.DataFrame = [label: double, features: vector]

scala> df.show(10)
+-----+--------------------+
|label|            features|
+-----+--------------------+
|  0.0|(780,[127,128,129...|
|  1.0|(780,[158,159,160...|
|  1.0|(780,[124,125,126...|
|  1.0|(780,[152,153,154...|
|  1.0|(780,[151,152,153...|
|  0.0|(780,[129,130,131...|
|  1.0|(780,[158,159,160...|
|  1.0|(780,[99,100,101,...|
|  0.0|(780,[154,155,156...|
|  0.0|(780,[127,128,129...|
+-----+--------------------+
only showing top 10 rows
```

[`LibSVMDataSource`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/source/libsvm/LibSVMDataSource.html) implements Spark SQL data source API for loading `LIBSVM` data as a DataFrame.

```
Dataset<Row> df = spark.read.format("libsvm").option("numFeatures", "780").load("data/mllib/sample_libsvm_data.txt");
df.show(10);
/*
Will output:
+-----+--------------------+
|label|            features|
+-----+--------------------+
|  0.0|(780,[127,128,129...|
|  1.0|(780,[158,159,160...|
|  1.0|(780,[124,125,126...|
|  1.0|(780,[152,153,154...|
|  1.0|(780,[151,152,153...|
|  0.0|(780,[129,130,131...|
|  1.0|(780,[158,159,160...|
|  1.0|(780,[99,100,101,...|
|  0.0|(780,[154,155,156...|
|  0.0|(780,[127,128,129...|
+-----+--------------------+
only showing top 10 rows
*/
```

In SparkR we provide Spark SQL data source API for loading `LIBSVM` data as a DataFrame.

```
> df = read.df("data/mllib/sample_libsvm_data.txt", "libsvm")
> head(select(df, df$label, df$features), 10)

   label                      features
1      0 <environment: 0x7fe6d35366e8>
2      1 <environment: 0x7fe6d353bf78>
3      1 <environment: 0x7fe6d3541840>
4      1 <environment: 0x7fe6d3545108>
5      1 <environment: 0x7fe6d354c8e0>
6      0 <environment: 0x7fe6d35501a8>
7      1 <environment: 0x7fe6d3555a70>
8      1 <environment: 0x7fe6d3559338>
9      0 <environment: 0x7fe6d355cc00>
10     0 <environment: 0x7fe6d35643d8>
```
